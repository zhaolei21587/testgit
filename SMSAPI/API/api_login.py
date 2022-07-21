'''
    登录接口对象封装
'''

import requests
from Common.log import *



class ApiLogin:

    s = requests.Session()

    def aip_post_login(self,url,data):
        '''
        获取登录API的response响应
        :param url: 登录API地址
        :param data: 请求参数（username，password）
        :return: 登录API的response响应
        '''
        return self.s.post(url,data=data)


    def get_login_cookie(self):
        '''
        登录
        :return: 登录API的sessionid
        '''
        data = {'username': 'byhy', 'password': '88888888'}
        s_login = self.aip_post_login('http://127.0.0.1/api/mgr/signin', data)
        logger.debug('获取登录API的sessionid')
        return s_login.cookies.get_dict()


