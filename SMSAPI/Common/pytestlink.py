import testlink
from testlink import TestLinkHelper

url = 'http://127.0.0.1:8081/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
key = '3192aa2896b90e9ce13220b3d6c3427f'



class TestlinkClient:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.tlc = testlink.TestlinkAPIClient(self.url, self.key)

    def get_information_test_project(self):
        self.tlc.listProjects()

    def get_test_plan_by_project(self, testprojectname):
        '''
        通过项目名称获取项目ID，返回数据为项目ID
        通过项目ID获取项目下的所有测试计划，返回的数据格式为包含字典的列表
        字典为每项测试计划的基本数据，如测试计划ID、测试计划名称、是否公共、是否活动等
        :param testprojectname: 项目名称
        :return:以字典格式返回测试计划中的基本数据如测试计划ID、测试计划名称等
        '''
        try:
            project_id = self.tlc.getTestProjectByName(testprojectname)
        except Exception as e:
            print(e)

        try:
            project_test_plans = self.tlc.getProjectTestPlans(project_id)
            return project_test_plans
        except Exception as e:
            print(e)

    def create_test_plan(self,testprojectname=None, testplanname='SMS系统接口自动化测试用例', active=1, public=1):
        '''

        :param testplanname: 测试项目名称
        :param testprojectname: 测试计划名称
        :param active: 活动 可选0或1 0为非活动 1为活动 默认为1
        :param public: 公共 可选0或1 0为非公共 1为公共 默认为1
        :return: 创建状态信息和测试计划ID等信息
        '''
        project_test_plans = self.get_test_plan_by_project(testprojectname)
        exist_plan_list = [x.get('name') for x in project_test_plans]
        if testplanname not in exist_plan_list:
            print('测试计划：{}不存在！'.format(testplanname))

    def get_build_id_by_plan(self, test_plan_name, build_name, testprojectname='接口自动化测试计划'):
        '''

        :param test_plan_name: 测试计划名称
        :param build_name: 版本号
        :param testprojectname: 项目名称
        :return: 包含字典的列表,字典为每个版本的基本信息，如测试计划ID、版本ID、版本名称、是否打开、是否活动等
        '''
        project_test_plans = self.get_test_plan_by_project(testprojectname)
        try:
            for plan in project_test_plans:
                if plan.get('name') == test_plan_name:
                    test_plan_id = plan.get('id')
                    break
        except Exception as e:
            print(e)

        try:
            builds = self.tlc.getBuildsForTestPlan(test_plan_id)
            for build in builds:
                if build.get('name') == build_name:
                    build_id = build.get('id')
                    break
            return build_id
        except Exception as e:
            print(e)

    def report_test_result(self, test_case_id=None, test_result=None, testprojectname='接口自动化测试计划',test_plan_name='SMS系统接口自动测试用例', build_name='SMS_V0.0.2'):
        '''

        :param test_case_id: 测试用例id
        :param test_result: 测试结果，p为通过，f为失败
        :param testprojectname: 测试项目名称
        :param test_plan_name: 测试计划名称
        :param build_name: 测试版本
        :return: 无
        '''
        build_id = self.get_build_id_by_plan(test_plan_name, build_name, testprojectname)
        project_test_plans = self.get_test_plan_by_project(testprojectname)

        for plan in project_test_plans:
            if plan.get('name') == test_plan_name:
                test_plan_id = plan.get('id')
            else:
                pass
        self.tlc.reportTCResult(None, test_plan_id, None, test_result, "", guess=True,
                                testcaseexternalid=test_case_id, platformname="0", buildid=build_id)




if __name__ == '__main__':
    deamo = TestlinkClient(url,key)
    # n = deamo.get_test_plan_by_project('接口自动化测试计划')
    # res = deamo.report_test_result(test_case_id='SMS_-22', test_result='p')
    # print(res)

