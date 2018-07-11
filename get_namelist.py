from selenium import webdriver
from lxml import etree
import time
import numpy
import json


def get_source(url):
    '''
    获取页面内容
    :param url:
    :return:
    '''
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    driver.get(url)
    print('\r\n' + '#' * 30 + '打开了' + '#' * 30)
    time.sleep(numpy.random.randint(4, 6))
    texts = driver.page_source
    dom = etree.HTML(texts)
    driver.close()
    driver.quit()
    return dom


def get_names():
    '''
    获取企业名

    :return:
    '''
    url_list = [
        'https://www.atobo.com.cn/Companys/s-p4-c1097/',
        'https://www.atobo.com.cn/Companys/s-p4-c1097-y2/',
        'https://www.atobo.com.cn/Companys/s-p4-c1102/',
        'https://www.atobo.com.cn/Companys/s-p4-c1100/',
        'https://www.atobo.com.cn/Companys/s-p4-c1160-k161729/',
        'https://www.atobo.com.cn/Companys/s-p4-c1160-k161729-y2/',
        'https://www.atobo.com.cn/Companys/s-p4-c1160-k161729-y3/',
        'https://www.atobo.com.cn/Companys/s-p4-c1160-k460451/',
    ]
    name_list = []
    for url in url_list:
        dom = get_source(url)
        name_list += dom.xpath('//li[@class="pp_name"]/a/@title')
        print('\r\n 当前的地址是：%s' % url)
        print(name_list)

    url_list2 = [
        'http://company.kuyiso.com/chongqing/fangdichan-wuyeguanli_26/',
        'http://company.kuyiso.com/chongqing/fangdichan-wuyeguanli_26/page2/',
        'http://company.kuyiso.com/chongqing/fangdichan-wuyeguanli_26/page3/',
        'http://company.kuyiso.com/chongqing/jiudian1_3982/',
        'http://company.kuyiso.com/chongqing/jiudian1_3982/page2/',
        'http://company.kuyiso.com/chongqing/jiudian1_3982/page3/',
        'http://company.kuyiso.com/chongqing/jiudian1_3982/page4/',
        'http://company.kuyiso.com/chongqing/jiudian1_3982/page5/',
        'http://company.kuyiso.com/chongqing/jiudian1_3982/page6/',
        'http://company.kuyiso.com/chongqing/jiudian1_3982/page7/',
        'http://company.kuyiso.com/chongqing/jiudian1_3982/page8/',
        'http://company.kuyiso.com/chongqing/jiudian1_3982/page9/',
        'http://company.kuyiso.com/chongqing/fangdichan_7722/',
        'http://company.kuyiso.com/chongqing/fangdichan_7722/page2/',
        'http://company.kuyiso.com/chongqing/fangdichan_7722/page3/',
        'http://company.kuyiso.com/chongqing/menchuangweixiu_6883/',
        'http://company.kuyiso.com/chongqing/bieshugaizaojiagu_6892/',
        'http://company.kuyiso.com/chongqing/fangchanzhongjie1_6633/'
    ]

    nam_list2 = []
    kys_list = []

    for url in url_list2:
        dom = get_source(url)
        nam_list2 += dom.xpath('//div[@class="compList"]/ul//li//span/a/text()')
        kys_list += dom.xpath('//div[@class="compList"]/ul//li//span/a/@href')
        print('\r\n 当前的地址是：%s' % url)
        print(nam_list2)
        print(kys_list)

    name_list = list(set(name_list + nam_list2))

    return name_list, kys_list


def save_2_file():
    content, kys_list = get_names()
    cont = json.dumps(content, ensure_ascii=False, indent=4)
    fd = open('./work_files/company_list1.json', 'w', encoding='utf-8')
    fd.write(cont)
    fd.close()
    print('企业名处理流程结束')

    fe = open('./work_files/urls_list.json', 'r', encoding='utf-8')
    url_list = json.load(fe)
    url_list += kys_list
    url_list = list(set(url_list))
    fe.close()
    kys_lst = json.dumps(url_list, ensure_ascii=False, indent=4)
    fe = open('./work_files/urls_list.json', 'w', encoding='utf-8')
    fe.write(kys_lst)
    fe.close()
    print('地址列表处理流程结束')

save_2_file()
