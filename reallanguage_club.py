import random
from time import sleep

import requests
from bs4 import BeautifulSoup
import json
import csv

# url = "https://reallanguage.club/anglijskie-slova-po-temam/"
#
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 Mobile Safari/537.36"
}
# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)
#
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

# with open("index.html", encoding="utf-8") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
# all_categories_hrefs = soup.find("tr").find_all("a")
#
all_categories_dict = {}
# for item in all_categories_hrefs:
#     item_text = item.text
#     item_href = item.get("href")
#
#     all_categories_dict[item_text] = item_href
#
# with open("all_categories_dict.json", "w", encoding="utf-8") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)


# with open("all_categories_dict.json", encoding="utf-8") as file:
#     all_categories = json.load(file)
#

count = 2
print(f"Всего итерраций: {count}")
#
# count_cat = 19
# for category_name, category_href in all_categories.items():

url = "https://infoselection.ru/obrazovanie1/stranitsy/anglijskij-yazyk/item/916-300-populyarnykh-fraz-na-anglijskom"

req = requests.get(url=url, headers=headers)
src = req.text

with open(f"data1/{count}.html", "w", encoding="utf-8") as file:
    file.write(src)

with open(f"data1/{count}.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

# origin = "Оригинал"
# translate = "Перевод"

# with open(f"data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         (
#             origin,
#             translate
#         )
#     )

words_all = soup.find_all(class_="zebra1")
words_info = []
for word in words_all:
    words = word.find_all("tr")

    for item in words:

        word_tds = item.find_all("td")
        if len(word_tds) == 3:
            print(word_tds)
            translate = word_tds[1].text
            origin = word_tds[2].text

#
            words_info.append(
                {"model": "method.cardwords", "fields": {"origin": origin, "translate": translate, "cat": 72}}
            )
#
#         # with open(f"data/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
#         #     writer = csv.writer(file)
#         #     writer.writerow(
#         #         (
#         #             origin,
#         #             translate
#         #         )
#         #     )
with open(f"data1/{count}.json", "a", encoding="utf-8") as file:
    json.dump(words_info, file, ensure_ascii=False)

# count_cat +=1
count += 1
print(f"# Итеррация {count}, фаил записан... ")
# iteration_count = iteration_count - 1

# if iteration_count == 0:
#     print("Работа закончена")
#     break
print(f"Осталось итерраций: {count}")
sleep(random.randrange(2,4))