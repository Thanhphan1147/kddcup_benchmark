#!/bin/bash
#echo 'export PATH="/home/ubuntu/anaconda3/bin:$PATH"' >> ~/.bashrc
echo 'running as $(whoami), in $(pwd)'
echo 'export PATH="/root/anaconda3/bin:$PATH"' >> ~/.bashrc
echo $PATH

HASH="sha1:b07c86db1a39:696471a7f56df7014738a7da317d83442a010da8"

echo 'conf = get_config()' > config
echo "conf.NotebookApp.ip = '0.0.0.0'" >> config
echo "conf.NotebookApp.password = u'$HASH'" >> config
echo "conf.NotebookApp.port = 9999" >> config

cat config
echo "$CONFIGFILE"

./launch_notebook.sh
