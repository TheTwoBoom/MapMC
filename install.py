def install(paket):
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', paket])
def upgrade():
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', paket])
