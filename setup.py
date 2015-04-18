#!/usr/bin/env python

import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='runoerp',
      version='1.0',
      description='Developer Utility tool to run openerp server, upgrade all...',
      author='Dhinesh',
      author_email='dvdhinesh.mail@gmail.com',
      url='https://github.com/dvdhinesh/runoerp',
      long_description=read('README.md'),
      license=read('LICENSE'),
      scripts=['runoerp'],
      data_files=[ ('/usr/share/applications', ["runoerp.desktop"]),
		   ('/usr/share/runoerp', ["runoerp.ico"]),
		   ('/usr/share/runoerp', ["runoerplogo"])
                 ]
     )
