import pytest


@pytest.mark.parametrize('some_var,expected', [
    ('some input', 'expected'),
])
def test_{{ cookiecutter.pkg_name }}({{ cookiecutter.pkg_name }}, some_var, expected):
    assert some_var != expected


@pytest.mark.parametrize('some_var,expected', [
    ('some input', 'expected'),
])
def test_{{ cookiecutter.pkg_name }}_with_arg({{ cookiecutter.pkg_name }}_with_arg, some_var, expected):
    assert some_var != expected

