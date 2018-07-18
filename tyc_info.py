from selenium import webdriver
from numpy import random
from time import sleep
from lxml import etree
import json
import pprint

'''
天眼查
'''


def get_page(url):
    '''
    得到页面源码和选择器对象
    :param url:
    :return:
    '''
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Chrome()
    driver.get(url)
    sleep(random.randint(5, 7))
    cks_f = open('./work_files/tyc_cookies.json', 'r')
    cookie = json.load(cks_f)
    for con in cookie:
        driver.add_cookie(con)
    driver.refresh()
    driver.get(url)
    sleep(3)
    content = driver.page_source
    dom = etree.HTML(content)

    driver.close()
    driver.quit()

    return dom, content


def get_infos():
    '''
    1.获取地址列表
    2.判断列表中的元素是否属于天眼查
    3.通过选择器匹配元素
    4.获得元素做成字典入表
    q:查看更多的情况
    :param url:
    :return:
    '''

    fl = open('./work_files/urls_list.json', 'r', encoding='utf-8')
    url_list = json.load(fl)
    fl.close()
    tyc_list = []
    for url in url_list:
        if 'tianyancha' in url:
            print('#' * 70 + '\r\n')
            try:
                pprint.pprint(tyc_list)
                # try:
                dom, content = get_page(url)

                # 公司现用名
                title = dom.xpath('//h1[@class="name"]/text()')[0]
                print(title)

                # 公司曾用名
                old_tilte = dom.xpath('//span[@class="history-content"]/text()')
                if len(old_tilte) == 0:
                    old_tilte = title
                else:
                    old_tilte = old_tilte[0]
                print(old_tilte)

                # 电话
                phone_num = dom.xpath('//div[@class="detail "]/div[1]/div/span[2]/text()')
                if len(dom.xpath('//span[@class="link-click ml10"]/text()')) != 0:
                    phone_num = dom.xpath('//span[@class="pl10"]/script/text()')[0]
                    # print(type(phone_num))
                print(phone_num)

                # 公司网站
                web_url = dom.xpath('//a[@class="company-link"]/@href')
                if len(web_url) != 0:
                    web_url = web_url[0]
                else:
                    web_url = dom.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[5]/div[2]/div[1]/span[2]/text()')[
                        0]
                print(web_url)

                # 地址
                addr = dom.xpath('//span[@class="address"]/@title')
                if len(addr) != 0:
                    addr = addr[0]
                else:
                    addr = '暂无信息'
                print(addr)

                # 简介
                intro = dom.xpath('//div[@class="summary"]/span[2]/text()')[0]
                print(intro)

                # 法人代表
                ow_name = dom.xpath('//div[@class="humancompany"]/div/a/@title')[0]
                ow_info_url = dom.xpath('//div[@class="humancompany"]/div/a/@href')[0]
                print(ow_name)
                print(ow_info_url)

                # 注册资本
                capital = dom.xpath('//*[@id="_container_baseInfo"]/table[1]/tbody/tr[1]/td[2]/div[2]/@title')[0]
                print(capital)

                # 公司状态
                status = dom.xpath('//div[@class="num-opening"]/@title')
                if len(status) != 0:
                    status = status[0]
                else:
                    status = '暂无信息'
                print(status)

                # 注册时间
                # reg_time =

                # 工商注册号
                reg_num = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[1]/td[2]/text()')[0]
                print(reg_num)

                # 组织机构代码
                ocode = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[1]/td[4]/text()')[0]
                print(ocode)

                # 统一信用代码
                ucc = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[2]/td[2]/text()')[0]
                print(ucc)

                # 公司类型
                cp_type = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[2]/td[4]/text()')[0]
                print(cp_type)

                # 纳税人识别号
                tin = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[3]/td[2]/text()')[0]
                print(tin)

                # 所属行业
                industry = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[3]/td[4]/text()')[0]
                print(industry)

                # 纳税人资质
                tq = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[5]/td[2]/text()')[0]
                print(tq)

                # 人员规模
                ss = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[5]/td[4]/text()')[0]
                print(ss)

                # 实缴资本
                pinc = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[6]/td[2]/text()')[0]
                print(pinc)

                # 登记机关
                ra = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[6]/td[4]/text()')[0]
                print(ra)

                # 参保人数
                nop = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[7]/td[2]/text()')[0]
                print(nop)

                # 英文名
                eng_name = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[7]/td[4]/text()')[0]
                print(eng_name)

                # 注册地址
                reg_adrs = dom.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[8]/td[2]/text()')[0]
                print(reg_adrs)

                # 经营范围
                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                driver = webdriver.Chrome(chrome_options=option)
                # driver = webdriver.Chrome()
                driver.get(url)
                sleep(3)
                cks_f = open('./work_files/tyc_cookies.json', 'r')
                cookie = json.load(cks_f)
                for con in cookie:
                    driver.add_cookie(con)
                driver.refresh()
                driver.get(url)
                sleep(3)
                dom2 = etree.HTML(driver.page_source)
                if len(dom2.xpath('//*[@class="js-shrink-container"]')) != 0:
                    if len(dom.xpath('//*[@class="js-full-container hidden"]')) != 0:
                        bs = dom.xpath('//*[@class="js-full-container hidden"]/text()')
                        bs = list(set(bs))
                        # bs = bs.remove('详情')
                    else:
                        bs = '暂无信息'
                else:
                    bs = '暂无信息'
                print(bs)
                # //*[@id="_container_baseInfo"]/table[2]/tbody/tr[9]/td[2]/span/span
                #

                # 工商执照照片
                pic_url = dom.xpath('//a[@class="ripple ml10 link-click"]/@href')
                if len(pic_url) != 0:
                    option = webdriver.ChromeOptions()
                    option.add_argument('headless')
                    driver = webdriver.Chrome(chrome_options=option)
                    driver.get(pic_url[0])
                    sleep(3)
                    cks_f = open('./work_files/tyc_cookies.json', 'r')
                    cookie = json.load(cks_f)
                    for con in cookie:
                        driver.add_cookie(con)
                    driver.refresh()
                    driver.get(pic_url[0])
                    sleep(3)
                    con3 = driver.page_source
                    dom3 = etree.HTML(con3)
                    pic = dom3.xpath('//*[@id="web-content"]/div/div/div[1]/div[2]/img/@src')[0]
                    driver.close()
                    driver.quit()
                else:
                    pic = '未上传'
                print(pic)

                info_dict = {
                    '公司名': title,
                    '曾用名': old_tilte,
                    '联系电话': phone_num,
                    '公司网站': web_url,
                    '法人': ow_name,
                    '地址': addr,
                    '简介': intro,
                    '注册资本': capital,
                    '公司状态': status,
                    '工商注册号': reg_num,
                    '组织机构代码': ocode,
                    '统一信用代码': ucc,
                    '公司类型': cp_type,
                    '纳税人识别号': tin,
                    '所属行业': industry,
                    '纳税人资质': tq,
                    '人员规模': ss,
                    '实缴资本': pinc,
                    '登记机关': ra,
                    '参保人数': nop,
                    '英文名': eng_name,
                    '注册地址': reg_adrs,
                    '经营范围': bs,
                    '法人简介': ow_info_url,
                    '执照实拍': pic,
                    '当前企业网址': url
                }

                print('#' * 70 + '\r\n')
                pprint.pprint(info_dict)
                tyc_list.append(info_dict)
                # tyc_list = list(set(tyc_list))

                ft = open('./work_files/tyc_infos_bak2.json', 'w', encoding='utf-8')
                jstr = json.dumps(tyc_list, ensure_ascii=False, indent=4)
                ft.write(jstr)
                ft.close()
                print('存储完毕')
                print('#' * 70)
            except:
                print('网络出问题了么。。。等一下吧')
                sleep(random.randint(7, 14))

        else:
            print('不是天眼的网站')
            sleep(1)


##########################################

# url = 'https://www.tianyancha.com/company/140777575'
# get_infos(url)
get_infos()
