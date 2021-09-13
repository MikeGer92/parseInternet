from bs4 import BeautifulSoup as bs
import requests
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)
# db = client['users020821']
# persons = db.persons
# persons.insert_one({
#     'name': 'Mike',
#     'age': 46,
#     'status': 'married',
#     'children': [{'son': 'Vit'}, {'son': 'Dim'}],
#     'create': '02.08.2021'
# })
# for doc in persons.find({}):
#     pprint(doc)
db_vacancy = client['userHH']
vacancy010821 = db_vacancy.vacancy010821
# vacancy = {'Вакансия': 'Junior DevOps', 'З/П': ['50000', '–', '90000', 'руб.']}
# vacancy020821.insert_one(




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
        vacancy_dic['Вакансия'] = vacancy_name
        vacancy_salary_tag = el.find('span', attrs={'data-qa': 'vacancy-serp__vacancy-compensation'})
        if vacancy_salary_tag:
            vacancy_salary_tag = vacancy_salary_tag.getText().replace('\u202f', '').split(' ')
            if 'от' in vacancy_salary_tag:
                vacancy_dic['salary'] = [{'min': int(vacancy_salary_tag[1])}, {'max': None}, vacancy_salary_tag[2]]
            elif 'до' in vacancy_salary_tag:
                vacancy_dic['salary'] = [{'min': None}, {'max': int(vacancy_salary_tag[1])}, vacancy_salary_tag[2]]
            else:
                vacancy_dic['salary'] = [{'min': int(vacancy_salary_tag[0])}, {'max': int(vacancy_salary_tag[2])},
                                         vacancy_salary_tag[3]]
        else:
            vacancy_dic['salary'] = None
        vacancy010821.insert_one(vacancy_dic)
        # if 'от' in vacancy_salary_tag:
        #     vacancy_dic['мин.З/П'] = (f"{int(vacancy_salary_tag[1])} {vacancy_salary_tag[2]}")
        # elif 'до' in vacancy_salary_tag:
        #     vacancy_dic['макс.З/П'] = (f"{int(vacancy_salary_tag[1])} {vacancy_salary_tag[2]}")
        # else:
        #     vacancy_dic['З/П'] = (f"от {int(vacancy_salary_tag[0])} до {int(vacancy_salary_tag[2])} {vacancy_salary_tag[3]}")
        main_list.append(vacancy_dic)

    # pprint(main_list)

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


# full_parse_hh(params_hh, headers, url_hh)


for doc in vacancy010821.find({'З/П': {'$gt': 60000}}):

    pprint(doc)



#для запуска МОНГО вводим: .\mongod.exe --dbpath C:/bases
