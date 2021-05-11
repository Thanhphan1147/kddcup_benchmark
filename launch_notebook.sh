#!/bin/bash
r=$(which python)
jupyter notebook --generate-config
cat /tmp/config.py >> ~/.jupyter/jupyter_notebook_config.py