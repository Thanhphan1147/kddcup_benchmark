#!/bin/bash
r=$(which python)
echo "python: $r"
jupyter notebook --generate-config
cat /tmp/config.py >> ~/.jupyter/jupyter_notebook_config.py
jupyter notebook
