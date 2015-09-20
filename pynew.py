#!/usr/bin/env python3

import sys
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(argv):
    #Create main project folder
    target_dir = str(argv[1])
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
        logger.info('--Created folder ' + target_dir)

    #Create sub project folders
    os.chdir(target_dir)

    folders = [target_dir, 'bin','tests','docs']
    for folder in folders:
        os.mkdir(folder)
        logger.info('--Created subfolder ' + folder)


if __name__ == "__main__":
    main(sys.argv)

