import blog_spider
import threading
import time


def single_thread():
    print("single_thread begin")
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print("single_thread end")


def multi_thread():
    print("multi_thread begin")
    threads = []
    ##开启了50个线程，因为blog_spider.urls有50个
    for url in blog_spider.urls:
        threads.append(
            ##(url,)表示其元组，(url)表示的是字符串
            threading.Thread(target=blog_spider.craw, args=(url,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("multi_thread end")


if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single thread cost:", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi thread cost:", end - start, "seconds")
