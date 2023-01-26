#!/usr/bin/python3
""" Prepare web servers for web_static deployment """
from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ['54.82.173.163', '18.210.20.118']


def do_deploy(archive_path):
    """
        distributes the archive
    """
    # check that archive_path exists and return False if it doesn't
    if os.path.exists(archive_path):
        # derive file and folder names from archive name
        filename = archive_path[9:]
        archive_folder = "/data/web_static/releases/" + filename[:-4]
        tmp_archive = "/tmp/" + filename
        # upload archive
        put(archive_path, "/tmp/")
        # create necessary repo unzip archive into it
        run("sudo mkdir -p {}".format(archive_folder))
        run("sudo tar -xzf {} -C {}/".format(tmp_archive,
                                             archive_folder))
        # delete archive file
        run("sudo rm {}".format(tmp_archive))
        # move unzipped files to correct folder and delete web_static
        run("sudo mv {}/web_static/* {}".format(archive_folder,
                                                archive_folder))
        run("sudo rm -rf {}/web_static".format(archive_folder))
        # delete current sym link and craete a new one
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(archive_folder))

        print("New version deployed!")
        return True
    else:
        return False
