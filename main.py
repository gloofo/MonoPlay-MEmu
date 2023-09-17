from pymemuc import PyMemuc
from time import sleep
import sys
memuc = PyMemuc(debug=True)

print(
'''
====================================================================================
============================== TRY TO RELAX YOUR ANUS ==============================
========================== PROTOTYPE PROJECT BY: @gloofo ===========================
========================== Contact me at Telegram: @gloofo =========================
============================ I LOVE PAWGS & BIG BOOBIES ============================
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

def getInvitation():
    try:
        invitationLink = input("Enter the invitation link: ")
    except ValueError:
        print("The entered value is invalid. Please try again.")
        sys.exit()

    return invitationLink

indexData = getIndex()
getBrowserPackage = getPackage()
invite = getInvitation()

# list out all vms, get the index of the first one
# for ex. first emulator index = 0
# second emulator index = 1 and etc.

def getIndexValue():
    index = memuc.list_vm_info()[indexData]['index']
    return index

# start the vm
def start_emu(indexNumber: int):
    indexValue = getIndexValue()
    memuc.start_vm(indexValue, timeout=30)
    memuc.set_configuration_vm("is_customed_resolution", "1", vm_index=indexNumber)
    memuc.set_configuration_vm("resolution_width", "460", vm_index=indexNumber)
    memuc.set_configuration_vm("resolution_height", "680", vm_index=indexNumber)
    memuc.set_configuration_vm("vbox_dpi", "160", vm_index=indexNumber)
    # set to remember window location
    memuc.set_configuration_vm("start_window_mode", "1", vm_index=indexNumber)

def start_automate(indexNumber: int, p1: str, p2: str, p3: str, link: str):
    #memuc.send_adb_command_vm(f"shell pm enable {packageName}", indexNumber)
    memuc.send_adb_command_vm(f"shell pm clear {p1}", indexNumber) #mono
    memuc.send_adb_command_vm(f"shell pm clear {p2}", indexNumber) #ps
    #memuc.send_adb_command_vm(f"shell pm clear {p3}", indexNumber) #mozilla
    memuc.send_adb_command_vm(f"shell rm -r /sdcard/Android/data/{p1}", indexNumber) #ps
    memuc.send_adb_command_vm(f"shell rm -r /sdcard/Android/data/{p2}", indexNumber) #mono
    #memuc.send_adb_command_vm(f"shell rm -r /sdcard/Android/data/{p3}", indexNumber) #mozilla

    sleep(2)
    memuc.send_adb_command_vm(f"shell rm -r /data/data/{p1}/*", indexNumber) #ps
    memuc.send_adb_command_vm(f"shell rm -r /data/data/{p3}/cache/*", indexNumber) #browser
    sleep(5)
     
    memuc.send_adb_command_vm(f"shell am start -a android.intent.action.VIEW -d {link}", indexNumber)
    #shell am start -a "android.intent.action.VIEW" -d "http://www.google.com" --es "com.android.browser.application_id" "com.package.name"
    sleep(35)
    memuc.send_adb_command_vm(f"shell am force-stop {p1}", indexNumber) #ps
    memuc.send_adb_command_vm(f"shell am force-stop {p3}", indexNumber) #mono
    memuc.send_adb_command_vm(f"shell shell am kill {p1}", indexNumber) #ps
    memuc.send_adb_command_vm(f"shell shell am kill {p3}", indexNumber) #mozilla

#com.google.android.gms
#com.scopely.monopolygo
#org.mozilla.firefox"

indexValue = getIndexValue()
start_emu(indexValue)

while True:
    sleep(2)
    start_automate(indexValue, "com.scopely.monopolygo", "com.google.android.gms", getBrowserPackage, invite)

