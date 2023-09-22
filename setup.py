from setuptools import setup, find_packages

setup(
    name="vritools",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click",
        "re",
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "vritools=cli.main_cli:main",
        ],
    },
)
