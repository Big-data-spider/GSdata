from selenium import webdriver
from lxml import etree
import time
import numpy
import json
import random


def qcc_kukis():
    driver = webdriver.Chrome()
    driver.get('https://www.qichacha.com/user_login')
    time.sleep(5)
    driver.find_element_by_link_text('密码登录').click()
    driver.find_element_by_id("nameNormal").send_keys('15939067986')
    driver.find_element_by_id("pwdNormal").send_keys('1231512315')
    time.sleep(15)
    # driver.find_element_by_link_text('立即登录').click()
    # time.sleep(10)
    cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookies = driver.get_cookies()
    cookiestr = ';'.join(item for item in cookie)
    print(cookie)
    print('#' * 70)
    print(cookiestr)

    f = open('./work_files/qcc_cookies.json', 'w')
    f.write(json.dumps(cookies, ensure_ascii=False, indent=4))
    f.close()


def ty_kukis():
    driver = webdriver.Chrome()
    driver.get('https://www.tianyancha.com/search?key=%E7%BD%91%E7%BB%9C')
    time.sleep(5)
    driver.find_element_by_link_text('登录/注册').click()
    time.sleep(2)
    # driver.find_element_by_link_text('账号密码登录').click()
    driver.find_element_by_xpath(
        '//div[@class="modulein modulein2 message_box pl15 pr15 f-base collapse in"]/div[1]').click()
    driver.find_element_by_xpath('//div[@class="pb30 position-rel"]/input').send_keys('15939067986')
    driver.find_element_by_xpath('//div[@class="pb40 position-rel"]/input').send_keys('baby12357')
    time.sleep(15)
    # driver.find_element_by_link_text('立即登录').click()
    # time.sleep(10)
    cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookies = driver.get_cookies()
    cookiestr = ';'.join(item for item in cookie)
    print(cookie)
    print('#' * 70)
    print(cookiestr)

    f = open('./work_files/tyc_cookies.json', 'w')
    f.write(json.dumps(cookies, ensure_ascii=False, indent=4))
    f.close()


# qcc_kukis()
# ty_kukis()

'''
然后又从文件取出cookie，因为取出的时候是字符串形式，然后通过cookie =json.loads(cookie)转为字典，因为取出的cookie，使用通过循环add到driver，然后刷新一下driver就可以了

f1 = open('cookie.txt')
cookie = f1.read()
cookie =json.loads(cookie)
for c in cookie:
    driver.add_cookie(c)
# # 刷新页面
driver.refresh()
'''