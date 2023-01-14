#!/bin/bash
# script to install a bash script that will run "apt-get update" and "apt-get upgrade -y" at once
# run this script with the "source"/"." command, like so: ". ./install.sh"

bindir=$HOME/.local/bin

mkdir -p $bindir
echo "sudo apt-get update && sudo apt-get upgrade -y" > $bindir/run-apt.sh
chmod 744 $bindir/run-apt.sh
. $HOME/.profile
echo "run-apt.sh script installed $bindir"
