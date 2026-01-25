# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Gild56\\Documents\\vscode_folder\\gd_numworks\\gd.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Gild56\\Documents\\vscode_folder\\gd_numworks\\emulator.py', '.'), ('C:\\Users\\Gild56\\Documents\\vscode_folder\\gd_numworks\\ion.py', '.'), ('C:\\Users\\Gild56\\Documents\\vscode_folder\\gd_numworks\\resources', 'resources/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='geometry_works_v1.1.1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
