
import csv
import urllib.request as request
import json
# mac電腦需要添加下方ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

# 利用json模組存取資料
with request.urlopen(src) as response:
    data = json.load(response)


# attraction.csv需要取得景點名稱,區域,經度,緯度,第一張圖檔網址
tapeilist = data["result"]["results"]

with open("attraction.csv", mode="w", encoding="utf-8")as file:
    for information in tapeilist:
        lines = [information["stitle"]+",", information["address"][4:8]+",",
                 information["longitude"]+","+"https", information["file"].split("https")[1]+"\n"]
        file.writelines(lines)

# mrt.csv需要取得捷運站名稱, 景點名稱一, 景點名稱二, 景點名稱三...
with open("mrt.csv", mode="w", encoding="utf-8")as file:
    items = []
    for information in tapeilist:
        # 建立所有資料的dict
        dict = {}
        dict["MRT"] = information["MRT"]
        dict["stitle"] = information["stitle"]
        items.append(dict)

    merged_data = {}
    # 把相同捷運站的資料做分類，放到合併後的dict
    for item in items:
        mrt = item["MRT"]
        stitle = item["stitle"]

        if mrt in merged_data:
            merged_data[mrt].append(stitle)
        else:
            merged_data[mrt] = [stitle]

    for mergerd_item in merged_data.items():
        # 逐一印出合併後的資料
        print(mergerd_item)

        writer = csv.writer(file)
        writer.writerow(mergerd_item)
