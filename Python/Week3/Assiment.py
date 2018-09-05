def descending(l):
	if l==[]:
		return(True)
	else:
		for i in range(0, len(l)):
			k=i
			if not k+1==len(l) and l[k]<l[k+1]:
				return(False)
		else:
			return(True)
          
def valley(l):
	n=len(l)
	m=l+[]
	m.sort()
	min=m[0]
	indx=l.index(min)
	if (n-indx)==1:
	 return (False)
	 
	for i in range(0, indx):
		k=i
		if not (indx-1)==n and l[k]<=l[k+1]:
			return(False)
	for i in range(indx,n):
		k=i
		if not (k+1)==len(l) and l[k]>=l[k+1]:
			return(False)
	else:
		return(True)
		
		
def transpose(matrix ):
    if not matrix: return []
    return [ [ row[ i ] for row in matrix ] for i in range( len( matrix[ 0 ] ) ) ]