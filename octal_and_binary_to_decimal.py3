##################################
#	Octal & Binary to Decimal	#
#		 By: Knowledgeless	   # 
##################################

def convert(n, b):
	k = []
	i = 0
	while(n>0):
		k.insert(0, n%10)
		n = n//10
		d = len(k)-1
		j = 0		
	for i in k:
		j += i*(b**d)
		d = d - 1
	print(j)
	
T = int(input())
for i in range (T):
	n = int(input())
	b = int(input())
	convert(n, b)