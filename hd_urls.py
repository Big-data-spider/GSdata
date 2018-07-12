from selenium import webdriver
from lxml import etree
import time
import numpy
import json
import random


def get_urls():
    '''
    获得名称列表
    通过名称列表搜索天眼
    通过天眼筛选出来的内容得到url
    通过url得到信息
    :return:
    '''
    fc = open('./work_files/urls_list.json', 'r', encoding='utf-8')
    lists = json.load(fc)
    fc.close()

    fd = open('./work_files/company_list1.json', 'r', encoding='utf-8')
    # fd = open('./work_files/company_list.json', 'r', encoding='utf-8')
    com_name = json.load(fd)
    print(com_name)
    random.shuffle(com_name)
    for name in com_name:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=option)
        # driver = webdriver.Chrome()
        driver.get('https://www.ubaike.cn/')
        print('\r\n' + '#' * 30 + '打开了' + '#' * 30)

        # 导入cookies
        cks_f = open('./work_files/hd_cookies.json', 'r')
        cookie = json.load(cks_f)
        for con in cookie:
            driver.add_cookie(con)

        driver.refresh()
        time.sleep(3)

        driver.find_element_by_id("search-kw").send_keys(name)
        elsem_so = driver.find_element_by_xpath('//i[@class="fa fa-search"]')
        elsem_so.click()
        time.sleep(numpy.random.randint(4, 6))
        time.sleep(3)
        contents = driver.page_source
        # print(contents)
        dom = etree.HTML(contents)
        link_u = dom.xpath('//a[@class="title"]/@href')
        for ls in link_u:
            nrl = 'https:' + ls
            print(nrl)
            lists.append(nrl)

        lists = list(set(lists))
        print(lists)

        jstr = json.dumps(lists, ensure_ascii=False, indent=4)
        file = open('./work_files/urls_list.json', 'w', encoding='utf-8')
        file.write(jstr)
        file.close()

        time.sleep(10)

        driver.quit()


get_urls()
