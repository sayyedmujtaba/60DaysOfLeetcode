#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range (N,0,-1):
            for j in range (N-i):
                print(" ", end="")
            for k in range (i*2-1):
                print("*", end="")
            print()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends