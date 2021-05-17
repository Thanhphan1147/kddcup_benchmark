#!/bin/bash
source ~/.bashrc
r=$(which python)
echo "python: $r"
# useradd jupyter
# su jupyter
CONFIG="/home/$USER/config"
jupyter notebook --generate-config
cat $CONFIG > ~/.jupyter/jupyter_notebook_config.py
/bin/bash -c "jupyter notebook"
