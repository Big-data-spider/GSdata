from selenium import webdriver
from numpy import random
from time import sleep
from lxml import etree
import json
import pprint

'''
红盾
'''


def get_content(url):
    '''
    获取页面内容和源码
    :param url:
    :return:
    '''
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Chrome()
    driver.get(url)
    sleep(3)
    content = driver.page_source
    dom = etree.HTML(content)

    driver.close()
    driver.quit()

    return content, dom


def get_true_url(url):
    '''
    获取信息页面地址
    :param url:
    :return:
    '''
    content, dom = get_content(url)
    title = dom.xpath('//h1[@class="title"]/text()')[0]
    print(title)
    t_url = dom.xpath('//div[@class="comment-wrap art-content"]//p/a/@href')
    if len(t_url) == 0:
        t_url = None
    else:
        t_url = t_url[0]
    print(t_url)
    return t_url


def get_infos():
    '''
    红盾信息采集
    :param url:
    :return:
    '''

    fl = open('./work_files/urls_list.json', 'r', encoding='utf-8')
    url_list = json.load(fl)
    fl.close()
    tyc_list = []

    for url in url_list:
        if 'ubaike.cn' in url:
            turl = get_true_url(url)
            if turl != None:
                content, dom = get_content(turl)

                title = dom.xpath('//h1[@class="title"]/text()')[0]
                print(title)

                phone_num = dom.xpath('//p[@class="tel"]/text()')
                if len(phone_num) == 0:
                    phone_num = '未收录'
                else:
                    phone_num = phone_num[0]
                print(phone_num)

                addr = dom.xpath('//p[@class="dizhi"]/text()')
                if len(addr) == 0:
                    addr = '未收录'
                else:
                    addr = addr[0]
                print(addr)

                ow_name = dom.xpath('//*[@id="partners"]/div[2]/text()')[0]
                print(ow_name)

                reg_num = dom.xpath('//*[@id="partners"]/div[3]/div[2]/text()')[0]
                print(reg_num)

                ucc = dom.xpath('//*[@id="partners"]/div[4]/div[2]/text()')[0]
                print(ucc)

                capital = dom.xpath('//*[@id="partners"]/div[5]/div[2]/text()')[0]
                print(capital)

                setup_time = dom.xpath('//*[@id="partners"]/div[5]/div[2]/text()')[0]
                print(setup_time)

                cp_type = dom.xpath('//*[@id="partners"]/div[7]/div[2]/text()')[0]
                print(cp_type)

                bs = dom.xpath('//*[@id="partners"]/div[8]/div[2]/text()')[0]
                print(bs)

                reg_adrs = dom.xpath('//*[@id="partners"]/div[9]/div[2]/text()')[0]
                print(reg_adrs)

                status = dom.xpath('//*[@id="partners"]/div[11]/div[2]/text()')[0]
                print(status)

                time_limit = dom.xpath('//*[@id="partners"]/div[10]/div[2]/text()')[0]
                print(time_limit)

                info_dict = {
                    '公司名': title,
                    '联系电话': phone_num,
                    '法人': ow_name,
                    '地址': addr,
                    '注册资本': capital,
                    '公司状态': status,
                    '工商注册号': reg_num,
                    '统一信用代码': ucc,
                    '公司类型': cp_type,
                    '注册地址': reg_adrs,
                    '经营范围': bs,
                    '当前企业网址': url,
                    '成立日期': setup_time,
                    '营业期限': time_limit,
                    '信息页url': turl
                }

                print('#' * 70 + '\r\n')
                pprint.pprint(info_dict)
                tyc_list.append(info_dict)

                ft = open('./work_files/hd_infos.json', 'w', encoding='utf-8')
                jstr = json.dumps(tyc_list, ensure_ascii=False, indent=4)
                ft.write(jstr)
                ft.close()
                print('#' * 30 + '存储完毕' + '#' * 30)


get_infos()
# url = 'https://www.ubaike.cn/q_978.html'
# get_true_url(url)
