from pymemuc import PyMemuc
from time import sleep
memuc = PyMemuc(debug=True)

# list out all vms, get the index of the first one
index = memuc.list_vm_info()[0]['index']
index2 = memuc.list_vm_info()[10]['index']


# start the vm

def start_emu(indexNumber: int):
    memuc.start_vm(index)
    memuc.set_configuration_vm("is_customed_resolution", "1", vm_index=indexNumber)
    memuc.set_configuration_vm("resolution_width", "460", vm_index=indexNumber)
    memuc.set_configuration_vm("resolution_height", "680", vm_index=indexNumber)
    memuc.set_configuration_vm("vbox_dpi", "160", vm_index=indexNumber)
    # set to remember window location
    memuc.set_configuration_vm("start_window_mode", "1", vm_index=indexNumber)

def start_automate(indexNumber: int, p1: str, p2: str, p3: str):
    #memuc.send_adb_command_vm(f"shell pm enable {packageName}", indexNumber)
    memuc.send_adb_command_vm(f"shell pm clear {p1}", indexNumber) #mono
    memuc.send_adb_command_vm(f"shell pm clear {p2}", indexNumber) #ps
    memuc.send_adb_command_vm(f"shell rm -r /sdcard/Android/data/{p1}", indexNumber) #ps
    memuc.send_adb_command_vm(f"shell rm -r /sdcard/Android/data/{p2}", indexNumber) #mono
    sleep(2)
    memuc.send_adb_command_vm(f"shell rm -r /data/data/{p1}/*", indexNumber) #ps
    sleep(5)
    memuc.send_adb_command_vm("shell am start -a android.intent.action.VIEW -d https://s.scope.ly/hVasLShVL20", indexNumber)
    sleep(35)
    memuc.send_adb_command_vm(f"shell am force-stop {p1}", indexNumber) #ps
    memuc.send_adb_command_vm(f"shell am force-stop {p3}", indexNumber) #mono
    memuc.send_adb_command_vm(f"shell shell am kill {p1}", indexNumber) #ps
    memuc.send_adb_command_vm(f"shell shell am kill {p3}", indexNumber) #mozilla

#com.google.android.gms
#com.scopely.monopolygo

start_emu(index2)

while True:
    sleep(2)
    start_automate(index2, "com.scopely.monopolygo", "com.google.android.gms", "org.mozilla.firefox")

