import math
#importing math library for math functions

def polar_cartesian(r, angle):
    x = float(r)*math.cos(float(angle)*math.pi/180)     #using math functions calculating x and y
    y = float(r)*math.sin(float(angle)*math.pi/180)
    return [x, y]                                       # returning data where the function is called


def cartesian_polar(x, y):
    r = math.sqrt(math.pow(float(x), 2) + math.pow(float(y), 2))        # using math functions calculate r and angle
    angle = 180*math.atan(float(y)/float(x))/math.pi
    return [r, angle]                                                   #returning data where the function is called


print('1 - for polar to cartsian')
print('2 - for cartesian to polar')
choice = input('Enter choice : ')       # taking input from user
#taking inputs from user

if choice == '1':     # making decision if choice = 1 run function polar_cartesian and print data
    r = input('Enter r : ')
    angle = input('Enter angle : ')
    [x,y] = polar_cartesian(r, angle)
    print('X : '+ str(x))
    print('Y : '+ str(y))

elif choice == '2':     #making decision if choice = 2 run function cartesian_polar and print data
    x = input('Enter X : ')
    y = input('Enter Y : ')
    [r,angle] = cartesian_polar(x, y)
    print('R : '+ str(r))
    print('Angl : ' + str(angle))

else:
    print('wrong choice!!')