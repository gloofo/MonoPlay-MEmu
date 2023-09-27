
from pymemuc import PyMemuc
from time import sleep
import sys
import os
import glob
from conn import *
memuc = PyMemuc()

print(
'''
====================================================================================
========================== PROTOTYPE PROJECT BY: @gloofo ===========================
========================== Contact me at Telegram: @gloofo =========================
====================================================================================
''')

getEmuIndex = 0
getPackageName = ""
getMonoDelay = 0
getLink = ""

def getIndex():
    try:
        getEmuIndex = int(input("Enter Emulator Index: "))
    except ValueError:
        print("The entered value is invalid. Please try again.")
        sys.exit()
    
    return getEmuIndex

def getPackage():
    try:
        getPackageName = input("Enter the package name for browser: ")
    except ValueError:
        print("The entered value is invalid. Please try again.")
        sys.exit()

    return getPackageName

def getNewLinkMono():
    try:
        getLinkName = input("Enter the invite link: ")
        os.system('cls')
    except ValueError:
        print("The entered value is invalid. Please try again.")
        sys.exit()

    return getLinkName



indexData = getIndex()
newLink = main()

# list out all vms, get the index of the first one
# for ex. first emulator index = 0
# second emulator index = 1 and etc.

def getIndexValue():
    index = memuc.list_vm_info()[indexData]['index']
    return index

def loading_animation(yourtext: str):
    symbols = ['-', '\\', '|', '/']
    for _ in range(20):  # Number of iterations for the animation
        for symbol in symbols:
            sys.stdout.write(f'\r{yourtext} {symbol}')
            sys.stdout.flush()
            sleep(0.1)  # Adjust the delay to control animation speed
    sys.stdout.write('\rLoading   ')  # Overwrite with spaces to clear the text
    sys.stdout.flush()
    
# start the vm
def start_emu():
    print(f"{loading_animation('Loading')}")
    os.system('cls')
    memuc.start_vm(indexValue, headless=True, timeout=60)
    
def start_automate(indexNumber: int, p1: str, p2: str, link: str):
    print(f"{loading_animation('Washing Clothes')}")
    os.system('cls')
    #memuc.send_adb_command_vm(f"shell pm enable {packageName}", indexNumber)
    memuc.send_adb_command_vm(f"shell pm clear {p1}", indexNumber) #mono
    memuc.send_adb_command_vm(f"shell pm clear {p2}", indexNumber) #ps
    #memuc.send_adb_command_vm(f"shell pm clear {p3}", indexNumber) #mozilla
    memuc.send_adb_command_vm(f"shell rm -r /sdcard/Android/data/{p1}", indexNumber) #ps
    memuc.send_adb_command_vm(f"shell rm -r /sdcard/Android/data/{p2}", indexNumber) #mono
    #memuc.send_adb_command_vm(f"shell rm -r /sdcard/Android/data/{p3}", indexNumber) #mozilla
    memuc.send_adb_command_vm(f"shell rm -r /data/data/{p1}/*", indexNumber) #ps
    memuc.send_adb_command_vm(f"shell rm -r /data/data/com.talpa.hibrowser/cache/*", indexNumber) #browser
    sleep(4)
    memuc.send_adb_command_vm(f"shell am start -a android.intent.action.VIEW -d {link}", indexNumber)
    #shell am start -a "android.intent.action.VIEW" -d "http://www.google.com" --es "com.android.browser.application_id" "com.package.name"
    print(f"{loading_animation('Launching Space-X')}")
    os.system('cls')
    sleep(45)
    print(f"{loading_animation('Lift-off')}")
    os.system('cls')
    memuc.send_adb_command_vm(f"shell am force-stop {p1}", indexNumber) #ps
    memuc.send_adb_command_vm(f"shell am force-stop com.talpa.hibrowser", indexNumber) #mono
    memuc.send_adb_command_vm(f"shell shell am kill {p1}", indexNumber) #ps
    memuc.send_adb_command_vm(f"shell shell am kill com.talpa.hibrowser", indexNumber) #mozilla
    print(f"{loading_animation('Landing')}")
    os.system('cls')
    sleep(2)

indexValue = getIndexValue()
start_emu()

def start():
    while True:
        sleep(2)
        start_automate(indexValue, "com.scopely.monopolygo", "com.google.android.gms", newLink)
