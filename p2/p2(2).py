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
        self.home = Hause()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_gob(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
        self.jpb = Job(job_list)

    def eat(self):
        if self.home.food<=0:
            self.shopping('food')
        else:
            if self.satieti > 1

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
        if manage =='fuel':
            print("i bought fuel")
            self.car.fuel +=100
            self.mony -= 100
        elif manage == 'food':
            print("i bought food")
            self.car.food += 50
            self.mony -= 50
        elif manage == 'delicacies'
            self.gladness += 10
            self.satieti +=2
            self.mony -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 10
        self.mony -= 50

    def days_indexes(self, day):
        day = f'today the {day} of {self.name} life'
        print(f'day:=^50')
        print(f'{self.name} indexes')
        print(f'mony - {self.mony}')
        print(f'gladness - {self.gladness}')

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





