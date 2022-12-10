#!/bin/bash

./srcds_run -game csgo -usercon +game_type 0 +game_mode 1 +mapgroup mg_active +map de_dust2 +setsteamaccount 959D69F92DFB498FA8E85DA84B753D1E -tickrate 128 -port 27015 -pingboost 3 -exec esl5on5.cfg -maxplayers 12 -addhltv1 1 -ip xxx.xxx.xxx.xxx

# probar pingboost con sus tres distintos valores <1/2/3>
