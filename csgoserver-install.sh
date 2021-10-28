#/bin/bash

dpkg --configure -a

apt install steamcmd -y

add-apt-repository multiverse
dpkg --add-architecture i386
apt update
apt install lib32gcc1 steamcmd -y
apt install lib32gcc1 -y

mkdir ~/Steam && cd ~/Steam

curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -

apt install tmux screen -y;

cd ~/Steam
./steamcmd.sh +login anonymous +force_install_dir ../cs_go +app_update 740 validate +quit
