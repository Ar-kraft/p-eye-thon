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

class YandexDisk:
    def __init__(self, token):
        self.token = token
    def get_headers(self):
        return{
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json
    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, 'overwrite':"true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
