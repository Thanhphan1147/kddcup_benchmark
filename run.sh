#!/bin/bash
useradd -m jupyter
cp -r scripts/ /home/jupyter
cd /home/jupyter/scripts
echo "$(pwd), $(whoami)"
su -c "./get_script.sh" jupyter
