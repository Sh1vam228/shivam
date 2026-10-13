class Solution(object):
    def reverseWords(self, s):
        d=s.split()
        d=d[::-1]
        f=''
        for i in d:
            f+=i
            f+=' '
        return f[:-1]    
        