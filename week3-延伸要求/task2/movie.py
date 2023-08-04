from os import write
import bs4
import urllib.request as req
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def getData(url):
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")

    datas = ["文章標題", "推文數量", "發佈時間"]

    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            # 如果文章存在才需要進到裡面抓文章發佈的時間
            postUrl = "https://www.ptt.cc"+title.a["href"]
            request = req.Request(postUrl, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"})
            with req.urlopen(request) as response:
                data = response.read().decode("utf-8")
                html = bs4.BeautifulSoup(data, "html.parser")
            datas[2] = html.find_all(
                "span", class_="article-meta-value")[-1].string
            datas[0] = title.a.string

        else:
            datas[0] = "已刪除的文章"
            datas[2] = "無法存取發布時間"

        nrecs = title.parent.find("div", class_="nrec")

        if nrecs.span != None:
            datas[1] = nrecs.span.text

        else:
            datas[1] = "沒有推文"

        file.write(f"{datas[0]},{datas[1]},{datas[2]}\n")

    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]


with open("movie.txt", mode="w", encoding="utf-8")as file:
    pageurl = "https://www.ptt.cc/bbs/movie/index.html"
    count = 0
    while count < 3:
        pageurl = "https://www.ptt.cc"+getData(pageurl)
        count += 1
        file.write('\n')
