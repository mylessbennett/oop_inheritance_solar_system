class System:
    """ Keeps a list of planets and sums the total mass in solar system """

    def __init__(self, bodies):
        self.bodies = []

    def add(self):
        self.bodies.append(self)

    def total_mass(self):
        mass = 0
        for body in self.bodies:
            mass += body.mass


class Body:
    """ Keeps track of celestial bodies """

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass


class Planet(Body):
    """ Represents planets in the solar system """

    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year


class Star(Body):
    """ Represents stars in our solar system """

    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type


class Moon(Body):
    """ Represents moons in our solar system """

    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet
