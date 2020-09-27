#!C:\Users\User\PycharmProjects\PyCharm\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'navi==0.1.0a19','console_scripts','navi-create'
__requires__ = 'navi==0.1.0a19'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('navi==0.1.0a19', 'console_scripts', 'navi-create')()
    )
