class Fighters:

    population = 0

    def __init__(self, name):
        self.name = name
        print('Identification {0}'.format(self.name))

        Fighters.population += 1

    def __del__(self):
        print('{0} retired'.format(self.name))

        Fighters.population -= 1

        if Fighters.population == 0:
            print('{0} be the last'.format(self.name))
        else:
            print('We have {0:d} fighters'.format(Fighters.population))

    def sayhi(self):
        print('Hello people! My name is {0}'.format(self.name))

    def howMany():
        print('We have {0:d} fighters'.format(Fighters.population))

    howMany = staticmethod(howMany)

fighter1 = Fighters('Fedor Emilianenko')
fighter1.sayhi()
Fighters.howMany()

fighter2 = Fighters('John Jons')
fighter2.sayhi()
Fighters.howMany()

fighter3 = Fighters('Francis Nganue')
fighter3.sayhi()
Fighters.howMany()

fighter4 = Fighters('Stipe Miocic')
fighter4.sayhi()
Fighters.howMany()

fighter5 = Fighters('Israel Adesania')
fighter5.sayhi()
Fighters.howMany()

print('\nIn this place fighters can fight\n')
print('\nfighters ended their careers\n')
del fighter1
del fighter2
del fighter3
del fighter4
del fighter5

Fighters.howMany()