#!/usr/bin/python3
"""Pack the web_static files"""
from fabric.api import local, task, env, put
import os
import re


env.hosts = ["100.24.237.78", "3.94.211.44"]


@task
def do_deploy(archive_path):
    """upload compressed file to the server"""

    if not os.path.exists(f"{os.getcwd()}/{archive_path}"):
        return False
    
    try:
        name_tar_file = archive_path.split("/")[-1]
        put(archive_path, "/tmp/")
        decompress_path = f"/data/web_static/releases/{name_tar_file.split('.')[0]}/"
        run(f"mkdir -p {decompress_path}")
        run(f"tar -xzf /tmp/{name_tar_file} -C {decompress_path}")
        run(f"rm /tmp/{name_tar_file}")

        run('mv {}/web_static/* {}/'.format(data_path, data_path))
        run('rm -rf {}/web_static'.format(data_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(data_path))
        return True
    except:
        return False
