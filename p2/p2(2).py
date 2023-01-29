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
        if not self.car.drive():
            if self.car.fuel < 20 :
                self.shopping('fuel')
            else:
                self.to_repair()
        self.mony += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satieti -= 4



    def shopping(self):
        if not self.car.drive:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()

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
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

job_list = {
    'cleaner':{
        'salary': 20,
        'gladness_less': 20
    },
    'teacher': {
        'salary': 20,
        'gladness_less': 30
    },
    'traider': {
        'salary': 60,
        'gladness_less': 5
    }
}

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





