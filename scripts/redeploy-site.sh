#!/bin/bash

cd ~/project-team-js;

git fetch && git reset origin/main --hard;
chmod +x ~/project-team-js/scripts/deploy_commands.sh;
tmux kill-session -t portfolio-site;
tmux new-session -d -s portfolio-site;
tmux send-keys -t portfolio-site "~/project-team-js/scripts/deploy_commands.sh" Enter;