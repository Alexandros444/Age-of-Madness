import pywinauto
from pywinauto.application import Application
import pyautogui
from time import sleep

# while True:
#     print(f"({pyautogui.position().x}, {pyautogui.position().y})")
#     sleep(1)

# options_button = (2139, 87)
# mods_button = (1754, 624)
mods_button = (-1510, 1168)
my_mods_button = (-1089, 312)
import_mods_button = (-712, 1147)
back_button = (-1490, 1148)
singleplayer_button = (-1526, 549)
skirmish_button = (-1172, 790)
data_mod_button = (-356, 526)
age_of_madness_button = (-463, 574)
start_game_button = (-929, 1145)
# my_mods_button = (1555, 96)
# import_mods_button = (2074, 1176)
# back_button = (1039, 1182)
# singleplayer_button = (1012, 414)
# skirmish_button = (1447, 723)
# data_mod_button = (2431, 369)
# age_of_madness_button = (2295, 434)
# start_game_button = (1765, 1173)

menu_button = (-39, 299)
quit_game_button = (-942, 655)
sure_button = (-1094, 823)
ok_button = (-1025, 819)
return_to_menu_button = (-1503, 1142)
#quit_game_button = (1714, 543)
# sure_button = (1531, 756)
# ok_button = (1636, 756)
# return_to_menu_button = (1027, 1170)

print("TOOD FIX THIS SHIT APPLICATION")
exit()

def openApp():
    # app = Application().start('notepad.exe', timeout=10)

    app = Application(backend="uia").connect(path=r"D:\\Spiele\\Steam\\steamapps\\common\\AoE2DE\\AoE2DE_s.exe")

    main_dlg = app.MainDialog.click_input(coords=(100, 200))

    # main_dlg = app.window(title_re="Age of Empires II.*")
    main_dlg.wait('visible')

    return main_dlg

def fromMenu(main_dlg):

    #print("Visible")
    # main_dlg.click_input(coords=options_button)
    # sleep(.1)
    main_dlg.click_input(coords=mods_button)
    sleep(.1)
    main_dlg.click_input(coords=my_mods_button)
    sleep(.1)
    main_dlg.click_input(coords=import_mods_button)
    sleep(4)
    main_dlg.click_input(coords=back_button)
    sleep(.1)
    main_dlg.click_input(coords=singleplayer_button)
    sleep(.1)
    main_dlg.click_input(coords=skirmish_button)
    sleep(.1)
    main_dlg.click_input(coords=data_mod_button)
    sleep(.1)
    pywinauto.mouse.double_click(button='left', coords=age_of_madness_button)
    sleep(4)
    main_dlg.click_input(coords=start_game_button)


def fromGame(main_dlg):
    main_dlg.click_input(coords=quit_game_button)
    sleep(.1)
    main_dlg.click_input(coords=sure_button)
    sleep(.1)
    main_dlg.click_input(coords=ok_button)
    sleep(.1)
    main_dlg.click_input(coords=return_to_menu_button)
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
    usrin = input("Ingame something, menu just enter")
    main_dlg = openApp()
    if usrin:
        fromGame(main_dlg)
    else:
        fromMenu(main_dlg)
