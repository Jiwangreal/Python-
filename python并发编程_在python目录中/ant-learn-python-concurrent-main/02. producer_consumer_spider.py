import queue
import blog_spider
import time
import random
import threading

##输入队列url_queue，输出队列：html_queue
##queue.Queue仅仅做标明类型作用，不用也行
def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        html_queue.put(html)

        ##打印当前线程的名字：threading.current_thread().name
        print(threading.current_thread().name, f"craw {url}",
              "url_queue.size=", url_queue.qsize())
        ##随机睡眠1-2s
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for result in results:
            fout.write(str(result) + "\n")
        print(threading.current_thread().name, f"results.size", len(results),
              "html_queue.size=", html_queue.qsize())
        time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    url_queue = queue.Queue()
    html_queue = queue.Queue()

    ##主线程将数据扔到生产者
    for url in blog_spider.urls:
        url_queue.put(url)

    ##3个生产者线程，生产者产生中间的数据仍到html_queue
    for idx in range(3):
        ##name=f"craw{idx}"表示线程名字
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue),
                             name=f"craw{idx}")
        t.start()

    ##2个消费者线程对html_queue进行处理
    fout = open("02.data.txt", "w")
    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, fout),
                             name=f"parse{idx}")
        t.start()
