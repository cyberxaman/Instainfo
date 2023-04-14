#!/bin/bash
# made by cyberxaman

clear

RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

trap 'echo -e "${RED}\nProgram interrupted. Goodbye! 👋${NC}"; exit' INT

printf "${RED}"
cat << "EOF"
 _           _        _        __       
(_)_ __  ___| |_ __ _(_)_ __  / _| ___  
| | '_ \/ __| __/ _` | | '_ \| |_ / _ \ 
| | | | \__ \ || (_| | | | | |  _| (_) |
|_|_| |_|___/\__\__,_|_|_| |_|_|  \___/ 
                                        
EOF
printf "${NC}"
printf "${YELLOW}   <---(( Coded by cyberxaman ))--> \n${NC}"
printf "${CYAN}-----------------------------------------\n"
printf "-----------------------------------------\n${NC}"

# installation

pip3 install instaloader
pip3 install pyshortener
pip3 install termcolor
