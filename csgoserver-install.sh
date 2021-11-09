#!/bin/bash

sudo apt update
sudo apt upgrade

sudo dpkg --configure -a

sudo apt install steamcmd -y

sudo add-apt-repository multiverse
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install lib32gcc1 steamcmd -y
sudo apt install lib32gcc1 -y

mkdir ~/Steam && cd ~/Steam

sudo curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -

sudo apt install tmux screen -y;

cd ~/Steam
./steamcmd.sh +login anonymous +force_install_dir ~/cs_go/ +app_update 740 validate +quit

cp ~/csgo-server/esl5on5.cfg /cs_go/csgo/cfg/
cp ~/csgo-server/eslMastersGotv.cfg /cs_go/csgo/cfg/
cp ~/csgo-server/server.cfg /cs_go/csgo/cfg/

cd ~
git clone https://github.com/jffz/docker-ebot.git 
