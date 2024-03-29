PACKAGE := leetcode_runner
TEST_FOLDER := tests
PYPI_PACKAGE := leetcode-runner
MODULES := $(wildcard $(PACKAGE)/*.py)

# MAIN TASKS ##################################################################

.PHONY: all
all: install

.PHONY: ci
ci: format check test ## Run all tasks that determine CI status

.PHONY: watch
watch: install .clean-test ## Continuously run all CI tasks when files chanage
	poetry run sniffer

.PHONY: run
run: install ## Start the program
	poetry run python $(PACKAGE)/__main__.py

.PHONY: shell
shell: install ## Launch an IPython session
	poetry run ipython --ipython-dir=notebooks

# SYSTEM DEPENDENCIES #########################################################

.PHONY: doctor
doctor:  ## Confirm system dependencies are available
	bin/verchew

# PROJECT DEPENDENCIES ########################################################

VIRTUAL_ENV ?= .venv
DEPENDENCIES := $(VIRTUAL_ENV)/.poetry-$(shell bin/checksum pyproject.toml poetry.lock)

.PHONY: install
install: $(DEPENDENCIES) .cache

$(DEPENDENCIES): poetry.lock
	@ rm -rf $(VIRTUAL_ENV)/.poetry-*
	@ poetry config virtualenvs.in-project true
	poetry install
	@ touch $@

ifndef CI
poetry.lock: pyproject.toml
	poetry lock --no-update
	@ touch $@
endif

.cache:
	@ mkdir -p .cache

# CHECKS ######################################################################

.PHONY: format
format: install
	poetry run isort $(PACKAGE)
	poetry run black $(PACKAGE)
	@ echo

.PHONY: check
check: install format  ## Run formaters, linters, and static analysis
ifdef CI
	git diff --exit-code
endif
	poetry run mypy $(PACKAGE) --config-file=.mypy.ini
	poetry run pylint $(PACKAGE) --rcfile=.pylint.ini
	poetry run pydocstyle $(PACKAGE)

# TESTS #######################################################################

RANDOM_SEED ?= $(shell date +%s)
FAILURES := .cache/v/cache/lastfailed

PYTEST_OPTIONS := --random --random-seed=$(RANDOM_SEED)
ifndef DISABLE_COVERAGE
PYTEST_OPTIONS += --cov=$(PACKAGE)
endif
PYTEST_RERUN_OPTIONS := --last-failed --exitfirst

.PHONY: test
test: test-all ## Run unit and integration tests

.PHONY: test-unit
test-unit: install
	@ ( mv $(FAILURES) $(FAILURES).bak || true ) > /dev/null 2>&1
	poetry run pytest $(TEST_FOLDER) $(PYTEST_OPTIONS)
	@ ( mv $(FAILURES).bak $(FAILURES) || true ) > /dev/null 2>&1
ifndef DISABLE_COVERAGE
	poetry run coveragespace update unit
endif

.PHONY: test-all
test-all: install
	@ if test -e $(FAILURES); then poetry run pytest $(TEST_FOLDER) $(PYTEST_RERUN_OPTIONS); fi
	@ rm -rf $(FAILURES)
	poetry run pytest $(TEST_FOLDER) $(PYTEST_OPTIONS)
ifndef DISABLE_COVERAGE
	poetry run coveragespace update overall
endif

.PHONY: read-coverage
read-coverage:
	bin/open htmlcov/index.html

# BUILD #######################################################################

DIST_FILES := dist/*.tar.gz dist/*.whl
EXE_FILES := dist/$(PACKAGE).*

.PHONY: dist
dist: install $(DIST_FILES)
$(DIST_FILES): $(MODULES) pyproject.toml
	rm -f $(DIST_FILES)
	poetry build

.PHONY: exe
exe: install $(EXE_FILES)
$(EXE_FILES): $(MODULES) $(PACKAGE).spec
	# For framework/shared support: https://github.com/yyuu/pyenv/wiki
	poetry run pyinstaller $(PACKAGE).spec --noconfirm --clean

$(PACKAGE).spec:
	poetry run pyi-makespec $(PACKAGE)/__main__.py --onefile --windowed --name=$(PACKAGE)

# RELEASE #####################################################################

.PHONY: upload
upload: dist ## Upload the current version to PyPI
	#git diff --name-only --exit-code
	poetry publish
	bin/open https://pypi.org/project/$(PYPI_PACKAGE)

# CLEANUP #####################################################################

.PHONY: clean
clean: .clean-build .clean-docs .clean-test .clean-install ## Delete all generated and temporary files

.PHONY: clean-all
clean-all: clean
	rm -rf $(VIRTUAL_ENV)

.PHONY: .clean-install
.clean-install:
	find $(PACKAGE) tests -name '__pycache__' -delete
	rm -rf *.egg-info

.PHONY: .clean-test
.clean-test:
	rm -rf .cache .pytest .coverage htmlcov

.PHONY: .clean-docs
.clean-docs:
	rm -rf docs/*.png site

.PHONY: .clean-build
.clean-build:
	rm -rf *.spec dist build

# HELP ########################################################################

.PHONY: help
help: all
	@ grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
