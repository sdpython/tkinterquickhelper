"""
@brief      test log(time=1s)
"""
import os
import sys
import unittest

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from src.tkinterquickhelper.funcwin import fix_python35_dll


class TestPatchsVenv(unittest.TestCase):

    def test_patch_installation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_patch_installation")
        copied = fix_python35_dll(sys.prefix, temp, force=True)
        for c in copied:
            fLOG("copied", os.path.split(c)[-1])


if __name__ == "__main__":
    unittest.main()
