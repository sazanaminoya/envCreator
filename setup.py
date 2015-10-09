# coding: utf-8

from distutils.core import setup

import py2exe, sys, os

if hasattr(sys, 'setdefaultencoding'):
    import locale
    lang, enc = locale.getdefaultlocale()
    sys.setdefaultencoding(enc or 'cp932')
    del sys.setdefaultencoding

sys.argv.append('py2exe')

option = {
    'bundle_files': 1,
    'compressed': True
}

setup(
    options = {
        'py2exe': option
    },
    console = [
        {'script': 'envCreator.py'}
    ],
    zipfile = None #'envCreator.zip' 
)
