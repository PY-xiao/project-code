import sys
import os
import PyInstaller.__main__

# 文件列表
files = ['music.py', 'index.py', 'demo.py']

# 设置 PyInstaller 参数
params = [
    '--onefile',               # 生成一个独立的可执行文件
    '--windowed',              # 隐藏命令行窗口
    '--add-data', ','.join([f + ';' + f for f in files])  # 添加源码文件到可执行文件中
]

# 添加依赖模块
modules = ['os', 'sys', 'time', 'random', 'PyQt5', 'pygame', 'tkinter', 'mutagen']
params.extend(['--hidden-import', module] for module in modules)

# 执行 PyInstaller 打包
PyInstaller.__main__.run(params + files)