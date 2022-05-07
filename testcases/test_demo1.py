import json

import pytest
import requests
import Login
import logging
import json
class TestDome:
    def test_S_Asm_Login(self):
        request_url = f"https://{server_ip}:{port}/backend/api/login"
        json_data_Mw = {"account": account,
                        "password": password,
                        }

        json_data = Pub_rsa_encrypt_api.encrypt_data(server_ip, json_data_Mw, port)
        # 发送请求
        response = requests.post(url=request_url, headers=headers, params=params, data=json_data, verify=False)

        # 请求结果转换
        response_text = json.loads(response.text)

        # 日志打印：

        # 结果判断
        if response.status_code != 200:
            raise AssertionError(f"登录管理平台失败，响应码非200，响应码是：{response.status_code}")

        result = response_text


    def test_getCertificate(self):
        url1 = "https://172.29.138.20:8443/phpdir/trade.php"
        datas = {
            "tradecode": "certificate_status",
            "mod": "system_set",
            "tradetype": "normal",
            "login": "admin",
            "cache": 9999,
            "token": "MC3OcY1sUe9cL5"
        }
        res = requests.get(url=url1, params=datas, verify=False)

        ress=res.json()
        # 返回的是字典而不是字符串！！！
        assert ress=={'C': 'CN', 'ST': 'Hunan', 'L': 'Changsha', 'O': 'Infogo', 'OU': 'ASM', 'CN': 'localhost'}

if __name__ == '__main__':
    pytest.main(['-v', '-s'])
