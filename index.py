from math import sin, cos, radians
from sys import argv


def main():

    #Getting the for in N and the angle in degrees from argv:
    # if not argv[1].isdigit():
    #     print('argumet 1 is not valid, eding process...')
    #     exit()
    # if not argv[2].isdigit(): 
    #     print('argument 2 is not valid, ending process...')
    #     exit()

    # converting from string to float:
    # vectorForce = float(argv[1])
    # vectorAngle = float(argv[2])

    # getting user input through 'input()' function:
    vecForceStr = input("Vector Force: ")
    vecAngleStr = input("Vector Angle: ")

    # converting from string to float:
    vectorForce = float(vecForceStr)
    vectorAngle = float(vecAngleStr)

    # python trigonometic functions defaut to rads, so we need to convert from degrees to rads:
    vectorAngle = radians(vectorAngle)  
    
    # cauculatin the x and y vectors correspondently:
    # sin = OA/tam cos = AA/tam
    vectorX = sin(vectorAngle) * vectorForce
    vectorY = cos(vectorAngle) * vectorForce

    print(f'X for is : {vectorX:.3f}N and Y force is: {vectorY:.3f}N')


if __name__ == '__main__': main()