#!/bin/bash

cd ~/project-team-js;

git fetch && git reset origin/main --hard;
chmod +x ~/project-team-js/scripts/deploy_commands.sh;

./project-team-js/scripts/deploy_commands.sh
systemctl daemon-reload
systemctl restart myportfolio