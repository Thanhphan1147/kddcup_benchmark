#!/bin/bash
useradd -m jupyter
cp -r scripts/ /home/jupyter
cd /home/jupyter
echo "$(pwd), $(whoami)"
su -c "scripts/get_script.sh" jupyter
