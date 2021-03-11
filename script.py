a=0
n=int(input("\nInserta número:\n"))
for i in range(1,n+1):
 if(n % i==0):
  a=a+1
if(a!=2):
 print("No es Primo..")
else:
 print("Es Primo!!")
