#!/usr/bin/python3
"""Script that creates and distributes an archive
to your web servers"""
from fabric.api import *
from datetime import datetime
from os.path import exists, splitext


env.hosts = ['54.87.180.223', '52.23.245.155', 'localhost']


@task
def do_pack():
    """Function that archive web_static folder """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(date)
    print("Packing web_static to {}".format(path))
    if local('{} && tar -cvzf {} web_static'.format(mkdir, path)).succeeded:
        return path
        print("web_static packed: {} -> {}Bytes".format(path, size))
    return None


@task
def do_deploy(archive_path):
    """ Function that deply archive"""

    # Checking if path exists
    if not exists(archive_path):
        return False
    # Spliting the files
    arch_name = archive_path.split('/')[1]
    file_name = splitext(arch_name)[0]
    tmp_path = "/tmp/{}".format(arch_name)
    data_path = "/data/web_static/releases/{}".format(file_name)
    # Fabric commands
    put(archive_path, '/tmp/')
    run('mkdir -p {}'.format(data_path))
    run('tar -xzf {}  -C {}'.format(tmp_path, data_path))
    run('rm {}'.format(tmp_path))
    run('mv {}/web_static/* {}/'.format(data_path, data_path))
    run('rm -rf {}/web_static'.format(data_path))
    run('rm -rf /data/web_static/current')
    run('ln -s {} /data/web_static/current'.format(data_path))
    print("New version deployed!")
    return True


@task
def deploy():
    """Function that creates and distributes an archive
    to your web servers"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
