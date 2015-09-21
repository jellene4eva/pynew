#!/usr/bin/env python3

import os
import logging
import stat
import shutil

logger = logging.getLogger(__name__)

class Pynew():

    def create_main_dir(project_name):
        if not os.path.exists(project_name):
            os.mkdir(project_name)
            logger.info('--Created folder ' + project_name)

    def create_sub_dir(main_dir):
        main_dir = main_dir.lower()
        folders = (
            main_dir,
            'bin',
            main_dir + '/test',
            'docs'
        )
        for folder in folders:
            os.mkdir(folder)
            logger.info('--Created subfolder ' + folder)

    def create_init_file(main_dir):
        main_dir = main_dir.lower()
        folders = (
            main_dir,
            main_dir + '/test'
        )
        for folder in folders:
            os.mknod(folder + "/__init__.py")
            logger.info('--Created file ' + folder + "/__init__.py")

    def seed_file(main_dir):
        main_dir = main_dir.lower()
        current_path = os.getcwd()

        setup_destination = '/'.join([current_path, "setup.py"])
        main_destination = '/'.join([current_path, main_dir, "main.py"])

        origin = os.path.dirname(os.path.abspath(__file__))
        setup_path = '/'.join([origin, "example_setup.py"])
        main_path = '/'.join([origin, "example_main.py"])

        shutil.copyfile(setup_path, setup_destination)
        logger.info('--Created file ' + setup_destination)

        shutil.copyfile(main_path, main_destination)
        logger.info('--Created file ' + main_destination)

    def create_symlink_file(main_dir):
        main_dir = main_dir.lower()

        current_path = os.getcwd()

        main_destination = '/'.join([current_path, main_dir, "main.py"])
        bin_destination = '/'.join([current_path, "bin", main_dir])

        os.symlink(main_destination, bin_destination)
        logger.info('--Linked file ' + bin_destination)

        #Make symlink file executable
        st = os.stat(bin_destination)
        os.chmod(bin_destination, st.st_mode | stat.S_IEXEC)
