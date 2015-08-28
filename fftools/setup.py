import sys
from glob import glob

if sys.version_info < (2, 6):
    sys.stderr.write('You must have at least Python 2.6 for fftools\n')
    sys.exit(0)

import os
from distutils.core import setup, Command
from distutils import ccompiler

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

rootname = os.getcwd()
fftools_home = rootname + "/fftools/"

setup_args = {}
packages = [
        'fftools',
        ]

if __name__ == "__main__":
    setup(name="fftools",
        version="0.0.1.dev0",
        author="Hai Nguyen",
        author_email="hainm.comp@gmail.com",
        packages=packages,
        description="""fftools""",
        license = "BSD License",
        classifiers=[
                    'Development Status :: 4 - Beta',
                    'Operating System :: Unix',
                    'Operating System :: MacOS',
                    'Intended Audience :: Science/Research',
                    'License :: OSI Approved :: BSD License',
                    'Programming Language :: Python :: 2.6'
                    'Programming Language :: Python :: 2.7',
                    'Programming Language :: Python :: 3.3',
                    'Programming Language :: Python :: 3.4',
                    'Programming Language :: Cython',
                    'Programming Language :: C',
                    'Programming Language :: C++',
                    'Topic :: Scientific/Engineering'],
    )
