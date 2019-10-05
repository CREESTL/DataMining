"""
Вызовем API для сайта Hacker News
Пример вызова для этого сайта (самая популярная статья)

https://hacker-news.firebaseio.com/v0/item/9884165.json

Ответ - словарь
Ключ 'descendants' - количество комментариев
Ключ 'kids' - все дочерние комментарии

Создадим вызов API для получения инедтефикаторов самых популярных статей

"""
import requests
from operator import itemgetter

#создание вызова API и сохранение результатов
url = "https://hacker-news.firebaseio.com/v0/topstories.json" #выдает 500 самых популярных статей
r = requests.get(url)
print("Status code: ", r.status_code)

#обработка информации о каждой статье
sub_ids = r.json()
sub_dicts = []# массив словарей для каждой статьи
for sub_id in sub_ids[:30]:
    #создадим вызов API для каждой статьи
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(sub_id) + ".json"
    sub_r = requests.get(url)
    print("Substatus code: ", sub_r.status_code)
    response_dict = sub_r.json()

    sub_dict = {
        "title": response_dict["title"],
        "link": "http://news.ycombinator.com/item?id=" + str(sub_id),
        "comments": response_dict.get("descendants", 0)
    }
    sub_dicts.append(sub_dict)

sub_dicts = sorted(sub_dicts, key=itemgetter("comments"), reverse = True)#сортируем список по количеству комментариев на каждой статье
#сортируем в обратном порядке, чтобы статьи с наибольшим количеством комментариев были на первом месте

for sub_dict in sub_dicts:
    print("\nTitle: ", sub_dict["title"])
    print("Discussed link: ", sub_dict["link"])
    print("Comments: ", sub_dict["comments"])

