#!/bin/bash
# echo 'export PATH="/home/ubuntu/anaconda3/bin:$PATH"' >> ~/.bashrc
echo "------------running as $(whoami), in $(pwd)"
PWD=$(pwd)
USER=$(whoami)

echo 'export PATH="/home/$USER/anaconda3/bin:$PATH"' >> /home/$USER/.bashrc
echo "------------path: $PATH"

CONFIG="/home/$USER/config"
HASH="sha1:b07c86db1a39:696471a7f56df7014738a7da317d83442a010da8"

echo 'conf = get_config()' > $CONFIG
echo "conf.NotebookApp.ip = '0.0.0.0'" >> $CONFIG
echo "conf.NotebookApp.password = u'$HASH'" >> $CONFIG
echo "conf.NotebookApp.port = 9999" >> $CONFIG

echo "---------"
cat $CONFIG

./scripts/launch_notebook.sh
