import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
# from treelib import Tree

data = []

for p in range(1, 18):
  print(p)
  url = f"https://tutortop.ru/courses_category/programmirovanie/page/{p}/"
  r = requests.get(url)
  sleep(3)
  soup = BeautifulSoup(r.text, "html.parser")

  courses = soup.findAll('div', class_='tab-course-item tab-course-item-bg')

  i = 0
  for cours in courses:
    if i < 30:
      # название курса
      name = cours.find('div', class_='m-course-title').text
      # описание курса
      try:
        txt = cours.find('a', class_='tab-link-course popup-course-link pop-up-new-window').get('href').replace('/goto/?number=', '').replace('&term=9', '')
        txt = 'course__wrap__box post__' + txt
        descript = soup.find('div', class_= txt).find('div', class_='course__wrap__box__content').find('div', class_='clock__box').find('p', class_='heart').text.strip().replace('Особенности: ', '')
      except:
        descript = '-'
      # рейтинг курса
      try:
        rate = cours.find('div', class_='course__wrap__box__top_rating rating_count_green').text
      except:
        rate = cours.find('div', class_='course__wrap__box__top_rating rating_count_red').text
      # Школа
      school = cours.find('a', class_ = 'course__col_school_name popup-course-link pop-up-new-window').text.strip()
      # начало курса
      start = cours.find('div', class_='tab-course-col tab-course-col-date-t tab-course-col-date').contents[1].text.strip()
      # продолжительность
      length = cours.find('div', class_='course_duration').text.strip()
      # цена
      try:
        txt = cours.find('a', class_='tab-link-course popup-course-link pop-up-new-window').get('href').replace('/goto/?number=', '').replace('&term=9', '')
        txt = 'course__wrap__box post__' + txt
        price = soup.find('div', class_= txt).find('div', class_='course__wrap__box__price__left').find('span', class_='summ').text.replace('\xa0', ' ').strip()
      except:
        price = '-'
      data.append([name, descript, rate, school, start, length, price])
      i+=1

frame = pd.DataFrame(data, columns=['name', 'descript', 'rate', 'school', 'start', 'length', 'price'])

# frame.to_json('fr.json')

# Сохранение в JSON
#with open('fr.json', 'w', encoding='utf-8') as file:
#  frame.to_json(file, force_ascii=False, orient = 'split', compression = 'infer')
#

# Сохранение в CSV
frame.to_csv(path_or_buf='fr1.csv', sep=';', encoding='utf-8')
