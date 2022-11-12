import os
from urllib.request import urlopen
import json
base_url = os.environ['base_url']

def get_all_items():
    url = base_url + "items/all"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

def get_all_mirror():
    url = base_url +"items/mirror"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

def get_items_from_id(id):
    url = base_url +"items/from/?user_id="+str(id)
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json 

def get_mirror_from_id(id):
    url = base_url +"items/mirror/from/?user_id="+str(id)
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json    

def get_all_users():
    url = base_url +"users/all"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json    

def get_item_from_id(id):
    url = base_url +"items/from/?user_id="+str(id)
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json    

def get_error_new():
    url = base_url +"items/new/error"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json    

def get_item_for_parents(id):
    url = base_url +"items/primes"
    response = urlopen(url)
    data_json = json.loads(response.read())
    
    url = base_url +"items/from/?user_id="+str(id)
    response = urlopen(url)
    read = json.loads(response.read())
    for item in read:
        data_json+=[item['name']]
    return data_json      

def get_aprove_list(id):
    url = base_url +"items/from/aprove/?user_id="+str(id)
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json 

def get_data_from_user(id):
    url = base_url +"users/data/?id="+str(id)
    response = urlopen(url)
    return json.loads(response.read())

def get_user_from_item(id):
    url = base_url +"items/user_from/?id="+str(id)
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json    

def get_all_users():
    url = base_url +"users/all"
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json    

def get_credits_from_user(user_id):
    url = base_url +"users/credits/?user_id="+str(user_id)
    response = urlopen(url)
    data_json = json.loads(response.read())
    return int(data_json['credits'])    
