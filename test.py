import datetime
import os

now = datetime.datetime.today()
print(now)

NAME = os.environ["NAME1"]
print('NAME:{}'.format(NAME))
