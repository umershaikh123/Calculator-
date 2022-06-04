 
from typing import List


print("\n")
list = []
operator = []

error = True
while (error == True):
    for i in range(4):
        print("Enter your " , i+1 ," number : ")
        list.append( float(input("Number : ")) )
        print("\n")
 
        if( i != 3):
           print("Now enter an operator , such as: + , - , * , / ")            
           operator.append( input("Operator : ") )
           print("\n")
    
    for j in range(3):
        if (operator[j] == "/" and list[j+1] == 0 or list[j+1] == 0.0):
            print("Error value cannot be divided by zero !")
            print("Type the value again", "\n")
            error = True
        else:
            error = False
        if(operator[j] == "/"):
            list[j] = float(list[j])
            list[j+1] = float(list[j+1])        
       
operator.append(" = ")
Result = [ '0', '0', '0']
p = 0

def add(a,b):
    return a+b

def subtract(a,b):    
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b 

o = ["/" , "*" , "-" , "+"]

def operation(s, a,b):
    if(o[s] == "/"):
       return divide(a,b)

    elif(o[s] == "*"):
        return multiply(a,b)    

    elif(o[s] == "-"):
        return subtract(a,b) 

    elif(o[s] == "+"):
        return add(a,b) 



for i in range(4):

    for j in range(3):

        if(operator[j] == o[i]):

           if (j == 0):
               if(Result[j+1] == '0'):
                  Result[j] = operation( i , list[j] ,list[j+1] )
                  p = j

               elif(Result[j+1] != '0' and Result[j+2] != '0'):
                   Result[j] =  operation( i ,list[j] ,Result[p] )
                   p = j

               elif(Result[j+1] !='0' and Result[j+2] == '0'):
                    Result[j] =  operation( i ,list[j],Result[j+1])
                    p = j

 
           elif(j == 1):
                if(Result[j-1] == '0' and Result[j+1] == '0'):
                    Result[j] =  operation( i ,list[j],list[j+1])
                    p = j

                elif(Result[j-1] != '0' and Result[j+1] == '0'):
                      Result[j] =  operation( i ,Result[j-1],list[j+1])
                      p = j

                elif(Result[j-1] == '0' and Result[j+1] != '0'):
                   Result[j] =  operation( i ,list[j], Result[j+1])
                   p = j
   
                elif(Result[j-1] != '0' and Result[j+1] != '0'):
                    Result[j] =  operation( i ,Result[j-1],Result[j+1])
                    p = j    



           elif(j == 2):
               if(Result[j-1] == '0'):
                   Result[j] =  operation( i ,list[j],list[j+1])
                   p = j

               elif(Result[j-1] != '0' and Result[j-2] != '0'):
                   Result[j] = operation( i, Result[p],list[j+1])
                   p = j

               elif(Result[j-1] != '0'):
                   Result[j] =  operation( i ,Result[j-1],list[j+1] )
                   p = j

 

ans = Result[p] 

for i in range(4):
    string = "{}  {} "
    print( string.format(list[i] , operator[i]) , end="")

print(" " , ans , "\n")


 