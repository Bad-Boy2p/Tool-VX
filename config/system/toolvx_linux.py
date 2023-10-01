import os
from time import sleep
import random
import webbrowser as web
from pystyle import *
import subprocess



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

#def for slowing write and style
import sys, time
st = 0.0001
# i called it sp for slowPrint
def sp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(st)
  print()
# and change the st variable to what you want
logo1 = red +  """████████╗ ██████╗  ██████╗ ██╗         ██╗   ██╗██╗  ██╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║         ██║   ██║╚██╗██╔╝
   ██║   ██║   ██║██║   ██║██║         ██║   ██║ ╚███╔╝ 
   ██║   ██║   ██║██║   ██║██║         ╚██╗ ██╔╝ ██╔██╗ 
   ██║   ╚██████╔╝╚██████╔╝███████╗     ╚████╔╝ ██╔╝ ██╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝      ╚═══╝  ╚═╝  ╚═╝
                                                        """

logo2 = blue +  """ ███████████                   ████     █████   █████ █████ █████
░█░░░███░░░█                  ░░███    ░░███   ░░███ ░░███ ░░███ 
░   ░███  ░   ██████   ██████  ░███     ░███    ░███  ░░███ ███  
    ░███     ███░░███ ███░░███ ░███     ░███    ░███   ░░█████   
    ░███    ░███ ░███░███ ░███ ░███     ░░███   ███     ███░███  
    ░███    ░███ ░███░███ ░███ ░███      ░░░█████░     ███ ░░███ 
    █████   ░░██████ ░░██████  █████       ░░███      █████ █████
   ░░░░░     ░░░░░░   ░░░░░░  ░░░░░         ░░░      ░░░░░ ░░░░░ 
                                                                 
                                                                 
                                                                 """
logo3 = yellow +  """ ___________  ______      ______    ___           ___      ___  ___  ___  
("     _   ")/    " \    /    " \  |"  |         |"  \    /"  ||"  \/"  | 
 )__/  \\__/// ____  \  // ____  \ ||  |          \   \  //  /  \   \  /  
    \\_ /  /  /    ) :)/  /    ) :)|:  |           \\  \/. ./    \\  \/   
    |.  | (: (____/ //(: (____/ //  \  |___         \.    //     /\.  \   
    \:  |  \        /  \        /  ( \_|:  \         \\   /     /  \   \  
     \__|   \"_____/    \"_____/    \_______)         \__/     |___/\___| 
                                                                          
                                                                          
                                                                          
                                                                          
                                                                          
                                                                          
                                                                          
                                                                          
                                                                          """


logo4 = green + """▄▄▄█████▓ ▒█████   ▒█████   ██▓        ██▒   █▓▒██   ██▒
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒       ▓██░   █▒▒▒ █ █ ▒░
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░        ▓██  █▒░░░  █   ░
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░         ▒██ █░░ ░ █ █ ▒ 
  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒      ▒▀█░  ▒██▒ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░      ░ ▐░  ▒▒ ░ ░▓ ░
    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░      ░ ░░  ░░   ░▒ ░
  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░           ░░   ░    ░  
             ░ ░      ░ ░      ░  ░         ░   ░    ░  
                                           ░            
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        """
   


                                                                                                                                                                   

logo5 = purple + """~~~888~~~                   888       Y88b      / Y88b    / 
   888     e88~-_   e88~-_  888        Y88b    /   Y88b  /  
   888    d888   i d888   i 888         Y88b  /     Y88b/   
   888    8888   | 8888   | 888          Y888/      /Y88b   
   888    Y888   ' Y888   ' 888           Y8/      /  Y88b  
   888     "88_-~   "88_-~  888            Y      /    Y88b 
                                                            """                                                                                                                    
logo6 = red + """sdSS_SSSSSSbs    sSSs_sSSs      sSSs_sSSs    S.             .S    S.    .S S.   
YSSS~S%SSSSSP   d%%SP~YS%%b    d%%SP~YS%%b   SS.           .SS    SS.  .SS SS.  
     S%S       d%S'     `S%b  d%S'     `S%b  S%S           S%S    S%S  S%S S%S  
     S%S       S%S       S%S  S%S       S%S  S%S           S%S    S%S  S%S S%S  
     S&S       S&S       S&S  S&S       S&S  S&S           S&S    S%S  S%S S%S  
     S&S       S&S       S&S  S&S       S&S  S&S           S&S    S&S   SS SS   
     S&S       S&S       S&S  S&S       S&S  S&S           S&S    S&S    S_S    
     S&S       S&S       S&S  S&S       S&S  S&S           S&S    S&S   SS~SS   
     S*S       S*b       d*S  S*b       d*S  S*b           S*b    S*S  S*S S*S  
     S*S       S*S.     .S*S  S*S.     .S*S  S*S.          S*S.   S*S  S*S S*S  
     S*S        SSSbs_sdSSS    SSSbs_sdSSS    SSSbs         SSSbs_S*S  S*S S*S  
     S*S         YSSP~YSSY      YSSP~YSSY      YSSP          YSSP~SSS  S*S S*S  
     SP                                                                SP       
     Y                                                                 Y        

                                                                                                                                                                """              

