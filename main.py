with open("./reto.txt") as f:
    data = f.read().replace("\n\n", " ").replace("\n", " ").split("\n")
    print("hóla")
