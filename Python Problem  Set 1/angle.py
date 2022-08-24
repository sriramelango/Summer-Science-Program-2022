# Angle Unit Conversion
# Python Problem Set 1
# 6/24/22
# Sriram Elango

import math

def convertAngle(degrees, minutes, seconds, optRadians, optNormalize):

    if (degrees < 0.0 or degrees == -0.0):
        answer = degrees - (minutes/60) - (seconds/3600)
    else:
        answer = degrees + (minutes/60) + (seconds/3600)

    if (optNormalize):
        if (answer < 0):
            while (answer < 0):
                answer += 360
        if (answer > 360):
            while (answer > 360):
                answer -= 360

    if (optRadians):
        answer = (answer * math.pi)/180

    return answer


# test cases for part a
#print(convertAngle(90, 6, 36)) # should print 90.11
#print(convertAngle(-90, 6, 36)) # should print -90.11
#print(convertAngle(-0.0, 30, 45)) # should print -0.5125

# test cases for part b (uncomment these, comment out previous tests)
#print(convertAngle(90, 6, 36, True)) # should print 1.57271618897
#print(convertAngle(-90, 6, 36, True)) # should print -1.57271618897
#print(convertAngle(90, 6, 36, False)) # should print 90.11
#print(convertAngle(-90, 6, 36, False)) # should print -90.11

# these are the test cases you will demonstrate when getting this homework checked off
# test cases for part c (uncomment these, comment out previous tests)
print(convertAngle(90, 6, 36, False, False)) # should print 90.11
print(convertAngle(90, 6, 36, True, False)) # should print 1.57271618897
print(convertAngle(90, 6, 36, False, True)) # should print 90.11
print(convertAngle(90, 6, 36, True, True)) # should print 1.57271618897
print(convertAngle(-90, 6, 36, False, False)) # should print -90.11
print(convertAngle(-90, 6, 36, True, False)) # should print -1.57271618897
print(convertAngle(-90, 6, 36, False, True)) # should print 269.89
print(convertAngle(-90, 6, 36, True, True)) # should print 4.71046911821
print(convertAngle(540, 0, 0, False, True)) # should print 180.0
print(convertAngle(-0.0, 30, 45, False, False)) # should print -0.5125
