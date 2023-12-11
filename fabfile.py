#!/usr/bin/python3
"""Pack the web_static files"""
from fabric.api import run
from datetime import datetime


@task
def host_type():
    dt = datetime.now()
    tar_file_name = "web_static_{}{}{}{}{}{}".format(
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second
    )

    print(tar_file_name)

    run('uname -s')
