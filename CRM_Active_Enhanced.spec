# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('D:\\TOOLS\\DIRECT .EXE BUILDER\\modules', 'modules')],
    hiddenimports=['modules', 'modules.constants', 'modules.logger_config', 'modules.utils', 'modules.db_manager', 'modules.address_book_gui', 'modules.file_creator_gui', 'modules.file_search_gui', 'modules.settings_gui', 'modules.lotting_system_gui', 'modules.dialogs', 'modules.screenshot_monitor', 'modules.crm_display_scaling', 'modules.enhanced_beautiful_gui', 'modules.beautiful_styling', 'modules.enhanced_standardized_integration', 'modules.migration_tools_gui', 'modules.customizations', 'modules.standardized_directory', 'modules.standardized_naming', 'tkinter', 'tkinter.ttk', 'tkinter.filedialog', 'tkinter.messagebox', 'sqlite3', 'json', 'datetime', 'random', 're', 'platform', 'subprocess', 'tempfile', 'logging', 'traceback', 'os', 'sys', 'PIL', 'PIL.Image', 'win32clipboard', 'win32con'],
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
    name='CRM_Active_Enhanced',
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
