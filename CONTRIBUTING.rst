Contributing
============

The project should be installed in a `virtualenv`_ in editable mode. The
dev requirements can be installed from ``requirements/dev.txt``. If you
already have `nox`_ and `pre-commit`_ installed globally, you can skip
the dev requirements.

.. code-block:: text

    $ pip install -e . -r requirements/dev.txt

Install `pre-commit`_ hooks to automatically format and lint code when
committing. Otherwise any issues will be caught in CI once your PR is
submitted.

.. code-block:: text

    $ pre-commit install
    $ git commit

Run `nox`_ to run tests for all Python versions, style checks, and docs
build. These all run during CI as well.

.. code-block:: text

    $ nox

Run `pytest`_ to run the tests for the current Python environment only.

.. code-block:: text

    $ pytest


.. _virtualenv: https://virtualenv.pypa.io/en/stable/
.. _nox: https://nox.thea.codes/en/stable/
.. _pre-commit: https://pre-commit.com/
.. _pytest: https://docs.pytest.org/en/latest/
