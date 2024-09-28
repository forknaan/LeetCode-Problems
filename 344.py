# Furqan Saeed
# fsaeed@andrew.cmu.edu

# Reverse String
def reverseString(s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s