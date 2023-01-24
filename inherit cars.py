class Cars:
    def __init__(self, brand, year, engine):
        self.brand = brand
        self.year = year
        self.engine = engine
        print('Like the car: {0}'.format(self.brand))

    def info(self):
        print('We have car: {0}, Year: {1}, Engine: {2}, '.format(self.brand, self.year, self.engine), end=' ')

class Italia(Cars):
    def __init__(self, brand, year, engine, turbine):
        Cars.__init__(self, brand, year, engine)
        self.turbine =turbine
        print('Bought a car from an Italian car dealer: {0}'.format(self.brand))

    def info(self):
        Cars.info(self)
        print('Turbine: "{0:s}"'.format(self.turbine))


class Japan(Cars):
    def __init__(self, brand, year, engine, armor):
        Cars.__init__(self, brand, year, engine)
        self.armor = armor
        print('Bought a car from a Japanese car dealer: {0}'.format(self.brand))

    def info(self):
        Cars.info(self)
        print('Armor: "{0:s}"'.format(self.armor))


class Herman(Cars):
    def __init__(self, brand, year, engine, pnevmo):
        Cars.__init__(self, brand, year, engine)
        self.pnevmo = pnevmo
        print('Bought a car from a Herman car dealer: {0}'.format(self.pnevmo))

    def info(self):
        Cars.info(self)
        print('Pnevmo: "{0:s}"'.format(self.pnevmo))


i = Italia('Maserati', 2019, 3000, 'Super')
j = Japan('Lexus', 2020, 5700, 'B7')
h = Herman('Audi', 2021, 6000, 'Full')
print()

bestcars = [i, j, h]
for bs in bestcars:
    bs.info()