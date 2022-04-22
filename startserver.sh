#!/bin/bash

./srcds_run -game csgo -usercon +game_type 0 +game_mode 1 +mapgroup mg_active +map de_dust2 +setsteamaccount 7C933D72733239CFD536911B88ABDAD7 -tickrate 128 -port 27015 -pingboost 3 -exec server.cfg -maxplayers 12 -addhltv1 1 -ip xxx.xxx.xxx.xxx

# probar pingboost con sus tres distintos valores <1/2/3>
