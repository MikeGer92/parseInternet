import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from variables import TEST_LOGIN, TEST_PASSW, TEST_LOGIN_MAIL, TEST_MAIL_PASSW, LOGIN, PASSWORD

chrome_options = Options()
chrome_options.add_argument('start-maximized')


driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)
url = 'https://mail.ru'
driver.get(url)

login = driver.find_element_by_name('login')
login.send_keys(LOGIN)
enter_passw = driver.find_element_by_xpath("//button[@data-testid='enter-password']")
enter_passw.click()
passw = driver.find_element_by_xpath("//input[@class='password-input svelte-1tib0qz']")
time.sleep(3)
passw.send_keys(PASSWORD)

passw.send_keys(Keys.ENTER)
list_wait = WebDriverWait(driver, 15)
list_wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'js-tooltip-direction_letter-bottom')))
letters_links_list = set()

while True:
    letters_links_list_len = len(letters_links_list)
    letters_links = driver.find_elements_by_class_name('js-tooltip-direction_letter-bottom')
    for link in letters_links:
        letters_links_list.add(link.get_attribute('href'))
    actions = ActionChains(driver)
    actions.move_to_element(letters_links[-1])
    actions.perform()
    if len(letters_links_list) == letters_links_list_len:
        break

print (len(letters_links))

