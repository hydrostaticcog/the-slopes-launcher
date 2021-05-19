import os
from setuptools import setup

setup(
    name = "The Slopes Launcher",
    version = "0.02",
    author = "hydrostaticcog",
    author_email = "hydrostaticcog@gmail.com",
    description = "Launches The Slopes (ski resort simulator)",
    license = "AGPL-3.0",
    url = "https://github.com/hydrostaticcog/the-slopes-launcher",
    packages=['slopeslauncher'],
    entry_points = {
        'console_scripts' : ['slopeslauncher = slopeslauncher.launcher:main']
    },
    data_files = [
        ('share/applications/', ['slopeslauncher.desktop'])
    ],
    classifiers=[
        "License :: AGPL-3.0 License",
    ],
)