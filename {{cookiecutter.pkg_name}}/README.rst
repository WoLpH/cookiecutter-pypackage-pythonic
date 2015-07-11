{{ '=' * cookiecutter.project_name|count }}
{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|count }}


.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?branch=master
    :alt: {{ cookiecutter.project_name }} test status
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://badge.fury.io/py/{{ cookiecutter.repo_name }}.svg
    :alt: {{ cookiecutter.project_name }} Pypi version
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}

.. image:: https://coveralls.io/repos/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badge.svg?branch=master
    :alt: {{ cookiecutter.project_name }} code coverage
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo_name }}.svg
    :alt: Supported Python versions
    :target: https://crate.io/packages/{{ cookiecutter.repo_name }}?version=latest

``{{ cookiecutter.repo_name }}`` - {{ cookiecutter.project_short_description}}

Links
-----

* Documentation
    - http://{{ cookiecutter.repo_name }}.readthedocs.org/en/latest/
* Source
    - https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
* Bug reports 
    - https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues
* Package homepage
    - https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
* My blog
    - http://wol.ph/

Install
-------

To install the latest release:

.. code-block:: bash

    pip install {{ cookiecutter.repo_name }}

Or if `pip` is not available:
    
.. code-block:: bash

    easy_install {{ cookiecutter.repo_name }}
   
To install the latest development release:

.. code-block:: bash

    git clone --branch develop https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git {{ cookiecutter.repo_name }}
    cd ./{{ cookiecutter.repo_name }}
    virtualenv .env
    source .env/bin/activate
    pip install -e .

To run the tests you can use the `py.test` command or just run `tox` to test
everything in all supported python versions.

Usage
-----

* TODO

Contributing
------------

Help is greatly appreciated, just please remember to clone the **development**
branch and to run `tox` before creating pull requests.

Travis tests for `flake8` support and test coverage so it's always good to
check those before creating a pull request.

Development branch: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/tree/development

Info
----

==============  ==========================================================
Python support  Python 2.7, >= 3.3
Blog            http://wol.ph/
Source          https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
Documentation   http://{{ cookiecutter.repo_name }}.rtfd.org
Changelog       http://{{ cookiecutter.repo_name }}.readthedocs.org/en/latest/history.html
API             http://{{ cookiecutter.repo_name }}.readthedocs.org/en/latest/modules.html
Issues/roadmap  https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues
Travis          http://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
Test coverage   https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
Pypi            https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
Ohloh           https://www.ohloh.net/p/{{ cookiecutter.repo_name }}
License         `BSD`_.
git repo        .. code-block:: bash

                    $ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git
install dev     .. code-block:: bash

                    $ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git {{ cookiecutter.repo_name }}
                    $ cd ./{{ cookiecutter.repo_name }}
                    $ virtualenv .env
                    $ source .env/bin/activate
                    $ pip install -e .
tests           .. code-block:: bash

                    $ py.test
==============  ==========================================================

.. _BSD: http://opensource.org/licenses/BSD-3-Clause
.. _Documentation: http://{{ cookiecutter.repo_name }}.readthedocs.org/en/latest/
.. _API: http://{{ cookiecutter.repo_name }}.readthedocs.org/en/latest/modules.html
