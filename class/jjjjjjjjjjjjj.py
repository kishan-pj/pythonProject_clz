
from math import sqrt

def distance(x1,y1,x2,y2):
    """Calculate length of line between two points"""
    dx=x2-x1
    dy=y2-y1
    d=sqrt(dx**2+dy**2)
    print(int(d))


distance(4,6,2,4)
