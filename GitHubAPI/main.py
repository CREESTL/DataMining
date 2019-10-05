"""
У каждого веб-приложения есть API - это часть сайта, которая обрабатывает взаимодействия с программами,
которые запращивают с сайта информацию через особые URL-адреса
Запросы называются вызовами API


Напишем программу для автоматической загрузки информации с GitHub о самых популярных
проектах на Python и выведем визуализацию этих данных

Пример вызова

https://api.github.com/search/repositories?q=language:python&sort=stars

api.github.com - передает запрос части сайта GitHub, отвечающей за API
search/repositories - поиск по репозиториям GitHub
? - значит мы собираемся передать аргумент вручную
q - запрос
= - определение запроса
language:python - все проекты на python
&sort=stars - сортировка по количесвту звезд у проекта (чем больше, тем он популярнее)

Многие API ставят лимит на количество запросов в единицу времени
Его можно узнать примерно так
https://api.github.com/rate_limit

Модуль requests отвечает за вызовы API

"""


#прога выдвает вызов API для проектов с наиюольшим кодичеством звезд

import requests as req

#создание вызова API и сохранение ответа
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = req.get(url)
print("status code: ", r.status_code)#код 200 - признак успешного ответа

#сохранение ответа API в переменной
response_dict = r.json() #вызывается функция с таким именем, какой формат хотим получить

#обработка результатов
print("Total repositories: ", response_dict["total_count"])
print("Repositories returned: ", len(response_dict["items"])) #items - все возвращенные(?) репозитории

#вывод выбранных данных о каждом репозитории
dicts = response_dict["items"]
for dict in dicts:
    #выберем некоторые данные
    print("Some data about the first repository:")
    print("Name: ", dict["name"])
    print("Owner: ", dict["owner"]["login"])
    print("Stars: ", dict["stargazers_count"])
    print("Reposiroty: ", dict["html_url"])
    print("Descriptions: ", dict["description"])
