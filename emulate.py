#!/usr/bin/python
from os.path import isfile, join
import sys
import os

if len(sys.argv) != 4:
    print("emulate.py firmware build_dir package_dir")
    exit()

firmware_name=sys.argv[1]
build_dir=sys.argv[2]
package_dir=sys.argv[3]
bootloader_name=join(build_dir, "bootloader.bin")
partitions_name= join(build_dir, "partitions.bin")
print(firmware_name, build_dir,bootloader_name, partitions_name)
fout=open("esp32flash.bin","wb")
bootloader=open(bootloader_name,"rb").read()
fout.seek(0x1000);
fout.write(bootloader);
partitions=open(partitions_name,"rb").read()
fout.seek(0x8000);
fout.write(partitions);
firmware=open(firmware_name,"rb").read()
fout.seek(0x10000);
fout.write(firmware);
fout.seek(0x3fffff);
fout.write(bytearray([0]));
fout.close();
os.system(join(package_dir,"ttgo-tdisplay-emulator/xtensa-softmmu/qemu-system-xtensa -machine esp32 -drive file=esp32flash.bin,if=mtd,format=raw"))
