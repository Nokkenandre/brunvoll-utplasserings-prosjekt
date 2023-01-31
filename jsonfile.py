def readvalue(name):
    import json as j
    file = open("Thrustere.json")
    data = j.load(file)
    for key, value in data.items():
        if key == name:
            return value