logo7 = bblue + """88888888888                888      888     888 Y88b   d88P 
    888                    888      888     888  Y88b d88P  
    888                    888      888     888   Y88o88P   
    888   .d88b.   .d88b.  888      Y88b   d88P    Y888P    
    888  d88""88b d88""88b 888       Y88b d88P     d888b    
    888  888  888 888  888 888        Y88o88P     d88888b   
    888  Y88..88P Y88..88P 888         Y888P     d88P Y88b  
    888   "Y88P"   "Y88P"  888          Y8P     d88P   Y88b 
                                                            
                                                            
                                                            """

logo8 = bred + """ ___________  ______      ______    ___           ___      ___  ___  ___  
("     _   ")/    " \    /    " \  |"  |         |"  \    /"  ||"  \/"  | 
 )__/  \\__/// ____  \  // ____  \ ||  |          \   \  //  /  \   \  /  
    \\_ /  /  /    ) :)/  /    ) :)|:  |           \\  \/. ./    \\  \/   
    |.  | (: (____/ //(: (____/ //  \  |___         \.    //     /\.  \   
    \:  |  \        /  \        /  ( \_|:  \         \\   /     /  \   \  
     \__|   \"_____/    \"_____/    \_______)         \__/     |___/\___| 


                                                                                                                                                                                                                                                                                                        """
logo_list = [logo1, logo2, logo3, logo4, logo5, logo6, logo7, logo8]     

def down() :
	down_logo = green + """  _____                      _                 _  
 |  __ \                    | |               | | 
 | |  | | _____      ___ __ | | ___   __ _  __| | 
 | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` | 
 | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | 
 |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| 
                                                  
                                                  """
	print(Box.Lines("By Bad Boy\ngithub => https://github.com/Bad-Boy2p\nVersion 1.0"))
	os.system("clear")
	sp(down_logo)

def done() :
	done_banner = green + """ ██████████                               
░░███░░░░███                              
 ░███   ░░███  ██████  ████████    ██████ 
 ░███    ░███ ███░░███░░███░░███  ███░░███
 ░███    ░███░███ ░███ ░███ ░███ ░███████ 
 ░███    ███ ░███ ░███ ░███ ░███ ░███░░░  
 ██████████  ░░██████  ████ █████░░██████ 
░░░░░░░░░░    ░░░░░░  ░░░░ ░░░░░  ░░░░░░  
                                          
                                          
                                          """
	sp(done_banner)

def e() :
	error_banner = red + """███████╗██████╗ ██████╗  ██████╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝
██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗
███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
                                         """
	sp(error_banner)

                                                                                                                                                                                                                                                                                                                         
os.system("clear")
sp(random.choice(logo_list))
print(Box.Lines("By Bad Boy\ngithub => https://github.com/Bad-Boy2p\nVersion 1.0"))
pwd = "/home/kali/"
def red_hawk() :
	red_pwd = pwd + "RED_HAWK"
	down()
	sleep(2)
	os.system("sudo apt update -y")
	os.system("sudo apt  upgrade -y")
	os.system("sudo apt install git -y")
	os.system("sudo apt install php -y")
	os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
	os.system(f"mv RED_HAWK {pwd}")
	os.system("clear")
	# التحقق من وجود المجلد
	if os.path.exists(red_pwd) and os.path.isdir(red_pwd):
   	 done()
   	 print(f"{success} the tool was saved in :{yellow} {red_pwd}")
   	 
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input("are you want to see how to use the tool  (y , n):  ")
	if watch == "y" or watch == "yes" or watch == "Y" or watch == "YES": 
		web.open("https://github.com/Tuhinshubhra/RED_HAWK")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
	
	
	
	
	
