#/bin/bash

sudo apt install steamcmd -y

sudo add-apt-repository multiverse
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install lib32gcc1 steamcmd -y

sudo apt install lib32gcc1 -y

mkdir ~/Steam && cd ~/Steam

curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -

sudo apt install tmux screen -y;

cd ~/Steam
./steamcmd.sh
