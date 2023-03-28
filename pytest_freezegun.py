# -*- coding: utf-8 -*-

from distutils.version import LooseVersion

from freezegun import freeze_time
import pytest


MARKER_NAME = "freeze_time"
FIXTURE_NAME = "freezer"


@pytest.fixture(name=FIXTURE_NAME)
def freezer_fixture(request):
    """Freeze time and make it available to the test."""
    args = []
    kwargs = {}
    ignore = []

    # If we've got a marker, use the arguments provided there
    marker = request.node.get_closest_marker("freeze_time")
    if marker:
        ignore = marker.kwargs.pop("ignore", [])
        args = marker.args
        kwargs = marker.kwargs

    # Always want to ignore _pytest
    ignore.append("_pytest.terminal")
    ignore.append("_pytest.runner")

    # Freeze time around the test
    freezer = freeze_time(*args, ignore=ignore, **kwargs)
    frozen_time = freezer.start()
    # NOTE(ilya): Give us access to the underlying freezer object and the standard set of freezegun
    # API methods.
    frozen_time.obj = freezer
    yield frozen_time
    freezer.stop()


def pytest_collection_modifyitems(items):
    """Inject our fixture into any tests with our marker."""
    for item in items:
        if item.get_closest_marker("freeze_time"):
            item.fixturenames.insert(0, FIXTURE_NAME)


def pytest_configure(config):
    """Register our marker."""
    config.addinivalue_line(
        "markers", "{}(...): use freezegun to freeze time".format(MARKER_NAME)
    )
