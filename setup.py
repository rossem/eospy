from setuptools import setup, find_packages
import os

setup(name='eospy',
      #version=os.getenv('BUILD_VERSION', 'DEV'),
      version='1.0.1',
      description='Python library for the eosio REST API',
      author='deck',
      author_email='deck@eosnewyork.io',
      url='https://github.com/eosnewyork/eospy',
      packages=find_packages(),
      install_requires=[
          'requests'
      ],
      entry_points = {
          'console_scripts' :[
              'validate_chain = eospy.command_line:validate_chain',
              'pycleos = eospy.command_line:cleos'
          ],
      }
)
