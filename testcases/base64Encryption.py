# -*- coding: utf-8 -*-


"""
文件说明：
	AES加密解密
"""


#导入标准库
import os
import sys
import json
import base64
import binascii
import traceback
import logging as log

#模块路径加入项目搜索路径
project_root_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
module_dir_path = os.path.dirname(os.path.abspath(__file__))
module_dir_name = os.path.split(os.path.dirname(os.path.abspath(__file__)))[-1]
module_name = os.path.split(os.path.abspath(__file__))[-1].replace('.py','')
sys.path.append(module_dir_path)
# print(f"当前模块搜索路径包括：{sys.path}")
import re
import base64



# 返回字符串
def base64_decode(temp):
    """
    base64解码
    :param temp:需要解码的base64字符串
    :return:解码后的字符串
    """
    return str(base64.b64decode(temp.encode("utf-8")), "utf-8")


# 返回字符串
def base64_encode(temp):
    """
    base64编码
    :param temp:需要编码的字符串
    :return:base编码后的字符串

    """

    return str(base64.b64encode(temp.encode('utf-8')), 'utf-8')


def D_base64_decode(temp):
    """
    base64解码：解决base64有等号的问题
    :param temp:需要解码的base64字符串
    :return:解码后的字符串
    """
    temp = temp.replace(",", "+")
    temp = temp.replace(":", "=")
    temp = temp.replace(".", "//")
    temp = bytes(temp, encoding='utf-8')
    dStr = base64.b64decode(temp).decode()
    log.debug("BASE64 Decode result is: \n" + dStr)
    return dStr


def D_base64_encode(temp):
    """
      base64编码：解决base64有等号的问题
      :param temp:需要编码的字符串
      :return:base编码后的字符串

    """
    # temp = bytes(temp,encoding='utf-8')
    eStr = str(base64.b64encode(temp.encode('utf-8')), 'utf-8')
    eStr = eStr.replace(r"+", r",")
    eStr = eStr.replace(r"=", r":")
    eStr = re.sub(r'/', r'.', eStr)

    log.debug("BASE64 encode result is: \n" + eStr)
    return eStr


def Asm_base64_encode(temp):
    """
      base64编码：解决base64有等号的问题
      :param temp:需要编码的字符串
      :return:base编码后的字符串

    """
    # temp = bytes(temp,encoding='utf-8')
    # eStr = str(base64.b64encode(temp.encode('utf-8')), 'utf-8')
    eStr = str(temp)
    eStr = eStr.replace(r"+", r",")
    eStr = eStr.replace(r"=", r":")
    eStr = re.sub(r'/', r'.', eStr)

    log.debug("BASE64 encode result is: \n" + eStr)
    return eStr

def Asm_base64_decode(temp):
    """
    base64解码：解决base64有等号的问题
    :param temp:需要解码的base64字符串
    :return:解码后的字符串
    """
    temp = temp.replace(",", "+")
    temp = temp.replace(":", "=")
    temp = temp.replace(".", "//")
    dStr = temp
    log.debug("BASE64 Decode result is: \n" + dStr)
    return dStr