# input
n= int(input("Dijite el valor n:"))

#processing

s=0
i=1
while i<=n:
    s=s+i
    i=i+1 

print("la suma de los " + str(n)+ "primeros numeros naturales es "+ str (s))