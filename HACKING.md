# Running tests

Just running `tox` should run all tests on the supported python/pytest configurations.

# Releasing

Building and uploading a release:

    rm dist/* && \
    .tox/flake8/bin/python setup.py sdist bdist_wheel && \
    twine upload dist/*
