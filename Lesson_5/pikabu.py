import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains



chrome_options = Options()
# chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)
url = 'https://pikabu.ru/'
driver.get(url)

for i in range(5):
    time.sleep(10)
    articles = driver.find_elements_by_tag_name('article')
    actions = ActionChains(driver)
    actions.move_to_element(articles[-1])
    actions.perform()