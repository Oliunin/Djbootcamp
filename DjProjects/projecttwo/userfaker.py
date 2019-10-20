import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','projecttwo.settings')

import django
django.setup()

import random
from AppTwo.models import My_user
from faker import Faker

fakegen = Faker()
def adduser(N=10):
    for entry in range(N):
        fake_name = fakegen.name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()
        u = My_user.objects.get_or_create(u_name=fake_name,u_lastname=fake_lastname,u_email=fake_email)[0]


if __name__ == '__main__':
    N = int(input('Сколько сгенерировать пользователей?'))
    print('генерирую пользователей')
    adduser(N)
    print('Сгенерировал', N,'пользователей')
