#!/bin/bash
ID="$(whoami)-$(pwd)"
HOME=$(pwd)
echo "-----------------$ID----------------"

wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
bash Anaconda3-2020.11-Linux-x86_64.sh

wget http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz
wget http://kdd.ics.uci.edu/databases/kddcup99/kddcup.testdata.unlabeled.gz
gunzip kddcup.data.gz kddcup.testdata.unlabeled.gz

./set_up_server.sh
