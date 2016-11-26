#!/usr/bin/python

import hashlib
import os
from crypt import encrypt_file
import random

#from Crypto.Cipher import AES
from states import State


def dialog(state, **kwargs):
    os.system("clear")
    if state == State.GREETING:
        greeting(**kwargs)
    if state == State.AUTHENTIFICATION: 
        authentification(**kwargs)                    
    elif state == State.REGISTRATION:
        registration(**kwargs)
    elif state == State.UTILIZATION:
        utilization(**kwargs)
    elif state == State.ERROR:
        error(**kwargs)


def greeting(**kwargs):
    if 'msg_to_print' in kwargs:
        print kwargs['msg_to_print']

    command = raw_input("1) Login\n2) Register\n")
    if command == '1':
        dialog(State.AUTHENTIFICATION)
    elif command == '2':
        dialog(State.REGISTRATION)
    else:
        dialog(State.ERROR)

def get_users():
    users = {}
    with open('users') as f:
        for line in f.readlines():
            users[line.split(':')[0]] = line.split(':')[1].rstrip()
    return users

def registration():
    users = get_users()
    username = raw_input("Username: ")
    if users.get(username):
        dialog(State.GREETING, msg_to_print="Such user already exists")
    password = raw_input("Password: ")
    password_repeated = raw_input("Confirm password: ")
    while (password != password_repeated):
        password_repeated = raw_input("Confirm password: ")
    with open('users', 'a') as f:
        f.write("{username}:{password}\n"
         .format(username=username,
             password=hashlib.sha256(password).digest()))
    dialog(State.GREETING, msg_to_print="You have successfully registered\n")


def files(dir_):
    absolute_paths_to_files = []
    for root, dirs, files in os.walk(dir_):
        for name in files:
            absolute_paths_to_files.append(os.path.join(root, name))
    return absolute_paths_to_files


def encrypt_folder(key, folder):
    print "Encrypting {} folder".format(folder)
    for ef in files(folder):
        print "Encrypting {}".format(ef)
        encrypt_file(key, ef)

def authentification(**kwargs):
    if 'msg_to_print' in kwargs:
        print kwargs['msg_to_print']
    users = get_users()

    username = raw_input("Username: ")
    if not username in users:
        dialog(State.AUTHENTIFICATION, msg_to_print="No such user")

    passhash = hashlib.sha256(raw_input("Password: ")).digest()
    if not passhash == users[username]:
        dialog(State.AUTHENTIFICATION, msg_to_print="Wrong password")

    if not os.path.exists(username):
        os.mkdir(username)
    key = passhash
    encrypt_folder(key, username)
    dialog(State.UTILIZATION, msg_to_print="You've logged in", user=username, key=passhash)
  
def utilization(**kwargs):
    #if 'msg_to_print' in kwargs:
    #    print kwargs['msg_to_print']
    a = raw_input("Tap anything to finish session...")
    encrypt_folder(kwargs['key'], kwargs['user'])
    print "You've successfuly loged off"

if __name__ == '__main__':
    dialog(State.GREETING)
