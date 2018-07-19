import json
import pprint


def che_qcc():
    '''
    企查查数据筛选
    '''
    fd = open('./work_files/qcc_infos.json', 'r', encoding='utf-8')
    qcc_list = json.load(fd)
    fin_list = []
    str_list = ["[", "]", "\\ufeff", " ", "'"]
    for dits in qcc_list:
        elem_one = dits['登记机关']
        print('#' * 70)
        print(elem_one)
        if '重庆' in elem_one:
            elem_two = dits['经营范围']
            # 住宿 房地产 房屋 家电 日用 酒店 物业 房屋租赁 写字楼 商铺 楼盘 饭店
            if ('房地产' or '住宿' or '房屋' or '家电' or '日用' or '酒店' or '物业' or '房屋租赁' or '写字楼' or '楼盘' or '饭店') in elem_two:
                dits['简介'] = str(dits['简介'])
                for x in str_list:
                    jianjie = dits['简介'].replace(x, '').replace(',,', '').replace('。,', '。')
                    dits['简介'] = jianjie
                fin_list.append(dits)
                print('#' * 70)
                pprint.pprint(fin_list)
    js_list = json.dumps(fin_list, ensure_ascii=False, indent=4)
    fd = open('./work_files/qcc_fin_info.json', 'w', encoding='utf-8')
    fd.write(js_list)
    fd.close()
    print('完工。。齐活')


def che_tyc():
    '''
    天眼查数据筛选
    :return:
    '''
    '''企查查数据筛选'''
    fd = open('./work_files/tyc_infos_bak2.json', 'r', encoding='utf-8')
    qcc_list = json.load(fd)
    fin_list = []
    for dits in qcc_list:
        elem_one = dits['登记机关']
        print('#' * 70)
        print(elem_one)
        if '重庆' in elem_one:
            elem_two = dits['经营范围']
            print(type(elem_two))
            for s in elem_two:
                # 住宿 房地产 房屋 家电 日用 酒店 物业 房屋租赁 写字楼 商铺 楼盘 饭店
                if ('房地产' or '住宿' or '房屋' or '家电' or '日用' or '酒店' or '物业' or '房屋租赁' or '写字楼' or '楼盘' or '饭店') in s:
                    fin_list.append(dits)
                    print('#' * 70)
                    pprint.pprint(fin_list)
    js_list = json.dumps(fin_list, ensure_ascii=False, indent=4)
    fd = open('./work_files/tyc_fin_info.json', 'w', encoding='utf-8')
    fd.write(js_list)
    fd.close()
    print('完工。。齐活')


def main():
    che_qcc()
    # che_tyc()


main()
