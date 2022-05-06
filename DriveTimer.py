import time 

isdriving = False
driveSec = 0
driveMin = 0
driveHour = 0

while isdriving == True:
    time.sleep(1)
    driveSec +=1
    if driveSec == 60:
        driveMin += 1
        driveSec = 0
    if driveMin == 60:
        driveHour += 1
        driveMin = 0

    

