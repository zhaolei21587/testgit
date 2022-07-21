import pytest
from Common.public_api import *
from _pytest import runner
from _pytest.runner import runtestprotocol
from _pytest.runner import pytest_runtest_makereport
from TestCase.ctest_a import *

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):

    print("------------------------Start---------------------------")
    out = yield  # 钩子函数的调用结果
    res = out.get_result()  # 获取用例执行结果
    print("执行结果：{}".format(res))
    # if res.when == "call":  # 只获取call用例失败时的信息
    #      print("测试用例：{}".format(res.nodeid))
        # print("用例描述：{}".format(item.function.__doc__))
        # print("测试步骤：{}".format(call))
        # print("用例失败异常信息：{}".format(call.excinfo))
        # print("用例失败时的详细日志：{}".format(res.longrepr))

    value,rows = read_excel('testlink_result.xlsx','Result')

    testcaseresult = res.outcome
    if testcaseresult == 'passed':
        testcaseresult = 'p'
    elif testcaseresult == 'failed':
        testcaseresult = 'f'
    write_excel('testlink_result.xlsx', rows, 2, testcaseresult)


    print("------------------------End---------------------------")



