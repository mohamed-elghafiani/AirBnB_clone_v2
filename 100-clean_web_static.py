#!/usr/bin/python3
from fabric.api import run, local, env
import os
import re

env.hosts = ["100.24.237.78", "3.94.211.44"]


def do_clean(number=0):
    """Clean outdated versions"""
    versions = os.listdir("versions/")
    versions_dated = {}
    for version in versions:
        date = re.findall("web_static_([0-9]+).+", version)[0]
        versions_dated[int(date)] = version

    if number == 0 or number == 1:
        for vdate in sorted(versions_dated)[:-1]:
            local("rm versions/{}".format(versions_dated[vdate]))
            run(f"rm -rf /data/web_static/releases/web_static_{vdate}/*")
    else:
        for vdate in sorted(versions_dated)[:-number]:
            local("rm versions/{}".format(versions_dated[vdate]))
            run(f"rm -rf /data/web_static/releases/web_static_{vdate}/*")
