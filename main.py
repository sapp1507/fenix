from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime as dt
from utils import get_weekday, Dish
import pprint
from time import sleep


pp = pprint.PrettyPrinter(indent=3, width=5)

URL = 'https://xn------5cdadeibbrgfiqc2aax5ay5add2d.xn--p1ai/menu/'
driver = webdriver.Chrome()
driver.get(URL)

assert 'Вкусные обеды во Владимире' in driver.title
week = driver.find_element(By.ID, 'week')
options = week.find_elements(By.TAG_NAME, 'option')
date = {}
dishes = []
for i, option in enumerate(options):
    t = option.get_attribute('value')
    day = dt.strptime(option.get_attribute('value'), '%Y-%m-%d')
    date[i] = [day, get_weekday(day.weekday())]

item = driver.find_element(By.CLASS_NAME, 'select-selected')
days = driver.find_element(By.CLASS_NAME, 'select-items')
span = days.find_elements(By.TAG_NAME, 'span')
for day in span:
    item.click()
    day.click()
    # driver.implicitly_wait(1)
    sleep(.5)
    dishes = driver.find_elements(By.CLASS_NAME, 'dish')

    if len(dishes) == 0:
        continue
    for dish in dishes:
        category = dish.find_element(By.CLASS_NAME, 'text-center').text
        print(f'Категория: {category}')
        names = dish.find_elements(By.CLASS_NAME, 'dish__item')
        for name in names:
            url = name.find_element(By.CLASS_NAME, 'dish__photo-wrap').get_attribute('href')
            txt = name.find_element(By.CLASS_NAME, 'dish__name').text
            weight = name.find_element(By.CLASS_NAME, 'dish__weight').text
            desc = name.find_element(By.CLASS_NAME, 'dish__description').text
            price = name.find_element(By.CLASS_NAME, 'dish__price').text
            dish_id = name.find_element(By.CLASS_NAME, 'add-to-bas').get_attribute('data-id')

            print(f'url: {url}\n'
                  f'txt: {txt}\n'
                  f'weight: {weight}\n'
                  f'desc: {desc}\n'
                  f'price: {price}\n'
                  f'dish_id: {dish_id}\n')
