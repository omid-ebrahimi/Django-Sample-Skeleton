#!H:\Web-Programming\Python\Practices\Books\Virtual-Environment\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==0.8','console_scripts','easy_install'
__requires__ = 'setuptools==0.8'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('setuptools==0.8', 'console_scripts', 'easy_install')()
    )
