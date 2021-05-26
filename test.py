import datetime
import os

now = datetime.datetime.today()
print(now)

NAME = os.environ["NAME1"]
print('NAME:{}'.format(NAME))

super_secret = os.environ["super_secret"]
print('super_secret:{}'.format(super_secret))