def max_p() :
	max_pwd = pwd + "MaxPhisher"
	down()
	
	sleep(2)
	os.system("sudo apt update -y")
	os.system("sudo apt upgrade -y")
	os.system("sudo apt install git python3 php openssh -y")
	os.system("git clone https://github.com/KasRoudra/MaxPhisher")
	os.system(f"mv MaxPhisher {pwd}")
	os.system("clear")
	if os.path.exists(red_pwd) and os.path.isdir(red_pwd):
   	 done()
   	 print(f"{success} the tool was saved in :{yellow} {max_pwd}")   	 
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input("are you want to see how to use the tool  (y , n):  ")
	if watch == "y" or watch == "yes" or watch == "Y" or watch == "YES": 
		web.open("git clone https://github.com/KasRoudra/MaxPhisher")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
		
	
def py_p() :
	py_pwd = pwd + "PyPhisher"
	down()
	sleep(2)
	os.system("sudo apt update -y")
	os.system("sudo apt upgrade -y")
	os.system("sudo apt install git python3 php openssh -y")
	os.system("git clone https://github.com/KasRoudra/PyPhisher")
	os.system(f"mv PyPhisher {pwd}")
	os.system("clear")
	if os.path.exists(py_pwd) and os.path.isdir(py_pwd):
   	 done()
   	 print(f"{success} the tool was saved in : {yellow}{py_pwd}")
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input("are you want to see how to use the tool  (y , n):  ")
	if watch == "y" :
		web.open("https://github.com/KasRoudra/PyPhisher")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
	
	
	
	
	
def beef() :
	beef_pwd = pwd + "beef"
	down()
	sleep(2)
	os.system("sudo apt update -y")
	os.system("sudo apt upgrade -y ")
	os.system("sudo apt install git -y")
	os.system("git clone https://github.com/beefproject/beef")
	os.system(f"mv beef {pwd}")
	os.system("clear")
	if os.path.exists(beef_pwd) and os.path.isdir(beef_pwd):
   	 done()
   	 print(f"{success} the tool was saved in : {yellow}{beef_pwd}")
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input("are you want to see how to use the tooll (y , n):  ")
	if watch == "y" :
		web.open("https://github.com/beefproject/beef")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()



																
def metasploit() :
	down()
	sleep(2)
	os.system("sudo apt update -y ")
	os.system("sudo apt upgrade -y ")
	os.system("sudo apt install ruby curl wget nmap -y")
	os.system("sudo apt install metasploit-framework -y")
	print(f"{success}download successfly run with 'msfconsole' ")
	


def andro() :
	andro_pwd = pwd + "AndroRAT"
	down()
	os.system("clear")
	os.system("sudo apt update -y && sudo apt upgrade -y")
	os.system("sudo apt install git -y")
	os.system("git clone https://github.com/karma9874/AndroRAT")
	os.system(f"mv AndroRAT {pwd}")
	os.system("clear")
	if os.path.exists(andro_pwd) and os.path.isdir(andro_pwd):
   	 print(f"{success} the tool was saved in : {yellow}{andro_pwd}")
   	 done()
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input("are you want to see how to use the tool  (y , n):  ")
	if watch == "y" :
		web.open("https://github.com/karma9874/AndroRAT")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
	
def phone_sploit() :
	phone_pwd = pwd + "PhoneSploit"
	down()
	os.system("clear")
	os.system("sudo apt update -y && sudo apt upgrade -y")
	os.system("cd $HOME")
	os.system("sudo apt  install adb -y")
	os.system("git clone https://github.com/aerosol-can/PhoneSploit")
	os.system(f"mv PhoneSploit {pwd}")
	os.system("clear")
	if os.path.exists(phone_pwd) and os.path.isdir(phone_pwd):
   	 done()
   	 print(f"{success} the tool was saved in : {yellow}{phone_pwd}")
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input(yellow + "are you want to see how to use the tool (n , y) :  ")
	if watch == "y" :
		web.open("https://github.com/aerosol-can/PhoneSploit")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
	
def mask_p() :
	mask_pwd = pwd + "maskphish"
	down()
	os.system("clear")
	os.system("sudo apt update -y && sudo apt  upgrade -y")
	os.system("sudo apt install git -y")
	os.system("git clone https://github.com/jaykali/maskphish")
	os.system(f"mv maskphish {pwd}")
	os.system("clear")
	if os.path.exists(mask_pwd) and os.path.isdir(mask_pwd):
   	 done()
   	 print(f"{success} the tool was saved in : {yellow}{mask_pwd}")
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input(yellow + "are you want to see how to use the tool (n , y) :  ")
	if watch == "y" :
		web.open("https://github.com/jaykali/maskphish")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
		
