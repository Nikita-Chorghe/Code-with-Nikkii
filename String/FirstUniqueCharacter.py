class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        allelem = {}
        for i in range(len(s)):
            if s[i] not in allelem:
                unique[s[i]] = i
                allelem[s[i]] = i
            elif s[i] in unique:
                unique.pop(s[i])
                
        if (len(unique)>0):
            result = list(unique.keys())[0]
            return unique[result]
        else:
            return -1
          
            
                

        