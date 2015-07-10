import pytest

from {{ cookiecutter.pkg_name }} import {{ cookiecutter.pkg_name | capitalize }}


@pytest.fixture
def {{ cookiecutter.pkg_name }}():
    return {{ cookiecutter.pkg_name | capitalize }}('arg')


@pytest.fixture
def {{ cookiecutter.pkg_name }}_with_arg():
    return {{ cookiecutter.pkg_name | capitalize }}('some_arg', 'some other arg')

