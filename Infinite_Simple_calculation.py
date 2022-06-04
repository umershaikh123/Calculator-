
from typing import List


print("\n")
list = []
operator = []

print("Please Enter the same input again.") 
n = int(input("Input : "))        

for i in range(n):
    print("\n","Enter your " , i+1 ," number : ")
    list.append( float(input(" Number : ")) )
    print("\n")

    if( i != n-1):
        print(" Now enter an operator , such as: + , - , * , / ")           
        operator.append( input(" Operator : ") )   
        print("\n")



operator.append(" = ")
p = []
k = []
Result = []
C = []
 
for i in range (n-1):
    Result.append("0")
    k.append('0') 

for i in range (n-1):     
    C.append(0)

 
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


 
s = 0
p_o = 0
p_o1 = 0
p_o2 = 0
g = 0
g1 = 0
g2 = 0
Rm = n-1
 

for i in range(4):

    for j in range(n):

        if(operator[j] == o[i]):


# Section 1
            for s in range(1):

                if j == 0:           

                    if(Result[j+1] == '0'):                                           
                        Result[j] = operation(i , list[j] , list[j+1])
                        p.append(j)
                        s = j            

                        for l in range(len(k)):
                            if(l == len(p)-1 ):
                                k[l] = p[-1]  

                        sum = 0
                        for v in range(len(C)):
                            if(k[v] != '0'):
                              C[k[v]] = sum  
                              sum = sum+1 
    

                    elif Result[j+1] != '0':
                        if(Result[j+1] != '0' and Result[j+2] == '0'):
                            Result[j] = operation(i , list[j] , Result[j+1])
                            p.append(j) 
                            s = j     
                                                  
                            for l in range(len(k)):
                                if(l == len(p)-1 ):
                                    k[l] = p[-1]

                            sum = 0
                            for v in range(len(C)):
                                if(k[v] != '0'):
                                    C[k[v]] = sum  
                                    sum = sum+1
                            break



                        for u1 in range(j+1 , Rm):
                            if (Result[u1] == '0'):
                                p_o = u1                                
                                break

                            elif(u1 == Rm-1 and Result[Rm-1] != '0'  and Result[Rm-2] != '0'):
                                p_o = Rm
                                break                          

                                                    
                        g = 0
                        for f1 in range(j+1, p_o):                           
                            if(g < C[f1]):
                                g = f1                                                                                                   
                        Result[j] = operation(i ,list[j], Result[g] )
                        p.append(j)
                        s = j
    
                        for l in range(len(k)):
                            if(l == len(p)-1 ):
                                k[l] = p[-1]

                        sum = 0
                        for v in range(len(C)):
                            if(k[v] != '0'):
                              C[k[v]] = sum  
                              sum = sum+1
 
                        

 # Section 2
         
            for a in range(1):
                if (j > 0 and j < Rm-1):
                    

                    if(j == Rm-2):  

                        if(Result[j+1] != '0' and Result[j-1] == '0' ):
                            Result[j] = operation(i , list[j] ,  Result[j+1] )
                            p.append(j)                               
                            for l in range(len(k)):
                                if(l == len(p)-1 ):
                                    k[l] = p[-1]

                            sum = 0
                            for v in range(len(C)):
                                if(k[v] != '0'):
                                    C[k[v]] = sum  
                                    sum = sum+1
                 
                            s = j
                            break         



                        elif(Result[j-1] != '0' and Result[j+1] == '0' ):
                            Result[j] = operation(i , Result[j-1],list[j+1] )
                            p.append(j)
                                         
                            for l in range(len(k)):
                                if(l == len(p)-1 ):
                                    k[l] = p[-1]


                            sum = 0
                            for v in range(len(C)):
                                if(k[v] != '0'):
                                    C[k[v]] = sum  
                                    sum = sum+1                                                             
 
                            s = j
                            break 


                        elif(Result[j-1] != '0' and Result[j+1] != '0'  and Result[j-2] == '0'):
                            Result[j] = operation(i ,Result[j-1],Result[j+1]  )
                            p.append(j)                               
                            for l in range(len(k)):
                                if(l == len(p)-1 ):
                                    k[l] = p[-1]

                            sum = 0
                            for v in range(len(C)):
                                if(k[v] != '0'):
                                    C[k[v]] = sum  
                                    sum = sum+1
                            
                            s = j
                            break                      


                        elif(Result[j-1] != '0' and Result[j+1] != '0'  and Result[j-2] != '0'):

                            for t1 in reversed( range(0 ,j ) ) :  

                                if(Result[t1] == '0'):
                                    p_o = j-t1                                                    
                                    break

                                elif(t1 == 0 and Result[0] != '0' and Result[1] != '0' ):
                                    p_o = 0
                                    break  

                            g = 0
                            for q1 in range(p_o, j) :
                                if(g < C[q1]):
                                    g = q1
                                     
                            Result[j] = operation(i ,Result[g],Result[j+1])
                            p.append(j)                            
                                                   
                            for l in range(len(k)):
                                if(l == len(p)-1 ):
                                    k[l] = p[-1]

                            sum = 0
                            for v in range(len(C)):
                                if(k[v] != '0'):
                                    C[k[v]] = sum  
                                    sum = sum+1
                                   
                            s = j
                            break 



                    if(j == 1):
                        if(Result[j-1] != '0'  and Result[j+1] == '0' ):
                            Result[j] = operation(i , Result[j-1] , list[j+1])
                            p.append(j)         


                            for l in range(len(k)):
                                if(l == len(p)-1 ):
                                    k[l] = p[-1]

                            sum = 0                           
                            for v in range(len(C)):
                                if(k[v] != '0'):
                                    C[k[v]] = sum  
                                    sum = sum+1

                            s = j
                            break 

                        elif(Result[j+1] != '0'  and Result[j-1] == '0' ):
                            Result[j] = operation(i , list[j+1] , Result[j+1])
                            p.append(j)  

                            for l in range(len(k)):
                                if(l == len(p)-1 ):
                                    k[l] = p[-1]                             

                            sum = 0
                            for v in range(len(C)):
                                if(k[v] != '0'):
                                    C[k[v]] = sum  
                                    sum = sum+1
                                       
                            s = j
                            break


                        elif(Result[j-1] != '0' and Result[j+1] != '0' ):
                            Result[j] = operation(i ,Result[j-1],Result[j+1]  )
                            p.append(j)                               
                            for l in range(len(k)):
                                if(l == len(p)-1 ):
                                    k[l] = p[-1]

                            sum = 0
                            for v in range(len(C)):
                                if(k[v] != '0'):
                                    C[k[v]] = sum  
                                    sum = sum+1
                    
                            s = j
                            break 





                    if Result[j-1] == '0' and Result[j+1] == '0' :
                        Result[j] = operation ( i ,list[j] , list[j+1] )
                        p.append(j)

                        for l in range(len(k)):
                            if(l == len(p)-1 ):
                                k[l] = p[-1]

                        sum = 0
                        for v in range(len(C)):
                            if(k[v] != '0'):
                              C[k[v]] = sum  
                              sum = sum+1

                        s = j




                    elif(Result[j-1] != '0' and Result[j+1] == '0' ):
                           
                          if(j != 1):
                            if(Result[j-1] != '0'  and Result[j+1] == '0' and Result[j-2] == '0'):
                                Result[j] = operation(i , Result[j-1] , list[j+1])                    
                                p.append(j)  

                                for l in range(len(k)):
                                    if(l == len(p)-1 ):
                                        k[l] = p[-1]                                 

                                sum = 0
                                for v in range(len(C)):
                                    if(k[v] != '0'):
                                        C[k[v]] = sum  
                                        sum = sum+1
                       
                                s = j
                                break 
                         
                                                 
                          for t2 in reversed( range(0 ,j ) ) :                                                                              
                            if(Result[t2] == '0'):
                                p_o = j-t2                               
                                break

                            elif(t2 == 0 and Result[0] != '0' and Result[1] != '0' ):
                                p_o = 0
                                break 

                          g = 0
                          for ad in range(p_o, j) :
                              if(g < C[ad]):
                                g = ad
                                

                          Result[j] = operation(i ,Result[g],list[j])
                          p.append(j)
                           
                          for l in range(len(k)):
                              if(l == len(p)-1 ):
                                 k[l] = p[-1]

                          sum = 0
                          for v in range(len(C)):
                                if(k[v] != '0'):
                                  C[k[v]] = sum  
                                  sum = sum+1
                                                         
                          s = j



                    elif Result[j-1] == '0' and Result[j+1] != '0':
                        
                        if(j != Rm-2):                        
                            if(Result[j-1] == '0' and Result[j+1] != '0' and Result[j+2] == '0'):
                                Result[j] = operation(i , list[j] , Result[j+1])
                                p.append(j)                               
                                for l in range(len(k)):
                                   if(l == len(p)-1 ):
                                    k[l] = p[-1]

                                sum = 0
                                for v in range(len(C)):
                                    if(k[v] != '0'):
                                        C[k[v]] = sum  
                                        sum = sum+1
                                                                               
                                s = j
                                break


                        for m2 in range(j+1 , Rm):
                            if(Result[m2] == '0'):
                                p_o = m2                                                       
                                break

                            elif(m2 == Rm-1 and Result[Rm-1] != '0' and Result[Rm-2] != '0' ):
                                p_o = Rm                                                                                      
                                break
                                                                                                             
                        we = 0   
                        we = C[p_o-1] + 1                         
                        Result[j] = operation(i ,list[j], Result[we] )
                        p.append(j)
            
                        for l in range(len(k)):
                            if(l == len(p)-1 ):
                                k[l] = p[-1]

                        sum = 0
                        for v in range(len(C)):
                            if(k[v] != '0'):
                              C[k[v]] = sum  
                              sum = sum+1

                        s = j                                      



                    elif Result[j-1] != '0' and Result[j+1] != '0':

                        if(j != 1 or j != Rm-2): 
                            if(Result[j-1] != '0' and Result[j-2] == '0'  and Result[j+1] != '0' and Result[j+2] == '0'  ):
                                Result[j] = operation(i , Result[j-1] , Result[j+1])
                                p.append(j)

                                for l in range(len(k)):
                                    if(l == len(p)-1 ):
                                        k[l] = p[-1]                                                                      
                                sum = 0
                                for v in range(len(C)):
                                    if(k[v] != '0'):
                                        C[k[v]] = sum  
                                        sum = sum+1
                                        
                                s = j
                                break 

                        for w3 in reversed( range(0 , j) ) :
                            if(Result[w3] == '0'):                                                         
                                p_o1 = j-w3                                                      
                                break

                            elif(w3 == 0 and Result[0] != '0'  and Result[1] != '0'):
                                p_o1 = 0
                                break  

                        g1 = 0
                        for e4 in range(p_o1, j) :
                            if(g1 < C[e4]):
                                g1 = e4
                                
                        for r4 in range(j+1 , Rm):
                            if(Result[r4] == '0'):
                                p_o2 = r4                                                          
                                break

                            elif(r4 == Rm-1 and Result[Rm-1] != '0' and Result[Rm-2] != '0' ):
                                p_o2 = Rm                               
                                break  

                        g2 = 0
                        for y2 in range(j+1, p_o2):
                            if(g2 < C[y2]):
                                g2 = y2
                                
                                
                        Result[j] = operation(i ,Result[ g2 ] , Result[g1])
                        p.append(j)
    
                        for l in range(len(k)):
                            if(l == len(p)-1 ):
                                k[l] = p[-1]    

                        sum = 0
                        for v in range(len(C)):
                            if(k[v] != '0'):
                              C[k[v]] = sum  
                              sum = sum+1

                        s = j                    


