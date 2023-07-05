import serial
import time
from enum import Enum
import random

# commands = Enum('command', ['BREAK', 'FOR', 'BACK'])
#define BREAK 0
#define FOR 1
#define BACK 2
#define RIGHT 3
#define LEFT 4


serialcomm = serial.Serial('/dev/ttyUSB0', 9600)
serialcomm.timeout = 1
i=0

while True:
    i = input("Enter Input: ").strip()
    if i == "q":
        print('finished')
        break

    serialcomm.write(i.encode())
    # command = random.randint(0,5)
    # print("round", i, "command", command)
    # serialcomm.write((str(command)).encode())
    time.sleep(0.5)
    print(serialcomm.readline().decode('ascii'))

    # i+=1




serialcomm.close()