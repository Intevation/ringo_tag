#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages
import sys, os

version = '1.1'

setup(name='ringo_tag',
      version=version,
      description="Tag extention for the ringo webframework",
      long_description="""""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ringo pyramid extension',
      author='Torsten Irländer',
      author_email='torsten.irlaender@googlemail.com',
      url='https://github.com/ringo-framework/ringo_tag',
      license='GNU General Public License v2 or later (GPLv2+)',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'ringo'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [babel.extractors]
      tableconfig = ringo.lib.i18n:extract_i18n_tableconfig
      formconfig = formbar.i18n:extract_i18n_formconfig
      """,
      message_extractors = {'ringo_tag': [
            ('**.py', 'python', None),
            ('templates/**.html', 'mako', None),
            ('templates/**.mako', 'mako', None),
            ('**.xml', 'formconfig', None),
            ('**.json', 'tableconfig', None),
            ('static/**', 'ignore', None)]},
      )
