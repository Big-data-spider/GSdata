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
        # option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        # driver = webdriver.Chrome(chrome_options=option)
        driver = webdriver.Chrome()
        driver.get('https://www.qichacha.com/')
        print('\r\n' + '#' * 30 + '打开了' + '#' * 30)

        cks_f = open('./work_files/qcc_cookies.json', 'r')
        cookie = json.load(cks_f)
        for con in cookie:
            driver.add_cookie(con)

        driver.refresh()
        time.sleep(3)

        driver.find_element_by_id("searchkey").send_keys(name)
        elsem_so = driver.find_element_by_id("V3_Search_bt")
        elsem_so.click()
        time.sleep(numpy.random.randint(4, 6))
        elem_city = driver.find_element_by_xpath('//*[@id="prov_box"]/a[4]')
        elem_city.click()
        elem_zhuangtai = driver.find_element_by_xpath('//div[@tyc-event-ch="CompanySearch.Filter.Qiyezhuantai"]')
        elem_zhuangtai.click()
        # elem_sel = driver.find_element_by_xpath('//*[@id="web-content"]/div/div[1]/div/div[1]/div[2]/div[3]/div/div[4]/div[2]/div[3]')
        elem_sel = driver.find_element_by_link_text('存续')
        elem_sel.click()
        time.sleep(3)
        contents = driver.page_source
        # print(contents)
        dom = etree.HTML(contents)
        lists += dom.xpath('//a[@tyc-event-ch="CompanySearch.Company"]/@href')

        lists = list(set(lists))
        print(lists)

        jstr = json.dumps(lists, ensure_ascii=False, indent=4)
        file = open('./work_files/urls_list.json', 'w', encoding='utf-8')
        file.write(jstr)
        file.close()

        time.sleep(10)

        driver.quit()

# get_urls()

# class="tyc-num lh24"
