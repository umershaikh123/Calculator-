# This program needs the following files to run
# M_Simple_2N
# M_Simple_3N
# M_Simple_4N
# M_Simple_5N
# Scientific_2N
# Scientific_3N
# Scientific_4N
# Scientific_5N
# Infinite_Simple_calculation
# Infinite_Scientific_calculation


print("\n", "Hello and Welcome to the Calculator program.")

repeat = True

while(repeat == True):
    print("\n", "Press 1 to perform simple calculation ")
    print("\n", "Press 2 to perform Scientific calculation ")
    print("\n", "Press any other button to quit the program ")
    response = input(" Response : ")
 
    if(response == '1'):
          print('\n',"Type how many numbers you want to perform calculations on simultaneously.")
          print(" Select From 2 to infinity")
          number = int(input(" Input : "))

          if(number == 2):
               
               import M_Simple_2N

               print("\n","Do you want to continue the program ?")
               print(" Type 'yes' to repeat or 'no' to stop the program")
               ans = input(" Input : ")
               if(ans == 'yes'):
                    repeat == True
                    continue
               else:
                    repeat == False
                    break

          elif(number == 3):
               import M_Simple_3N
               print("\n","Do you want to continue the program ?")
               print(" Type 'yes' to repeat or 'no' to stop the program")
               ans = input(" Input : ")
               if(ans == 'yes'):
                    repeat == True
                    continue
               else:
                    repeat == False
                    break


          elif(number == 4):
               import M_Simple_4N
               print("\n","Do you want to continue the program ?")
               print(" Type 'yes' to repeat or 'no' to stop the program")
               ans = input(" Input : ")
               if(ans == 'yes'):
                    repeat == True
                    continue
               else:
                    repeat == False
                    break


          elif(number == 5):
               import M_Simple_5N
               print("\n","Do you want to continue the program ?")
               print(" Type 'yes' to repeat or 'no' to stop the program")
               ans = input(" Input : ")
               if(ans == 'yes'):
                    repeat == True
                    continue
               else:
                    repeat == False
                    break


          elif(number > 5):
               import Infinite_Simple_calculation
               print("\n","Do you want to continue the program ?")
               print(" Type 'yes' to repeat or 'no' to stop the program")
               ans = input(" Input : ")
               if(ans == 'yes'):
                    repeat == True
                    continue
               else:
                    repeat == False
                    break              


          else:
               print("\n" , "Error , Please type the correct value")             
               continue

    elif(response == '2'):
          print("\n","Type how many numbers you want to perform calculations on simultaneously.")
          print(" From 2 to infinity")
          number = int(input(" Input : "))

          if(number == 2):
               import Scientific_2N
               print("\n","Do you want to continue the program ?")
               print(" Type 'yes' to repeat or 'no' to stop the program")
               ans = input(" Input : ")
               if(ans == 'yes'):
                    repeat == True
                    continue
               else:
                    repeat == False
                    break


          elif(number == 3):
               import Scientific_3N
               print("\n","Do you want to continue the program ?")
               print(" Type 'yes' to repeat or 'no' to stop the program")
               ans = input(" Input : ")
               if(ans == 'yes'):
                    repeat == True
                    continue
               else:
                    repeat == False
                    break


          elif(number == 4):
               import Scientific_4N
               print("\n","Do you want to continue the program ?")
               print(" Type 'yes' to repeat or 'no' to stop the program")
               ans = input(" Input : ")
               if(ans == 'yes'):
                    repeat == True
                    continue
               else:
                    repeat == False
                    break


          elif(number == 5):
               import Scientific_5N
               print("\n","Do you want to continue the program ?")
               print(" Type 'yes' to repeat or 'no' to stop the program")
               ans = input(" Input : ")
               if(ans == 'yes'):
                    repeat == True
                    continue
               else:
                    repeat == False
                    break     

          elif(number > 5):
               import Infinite_Scientific_calculation
               print("\n","Do you want to continue the program ?")
               print(" Type 'yes' to repeat or 'no' to stop the program")
               ans = input(" Input : ")
               if(ans == 'yes'):
                    repeat == True
                    continue
               else:
                    repeat == False
                    break               

          else:
                print("Error , Please type the correct value")
                continue

    if(response != '1' or response != '2'):
        print('\n'," Quitting the program")
        repeat == False
        break              


print("\n" , "Program has ended.")              
