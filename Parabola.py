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
    contAnalyse = True
    while (contAnalyse):
        analyse: str = input("\nDo you want you want to analyse this parabola? (y,n)")
        if analyse == "y":
            sQuery: float = float(input("\nWhat do you value of horizontal displacement do you want to analyse for?"))
            # if s is bigger than midpoint, find difference and minus from midpoint
            formmattedSQuery = horizontalDisplacement - (sQuery - horizontalDisplacement) if sQuery > horizontalDisplacement else sQuery
            # t = S_x / V_x
            tAtQuery: float = formmattedSQuery / horizontalVelocity
            tAtQuery = (2 * time) - tAtQuery if sQuery > horizontalDisplacement else tAtQuery
            print(f"\nThe parabola at {sQuery}m of horizontal displacment has a time value of {tAtQuery}s")
        else:
            contAnalyse = False


def halfParabola():
    print("If you have variable input it, otherwise input question mark, you must have at least two variables")
    horizontalDisplacement: str = input("\nInput Horizontal Displacment")
    horizontalVelocity: str = input("Input Horizontal Velocity")
    time: str = input("Input time")

    # t = s / v
    time: float = horizontalDisplacement / horizontalVelocity if time == "?" else float(time)
    #  s = vt
    horizontalDisplacement: float = time * horizontalVelocity if horizontalDisplacement == "?" else float(horizontalDisplacement)
    # v = s / t
    horizontalVelocity: float = horizontalDisplacement / time if horizontalVelocity == "?" else float(horizontalVelocity)
    verticalVelocity: float = g * time
    verticalDisplacement: float = (g * (time * time)) / 2

    print("\nGenerating Parabola Info.")
    #time.sleep(1)
    print("Generating Parabola Info..")
    #time.sleep(1)
    print("Generating Parabola Info...")
    #time.sleep(1)
    print(f"\nVertical Final Velocity: {verticalVelocity}m s-1\nVertical Displacement: {abs(verticalDisplacement)}m\nHorizontal Velocity: {horizontalVelocity}m s-1\nHorizontal Displacement: {horizontalDisplacement}m\nTime: {time}s\n")


while True:
    mode: str = input("Half Parabola, Full Parabola (h, f)")

    if mode == "f":
        fullParabola()
    elif mode == "h":
        halfParabola()

# add time at certain displacment and variable inputs