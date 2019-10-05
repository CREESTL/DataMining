import pygal.maps.world as maps
from population_data import pop_dict, get_country_code

wm = maps.World()
wm.title = "Populatin of countries in North America"
                        # ca - Canada, mx - Mexicom, us - United States
#wm.add("North America", ["ca", "mx", "us"]) #каждый вызов add создает новый цвет для набора стран из массива
#но мы вставим не массив, а словарь
wm.add("North America", {"ca": 34126000, "us": 309349000, "mx": 113423000})



wm.render_to_file("americas.svg")

