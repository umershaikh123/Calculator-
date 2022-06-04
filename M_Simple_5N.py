 
from typing import List


print("\n")
list = []
operator = []

error = True
while (error == True):
    for i in range(5):
        print("Enter your " , i+1 ," number : ")
        list.append( float(input("Number : ")) )
        print("\n")
 
        if( i != 4):
           print("Now enter an operator , such as: + , - , * , / ")           
           operator.append( input("Operator : ") )
           print("\n")
    
    for j in range(4):
        if (operator[j] == "/" and list[j+1] == 0 or list[j+1] == 0.0):
            print("Error value cannot be divided by zero !")
            print("Type the value again", "\n")
            error = True
        else:
            error = False
    

       
operator.append(" = ")
 
Result = [ '0', '0', '0' , '0']
p = []
s = 0

def add(a,b):
    return a+b

def subtract(a,b):    
    return a-b

def multiply(a,b):
    return (a*b)

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

    for j in range(5):

        if(operator[j] == o[i]):

            if (j == 0):

                if(Result[j+1] == '0' ):
                    Result[j] = operation( i ,list[j],list[j+1] )
                    p.append(j)
                    s = j

                elif(Result[j+1] != '0' and Result[j+2] == '0'):
                    Result[j] = operation( i , list[j],Result[j+1] )
                    p.append(j)
                    s = j

                elif(Result[j+1] != '0' and Result[j+2] != '0' and Result[j+3] != '0'):
                    Result[j] = operation( i , list[j],Result[s] )
                    p.append(j)
                    s = j                              

                elif(Result[j+1] != '0' and Result[j+2] != '0'):
                    Result[j] = operation( i , list[j],Result[s])
                    p.append(j)
                    s = j

            elif(j == 1):

                if(Result[j-1] == '0' and Result[j+1] == '0'):
                    Result[j] = operation( i , list[j],list[j+1] )
                    p.append(j)
                    s = j

                elif(Result[j-1] != '0' and Result[j+1] == '0'):
                    Result[j] = operation( i , Result[j-1],list[j+1] )
                    p.append(j)
                    s = j

                elif(Result[j-1] == '0' and Result[j+1] != '0'):
                    Result[j] = operation( i , list[j+1],Result[j+1] )
                    p.append(j)
                    s = j

                elif(Result[j-1] != '0' and Result[j+1] != '0' and Result[j+2] != '0'):
                    Result[j] = operation( i , Result[j-1],Result[p[i]] )
                    p.append(j)
                    s = j          

                elif(Result[j-1] != '0' and Result[j+1] != '0'):
                    Result[j] = operation( i , Result[j-1],Result[j+1] )
                    p.append(j)
                    s = j
                    

                elif(Result[j-1] == '0' and Result[j+1] != '0' and Result[j+2] != '0'):
                    Result[j] = operation( i , list[j],Result[s] )
                    p.append(j)                        
                    s = j




            elif(j == 2):
                if(Result[j-1] == '0' and Result[j+1] == '0'):
                    Result[j] = operation( i , list[j],list[j+1] )
                    p.append(j)
                    s = j 
                elif(Result[j-1] != '0' and Result[j+1] == '0'):
                    Result[j] = operation( i , Result[j-1],list[j+1] )
                    p.append(j)
                    s = j

                elif(Result[j-1] == '0' and Result[j+1] != '0'):
                    Result[j] = operation( i , list[j],Result[j+1] )
                    p.append(j)
                    s = j

                elif(Result[j-1] != '0' and Result[j+1] != '0' and Result[j-2] != '0'):
                    Result[j] = operation( i , Result[p[i]],Result[j+1] )
                    p.append(j)
                    s = j

                elif(Result[j-1] != '0' and Result[j+1] != '0'):
                    Result[j] = operation( i , Result[j-1],Result[j+1] )
                    p.append(j) 
                    s = j

                elif(Result[j+1] == '0' and Result[j-1] != '0' and Result[j-2] != '0'):
                    Result[j] = operation( i , Result[s],list[j+1] )
                    p.append(j) 
                    s = j                                   

            elif(j == 3):       

                if(Result[j-1] == '0' ):
                    Result[j] = operation( i , list[j],list[j+1] )
                    p.append(j)
                    s = j

                elif(Result[j-1] != '0' and Result[j-2] == '0'):
                    Result[j] = operation( i , Result[j-1],list[j+1] )
                    p.append(j)
                    s = j

                elif(Result[j-1] != '0' and Result[j-2] != '0' and Result[j-3] != '0'):
                    Result[j] = operation( i , Result[s],list[j+1] )
                    p.append(j)
                    s = j                              

                elif(Result[j-1] != '0' and Result[j-2] != '0' and Result[j-3] == '0'):
                    Result[j] = operation( i , Result[s],list[j+1] )
                    p.append(j)
                    s = j
                    
print(p)
ans = Result[s] 

for i in range(5):
    string = "{}  {} "
    print( string.format(list[i] , operator[i]) , end="")

print(" " , ans , "\n")


