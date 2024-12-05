import pickle


def input_dictionary():
    ch = ""
    dictionary = dict()
    while ch != "n":
        Cid = input("Enter item ID: ")
        name = input("Enter gift name: ")
        cost = int(input("Enter cost: "))

        dictionary[Cid] = [name, cost]

        ch = input("Would you like to add another? (y/n) ")

    return dictionary


def create():
    with open("08.dat", "wb") as file:
        pickle.dump(input_dictionary(), file)


def read():
    with open("08.dat", "rb") as file:
        d = pickle.load(file)
        print(d)


def update():
    with open("08.dat", "rb") as file:
        d = pickle.load(file)

    name = input("Enter the name of the item to update: ")

    for Cid in d:
        if d[Cid][0] == name:
            new_cost = int(input("Enter the new cost: "))
            d[Cid][1] = new_cost
            break
    else:
        print("Item not found")

    with open("08.dat", "wb") as file:
        pickle.dump(d, file)


create()
read()
update()
read()
