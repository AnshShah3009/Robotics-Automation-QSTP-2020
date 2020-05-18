import math


def polar_cartesian(r, angle):
    x = float(r)*math.cos(float(angle)*math.pi/180)
    y = float(r)*math.sin(float(angle)*math.pi/180)
    return [x, y]


def cartesian_polar(x, y):
    r = math.sqrt(math.pow(float(x), 2) + math.pow(float(y), 2))
    angle = 180*math.atan(float(y)/float(x))/math.pi
    return [r, angle]


print('1 - for polar to cartsian')
print('2 - for cartesian to polar')
choice = input('Enter choice : ')

if choice == '1':
    r = input('Enter r : ')
    angle = input('Enter angle : ')
    [x,y] = polar_cartesian(r, angle)
    print('X : '+ str(x))
    print('Y : '+ str(y))
elif choice == '2':
    x = input('Enter X : ')
    y = input('Enter Y : ')
    [r,angle] = cartesian_polar(x, y)
    print('R : '+ str(r))
    print('Angl : ' + str(angle))
else:
    print('wrong choice!!')
