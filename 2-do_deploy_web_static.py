#!/usr/bin/python3
""" Function that compress a folder """
from datetime import datetime
from fabric.api import *
import os


env.hosts = ['54.82.173.163', '18.210.20.118']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploys """
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path[archive_path.find('/') + 1:]
        folder = filename[:filename.find('.')]
        archive_path = "/data/web_static/releases/{}/".format(folder)
        tmp_path = "/tmp/{}".format(filename)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(archive_path))
        run("tar -xzf {} -C {}".format(tmp_path, archive_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(archive_path, archive_path))
        run("rm -rf {}web_static".format(archive_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(archive_path))
        print("New version deployed!")
        return True
    except Exception:
        return False
