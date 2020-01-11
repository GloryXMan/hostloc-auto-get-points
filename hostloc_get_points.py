import os
import requests
import time
import random


def randomly_gen_uspace_url():
    url_list = []
    # 生成的随机数可能会重复，懒得去重了，多生成几个就行了
    for i in range(15):
        uid = random.randint(10000, 35000)
        url = "https://www.hostloc.com/space-uid-{}.html".format(str(uid))
        url_list.append(url)
    return url_list


def get_points(username, password):
    headers = {
        "User-Angent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }
    url_list = randomly_gen_uspace_url()
    login_url = "https://www.hostloc.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
    login_data = {
        "fastloginfield": "username",
        "username": username,
        "password": password,
    }
    s = requests.Session()
    s.post(url=login_url, data=login_data, headers=headers)
    for url in url_list:
        try:
            s.get(url)
            print("用户空间链接：" + url + " 访问成功")
            time.sleep(2)
        except Exception as e:
            print(e)
        continue


if __name__ == "__main__":
    username = os.environ["HOSTLOC_USERNAME"]
    password = os.environ["HOSTLOC_PASSWORD"]
    get_points(username, password)
