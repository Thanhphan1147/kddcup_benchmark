#!/bin/bash
useradd -m jupyter
cd /home/jupyter
su -c "scripts/get_scripts.sh" jupyter