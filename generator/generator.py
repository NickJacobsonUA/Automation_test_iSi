#lesson 4.1
import random

from data.data import Person
from faker import Faker


fake = Faker('en_US') # data generation
Faker.seed()

def generated_person():
    yield Person(
        firstname= 'Auto',
        lastname= fake.last_name(),
        full_name=fake.name() + " " + fake.last_name() + " " + fake.name(),
        username=f'Auto_{fake.user_name()}',
        age=random.randint(10,80),
        department=fake.job(),
        salary=random.randint(10000,100000),
        email = fake.email(),
        address = fake.street_address(),
        address_buffalo = '1500 Broadway, Buffalo, NY 14212, USA',
        mobile=fake.msisdn(),
        password='000000'
    )

def generated_file():
    path = rf'D:\Downloads\filetest{random.randint(0,999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World {random.randint(0,999)}')
    file.close()
    return file.name, path # возращаем имя файла через метод file.name