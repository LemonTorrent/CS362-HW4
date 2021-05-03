def calcVolume( dimension ):
    # error handle input
    print("-----------------------------------------")
    if ((type(dimension) != int) and type(dimension) != float):
        return -1
    print("pass, input:", dimension)

    volume = (dimension ** 3)
    print("volume:", volume)

    #print("volume")
    return volume
