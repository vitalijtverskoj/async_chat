import logging
import sys

cli_logger = logging.getLogger('client')

_format = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] > %(message)s')

crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.CRITICAL)
crit_hand.setFormatter(_format)

fh = logging.FileHandler('client.log', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(_format)

cli_logger.addHandler(fh)
cli_logger.addHandler(crit_hand)
cli_logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    console = logging.StreamHandler(sys.stderr)
    console.setLevel(logging.DEBUG)
    console.setFormatter(_format)
    cli_logger.addHandler(console)
    cli_logger.info('Тестовый запуск логирования')
    cli_logger.critical('critical!')
    cli_logger.error('error!')
    cli_logger.warning('warning!')
    cli_logger.info('info!')
    cli_logger.debug('debug!')
