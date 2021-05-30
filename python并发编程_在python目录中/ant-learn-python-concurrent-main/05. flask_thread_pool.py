import flask
import json
import time
from concurrent.futures import ThreadPoolExecutor

##起个名字
app = flask.Flask(__name__)

##初始化一个pool对象
pool = ThreadPoolExecutor()


def read_file():
    ##100毫秒，sleep模拟IO操作
    time.sleep(0.1)
    return "file result"


def read_db():
    time.sleep(0.2)
    return "db result"


def read_api():
    time.sleep(0.3)
    return "api result"


@app.route("/")
def index():
    # 不用pool
    ##模拟读取web的3个三个操作
    # result_file = read_file
    # result_db = read_db
    # result_api = read_api

    # return json.dumps({
    #     "result_file": result_file,
    #     "result_db": result_db,
    #     "result_api": result_api,
    # })


    # 使用pool
    ##模拟读取web的3个三个操作
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)

    return json.dumps({
        "result_file": result_file.result(),
        "result_db": result_db.result(),
        "result_api": result_api.result(),
    })


if __name__ == "__main__":
    ##启动flask方法
    app.run()
