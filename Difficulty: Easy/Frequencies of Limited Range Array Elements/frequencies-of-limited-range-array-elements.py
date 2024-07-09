class Solution:
    def frequencyCount(self, arr, N, P):
        
        for i in range(N):
            if arr[i] > N:
                arr[i] = 0
                
        for i in range(N):
            if arr[i] % (N + 1) != 0:
                arr[(arr[i] % (N + 1)) - 1] += (N + 1)
                
        for i in range(N):
            arr[i] = arr[i] // (N + 1)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends