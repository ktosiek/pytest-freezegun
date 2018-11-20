================
pytest-freezegun
================

.. image:: https://travis-ci.org/ktosiek/pytest-freezegun.svg?branch=master
    :target: https://travis-ci.org/ktosiek/pytest-freezegun
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/ktosiek/pytest-freezegun?branch=master&svg=true
    :target: https://ci.appveyor.com/project/ktosiek/pytest-freezegun/branch/master
    :alt: See Build Status on AppVeyor

Wrap tests with fixtures in freeze_time


Features
--------

* Freeze time in both the test and fixtures
* Access the freezer when you need it


Installation
------------

You can install "pytest-freezegun" via `pip`_ from `PyPI`_::

    $ pip install pytest-freezegun


Usage
-----

All the features can be seen in this example:

.. code-block:: python

    @pytest.fixture
    def current_date():
        return datetime.now().date()

    @pytest.mark.freeze_time('2017-05-21')
    def test_current_date(current_date):
        assert current_date == date(2017, 5, 21)

    @pytest.mark.freeze_time
    def test_changing_date(current_date, freezer):
        freezer.move_to('2017-05-20')
        assert current_date == date(2017, 5, 20)
        freezer.move_to('2017-05-21')
        assert current_date == date(2017, 5, 21)

    def test_not_using_marker(freezer):
        now = datetime.now()
        time.sleep(1)
        later = datetime.now()
        assert now == later

Contributing
------------
Contributions are very welcome.
Tests can be run with `tox`_.
You can later check coverage with `coverage combine && coverage html`.
Please try to keep coverage at least the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-freezegun" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

Credits
-------

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/ktosiek/pytest-freezegun/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
