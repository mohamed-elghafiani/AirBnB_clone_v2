#!/usr/bin/env bash
# a script for  preparing a web server

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

#Give user/group permission to ubuntu
sudo chown -R ubuntu:ubuntu /data/
sudo chgrp -R ubuntu /data/

#Update the Nginx configuration to serve the content
df_path="/etc/nginx/sites-available/default"
new_loc="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "/^\tserver_name _;/a\\$new_loc" $df_path

# Starting the server
sudo service nginx start
