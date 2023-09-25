import json
import random
import time

import undetected_chromedriver as uc
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')


def get_data():
    driver = uc.Chrome(version_main=117, options=options)
    data = []
    with open('urls.txt') as file:
        urls = file.readlines()
    count = 0
    try:
        for url in urls:
            driver.get(url)

            try:
                name = driver.find_element(By.CSS_SELECTOR, "[class='HjBfq']").text
            except Exception as ex:
                name = None

            '''details'''
            details = driver.find_elements(By.CSS_SELECTOR, "[class='SrqKb']")
            try:
                price_range = details[0].text
            except IndexError:
                price_range = None
            try:
                cusines = details[1].text
            except IndexError:
                cusines = None
            try:
                meals = details[2].text
            except IndexError:
                meals = None

            '''details'''

            '''media'''
            photos_list = []
            photos = driver.find_elements(By.CSS_SELECTOR, "[class='basicImg']")
            try:
                if photos:
                    for photo in photos:
                        photos_list.append(photo.get_attribute('src'))
                else:
                    return None
            except StaleElementReferenceException:
                photos_list = []

            ''''media'''

            '''location and contacts'''
            locs = driver.find_elements(By.CSS_SELECTOR, "[class='kDZhm IdiaP']")
            address = locs[0].text

            links = driver.find_elements(By.CSS_SELECTOR, "[class='YnKZo Ci Wc _S C FPPgD']")
            try:
                geo = links[0].get_attribute('href')
            except IndexError:
                geo = None
            try:
                website = links[1].get_attribute('href')
            except IndexError:
                website = None

            phones = driver.find_elements(By.CSS_SELECTOR, "[class='BMQDV _F Gv wSSLS SwZTJ']")
            try:
                phone = phones[1].get_attribute('href')
            except IndexError:
                phone = None
            '''location and contacts'''

            '''Rating'''
            try:
                rating_num = driver.find_element(By.CSS_SELECTOR, "[class='ZDEqb']").text
            except IndexError:
                rating_num = None
            try:
                reviews_num = driver.find_element(By.CSS_SELECTOR, "[class='IcelI']").text
            except IndexError:
                reviews_num = None
            try:
                rating = driver.find_element(By.CSS_SELECTOR, "[class='cNFlb']").text
            except IndexError:
                rating = None
            '''Rating'''
            loc_links_dict = {
                'Геолокация': geo,
                'Вебсайт': website,
                'Номер телефона': phone
            }
            location_dict = {
                'Адрес': address,
                'Способы связи': loc_links_dict
            }
            rating_dict = {
                'Оценка': rating_num,
                'Отзывы': reviews_num,
                'Рейтинг': rating,
            }
            details = {
                'Ценовой диапазон': price_range,
                'КУХНИ': cusines,
                'Еда': meals,
                'Рейтинги и отзывы': rating_dict
            }
            data_dict = {
                'Название': name,
                'Медиа': photos_list,
                'Детали': details,
                'Адреса и ссылки': location_dict
            }
            info = {
                'INFO': data_dict
            }
            data.append(info)
            count += 1
            print(f'Обработана {count}-я страница из {len(urls)}')
            time.sleep(random.randrange(3, 5))
        with open('items.json', 'a', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    get_data()
