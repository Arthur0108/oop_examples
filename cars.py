class Car:

    population = 0

    def __init__(self, name):
        self.name = name
        print('Initilizacion {0}'.format(self.name))

        Car.population += 1

    def __del__(self):
        print('We sold', format(self.name))

        Car.population -= 1

        if Car.population == 0:
            print('{0} be the last'.format(self.name))
        else:
            print('We have {0:d} cars'.format(Car.population))

    def howMany():
        print('We have {0:d} cars'.format(Car.population))

    howMany = staticmethod(howMany)

car1 = Car('BMW')
Car.howMany()

car2 = Car('Audi')
Car.howMany()

car3 = ('Mercedes')
Car.howMany()

print('\nWe have the best cars')
print('Sold this cars')

del car1
del car2

Car.howMany()