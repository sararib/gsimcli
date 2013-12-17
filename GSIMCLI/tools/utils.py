'''
Created on 6 de Nov de 2013

@author: julio
'''
import os


def dms2dec(d, m, s):
    """Converts Degrees, Minutes, Seconds formatted coordinates to decimal.

    Formula:
    DEC = (DEG + (MIN * 1/60) + (SEC * 1/60))

    Assumes that data is signalled.
    """
    return int(d) + float(m) / 60 + float(s) / 3600


def is_number(s):
    """Check if s is a number"""
    try:
        float(s)
        return True
    except ValueError:
        return False
    # except TypeError:
    #    return False


def skip_lines(file_id, nlines):
    """Skip the next nlines from the file handled with file_id."""
    for i in xrange(nlines):  # @UnusedVariable
        file_id.readline()


def filename_seq(file_id, n):
    """Generator to create a sequence of numbered filenames.

    """
    base, ext = os.path.splitext(file_id)
    for i in xrange(n):
        fname = base + '_' + str(i) + ext
        i += 1
        yield fname


def filename_numbering(file_id, n):
    """Insert a numeric index in a filename.

    """
    base, ext = os.path.splitext(file_id)
    fname = base + '_' + str(n) + ext
    return fname


if __name__ == '__main__':
    pass
