# -*- coding: utf-8 -*-
"""
@file
@brief  Handles window `Tk <https://docs.python.org/3.4/library/tkinter.html#tkinter.Tk>`_
"""
import sys
import tkinter
import tkinter.tix as ttix  # pylint: disable=W0402


def X_is_running():
    """
    Checks that *X* is running.
    """
    from subprocess import Popen, PIPE
    try:
        p = Popen(["xset", "-q"], stdout=PIPE, stderr=PIPE)
        p.communicate()
        return p.returncode == 0
    except Exception:
        # this function can fail on eBook
        # moved as a warning
        # also remove the warning at is not always meaningful
        # import warnings
        # warnings.warn(
        #    "Unable to detected if X11 is running with command xset -q, we assume it is not.\n{0}".format(e))
        return False


def has_x_server():
    """
    Detects the presences of X server.
    """
    if sys.platform.startswith("win"):
        return True
    return X_is_running()


_has_x_server = has_x_server()


def create_tk():
    """
    Calls `Tk <https://docs.python.org/3/library/tkinter.html#tkinter.Tk>`_
    or `Tcl <https://docs.python.org/3/library/tkinter.html#tkinter.Tcl>`_
    depending on that fact there is a X server.

    @return         main window
    """
    global _has_x_server  # pylint: disable=W0602
    return tkinter.Tk() if _has_x_server else tkinter.Tcl()


def create_tixtk():
    """
    Calls `Tk <https://docs.python.org/3.4/library/tkinter.html#tkinter.Tk>`_
    or `Tcl <https://docs.python.org/3.4/library/tkinter.html#tkinter.Tcl>`_
    depending on that fact there is a X server.

    @return         main window
    """
    global _has_x_server  # pylint: disable=W0602
    return ttix.Tk() if _has_x_server else ttix.Tcl()
