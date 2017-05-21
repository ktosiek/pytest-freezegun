# -*- coding: utf-8 -*-

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
