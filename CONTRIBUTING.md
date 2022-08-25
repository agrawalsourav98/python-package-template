# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

You can contribute by reporting bugs, fixing bugs, implementing features, writing documentation and submitting feedback.

## Dependencies

We use `pip` to manage the [dependencies](https://pip.pypa.io/en/stable/).

To prepare the development environment,

```bash
make dev-install
```

## Formatting

After installation you may execute code formatting.

```bash
make format
```

This would run black and isort.

### Checks

Many checks are configured for this project.
Command `make type-safety` will check static type checking.
Command `make pre-commit` will check commit readiness.
Command `make check-safety` command will look at the security of your code.

Comand `make lint` applies all checks.

### Before submitting

Before submitting your code please do the following steps:

1. Add any changes you want
2. Add tests for the new changes
3. Edit documentation if you have changed something significant
4. Run `make lint` to ensure that formatting, types, security and docstrings are okay.

## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.
