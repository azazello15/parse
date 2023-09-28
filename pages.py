import json

import requests
from bs4 import BeautifulSoup

cookies = {
    'TASameSite': '1',
    'TAUnique': '%1%enc%3ARqJZljp%2F4CYtfvhPrqC0KgxICkpx%2BIlXScW4XgZMFBQ2jHwltRJPGQ%3D%3D',
    'TASSK': 'enc%3AADHo0XKXwwDYs8hVvQr%2BnjJ3pIfe2mV65iEboxr8GIHGWnTt3HJ5NZXqI1UnZGT65qRl%2B1CqcBZ2vw5jp28jxaMC67jo%2B9mBwGXMII90VcYadSK1nsmPAcV2Xvx5bCqcNQ%3D%3D',
    'TATravelInfo': 'V2*A.2*MG.-1*HP.2*FL.3*RS.1',
    '_pbjs_userid_consent_data': '3524755945110770',
    '_lc2_fpi': 'b140173de591--01harzbzfzdtw2gxdwrjwrd9ha',
    'pbjs_sharedId': 'aa1b7c15-e377-4461-96de-247c5af2bd52',
    '_ga': 'GA1.1.1966254062.1695202804',
    '_ga_QX0Q50ZC9P': 'GS1.1.1695309896.5.0.1695309896.60.0.0',
    'TART': '%1%enc%3ALX74T66gtCr7H68CV0GdO1Lo6q3GeCJnSE0gwu%2B4tXaZgqESQWtWhVchvGwYAZ5LjcUVV%2FjQ5bY%3D',
    'TADCID': 'SAxTKUpsch1HVGVdABQCCKy0j55CTpGVsECjuwJMq3iDT461rTbolTvQIt7J-KwdDvic5dM3vuEMuxUq9cHT3sdzvLNzcETTJtE',
    'TAAUTHEAT': 'ytXP6rfs_3qaGj5BABQCobW21V9oR1-Dg22GNw6BiDhaT-x1ykjkuqD8VjsCjhG2A2rnKeBntFmahe3FKYlkuemC5n93itq33SWqR4ARDL5so2IP9ODoKSkzWM4mVO3KRVJ9_XFKVdIOunmkcUFn_XS4iLjkJ99i59OiW_aFoVii5dwt6tIlNdinrBd6A8AZSWJy2geAWL9rN6P9BvtjSR2cO13HL_unBV5M',
    '__vt': '6BWEpV7m53q3RcQ0ABQCCQPEFUluRFmojcP0P3EgGihg701WRLevyj7T3PLYbiKpoErUMhDyfJTL0tIHg8r89LDCpn6rvv1M_Lu11loEtbS67-qp9pE8lQUMizFDLex6U602bGqqooMG8VI95kq06iPyWbPNfVf5vrhkJLteQHRC_ywCmRgYaxEcLw-QSlAZoSj7sUfAriRB66C_qBlcSYTmH3O4eLrE-7FKPjMA1yPSkk8Zyh-DzeqJuQZsox2CQ1d64LKvUPSw0KtmT_YmYow8mzFtPiXaNk-vkV-T33lbGqBijmp_v45lvc1HeCnFOkUYNNCztW1PUKpUufsv6aF7ynQTYyQpC5iS8Di8TjZyJTVxxOtonQ58_Q3_WmlpODQ3oL3UKMNHDGpIgw47SMKbyuFuKzPRCUWUCyWKJMXCT53S9Gh7RrEXwZnHDOmg1kNuIovDaT1c8-FUGg',
    'PAC': 'APypYAn7uexR8yBSK3RPNqzsEuO4wYNiAFRHy94X4FUPOPAUD-Kx7IW3CUKKO8RfkPnv9CdkEcmok6nQ8-DfoE5vyAe-D4Uu-tqiJ68LnC2aUhec_grsTvtzEGG1KJpohw9hnkHB4qzIZgSQIZ3WCZcy40V1b21vQiyeGIcqw5LU4YVa1r07lVAZGBpOcT02fepQKZMNfNVAeip6IMqIke2EPDl_11E1apegmVSUmLyxyNIOJt9nuYKyPG0MS3617yjHWDSsk-WtQ48tvnIjcos%3D',
    'SRT': 'TART_SYNC',
    'ServerPool': 'T',
    'PMC': 'V2*MS.41*MD.20230920*LD.20230928',
    'TASID': '7B548DA6BECF4B07B18CDC3CD9FF9C0B',
    'TAReturnTo': '%1%%2FRestaurant_Review-g662606-d21153255-Reviews-McGuires_Irish_Bar-Costa_Adeje_Adeje_Tenerife_Canary_Islands.html',
    '_abck': '1541154A1CE06BCB3D2A7D8F8C9DB52B~-1~YAAQRc8ti8k6zNaKAQAAF3bs2grX5WHgK6U/j5SoCbzRG7S6tyhiDpPsXojV2dIt3Iky7dHJ+ya1QCJ2wAJ/ThkNz6GLgDmKnUAhKcXNI+gVoLTjMUWft0y/RBboIBiEFPQHlmuz8wnq+JnwuvD23ZOlmXxCs8ilWwU6Bk5FRcOr9tX3htzvmX7KCFHqxlWrGFo8HPY7pkL9sOOBjFGLHs+tG04ms8bdWSTunYykgido/hyw3IoISrc7fbaGiq3fTKTgw6sfexukDFRsfte2EXXetyRxx0uODsQqVm9Xmr4NQ63d7Vbe3wwCmg0lcXdTKKqhS/vv9epGaqGxLHm7DxPrLhNwzD/RIpqye+Jgb3BqLX3ZKEQ8MBQG1Uyz6GyEsZtDzhXf1ASoEQj96D2J~-1~-1~-1',
    'bm_sz': '5937B2D7507D887E14FD8D5431197682~YAAQRc8ti8o6zNaKAQAAF3bs2hVNnFUbUI3bcS6B3LxHGHdUWHaFNkYHAK25cr0UkEQUk/eEKStvGpWuPjncO9dyYoBGbMhrR3k/0kfdith/88keRxvvsP/pxb63y6LZAQotY9qVvAQSc0KC4TRw0+E+6Rt7Gocbjf1v3vTsiqWkOHf2t/2p03QAp2F6yzEozAkzcD4p8/G2vcVZCqf5mPXnZMSLn9KhSaXOP8ypjyskdSHHP2YteFW67iY8TMQglsLuGKvngyFGfObneCi1eCfGUxe2ZIdVgebvCSkKmtwrRem4/5+opA==~4473913~4468786',
    'roybatty': 'TNI1625!AMYSD4A4PvDK725lXGJvRLtAKm2V9hL7myCwS5htYLoVJ%2F6eKKP8rX7zDoqcZ7s6P8I9S5ckOMc%2FGtvwprQHHnVPJ3L516NDRREz%2BnBoLCudYQgiBCu8yNBIAFojJmZ5PCCohcz21nX5JYh9eVocHB1VMVAgHRwAaBqRZRYgsx7C%2C1',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Sep+28+2023+11%3A37%3A11+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=8DD7DC3022D0E1F9CB1FF3FB7B28CE59&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
    'TASession': '%1%V2ID.7B548DA6BECF4B07B18CDC3CD9FF9C0B*SQ.7*LS.DemandLoadAjax*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.8DD7DC3022D0E1F9CB1FF3FB7B28CE59*LF.en*FA.1*DF.0*TRA.false*LD.21153255*EAU.%27',
    'TAUD': 'LA-1695202688223-1*RDD-1-2023_09_20*LG-687426683-2.1.F.*LD-687426684-.....',
    'TATrkConsent': 'eyJvdXQiOiIiLCJpbiI6IkFMTCJ9',
    'datadome': '5l8A-vQKZQHJrPwMYRdFdnQO8piDI~L9z5lSZguVJs1oyGa4LrtFIq~u6TXtw9C7HO9qwUdTLKhclb_QajhEY3Rx2DHOhmXPz9UasY25heRNoyPUKb86G80lZR_Xl9mS',
}

