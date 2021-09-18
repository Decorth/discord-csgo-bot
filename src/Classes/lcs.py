class lcs:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getAnswer(self):
	    m = len(self.x) 
	    n = len(self.y) 
	  
	    L = [[None]*(n + 1) for i in range(m + 1)] 
	  
	    for i in range(m + 1): 
	        for j in range(n + 1): 
	            if i == 0 or j == 0 : 
	                L[i][j] = 0
	            elif self.x[i-1] == self.y[j-1]: 
	                L[i][j] = L[i-1][j-1]+1
	            else: 
	                L[i][j] = max(L[i-1][j], L[i][j-1]) 
	    return L[m][n]