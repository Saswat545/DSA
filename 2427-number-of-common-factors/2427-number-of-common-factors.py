class Solution(object):
    def commonFactors(self, a, b):
        def get_gcd(x, y):
            while y:
                x, y = y, x % y
            return x            
        g = get_gcd(a, b)
        return sum(1 for i in xrange(1, g + 1) if g % i == 0)
