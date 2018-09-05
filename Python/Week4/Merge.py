def Merge(A,B):#Merge A[0:m], B[0:n]
	(C,m,n)=([],len(A), len(B))
	(i,j)=(0,0)
	while i+j <m+n:
	    if i==m:
		    C.append(B[j])
		    j=j+1
	    elif j==n:
		    C.append(A[i])
		    i=i+1
	    elif A[i]<=B[j]:
		    C.append(A[i])
		    i=i+1
	    elif A[i]>B[j]:
		    C.append(B[j])
		    j=j+1
	return(C)
	
	def mergesort(A,left,right):
	#sort the slice A[left:right]
	if right -left <=1:
		return (A[left:right])
	if right -left>1:
		mid=(left+right)//2
	L=mergesort(A,left,mid)
	R=mergesort(A,mid,right)
	return(Merge(L,R))
	
	def Quicksort(A,l,r):
	if r-l<=1:
		return()
	yellow=l+1
	for green in range(l+1,r):
			if A[green]<=A[l]:
				(A[yellow],a[green])=(A[green],a[yellow])
				yellow=yellow+1
			(A[l],A[yellow-1])=(A[yellow-1],A[l])
			Quicksort(A,l,yellow-1)
			Quicksort(A,yellow,r)
	return(A)

	[(x,y,z) for x in range(100) for y in range(x,100) for z in range(y,100) if squre(x)+square(y)==square(z)]
	
	def square(x):
	return(x*x)
	
	def iseven(x):
	return(x%2==0)
	
	
(1) Consider the following Python function.
  def mystery(l):
     if l == []:
        return (l)
     else:
        return (l[-1:] + mystery(l[:-1]))
		
		Ans : [15, 81, 17, 23, 13]
		
	(2) pairs = [ (x,y) for x in range(4) for y in range(3) if (x+y)%3 == 0 ]
	
	Ans: [(0, 0), (1, 2), (2, 1), (3, 0)]
	
	
	
	