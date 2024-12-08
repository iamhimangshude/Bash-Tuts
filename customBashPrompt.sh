#!/bin/bash

# Colors
GREEN='\[\e[31m\]'
BLUE='\[\e[34m\]'
WHITE='\[\e[37m\]'
CYAN='\[\e[36m\]'
YELLOW='\[\e[33m\]'
MAGENTA='\[\e[35m\]'

# Bright Colors
BRGREEN='\[\e[92m\]'

# Background Colors
BGGREEN='\[\e[42m\]'

RESET='\[\e[0m\]'
BOLD='\[\e[1m\]'
NORMAL='\[\e[0m\]'

city=$(curl -s ipinfo.io/city)
weather=$(curl -s http://wttr.in/$city?format=3)


#PS1="$BOLD$GREEN\u$BLUE@$CYAN\h [\W] | $WHITE\t | $MAGENTA$weather\n$YELLOW\$$NORMAL "
delay=0.5
echo "Hello $(whoami)!"

sleep $delay
echo "$(hostname):"
echo -e "Where to go?
1 - Documents
2 - Downloads
3 - Github
9 - Custom Path
0 - Home\a"


read choice

case $choice in
	1)
		cd ~/Documents
		;;
	2)
		cd ~/Downloads
		;;
	3)
		cd ~/Github
		;;
	9)
		echo "Enter your full path (/home/$(whoami)): "
		read pathAddr
		cd "$pathAddr" || exit
		;;
	0)
		cd ~
		;;

esac

check_git_status() {
	if [[ -d ".git" ]]; then
		branch=$(git branch --show-current)
		PS1="$BOLD-> $BLUE\W$RESET$BOLD on branch $BGGREEN$BLUE$branch$RESET$BOLD$WHITE (git) \$$NORMAL "
	else
		PS1="$BOLD-> \W \$$NORMAL "
	fi
}

PROMPT_COMMAND="check_git_status"
