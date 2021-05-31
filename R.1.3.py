def minmax(data):
    smallest = largest = data[0]
    for entry in data:
        if smallest > entry:
            smallest = entry
        if largest < entry:
            largest = entry
    return (smallest, largest)


print(minmax([0,22,24,4,15,76,89,52,-2,51,3,-4,25,6,-4,-11]))