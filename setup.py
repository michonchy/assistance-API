#!usr/bin/env python

from setuptools import setup, find_packages

setup(name='assistanse-API',
      version='0.1',
      description='説明',
      url='https://github.com/michonchy/assistance-API',
      packages=find_packages(),
      package_dir={'AssistanceAPI': 'AssistanceAPI'},
      py_modules=['AssistanceAPI'],
      )