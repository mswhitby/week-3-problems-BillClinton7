def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
  	return n1 - n2
  	
def multiply(n1, n2):
  	return n1 * n2
  	
def divide(n1, n2):
  	return n1 / n2
  	
print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3.Multiply")
print("4.Divide")
	
while True:
    choice = input("Enter choice(1/2/3/4):")
    if choice in ('1','2','3','4'):
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
		
    if choice == '1':
    	print(num1, "+", num2, "=", (num1 + num2))
    	     
    elif choice == '2':	
        print(num1, "-", num2, "=", (num1 - num2))
            
    elif choice == '3':
    	print(num1, "*", num2, "=", (num1 * num2))
    		 
    elif choice == '4':
        print(num1, "/", num2, "=", (num1 / num2))
           
         
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "yes":
        pass
    elif next_calculation == "no":
        break
    else:
        print("Invalid Input")





