class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in s.lower() if 'a' <= c <= 'z' or '0' <= c <= '9'])
        l,r = 0, len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
                
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
               