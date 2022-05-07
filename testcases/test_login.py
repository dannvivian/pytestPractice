import json

import pytest
import requests
import  base64Encryption
import logging
class TestLogin:
    sessionCode =  requests.session()
    def test_getlogin(self):
        asm_host_ip = "172.29.138.20"
        login_admin_user = "admin"
        login_admin_passwd = "888888"
        login_admin_port = 8443
        # 登录管理平台，获取配置信息
        login_url = f'https://{asm_host_ip}:{login_admin_port}/phpdir/trade.php?tradecode=login&tradetype=normal&mod=default'
        # User-Agent设为空时不启用csrf校验
        login_data = {
            "login": login_admin_user,
            "password": base64Encryption.base64_encode(login_admin_passwd),
            "authcode": 1234
        }
        headers = {"User-Agent": "","X-Requested-With":"XMLHttpRequest"}

        # noinspection PyCallingNonCallable
        aa = TestLogin.sessionCode.request("post",login_url, headers=headers, data=login_data, verify=False)
        # 表示这一行跳过代码校验
        if aa.status_code != 200:
            raise AssertionError(f"请求登录{asm_host_ip}管理平台失败，响应码：{aa.status_code},响应内容：{aa.text}")
        login_res = json.loads(aa.text)

        logging.info(f"请求登录{asm_host_ip}返回结果{login_res}")


if __name__ == '__main__':
    pytest.main(['-v', '-s'])