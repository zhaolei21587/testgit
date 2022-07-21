import allure
import pytest

from API.api_login import *
from Common.public_api import *
from Common.yaml_util import *
from Common.log import *


@allure.feature('这里是一级标签')
@pytest.mark.run(order=1)
class TestLogin:
    @allure.story('说明用户场景')
    @pytest.mark.parametrize('caseinfo',read_yaml('data_login.yml'))
    def test_login(self,caseinfo):
        id = caseinfo['caseid']
        logger.info("{}：{}".format(id,caseinfo['name']))
        value, rows = read_excel('testlink_result.xlsx', 'Result')
        rows += 1
        write_excel('testlink_result.xlsx', rows, 1, id)
        url = 'http://127.0.0.1/api/mgr/signin'
        data = caseinfo['params']
        logger.info('连接allure，生成报告')
        with allure.step('登录'):
            s = ApiLogin().aip_post_login(url,data)
        assert s.status_code == caseinfo['codeNo']
        assert s.json() == caseinfo['e']

        


