import pickle


def create():
    f = open("items.dat", "wb")
    f.close()


def write():
    f = open("items.dat", "ab")
    id_ = input("Enter ID: ")
    gift = input("Gift name: ")
    cost = input("Enter cost: ")
    data = [id_, gift, cost]
    pickle.dump(data, f)
    f.close()


def read():
    f = open("items.dat", "rb")
    try:
        while True:
            line = pickle.load(f)
            print(line)
    except EOFError:
        pass


def UPDATEINFO():
    gr = input("Enter the name to update: ")
    f = open("items.dat", "rb")

    lines = []
    try:
        while True:
            line = pickle.load(f)
            lines.append(line)
    except EOFError:
        pass

    gift_names = [line[1] for line in lines]
    index = gift_names.index(gr)

    attribute = int(
        input(
            """
Which attribute would you like to update?
0: ID
1: Gift name
2: Cost

> """
        )
    )
    updated_value = input("What would you like to modify it to?")
    lines[index][attribute] = updated_value

    f.close()

    fil = open("items.dat", "wb")
    for l in lines:
        pickle.dump(l, fil)
    fil.close()


# UNCOMMENT IF YOU ARE RUNNING FOR THE FIRST TIME
# create()
# write()
read()
UPDATEINFO()
read()
