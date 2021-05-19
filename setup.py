import os
from setuptools import setup

setup(
    name = "The Slopes Launcher",
    version = "0.02",
    author = "hydrostaticcog",
    author_email = "hydrostaticcog@gmail.com",
    description = "Launches The Slopes (ski resort simulator)",
    license = "AGPL-3.0",
    url = "none yet",
    packages=['skisimlauncher'],
    entry_points = {
        'console_scripts' : ['skisimlauncher = skisimlauncher.launcher:main']
    },
    data_files = [
        ('share/applications/', ['skisimlauncher.desktop'])
    ],
    classifiers=[
        "License :: AGPL-3.0 License",
    ],
)