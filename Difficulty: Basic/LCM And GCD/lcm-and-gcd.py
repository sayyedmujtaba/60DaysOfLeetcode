#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        def gcd(a,b):
            while b:
                a,b = b, a % b
            return a
        
        gcd_val = gcd(A, B)
        lcm_val = (A*B)//gcd_val
        
        return[lcm_val, gcd_val]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends