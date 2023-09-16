import json

import requests
from bs4 import BeautifulSoup

cookies = {
    'TAUnique': '%1%enc%3A5EPBin1ZXG7VXrMro2Rf4x84Gzgpnir%2BBME5XeeEOhwYvJ58lDKZ6g%3D%3D',
    'TADCID': 'TSfHOnfMvOqAf4taABQCCKy0j55CTpGVsECjuwJMq3g_p2OsfAnKsldbqqxbvVvT9vVqR47kbJ0YfMRHmLacil_ux61AMMkdM4E',
    'TASameSite': '1',
    'TASSK': 'enc%3AAGYWyxiIqINmnRQn3QGDyfqQYIyL0gQi1hMDUrfEKVVWyWWijEXs97cJ1hgg0KUeZowfURjJjvfEA%2B%2BOWi65umqePj70xVUezTfufYeg90lktCJgaAcpUqQEWK4k7ZDOlA%3D%3D',
    'ServerPool': 'A',
    'PMC': 'V2*MS.6*MD.20230916*LD.20230916',
    'TART': '%1%enc%3A1V6zK6NkX%2BOfYZ9XPTWO16Km%2BLF7pvjGavZ27QGshvzibCQc4%2FDNVtR69lN86Jy7TDefwdednzM%3D',
    'TATravelInfo': 'V2*A.2*MG.-1*HP.2*FL.3*RS.1',
    'TASID': '587A7987FCA64FBC81ED1C79C6B117B8',
    '_abck': '6BAC85C7FE26737E448A6FD0FE5EA7D4~-1~YAAQoANJF21v3IaKAQAAjhv8nAqNZj8V/X0L9XO4ZEr3idrgG7tGgBKSVRSfwOAXAowtd7Jv9+CFxLnwgcKhcOpG+ywJaFTnefYUdMPSnGnFSb0xtsIsK9SVMEoiiOBCa4oLHKWuSoDhU6BRPG+OOqqjwH+rBn/rYmJHQHRTMfLukSJwE/YjWqvK6Umy+kDpHOjQnksa8iFMbm/lDu3i2y7C+Xjq6Zl9P6gWEZTaAt7Xr9/x1/mfUJfHbJdPtm/UtEyZDDeR0PhAIcaXgRYY8kW+DWCqmo5pPiQnCfBokwNgSpoTwmvC0KS6jzywOMLYM0ouyYKv60ObdTnWgg4+ye6YjTBam4hd/7TXZiiF5E7zApmxwnI0g6EL9BlK0ipA6g==~-1~-1~-1',
    'bm_sz': 'E4C73D9B449AD3876159499B7F709407~YAAQoANJF25v3IaKAQAAjhv8nBViqZ+ttM8BWtaJVt5GFcsTBOlCMOTJ/2zUp11gMqdLTsdwhMiJw82fVrx+ceqVJt7MK73kDWNYu6XCHfhPpvcQ24limntFRm6GpEbmTAafmbc70GShpuKRVdFKhPirWIhbrWl7wGd+8Arn2ZO08OaQAVZmUQmmv14M70HvNbxZvsq5tXW58/72mqp6/0U54iC4EDoee9HZIVWuHbZBVS/aW/OAMEd9rsPLb4KPVyotFGZuaEr6qealR5RNKR3bLC6lZCvHiNM+CfZ+z099Gqzm830oOw==~3491383~3289157',
    'PAC': 'AHZFw9UmlrJ79nxlpB2bO36WErWqH8kEz1iMLxrGVtDLXMDjT6jV9APErmHBUyA_HHOFgB6B92ydA0CxnUqTdfMzIOQwb9EGgiVEnRMwqmHtR0IAuR0JqEugKJqy1nJYJFMzl-Rw_Zl2L9ToAIWLKDvOEwKsYlnU2THR5NK9D7jadi9RowLoTdzKw5xRNUbhRKkRYiXSW7-gVeGEmDyYsBWlQB_nOqAluSS3l0OE1l4WQ4my_GuWdhSg1tVsXSR4VOw70TaSGql9oDw4FjisS0HRb7OjLbIBj9UTRjhUyQ_yz0aayTI54VIi0H43Z37UQm2R7scDapvxt9-ScL04k2j8jy994Ro4F6Op8yXfTAxv',
    'VRMCID': '%1%V1*id.13091*llp.%2FFindRestaurants%3Fgeo%3D187479%26establishmentTypes%3D10591%252C9909%252C9900%252C11776%252C16556%252C9901%26priceTypes%3D10953%252C10955%252C10954%26broadened%3Dfalse*e.1695455688549',
    'TATrkConsent': 'eyJvdXQiOiIiLCJpbiI6IkFMTCJ9',
    '_pbjs_userid_consent_data': '3524755945110770',
    '_li_dcdm_c': '.tripadvisor.com',
    '_lc2_fpi': 'b140173de591--01haefrdmwcct51m4zyekj3dz0',
    'pbjs_sharedId': 'bd2b46f9-adb8-4deb-a0c6-deab1a040022',
    '_ga_QX0Q50ZC9P': 'GS1.1.1694850889.1.0.1694850889.60.0.0',
    '_ga': 'GA1.1.1465974672.1694850890',
    'TAAUTHEAT': 'E56LR0nlbl9bY-zaABQCobW21V9oR1-Dg22GNw6BiDgWp0jiK_yImTiW7rVtfxd4IovhqCOUz6IoGdkHFgmfxScM4JEjBiUF30nPKjjgyRtIfPyLZ8Tld4qPRDtyYIlyzaFkHt43w22yMXi3iTMuLHLUKVA3OVShRJ8CY5_Sj5T6Bf3CnI1z3BNKXILTCUTBl_IGpk_cQs_KRJPeOjIR2SopRPodRRs81Fj6',
    'TASession': '%1%V2ID.587A7987FCA64FBC81ED1C79C6B117B8*SQ.3*PR.40185%7C*LS.RegistrationController*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.8DD7DC3022D0E1F9CB1FF3FB7B28CE59*FA.1*DF.0*TRA.true*LD.187479*EAU._',
    'TAUD': 'LA-1694850899458-1*RDD-1-2023_09_16*LG-1-2.1.F.*LD-2-.....',
    'datadome': '32OHj9H7wYrMY5ipEaD2KYLWBFO7imcBBbMd~3_EuwFZKMhzyhIm-YJXJT9svLxgPRcx2kKm0iIvGpEWkoeLnhcWTZ_yf26ijdc76BD_r1o3gv4xvvfE1jOIJdYEbodE',
    '__vt': 'FRKwRTgwkBN9UqbAABQCCQPEFUluRFmojcP0P3EgGigdSGHMyA7a_5QXBxApVRVl4Qy9OYhdJ8LJqKjD576S1Wow5CaYS_Lg3JbUAwxHK40lKesynYRQoCcj0U5msS9Mrl4nbk6Xwy_jTjH-6eIGpVAGyA',
    'G_AUTH2_MIGRATION': 'informational',
    'SRT': 'TART_SYNC',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Sep+16+2023+10%3A56%3A14+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=8ef7cde7-f543-4851-acdd-667d9ddfc94f&interactionCount=1&landingPath=https%3A%2F%2Fwww.tripadvisor.com%2FFindRestaurants%3Fgeo%3D187479%26establishmentTypes%3D10591%252C9909%252C9900%252C11776%252C16556%252C9901%26priceTypes%3D10953%252C10955%252C10954%26broadened%3Dfalse&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1',
}

