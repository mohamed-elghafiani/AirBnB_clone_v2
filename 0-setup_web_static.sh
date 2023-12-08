#!/usr/bin/env bash
# A script for preparing web servers

# install nginx web server
sudo apt-get -y update && \
sudo apt-get -y install nginx

# creating the folders/files if doesn't exists
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# fake HTML files
echo "
<!DOCTYPE html>
<html>
  <head>
    <title>Fake page!</title>
  </head>
  <body>
    <h3>Hello, from the underworld!!!</3>
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolik link
if [ -d /data/web_static/releases/test/ ]
    sudo rm -r /data/web_static/releases/test/
    sudo ln -s /data/web_static/current /data/web_static/releases/test/
else
    sudo ln -s /data/web_static/current /data/web_static_releases/test/
fi

# change ownerships
sudo find /data -exec sudo chown ubuntu:ubuntu {} +
sudo chown ubuntu:ubuntu /data

# configuring the web server to serve the content of /data/web_static/current/ to hbnb_static
sudo cp /etc/nginx/nginx.conf
echo "http {
    server {
        location /hbnb_static {
            alias /data/web_static/current/
        }
    }
}

events {
}" | sudo tee /etc/nginx/nginx.conf
