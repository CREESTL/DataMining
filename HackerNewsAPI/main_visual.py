import requests
import pygal
from operator import itemgetter
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

"""

Прога вызывает API с сайта Hacker News и строит диаграмму
по количеству комментариев на самых популярных статьях

"""
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("Main request status: ", r.status_code)

ids = r.json()#номера всех популярных статей
dicts = []#массив словарей с данными по каждой статье

for id in ids[:10]: #выведем инфу по 10 статьям
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(id) + ".json"
    r = requests.get(url)
    print("Sub status code: ", r.status_code)
    dict = r.json()

    if dict["title"] is not None:
        r_dict = {
            "title": dict["title"],
            "xlink": "http://news.ycombinator.com/item?id=" + str(id),
            "value": dict.get("descendants", 0)
        }
    else:
        r_dict = {
            "xlink": "http://news.ycombinator.com/item?id=" + str(id),
            "value": dict.get("descendants", 0)
        }

    dicts.append(r_dict)

    dicts = sorted(dicts, key=itemgetter("value"), reverse=True)

config = pygal.Config()
style = LS("#336699", base_style = LCS)
config.x_label_rotation = 45
config.show_legend = False
config.title_font_size = 24
config.label_font_size = 16
config.show_y_guides = False
config.truncate_label = 20
config.width = 1000

graf = pygal.Bar(config, style = style)
graf.title = "Most popular Hacker News topics"
graf.x_labels = (dicts[i]["title"] for i in range(len(dicts)))

graf.add("", dicts)
graf.render_to_file("Hacker-Nes.svg")


