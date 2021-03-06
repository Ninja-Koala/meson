#!/usr/bin/env python3

import sys
import pathlib

[ifilename, ofilename] = sys.argv[1:3]

ftempl = '''int %s() {
    return 6;
}
'''

d = pathlib.Path(ifilename).read_text().split('\n')[0].strip()

pathlib.Path(ofilename).write_text(ftempl % d)
