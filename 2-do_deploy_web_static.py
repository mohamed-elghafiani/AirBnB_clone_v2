#!/usr/bin/python3
"""Pack the web_static files"""
from fabric.api import local, task, env
import os
import re


env.hosts = ["100.24.237.78", "3.94.211.44"]


@task
def do_deploy(archive_path):
    """upload compressed file to the server"""

    if not os.path.exists(f"{os.getcwd()}/{archive_path}"):
        print("False: Not found")
        return False
    
    name_tar_file = archive_path.split("/")[1]
    put(archive_path, "/tmp/")
    decompress_path = f"/data/web_static/releases/{name_tar_file.split(".")[0]}/"
    run(f"mkdir -p {decompress_path}")
    run(f"tar -xf /tmp/{name_tar_file} -C {decompress_path}")
    run(f"rm /tmp/{name_tar_file}")
    run(f"rm -r /data/web_static/current")
    run(f"ln -s {decompress_path} /data/web_static/current")
    print("Website depolyed successfuly")
    return True
