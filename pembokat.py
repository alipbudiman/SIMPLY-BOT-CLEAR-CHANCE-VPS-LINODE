import schedule
import time
import os

print("==== SUCCESS LOGIN PEMBOKAT V1 ====\nVersion: 1.0\nCreator: Alif Budiman\nLine: https://line.me/ti/p/~alifbudimanwahabbi\nWA : 082113791904\n\n\n\n")
print("-------------------------------------[ REAPORT ]--------------------------------------")
os.system('systemd-resolve --flush-caches')
os.system('sync; echo 1 > /proc/sys/vm/drop_caches && echo 2 > /proc/sys/vm/drop_caches && echo 3 > /proc/sys/vm/drop_caches')
print("--------------------------------Resolv Statistic--------------------------------------")
os.system('systemd-resolve --statistics')
print("--------------------------------Memory Status-----------------------------------------")
status = os.popen('free').read()
print(status)
print("-------------------------------Load Server Status-------------------------------------")
load = os.popen('uptime').read()
print(load)
print("--------------------------------------------------------------------------------------")

def do_clearchance():
    print("-------------------------------------[ REAPORT ]--------------------------------------")
    os.system('systemd-resolve --flush-caches')
    os.system('sync; echo 1 > /proc/sys/vm/drop_caches && echo 2 > /proc/sys/vm/drop_caches && echo 3 > /proc/sys/vm/drop_caches')
    print("--------------------------------Resolv Statistic--------------------------------------")
    os.system('systemd-resolve --statistics')
    print("--------------------------------Memory Status-----------------------------------------")
    status = os.popen('free').read()
    print(status)
    print("-------------------------------Load Server Status-------------------------------------")
    load = os.popen('uptime').read()
    print(load)
    print("--------------------------------------------------------------------------------------")

def do_cleartemp():
    os.system('clear')
    print("_________auto clear temp in 3 hours_________")

schedule.every(30).minutes.do(do_clearchance)
schedule.every(3).hours.do(do_cleartemp)

while 1:
    schedule.run_pending()
    time.sleep(1)

