#!/usr/bin/python3
""" Generates a .tgz archive from the contents of the web_static folder
    in AirBnB Clone repo
"""
import os
from fabric.api import *
from datetime import datetime


def do_pack():
    """ creates the versions folder and it,
        generates the archive
    """
    try:
        # create the directory 'versions' if it doesn't exist
        local('mkdir -p versions')
        # generate the archive into the created folder
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = 'versions/web_static_{}.tgz'.format(now)
        # print(f'Packing web_static to {archive_path}')
        local('tar -cvzf {} web_static/'.format(archive_path))
        # print(f'web_static packed: {archive_path} -> {size}Bytes')
        return archive_path
    except Exception:
        return None
