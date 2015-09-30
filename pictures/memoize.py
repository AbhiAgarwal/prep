class memoize(object):
    def __init__ (self, f):
        self.f = f
        self.storage = {}
    def __call__ (self, *args, **kwargs):
        key = str((self.f.__name__, args, kwargs))
        try:
            value = self.storage[key]
        except KeyError:
            value = self.f(*args, **kwargs)
            self.storage[key] = value
