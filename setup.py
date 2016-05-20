# Copyright (c) 2015 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the MIT License
# accompanying the software ("License").  This software is distributed "AS IS"
# as set forth in the License.

"""
steelscript.o365
====================
Office 365 Usage App Framework Plugin

"""
from setuptools import setup, find_packages
from gitpy_versioning import get_version

install_requires = (
    'steelscript.appfwk',

    # Add any special python package requirements below this line
)

setup_args = {
    'name':                'steelscript.o365',
    'namespace_packages':  ['steelscript'],
    'version':             get_version(),

    # Update the following as needed
    'author':              'Gwen Blum',
    'author_email':        'gwen.blum@gmail.com',
    'url':                 '',
    'license':             'MIT',
    'description':         'Office 365 Usage App Framework Plugin',
    'long_description':    __doc__,

    'packages': find_packages(exclude=('gitpy_versioning',)),
    'zip_safe': False,
    'install_requires': install_requires,
    'extras_require': None,
    'test_suite': '',
    'include_package_data': True,
    'entry_points': {
        # Uncomment these lines to enable steel commands for this module
        # 'steel.commands': [
        #     'o365 = steelscript.o365.commands'
        # ],
        'portal.plugins': [
            'o365 = steelscript.o365.appfwk.plugin:Plugin'
        ],
    },

    'classifiers': (
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ),
}

setup(**setup_args)
