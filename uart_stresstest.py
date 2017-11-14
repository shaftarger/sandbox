import serial
import binascii
import time

TEST_BOOTDONE   = "boot complete"

def main():
    # ser = serial.Serial('/dev/ttyUSB0', 115200)
    ser = serial.Serial('/dev/ttyS0', 115200)

    print("===========================")
    print("stress Test Start...")

while True:
    ser = serial.Serial('/dev/ttyS0', 115200)
    print("sending bootloader")
    #bootloader =open("/home/arsenechen/home_3/arsene.chen/schubert/imagegenerator/bins/uart_bootimage_250s3_4g32dw_ur0.bin", "rb").read()
    bootloader =open("/home/arsenechen/Project/schubert/imagegenerator/bins/uart_bootimage_266s3_16070732.bin", "rb").read()
    ser.write(bootloader)

    #resp = ser.read(898)
    #print(resp)

    #resp = ser.read(len(TEST_BOOTDONE))
    #print("get string:" + resp)

    time.sleep(5)	#wait uboot reset


if __name__ == '__main__':
    main()
