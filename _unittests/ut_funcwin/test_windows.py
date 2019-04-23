"""
@brief      test log(time=1s)
"""
import unittest
import warnings
from tkinter import TclError
from pyquickhelper.loghelper.flog import fLOG
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv
from tkinterquickhelper.funcwin import open_window_params, open_window_function
from tkinterquickhelper.funcwin.function_helper import get_function_list, private_get_function
import tkinterquickhelper


def my_tst_function(a, b):
    """
    Returns *a+b*.
    @param      a   (float) float
    @param      b   (float) float
    @return         a+b
    """
    return (a or 1) + (b or 1)


class TestWindows (unittest.TestCase):

    def test_open_window_params(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fix_tkinter_issues_virtualenv(fLOG=fLOG)
        params = dict(p1="p1", p2=3)
        try:
            win = open_window_params(params, do_not_open=True)
        except TclError as e:
            warnings.warn("TclError" + str(e))
            return
        fLOG(type(win))
        assert isinstance(
            win,
            tkinterquickhelper.funcwin.frame_params.FrameParams)

    def test_open_window_function(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fix_tkinter_issues_virtualenv(fLOG=fLOG)
        func = my_tst_function
        try:
            win = open_window_function(func, do_not_open=True)
        except TclError as e:
            warnings.warn("TclError" + str(e))
            return
        fLOG(type(win))
        assert isinstance(
            win,
            tkinterquickhelper.funcwin.frame_function.FrameFunction)
        win.refresh()
        win.update()
        win.run_function(0, 1)

    def test_get_function_list(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fix_tkinter_issues_virtualenv(fLOG=fLOG)
        funcs = get_function_list(tkinterquickhelper)
        assert isinstance(funcs, dict)
        assert len(funcs) > 0
        f = private_get_function("os.listdir")
        fLOG("**", f)


if __name__ == "__main__":
    unittest.main()
