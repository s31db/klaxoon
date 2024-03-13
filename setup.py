from setuptools import setup, find_packages

setup(
    name="klaxoon",
    version="0.1",
    author="Samuel Bastiat",
    author_email="samuel.bastiat@gmail.com",
    description="Python klaxoon library",
    url="https://github.com/s31db/klaxoon",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "configure-klaxoon-token=klaxoon.gui.configure_token_gui:configure_api_token",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
