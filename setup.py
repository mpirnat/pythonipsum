import os

from setuptools import setup, find_packages

version = "0.1"

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'loremipsum',
]


setup(
    name="pythonipsum",
    version=version,
    description="A lorem ipsum generator for the Python world.",
    author="Mike Pirnat",
    author_email="",
    packages=['pythonipsum'],
    package_dir={'pythonipsum': 'pythonipsum'},
    package_data={'pythonipsum': ['pythonipsum/data/*.txt']},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'loremipsum',
    ]
)
