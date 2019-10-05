"""

Рисуется карта мира
Страны раскрашиваются в зависимотси от населения
Прилагается числовая информация  населении при наведении мыши на страну


"""

import json
from pygal.maps.world import COUNTRIES
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
import pygal.maps.world as maps


# получает название страны - выводит ее код
def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None


cc_populations = {}
filename = "population_json.json"
with open(filename) as f:
    pop_data = json.load(f)

    for pop_dict in pop_data:
        if pop_dict['Year'] == 2010: #население всех стран в 2010 году
            country_name = pop_dict['Country Name'] #из json достаем код страны, название и население
            population = pop_dict['Value']
            code = get_country_code(country_name)
            if code:
                cc_populations[code] = population #создаем новый словарь   КОД - НАСЕЛЕНИЕ
                print("(" + str(code) + ") " + country_name + ": " + str(int(population)))
            else:
                print("ERROR!!! Country " + country_name + " will not be shown on the picture!!!")
    print("RENDERING COMPLETE")

"""
Сгруппируем страны по 3 уровням населения
1) Менее 10 миллионов
2) От 10 миллионов до миллиарда
3) Более миллиарда
"""


cc1, cc2, cc3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc1[cc] = pop
    elif pop < 1000000000:
        cc2[cc] = pop
    else:
        cc3[cc] = pop

"""
RotateStyle принимает аргумент - цвет в ШЕСТНАДЦАТИРИЧНОМ ФОРМАТЕ RGB
Сначала пишется решется #
Затем шесть цифр
Первые две цифры - количество красного (Red)
Вторые две цифры - количество зеленого (Green)
Третьи две цифры - количество синего (Blue)
"""
style = RS("#336699", base_style = LCS) #LCS - LightColorizedStyle из импорта - осветляет цфета оформления немного
wm = maps.World(style = style)
wm.title = "World population if 2010"
wm.add("0-10m", cc1)
wm.add("10m-1b", cc2)
wm.add("1b+", cc3)
wm.render_to_file("world_2010.svg")