def nex_p() :
	nex_pwd = pwd + "nexphisher"
	down()
	os.system("clear")
	os.system("sudo apt update -y && sudo apt upgrade -y && sudo apt install git -y")
	os.system("git clone https://github.com/htr-tech/nexphisher")
	os.system(f"mv nexphisher {pwd}")
	os.system("clear")
	if os.path.exists(nex_pwd) and os.path.isdir(nex_pwd):
   	 done()
   	 print(f"{success} the tool was saved in : {yellow}{nex_pwd}")
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input(yellow + "are you want to see how to use the tool (n , y) :  ")
	if watch == "y" :
		web.open("https://github.com/htr-tech/nexphisher")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
		
def router_function() :
	os.system("sudo apt update -y &&  sudo apt upgrade -y")
	os.system("sudo apt install python-pip -y")
	os.system("sudo apt install git -y")
	os.system("git clone https://www.github.com/threat9/routersploit")
	os.system(f"mv routersploit {pwd}")
	os.system("clear")
def router() :
	r_pwd = pwd + "routersploit"
	down()
	router_function()
	if os.path.exists(r_pwd) and os.path.isdir(r_pwd):
   	 done()
   	 print(f"{success} the tool was saved in : {yellow}{r_pwd}")
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input(yellow + "are you want to see how to use the tool (n , y) :  ")
	if watch == "y" :
		web.open("https://www.github.com/threat9/routersploit")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
		
		
		
def cam() :
	cam_pwd = pwd + "CamHacker"
	down()
	os.system("sudo apt update -y && sudo apt upgrade -y")
	os.system("sudo apt install git -y")
	os.system("git clone https://github.com/KasRoudra/CamHacker")
	os.system(f"mv CamHacker {pwd}")
	os.system("clear")
	if os.path.exists(cam_pwd) and os.path.isdir(cam_pwd):
   	 done()
   	 print(f"{success} the tool was saved in : {yellow}{cam_pwd}")
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input(yellow + "are you want to see how to use the tool (n , y) :  ")
	if watch == "y" :
		web.open("https://github.com/KasRoudra/CamHacker")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
		
		
		
def wifite():
	wifi_pwd = pwd + "wifite"
	down()
	os.system("sudo apt  update -y && sudo apt upgrade -y")
	os.system("sudo apt install git -y")
	os.system("git clone https://github.com/derv82/wifite")
	os.system(f"mv wifite {pwd}")
	os.system("clear")
	if os.path.exists(wifi_pwd) and os.path.isdir(wifi_pwd):
   	 done()
   	 print(f"{success} the tool was saved in : {yellow}{wifi_pwd}")
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input(yellow + "are you want to see how to use the tool (n , y) :  ")
	if watch == "y" :
		web.open("https://github.com/derv82/wifite")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
	
	
def sqlmap() :
	sql_pwd = pwd + "sqlmap"
	down()
	os.system("sudo apt update -y && sudo apt upgrade -y")
	os.system("sudo apt install git -y")
	os.system("git clone https://github.com/sqlmapproject/sqlmap")
	os.system(f"mv sqlmap {pwd}")
	os.system("clear")
	if os.path.exists(sql_pwd) and os.path.isdir(sql_pwd):
   	 done()
   	 print(f"{success} the tool was saved in : {yellow}{sql_pwd}")
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input(yellow + "are you want to see how to use the tool (n , y) :  ")
	if watch == "y" :
		web.open("https://github.com/sqlmapproject/sqlmap")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
	
	
	
	
	
def user_recon() :
	user_pwd = pwd + "userrecon"
	down()
	os.system("sudo apt update -y && sudo apt upgrade -y")
	os.system("sudo apt install git -y")
	os.system("git clone https://github.com/wishihab/userrecon")
	os.system(f"mv userrecon {pwd}")
	os.system("clear")
	if os.path.exists(user_pwd) and os.path.isdir(user_pwd):
   	 done()
   	 print(f"{success} the tool was saved in : {yellow}{user_pwd}")
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input(yellow + "are you want to see how to use the tool (n , y) :  ")
	if watch == "y" :
		web.open("https://github.com/wishihab/userrecon")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
	
	
	
	
	
	

def phone_infoga() :
	infoga_pwd = pwd + "PhoneInfoga"
	down()
	os.system("sudo apt update -y && pkg upgrade -y")
	os.system("sudo apt install git -y")
	os.system("git clone https://github.com/sundowndev/PhoneInfoga.git")
	os.system(f"mv PhoneInfoga {pwd}")
	os.system("clear")
	if os.path.exists(infoga_pwd) and os.path.isdir(infoga_pwd):
   	 done()
   	 print(f"{success} the tool was saved in : {yellow}{infoga_pwd}")
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input(yellow + "are you want to see how to use the tool (n , y) :  ")
	if watch == "y" :
		web.open("https://github.com/sundowndev/PhoneInfoga.git")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
	
	
	
	
