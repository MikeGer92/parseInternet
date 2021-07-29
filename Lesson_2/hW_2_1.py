from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

url_hh = 'https://www.hh.ru'
params_hh = {'area': '', 'fromSearchLine': 'true', 'st': 'searchVacancy', 'text': 'Python junior', 'form': 'suggest_post', 'page': '0'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55'}
main_list = []

def get_last_page_hh(par, head, adr):
    response = requests.get(adr+'/search/vacancy', params=par, headers=head)
    soup = bs(response.text, 'html.parser')
    last_page = soup.find_all('span', attrs={'class': 'pager-item-not-in-short-range'})
    last_page_num = int(last_page.split(';')[-1][5:7])+1
    return last_page_num


def get_parse_hh(par, head, adr):
    response = requests.get(adr+'/search/vacancy', params=par, headers=head)
    soup = bs(response.text, 'html.parser')
    vacancy_list = soup.find_all('div', attrs={'class': 'vacancy-serp-item__row_header'})
    for el in vacancy_list:
        vacancy_dic = {}
        vacancy_name = el.find('span', attrs={'class': 'bloko-header-section-3 bloko-header-section-3_lite'}).text
        vacancy_salary_tag = el.find('div', attrs={'class': 'vacancy-serp-item__sidebar'})
        # vacancy_salary = vacancy_salary_tag.find('span', attrs={'class': 'bloko-header-section-3 bloko-header-section-3_lite'}).getText()
        vacancy_dic['name'] = vacancy_name
        vacancy_dic['salary'] = vacancy_salary_tag
        main_list.append(vacancy_dic)
    pprint(main_list)

# vacancy_name = input('Введите название вакансии, которую необходимо найти:_')
# params_hh['text'] = vacancy_name
def full_parse_hh(*args, **kwargs):
    l_p_n = get_last_page_hh(*args, **kwargs)
    print(l_p_n)
    for i in range(l_p_n):
        params_hh['page'] = i
        get_parse_hh(*args, **kwargs)
    print(len(main_list))
    print(main_list)

# full_parse_hh(params_hh, headers, url_hh)
# print(get_last_page_hh(params_hh, headers, url_hh))
get_parse_hh(params_hh, headers, url_hh)



