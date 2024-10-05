from setuptools import setup, find_packages

setup(
    name='PackageName',
    version='0.0.1',
    description='Setting up a python package',
    author='Author',
    author_email='author@email.com',
    packages=find_packages(include=['package', 'package.*']),
    
)
