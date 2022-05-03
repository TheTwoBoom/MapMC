import install
install.install("colorama")
install.install("easygui_qt")
install.install("argparse")
import subprocess
import sys
from glob import glob
import os
import json
import shutil
from colorama import *
from argparse import ArgumentParser
import easygui_qt
import version_detect

print(Fore.WHITE + Back.BLACK + "Welcome in MapMC!")

parser = ArgumentParser()
args = parser.parse_args()

folder = easygui_qt.easygui_qt.get_directory_name(title='Select a folder')
if folder == '':
    easygui_qt.easygui_qt.get_abort(message='You must select a folder!', title='MapMC')
parser.add_argument("-f", "--folder", dest=folder, default="")
os.chdir(folder)
directory = os.getcwd()
os.chdir('advancements')
version_detect.version()
print(Fore.WHITE + Back.BLACK + "Map wird in Minecraft verschoben!")
try:
    os.chdir(directory)
    original = os.getcwd()
    target = os.getenv('APPDATA') + "\.minecraft\saves"
    shutil.move(original, target)
except PermissionError:
    pass
