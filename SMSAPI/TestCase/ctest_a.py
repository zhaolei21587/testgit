# import logging
from Common.log import *


class Test_ab:
    n = 'sms12'
    # logger = logging.getLogger(__name__)
    # globals(logger)

    def startup(self):
        print('startup')

    def teardown(self):
        print('teardown')

    def test_a(self):
        'sms1'
        # logger = Logs()
        name = 'kkk'
        logger.info('你们村里有个姑娘叫小芳222!')
        print('123789877')
        assert 1

    def test_b(self):
        'sms2'
        print('1234')
        logging.warning('这是一个warning')
        assert 1

    def test_c(self):
        'sms3'
        print('1234')
        assert 1

