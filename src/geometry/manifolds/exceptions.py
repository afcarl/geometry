
class DoesNotBelong(Exception):
    ''' Exception thrown when a point does not belong
        to a certain manifold *M*. '''
    def __init__(self, M, point, e, context=None):
        self.M = M
        self.point = point
        self.e = '%s' % e
        self.context = context
        
    def __str__(self):
        s = ''
        if self.context is not None:
            s += '%s\n' % self.context
        s += '%s: The point does not belong here: %s\n' % (self.M, self.point)
        s += self.e
        return s 
