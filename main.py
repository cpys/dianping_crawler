# -*- coding:utf-8 -*-

import requests
import json


def main():
    resp = requests.post(url="http://www.dianping.com/search/map/ajax/json",
                         data={
                             'cityId': 224,
                             'cityEnName': 'nanning',
                             'promoId': 0,
                             'shopType': 1,
                             'categoryId': 10,
                             'sortMode': 2,
                             'shopSortItem': 0,
                             'searchType,': 1,
                             'branchGroupId': 0,
                             'aroundShopId': 0,
                             'shippingTypeFilte,rValue': 0,
                             'page': 1,
                             'glong1': 108.3013409255982,
                             'glat1': 22.8306663467147,
                             'glong2': 108.34133802642828,
                             'glat2': 22.792966960083117,
                         },
                         headers={
                             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.18 Safari/537.36'
                         })
    if resp.status_code == 200:
        try:
            content = json.loads(resp.text)
        except Exception as e:
            print(e)
        else:
            shopRecordBeanList = content['shopRecordBeanList']
            # for shopRecordBean in shopRecordBeanList:
            #     addr = shopRecordBean['address']
            #     avgPrice = shopRecordBean['avgPrice']
            #     defaultPic = shopRecordBean['defaultPic']
            print(len(shopRecordBeanList))
            for shopRecordBean in shopRecordBeanList:
                print(shopRecordBean['shopName'])

    print(resp)


if __name__ == "__main__":
    main()
