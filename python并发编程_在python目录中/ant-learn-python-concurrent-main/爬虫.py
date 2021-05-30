import urllib.request
import os
import random

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header = [('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')]
   
    # ##使用代理的方式，但是爬取的图片不是妹子图片了，是乱七八糟的图片了
    # iplist = ['119.6.144.73:81', '183.203.208.166:8118', '111.1.32.28:81']
    # proxy = random.choice(iplist)
    # proxy_support = urllib.request.ProxyHandler({'http':proxy})
    # opener = urllib.request.build_opener(proxy_support)
    # urllib.request.install_opener(opener)
   
    response = urllib.request.urlopen(req)
    html = response.read()
    print(url)
    return html


def get_page(url):
    ##html是字符串
    html = url_open(url).decode('utf-8')
    #表示找到标签是1293的位置
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    return html[a:b]

def find_img(page_url):
    html = url_open(page_url).decode('utf-8')
    img_addrs = []
    a = html.find('img src=')

    while a != -1:
        ##url最多不会超过255
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(html[a+9,b+4])
        else:
            b = a + 9
        a = html.find('img src=', b)

    # for each in img_addrs:
    #     print(each)
    return img_addrs


def save_img(folder,img_addrs):
    ##按照/进行分割，取最后一个成员
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            ##
            img = url_open(filename)
            f.write(img)

def download_mm(folder='OOXX', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= 1
        ##拼接字符串
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_img(page_url)
        save_img(folder,img_addrs)

if __name__ == '__main':
    download_mm()