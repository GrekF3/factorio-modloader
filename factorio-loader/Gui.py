from time import sleep
import Cracked_Mods_Checker
from Factorio_Mods_checker import Checker
import dearpygui.dearpygui as dpg
import json



dpg.create_context()


def Mod_Finder(sender, app_data):
    mod = dpg.get_value('Mod_name')
    print(mod)

# mods_picker
activated = []
def Mods_Picker(Sender):
    if dpg.get_value(Sender) == True:
        activated.append(Sender)
        print(activated)
    else:
        activated.remove(Sender)
        print(activated)
         
        
def Updater():
        dpg.hide_item('Mods_group')
        dpg.show_item('Update_Window')

        Checker.all_mods_checker()

        dpg.show_item('Updated')
        dpg.show_item('Mods_group')


with dpg.window(tag="Main"):
    
    dpg.add_text("Created by GrekF3", bullet=True)
    search = dpg.add_input_text(label="Mod Name", width=500, tag='Mod_name')
    with dpg.group(horizontal=True):
         dpg.add_button(label='Search', callback=Mod_Finder)
         dpg.add_button(label='Update Mods', callback=Updater)
    with dpg.group(horizontal=False, tag='Update_Window', show=False):
        dpg.add_progress_bar(show=True, default_value=0.0,tag='Updater_Bar',label='Update...')
        dpg.add_loading_indicator(show=True)
    dpg.add_text('Mods Updated', show=False, tag='Updated')

    try:
        mods_list = []
        with open('factorio-loader/mods.json', 'r', encoding='UTF-8') as r:
            data = json.load(r)
            for mods in data:
                mod_name = mods.get('Название мода:')
                mods_list.append(mod_name)
            r.close
        dpg.add_text('Aviabled mods:')
        with dpg.group(horizontal=False, tag='Mods_group', show=True):
            for mod in mods_list:
                dpg.add_checkbox(label=mod, tag=mod, callback=Mods_Picker)
    except:
         pass
    

    


dpg.create_viewport(title='Factorio Mods Downloader', width=1000, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Main", True)
dpg.start_dearpygui()
dpg.destroy_context()