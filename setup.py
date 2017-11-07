import sys
from cx_Freeze import setup, Executable

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base=None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable('Interface.py', base=base)
]

options={
    'build_exe':{
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR,'DLLS', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
        ],
    },
}


setup(name = 'Interface',
      version = '1.0',
      description = "App calculant une plage ip par rapport à un nombre d'hote",
      options = options,
      executables = executables
      )