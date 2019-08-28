try:
	n=int(input())
except:
	pass
for x in range(1,n+1):
	print(x,end=" ")
print(end="\n")
for i in range(n-1):
	for t in range (1,n-i):
		print(t, end=" ")
	print('* '*(i*2+1) , end=" ")	
	print(end="\n")	
