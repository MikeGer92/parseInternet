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
    last_page = soup.find_all('span', attrs={'class': 'pager-item-not-in-short-range'})[-1].text
    last_page_num = int(last_page)
    return last_page_num


def get_parse_hh(par, head, adr):
    response = requests.get(adr+'/search/vacancy', params=par, headers=head)
    soup = bs(response.text, 'html.parser')
    vacancy_list = soup.find_all('div', attrs={'class': 'vacancy-serp-item__row_header'})
    for el in vacancy_list:
        vacancy_dic = {}
        vacancy_name = el.find('span', attrs={'class': 'bloko-header-section-3 bloko-header-section-3_lite'}).text
        vacancy_salary_tag = el.find('span', attrs={'data-qa': 'vacancy-serp__vacancy-compensation'})
        if vacancy_salary_tag:
            vacancy_salary_tag = vacancy_salary_tag.getText().replace('\u202f', '').split(' ')
            if 'от' in vacancy_salary_tag:
                vacancy_dic['мин. З/П'] = (f"{int(vacancy_salary_tag[1])} {vacancy_salary_tag[2]}")
            elif 'до' in vacancy_salary_tag:
                vacancy_dic['макс. З/П'] = (f"{int(vacancy_salary_tag[1])} {vacancy_salary_tag[2]}")
            else:
                vacancy_dic['З/П'] = (f"от {int(vacancy_salary_tag[0])} до {int(vacancy_salary_tag[2])} {vacancy_salary_tag[3]}")
        else:
            vacancy_dic['З/П'] = (f"не указана")

        vacancy_dic['Вакансия'] = vacancy_name
        main_list.append(vacancy_dic)
    pprint(main_list)

# vacancy_name = input('Введите название вакансии, которую необходимо найти:_') для поиска заданной пользователем вакансии
# params_hh['text'] = vacancy_name
def full_parse_hh(*args, **kwargs):
    l_p_n = get_last_page_hh(*args, **kwargs)
    print(f'Найдено {l_p_n} страниц с вакансиями:')
    user_l_p_n = input(f'Введите необходимое количество страниц для сбора данных(по умолчанию {l_p_n}):_')
    try:
        user_l_p_n = int(user_l_p_n)
    except ValueError:
        print(f'Вы ввели некорректное число страниц, будут обработаны все найденные страницы')
        user_l_p_n = l_p_n
    finally:
        if 0 < user_l_p_n <= l_p_n:
            l_p_n = user_l_p_n
        else:
            print(f'Вы ввели некорректное число страниц, будут обработаны все найденные страницы')
        for i in range(l_p_n):
            print(f'Страница {i + 1}:')
            params_hh['page'] = i
            get_parse_hh(*args, **kwargs)


# get_parse_hh(params_hh, headers, url_hh) - для тестового парсинга первой страницы
# get_last_page_hh(params_hh, headers, url_hh) #- для печати количества найденных страниц с вакансией
full_parse_hh(params_hh, headers, url_hh)




