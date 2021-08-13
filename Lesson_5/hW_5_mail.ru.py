import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from variables import TEST_LOGIN, TEST_PASSW, TEST_LOGIN_MAIL, TEST_MAIL_PASSW

chrome_options = Options()
chrome_options.add_argument('start-maximized')


driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)
url = 'https://mail.ru'
driver.get(url)

login = driver.find_element_by_name('login')
login.send_keys(TEST_LOGIN_MAIL)
enter_passw = driver.find_element_by_xpath("//button[@data-testid='enter-password']")
enter_passw.click()
passw = driver.find_element_by_xpath("//input[@class='password-input svelte-1eyrl7y']")
time.sleep(3)
passw.send_keys(TEST_MAIL_PASSW)

passw.send_keys(Keys.ENTER)
time.sleep(10)
letters = driver.find_elements_by_class_name('llc__content')
actions = ActionChains(driver)
actions.move_to_element(letters[-1])
actions.perform()
time.sleep(3)
letters_links_list = []
letters_links = driver.find_elements_by_xpath("//a[contains(@class, 'js-tooltip-direction_letter-bottom')]")
for link in letters_links:
    letters_links_list.append(link.get_attribute('href'))
time.sleep(2)

