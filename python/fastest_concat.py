from cStringIO import StringIO
from UserString import MutableString
from array import array

import sys, timeit

loop_count = 80000

def fastest():
    out_str = ''.join([`num` for num in xrange(loop_count)])
    return out_str

def second():
    out_str = ''.join(`num` for num in xrange(loop_count))
    return out_str

def third():
    out_str = ''
    for num in xrange(loop_count):
        out_str += `num`
    return out_str

print 'fastest=', timeit.timeit(fastest, number=10)
print 'second=', timeit.timeit(second, number=10)
print 'third=', timeit.timeit(third, number=10)
