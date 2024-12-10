#!/bin/bash

# Colors
GREEN="\[\e[32m\]"
BLUE="\[\e[34m\]"
# WHITE="\[\e[37m\]"
# CYAN="\[\e[36m\]"
# YELLOW="\[\e[33m\]"
# MAGENTA="\[\e[35m\]"
LGRAY="\[\e[37m\]"

# Bright Colors
# BRGREEN="\[\e[92m\]"

# Background Colors
# BGGREEN="\[\e[42m\]"

# RESET="\[\e[0m\]"
BOLD="\[\e[1m\]"
NORMAL="\[\e[0m\]"



#PS1="$BOLD$GREEN\u$BLUE@$CYAN\h [\W] | $WHITE\t | $MAGENTA$weather\n$YELLOW\$$NORMAL "

check_git_status() {
	if [[ -d ".git" ]]; then
		branch=$(git branch --show-current 2>/dev/null)
		echo -ne "${GREEN}($branch)${NORMAL} "
		
	fi
}

check_venv(){
	if [[ $VIRTUAL_ENV != "" ]]; then
		echo -ne "${LGRAY}($(basename "$VIRTUAL_ENV" 2>/dev/null))${NORMAL} "
	fi
}

main() {
	PS1="$(check_venv)${BOLD}${BLUE}\W $(check_git_status)${NORMAL}\$${NORMAL} "
}

PROMPT_COMMAND="main"

