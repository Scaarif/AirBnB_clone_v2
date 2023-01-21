#!/usr/bin/python3
""" Based on the module '1-pack_web_static', distributes an archive
    to your web servers (using the function it defines, do_deploy
"""
from fabric.api import *
import os


# set the user to use for ssh
env.user = 'ubuntu'
# set the hosts/servers to be involved
env.hosts = ['54.82.173.163', '18.210.20.118']

# the fn wil then be run on both hosts (one after the other)


def do_deploy(archive_path):
    """ distributes an archive (in archive_path)
    to all web_servers
    Note: returns False if archive doesn't exist
    """
    # check that archive (archive_path) exists
    filename = archive_path[archive_path.find('/') + 1:]
    root = '/data/web_static/releases/'
    if not os.path.exists(archive_path):
        return False
    try:
        # upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        folder = filename[:filename.find('.')]
        archive = root + folder
        # create the folder (to hold the archive)
        run('mkdir -p {}/'.format(archive))
        # extract the files/archive in created folder
        run('tar -xzf /tmp/{} -C {}/'.format(filename, archive))
        run('mv {}/web_static/* {}/'.format(archive, archive))
        run('rm -rf {}/web_static'.format(archive))
        # delete the archive from the web server
        run('rm -f /tmp/{}'.format(filename))
        # delete the symbolic link /data/web_static/current on the web server
        run('rm -f /data/web_static/current')
        # create a new symbolic link /data/web_static/current
        run('ln -s {}/ {}current'.fomat(archive, root))
        # return True if all operations are correctly done, else return False
        print('New version deployed!')
        return True
    except Exception:
        return False
