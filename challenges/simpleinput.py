a=list()
try:
	a = [int(x) for x in input().split('')]
except:
	pass
n=0;
for i in range(len(a)):
	n=n+a[i]
	if n>-1:
		print(a[i])
	else:
		break;	




n=0
while n>-1:
	t=int(input())
	n=n+t
	if n>-1:
		print(t)
	else:
		break;	
