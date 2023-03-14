from Cracked_Mods_Checker import CrackedMods
import requests
import json

# Url
headers = {'Accept': 'application/json'}
url = 'https://mods.factorio.com/api/mods?page=1'
response = requests.get(url, headers=headers)
result_json = json.dumps(response.json(), indent=2)

# Finder
items = json.loads(str(result_json))
item = items['pagination']
links = item['links']
last_link = links['last']

# Last_Page
page = int((last_link[last_link.find("=") + 1 : ]))


# All mods Finder

def all_mods_checker(pages):

    all_mods_list = []

    for page in range(pages):
        mods = requests.get(f'https://mods.factorio.com/api/mods?page={page}', headers=headers)
        res = json.dumps(mods.json(), indent=2)

        items = json.loads(str(res))
        mods_res = items['results']
        for mod in mods_res:
            mod_name = mod['name']
            all_mods_list.append(mod_name)
    
    return all_mods_list

print(all_mods_checker(page))


