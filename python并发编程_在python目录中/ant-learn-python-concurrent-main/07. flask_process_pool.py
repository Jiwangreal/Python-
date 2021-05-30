import flask
from concurrent.futures import ProcessPoolExecutor
import math
import json


app = flask.Flask(__name__)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

##执行的时候，将将route中的<numbers>作为参数，传递到numbers这里面
@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    ##numbers是一个字符串
    number_list = [int(x) for x in numbers.split(",")]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))


if __name__ == "__main__":
    ##多进程与多线程写法上的区别：
    ##因为多进程他们环境之间是相互完全隔离的，在定义process_pool时，他所依赖使用的函数都必须得声明定义完毕
    ##所以process_pool必须放在所有依赖函数的最下面才可以使用
    ##然而多线程的定义放到哪都行
    ##在flask中使用多进程的方式，必须放到__main__下面，在app.run()之前初始化process_pool = ProcessPoolExecutor()
    process_pool = ProcessPoolExecutor()
    app.run()
