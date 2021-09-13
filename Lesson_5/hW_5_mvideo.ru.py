import ast
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db_new_products = client['new_product_mvideo']
new_poducts13092021 = db_new_products.new_poducts13092021

chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)
url = 'https://mvideo.ru/?cityId=CityCZ_2128'
driver.get(url)
time.sleep(5)
try:
    close_btn = driver.find_element_by_class_name('modal-layout__close')
except Exception:
    pass
else:
    close_btn.click()

btn_wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)
new_prod_block = driver.find_element_by_xpath('//div[contains(h2, "Новинки")]')
actions.move_to_element(new_prod_block).perform()
while True:
    try:
        next_btn = btn_wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(h2, "Новинки")]/../..//a[contains(@class, "next-btn")]')))
    except Exception:
        break
    else:
        next_btn.click()

new_products_list = driver.find_elements_by_xpath('//div[contains(h2, "Новинки")]/../..//a[contains(@class, "fl-product-tile-picture")]')
new_products_dic = {}
for product in new_products_list:
    prod_info = product.get_attribute('data-product-info')
    product_info_dic = ast.literal_eval(prod_info)
    new_poducts13092021.insert_one(product_info_dic)


#для запуска МОНГО вводим: .\mongod.exe --dbpath C:/bases