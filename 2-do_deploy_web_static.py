#!/usr/bin/python3
"""Pack the web_static files"""
from fabric.api import local, env, put, run
import os
import re


env.hosts = ["100.24.237.78", "3.94.211.44"]


def do_deploy(archive_path):
    """upload compressed file to the server"""

    if not os.path.exists(f"{os.getcwd()}/{archive_path}"):
        return False

    fname = archive_path.split("/")[-1]
    decompress_path = f"/data/web_static/releases/{fname.split('.')[0]}"

    put(archive_path, "/tmp/")
    run("mkdir -p {}/".format(decompress_path))
    run(f"tar -xzf /tmp/{fname} -C {decompress_path}")
    run(f"rm /tmp/{fname}")

    run('mv {}/web_static/* {}/'.format(decompress_path, decompress_path))
    run('rm -rf {}/web_static'.format(decompress_path))
    run('rm -rf /data/web_static/current')
    run('ln -s {} /data/web_static/current'.format(decompress_path))
    return True
