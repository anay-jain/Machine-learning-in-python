import sys

print(sys.argv) # will give file name 
 
def printsum():
 	print(int(sys.argv[1]) + int(sys.argv[2]))
printsum()
# print(sys.version)
# print(sys.path)
# print(sys.maxint)
print(sys.stdout)
print(type(sys.stdout))