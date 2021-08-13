from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
# chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('start-maximized')


driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)

url = 'https://lenta.com/catalog/myaso-ptica-kolbasa/'
driver.get(url)
close = driver.find_element_by_xpath("//div[@class='close-control']")
close.click()
# cookie_button = driver.find_element_by_class_name('cookie-usage-notice__button-inner--desktop')
# if cookie_button:
#     cookie_button.click()

while True:
    try:
        load_more_wait = WebDriverWait(driver, 10)
        load_more_click = load_more_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'catalog-grid-container__pagination-button')))
        load_more_click.click()
    except Exception as e:
        print(e)
        break
print('Загрузка всех страниц закончена')
