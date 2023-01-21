#!/usr/bin/python3
""" Based on the modules '1-pack_web_static' & '2-do_deploy_web_static',
    creates and distributes an archive to your web servers
    (using the function it defines, deploy)
"""
import os
from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """ calls the do_pack and do_deploy
        functions
    """
    # call the do_pack fn and store the path of the created archive(how?)
    archive_path = do_pack()
    # return false if no archive has been created
    if not archive_path:
        return False
    # call the do_deploy(archive_path) function, using the new path
    return do_deploy(archive_path)
