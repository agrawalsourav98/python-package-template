# Python Package Template

Template to create Python Packages.

- Github repo: <https://github.com/agrawalsourav98/python-package-template>
- Free Software: BSD License

## Development Features

- Supports `Python 3.9` and higher
- PIP as dependencies manager. See configuration in `setup.py`. Supports easy versioning similar to poetry.
- Automatic codestyle using `black` and `isort`
- Checks using `flake8`, which can be extended using extensions
- Ready to use `pre-commit` hooks with code-formatting.
- Type checking with `mypy`; security checks using `bandit` and `safety`.
- Testing setup with `pytest`
- Ready to use `.editorconfig` and `.gitignore`.

## Deployment Features

- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc with Makefile. More details in [makefile-usage](##Makefile-Usage).
- [Dockerfile](./Dockerfile) for your package

## Makefile Usage

[Makefile](./Makefile) contains a lot of functions for faster development.

1. Normal Install

    To install run,

    ```bash
    make install
    ```

    To uninstall,

    ```bash
    make uninstall
    ```

2. Developer Install

    To download and install Poetry run:

    ```bash
    make dev-install
    ```

    To uninstall

    ```bash
    make uninstall
    ```

3. Run formatting

    To run formatting (black and isort):

    ```bash
    make format
    ```

4. Running tests

    To run tests:

    ```bash
    make test
    ```

5. Linting

    Liniting runs tests, pre-commit hooks, type checking and safety checking.

    ```bash
    make lint
    ```

    To run individually,

    Safety Check, runs `bandit` and `safety`

    ```bash
    make check-safety
    ```

    Type checking, runs `mypy`

    ```bash
    make type-checking
    ```

    Pre-commit, runs formatters, flake8 and some pre commit hooks

    ```bash
    make pre-commit
    ```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

## TODOS

- Add docs support
- Add cookiecutter support
- Add CI/CD configs

## Acknowledgements

This template was inspired by,

- [python-package-template](https://github.com/TezRomacH/python-package-template)
