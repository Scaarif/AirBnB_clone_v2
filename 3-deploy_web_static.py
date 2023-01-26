#!/usr/bin/python3
""" Based on the modules '1-pack_web_static' & '2-do_deploy_web_static',
    creates and distributes an archive to your web servers
    (using the function it defines, deploy)
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


env.user = 'ubuntu'
env.hosts = ['54.82.173.163', '18.210.20.118']


def do_deploy(archive_path):
    """
        Distributes the archive
    """
    if os.path.exists(archive_path):
        filename = archive_path[9:]
        archive_folder = "/data/web_static/releases/" + filename[:-4]
        tmp_archive = "/tmp/" + filename
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(archive_folder))
        run("sudo tar -xzf {} -C {}/".format(tmp_archive,
                                             archive_folder))
        run("sudo rm {}".format(tmp_archive))
        run("sudo mv {}/web_static/* {}".format(archive_folder,
                                                archive_folder))
        run("sudo rm -rf {}/web_static".format(archive_folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(archive_folder))

        print("New version deployed!")
        return True
    else:
        return False


def deploy():
    """ calls the do_pack and do_deploy
        functions
    """
    # call the do_pack fn and store the path of the created archive(how?)
    deploy.set = getattr(deploy, 'set', 0) + 1
    # only store archive_path if its not been set (i.e. make it static)
    if deploy.set == 1:
        deploy.archive_path = do_pack()
    # return false if no archive has been created
    if not deploy.archive_path:
        return False
    # call the do_deploy(archive_path) function, using the returned path
    return do_deploy(deploy.archive_path)
