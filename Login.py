# -*- coding: utf-8 -*-


"""
文件说明：
	ASM/ASC管理平台登录方法
"""
#导入标准库
import os
import sys
import json
import datetime
import logging as log


#模块路径加入项目搜索路径
project_root_path = os.path.split(os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0])[0]
module_dir_path = os.path.dirname(os.path.abspath(__file__))
module_dir_name = os.path.split(os.path.dirname(os.path.abspath(__file__)))[-1]
module_name = os.path.split(os.path.abspath(__file__))[-1].replace('.py','')
sys.path.append(module_dir_path)



import urllib3
import requests

from Conf.GlobalConf import GlobalConf
from Common.Encryption.Base64 import base64Encryption
from TestServerCommonOpt.AsmServerComOpt.ManageWeb.ServerBaseOptPy import Pub_rsa_encrypt_api


urllib3.disable_warnings()
# 请求头信息
public_request_fun_config= GlobalConf.GlobalConf().read_public_request_fun_config()
headers=public_request_fun_config['headers']
params=public_request_fun_config['params']


def login(server_ip, login_name, login_password, login_authcode="1234",port="8443"):
    """
    登录ASM/ASC管理平台接口
        用于获取登陆后请求其他接口所需关键信息
    Args:
        server_ip:环境IP
        login_name:登陆用户名
        login_password:登陆用户密码
        login_authcode:验证码
    Returns:字典

    """
    try:
        log.debug(f"请求信息：{server_ip}, {login_name}, {login_password}, {login_authcode}")
        login_url = f'https://{server_ip}:{port}/phpdir/trade.php?tradecode=login&tradetype=normal&mod=default'
        # User-Agent设为空时不启用csrf校验
        login_data = {
            "login": login_name,
            "password": base64Encryption.base64_encode(login_password),
            "authcode": login_authcode
            }
        login_r = requests.post(login_url, headers=headers, data=login_data, verify=False)
        if login_r.status_code!=200:
            raise AssertionError(f"请求登录{server_ip}管理平台失败，响应码：{login_r.status_code},响应内容：{login_r.text}")
        login_res = json.loads(login_r.text)
        log.debug(f"请求登录{server_ip}返回结果{login_res}")
        if "token" not in login_res.keys():
            raise AssertionError(f"请求登录{server_ip}管理平台失败，返回结果:{login_res}")
        return login_res
    except Exception as e:
        raise Exception(f"{sys._getframe().f_code.co_name}报错 ：line {e.__traceback__.tb_lineno}: {e}")




def login_2722(server_ip,account,password,port="8443"):
    """
    2722基线以后管理平台登录方式
    :param server_ip:
    :param login_name:
    :param login_password:
    :param login_authcode:
    :return:
    """
    result = False
    try:
        # RsaPublicKey= Pub_getPublicInfo.get_publice_info(server_ip,port)['AdministratorInfo']['RsaPublicKey']
        # log.debug(f"公钥：\n{RsaPublicKey}")
        request_url = f"https://{server_ip}:{port}/backend/api/login"
        json_data_Mw = {"account": account,
                     "password": password,
                     }

        json_data = Pub_rsa_encrypt_api.encrypt_data(server_ip,json_data_Mw,port)
        # 发送请求
        response = requests.post(url=request_url, headers=headers, params=params, data=json_data, verify=False)

        # 请求结果转换
        response_text = json.loads(response.text)

        # 日志打印：
        log.info(f"请求URL：{response.url}\n\t"
                 f"请求参数：{json_data}\n\t"
                 f"响应码：{response.status_code}\n\t"
                 f"响应结果：{response_text}\n\t")

        # 结果判断
        if response.status_code != 200:
            raise AssertionError(f"登录管理平台失败，响应码非200，响应码是：{response.status_code}")

        result = response_text

    except AssertionError as e:
        raise AssertionError(f"{sys._getframe().f_code.co_name}报错 ：line {e.__traceback__.tb_lineno}: {e}")
    except Exception as e:
        raise Exception(f"{sys._getframe().f_code.co_name}报错 ：line {e.__traceback__.tb_lineno}: {e}")

    return result



if __name__ == '__main__':
    from Log import globalLog

    log_res=login("172.31.88.52", "admin", "888888", "1")
    print(log_res)
