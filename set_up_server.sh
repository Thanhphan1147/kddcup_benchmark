#!/bin/bash
# wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
# bash Anaconda3-2020.11-Linux-x86_64.sh
# echo "export PATH="/home/ubuntu/anaconda3/bin:$PATH" >> ~/.bashrc
echo $PATH

HASH="sha1:b07c86db1a39:696471a7f56df7014738a7da317d83442a010da8"
CONFIGFILE="config"
echo 'config: $CONFIGFILE'

echo 'conf = get_config()' > config
echo "conf.NotebookApp.ip = '0.0.0.0'" >> config
echo "conf.NotebookApp.password = u'$HASH'" >> config
echo "conf.NotebookApp.port = 9999" >> config

cat config
echo "$CONFIGFILE"

./launch_notebook.sh

# wget http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz
# wget http://kdd.ics.uci.edu/databases/kddcup99/kddcup.testdata.unlabeled.gz
# gunzip kddcup.data.gz kddcup.testdata.unlabeled.gz
