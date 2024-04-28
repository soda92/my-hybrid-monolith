# -*- mode: python -*-
# -*- coding: utf-8 -*-

"""
This is a PyInstaller spec file.
"""

import os
from PyInstaller.building.api import PYZ, EXE, COLLECT
from PyInstaller.building.build_main import Analysis
from PyInstaller.utils.hooks import is_module_satisfies
from PyInstaller.archive.pyz_crypto import PyiBlockCipher

# Constants
DEBUG = os.environ.get("CEFPYTHON_PYINSTALLER_DEBUG", False)
PYCRYPTO_MIN_VERSION = "2.6.1"

cipher_obj = None

a = Analysis(
    ["../wxpython.py"],
    hookspath=["."],  # To find "hook-cefpython3.py"
    cipher=cipher_obj,
    win_private_assemblies=True,
    win_no_prefer_redirects=True,
)

if not os.environ.get("PYINSTALLER_CEFPYTHON3_HOOK_SUCCEEDED", None):
    raise SystemExit("Error: Pyinstaller hook-cefpython3.py script was "
                     "not executed or it failed")

pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=cipher_obj)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name="cefapp",
          debug=DEBUG,
          strip=False,
          upx=False,
          console=DEBUG,
          icon="../resources/wxpython.ico")

COLLECT(exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=False,
        name="cefapp")