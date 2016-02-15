"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
import sys
import os.path
from setuptools import setup, find_packages
import py2exe


APP = ['opencmiss/neon/neon.py']
DATA_FILES = [('bin', [os.path.join('..', 'bin', 'ventilation-' + sys.platform + '.exe')]), 
    (os.path.join('data', 'Ventilation', 'Geom'), [os.path.join('..', 'data', 'Ventilation', 'Geom', 'tree.ipelem'), os.path.join('..', 'data', 'Ventilation', 'Geom', 'tree.ipnode'), os.path.join('..', 'data', 'Ventilation', 'Geom', 'tree.ipfiel')]),
]
OPTIONS = {'py2exe': {
        'packages': find_packages(),
    }
}


setup(
    windows=['opencmiss/neon/neon.py'],
    options=OPTIONS,
    data_files=DATA_FILES,
)
