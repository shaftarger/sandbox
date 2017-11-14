import serial
import binascii

TEST_START      = "#START%"
TEST_DOSOK      = "DOSOK"
TEST_NEXT       = "#NEXT%"
TEST_ERRCODE    = "PASS0000"


def main():
    # ser = serial.Serial('/dev/ttyUSB0', 115200)
    ser = serial.Serial('COM1', 115200)

    print("===========================")
    print("Module Test Start...")
    print("send start")
    ser.write(TEST_START.encode())

    print("receive DOSOK")
    resp = ser.read(len(TEST_DOSOK))
    print("get string:" + resp)

    print("send NEXT")
    ser.write(TEST_NEXT.encode())
    
    print("receive Test Result")
    # print(len(TEST_ERRCODE))
    resp = ser.read(len(TEST_ERRCODE))
    print("get string:" + resp)

    print("send NEXT")
    ser.write(TEST_NEXT.encode())
    
    print("Module Test Done...")
    print("===========================")


if __name__ == '__main__':
    main()
