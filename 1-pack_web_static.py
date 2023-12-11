#!/usr/bin/python3
"""Pack the web_static files"""
from fabric.api import local, task
from datetime import datetime


@task
def do_pack():
    """Packing the web_static files"""
    dt = datetime.now()
    tar_file_name = "web_static_{}{}{}{}{}{}".format(
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second
    )
    local('mkdir -p versions')
    if local(f'tar -czvf versions/{tar_file_name}.tgz web_static/').succeeded:
        return f"versions/{tar_file_name}.tgz"
    else:
        return None
