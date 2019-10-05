"""
Построим диаграмму популярности проектов на Python
Высота каждого столбца - количество звезд проекта
Щелчок по столбцу откроет домашнюю страницу проекта
"""

import requests as req
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#создание вызова API и сохранение ответа
URL = "https://api.github.com/search/repositories?q=language:python&sort=star"
r = req.get(URL)
print("Status code: ", r.status_code)

#сохранение ответа в переменной
response_dict = r.json()
print("Total repositories: ", response_dict["total_count"])

#анализ информации о репозиториях
dicts = response_dict["items"]
print("Number of items = ", str(len(dicts)))

#чтобы пр наведении мыши на столбец диаграммы показывалось не только число, но и дополнительное
#описание, нужно в метод add() передать не массив значений, а массив словарей
#каждый словарь должен иметь вид
#{"value": 12345, "label": "Description of mah dick"}
#где "value" определяет высоту столбца, а "label" - подсказку, которая появится при наведении мыши
#сгенерируем массив словарей для каждого репозитория
#ПОЧЕМУ-ТО если оставит "label", то выдает ошибку кодировки utf-8

names, plot_dicts = [], []
for dict in dicts:
    names.append(dict["name"]) #добавляем имя каждого проекта в массив
    if dict["description"] is not None:
        plot_dict = {
            "value": dict["stargazers_count"],
            "label": dict["description"],
            "xlink": dict["html_url"],
        }
    else:
        print(dict["name"] + " has no description")
        plot_dict = {
            "value": dict["stargazers_count"],
            "xlink": dict["html_url"],
        }
    plot_dicts.append(plot_dict)
#построение визуализации

#создадим определенные конфиг для диаграммы
#позже он будет добавлен при изображении
my_style = LS("#333366", base_style = LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45# поворот надписей по x
my_config.show_legend = False# не показыать легенду диаграммы
my_config.title_font_size = 24# размер заголовка
my_config.label_font_size = 14# размер подписей
my_config.major_label_font_size = 20# ОСНОВНЫЕ ПОДПИСИ идут по оси y с разделением в 5000 звезд дадим им другой размер для наглядности
my_config.truncate_label = 15# если название проекта очень длинное, о оно сократится до 15 символов
my_config.show_y_guides = False# не показывать горизонтальные полосы на диаграмме
my_config.width = 1000

#x_label_rotation - поповорот надписей по x, show__lenend = False - не показывать легенду диаграммы
chart = pygal.Bar(my_config, style = my_style)
chart.title = "Most Starred Python Projects on GitHub"
chart.x_labels = names

chart.add("", plot_dicts)
chart.render_to_file("python_repos.svg")