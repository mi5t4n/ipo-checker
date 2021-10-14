from setuptools import setup

setup(
    name="ipo",
    packages=["ipo_checker"],
    entry_points = {
        "console_scripts": [
            "ipo = ipo_checker.main:cli",
        ]
    }
)
