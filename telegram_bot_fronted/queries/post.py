import telegram_bot_fronted.queries.environment
from urllib.request import urlopen
import requests
import json

base_url = telegram_bot_fronted.queries.environment.base_url

def post_new_item(name:str, parents:str,description:str,id_in:int):
    url = base_url+"items/new/"
    my_data = {
                'name': name,
                'parents':parents,
                'description': description,
                'user_id': id_in
            }
    r = requests.post(url, json = my_data)

def post_new_user(id_in:int,name:str,username:str ):
    url = base_url+"users/new/"
    my_data = {
                'id': id_in,
                'name': name,
                'username': username
            }
    return requests.post(url, json = my_data)

def post_aprove_mirror(id,credits):
    url = base_url+"items/mirror/aprove"
    my_data = {
                'id': int(id),
                'credits': int(credits)
            }
    r = requests.post(url, json = my_data)

def post_set_admin(username):
    url = base_url+"users/set_admin/?username="+username
    response = urlopen(url)
    return json.loads(response.read())