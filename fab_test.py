#!/usr/bin/python3
from fabric.api import put, env

env.hosts = [
        "100.24.237.78"
        ]
env.user = "ubuntu"

def upload(archive_path):
    upload = put(archive_path, "/tmp/")
