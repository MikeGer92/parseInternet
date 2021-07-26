from pprint import pprint
import requests
url = 'https://www.google.ru'

response = requests.get(url)
print()

response.status_code
response.ok
response.headers
response.content



response.text




































# # e5e4cd692a72b0b66ea0a6b80255d1c3
# # api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# import requests
# from pprint import pprint
#
# main_link = 'https://api.openweathermap.org/data/2.5/weather'
# city = 'Larnaca'
# appid = 'e5e4cd692a72b0b66ea0a6b80255d1c3'
# params = {'q': city,
#           'appid': appid}
# response = requests.get(main_link, params=params)
# if response.ok:
#     j_data = response.json()
#     # pprint(j_data)
#     print(f"В городе {j_data['name']} температура {j_data['main']['temp'] - 273.15} градусов")