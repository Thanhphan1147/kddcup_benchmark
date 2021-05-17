#!/bin/bash
source ~/.bashrc
r=$(which python)
echo "python: $r"
git clone https://github.com/Thanhphan1147/kddcup_benchmark.git
cd kddcup_benchmark
# useradd jupyter
# su jupyter
jupyter notebook --generate-config
cat config > ~/.jupyter/jupyter_notebook_config.py
jupyter notebook
