#!/usr/bin/python3
""" Generates a .tgz archive from the contents of the web_static folder
    in AirBnB Clone repo
"""
from fabric.api import *


def do_pack():
    """ creates the versions folder and it,
        generates the archive
    """
    # create the directory versions if it doesn't exist
    local('mkdir -p versions')
    # generate the archive into the created folder
    archive = local('tar -cvzf versions/web_static_$(date +%Y%m%d%H%M%S).tgz\
            web_static/* web_static')
    if archive.succeeded:
        # get the newly created file and create a path to return
        res = local('ls -1t versions/', capture=True)
        archive_file = res.split('\n')[0]
        return f'versions/{archive_file}'
    else:
        return None
