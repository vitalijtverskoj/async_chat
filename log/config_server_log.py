import logging
import sys
from logging import handlers

serv_logger = logging.getLogger('server')

_format = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] > %(message)s')

crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.CRITICAL)
crit_hand.setFormatter(_format)

fh = handlers.TimedRotatingFileHandler('server.log', when='d', interval=1, encoding='utf-8',
                                                        backupCount=5)
fh.setLevel(logging.DEBUG)
fh.setFormatter(_format)

serv_logger.addHandler(fh)
serv_logger.addHandler(crit_hand)
serv_logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    console = logging.StreamHandler(sys.stderr)
    console.setLevel(logging.DEBUG)
    console.setFormatter(_format)
    serv_logger.addHandler(console)
    serv_logger.info('Тестовый запуск логирования')
    serv_logger.critical('critical!')
    serv_logger.error('error!')
    serv_logger.warning('warning!')
    serv_logger.info('info!')
    serv_logger.debug('debug!')
