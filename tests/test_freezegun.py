# -*- coding: utf-8 -*-
from datetime import datetime


def test_freezing_time(testdir):
    testdir.makepyfile("""
        import pytest
        from datetime import date, datetime

        @pytest.mark.freeze_time('2017-05-20 15:42')
        def test_sth():
            assert datetime.now().date() == date(2017, 5, 20)
    """)

    result = testdir.runpytest('-v', '-s')
    assert result.ret == 0


def test_no_mark(testdir):
    testdir.makepyfile("""
        import datetime

        def test_sth():
            assert datetime.datetime.now() > {}
    """.format(repr(datetime.now())))

    result = testdir.runpytest('-v', '-s')
    assert result.ret == 0


def test_move_to(testdir):
    testdir.makepyfile("""
        from datetime import date
        import pytest

        @pytest.mark.freeze_time
        def test_changing_date(freezer):
            freezer.move_to('2017-05-20')
            assert date.today() == date(2017, 5, 20)
            freezer.move_to('2017-05-21')
            assert date.today() == date(2017, 5, 21)
    """)

    result = testdir.runpytest('-v', '-s')
    assert result.ret == 0
