#!/usr/bin/python3
"""
Fabric script to generate tgz my_archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """making an my_archive on web_static folder"""

    my_time = datetime.now()
    my_archive = 'web_static_' + my_time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(my_archive))
    if create is not None:
        return my_archive
    else:
        return None
