"""
@brief      test log(time=1s)
"""
import os
import sys
import unittest
import io
import warnings
from tkinterquickhelper.funcwin.default_functions import _clean_name_variable, _get_format_zero_nb_integer, file_list, file_split


class TestMissingFuncWin (unittest.TestCase):

    def test_missing_funcwin_file_list(self):
        assert _clean_name_variable("s-6") == "s_6"
        assert _get_format_zero_nb_integer(5006) == "%04d"
        ioout = io.StringIO()
        file_list(os.path.abspath(os.path.dirname(__file__)), out=ioout)
        s = ioout.getvalue()
        assert len(s) > 0

    def test_missing_funcwin_file_split(self):
        assert _clean_name_variable("s-6") == "s_6"
        assert _get_format_zero_nb_integer(5006) == "%04d"
        ioout = [io.StringIO(), io.StringIO()]
        if sys.version_info[0] == 2:
            warnings.warn("skip testing Python 2.7")
            return
        file_split(os.path.abspath(__file__), out=ioout, header=True)
        ioout = [io.StringIO(), io.StringIO()]
        s1 = ioout[0].getvalue()
        s2 = ioout[0].getvalue()
        self.assertEqual(s1[:5], s2[:5])
        nb = file_split(os.path.abspath(__file__), out=ioout, header=False)
        size = os.stat(os.path.abspath(__file__)).st_size
        sa = 0
        for li in ioout:
            s = li.getvalue()
            assert len(s) > 0
            sa += len(s)
        assert 0 < sa <= size
        if sa not in (size, size - nb - 1, size - nb, size - 1):
            raise AssertionError("{0} != {1}, nb={2}".format(sa, size, nb))


if __name__ == "__main__":
    unittest.main()
