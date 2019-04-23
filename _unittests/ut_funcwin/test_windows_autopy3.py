"""
@brief      test log(time=2s)
"""
import os
import sys
import unittest
import warnings
import threading
import time
from tkinter import TclError
from pyquickhelper.loghelper.flog import fLOG
from pyquickhelper.pycode import get_temp_folder
from tkinterquickhelper.funcwin import main_loop_functions


def my_tst_function2(a, b):
    """
    Returns *a+b*.
    @param      a   (float) float
    @param      b   (float) float
    @return         a+b
    """
    return a + b


class TestWindowsAutopy3(unittest.TestCase):

    def test_open_window_params(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        try:
            import autopy3
            import autopy3.key
            import autopy3.mouse
            import autopy3.screen
            autop = __name__ == "__main__"
        except ImportError:
            warnings.warn("autopy3 is not installed")
            autop = False

        temp = get_temp_folder(__file__, "temp_autopy3")
        root = [None]

        def f():
            if autop:
                fLOG("size", autopy3.screen.get_size())
                icon = autopy3.bitmap.Bitmap.open(
                    os.path.join(temp, "..", "data", "icon.png"))
                img = os.path.join(temp, "screen.png")
                screen = autopy3.bitmap.capture_screen()
                pos = screen.find_bitmap(icon)
                iter = 0
                while not pos and iter < 3:
                    if iter > 1:
                        fLOG("iter", iter, pos)
                    time.sleep(1)
                    screen = autopy3.bitmap.capture_screen()
                    pos = screen.find_bitmap(icon)
                    iter += 1
                if not pos:
                    warnings.warn("unable to find icon in the screen")
                    pos = (117, 108)
                screen.save(img)
                fLOG("pos=", pos)

                # test
                fLOG((1, 1), autopy3.screen.point_visible(
                    1, 1), autopy3.screen.get_size())
                if not autopy3.screen.point_visible(1, 1):
                    warnings.warn("autopy3.screen.point_visible is False")

                # closes the window
                if False and autopy3.screen.point_visible(1, 1):
                    # does not seem to work (point not visible)
                    dend = (986 - 117, 116 - 108)
                    end = (dend[0] + pos[0], dend[1] + pos[1])
                    autopy3.mouse.move(end[0], end[1])
                    autopy3.mouse.click(button=autopy3.mouse.LEFT_BUTTON)

            time.sleep(2)

            it = 0
            while root[0] is not None:
                fLOG("stop", it)
                # the window does not die if it does have the docus
                root[0].event_generate("<Alt-F4>")
                time.sleep(1)
                it += 1
                if it > 3:
                    root[0].destroy()
                    break

        th = threading.Thread(target=f)
        th.start()

        try:
            r = main_loop_functions(
                dict(my_tst_function2=my_tst_function2), init_pos=(100, 100), mainloop=False)
            if __name__ != "__main__":
                # does not work very well
                return
            root[0] = r
            r.mainloop()
            root[0] = None
            try:
                r.destroy()
                del r
            except Exception as e:
                fLOG(e)
        except TclError as e:
            warnings.warn("TclError" + str(e))


if __name__ == "__main__":
    unittest.main()
