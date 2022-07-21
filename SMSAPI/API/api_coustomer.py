'''
    客户列表接口对象封装
'''

import requests
from API.api_login import *

class ApiCoustomer:

    s = ApiLogin().s

    def api_get_coustomer(self, url, params):
        '''
        获取客户列表response响应
        :param url: 客户列表API地址
        :param params: 请求参数
        :return: 客户列表的response响应
        '''
        return self.s.get(url,params=params)

    def api_post_addcoustomer(self, url, name,phone,address):
        '''
        添加客户API
        :param url: 添加客户API地址
        :param name: 客户名字
        :param phone: 客户电话
        :param address: 客户地址
        :return: 无
        '''
        data = {"action":"add_customer",
                "data":{
                    "name":name,
                    "phonenumber":phone,
                    "address":address
                    }
                }
        s = self.s.post(url=url,json=data)
        # print(s.content.decode('unicode_escape'))

    def api_delete_coustomer(self, url, id):
        '''
        删除单个客户
        :param url: 删除客户API地址
        :param id: 客户id
        :return: 无
        '''
        data = {"action": "del_customer",
                "id": id
                }
        self.s.delete(url=url,json=data)

    def api_delete_allcoustomer(self,url):
        '''
        删除列表中所有客户
        :param url: 删除客户API地址
        :return: 无
        '''
        params = {'action': 'list_customer','pagesize':'10','pagenum':1,'keywords':""}
        s = ApiCoustomer().api_get_coustomer(url, params)
        msg = s.json()['retlist']
        if len(msg) > 0:
            for i in range(len(msg)):
                idnum = msg[i]['id']
                ApiCoustomer().api_delete_coustomer(url, idnum)
        else:
            pass