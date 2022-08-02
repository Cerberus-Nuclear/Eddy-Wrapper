# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Projects\\Eddy-Wrapper\\eddymc_wrapper\\eddy_wrapper.py'],
             pathex=['C:\\Projects\\Eddy-Wrapper\\eddymc_wrapper'],
             binaries=[],
             datas=[('C:\\Projects\\Eddy-core\\eddymc_core\\static\\style.css', '.\\static'),
                    ('C:\\Projects\\Eddy-core\\eddymc_core\\static\\MCNP_template.html', '.\\static'),
                    ('C:\\Projects\\Eddy-core\\eddymc_core\\static\\SCALE_template.html', '.\\static'),
                    ],
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
          [],
          exclude_binaries=True,
          name='Eddy_0.4.3',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Eddy_exe')
