# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['--add-binaryC:\\Users\\Windows 10\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\tabula\\tabula-1.0.4-jar-with-dependencies.jar;\\tabula', 'login.py'],
             pathex=['D:\\zayd\\PROJECT_SEM_2\\working'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='D:\\zayd\\PROJECT_SEM_2\\working\\icon.ico')
