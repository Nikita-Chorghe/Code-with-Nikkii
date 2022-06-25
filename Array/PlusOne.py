class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        sum = 0
        decimal = 1
        for i in range(len(digits)):
            sum = sum + ((digits[i] * (decimal)))
            decimal *=10
        sum1 = sum+1
        x = [int(a) for a in str(sum1)]
        return x
                
       
            
        
         
        
            
        