#!/usr/bin/python3
from fabric.api import env, task

do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy

env.hosts = ["100.24.237.78", "3.94.211.44"]


@task
def deploy():
    """Fully deploy site to remote servers"""
    archive_path = do_pack()
    if archive_path:
        do_deploy(archive_path)
