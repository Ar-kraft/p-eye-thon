from pprint import pprint

import requests

# def sphero_request():
#     url = "https://www.superheroapi.com/api.php/2619421814940190/"
#     id = "332/"
#     stats = "powerstats/"
#     timeout = 5
#     response = requests.get(url+id+stats, timeout=timeout)
#     pprint(response.json())
#
# if __name__ == '__main__':
#     sphero_request()

def sphero_request_raw(name):
    url = "https://www.superheroapi.com/api.php/2619421814940190/"
    search = "search/"
    # name = input('Enter name of')
    name = name
    timeout = 5
    response = requests.get(url+search+name, timeout=timeout)
    output_classified = (response.json())
    print(output_classified['results'][0]['powerstats']['intelligence'])
    return output_classified['results'][0]['powerstats']['intelligence']

char1 = 'Hulk'
char2 = 'Captain America'
char3 = 'Thanos'

# if __name__ == '__main__':
    # sphero_request_raw(char1)
    # sphero_request_raw(char2)
    # sphero_request_raw(char3)

num1 = int(sphero_request_raw(char1))
num2 = int(sphero_request_raw(char2))
num3 = int(sphero_request_raw(char3))

if(num1 > num2):
    if(num1 > num3):
        print("Smartest hero is "+ str(char1))
    else:
        print("Smartest hero is "+ str(char3))
else:
    if(num2 > num3):
        print("Smartest hero is " + str(char2))
    else:
        print("Smartest hero is " + str(char3))

# array_of_id = {'Hulk': '332', 'Captain America': '149'}
#
# def sphero_request_id():
#     url = "https://www.superheroapi.com/api.php/2619421814940190/"
#     ID = array_of_id['Hulk']+"/"
#     stats = "powerstats/"
#     timeout = 5
#     response = requests.get(url+ID+stats, timeout=timeout)
#     output_dict = (response.json())
#     pprint(output_dict["intelligence"])
#
# if __name__ == '__main__':
#     sphero_request_id()
