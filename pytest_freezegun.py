# -*- coding: utf-8 -*-

import pytest
from freezegun import freeze_time


@pytest.yield_fixture
def freezer(request):
    marker = request.node.get_marker('freeze_time')
    args, kwargs = (marker.args, marker.kwargs) if marker else ((), {})
    with freeze_time(*marker.args, **marker.kwargs) as freezer:
        yield freezer


@pytest.fixture(autouse=True)
def _auto_freezer(request):
    if request.node.get_marker('freeze_time'):
        request.getfixturevalue('freezer')
