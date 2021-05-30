#!/bin/bash
userdel jupyter
rm -rf /home/jupyter
useradd -m jupyter
cp *.sh /home/jupyter
cd /home/jupyter

echo "--- DEBUG: $(pwd), $(whoami)"
chown -c jupyter *.sh

# su -c "git clone https://github.com/Thanhphan1147/kddcup_benchmark.git" jupyter
# cd kddcup_benchmark
su -c "./get_script.sh" jupyter
