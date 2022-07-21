import yaml


# 读取yaml文件
def read_yaml(yaml_Name):
    with open(r'.\Data\{}'.format(yaml_Name), encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


# 写入yaml文件
def write_yaml(data):
    with open('E:\SMS_API\Data\LoginSeesion1.yml', encoding='utf-8', mode='a') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 清空yaml文件
def clear_yaml(path):
    with open( 'E:\SMS_API\Data\{}'.format(path), encoding='utf-8', mode='w') as f:
        f.truncate()

