help:
	@cat makefile

clean:
	@rm -fr *.egg-info dist .coverage venv xclean.sqlite
	@find . -depth -type d -name .pytest_cache -exec rm -fr {} \;
	@find . -depth -type d -name __pycache__ -exec rm -fr {} \;

venv:
	@python3.10 -m venv venv
	@venv/bin/python -m pip install --upgrade pip setuptools wheel build pytest coverage pytest-cov twine

test: venv
	@venv/bin/pytest --cov --cov-branch --cov-report term-missing

install: venv
	@venv/bin/pip install -e .

build: venv
	@rm -fr dist *.egg-info
	@venv/bin/python -m build

upload-test: build
	@venv/bin/python -m twine upload --repository testpypi dist/*

upload-prod: build
	@venv/bin/python -m twine upload dist/*
