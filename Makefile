# See https://makefiletutorial.com/ for help in writing makefiles

#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`
# Change this to customized name
PACKAGE_PATHS := sample
DOCKER_TAG := sample-docker

#* Installation
.PHONY: install
install:
	@echo "Performing package installation"
	@$(PYTHON) -m pip install .

#* Removal
.PHONY: uninstall
uninstall:
	@echo "Removing the package"
	@$(PYTHON) -m pip uninstall .

#* Developement setup
.PHONY: dev-install
dev-install:
	@echo "Performing dev installation"
	@echo "Installing dev dependencies"
	@$(PYTHON) -m pip install .[dev]
	@echo "Installing devlopment version of package"
	@$(PYTHON) -m pip install -e .

#* Run pre-commit includes formatters and other checkers
.PHONY: pre-commit
pre-commit:
	@echo "Running pre-commit"
	@$(PYTHON) -m pre_commit run

.PHONY: format
format:
	@echo "Running isort"
	@$(PYTHON) -m isort -settings-file pyproject.toml .
	@echo "Running black"
	@$(PYTHON) -m black --config pyproject.toml .

#* Test
.PHONY: test
test:
	@echo "Running pytest"
	- @PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m pytest -c pyproject.toml

#* Static Type Checking
.PHONY: type-checking
type-checking:
	@echo "Running mypy"
	@$(PYTHON) -m mypy --config-file pyproject.toml $(PACKAGE_PATHS)

#* Check Common Security Issues
.PHONY: check-safety
check-safety:
	@echo "Running safety"
	$(PYTHON) -m safety check
	@echo "Running bandit"
	$(PYTHON) -m bandit -ll --recursive $(PACKAGE_PATHS)

#* Single command to run checks and format code
.PHONY: lint
lint: test pre-commit type-checking check-safety

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	@echo "Removing pycache"
	@find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: dsstore-remove
dsstore-remove:
	@echo "Removing .DS_Store files"
	@find . | grep -E ".DS_Store" | xargs rm -rf

.PHONY: mypycache-remove
mypycache-remove:
	@echo "Removing mypy cache"
	@find . | grep -E ".mypy_cache" | xargs rm -rf

.PHONY: ipynbcheckpoints-remove
ipynbcheckpoints-remove:
	@echo "Removing ipynbcheckpoints"
	@find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

.PHONY: pytestcache-remove
pytestcache-remove:
	@echo "Removing pytest cache"
	@find . | grep -E ".pytest_cache" | xargs rm -rf

.PHONY: build-remove
build-remove:
	@echo "Removing build"
	@rm -rf build/

.PHONY: clean
clean: pycache-remove dsstore-remove mypycache-remove ipynbcheckpoints-remove pytestcache-remove

.PHONY: docker
docker:
	@echo "Building docker container"
	@docker build --tag $(DOCKER_TAG) .
