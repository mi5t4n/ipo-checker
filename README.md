# IPO Checker

Checks more than one account for an IPO.

    Usage: ipo_checker.py [-h] --file FILE

    IPO Checker for a list.

    optional arguments:
    -h, --help         show this help message and exit
    --file FILE        Name of the pattern file.

# Requirements

1. Python 3.6+

# Installation

1. Install [pipenv](https://pipenv.pypa.io/en/latest/).
2. Initialize virtualize environment in the project folder using `pipenv shell`.
3. Install python libraries and CLI `pipenv install -e .` or `pipenv run pip install -e .`

# Configuration

1. Copy `list.txt.example` as `list.txt`
2. Add BOID and username in the file.

# How to use the tool?

    pipenv run ipo [ --file=list.txt ]

    [John Doe] :: Congratulation Alloted !!! Alloted quantity : 10
    [Joshue Doe] :: Sorry, not alloted for the entered BOID.

# Development Guide

1. Install packages in development mode: `pipenv install --dev`
2. Install Pre-commit Hook: `pipenv run pre-commit install`
3. mypy Typing install: `pipenv run mypy ipo_checker --install-types`

# Other Commands

1. Run Pre-commit Hook: `pipenv run pre-commit run --all-files -v`
2. Check MyPy Typing: `pipenv run mypy ipo_checker`
3. Format Black: `pipenv run black .`
