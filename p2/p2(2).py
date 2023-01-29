import random
class human:
    def __init__(self, name='human', jod=none, home=none, car=none):
        self.name=name
        self.jpb = job
        self.home = home
        self.car=car

        self.mony = 100
        self.gladness = 50
        self.satieti = 50

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_gob(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self, day):
        pass

    def is_alive(self):
        pass

    def alive(self, day):
        pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consuption = brand_list[self.brand]['consuption']

    def drive(self):
        if self.strength >0 and self.fuel > self.consuption:
            self.fuel-= self.consuption
            self.strength -= 1
            return True
        else:
            print('опять сламалса телик апять машина сдох')
            return False

class Hause:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Gob:
    def __init__(self,job_list):
        pass

brands_of_car = {
    'BMW':{
        'fuel':100,
        'consuption' : 6,
        'strength': 100
    },
    'shaparoshez': {
        'fuel': 50,
        'consuption': 500,
        'strength': 1000
    },
    'tesa_chiti': {
        'fuel': 0,
        'consuption': 0
        'strength': 50
    }
}





