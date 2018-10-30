# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='nzigen_codes',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/nzigen/nzigen-codes',
      author='ysawa',
      author_email='ysawa@nzigen.com',
      license='MIT',
      packages=find_packages(),
      test_suite='test',
      install_requires=[
          'pycrypto',
      ],
      zip_safe=False)