import pytest

from API.api_coustomer import *
from Common.yaml_util import *


class TestCoustomer:

    url = "http://127.0.0.1/api/mgr/customers"

    def test_nosessioncoustomer(self):
        params = {'action': 'list_customer','pagesize':'10','pagenum':1,'keywords':""}
        s = requests.get(self.url,params=params)
        print("用例名称：未登录时列出客户")
        print('msg:',s.json())


    @pytest.mark.parametrize('caseinfo', read_yaml('data_nocoustomer.yml'))
    def test_unusualcoustomers(self,caseinfo):#,caseinfo
        ApiCoustomer().api_delete_allcoustomer(self.url)
        params = caseinfo['params']
        res = ApiCoustomer().api_get_coustomer(self.url,params)
        print("用例名称：", caseinfo['name'])
        print('response is:',res.json())
        assert caseinfo['e'] == res.json()



    def test_addcoustomers(self):
        for i in range(0,10):
            name = "武汉市桥西医院_" + str(i)
            phone = "1334567993" + str(i)
            address = "武汉市桥西医院北路_" + str(i)
            ApiCoustomer().api_post_addcoustomer(self.url,name,phone,address)

    @pytest.mark.parametrize('caseinfo', read_yaml('data_coustomers.yml'))
    def test_coustomers(self,caseinfo):
        params = caseinfo['params']
        res = ApiCoustomer().api_get_coustomer(self.url, params)
        print("用例名称：", caseinfo['name'])
        # for i in range(len(res.json()['retlist'])):
        #     result = set(res.json()['retlist'][i].items())
        #     expectreslut = set(caseinfo['e'][i].items())
        #     if expectreslut.issubset(result):
        #         testresult = True
        #     else:
        #         testresult = False
        # assert res.status_code == caseinfo['codeNo']
        # assert testresult == True