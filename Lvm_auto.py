import pyfiglet
import os

os.system("tput setaf 2")
result = pyfiglet.figlet_format("LVM AUTOMATION")
print(result)
os.system("tput setaf 4")
print("\t =====================================")
print("\t = 1. create physical volume         =")
print("\t =====================================")
print("\t = 2. create volume group            =")
print("\t =====================================")
print("\t = 3. create Logical volume          =")
print("\t =====================================")
print("\t = 4. create a partition Dynamically =")
print("\t =====================================")
print("\t = 5. increase partition size        =")
print("\t =====================================")
print("\t = 6. increase volume group size     =")
print("\t =====================================")

user_input=int(input("enter the service you want to use"))

if user_input==1:
    print("\t please enter the drive name to attach")
    device_name=input("\t enter your device name")
    os.system("pvcreate {}".format(device_name))
    print("\t +++++++++++++++++++++++++++++++++++")
    print("\t + your physical volume is created +")
    print("\t +++++++++++++++++++++++++++++++++++")
elif user_input==2:
    device_name = input("\t enter the device name ")
    vg_name=input("\t enter the volume group name ")
    os.system("vgcreate {} {}".format(vg_name,device_name))
    print("\t ++++++++++++++++++++++++++++++++++")
    print("\t +   The volume group is created  +")
    print("\t ++++++++++++++++++++++++++++++++++")
elif user_input==3:
    size=int(input("\t Enter the size of drive"))
    lv_name=input("\t Enter Volume group name")
    vg_name=input("\t Enter the volume group name")
    os.system("lvcreate --size {}G --name {} {}".format(size,lv_name,vg_name))
    print("\t +++++++++++++++++++++++++++++++++")
    print("\t +  Logical volume is created    +")
    print("\t +++++++++++++++++++++++++++++++++")
elif user_input==4:
    print("\t Attach a new harddisk")
    device_name=input("Enter the device name")
    os.system("pvcreate {}".format(device_name))
    print("\t Your physical volume is created")
    vg_name=input("Enter the volume group name ")
    os.system("vgcreate {} {}".format(vg_name,device_name))
    print("Your group is created ")
    size=int(input("Enter the size you want"))
    lv_name = input("Enter the name of the volume you want to make")
    os.system("lvcreate --size {}G --name {} {}".format(size,lv_name,vg_name))
    dir = input("\t Enter the name of the directory to be the mount point")
    os.system("mount /{}/{}/{} /{}".format(vg_name,lv-name,dir))
    print("\t+++++++++++++++++++++++++++++++++++++++")
    print("\t+ Dynamic Partition has been created  +")
    print("\t+++++++++++++++++++++++++++++++++++++++")

elif user_input==5:
    vg_name =input("Enter the volume group name :")
    lv_name =input("Enter the name of the volume you want to make")
    size=int(input("Enter the amount of size you want to increase"))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+\t new size has been added to your logical volume +")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
elif user_input==6:
    vg_name=input("Enter the volume group name")
    print("Attach a new harddisk")
    device_name("pvcreate {}".format(device_name))
    os.system("vgextend {} {}".format(vg_name,device_name))

    
    
