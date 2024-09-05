

import math

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        x = (mean * (len(rolls) + n)) - sum(rolls)
        if x > 6 * n or x < n:
            return []
        
        result = []
        nmf = math.floor(x / n)
        nmc = math.ceil(x / n)    
      
        count_nmf = x % n
        count_nmc = n - count_nmf
        
        result.extend([nmf] * count_nmc)
        result.extend([nmc] * count_nmf)
        
        return result
