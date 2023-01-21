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
    # create the directory 'versions' if it doesn't exist
    if not os.path.isdir('versions'):
        if local('mkdir -p versions').failed:
            return None
    # generate the archive into the created folder
    now = datetime.now()
    now_fstr = now.strftime("%Y%m%d%H%M%S")
    sources = 'web_static'
    archive_path = f'versions/web_static_{now_fstr}.tgz'
    print(f'Packing web_static to {archive_path}')
    if local(f'tar -cvzf {archive_path} {sources}').failed:
        return None
    # get the newly created file and create a path to return
    size = os.path.getsize(archive_path)
    print(f'web_static packed: {archive_path} -> {size}Bytes')
    return archive_path
