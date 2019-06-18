#Andrew McLaughlin
#28Oct18
#SysLog

import re;

def readFile():
    input = open("C:\\Users\student\Desktop\sysLog.txt", "r")

    exeCount = illegalCount = guestCount = 0

    exeTest = re.compile("exe")
    illegalTest = re.compile("illegal")
    guestTest = re.compile("guest")

    for line in input:
        if(exeTest.findall(line)):
            exeCount += 1
            print(line)
        elif(illegalTest.findall(line)):
            illegalCount += 1
            print(line)
        elif (guestTest.findall(line)):
            guestCount += 1
            print(line)

    print("exe found " + str(exeCount))
    print("illegal found " + str(illegalCount))
    print("guest found " + str(guestCount))

readFile()
