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
    package=find_packages("src"),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'loremipsum',
    ]
)
