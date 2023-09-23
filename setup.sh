#!/bin/bash
current_directory="$PWD"
# التحقق من وجود مجلد Termux باستخدام المتغير $PREFIX
if [ -d "$PREFIX" ]; then
    echo "your system is termux"
    pkg update -y
    pkg upgrade -y
    pkg install python -y
    pkg install python-pip
    pip install pystyle
    pip install requests
   chmod +x $current_directory/config/files/requests.py
   chmod +x main.py
   chmod +x $current_directory/config/system/toolvx_termux.py
   chmod +x $current_directory/config/system/toolvx_linux.py
    
elif [ -e /etc/os-release ]; then
    source /etc/os-release
    if [[ "$NAME" == *"Kali"* ]]; then
        echo "your system is kali linux"
        sudo apt update -y
        sudo apt upgrade -y
        sudo apt install python
        sudo apt install python-pip
        pip install requests
        pip install pystyle
        pip install webbrowser
       sudo chmod +x $current_directory/config/files/requests.py
       sudo chmod +x main.py
       sudo chmod +x $current_directory/config/system/toolvx_termux.py
       sudo chmod +x $current_directory/config/system/toolvx_linux.py
    else
        echo "Your system support does not comply with tool files"
    fi
else
    echo "unknown system"
fi

