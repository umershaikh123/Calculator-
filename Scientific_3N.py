 
import math
from typing import List

def sin(angle):
    degree = math.radians(angle)
    out = math.sin(degree)
    return out

def cos(angle):
     degree = math.radians(angle)
     out =math.cos(degree)
     
     return out

def tan(angle):
     degree = math.radians(angle)
     out = math.tan(degree)
     
     return out

def square_root(value):
     out = math.sqrt(value)
     return out

def log(value):
     out = math.log10(value)
     return out

def ln(value):
     out = math.log(value)
     return out   

def e(value):
     out = math.exp(value)
      
     return out

def Power(base , power):
     out = math.pow(base , power)    
     return out

print("\n")
list = ['0' , '0' , '0' ]
operator = []

error = True
while (error == True):
    print("\n")
     
 
    for i in range(3):

        print("Type a function from below that you want to perform on this value" ,"\n")
         
        print("'s.r' (square root) , e , log , ln , power , sin , cos , tan  " ,"\n")
         

        if( i == 0):
          print("You can also skip this if you want just press enter")

        function = input("Function : ")
        print("\n")
         
        print("Now Enter your", i+1," value : ")
        value = float( input("Value : ") )
        print("\n")
        list[i] = value
 

        if(function == "s.r" ):
            if(value < 0):
                print("Error , Square root value can't be negative","\n")               
                break
            out = square_root(value)
            list[i] =  out 

        elif(function == "e" ):
            out = e(value)
            list[i] =  out 

        elif(function == "log" ):
            if(value <= 0):
                print("Error , log value can't be zero or negative","\n")               
                break
            out = log(value)
            list[i] =  out 

        elif(function == "ln" ):
            if(value <= 0):
                print("Error , log value can't be zero or negative","\n")                
                break
            out = ln(value)
            list[i] =  out 

        elif(function == "power" ):

            print("Type the exponent of " , value)
            exp = int( input("Exponent : ") )
            if(value == 0 and exp == 0):
                print("Error , invalid expression ","\n")                
                break
            out = Power(value , exp)
            list[i] =  out             

        elif(function == "sin" ):
            out = sin(value)
            list[i] =  out 

        elif(function == "cos" ):
            out = cos(value)
            list[i] =  out 

        elif(function == "tan" ):
            out = tan(value)
            list[i] =  out 

        if( i != 2):
           print("Now enter an operator from given below  ")
           print("+ , - , * , / ")            
           operator.append( input("Operator : ") )
           print("\n")
    
    for j in range(2):
 
        if(list[j] == '0'):
            error == True
            break
        
        elif (operator[j] == "/" and list[j+1] == 0 or list[j+1] == 0.0):
            print("Error value cannot be divided by zero !")
            print("Type the value again","\n")
            error = True
            break

        else:
            error = False

        if(operator[j] == "/"):
            list[j] = float(list[j])
            list[j+1] = float(list[j+1])        



operator.append(" = ")
Result = [ '0', '0']
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

    for j in range(2):

        if(operator[j] == o[i]):

            if(j == 0):

                if(Result[j+1] == '0'):
                    Result[j] = operation(i ,list[j] , list[j+1])
                    p = j
                    

                elif(Result[j+1] != '0'):
                    Result[j] = operation( i ,list[j] , Result[j+1])
                    p = j
                   

            elif(j == 1):

                if(Result[j-1] == '0' ):
                    Result[j] = operation(i ,list[j] , list[j+1])
                    p = j
                    

                elif(Result[j-1] != '0' ):
                    Result[j] = operation(i , Result[j-1],list[j+1])
                    p = j
                


ans = Result[p] 

for i in range(3):
    string = "{}  {} "
    print( string.format(list[i] , operator[i]) , end="")

print(" " , ans , "\n")
