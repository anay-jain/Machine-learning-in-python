# x=0
# t=[int(x) for x in input().split('')]
# if x<t:
# 	pass
# elif x>t:
# 	if x<t:
# 		print("false")	
# 		break;
# print("true")		
n=int(input())
s=list()
b=False
for i in range(0,n):
	t=int(input())
	s.append(t)
for i in range(n):	
	if s[i]<s[i+1]:
		b=True
	elif s[i]>s[i+1]:
		b=True
		if s[i]<s[i+1]:
			b=False	
	else:
		b=False		

if b:
	print("true")
else:
	print("false")	
		