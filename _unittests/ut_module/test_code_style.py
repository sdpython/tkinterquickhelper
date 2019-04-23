"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8


class TestCodeStyle(unittest.TestCase):

    def test_code_style_src(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            warnings.warn(
                "skipping test_code_style because of Python 2 or " + sys.executable)
            return

        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        check_pep8(src_, fLOG=fLOG,
                   pylint_ignore=('C0103', 'C1801',
                                  'E0203',
                                  'R0201', 'R0901', 'R0902', 'R0911', 'R0912',
                                  'R0913', 'R0914', 'R0915', 'R1702', 'R1705',
                                  'W0613',
                                  'W0123', 'W0212', 'W0703', 'W0201'),
                   skip=["_nbconvert_config.py:",
                         #
                         "Redefining name 'fLOG'",
                         "tk_window.py:56",
                         "tk_window.py:68",
                         "function_helper.py:122",
                         "Unable to import 'Tkinter'",
                         "tk_window.py:50: W0603",
                         "tk_window.py:62: W0603",
                         "R1720",
                         ])

    def test_code_style_test(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            warnings.warn(
                "skipping test_code_style because of Python 2 or " + sys.executable)
            return

        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=fLOG, neg_pattern="temp_.*",
                   max_line_length=200,
                   pylint_ignore=('C0111', 'C0103', 'R0914', 'W0212', 'C0413', 'W0621',
                                  'W0703', 'W0622', 'W0122', 'R0912', 'R0201',
                                  'R0915', 'C1801'),
                   skip=["[E402] module ",
                         "test_windows_autopy3.py:",
                         "R1720",
                         ])


if __name__ == "__main__":
    unittest.main()
