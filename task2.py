#!/usr/bin/python

import os
import sys


def read_starting_with(position, from_):
  from_.read(position-1)
  return from_.read(32)

def signature(path):
  with open(path) as f:
     return read_starting_with(position=64, from_=f)

def files(dir_):
  absolute_paths_to_files = []
  for root, dirs, files in os.walk(dir_):
    for name in files:
      absolute_paths_to_files.append(os.path.join(root, name))
  return absolute_paths_to_files


if __name__ == '__main__':
  
  path_to_file = sys.argv[1]
  path_to_dir = sys.argv[2]

  given_signature = signature(path_to_file)

  for f in files(path_to_dir):
    print "{} {}".format('\033[92m[TRUE]\033[0m'
                             if signature(f) == given_signature else
                         '\033[91m[FALSE]\033[0m', f)
