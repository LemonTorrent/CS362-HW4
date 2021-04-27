def calcVolume( dimension ):
    volume = (dimension ** 3)
    return volume

measureDimension = input("Enter the length of a side of the cube: ")

volume = calcVolume(float(measureDimension))

print("Cube volume:", volume)
