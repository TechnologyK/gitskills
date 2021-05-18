import datetime
import os

now = datetime.datetime.today()
print(now)

NAME = os.environ["NAME"]
print('NAME:{}'.format(NAME))
