class Solution:
    def reverse(self, x: int) -> int:
        if x==abs(x) :
            number = int(str(x)[::-1])
        else: 
            number = (-1)*(int(str(abs(x))[::-1]))
        if (number>=2**31 or number<-(2**31)): 
            return 0
        else: 
            return number
        

        
    
            
           
        
     