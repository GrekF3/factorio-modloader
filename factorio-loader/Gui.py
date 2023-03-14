from time import sleep
import Cracked_Mods_Checker
from Factorio_Mods_checker import Checker
import dearpygui.dearpygui as dpg
import json

dpg.create_context()


def Mod_Finder(sender, app_data):
    mod = dpg.get_value('Mod_name')
    print(mod)

def Updater(sender, pages):
        dpg.hide_item('Mods_List')
        pages = Checker.pages()
        Checker.all_mods_checker()
        progress_value = 1/pages
        dpg.show_item('Updater_Bar')
        i = progress_value
        while i < 1:
            i = i + progress_value
            print(i)
            sleep(0.5)
            dpg.set_value('Updater_Bar', i)
        
        dpg.show_item('Updated')
        dpg.show_item('Mods_List')


with dpg.window(tag="Primary Window"):
    
    dpg.add_text("Created by GrekF3", bullet=True)
    search = dpg.add_input_text(label="Mod Name", width=500, tag='Mod_name')
    dpg.add_button(label='Search', callback=Mod_Finder)

    dpg.add_button(label='Update Mods', callback=Updater)
    dpg.add_progress_bar(show=False, default_value=0.0, label='Update...', tag='Updater_Bar')
    dpg.add_text('Mods Updated', show=False, tag='Updated')

    try:
        mods_list = []
        with open('factorio-loader/mods.json', 'r', encoding='UTF-8') as r:
            data = json.load(r)
            for mods in data:
                mod_name = mods.get('Название мода:')
                mods_list.append(mod_name)
            r.close
        dpg.add_listbox(items=mods_list, show=True, tag='Mods_List', width=400, label='Aviable Mods')
    except:
         pass
    

    


dpg.create_viewport(title='Factorio Mods Downloader', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()