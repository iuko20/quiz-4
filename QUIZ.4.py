import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import randint

p = 1

file = open('topAnime.csv', 'w', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['title', 'view', 'series'])


while p <= 6:
    url = f'https://animehd47.com/top-anime/page/{p}/'
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    anime_list = soup.find('div', class_='entry-content')

    all_anime = anime_list.find_all('div', class_='col-sm-6 col-md-3 zmovies')

    for each in all_anime:
        title = each.h3.text.strip()
        view = each.find('span', class_='views').text
        series_count = each.find('span', class_='series').text

        print(series_count)

        file_obj.writerow([title, view, series_count])

    p += 1
    sleep(randint(5, 15))
