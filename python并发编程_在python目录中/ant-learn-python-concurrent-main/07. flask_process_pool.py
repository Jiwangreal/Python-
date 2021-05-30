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

##ִ�е�ʱ�򣬽���route�е�<numbers>��Ϊ���������ݵ�numbers������
@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    ##numbers��һ���ַ���
    number_list = [int(x) for x in numbers.split(",")]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))


if __name__ == "__main__":
    ##���������߳�д���ϵ�����
    ##��Ϊ��������ǻ���֮�����໥��ȫ����ģ��ڶ���process_poolʱ����������ʹ�õĺ���������������������
    ##����process_pool���������������������������ſ���ʹ��
    ##Ȼ�����̵߳Ķ���ŵ��Ķ���
    ##��flask��ʹ�ö���̵ķ�ʽ������ŵ�__main__���棬��app.run()֮ǰ��ʼ��process_pool = ProcessPoolExecutor()
    process_pool = ProcessPoolExecutor()
    app.run()
