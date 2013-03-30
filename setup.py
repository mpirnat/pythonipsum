import os
import sys
import pythonipsum

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


requires = ['loremipsum']

testing_requires = ['konira']

setup(
    name='pythonipsum',
    version=pythonipsum.__version__,
    description='A lorem ipsum generator for the Python world.',
    long_description=open('README.md').read() + '\n\n' +
                     open('HISTORY.md').read(),
    author='Mike Pirnat',
    author_email='mpirnat@gmail.com',
    url='https://github.com/mpirnat/pythonipsum/',
    packages=['pythonipsum'],
    package_dir={'pythonipsum': 'pythonipsum'},
    package_data={'pythonipsum': ['pythonipsum/data/*.txt']},
    include_package_data=True,
    install_requires=requires + testing_requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
