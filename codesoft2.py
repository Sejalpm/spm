def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2
 
def multiply(n1,n2):
    return n1*n2
 
def divide(n1,n2):
    return n1/n2
 
print("operation -\n" \
      "1. Addition\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Division\n")
 
select = int(input("Select operation:"))
 
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
 
if select == 1:
    print(a,"+",b,"=",add(a,b))
 
elif select == 2:
    print(a,"-",b,"=",subtract(a,b))
 
elif select == 3:
    print(a,"*",b,"=",multiply(a,b))
 
elif select == 4:
    print(a,"/",b,"=",divide(a,b))
    
else:
    print("Invalid input")
