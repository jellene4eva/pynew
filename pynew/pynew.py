#!/usr/bin/env python3

import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Pynew():

    def create_main_dir(project_name):
        if not os.path.exists(project_name):
            os.mkdir(project_name)
            logger.info('--Created folder ' + project_name)

    def create_sub_dir(main_dir):
        main_dir = main_dir.lower()
        folders = [
            main_dir,
            'bin',
            main_dir + '/test',
            'docs'
        ]
        for folder in folders:
            os.mkdir(folder)
            logger.info('--Created subfolder ' + folder)

    def create_init_file(main_dir):
        main_dir = main_dir.lower()
        folders = [
            main_dir,
            main_dir + '/test'
        ]
        for folder in folders:
            os.mknod(folder + "/__init__.py")
            logger.info('--Created files ' + folder + "/__init__.py")

    def seed_init_file(main_dir):
        main_dir = main_dir.lower()
        pass