headers = {
    'authority': 'www.tripadvisor.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'TAUnique=%1%enc%3A5EPBin1ZXG7VXrMro2Rf4x84Gzgpnir%2BBME5XeeEOhwYvJ58lDKZ6g%3D%3D; TADCID=TSfHOnfMvOqAf4taABQCCKy0j55CTpGVsECjuwJMq3g_p2OsfAnKsldbqqxbvVvT9vVqR47kbJ0YfMRHmLacil_ux61AMMkdM4E; TASameSite=1; TASSK=enc%3AAGYWyxiIqINmnRQn3QGDyfqQYIyL0gQi1hMDUrfEKVVWyWWijEXs97cJ1hgg0KUeZowfURjJjvfEA%2B%2BOWi65umqePj70xVUezTfufYeg90lktCJgaAcpUqQEWK4k7ZDOlA%3D%3D; ServerPool=A; PMC=V2*MS.6*MD.20230916*LD.20230916; TART=%1%enc%3A1V6zK6NkX%2BOfYZ9XPTWO16Km%2BLF7pvjGavZ27QGshvzibCQc4%2FDNVtR69lN86Jy7TDefwdednzM%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TASID=587A7987FCA64FBC81ED1C79C6B117B8; _abck=6BAC85C7FE26737E448A6FD0FE5EA7D4~-1~YAAQoANJF21v3IaKAQAAjhv8nAqNZj8V/X0L9XO4ZEr3idrgG7tGgBKSVRSfwOAXAowtd7Jv9+CFxLnwgcKhcOpG+ywJaFTnefYUdMPSnGnFSb0xtsIsK9SVMEoiiOBCa4oLHKWuSoDhU6BRPG+OOqqjwH+rBn/rYmJHQHRTMfLukSJwE/YjWqvK6Umy+kDpHOjQnksa8iFMbm/lDu3i2y7C+Xjq6Zl9P6gWEZTaAt7Xr9/x1/mfUJfHbJdPtm/UtEyZDDeR0PhAIcaXgRYY8kW+DWCqmo5pPiQnCfBokwNgSpoTwmvC0KS6jzywOMLYM0ouyYKv60ObdTnWgg4+ye6YjTBam4hd/7TXZiiF5E7zApmxwnI0g6EL9BlK0ipA6g==~-1~-1~-1; bm_sz=E4C73D9B449AD3876159499B7F709407~YAAQoANJF25v3IaKAQAAjhv8nBViqZ+ttM8BWtaJVt5GFcsTBOlCMOTJ/2zUp11gMqdLTsdwhMiJw82fVrx+ceqVJt7MK73kDWNYu6XCHfhPpvcQ24limntFRm6GpEbmTAafmbc70GShpuKRVdFKhPirWIhbrWl7wGd+8Arn2ZO08OaQAVZmUQmmv14M70HvNbxZvsq5tXW58/72mqp6/0U54iC4EDoee9HZIVWuHbZBVS/aW/OAMEd9rsPLb4KPVyotFGZuaEr6qealR5RNKR3bLC6lZCvHiNM+CfZ+z099Gqzm830oOw==~3491383~3289157; PAC=AHZFw9UmlrJ79nxlpB2bO36WErWqH8kEz1iMLxrGVtDLXMDjT6jV9APErmHBUyA_HHOFgB6B92ydA0CxnUqTdfMzIOQwb9EGgiVEnRMwqmHtR0IAuR0JqEugKJqy1nJYJFMzl-Rw_Zl2L9ToAIWLKDvOEwKsYlnU2THR5NK9D7jadi9RowLoTdzKw5xRNUbhRKkRYiXSW7-gVeGEmDyYsBWlQB_nOqAluSS3l0OE1l4WQ4my_GuWdhSg1tVsXSR4VOw70TaSGql9oDw4FjisS0HRb7OjLbIBj9UTRjhUyQ_yz0aayTI54VIi0H43Z37UQm2R7scDapvxt9-ScL04k2j8jy994Ro4F6Op8yXfTAxv; VRMCID=%1%V1*id.13091*llp.%2FFindRestaurants%3Fgeo%3D187479%26establishmentTypes%3D10591%252C9909%252C9900%252C11776%252C16556%252C9901%26priceTypes%3D10953%252C10955%252C10954%26broadened%3Dfalse*e.1695455688549; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; _pbjs_userid_consent_data=3524755945110770; _li_dcdm_c=.tripadvisor.com; _lc2_fpi=b140173de591--01haefrdmwcct51m4zyekj3dz0; pbjs_sharedId=bd2b46f9-adb8-4deb-a0c6-deab1a040022; _ga_QX0Q50ZC9P=GS1.1.1694850889.1.0.1694850889.60.0.0; _ga=GA1.1.1465974672.1694850890; TAAUTHEAT=E56LR0nlbl9bY-zaABQCobW21V9oR1-Dg22GNw6BiDgWp0jiK_yImTiW7rVtfxd4IovhqCOUz6IoGdkHFgmfxScM4JEjBiUF30nPKjjgyRtIfPyLZ8Tld4qPRDtyYIlyzaFkHt43w22yMXi3iTMuLHLUKVA3OVShRJ8CY5_Sj5T6Bf3CnI1z3BNKXILTCUTBl_IGpk_cQs_KRJPeOjIR2SopRPodRRs81Fj6; TASession=%1%V2ID.587A7987FCA64FBC81ED1C79C6B117B8*SQ.3*PR.40185%7C*LS.RegistrationController*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.8DD7DC3022D0E1F9CB1FF3FB7B28CE59*FA.1*DF.0*TRA.true*LD.187479*EAU._; TAUD=LA-1694850899458-1*RDD-1-2023_09_16*LG-1-2.1.F.*LD-2-.....; datadome=32OHj9H7wYrMY5ipEaD2KYLWBFO7imcBBbMd~3_EuwFZKMhzyhIm-YJXJT9svLxgPRcx2kKm0iIvGpEWkoeLnhcWTZ_yf26ijdc76BD_r1o3gv4xvvfE1jOIJdYEbodE; __vt=FRKwRTgwkBN9UqbAABQCCQPEFUluRFmojcP0P3EgGigdSGHMyA7a_5QXBxApVRVl4Qy9OYhdJ8LJqKjD576S1Wow5CaYS_Lg3JbUAwxHK40lKesynYRQoCcj0U5msS9Mrl4nbk6Xwy_jTjH-6eIGpVAGyA; G_AUTH2_MIGRATION=informational; SRT=TART_SYNC; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Sep+16+2023+10%3A56%3A14+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=8ef7cde7-f543-4851-acdd-667d9ddfc94f&interactionCount=1&landingPath=https%3A%2F%2Fwww.tripadvisor.com%2FFindRestaurants%3Fgeo%3D187479%26establishmentTypes%3D10591%252C9909%252C9900%252C11776%252C16556%252C9901%26priceTypes%3D10953%252C10955%252C10954%26broadened%3Dfalse&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1',
    'referer': 'https://kwork.ru/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

params = {
    'geo': '187479',
    'establishmentTypes': '10591,9909,9900,11776,16556,9901',
    'priceTypes': '10953,10955,10954',
    'broadened': 'false',
}


def parse_url():
    count = 0
    urls = []
    for i in range(0, 3664, 30):
        url = f'https://www.tripadvisor.com/FindRestaurants?geo=187479&offset={i}&establishmentTypes=10591%2C9909%2C9900%2C11776%2C16556%2C9901&priceTypes=10953%2C10955%2C10954&broadened=false'

        response = requests.get(url, params=params, cookies=cookies,
                                headers=headers)

        soup = BeautifulSoup(response.content, 'lxml')

        titles = soup.find_all('div', class_='vIjFZ Gi o VOEhq')
        for title in titles:
            url = 'https://www.tripadvisor.com' + title.find('a').get('href')
            urls.append(url)
        count += 1
        print(count)

        with open('urls.txt', 'w', encoding='utf-8') as f:
            for url in urls:
                f.write(f'{url}\n')


def parse_page():
    with open('urls.txt', 'r') as f:
        urls = f.read().split()

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        name = soup.find('h1', class_='HjBfq').text
        print(name)


if __name__ == '__main__':
    # parse_url()
    parse_page()
