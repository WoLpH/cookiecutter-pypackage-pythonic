import pytest
import logging
from {{ cookiecutter.pkg_name }} import {{ cookiecutter.pkg_name | capitalize }}


LOG_LEVELS = {
    '0': logging.ERROR,
    '1': logging.WARNING,
    '2': logging.INFO,
    '3': logging.DEBUG,
}


def pytest_configure(config):
    logging.basicConfig(
        level=LOG_LEVELS.get(config.option.verbose, logging.DEBUG))


@pytest.fixture
def {{ cookiecutter.pkg_name }}():
    return {{ cookiecutter.pkg_name | capitalize }}('arg')


@pytest.fixture
def {{ cookiecutter.pkg_name }}_with_arg():
    return {{ cookiecutter.pkg_name | capitalize }}('some_arg', 'some other arg')

