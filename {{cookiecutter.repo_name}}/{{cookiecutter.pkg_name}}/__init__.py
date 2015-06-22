# -*- coding: utf-8 -*-
'''

{{ cookiecutter.project_name }}
{{ '-' * cookiecutter.project_name|count }}

{{ cookiecutter.project_short_description|wordwrap }}

'''

from __future__ import absolute_import, division, print_function, \
    with_statement, unicode_literals

from .{{ cookiecutter.pkg_name }} import {{ cookiecutter.pkg_name | capitalize }}

__all__ = [
    '{{ cookiecutter.pkg_name | capitalize }}',
]

