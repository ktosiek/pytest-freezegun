# -*- coding: utf-8 -*-

import pytest

from freezegun import freeze_time


class FreezegunPlugin(object):
    def __init__(self):
        self.freezer = None
        self.frozen_time = None

    @pytest.fixture(name='freezer')
    def freezer_fixture(self):
        if self.frozen_time is not None:
            yield self.frozen_time
        else:
            with freeze_time() as frozen_time:
                yield frozen_time

    @pytest.hookimpl(tryfirst=True)
    def pytest_runtest_setup(self, item):
        try:
            marker = item.get_closest_marker('freeze_time')
        except AttributeError:  # for pytest < 3.6.0
            marker = item.get_marker('freeze_time')

        if marker:
            ignore = marker.kwargs.pop('ignore', [])
            ignore.append('_pytest')

            self.freezer = freeze_time(
                *marker.args,
                ignore=ignore,
                **marker.kwargs
            )
            self.frozen_time = self.freezer.start()

    @pytest.hookimpl(trylast=True)
    def pytest_runtest_teardown(self):
        if self.freezer is not None:
            self.freezer.stop()
            self.freezer = None
            self.frozen_time = None


plugin = FreezegunPlugin()
