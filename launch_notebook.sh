#!/bin/bash
USER=$(whoami)
# head -n 5 /home/$USER/.bashrc
source /home/$USER/.bashrc
r=$(which python)
echo "python: $r"
# useradd jupyter
# su jupyter
CONFIG="/home/$USER/config"
jupyter notebook --generate-config
cat $CONFIG > /home/$USER/.jupyter/jupyter_notebook_config.py
# /bin/bash -c "jupyter notebook"
