import pywinauto
from pywinauto.application import Application, WindowSpecification
import pyautogui
from time import sleep
import keyboard
import argparse


# while True:
#     print(f"({pyautogui.position().x}, {pyautogui.position().y})")
#     sleep(1)

# options_button = (2139, 87)
# mods_button = (1754, 624)
# mods_button = (-1510, 1168)
# my_mods_button = (-1089, 312)
# import_mods_button = (-712, 1147)
# back_button = (-1490, 1148)
# singleplayer_button = (-1526, 549)
# skirmish_button = (-1172, 790)
# data_mod_button = (-356, 526)
# age_of_madness_button = (-463, 574)
# start_game_button = (-929, 1145)
# my_mods_button = (1555, 96)
# import_mods_button = (2074, 1176)
# back_button = (1039, 1182)
# singleplayer_button = (1012, 414)
# skirmish_button = (1447, 723)
# data_mod_button = (2431, 369)
# age_of_madness_button = (2295, 434)
# start_game_button = (1765, 1173)

# menu_button = (-39, 299)
# quit_game_button = (-942, 655)
# sure_button = (-1094, 823)
# ok_button = (-1025, 819)
# return_to_menu_button = (-1503, 1142)
#quit_game_button = (1714, 543)
# sure_button = (1531, 756)
# ok_button = (1636, 756)
# return_to_menu_button = (1027, 1170)

# print("TOOD FIX THIS SHIT APPLICATION")
# exit()

# New Coords
# Game_Menu = (1887, 54)
# Restart_Game = (975, 657)
# Yes_Sure = (812, 584)
# Fail_OK = (967, 668)

Game_Menu = (1887, 56)
Restart_Game = (972, 658)
Yes_Sure = (813, 585)
Error_OK = (972, 670)
Mods = (408, 932)
My_Mods = (852, 65)
Import_Mods = (1220, 904)
Back = (442, 905)
Singleplayer = (415, 300)
Skirmish = (763, 547)
Data_Mod = (1516, 285)
Age_of_Madness = (1475, 329)
Start_Game = (995, 907)


def list_open_Apps():
    desktop = pywinauto.Desktop(backend="uia")
    for window in desktop.windows():
        print(window.window_text())
    

def list_coords_loop(main_dlg : WindowSpecification):

    vs_app = pywinauto.Application().connect(title_re=".*Visual Studio Code")
    vs_dlg = vs_app.top_window()
    vs_rect = vs_dlg.rectangle()
    vs_width, vs_height = int(vs_rect.right - vs_rect.left), int(vs_rect.bottom - vs_rect.top)


    coords = []
    if main_dlg:
        rect = main_dlg.rectangle()
        x, y = rect.left, rect.top
    else:
        x,y = 0,0
    print(f"Coordinates of main_dlg: ({x}, {y})")
    while True:
        current_x, current_y = pyautogui.position().x - x, pyautogui.position().y - y
        print(f"({current_x}, {current_y})")
        if keyboard.is_pressed(hotkey="a"):
            vs_dlg.set_focus()     
            vs_dlg.wait('ready')  
            vs_dlg.click_input(coords=((vs_width // 2, vs_height - 50)))
            loc_name = input("Location Name?")
            coords.append((loc_name,f"({current_x}, {current_y})"))
            main_dlg.set_focus()
            main_dlg.click_input(coords=(current_x,current_y))

        
        if keyboard.is_pressed(hotkey="q"):
            break

    return coords



def openApp():
    app = Application().connect(title_re="Age of Empires II: Definitive Edition")
    # app = Application().connect(title_re=".*Notepad", class_name="Notepad")
    app.top_window().click_input(coords=(100, 100))
    main_dlg = app.top_window()
    
    # app = Application().start('notepad.exe', timeout=10)
    # app = Application().connect(title_re=".*Notepad", class_name="Notepad")
    # app = Application(backend="uia").connect(path=r"D:\\Spiele\\Steam\\steamapps\\common\\AoE2DE\\AoE2DE_s.exe")

    # main_dlg = app.MainDialog.click_input(coords=(100, 200))

    # main_dlg = app.window(title_re="Age of Empires II.*")
    try:
        main_dlg.wait('ready')
    except TimeoutError:
        print("App not Ready")
        exit()

    return main_dlg

def fromMenu(main_dlg):

    #print("Visible")
    # main_dlg.click_input(coords=options_button)
    # sleep(.1)
    main_dlg.click_input(coords=Mods)
    sleep(.1)
    main_dlg.click_input(coords=My_Mods)
    sleep(.1)
    main_dlg.click_input(coords=Import_Mods)
    sleep(4)
    main_dlg.click_input(coords=Back)
    sleep(.1)
    main_dlg.click_input(coords=Singleplayer)
    sleep(.1)
    main_dlg.click_input(coords=Skirmish)
    sleep(1)
    main_dlg.click_input(coords=Data_Mod)
    sleep(.1)
    main_dlg.click_input(coords=Age_of_Madness)
    # pywinauto.mouse.double_click(button='left', coords=Age_of_Madness)
    sleep(4)
    main_dlg.click_input(coords=Start_Game)


def fromGame(main_dlg):
    main_dlg.click_input(coords=Game_Menu)
    sleep(.1)
    main_dlg.click_input(coords=Restart_Game)
    sleep(.2)
    main_dlg.click_input(coords=Yes_Sure)
    sleep(2)
    main_dlg.click_input(coords=Error_OK)
    sleep(2)
    fromMenu(main_dlg)

# import win32api
# import time
# while True:
#     x, y = win32api.GetCursorPos()
#     print(x,y)
#     time.sleep(1)

# main_dlg.print_control_identifiers()

# main_dlg.SystemMenuItem.click_input()

#(['TitleBar', 'System', 'Menu', 'SystemMenu', 'System0', 'System1', 'System2', 'SystemMenuItem', 'MenuItem', 'Button', 'MinimiseButton', 'Minimise', 'Maximise', 'MaximiseButton', 'Button0', 'Button1', 'Button2', 'Close', 'Button3', 'CloseButton'])'

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Automatically load mod and start new Game")
    parser.add_argument("--list", action="store_true", help="List all Window names")
    parser.add_argument("--coords", action="store_true", help="List all Window names")

    args = parser.parse_args()
    if args.list:
        list_open_Apps()
        exit()


    if args.coords:
        main_dlg = openApp()
        coords = list_coords_loop(main_dlg)
        for c in coords:
            print(f"{c[0]} = {c[1]}")
        exit()
    
    usrin = input("Ingame something, menu just enter")
    main_dlg = openApp()
    if usrin:
        fromGame(main_dlg)
    else:
        fromMenu(main_dlg)
