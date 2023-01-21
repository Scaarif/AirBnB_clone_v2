#!/usr/bin/python3
""" Based on the module '3-deploy_web_static',
    deletes out-of-date archives using the function do_clean
"""
import os
from fabric.api import *


env.user = 'ubuntu'
env.hosts = ['54.82.173.163', '18.210.20.118']


def do_clean(number=0):
    """ deletes 'archives - number' archives in
    /data/web_static/releases/ of both servers
    """
    with cd("/data/web_static/releases/"):
        dirs = run('ls -1t | wc -l')
    files = local('ls -1t versions/ | wc -l', capture=True)
    number = int(number)
    # get the number of folders to delete
    if number < 2:
        number = 1
    else:
        # keep upto number(th) most recent archives
        with lcd("versions/"):
            local('rm -f $(ls -1t | tail -n {})'
                  .format(int(files) - number))
        with cd("/data/web_static/releases/"):
            run('sudo rm -rf $(ls -1t | tail -n {})'
                .format(int(files) - number))
