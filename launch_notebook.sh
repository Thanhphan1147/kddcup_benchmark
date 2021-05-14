#!/bin/bash
r=$(which python)
echo "python: $r"
useradd jupyter
# su jupyter
jupyter notebook --generate-config
cat /tmp/config.py >> ~/.jupyter/jupyter_notebook_config.py
jupyter notebook --allow-root
