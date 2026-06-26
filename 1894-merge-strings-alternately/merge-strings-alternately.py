class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        rtype = ""
        maxlen = len(word1)
        if(maxlen < len(word2)):
            maxlen = len(word2)
    
        for i in range(maxlen):
            if(len(word1) <= i):
                rtype = rtype + word2[i]
            
            elif(len(word2) <= i):
                rtype = rtype + word1[i]
            
            else:
                rtype = rtype + word1[i] + word2[i]

        return rtype
        