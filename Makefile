SHELL := /bin/bash
CWD := $(PWD)
PROJECT := ipo_checker
TMP_PATH := $(CWD)/.tmp

.PHONY: test clean
.DEFAULT_GOAL := help

# Read about configuring Makefile:
## https://dev.to/yankee/streamline-projects-using-makefile-28fe

shell: # Setup and activate virtualenv
	@pipenv shell

install-dep: # install app dependencies for development
	@pipenv install --dev
	@echo -e "\nInstalling mypy types..."
	@pipenv run mypy $(PROJECT) --install-types

install: # install CLI
	@pipenv run pip install -e .

ipo: # Run ipo checker
	@pipenv run ipo

clean: # remove python temp files
	@rm -rf $(TMP_PATH) __pycache__ .pytest_cache .mypy_cache ipo.egg-info
	@echo 'Deleted ${TMP_PATH} and python cache'
	@find . -name '*.pyc' -delete
	@echo 'Deleted *.pyc recursively'
	@find . -name '__pycache__' -delete
	@echo 'Deleted __pycache__ recursively'

test: # run pytest in verbose mode
	@pipenv run pytest -vvv

format: # format all files using black
	@pipenv run black .

check: # diff changes to be made by black and mypy
	@echo -e "\nChecking format..."
	@pipenv run black --check --diff .
	@echo -e "\nChecking typing..."
	@pipenv run mypy ${PROJECT}

pre-commit: # install pre-commit hooks
	@echo -e "\nInstalling pre-commit hook..."
	@pipenv run pre-commit install

distributions: # create distribution wheel and zip for PyPI
	@pip install -r publish.txt
	@python3 setup.py sdist bdist_wheel
	@echo "Use `twine upload dist/*` to upload to PyPI"

help: # Show this help
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
