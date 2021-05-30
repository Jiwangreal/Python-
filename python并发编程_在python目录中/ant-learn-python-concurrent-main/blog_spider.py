import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/sitehome/p/{page}"
    for page in range(1, 50 + 1)
]


def craw(url):
    #print("craw url: ", url)
    r = requests.get(url)
    ##len(r.text)表示该url网页的长度,r.text表示网页的内容
    # print(url, len(r.text))
    return r.text


def parse(html):
    # class="post-item-title"
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    ##解析出链接：(link["href"]
    ##解析出来标题：link.get_text()
    return [(link["href"], link.get_text()) for link in links]


if __name__ == "__main__":
    for result in parse(craw(urls[2])):
        print(result)
