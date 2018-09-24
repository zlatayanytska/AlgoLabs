class Insect:

    def __init__(self, name, speed, mass,):
        self.name = name
        self.speed = speed
        self.mass = mass

    def __repr__(self):
        return str(self.name)+" "+str(self.speed)+" "+str(self.mass)+" | "
