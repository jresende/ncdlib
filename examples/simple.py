#!/usr/bin/env python
"""Simple example of how to use ncdlib"""

# Copyright (C) 2013  Marco Almeida <marcoafalmeida@gmail.com>

# This file is part of ncdlib.

# ncdlib is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.

# ncdlib is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.

# You should have received a copy of the GNU General Public License
# along with ncdlib.  If not, see <http://www.gnu.org/licenses/>.


import sys
from ncdlib import compute_ncd, available_compressors


def compare_files(infile1, infile2):
    """Simply call compute_ncd() and return the result."""
    for compressor in available_compressors():
        ncd = compute_ncd(infile1, infile2, compressor)
        print("{0:8} NCD({1}, {2}) = {3:.4f}".format(compressor,
                                                     infile1,
                                                     infile2,
                                                     ncd))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: %s <file1> <file2>" % sys.argv[0])
    compare_files(sys.argv[1], sys.argv[2])
