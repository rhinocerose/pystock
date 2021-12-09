SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

install:  # Install the app locally
> poetry install
.PHONY: install

test:  ## Run tests
> poetry run pytest .
.PHONY: test

lint:  ## Run linting
> poetry run black --check .
> poetry run isort -c .
> poetry run flake8 .
> poetry run pydocstyle .
.PHONY: lint

lint-fix:  ## Run autoformatters
> poetry run black .
> poetry run isort .
.PHONY: lint-fix

typecheck:  ## Run typechecking
> poetry run mypy --show-error-codes --pretty .
.PHONY: typecheck
