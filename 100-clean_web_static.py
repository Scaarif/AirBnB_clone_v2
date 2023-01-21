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
        # delete from versions as well
        if int(files) > 1:
            with lcd("versions/"):
                local(f'rm -f $(ls -1t | tail -n {int(files) - 1})')
        # keep only the most recent version of your archive
        if int(dirs) > 1:
            with cd("/data/web_static/releases/"):
                run(f'rm -rf $(ls -1t | tail -n {int(dirs) -1})')
    else:
        # keep upto nth most recent archives
        if int(files) > number:
            with lcd("versions/"):
                local(f'rm -f $(ls -1t | tail -n {int(files) - number})')
        if int(dirs) > number:
            with cd("/data/web_static/releases/"):
                run(f'rm -rf $(ls -1t | tail -n {int(dirs) - number})')
