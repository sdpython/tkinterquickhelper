"""
@brief      test log(time=3s)
"""
import os
import unittest
from pyquickhelper.loghelper.flog import fLOG
from tkinterquickhelper.funcwin.storing_functions import get_icon
from tkinterquickhelper.funcwin import open_window_function, open_window_params
from tkinterquickhelper.funcwin.default_functions import test_regular_expression


class TestMakeWindow (unittest.TestCase):

    def test_FrameFunction(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        ico = get_icon()
        fLOG("icon", ico)
        assert os.path.exists(ico)

        if __name__ == "__main__":
            open_window_function(test_regular_expression)

    def test_open_window_params(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if __name__ == "__main__":
            par = {"user": os.environ["USERNAME"],
                   "password": ""}
            res = open_window_params(par,
                                     help_string="unit test",
                                     title="try the password *",
                                     top_level_window=None,
                                     key_save="unique")
            fLOG(res)


if __name__ == "__main__":
    unittest.main()
