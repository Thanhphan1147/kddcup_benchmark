#!/bin/bash
userdel jupyter
rm -rf /home/jupyter
useradd -m jupyter
# cp -r scripts/ /home/jupyter
cd /home/jupyter
echo "$(pwd), $(whoami)"

su -c "git clone https://github.com/Thanhphan1147/kddcup_benchmark.git" jupyter
cd kddcup_benchmark
su -c "scripts/get_script.sh" jupyter
