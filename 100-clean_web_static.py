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
    number = int(number)
    root = '/data/web_static/releases/'
    # get the number of folders to delete
    if number < 1:
        number = 2
    else:
        number += 1
    # keep upto number(th) most recent archives
    local('cd versions ; rm -rf $(ls -t | tail -n +{})'
          .format(number))
    run('cd {} ; rm -rf $(ls -t | tail -n +{})'
        .format(root, number))
