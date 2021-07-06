
from pprint import pprint

import requests

from ya_disk import YandexDisk

TOKEN = "AQAAAAA9roRjAADLWwSba_R74EPPujOnSoQgPyg"

#
# def test_request():
#    url = "https://httpbin.org/get"
#    params = {"model": "nike321"}
#    headers = {"Authorization": "secret - token - 123"}
#    timeout = 5
#    response = requests.get(url, params=params, headers=headers, timeout=timeout)
#    if response.status_code != 200:
#       print("ERROR")
#       return
#    # pprint(response)
#    pprint(response.json())

if __name__ == '__main__':
   ya = YandexDisk(token = TOKEN)
   # pprint(ya.get_files_list())
   ya.upload_file_to_disk(disk_file_path='netology', filename='data3.txt')
