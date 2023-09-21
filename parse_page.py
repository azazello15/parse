import json
import time

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
driver = uc.Chrome(version_main=117, options=options)
data = []
try:
    driver.get(
        'https://www.tripadvisor.com/Restaurant_Review-g187482-d23943324-Reviews-Quebracho_Asador_Argentino-Santa_Cruz_de_Tenerife_Tenerife_Canary_Islands.html')
    name = driver.find_element(By.CSS_SELECTOR, "[class='HjBfq']").text
    open_now = driver.find_element(By.CSS_SELECTOR, "[class='NehmB']").text
    '''details'''
    details = driver.find_elements(By.CSS_SELECTOR, "[class='SrqKb']")
    price_range = details[0].text
    cusines = details[1].text
    meals = details[2].text
    '''details'''

    '''location and contacts'''
    locs = driver.find_elements(By.CSS_SELECTOR, "[class='kDZhm IdiaP']")
    address = locs[0].text
    location = locs[1].text

    links = driver.find_elements(By.CSS_SELECTOR, "[class='YnKZo Ci Wc _S C FPPgD']")
    geo = links[0].get_attribute('href')
    website = links[1].get_attribute('href')
    phones = driver.find_elements(By.CSS_SELECTOR, "[class='BMQDV _F Gv wSSLS SwZTJ']")
    phone = phones[1].get_attribute('href')
    '''location and cjntacts'''

    '''Rating'''
    rating_num = driver.find_element(By.CSS_SELECTOR, "[class='ZDEqb']").text
    reviews_num = driver.find_element(By.CSS_SELECTOR, "[class='IcelI']").text

    rating = driver.find_elements(By.CSS_SELECTOR, "[class='cNFlb']")
    rating_1 = rating[0].text
    rating_2 = rating[1].text
    '''Rating'''
    loc_links_dict = {
        'Геолокация': geo,
        'Вебсайт': website,
        'Номер телефона': phone
    }
    location_dict = {
        'Адрес': address,
        'Местоположение': location,
        'Способы связи': loc_links_dict
    }
    rating_dict = {
        'Оценка': rating_num,
        'Отзывы': reviews_num,
        'Рейтинг_1': rating_1,
        'Рейтинг_2': rating_2,
    }
    details = {
        'Ценовой диапазон': price_range,
        'КУХНИ': cusines,
        'Еда': meals,
        'Рейтинги и отзывы': rating_dict
    }
    data_dict = {
        'Название': name,
        'Расписание': open_now,
        'Детали': details,
        'Адреса и ссылки': location_dict
    }
    info = {
            'INFO': data_dict
    }
    data.append(info)

    with open('items.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    time.sleep(3)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


if __name__ == '__main__':
    parse_links()
