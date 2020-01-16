import math
def volume(R,H):
    v= math.pi*pow(R,2)*H
    return v

print(volume(1,1))

def cone(R,H):
    v=math.pi*pow(R,2)*(H/3)
    return v

print(cone(1,1))
