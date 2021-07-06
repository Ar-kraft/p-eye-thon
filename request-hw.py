from pprint import pprint

import requests


def test_request():
    url = "https://httpbin.org/get"
    params = {"model": "nike321"}
    headers = {"Authorization": "secret - token - 123"}
    timeout = 5
    response = requests.get(url, params=params, headers=headers, timeout=timeout)
    if response.status_code !=200:
        print("ERROR")
        return
    #pprint(response)
    pprint(response.json())

if __name__ == '__main__':
    test_request()