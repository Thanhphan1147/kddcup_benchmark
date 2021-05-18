#!/bin/bash
ID="$(whoami)-$(pwd)"
HOME=$(pwd)
echo "---DEBUG: $HOME $(whoami)"

wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
bash Anaconda3-2020.11-Linux-x86_64.sh

wget http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz
wget http://kdd.ics.uci.edu/databases/kddcup99/kddcup.testdata.unlabeled.gz
gunzip kddcup.data.gz kddcup.testdata.unlabeled.gz

sh -c "./set_up_server.sh" jupyter
