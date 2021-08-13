from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from variables import TEST_LOGIN, TEST_PASSW

chrome_options = Options()
chrome_options.add_argument('--window-size=760,1080')


driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)
url = 'https://gb.ru/login'
driver.get(url)

login = driver.find_element_by_id('user_email')
login.send_keys(TEST_LOGIN)

passw = driver.find_element_by_id('user_password')
passw.send_keys(TEST_PASSW)

passw.send_keys(Keys.ENTER)

menu = driver.find_element_by_xpath("//span[contains(text(), 'меню')]")
menu.click()
button = driver.find_element_by_xpath("//button[@data-test-id='user_dropdown_menu']")
button.click()
link = driver.find_element_by_xpath("//div[@data-testid='animation-wrapper']//a[contains(@href, '/users/')]")
url = link.get_attribute('href')
driver.get(url)

edit_profile = driver.find_element_by_class_name('text-sm')
driver.get(edit_profile.get_attribute('href'))

gender = driver.find_element_by_name('user[gender]')
select = Select(gender)
select.select_by_value('male')

gender.submit()

