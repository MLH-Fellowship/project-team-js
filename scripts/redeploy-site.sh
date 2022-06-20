#!/bin/bash

cd ~/project-team-js;

git fetch && git reset origin/main --hard;
chmod +x ~/project-team-js/scripts/deploy_commands.sh;
tmux kill-server
tmux new-session -d -s  portfolio-site 'bash deploy_commands.sh';
tmux detach -s portfolio-site;