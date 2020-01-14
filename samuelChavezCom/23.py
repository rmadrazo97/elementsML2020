
def findGreatest(name, r):
    file = open(name, r)

    aggregate = 0
    index = 0
    # print(line)

    while True:
        line = file.readline()
        if not line:
            break
        column = line.split()
        print("cc", column)
        try:
            toAdd = max(int(column[index+1]), int(column[index]))
            aggregate += toAdd
            if toAdd == int(column[index+1]):
                index += 1
        except:
            print(column[0])
            aggregate = aggregate + int(column[0])

        print(aggregate, "index:", index)

    file.close
    return aggregate


print(findGreatest('triangle.txt', "r"))
