#!/usr/bin/python3
""" Do deploy """
from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ['54.82.173.163', '18.210.20.118']


def do_deploy(archive_path):
    ''' Distributes an archive to my web servers.
    '''
    if local("ls {}".format(archive_path)).failed:
        return False

    # Upload the archive to the /tmp/ directory of the web server
    op = put(archive_path, '/tmp/')
    if op.failed:
        return False

    # Parse out file name from argument
    filePathList = archive_path.split('/')
    fileName = filePathList[len(filePathList) - 1]
    fileNameNoExt = fileName.split('.')[0]

    # Create required directory if not exists
    op = run("mkdir -p /data/web_static/releases/{}".format(fileNameNoExt))
    if op.failed:
        return False

    # Unpack archive to required directory
    op = run(
            "tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
                fileName, fileNameNoExt))
    if op.failed:
        return False

    # Delete the archive from the server
    op = run("rm -rf /tmp/{}".format(fileName))
    if op.failed:
        return False

    # Move contents of archive to right directory
    op = run(
            "cp -r /data/web_static/releases/{}/web_static/*\
                    /data/web_static/releases/{}/".format(
                fileNameNoExt, fileNameNoExt))
    if op.failed:
        return False

    # Delete redundant web_static folder
    op = run(
            "rm -rf /data/web_static/releases/{}/web_static".format(
                fileNameNoExt))
    if op.failed:
        return False

    # Ensure the directories and files have the right permissions to avoid 403
    op = sudo("chmod -R 755 /data/web_static/")
    if op.failed:
        return False

    # Delete the symbolic link `current`
    op = run("rm -rf /data/web_static/current")
    if op.failed:
        return False

    # Create new symbolic link
    op = run(
            "ln -s -T /data/web_static/releases/{}/\
                    /data/web_static/current".format(fileNameNoExt))
    if op.failed:
        return False

    return True
