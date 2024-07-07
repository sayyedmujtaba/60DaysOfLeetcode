#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            return num * factorial(num - 1)
        
        res = []
        i = 1
        while True:
            fact = factorial(i)
            if fact > n:
                break
            res.append(fact)
            i += 1
        
        return res 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends