from django.shortcuts import render
import speedtest
import time
from datetime import datetime
import matplotlib.pyplot as plt

t = time.localtime()
currentTime = time.strftime("%I:%M", t)
currentTimeInMinutes = int(time.strftime("%M", t))
st = speedtest.Speedtest()


def downloadSpeed(request):
    return render(request, 'downloadSpeed/downloadSpeed.html')

def getSpeed():
	downloadSpeed = st.download()
	speed = int(downloadSpeed/8000)
	return speed

def getUpSpeed():
    uploadSpeed = st.upload()
    upSpeed = int(uploadSpeed/8000)
    return upSpeed

def getPing():
    # servernames = []
    # st.get_servers(servernames)
    ping = int(st.results.ping)
    return ping

def getCurrentTime():
	t = time.localtime()
	currentTime = int(time.strftime("%M", t))
	return currentTime

def downloadSpeed(request):
    speedList = []
    timeList = []
    limit = 0
    netSpeed = getSpeed()
    upSpeed = getUpSpeed()
    ping = getPing()

    print(netSpeed)
    # for limit in range(2):
    #     speed = getSpeed()
    #     currentTime = getCurrentTime()
    #     time.sleep(10)
    #     print(limit)
    #     y = speedList.append(speed)
    #     x = timeList.append(currentTime)

    # convertTOJson = str("[{ netSpeed : "+netSpeed+"}]")
    # return
    return render(request, 'downloadSpeed/downloadSpeed.html', {'downloadSpeed' : netSpeed,'uploadSpeed' : upSpeed,'ping' : ping} )
    # print(speedList)
    # print(timeList)
    # plotGraph(timeList, speedList)


def showSpeed(request):
    speedList = []
    timeList = []
    limit = 0
    netSpeed = getSpeed()

    for limit in range(2):
        speed = getSpeed()
        currentTime = getCurrentTime()
        time.sleep(10)
        print(limit)
        y = speedList.append(speed)
        x = timeList.append(currentTime)

    return render(request, 'downloadSpeed/downloadSpeed.html', {'downloadSpeed' : netSpeed} )
