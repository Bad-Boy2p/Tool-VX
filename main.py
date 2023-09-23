import os
import requests
from time import sleep



# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
version="1.0"

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"



def check_system():
    # التحقق من وجود مجلد /data/data/com.termux في Termux
    if os.path.exists('/data/data/com.termux'):
        return "Termux"

    # التحقق من وجود ملف /etc/os-release وكلمة "Kali" فيه في Kali Linux
    if os.path.exists('/etc/os-release'):
        with open('/etc/os-release', 'r') as os_release_file:
            for line in os_release_file:
                if 'Kali' in line:
                    return "Kali Linux"

    return "bad system"

system = check_system()
if system == "Termux" :
	print(f"{info} Checking your operating system ...")
	exec(open(os.getcwd() + "/config/files/connection_github.py").read())
	sleep(3)
	print(f"{success} your opiration system is {yellow}{system}")
	exec(open(os.getcwd() + "/config/system/toolvx_termux.py").read())
	print(f"{info} downloading termux mudoles")
if system == "Kali Linux" :
	print(f"{info} Checking your operating system ...")
	exec(open(os.getcwd() + "/config/files/connection_github.py").read())
	sleep(3)
	print(f"{success} your opiration system is {yellow}{system}")
	exec(open(os.getcwd() + "/config/system/toolvx_linux.py").read())
	

