import os
from Crypto.Cipher import AES
import cStringIO 
import random
import struct

def encrypt_file(key, in_filename, chunksize=64*1024):
    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    buffer = cStringIO.StringIO()
    with open(in_filename, 'rb') as infile:
	buffer.write(struct.pack('<Q', filesize))
	buffer.write(iv)

	while True:
	    chunk = infile.read(chunksize)
	    if len(chunk) == 0:
		break
	    elif len(chunk) % 16 != 0:
		chunk += ' ' * (16 - len(chunk) % 16)

	    buffer.write(encryptor.encrypt(chunk))

    with open(in_filename, 'wb') as out:
	out.write(buffer.getvalue())
	buffer.close()


def decrypt_file(key, in_filename, chunksize=24*1024):
    buffer = cStringIO.StringIO()
    with open(in_filename, 'rb') as infile:
	origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
	iv = infile.read(16)
	decryptor = AES.new(key, AES.MODE_CBC, iv)

	while True:
	    chunk = infile.read(chunksize)
	    if len(chunk) == 0:
		break
	    buffer.write(decryptor.decrypt(chunk))
	buffer.truncate(origsize)

    with open(in_filename, 'wb') as out:
	out.write(buffer.getvalue())
	buffer.close()
