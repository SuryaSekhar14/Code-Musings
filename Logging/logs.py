import logging

logging.basicConfig(filename='logs.log', filemode="w", level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

logger.info('Start of program')
logger.debug('Failed to load user')
