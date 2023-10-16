import math
import time

g: float = -9.81

def fullParabola():
    launchVelocity: float = float(input("\nInput Launch Velocity"))
    launchAngle: float = float(input("Input Launch Angle"))

    horizontalVelocity: float = math.cos(launchAngle * (math.pi / 180)) * launchVelocity
    verticalInitialVelocity: float = math.sin(launchAngle * (math.pi / 180)) * launchVelocity
    time: float = abs((0 - verticalInitialVelocity) / g)
    horizontalDisplacement: float = abs(time * horizontalVelocity)
    verticalDisplacement: float = abs((verticalInitialVelocity * time) + ((g * (time * time)) / 2))

    print("\nGenerating Parabola Info.")
    #time.sleep(1)
    print("Generating Parabola Info..")
    #time.sleep(1)
    print("Generating Parabola Info...")
    #time.sleep(1)
    print(f"\nHorizontal Velocity: {horizontalVelocity}m s-1\nHorizontal Displacment: {2 * horizontalDisplacement}m\nVertical Displacment: {verticalDisplacement}m\nVertical Initial Velocity: {verticalInitialVelocity}m s-1\nFull Parabola Time: {time * 2}s\nHalf Parabola Time: {time}s")


def halfParabola():
    horizontalDisplacement: float = float(input("\nInput Horizontal Displacment"))
    horizontalVelocity: float = float(input("Input Horizontal Velocity"))

    time: float = horizontalDisplacement / horizontalVelocity
    verticalVelocity: float = g * time
    verticalDisplacement: float = (g * (time * time)) / 2

    print("\nGenerating Parabola Info.")
    #time.sleep(1)
    print("Generating Parabola Info..")
    #time.sleep(1)
    print("Generating Parabola Info...")
    #time.sleep(1)
    print(f"\nVertical Final Velocity: {verticalVelocity}m s-1\nVertical Displacment: {abs(verticalDisplacement)}m\nTime: {time}s\n")


while True:
    mode: str = input("Half Parabola, Full Parabola (h, f)")

    if mode == "f":
        fullParabola()
    elif mode == "h":
        halfParabola()

# add time at certain displacment and variable inputs