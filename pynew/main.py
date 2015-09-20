#!/usr/bin/env python3

import sys
import os
import logging
from pynew import Pynew

def main(argv):
    Pynew.create_main_dir(argv[1])
    os.chdir(argv[1])
    Pynew.create_sub_dir(argv[1])
    Pynew.create_init_file(argv[1])
    Pynew.seed_init_file(argv[1])

if __name__ == "__main__":
    main(sys.argv)

