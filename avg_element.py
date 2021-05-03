def list_avg( element_list ):
    print("input:", element_list)
    if (len(element_list) == 0):
        return 0

    sum = 0
    for i in range(len(element_list)):
        sum += element_list[i]

    avg = sum / len(element_list)

    print("avg:", avg)
    return avg
