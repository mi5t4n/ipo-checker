from setuptools import setup

__version__ = "0.1.0"

setup(
    name="ipo",
    version=__version__,
    author="Sagar Tamang, Sagar Chamling",
    author_email="mi5t4n@gmail.com, sgr.raee@gmail.com",
    packages=["ipo_checker"],
    entry_points={
        "console_scripts": [
            "ipo = ipo_checker.main:cli",
        ]
    },
)
