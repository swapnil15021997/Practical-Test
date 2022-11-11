speed1 = int(input("Enter the speed of first tortoise: "))
distance = int(input("Enter the distance"))
speed2 = int(input("Enter the speed of Second tortoise: "))

dist1 = distance+(distance/10*2)
dist2 = distance+(distance/2)/5*1


time1 = dist1/speed1

time2 = dist2/speed2

relspeed = speed1+speed2

meet = (dist1+dist2)/relspeed 

print("Distance traveled by first torrtoise:",dist1)
print("Distance traveled by Second torrtoise:", dist2)
print("Time required to first torrtoise:", time1)
print("Time required to Second torrtoise:", time2)
print("Time required to meet two torrtoise:", meet)

