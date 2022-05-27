def install(paket):
    import subprocess
    import sys
    subprocess.check_call(['pip', 'install', paket])
def install_all():
    import subprocess
    import sys
    subprocess.check_call(['pip install -r requirements.txt'])
def upgrade():
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', "pip"])

upgrade()
install("matplotlib")
install("numpy")
install("colorama")
install("easygui_qt")
install("nbtlib")
install("Pillow")
install("requests")
install("tqdm")
install("urllib3")
install("minecraft_launcher_lib")
