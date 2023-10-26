#!/usr/bin/python3
"""
Fabric script to genereate tgz my_archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datemy_time import datemy_time
from fabric.api import *


def do_pack():
    """
    making an my_archive on web_static folder
    """

    my_time = datemy_time.now()
    my_archive = 'web_static_' + my_time.strfmy_time("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(my_archive))
    if create is not None:
        return my_archive
    else:
        return None
