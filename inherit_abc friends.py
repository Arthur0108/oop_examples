from abc import  *


class People(metaclass=ABCMeta):
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
        print('We have a friend {0}'.format(self.name))

    @abstractmethod
    def info(self):
        print('Name is {0}, age {1}, hobby {2}, '.format(self.name, self.age, self.hobby), end=' ')

class Artur(People):
    def __init__(self, name, age, hobby, job):
        People.__init__(self, name, age, hobby)
        self.job = job
        print('Friend: {}'.format(self.name))

    def info(self):
        People.info(self)
        print('Job: "{0:s}"'.format(self.job))


class Leha(People):
    def __init__(self, name, age, hobby, car):
        People.__init__(self, name, age, hobby)
        self.car = car
        print('Friend: {}'.format(self.name))

    def info(self):
        People.info(self)
        print('Car: "{0:s}"'.format(self.car))


class Dima(People):
    def __init__(self, name, age, hobby, gun):
        People.__init__(self, name, age, hobby)
        self.gun = gun
        print('Friend: {}'.format(self.name))

    def info(self):
        People.info(self)
        print('Gun: "{0:s}"'.format(self.gun))


a = Artur('Artur Gai', 32, 'IT', 'Military')
l = Leha('Alexey Kap', 32, 'Phisic', 'Skoda')
d = Dima('Dmitriy Ad', 33, 'Cars', 'AK')
print()

friends = [a, l, d]
for f in friends:
    f.info()