#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        N = abs(N)
        count = 0
        original_N=N
        while N>0:
            digit= N%10
            if digit != 0 and original_N % digit == 0:
                count+=1
            N//=10
        
        return count
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends