# Import the time library to make the program sleep 1 second
import time

# INPUT - START
# Ask the user to set the timer to both minutes and seconds
setTime = input("What do you want to set the timer to? (minutes:seconds - ##:##) ")

# CHECK SYNTAX - SELECTION
# The IF statement ensures the user doesn't input the incorrect syntax/numbers
if not setTime[0].isdecimal() or not setTime[1].isdecimal() or not setTime[3].isdecimal() or not setTime[4].isdecimal() or int(setTime[3]) > 5 and int(setTime[4]) >= 0:
    print("Error: Wrong syntax!")
    quit()

# PREPARATION - SEQUENCING
# These set the total minutes and seconds, which is then converted into integers
minutes = setTime[0] + setTime[1]
minutes = int(minutes)
seconds = setTime[3] + setTime[4]
seconds = int(seconds)
# Everything is added together in seconds so the program can countdown in the total amount of seconds
timer = (minutes * 60) + seconds

# LOOP - ITERATION
# This while loop is the main part of the actual timer. The while loop only ends once the timer has reached 0 (loops the timer when not 0)
while timer != 0:
    # These add zeros before the numbers just to make the design consistant
    addZeroSec = ''
    addZeroMin = ''
    # These converts the total seconds back down to minutes and seconds so it can be displayed
    timerMin = int(timer / 60)
    timerSec = int(timer % 60)
    # These IF statements checks if the value needs to have a 0 in front of it or not. (Not necessary but makes it look better)
    if timerSec < 10:
        addZeroSec = 0
    elif timerSec == 0:
        addZeroSec = 0
    if timerMin < 10:
        addZeroMin = 0
    elif timerMin == 0:
        addZeroMin = 0
    # This actually prints the time, while it is counting down
    print(str(addZeroMin) + str(timerMin) + ":" + str(addZeroSec) + str(timerSec))
    # This is the actual code that waits 1 second before proceeding
    time.sleep(1)
    # Making sure the timer goes after waiting 1 second
    timer -= 1

# OUTPUT - END
# Tells the user it is done when completed
print("Done!!!")