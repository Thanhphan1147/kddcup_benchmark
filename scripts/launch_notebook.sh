#!/bin/bash
source ~/.bashrc
r=$(which python)
echo "python: $r"
# useradd jupyter
# su jupyter
jupyter notebook --generate-config
cat config > ~/.jupyter/jupyter_notebook_config.py
jupyter notebook
