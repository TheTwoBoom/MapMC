import minecraft_launcher_lib
import subprocess
import os
import json
import shutil
from colorama import *
import easygui_qt
import version_detect
import requests

print(Fore.WHITE + Back.BLACK + "Welcome in MapMC!")
input_folder = easygui_qt.easygui_qt.get_directory_name(title='Select the MapMC input folder')
if input_folder == '':
    easygui_qt.easygui_qt.get_abort(message='You must select a folder!', title='MapMC')

os.chdir(input_folder)
directory = os.getcwd()
os.chdir('advancements')
mc_version = version_detect.version()
easygui_qt.easygui_qt.show_message(message="Map is moved to Minecraft!", title='MapMC')
try:
    os.chdir(directory)
    original = os.getcwd()
    target = minecraft_launcher_lib.utils.get_minecraft_directory() + "\saves"
    shutil.move(original, target)
except PermissionError:
    pass
name = "Notch"
options = {
    "username": name,
}
mc_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(mc_version, mc_directory, options)
minecraft_launcher_lib.fabric.install_fabric(mc_version, mc_directory)
subprocess.call(minecraft_command)
