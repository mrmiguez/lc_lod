from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name="lc_lod",
    version="0.0.1",
    packages=find_packages(exclude=['tests*']),
    # install_requires=['lxml >= 2.3'],
    author="Matthew Miguez",
    author_email="r.m.miguez@gmail.com",
    description="",
    # long_description=long_description,
    url='https://github.com/mrmiguez/lc_lod',
    # keywords="MODS metadata xml",
    license='MIT',
    # classifiers=[
    #     'Development Status :: 4 - Beta',
    #     'Intended Audience :: Other Audience',
    #     'License :: OSI Approved :: MIT License',
    #     'Natural Language :: English',
    #     'Programming Language :: Python :: 3.2',
    #     'Programming Language :: Python :: 3.3',
    #     'Programming Language :: Python :: 3.4',
    #     'Programming Language :: Python :: 3.5',
    #     'Programming Language :: Python :: 3.6',
    #     'Topic :: Text Processing :: Markup :: XML'
    # ]
)
