# -*- coding: utf-8 -*-

import pytest
from freezegun import freeze_time


def pytest_runtest_setup(item):
    marker = item.get_marker("freeze_time")
    if marker is not None:
        freezer = freeze_time(*marker.args, **marker.kwargs)
        freezer.start()
        item.addfinalizer(freezer.stop)
