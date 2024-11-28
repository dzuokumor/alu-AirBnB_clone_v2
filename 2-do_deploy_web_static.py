#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric import Connection
from os.path import exists
from invoke import UnexpectedExit

# Update the host IP addresses here
env_hosts = ['34.229.14.248', '3.80.109.32']

def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"

        for host in env_hosts:
            conn = Connection(host)

            # Upload the archive
            conn.put(archive_path, '/tmp/')

            # Create directory and extract the archive
            conn.run(f'mkdir -p {path}{no_ext}/')
            conn.run(f'tar -xzf /tmp/{file_n} -C {path}{no_ext}/')

            # Remove the temporary archive
            conn.run(f'rm /tmp/{file_n}')

            # Move the contents and clean up
            conn.run(f'mv {path}{no_ext}/web_static/* {path}{no_ext}/')
            conn.run(f'rm -rf {path}{no_ext}/web_static')
            conn.run(f'rm -rf /data/web_static/current')
            conn.run(f'ln -s {path}{no_ext}/ /data/web_static/current')

        return True
    except UnexpectedExit as e:
        print(f"Error during deployment: {e}")
        return False

