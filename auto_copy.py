import shutil
import os
import argparse

mod_dir = os.path.expanduser("C:\\Users\\Alexandros\\Games\\Age of Empires 2 DE\\76561198151190400\\mods\\local\\Age of Madness - Knights of Coconut\\resources\\")
aoe_game_dir = os.path.expanduser("D:\\Spiele\\Steam\\steamapps\\common\\AoE2DE\\resources\\")
orig_files_dir = os.path.expanduser("C:\\Users\\Alexandros\\Games\\Age of Empires 2 DE\\76561198151190400\\mods\\local\\Age of Madness - Knights of Coconut\\original_data\\resources\\")

def copy_files(src, dest):
    print(f"Copying files from '{src}' to '{dest}'...")
    if not os.path.exists(src):
        print(f"Source path '{src}' does not exist.")
        return

    if not os.path.exists(dest):
        print(f"Destination path '{dest}' does not exist.")
        return

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        print(f"Copying '{s}' to '{d}'...")
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    print(f"Files copied from '{src}' to '{dest}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy files from Mod Directory to Game Directory")
    parser.add_argument("--restore", action="store_true", help="Restore original files in Game Directory.")

    args = parser.parse_args()

    if args.restore:
        print("Restoring original files...")
        copy_files(orig_files_dir, aoe_game_dir)
    else:
        print("Copying files from Mod Directory to Game Directory...")
        copy_files(mod_dir, aoe_game_dir)