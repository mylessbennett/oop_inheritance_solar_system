class System:
    """ Keeps a list of planets and sums the total mass in solar system """

    def __init__(self):
        self.bodies = []

    def add(self, body):
        self.bodies.append(self)

    def total_mass(self):
        total = 0
        for body in self.bodies:
            total += body.mass
        return total


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


earth = Planet('Earth', 5972000000000000000000000, 24, 365)
earth_moon = Moon('Earth\'s Moon', 73476730900000000000000, 29, 'Earth')
sun = Star('Sun', 1989000000000000000000000000000, 'g-type')
solar_system = System()
solar_system.add(earth)
solar_system.add(earth_moon)
solar_system.add(sun)
# print(solar_system.total_mass())
