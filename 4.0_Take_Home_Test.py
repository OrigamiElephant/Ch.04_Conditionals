'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________


  1. What is missing from this code?
     
     midichlorians = float(input("Enter midichlorian count: ")
     if midichlorians > 10000:
         print("You have serious Jedi potential")
     else:
         print("Jedi, you will never be.")
'''
# The second ")" after "("Enter midichlorian count: ")
     
'''
  2. This runs, but there is something wrong. What is it?
     
     user_input = input("R2D2 is a: ")
     print("A. Droid")
     print("B. Storm Trooper")
     if user_input.upper() == "A":
         print("Correct!")
     else:
         print("Incorrect.")
'''
# It prints the answers you choose from after the question is answered


'''
     
  3. There are two things wrong with this code that tests if x is set to a
     positive value. One prevents it from running, and the other is subtle.
     Make sure the if statement works no matter what x is set to.
     Identify both issues. 
     
     x == 4
     if x >= 0:
         print("x is positive.")
     else:
         print("x is not positive.")
 '''
 # The value "x" was not set to being equal to 4. So the equation below couldn't work
 # It has it so if x = 0 then it will be positive, but 0 is neither
'''
  4. What three things are wrong with the following code?
     
     x = input("Enter a number: ")
     if x = 3
         print("You entered 3")
 '''
 # 1. The input command doesn't have "int" anywhere, so it can't collect a number
 # 2. The if needs a collon on the end
 # 3. if x = 3, should instead be, if x == 3
 
'''
  5. There are four things wrong with this code. Identify all four issues. 
     
     answer = input("What is the name of Poe Dameron's Droid? ")
     if a = "BB8":
         print("Correct!")
         else
         print("Incorrect! It is BB8.")
'''
# The answer to the question is set to "answer" when the if statement uses "a"
# if statement should say (if a == "BB8":)
# else does not need tobe indented
# else needs a collon after it

'''
  6. This program doesn't work correctly. What is wrong?
     
     x = input("Who are the top 3 greatest Jedi?")
     if x == "Yoda" or "Luke Skywalker" or "Obi-Wan Kenobi":
         print("That is correct!")
'''
# It prints "That is correct" no matter what you type

'''
  7. Look at the code below. Write your best guess here on what it will print.
     Next, run the code and see if you are correct.
     Clearly label your guess and the actual answer.
     
     x = 5
     y = x == 6
     z = x == 5
     print("x=", x)
     print("y=", y)
     print("z=", z)
     if y:
         print("Star Wars Episodes 1,2,3 are the best!")
     if z:
         print("Star Wars Episodes 4,5,6 are the best!")
'''
# Guess: it will print: Star Wars Episodes 4,5,6 are the best!
# Answer: it printed: Star Wars Episodes 4,5,6 are the best!

'''
 8. Look at the code below. Write you best guess on what it will print.
     Next, run the code and see if you are correct. 
     
     x = 5
     y = 10
     z = 10
     print(x < y) true
     print(y < z) false
     print(x == 5) true
     print(not x == 5) false
     print(x != 5) true (Incorrect)
     print(not x != 5) false (Incorrect)
     print(x == "5") false
     print(5 == x + 0.00000000001) false
     print(x == 5 and y == 10) true
     print(x == 5 and y == 5) false
     print(x == 5 or y == 5) false (Incorrect)
'''


'''
 9. Look at the code below. Write you best guess on what it will print.
     Next, run the code and see if you are correct. (HINT: when comparing strings, ASCII codes are used. https://www.ascii-code.com/)
  
     print("3" == "3") true
     print(" 3" == "3") false
     print(3 < 4) true
     print("3" < "4") false (Incorrect)
     print("3" < 4) false
     print("<" < ">") false (Incorrect)
     print((2 == 2) == "True") false
     print((2 == 2) == True) true
     print("?"<"!") false
'''


'''
 10. What things are wrong with this section of code?
     The programmer wants to set the force sensitivity variable according to the character the user selects.
     
     print("Welcome to the Jedi Academy!")

     print("A. Jedi Master")
     print("B. Sith Lord")
     print("C. Droid")

     user_input = input("Choose a character?")

     if user_input = A:
         money = 1000
     else if user_input = B:
         money = 900
     else if user_input = C:
         money = 0
'''
# The equal signs in the if statements need to be doubled (==)
# The letters A,B, and C need quotation marks around them too make the program work
# The statement "else if" needs to be shortened to "elif"
