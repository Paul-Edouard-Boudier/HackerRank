import math

def find_angle(AB: int, BC: int):
    """
    b² = a² + c² − 2ac.cos(β)
    cos(β) = (a² + c² - b²) / 2ac
    β = arccos((a² + c² - b²) / 2ac)

    calculate angle between B and M where M is middle of AC

    - calculate MC
        - calculate AC via pythagorus
        - AC / 2
    """
    if AB is not int or BC is not int:
        return False

    MC = (AB**2 + AC**2)/2

    
    print(angle)



if __name__ == '__main__':
    AB, BC = input(), input()
    find_angle(z)
