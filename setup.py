#!/usr/bin/env python3

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import find_packages

d = generate_distutils_setup(
#     packages = ['blender_api_msgs'],
#     packages = ['roscom'],
    packages = find_packages('src'),
    package_dir={'': 'src'}
)

setup(**d)

# from setuptools import setup, find_packages
# setup(
#     name = "roscom-blender-api",
#     version = "0.1",
#     package_dir = {'': 'src',},
#     packages = find_packages('src'),
#     entry_points={
#         'blender_api.command_source.build': 'ros = roscom:build'
#     }
# )
