class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
            :type deck: List[int]
            :rtype: bool
            """
        def gcd(x,y):
            while y:
                r = x%y
                x = y
                y = r
            return x
        l = []
        for i in set(deck):
            l.append(deck.count(i))
        return reduce(lambda x,y:gcd(x,y), l)>1 and len(deck)>1

