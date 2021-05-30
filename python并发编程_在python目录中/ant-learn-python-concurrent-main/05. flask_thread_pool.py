import flask
import json
import time
from concurrent.futures import ThreadPoolExecutor

##�������
app = flask.Flask(__name__)

##��ʼ��һ��pool����
pool = ThreadPoolExecutor()


def read_file():
    ##100���룬sleepģ��IO����
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
    # ����pool
    ##ģ���ȡweb��3����������
    # result_file = read_file
    # result_db = read_db
    # result_api = read_api

    # return json.dumps({
    #     "result_file": result_file,
    #     "result_db": result_db,
    #     "result_api": result_api,
    # })


    # ʹ��pool
    ##ģ���ȡweb��3����������
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)

    return json.dumps({
        "result_file": result_file.result(),
        "result_db": result_db.result(),
        "result_api": result_api.result(),
    })


if __name__ == "__main__":
    ##����flask����
    app.run()
