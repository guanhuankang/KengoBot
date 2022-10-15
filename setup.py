from setuptools import setup

setup(
    name = "kengobot",
    version = "1.0",
    packages=["kengobot"],
    requires=["xmltodict", "pillow", "requests"]
)