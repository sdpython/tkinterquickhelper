# -*- coding: utf-8 -*-
"""
@file
@brief  various basic functions often needed
"""

import os
import re
import random
from pyquickhelper.loghelper.flog import fLOG, GetSepLine
from pyquickhelper.filehelper.synchelper import explore_folder_iterfile


_keep_var_character = re.compile("[^a-zA-Z0-9_]")


def _clean_name_variable(st):
    """
    Cleans a string.

    @param      st      string to clean
    @return             another string
    """
    res = _keep_var_character.split(st)
    if res is None:
        raise ValueError("unable to clean " + st)
    return "_".join(res)


def _get_format_zero_nb_integer(nb):
    h = nb
    c = 0
    while h > 0:
        h = int(h / 10)
        c += 1
    if c > 20:
        raise ValueError(
            "this should not be that high %s (nb=%s)" % (str(c), str(nb)))
    return "%0" + str(int(c)) + "d"


def test_regular_expression(exp=".*", text="", fLOG=fLOG):
    """
    Tests a regular expression.
    @param      exp     regular expression
    @param      text    text to check
    @param      fLOG    logging function
    """
    fLOG("regex", exp)
    fLOG("text", text)
    ex = re.compile(exp)
    ma = ex.search(text)
    if ma is None:
        fLOG("no result")
    else:
        fLOG(ma.groups())


def IsEmptyString(s):
    """
    Tells if a string is empty.

    @param      s       string
    @return             boolean
    """
    if s is None:
        return True
    return len(s) == 0


def is_empty_string(s):
    """
    Tells if a string is empty.

    @param      s       string
    @return             boolean
    """
    if s is None:
        return True
    return len(s) == 0


def file_head(file="",
              head=1000,
              out=""):
    """
    Keeps the head of a file.

    @param      file        file name
    @param      head        number of lines to keep
    @param      out         output file, if == None or empty, then, it becomes:
                                file + ".head.%d.ext" % head
    @return                 out
    """
    if not os.path.exists(file):
        raise FileNotFoundError("unable to find file %s" % file)
    if IsEmptyString(out):
        f, ext = os.path.splitext(file)
        out = "%s.head.%d%s" % (file, head, ext)

    f = open(file, "r")
    g = open(out, "w")
    for i, line in enumerate(f):
        if i >= head:
            break
        g.write(line)
    f.close()
    g.close()
    return out


def file_split(file="", nb=2, out="", header=False, rnd=False):
    """
    Splits a file.

    @param      file        file name or stream
    @param      nb          number of files
    @param      out         output file, if == None or empty, then, it becomes:
                            ``file + ".split.%d.ext" % i``, it must contain ``%d``
                            or it must a a list or strings or streams
    @param      header      consider a header or not
    @param      rnd         randomly draw the file which receives the current line
    @return                 number of processed lines
    """
    if not os.path.exists(file):
        raise FileNotFoundError("unable to find file %s" % file)

    if is_empty_string(out):
        f, ext = os.path.splitext(file)
        out = "%s.split.%s%s" % (file, _get_format_zero_nb_integer(nb), ext)
    elif not isinstance(out, list) and "%d" not in out:
        raise ValueError("%d should be present in out='{0}'".format(out))

    size = os.stat(file).st_size
    f = open(file, "r") if isinstance(file, str) else file
    g = {}
    tot = 0
    last_line = 0
    for i, line in enumerate(f):
        last_line = i
        if i == 0 and header:
            for n in range(0, nb):
                if n not in g:
                    if isinstance(out, list):
                        if isinstance(out[n], str):
                            g[n] = open(out[n], "w")
                        else:
                            g[n] = out[n]
                    else:
                        g[n] = open(out % n, "w")
                g[n].write(line)
            continue

        if rnd:
            n = random.randint(0, nb - 1)
        else:
            n = int(min(nb, tot * nb / size))
            tot += len(line)

        if n not in g:
            if isinstance(out, list):
                if isinstance(out[n], str):
                    g[n] = open(out[n], "w")
                else:
                    g[n] = out[n]
            else:
                g[n] = open(out % n, "w")
        g[n].write(line)

        if (i + 1) % 10000 == 0:
            fLOG("    processed ", i, " bytes ", tot,
                 " out of ", size, " lines in ", out)

    if isinstance(file, str):
        f.close()
    for k, v in g.items():
        if not isinstance(out, list) or isinstance(out[k], str):
            v.close()
    return last_line


def file_list(folder, out=""):
    """
    Prints the list of files and sub files in a text file.

    @param      folder      folder
    @param      out         result
    @return                 out
    """
    if out is None or isinstance(out, str):
        if is_empty_string(out):
            out = "%s_.list_of_files.txt" % folder
        f = open(out, "w")
    else:
        f = out

    for li in explore_folder_iterfile(folder):
        f.write(li)
        f.write(GetSepLine())

    if isinstance(out, str):
        f.close()

    return out


def file_grep(file="", regex=".*", out="", head=-1):
    """
    Grep.

    @param      file        file name
    @param      regex        regular expression
    @param      out         output file, if == None or empty, then, it becomes:
                                file + ".head.%d.ext" % head
    @param      head        stops after the first head lines (or -1 if not stop)
    @return                 out
    """
    if not os.path.exists(file):
        raise FileNotFoundError("unable to find file %s" % file)
    if IsEmptyString(out):
        f, ext = os.path.splitext(file)
        out = "%s.regex.%d%s" % (file, head, ext)

    exp = re.compile(regex)

    f = open(file, "r")
    g = open(out, "w")
    nb = 0
    for line in f:
        if exp.search(line):
            g.write(line)
            nb += 1
            if nb >= head >= 0:
                break
    f.close()
    g.close()
    return out
