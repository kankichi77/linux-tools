#! /bin/bash
# script to install a bash script that will run "apt-get update" and "apt-get upgrade -y" at once

mkdir -p $HOME/bin
echo "sudo apt-get update && sudo apt-get upgrade -y" > $HOME/bin/run-apt.sh
chmod 744 $HOME/bin/run-apt.sh
. $HOME/.profile
