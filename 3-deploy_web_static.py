#!/usr/bin/python3
""" Based on the modules '1-pack_web_static' & '2-do_deploy_web_static',
    creates and distributes an archive to your web servers
    (using the function it defines, deploy)
"""
import os
from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack


env.user = 'ubuntu'
env.hosts = ['54.82.173.163', '18.210.20.118']

def do_deploy(archive_path):
    """ distribute an archive to all web servers """
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path[archive_path.find('/') + 1:]
        folder = filename[:filename.find('.')]
        put(archive_path, "/tmp/")
        run(f'mkdir -p data/web_static/releases/{folder}/')
        run(f'tar -xzf /tmp/{filename} -C data/web_static/releases/{folder}/')
        with cd(f"data/web_static/releases/{folder}/"):
            run('mv web_static/* .; rm -rf web_static')
        run(f'rm -f /tmp/{filename}')
        run('rm -f data/web_static/current')
        run(f'ln -s data/web_static/releases/{folder}/ data/web_static/current')
        print('New version deployed!')
        return True
    except Exception:
        return False


def deploy():
    """ calls the do_pack and do_deploy
        functions
    """
    # call the do_pack fn and store the path of the created archive(how?)
    archive_path = do_pack()
    # return false if no archive has been created
    if not archive_path:
        return False
    # call the do_deploy(archive_path) function, using the new path of the new archive
    deployed = do_deploy(archive_path)
    return deployed
