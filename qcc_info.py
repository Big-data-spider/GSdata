from selenium import webdriver
from numpy import random
from time import sleep
from lxml import etree
import json
import pprint

'''
企查查
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
    cks_f = open('./work_files/qcc_cookies.json', 'r', encoding='utf-8')
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
    2.判断列表中的元素是否属于企查查
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
        if 'qichacha' in url:
            # url = 'https://www.qichacha.com/firm_3f603703d59a04cbe427e5825099a565.html'

            print('#' * 70 + '\r\n')
            # try:
            pprint.pprint(tyc_list)
            # try:
            dom, content = get_page(url)

            # 公司现用名
            title = dom.xpath('//*[@id="company-top"]/div[1]/div[2]/div[1]/h1/text()')
            title_n = dom.xpath('//*[@id="company-top"]/div[1]/div[2]/div[1]/text()')
            if len(title) != 0:
                title = title[0].replace(' ', '').replace('\n', '')
            elif len(title_n) != 0:
                title = title_n[0].replace(' ', '').replace('\n', '')
            print(title)

            # 公司曾用名
            old_tilte = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[8]/td[2]/text()')
            if len(old_tilte) == 0:
                old_tilte = title
            else:
                old_tilte = '-'
            print(old_tilte)

            # 电话
            phone_num = dom.xpath('//*[@id="company-top"]/div[1]/div[2]/div[2]/span[2]/span/text()')
            if len(phone_num) != 0:
                phone_num = dom.xpath('//*[@id="company-top"]/div[1]/div[2]/div[2]/span[2]/span/text()')[0]
                # print(type(phone_num))
            else:
                phone_num = '暂无'
            print(phone_num)

            # 公司网站
            web_url = dom.xpath('//*[@id="company-top"]/div[1]/div[2]/div[2]/span[3]/a[1]/@href')
            if len(web_url) != 0:
                web_url = web_url[0]
            else:
                web_url = '暂无'
            print(web_url)

            # 邮箱
            email = dom.xpath('//*[@id="company-top"]/div[1]/div[2]/div[3]/span[1]/span[2]/a/text()')
            if len(email) == 0:
                email = '暂无'
            else:
                email = email[0]
            print(email)

            # 地址
            addr = dom.xpath('//a[@data-original-title="查看地址"]/text()')
            if len(addr) != 0:
                addr = addr[0].replace(' ', '').replace('\n', '')
            else:
                addr = '暂无'
            print(addr)

            # 简介
            intro = dom.xpath('//div[@class="m-t-sm m-b-sm"]//text()')
            if len(intro) == 0:
                intro = '暂无'
            else:
                intro = intro
            print(intro)

            # 法人代表

            ow_name = dom.xpath('//a[@class="bname"]/text()')
            ow_info_url = dom.xpath('//a[@class="bname"]/@href')
            if len(ow_name) != 0:
                if 'qichacha' not in ow_info_url:
                    ow_info_url = 'https://www.qichacha.com' + ow_info_url[0]
                    ow_name = ow_name[0]
                else:
                    ow_name = '未收录'
                    ow_info_url = '未收录'

            print(ow_name)
            print(ow_info_url)

            # 注册资本
            capital = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[1]/td[2]/text()')
            if len(capital) == 0:
                capital = '未收录'
            else:
                capital = capital[0].replace(' ', '').replace('\n', '')
            print(capital)

            # 公司状态
            status = dom.xpath('///*[@id="Cominfo"]/table[2]/tbody/tr[2]/td[2]/text()')
            if len(status) != 0:
                status = status[0].replace(' ', '').replace('\n', '')
            else:
                status = '暂无信息'
            print(status)

            # 注册时间
            reg_time = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[6]/td[2]/text()')
            if len(reg_time) == 0:
                reg_time = '未收录'
            else:
                reg_time = reg_time[0].replace(' ', '').replace('\n', '')
            print(reg_time)

            # 成立时间
            setup_time = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[2]/td[4]/text()')
            if len(setup_time) == 0:
                setup_time = '未收录'
            else:
                setup_time = setup_time[0].replace(' ', '').replace('\n', '')
            print(setup_time)

            # 工商注册号
            reg_num = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[4]/td[2]/text()')
            if len(reg_num) == 0:
                reg_num = "未收录"
            else:
                reg_num = reg_num[0].replace(' ', '').replace('\n', '')
            print(reg_num)

            # 组织机构代码
            ocode = dom.xpath('///*[@id="Cominfo"]/table[2]/tbody/tr[4]/td[4]/text()')
            if len(ocode) == 0:
                ocode = '未收录'
            else:
                ocode = ocode[0].replace(' ', '').replace('\n', '')
            print(ocode)

            # 统一信用代码
            ucc = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[3]/td[2]/text()')
            if len(ucc) == 0:
                ucc = '未收录'
            else:
                ucc = ucc[0].replace(' ', '').replace('\n', '')
            print(ucc)

            # 公司类型
            cp_type = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[5]/td[2]/text()')
            if len(cp_type) == 0:
                cp_type = '未收录'
            else:
                cp_type = cp_type[0].replace(' ', '').replace('\n', '')
            print(cp_type)

            # 纳税人识别号
            tin = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[3]/td[4]/text()')
            if len(tin) == 0:
                tin = '未收录'
            else:
                tin = tin[0].replace(' ', '').replace('\n', '')
            print(tin)

            # 所属行业
            industry = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[5]/td[4]/text()')
            if len(industry) == 0:
                industry = '未收录'
            else:
                industry = industry[0].replace(' ', '').replace('\n', '')
            print(industry)

            # 人员规模
            ss = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[9]/td[2]/text()')
            if len(ss) == 0:
                ss = '未收录'
            else:
                ss = ss[0].replace(' ', '').replace('\n', '')
            print(ss)

            # 实缴资本
            pinc = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[1]/td[4]/text()')
            if len(pinc) == 0:
                pinc = '未收录'
            else:
                pinc = pinc[0].replace(' ', '').replace('\n', '')
            print(pinc)

            # 登记机关
            ra = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[6]/td[4]/text()')
            if len(ra) == 0:
                ra = '未收录'
            else:
                ra = ra[0].replace(' ', '').replace('\n', '')
            print(ra)

            # 参保人数
            nop = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[8]/td[4]/text()')
            if len(nop) == 0:
                nop = '未收录'
            else:
                nop = nop[0].replace(' ', '').replace('\n', '')
            print(nop)

            # 英文名
            eng_name = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[7]/td[4]/text()')

            if len(eng_name) == 0:
                eng_name = '未收录'
            else:
                eng_name = eng_name[0].replace(' ', '').replace('\n', '')
            print(eng_name)

            # 注册地址
            reg_adrs = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[10]/td[2]/text()')
            if len(reg_adrs) == 0:
                reg_adrs = '未收录'
            else:
                reg_adrs = reg_adrs[0].replace(' ', '').replace('\n', '')
            print(reg_adrs)

            # 经营范围
            bs = dom.xpath('//*[@id="Cominfo"]/table[2]/tbody/tr[11]/td[2]/text()')
            if len(bs) == 0:
                bs = '未描述'
            else:
                bs = bs[0].replace(' ', '').replace('\n', '')
            print(bs)

            # 工商执照照片
            pic_url = dom.xpath('//*[@id="Cominfo"]/div[1]/a/@href')
            if len(pic_url) != 0:
                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                driver = webdriver.Chrome(chrome_options=option)
                driver.get('https://www.qichacha.com' + pic_url[0])
                sleep(3)
                cks_f = open('./work_files/qcc_cookies.json', 'r', encoding='utf-8')
                cookie = json.load(cks_f)
                for con in cookie:
                    driver.add_cookie(con)
                driver.refresh()
                driver.get('https://www.qichacha.com' + pic_url[0])
                sleep(3)
                con3 = driver.page_source
                dom3 = etree.HTML(con3)
                pic = dom3.xpath('//*[@id="download-snapshoot"]/@href')[0]
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
                '人员规模': ss,
                '实缴资本': pinc,
                '登记机关': ra,
                '参保人数': nop,
                '英文名': eng_name,
                '注册地址': reg_adrs,
                '经营范围': bs,
                '法人简介': ow_info_url,
                '执照实拍': pic,
                '当前企业网址': url,
                '邮箱': email,
                '注册时间': reg_time,
                '成立日期': setup_time
            }

            print('#' * 70 + '\r\n')
            pprint.pprint(info_dict)
            tyc_list.append(info_dict)
            # tyc_list = list(set(tyc_list))

            ft = open('./work_files/qcc_infos.json', 'w', encoding='utf-8')
            jstr = json.dumps(tyc_list, ensure_ascii=False, indent=4)
            ft.write(jstr)
            ft.close()
            print('存储完毕')
            # except:
            #     print('网络出问题了么。。。等一下吧')
            #     sleep(random.randint(7, 14))

        else:
            print('不是企查查的地址')
            sleep(1)


##########################################

# url = 'https://www.tianyancha.com/company/140777575'
# get_infos(url)
get_infos()
