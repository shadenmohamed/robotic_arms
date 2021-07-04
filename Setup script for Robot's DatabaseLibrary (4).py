Setup script for Robot's DatabaseLibrary distributions"""

from distutils.core import setup

import setuptools
import sys
import os

src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_path)

__version_file_path__ = os.path.join(src_path, 'DatabaseLibrary', 'VERSION')
__version__ = open(__version_file_path__, 'r').read().strip()

def main():
    setup(name         = 'robotframework-databaselibrary',
          version      = __version__,
          description  = 'Database utility library for Robot Framework',
          author       = 'Franz Allan Valencia See',
          author_email = 'franz.see@gmail.com',
          url          = 'https://github.com/franz-see/Robotframework-Database-Library',
          package_dir  = { '' : 'src'},
          packages     = ['DatabaseLibrary'],
          package_data = {'DatabaseLibrary': ['VERSION']},
          requires     = ['robotframework']
          )


if __name__ == "__main__":
    main()
from os.path import abspath, dirname, join

try:
    from setuptools import setup
except ImportError as error:
    from distutils.core import setup


version_file = join(dirname(abspath(__file__)), 'src', 'DatabaseLibrary', 'version.py')

with open(version_file) as file:
    code = compile(file.read(), version_file, 'exec')
    exec(code)

setup(name         = 'robotframework-databaselibrary',
      version      = VERSION,
      description  = 'Database utility library for Robot Framework',
      author       = 'Franz Allan Valencia See',
      author_email = 'franz.see@gmail.com',
      url          = 'https://github.com/franz-see/Robotframework-Database-Library',
      package_dir  = { '' : 'src'},
      packages     = ['DatabaseLibrary'],
      package_data = {'DatabaseLibrary': []},
      requires     = ['robotframework']