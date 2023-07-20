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
    # 先建一個空白的字典，放存在的捷運站為key，value則為空白
    info = {}
    for information in tapeilist:
        if information["MRT"] == None:
            continue
        else:
            info[information["MRT"]] = []
    print(info)

    # 利用迴圈將對應的景點append進去info字典，作為value

    for information in tapeilist:
        if information["MRT"] == None:
            continue
        else:
            info[information["MRT"]].append(information["stitle"])
    print(info)

    # 將info字典，逐一印出key & value

    for key, value in info.items():
        value = ','.join(value)
        file.write(f"{key}, {value}\n")
