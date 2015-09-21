#!/usr/bin/env python3

import sys
import os
import logging
from pynew import Pynew

logging.basicConfig(level=logging.INFO)

def main(argv):
    project = argv[1]

    Pynew.create_main_dir(project)
    os.chdir(project)
    Pynew.create_sub_dir(project)
    Pynew.create_init_file(project)
    Pynew.seed_file(project)
    Pynew.create_symlink_file(project)

if __name__ == "__main__":
    main(sys.argv)

