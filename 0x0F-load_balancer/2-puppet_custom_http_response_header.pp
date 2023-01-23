# as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
exec {'install':
      provider => shell,
      command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default ; sudo sed -i "s/listen \[::\]:80 default_server;/listen \[::\]:80 default_server;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
