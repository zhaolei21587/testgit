import logging
import datetime

logger = logging.getLogger()
now = datetime.datetime.now()
filename = now.strftime('%Y-%m-%d')

fh = logging.FileHandler(r'.\Log\{}.log'.format(filename),encoding='utf-8')

sh = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s : %(message)s')
formatter1 = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s : %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter1)
logger.addHandler(fh)
logger.addHandler(sh)
logger.setLevel(10)

