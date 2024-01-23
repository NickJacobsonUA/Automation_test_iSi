import random

from data.data import Gen_Data
from faker import Faker


fake = Faker('en_US')  # data generation
Faker.seed()


def generated_data():
    yield Gen_Data(
        firstname='Autotester',
        lastname=fake.last_name(),
        full_name=fake.name() + " " + fake.last_name() + " " + fake.name(),
        username=f'Auto{fake.user_name()}',
        default_passenger='TESTER PASSENGERSON',
        group_owner='ownerson9',
        age=random.randint(10, 80),
        department=fake.job(),
        id_number=f'Auto{random.randint(10000, 100000)}',
        email=fake.email(),
        address=fake.street_address(),
        address_buffalo='1500 Broadway, Buffalo, NY 14212, USA',
        mobile=fake.msisdn(),
        password='000000',
        universal='autotest',
        year=random.randint(1995, 2023),
        company=f'Auto{fake.company()}'
    )


def generated_file():
    path = rf'D:\Downloads\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World {random.randint(0, 999)}')
    file.close()
    return file.name, path



