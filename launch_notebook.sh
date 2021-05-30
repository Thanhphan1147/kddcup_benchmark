#!/bin/bash
USER=$(whoami)
# head -n 5 /home/$USER/.bashrc
/bin/bash - c "source /home/$USER/.bashrc"
r=$(which python)
echo "python: $r"
# useradd jupyter
# su jupyter
CONFIG="/home/$USER/config"
/bin/bash -c "jupyter notebook --generate-config"
cat $CONFIG > /home/$USER/.jupyter/jupyter_notebook_config.py
git clone https://github.com/Thanhphan1147/kddcup_benchmark.git
mv kddcup.* kddcup_benchmark
cd kddcup_benchmark
/bin/bash -c "jupyter notebook&"
