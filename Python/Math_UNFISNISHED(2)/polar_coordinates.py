import cmath
import math
import re

def polar_coordinates(z: str):
    """
    Convert complex number into polar coordinates
    print one line representing r
    print antoher line representing angle phi

    ----- PARAMS -----
    z :         string
        string representation of the complex number
        where j is supposed to represent the imaginary part of the number
            ex: z = x + yj
    """
    regex = r"(-?[0-9]*)((?:-|\+)[0-9]*)j"
    matches = re.search(regex, z)

    if not matches:
        return False

    x, y = int(matches.group(1)), int(matches.group(2))

    result = math.sqrt(x**2 + y**2)
    print(result)
    print(cmath.phase(complex(float(x), float(y))))


if __name__ == '__main__':
    z = input()
    polar_coordinates(z)
