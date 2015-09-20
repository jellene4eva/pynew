#!/usr/bin/env python3

import sys
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(argv):
    create_main_dir(argv[1])
    os.chdir(argv[1])
    create_sub_dir(argv[1])
    create_init_file(argv[1])

def create_main_dir(project_name):
    if not os.path.exists(project_name):
        os.mkdir(project_name)
        logger.info('--Created folder ' + project_name)

def create_sub_dir(main_dir):
    folders = [main_dir.lower(), 'bin','tests','docs']
    for folder in folders:
        os.mkdir(folder)
        logger.info('--Created subfolder ' + folder)

def create_init_file(main_dir):
    main_dir = main_dir.lower()
    files = ["README.md", "setup.py", main_dir + "/__init__.py"]
    for filename in files:
        os.mknod(filename)
        logger.info('--Created files ' + filename)

if __name__ == "__main__":
    main(sys.argv)

