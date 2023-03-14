from Cracked_Mods_Checker import CrackedMods
import requests
import json
import os

class Checker():

    headers = {'Accept': 'application/json'}

    def pages():
        # Url
        headers = Checker.headers
        url = 'https://mods.factorio.com/api/mods?page=1'
        response = requests.get(url, headers=headers)
        result_json = json.dumps(response.json(), indent=2)

        # Finder
        items = json.loads(str(result_json))
        item = items['pagination']
        links = item['links']
        last_link = links['last']

        # Last_Page
        pages = int((last_link[last_link.find("=") + 1 : ]))

        return pages

    # All mods Finder
    def all_mods_checker():

        all_mods_list = []

        pages = Checker.pages()
        # Mods Checker

        for page in range(pages):
            mods = requests.get(f'https://mods.factorio.com/api/mods?page={page}', headers=Checker.headers)
            res = json.dumps(mods.json(), indent=2)
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
        
        with open('factorio-loader/mods.json', 'w', encoding='UTF-8') as f:
            json.dump(all_mods_list, f, ensure_ascii=False, indent=4)
            f.close

        return all_mods_list