headers = {
    'authority': 'www.tripadvisor.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'TASameSite=1; TAUnique=%1%enc%3ARqJZljp%2F4CYtfvhPrqC0KgxICkpx%2BIlXScW4XgZMFBQ2jHwltRJPGQ%3D%3D; TASSK=enc%3AADHo0XKXwwDYs8hVvQr%2BnjJ3pIfe2mV65iEboxr8GIHGWnTt3HJ5NZXqI1UnZGT65qRl%2B1CqcBZ2vw5jp28jxaMC67jo%2B9mBwGXMII90VcYadSK1nsmPAcV2Xvx5bCqcNQ%3D%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; _pbjs_userid_consent_data=3524755945110770; _lc2_fpi=b140173de591--01harzbzfzdtw2gxdwrjwrd9ha; pbjs_sharedId=aa1b7c15-e377-4461-96de-247c5af2bd52; _ga=GA1.1.1966254062.1695202804; _ga_QX0Q50ZC9P=GS1.1.1695309896.5.0.1695309896.60.0.0; TART=%1%enc%3ALX74T66gtCr7H68CV0GdO1Lo6q3GeCJnSE0gwu%2B4tXaZgqESQWtWhVchvGwYAZ5LjcUVV%2FjQ5bY%3D; TADCID=SAxTKUpsch1HVGVdABQCCKy0j55CTpGVsECjuwJMq3iDT461rTbolTvQIt7J-KwdDvic5dM3vuEMuxUq9cHT3sdzvLNzcETTJtE; TAAUTHEAT=ytXP6rfs_3qaGj5BABQCobW21V9oR1-Dg22GNw6BiDhaT-x1ykjkuqD8VjsCjhG2A2rnKeBntFmahe3FKYlkuemC5n93itq33SWqR4ARDL5so2IP9ODoKSkzWM4mVO3KRVJ9_XFKVdIOunmkcUFn_XS4iLjkJ99i59OiW_aFoVii5dwt6tIlNdinrBd6A8AZSWJy2geAWL9rN6P9BvtjSR2cO13HL_unBV5M; __vt=6BWEpV7m53q3RcQ0ABQCCQPEFUluRFmojcP0P3EgGihg701WRLevyj7T3PLYbiKpoErUMhDyfJTL0tIHg8r89LDCpn6rvv1M_Lu11loEtbS67-qp9pE8lQUMizFDLex6U602bGqqooMG8VI95kq06iPyWbPNfVf5vrhkJLteQHRC_ywCmRgYaxEcLw-QSlAZoSj7sUfAriRB66C_qBlcSYTmH3O4eLrE-7FKPjMA1yPSkk8Zyh-DzeqJuQZsox2CQ1d64LKvUPSw0KtmT_YmYow8mzFtPiXaNk-vkV-T33lbGqBijmp_v45lvc1HeCnFOkUYNNCztW1PUKpUufsv6aF7ynQTYyQpC5iS8Di8TjZyJTVxxOtonQ58_Q3_WmlpODQ3oL3UKMNHDGpIgw47SMKbyuFuKzPRCUWUCyWKJMXCT53S9Gh7RrEXwZnHDOmg1kNuIovDaT1c8-FUGg; PAC=APypYAn7uexR8yBSK3RPNqzsEuO4wYNiAFRHy94X4FUPOPAUD-Kx7IW3CUKKO8RfkPnv9CdkEcmok6nQ8-DfoE5vyAe-D4Uu-tqiJ68LnC2aUhec_grsTvtzEGG1KJpohw9hnkHB4qzIZgSQIZ3WCZcy40V1b21vQiyeGIcqw5LU4YVa1r07lVAZGBpOcT02fepQKZMNfNVAeip6IMqIke2EPDl_11E1apegmVSUmLyxyNIOJt9nuYKyPG0MS3617yjHWDSsk-WtQ48tvnIjcos%3D; SRT=TART_SYNC; ServerPool=T; PMC=V2*MS.41*MD.20230920*LD.20230928; TASID=7B548DA6BECF4B07B18CDC3CD9FF9C0B; TAReturnTo=%1%%2FRestaurant_Review-g662606-d21153255-Reviews-McGuires_Irish_Bar-Costa_Adeje_Adeje_Tenerife_Canary_Islands.html; _abck=1541154A1CE06BCB3D2A7D8F8C9DB52B~-1~YAAQRc8ti8k6zNaKAQAAF3bs2grX5WHgK6U/j5SoCbzRG7S6tyhiDpPsXojV2dIt3Iky7dHJ+ya1QCJ2wAJ/ThkNz6GLgDmKnUAhKcXNI+gVoLTjMUWft0y/RBboIBiEFPQHlmuz8wnq+JnwuvD23ZOlmXxCs8ilWwU6Bk5FRcOr9tX3htzvmX7KCFHqxlWrGFo8HPY7pkL9sOOBjFGLHs+tG04ms8bdWSTunYykgido/hyw3IoISrc7fbaGiq3fTKTgw6sfexukDFRsfte2EXXetyRxx0uODsQqVm9Xmr4NQ63d7Vbe3wwCmg0lcXdTKKqhS/vv9epGaqGxLHm7DxPrLhNwzD/RIpqye+Jgb3BqLX3ZKEQ8MBQG1Uyz6GyEsZtDzhXf1ASoEQj96D2J~-1~-1~-1; bm_sz=5937B2D7507D887E14FD8D5431197682~YAAQRc8ti8o6zNaKAQAAF3bs2hVNnFUbUI3bcS6B3LxHGHdUWHaFNkYHAK25cr0UkEQUk/eEKStvGpWuPjncO9dyYoBGbMhrR3k/0kfdith/88keRxvvsP/pxb63y6LZAQotY9qVvAQSc0KC4TRw0+E+6Rt7Gocbjf1v3vTsiqWkOHf2t/2p03QAp2F6yzEozAkzcD4p8/G2vcVZCqf5mPXnZMSLn9KhSaXOP8ypjyskdSHHP2YteFW67iY8TMQglsLuGKvngyFGfObneCi1eCfGUxe2ZIdVgebvCSkKmtwrRem4/5+opA==~4473913~4468786; roybatty=TNI1625!AMYSD4A4PvDK725lXGJvRLtAKm2V9hL7myCwS5htYLoVJ%2F6eKKP8rX7zDoqcZ7s6P8I9S5ckOMc%2FGtvwprQHHnVPJ3L516NDRREz%2BnBoLCudYQgiBCu8yNBIAFojJmZ5PCCohcz21nX5JYh9eVocHB1VMVAgHRwAaBqRZRYgsx7C%2C1; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+28+2023+11%3A37%3A11+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=8DD7DC3022D0E1F9CB1FF3FB7B28CE59&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; TASession=%1%V2ID.7B548DA6BECF4B07B18CDC3CD9FF9C0B*SQ.7*LS.DemandLoadAjax*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.8DD7DC3022D0E1F9CB1FF3FB7B28CE59*LF.en*FA.1*DF.0*TRA.false*LD.21153255*EAU.%27; TAUD=LA-1695202688223-1*RDD-1-2023_09_20*LG-687426683-2.1.F.*LD-687426684-.....; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; datadome=5l8A-vQKZQHJrPwMYRdFdnQO8piDI~L9z5lSZguVJs1oyGa4LrtFIq~u6TXtw9C7HO9qwUdTLKhclb_QajhEY3Rx2DHOhmXPz9UasY25heRNoyPUKb86G80lZR_Xl9mS',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.289", "YaBrowser";v="23.7.5.734"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.734 Yowser/2.5 Safari/537.36',
}


