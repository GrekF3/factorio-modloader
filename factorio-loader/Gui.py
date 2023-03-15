from time import sleep
import Cracked_Mods_Checker
import dearpygui.dearpygui as dpg
import json
from Cracked_Mods_Checker import CrackedMods
import requests
import json
import os

# FACTORIO MODS CHECKER
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
            dpg.set_value('pages', f'{page}/{pages}')
            mods = requests.get(f'https://mods.factorio.com/api/mods?page={page}', headers=Checker.headers)
            res = json.dumps(mods.json(), indent=2)
            items = json.loads(str(res))
            mods_res = items['results']
            for mod in mods_res:
                try:
                    mod_name = mod['title']
                except:
                    mod_name = 'No name'

                try:
                    factorio_version = mod['latest_release']['info_json']['factorio_version']
                except:
                    factorio_version = 'No Version'
                
                try:
                    mod_version = mod['latest_release']['version']
                except:
                    mod_version = 'No Mod Version'
                
                try:
                    mod_desctiption = mod['summary']
                except:
                    mod_desctiption = 'No Nod Desctiprion'
                
                try:
                    mod_owner = mod['owner']
                except:
                    mod_owner = 'No Mod Owner'

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





dpg.create_context()

# mods_picker
activated = []
def Mods_Picker(Sender):
    if dpg.get_value(Sender) == True:
        activated.append(Sender)
        print(activated)
    else:
        activated.remove(Sender)
        print(activated)

def Checker_Mods():
    Checker.all_mods_checker()

        
def Updater():
    dpg.hide_item('Mods_group')
    dpg.hide_item('Update_button')
    dpg.show_item('Update_Window')

    Checker.all_mods_checker()

    dpg.show_item('Mods_group')
    dpg.show_item('Update_button')
    dpg.hide_item('Update_Window')

with dpg.window(tag="Main"):
    
    dpg.add_text("Created by GrekF3", bullet=True)
    search = dpg.add_input_text(label="Mod Name", width=500, callback=lambda s, a: dpg.set_value('mod_filter', a))
    with dpg.group(horizontal=True):
         dpg.add_button(label='Update Mods', callback=Updater, tag='Update_button')
    with dpg.group(horizontal=False, tag='Update_Window', show=False):
        dpg.add_loading_indicator(show=True)
        dpg.add_text(tag='pages')
    try:
        mods_list = []
        with open('factorio-loader/mods.json', 'r', encoding='UTF-8') as r:
            data = json.load(r)
            for mods in data:
                mod_name = mods.get('Название мода:')
                mod_version = mods.get('Версия Факторио:')
                mod = {
                    'mod_name': mod_name,
                    'mod_version': mod_version,
                }
                mods_list.append(mod)
            r.close
        dpg.add_text('Aviabled mods:')
        with dpg.child_window(tag='Mods_group', show=True, height=-1, width=-1):
            with dpg.filter_set(tag="mod_filter"):
                for mod in mods_list:
                    dpg.add_checkbox(label=mod.get('mod_name') + ' | ' + 'FACTORIO VERSION: ' + mod.get('mod_version'), tag=mod.get('mod_name'), callback=Mods_Picker, filter_key=mod.get('mod_name'))
    except:
         pass
    

    

dpg.create_viewport(title='Factorio Mods Downloader', width=1000)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Main", True)
dpg.start_dearpygui()
dpg.destroy_context()