
import concurrent.futures
import blog_spider

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    ##zip(blog_spider.urls, htmls)将每个url和html对应起来
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over")

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        ##参数是单个html
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    ##输出方法1
    #for future, url in futures.items():
    #    print(url, future.result())

    ##输出方法2
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())