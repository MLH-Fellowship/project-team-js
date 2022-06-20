#!/bin/bash

tmux new-session -d -s  portfolio-site 'bash deploy_commands.sh'
tmux detach -s portfolio-site