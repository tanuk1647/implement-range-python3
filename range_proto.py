import collections
import numbers


class Range(collections.abc.Sequence):
    def __init__(self, *args):
        if len(args) == 0:
            raise TypeError('Range expected 1 arguments, got 0')
        elif len(args) > 3:
            raise TypeError('Range expected at most 3 arguments,'
                            f' got {len(args)}')
        else:
            cargs = ()
            for arg in args:
                if isinstance(arg, numbers.Integral):
                    cargs += (arg,)
                elif hasattr(arg, '__index__'):
                    cargs += (arg.__index__(),)
                else:
                    raise TypeError(f"'{type(arg).__name__}' object "
                                    "cannot be interpreted as an integer")
            if len(cargs) == 1:
                self.start, self.stop, self.step = 0, cargs[0], 1
            elif len(cargs) == 2:
                self.start, self.stop, self.step = cargs[0], cargs[1], 1
            else:
                self.start, self.stop, self.step = cargs
                if self.step == 0:
                    raise ValueError('Range() arg 3 must not be zero')
            self._len = max(0,
                            ((self.stop - self.start) // self.step)
                            +  bool((self.stop - self.start) % self.step))
    
    def __len__(self):
        return self._len
    
    def __getitem__(self, i):
        if isinstance(i, slice):
            result = Range(*(i.indices(self._len)))
        elif isinstance(i, numbers.Integral):
            if not (-self._len <= i < self._len):
                raise IndexError('Range object index out of range')
            else:
                if i < 0:
                    i += self._len
                result = self.start + self.step * i
        else:
            raise TypeError('Range indices must be integers or slices, '
                            f'not {type(i).__name__}')
        return result
    
    def __bool__(self):
        return bool(self._len)
    
    def __repr__(self):
        if self.step == 1:
            result = f'Range({self.start}, {self.stop})'
        else:
            result = f'Range({self.start}, {self.stop}, {self.step})'
        return result
    
    def __eq__(self, other):
        if not isinstance(other, Range):
            return False
        return (self.start, self.stop, self.step) == (other.start, other.stop, other.step)
    
    def __ne__(self, other):
        return not self == other
    
    def __hash__(self):
        return hash((type(self), self.start, self.stop, self.step))