def parse_pages(url):
    r = requests.get(url=url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    data_list = []
    try:
        name = soup.find('h1', class_='HjBfq').text

        rating = soup.find('div', class_='YDAvY R2 F1 e k')
        rating_num = rating.find('span', class_='ZDEqb').text.strip()
        reviews_num = rating.find('a', class_='IcelI').text
        rating_text = rating.find('div', class_='cNFlb').text
        raiting_dict = {
            'Оценка': rating_num,
            'Количество отзывов': reviews_num,
            'Рейтинг': rating_text
        }

        location_contact = soup.find_all('div', class_='IdiaP')
        address = location_contact[0].text
        location = location_contact[1].text
        location_dict = {
            'Адрес': address,
            'Локация': location
        }

        images_list = []
        images = soup.find_all('div', class_='prw_rup prw_common_basic_image photo_widget mini landscape')
        for image in images:
            images_list.append(image.find_next('img').get('data-lazyurl'))
        items_dict = {
           'Название': name,
           'Рейтинг': raiting_dict,
           'Местоположение': location_dict,
           'Медиа': images_list
        }
        data = {
            '[INFO]': items_dict
        }
        data_list.append(data)
        with open('items.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    with open('urls.txt') as f:
        urls = f.readlines()
    count = 0
    for url in urls:
        parse_pages(url)
        count += 1
        print(f'[INFO] Обработалась {count}-я страница из {len(urls)}. Текущая - {url}')
