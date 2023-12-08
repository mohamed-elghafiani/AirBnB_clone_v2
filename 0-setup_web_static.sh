#!/usr/bin/env bash

# creating the folders/files if doesn't exists
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# fake HTML files
sudo touch /data/web_static/releases/test/index.html
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
if [ -d /data/web_static/current ]
then
    sudo rm -r /data/web_static/current
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
else
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi

# change ownerships
sudo find /data -type f,d -exec sudo chown ubuntu:ubuntu {} +
sudo chown ubuntu:ubuntu /data

# configuring the web server to serve the content of /data/web_static/current/ to hbnb_static
sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.old
echo "http {
    server {
        location /hbnb_static {
            alias /data/web_static/current/
        }
    }
}

events {
}" | sudo tee /etc/nginx/nginx.conf

# Starting the server
sudo service nginx start
