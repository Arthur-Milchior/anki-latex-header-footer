import sys

if (sys.version_info > (3, 0)):
    # Python 3 code in this block
    from . import latex21
else:
    from . import latex20
