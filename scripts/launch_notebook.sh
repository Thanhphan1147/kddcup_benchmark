#!/bin/bash
USER=$(whoami)
source /home/$USER/.bashrc
r=$(which python)
echo "python: $r"
# useradd jupyter
# su jupyter
CONFIG="/home/$USER/config"
/bin/bash -c "jupyter notebook --generate-config"
cat $CONFIG > ~/.jupyter/jupyter_notebook_config.py
/bin/bash -c "jupyter notebook"
