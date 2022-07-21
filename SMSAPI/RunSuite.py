from conftest import *
from Common.pytestlink import *
from Common.public_api import *

if __name__ == '__main__':
    pytest.main()
    # pytest_runtest_makereport(test_a(),call)
    # time.sleep(2)
    # os.system(r"allure generate ./temps -o ./Reports --clean")
    # url = 'http://127.0.0.1:8081/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
    # key = '3192aa2896b90e9ce13220b3d6c3427f'
    # committestlink = TestlinkClient(url, key)
    # value, rows = read_excel('testlink_result.xlsx', 'Result')
    # for item in value:
    #     committestlink.report_test_result(test_case_id=item['caseid'], test_result=item['result'])
