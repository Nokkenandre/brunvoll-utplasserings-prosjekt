def readvalue(thrustertype):
    import json
    file = open("Thrusters.json")
    data = json.load(file)
    for thruster in data['thrusters']:
        for i in data['thrusters'][thruster]:
            if thrustertype in data['thrusters'][thruster]:
                return data['thrusters'][thruster][thrustertype]['properties']['amount']
    return None
