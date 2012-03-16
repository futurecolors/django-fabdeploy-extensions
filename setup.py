#!/usr/bin/env python
#coding: utf-8
from distutils.core import setup

import sys
reload(sys).setdefaultencoding("UTF-8")

version = '0.2.0'

setup(
    name ='django-fabdeploy-extensions',
    version = version,
    author = 'Future Colors',
    author_email = 'info@futurecolors.ru',
    packages = ['fabdeploy_extensions', 'fabdeploy_extensions.extensions'],
    url = 'https://github.com/futurecolors/django-fabdeploy-extensions',
    download_url = 'https://github.com/futurecolors/django-fabdeploy-extensions/zipball/master',
    license = 'MIT license',
    description = u'Fabdeploy extension to use UWSGI'.encode('utf8'),
    long_description = open('README').read().decode('utf8'),
    requires = ['fab_deploy (>=0.7.1)', 'Fabric (>=1.0.0)', 'jinja2'],

    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
