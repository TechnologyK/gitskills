import datetime
import os
import logging.config

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    logging.config.fileConfig('logging.conf')
    now = datetime.datetime.today()
    logging.info(now)

    logging.info(os.environ)
    # NAME = os.environ["NAME"]
    # logging.info('NAME:{}'.format(NAME))

    # super_secret = os.environ["super_secret"]
    # logging.info('super_secret:{}'.format(super_secret))
