
wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
bash Anaconda3-2019.03-Linux-x86_64.sh
echo "export PATH=/home/ubuntu/anaconda3/bin:$PATH" >> ~/.bashrc
source ~/.bashrc
jupyter notebook --generate-config

HASH="sha1:b07c86db1a39:696471a7f56df7014738a7da317d83442a010da8"
CONFIG="conf = get_config()
conf.NotebookApp.ip = '0.0.0.0'
conf.NotebookApp.password = u'$HASH'
conf.NotebookApp.port = 9999"
echo "$CONFIG" > ~/.jupyter/jupyter_notebook_config.py
echo "$CONFIG"
