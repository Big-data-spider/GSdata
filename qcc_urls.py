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
    fd.close()
    print(com_name)
    random.shuffle(com_name)
    for name in com_name:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=option)
        # driver = webdriver.Chrome()
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
        # elem_city = driver.find_element_by_xpath('//*[@id="prov_box"]/a[4]')

        elem_comname = driver.find_element_by_link_text('企业名')
        elem_comname.click()
        print('从企业名称查询')
        time.sleep(1)

        contents = driver.page_source
        # print(contents)
        dom = etree.HTML(contents)

        cx = dom.xpath('//a[@data-append="存续"]')
        zc = dom.xpath('//a[@data-append="正常"]')

        bol_nor = False
        bol_ct = False
        bol_cx = False

        if (len(cx) != 0) or (len(zc) != 0):
            if len(cx) == 0 and len(zc) != 0:
                try:
                    elem_nor = driver.find_element_by_xpath('//a[@data-append="正常"]')
                    elem_nor.click()
                    bol_nor = True
                    print('公司状态正常')
                    time.sleep(1)
                except:
                    print('不是正常状态的企业')
                    bol_nor = False
            elif len(zc) == 0 and len(cx) != 0:
                try:
                    elem_buff = driver.find_element_by_xpath('//a[@data-append="存续"]')
                    elem_buff.click()
                    bol_cx = True
                    print('公司状态存续')
                    time.sleep(1)
                except:
                    print('不是存续状态的企业')
                    bol_cx = False
            else:
                try:
                    elem_buff = driver.find_element_by_xpath('//a[@data-append="存续"]')
                    elem_buff.click()
                    bol_cx = True
                    print('公司状态存续')
                    time.sleep(1)
                except:
                    print('不是存续状态的企业')
                    bol_cx = False

            try:
                elem_city = driver.find_element_by_xpath('//a[@data-append="重庆"]')
                elem_city.click()
                bol_ct = True
                print('是重庆的公司')
                time.sleep(1)
            except:
                print('不是重庆的公司')
                bol_ct = False
                com_name.remove(name)

            # 符合要求则获取列表
            if (bol_cx == True) and ((bol_nor == True) or (bol_ct == True)):
                print(name)
                print('符合要求，获取列表')

                contents = driver.page_source
                # print(contents)
                dom = etree.HTML(contents)
                urls = dom.xpath('''//a[@onclick="zhugeTrack('企业搜索-列表-公司名称')"]/@href''')
                print(urls)
                for rl in urls:
                    if 'qichacha' not in rl:
                        nrl = 'https://www.qichacha.com' + rl
                        print(nrl)
                        lists.append(nrl)

                lists = list(set(lists))
                print(lists)

                jstr = json.dumps(lists, ensure_ascii=False, indent=4)
                file = open('./work_files/urls_list.json', 'w', encoding='utf-8')
                file.write(jstr)
                file.close()
                time.sleep(numpy.random.randint(9, 14))
                driver.quit()

            else:
                print(name)
                print('不符合要求，下一个')
                time.sleep(numpy.random.randint(8, 13))
                driver.quit()

        else:
            print(name)
            print('不符合要求，下一个')
            time.sleep(numpy.random.randint(8, 13))
            driver.quit()

    fe = open('./work_files/company_list1.json', 'w', encoding='utf-8')
    jstr = json.dumps(com_name)
    fe.write(jstr)
    fe.close()


get_urls()

# class="tyc-num lh24"