# Section 3

            for x in range(1):

                if (j == Rm-1):
                                                          
                    if(Result[j-1] == '0'):
                        Result[j] = operation(i , list[j] , list[j+1])
                        p.append(j)
    

                        for l in range(len(k)):
                            if(l == len(p)-1 ):
                                k[l] = p[-1]                    
                       
                        s = j                            
                        sum = 0
                        for v in range(len(C)):
                            if(k[v] != '0'):
                              C[k[v]] = sum  
                              sum = sum+1



                    elif Result[j-1] != '0':

                        if(Result[j-1] != '0' and Result[j-2] == '0' ):
                            Result[j] = operation(i , Result[j-1] , list[j+1])
                            p.append(j)
                            for l in range(len(k)):
                                if(l == len(p)-1 ):
                                    k[l] = p[-1]

                            sum = 0
                            for v in range(len(C)):
                                if(k[v] != '0'):
                                    C[k[v]] = sum  
                                    sum = sum+1
                                 
                            print(Result,"\n")
                            s = j
                            break 
                                        
                        for u5 in reversed( range(0 , j+1) ):                            
                            if(Result[u5] == '0'):                              
                                p_o = j-u5                                                          
                                break

                            elif(u5 == 0 and Result[0] != '0' and Result[1] != '0'):
                                p_o = 0
                                break

                        g = 0
                        for he in range(p_o, j+1) :                           
                            if(g < C[he]):                                     
                                g = he
                                 
                        Result[j] = operation(i ,Result[g],list[j+1])
                        p.append(j)                                 
                        s = j    

                        for l in range(len(k)):
                            if(l == len(p)-1 ):
                                k[l] = p[-1]

                        sum = 0
                        for v in range(len(C)):
                            if(k[v] != '0'):
                              C[k[v]] = sum  
                              sum = sum+1

 
print("Result = " ,Result , "\n") 
print("Sequence of Calculation = " , k , "\n")  
ans = Result[s] 

for i in range(n):
    string = "{}  {} "
    print( string.format(list[i] , operator[i]) , end="")

print(" " , ans , "\n")