def mdork() :
	mdork_pwd = pwd + "M-dork"
	down()
	os.system("sudo apt update -y && sudo apt upgrade -y")
	os.system("sudo apt install python2 -y")
	os.system("sudo apt install git -y")
	os.system("pip2 install mechanize")
	os.system("git clone https://github.com/Ranginang67/M-dork")
	os.system(f"mv M-dork {pwd}")
	os.system("clear")
	if os.path.exists(mdork_pwd) and os.path.isdir(mdork_pwd):
   	 done()
   	 print(f"{success} the tool was saved in : {yellow}{mdork_pwd}")
	else:
  	  e()
  	  print(f"{error} cant find tool path :(")
	watch = input(yellow + "are you want to see how to use the tool (n , y) :  ")
	if watch == "y" :
		web.open("https://github.com/Ranginang67/M-dork")
	elif watch == "n" :
		pass
	else:
		pass
	back_btn = input(f"Click {green}Enter to back ")
	if back_btn == "" :
		back()
	else:
		print(f"{red}exiting :(")
		exit()
	
	
	
print(info + "1_RED HAWK")
print(info + "2_Max phisher")
print(info + "3_Py phisher")
print(info + "4_Beef")
print(info + "5_Metasploit")
print(info + "6_Androrat")
print(info + "7_Phone sploit")
print(info + "8_mask phishe")
print(info + "9_nexphishe")
print(info + "10_router sploit")
print(info + "11_cam hacker")
print(info + "12_wifite")
print(info + "13_sqlmap")
print(info + "14_user recon")
print(info + "15_Phone Infoga")
print(info + "16_M-dork")
print(info + "More on the way")
print(green + "[" + purple +  "0" + green + "]" + cyan + " Exit")
print("")
print("")
def exit_1() :
	
	print( green + "have a good day :)")
	exit()
def back() :
	os.system("clear")
	sp(random.choice(logo_list))
	print(Box.Lines("By Bad Boy\ngithub => https://github.com/Bad-Boy2p\nVersion 1.0"))
	print(info + "1_RED HAWK")
	print(info + "2_Max phisher")
	print(info + "3_Py phisher")
	print(info + "4_Beef")
	print(info + "5_Metasploit")
	print(info + "6_Androrat")
	print(info + "7_Phone sploit")
	print(info + "8_mask phishe")
	print(info + "9_nexphishe")
	print(info + "10_router sploit")
	print(info + "11_cam hacker")
	print(info + "12_wifite")
	print(info + "13_sqlmap")
	print(info + "14_user recon")
	print(info + "15_Phone Infoga")
	print(info + "16_M-dork")
	print(info + "More on the way")
	print(green + "[" + purple +  "0" + green + "]" + cyan + " Exit")
	print("")
	print("")
	choice = input(f"{red}root@ToolVX {green}==>  ")
	if choice == "1" :
		red_hawk()
	if choice == "2" :
		max_p()
	if choice == "3" :
		py_p()
	if choice == "4" :
		beef()
	if choice == "5" :
		metasploit()
	if choice == "6" :
		andro()
	if choice == "7" :
		phone_sploit()
	if choice == "8" :
		mask_p()
	if choice == "9" :
		nex_p()
	if choice == "10" :
		router()
	if choice == "11" :
		cam()
	if choice == "12" :
		wifite()
	if choice == "13" :
		sqlmap()
	if choice == "14" :
		user_recon()
	if choice == "15" :
		phone_infoga()
	if choice == "16" :
		mdork()
	if choice == "0" :
		exit_1()
	else :
		print(error + "bad choice !!")
		sleep(3)
		back()
choice = input(f"{red}root@ToolVX {green}==>  ")
if choice == "1" :
	red_hawk()
if choice == "2" :
	max_p()
if choice == "3" :
	py_p()
if choice == "4" :
	beef()
if choice == "5" :
	metasploit()
if choice == "6" :
	andro()
if choice == "7" :
	phone_sploit()
if choice == "8" :
	mask_p()
if choice == "9" :
	nex_p()
if choice == "10" :
	router()
if choice == "11" :
	cam()
if choice == "12" :
	wifite()
if choice == "13" :
	sqlmap()
if choice == "14" :
	user_recon()
if choice == "15" :
	phone_infoga()
if choice == "16" :
	mdork()
if choice == "0" :
	exit_1()
else :
	print(error + "bad choice !!")
	sleep(3)
	back()
	



















