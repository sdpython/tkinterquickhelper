"""
@brief      test log(time=1s)
"""
import unittest
import datetime
from pyquickhelper.loghelper.flog import fLOG
from tkinterquickhelper.funcwin.function_helper import extract_function_information
from tkinterquickhelper.funcwin.default_functions import file_grep
from tkinterquickhelper import check
from tkinterquickhelper.funcwin.storing_functions import _private_store, _private_restore, interpret_parameter


class TestFonctionHelper (unittest.TestCase):

    def test_fonction_info(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        res = extract_function_information(file_grep)
        for k in sorted(res):
            fLOG(k, res[k])
        for k in sorted(res["param"]):
            fLOG("--", k, res["param"][k], "-", res["types"][k])
        typstr = str  # unicode#
        if res["types"]["file"] != typstr:
            raise AssertionError(
                "type should be str not {0}\nres={1}".format(res["types"]["file"], res))

    def test_check(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        check()

    def test_fail(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        # change that value to test the build stops going through a failure
        assert True

    def test__private_store(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        params = dict(a="a", b="a2", c=1.0)
        fname = "pyquickhelper_test_function"
        _private_store(fname, params)
        params2 = _private_restore(fname)[0]
        if params2 != params:
            raise AssertionError("diff\n{0}\n{1}".format(params, params2))

    def test_interpret_parameter(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        typstr = str  # unicode#
        if interpret_parameter(typstr, "er") != "er":
            raise AssertionError(interpret_parameter(typstr, "er"))
        assert interpret_parameter(int, "0") == 0
        assert interpret_parameter(float, "1.3") == 1.3
        assert interpret_parameter(bool, 1)
        assert interpret_parameter(bool, "True")
        assert not interpret_parameter(bool, "false")
        assert interpret_parameter(None, "None") is None
        assert interpret_parameter(int, "None") is None
        assert interpret_parameter(None, "none") is None
        assert interpret_parameter(None, None) is None
        assert interpret_parameter(datetime.datetime, "None") is None
        r = interpret_parameter(datetime.datetime, "2015-02-03")
        if r != datetime.datetime(2015, 2, 3):
            raise AssertionError(r)
        assert interpret_parameter(object, "['3']") == ['3']


if __name__ == "__main__":
    unittest.main()
