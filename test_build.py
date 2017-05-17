
import sys
from build import merge_into
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

a = [1, 2, 3]
test(merge_into(a, [], 5, len(a)))



a = [1,  3,  5,  7,  9,  None,  None,  None]
b = [4,  5,  6]
test(merge_into(a, b, 5, len(b)))