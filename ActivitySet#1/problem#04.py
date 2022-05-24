# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
aa = input("Enter the Rate:")
a = float(aa)
if h <= 40:
 	print( h  * a)
elif h > 40:
	print(40* a + (h-40)*1.5*a)