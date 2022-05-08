style:
	black . --line-length 79

lint:
	black ndnt tests setup.py --line-length 79 --check
	flake8 ndnt
	flake8 tests --ignore=D

test:
	pytest --cov=ndnt --cov-report=html tests

cov:
	pytest --cov=ndnt --cov-report=term-missing:skip-covered --cov-report=xml tests
