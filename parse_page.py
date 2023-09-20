import json
import time

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from undetected_chromedriver import ChromeOptions


def parse_links():
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    driver = uc.Chrome(version_main=117, options=options)
    with open('urls.txt', 'r') as f:
        urls = f.read().split()

    item_list = []
    count = 0
    for url in urls[1:]:
        try:
            driver.get(url)
            links = driver.find_elements(By.CSS_SELECTOR, "[class='IdiaP ']")
            maps = links[0].get_attribute('href')
            website = links[1].get_attribute('href')
            print(links)
            # about = driver.find_element(By.CSS_SELECTOR, "[class='xHZAW']").text
            # details = driver.find_elements(By.CSS_SELECTOR, "[class='ui_columns ']")
            data = {
                'Место расположения': maps,
                'Вебсайт': website
            }
            item_list.append(data)
        except Exception as ex:
            print(f"Error occurred while parsing {url}: {str(ex)}")
        finally:
            driver.close()
            driver.quit()


if __name__ == '__main__':
    parse_links()
