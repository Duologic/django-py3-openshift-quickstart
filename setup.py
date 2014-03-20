from setuptools import setup

import os

# Put here required packages or
# Uncomment one or more lines below in the install_requires section
# for the specific client drivers/modules your application needs.
packages = ['Django<=1.6',
                   # 'CherryPy', # If you want serve Django through CherryPy
                  'static3',  # If you want serve the static files in the same server
                   #  'mysql-connector-python',
                   #  'pymongo',
                   'psycopg2',
                   'south',
      ]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='django16-testing', version='1.0',
      description='Trying out OpenShift Python-3.3 / Django-1.6',
      author='Jeroen Op \'t Eynde', author_email='jeroen@simplistic.be',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
     )
