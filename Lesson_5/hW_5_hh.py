import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains



chrome_options = Options()
# chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)
url = 'https://hh.ru/search/vacancy?area=&fromSearchLine=true&st=searchVacancy&text=Python+junior&from=suggest_post'
driver.get(url)

# page_element = driver.find_element_by_xpath("//div[@data-qa='pager-block']")
# actions = ActionChains(driver)
# actions.move_to_element(page_element)
# actions.perform()
vacancies = driver.find_elements_by_xpath("//span[@class='g-user-content']")
# vacancies = driver.find_elements_by_class_name('g-user-content')
for vacancy in vacancies:
    print(vacancy.find_element_by_xpath(".//a").text)
