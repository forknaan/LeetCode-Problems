#https://leetcode.com/problems/reverse-integer/description/

def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0] == '-':
            x = x[1::]
            x = '-' + x[::-1]
            x = int(x)
        else:
            x = int(x[::-1])
        
        a = 2**31 - 1
        b = (-2)**31
        if x < b or x > a:
            return 0
        else:
            return x