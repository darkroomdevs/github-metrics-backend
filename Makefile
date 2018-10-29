.PHONY:  run install test distclean venv/bin/activate flake migrate clean

.DEFAULT: help
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "venv					creates a virtual environment and install dependencies"
	@echo "test					runs tests"
	@echo "flake				runs flake8 linter"
	@echo "run					runs project on default port"
	@echo "distclean			cleans the project"
	@echo "clean 				delete cache folders"

venv: venv/bin/activate
venv/bin/activate: requirements-to-freeze.txt
	test -d venv || virtualenv venv
	venv/bin/pip install -Ur requirements-to-freeze.txt
	venv/bin/pip freeze | sort > requirements.txt
	touch venv/bin/activate

distclean: clean
	rm -fr *.egg *.egg-info/ dist/ build/

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr
	find . -name '*pytest_cache*' -type d | xargs rm -fr

flake:
	venv/bin/flake8 src tests

test:
	venv/bin/pytest --cov=src tests/

run:
	venv/bin/python manage.py runserver 0.0.0.0:8000

migrate:
	venv/bin/python manage.py migrate --fake
