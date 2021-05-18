import datetime
import sys

now = datetime.datetime.today()
print(now)

print('{}个参数'.format(len(sys.argv)))
print('参数列表：{}'.format(str(sys.argv)))
