import queue
import blog_spider
import time
import random
import threading

##�������url_queue��������У�html_queue
##queue.Queue�����������������ã�����Ҳ��
def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        html_queue.put(html)

        ##��ӡ��ǰ�̵߳����֣�threading.current_thread().name
        print(threading.current_thread().name, f"craw {url}",
              "url_queue.size=", url_queue.qsize())
        ##���˯��1-2s
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

    ##���߳̽������ӵ�������
    for url in blog_spider.urls:
        url_queue.put(url)

    ##3���������̣߳������߲����м�������Ե�html_queue
    for idx in range(3):
        ##name=f"craw{idx}"��ʾ�߳�����
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue),
                             name=f"craw{idx}")
        t.start()

    ##2���������̶߳�html_queue���д���
    fout = open("02.data.txt", "w")
    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, fout),
                             name=f"parse{idx}")
        t.start()
