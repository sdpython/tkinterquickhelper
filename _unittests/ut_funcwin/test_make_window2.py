"""
@brief      test log(time=3s)
"""
import unittest
import warnings
from tkinter import TclError
from tkinterquickhelper.funcwin.default_functions import test_regular_expression, file_grep, file_head
from tkinterquickhelper.funcwin.main_window import main_loop_functions


class TestMakeWindow2 (unittest.TestCase):

    def test_file_binary(self):
        functions = {"test_regular_expression": test_regular_expression,
                     "test_edit_distance": file_grep,
                     "file_head": file_head}
        try:
            main_loop_functions(
                functions, title="title: TestMakeWindow2", mainloop=False)
        except TclError as e:
            warnings.warn("TclError" + str(e))
            return


if __name__ == "__main__":
    unittest.main()
