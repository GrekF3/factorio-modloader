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

    for page in range(1):
        mods = requests.get(f'https://mods.factorio.com/api/mods?page={page}', headers=headers)
        res = json.dumps(mods.json(), indent=2)

        print(f'Работаю над страницей {page}')

        items = json.loads(str(res))
        mods_res = items['results']
        for mod in mods_res:
            mod_name = mod['title']
            factorio_version = mod['latest_release']['info_json']['factorio_version']
            mod_version = mod['latest_release']['version']
            mod_desctiption = mod['summary']
            mod_owner = mod['owner']

            mod = {
                'Название мода:':mod_name,
                'Версия Факторио:':factorio_version,
                'Версия Мода:':mod_version,
                'Описание мода:':mod_desctiption,
                'Автор мода:':mod_owner,
            }

            all_mods_list.append(mod)
    
    return all_mods_list




