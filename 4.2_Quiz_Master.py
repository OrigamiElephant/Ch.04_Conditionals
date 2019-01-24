'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score = 0
q = 0
A = input("1.What was kiddo called, at first, in the movie Kill Bill? ")
if A == "The Bride":
    print("Correct")
    score = score + 1
    q = q + 1
else:
    print("Incorrect. Answer: The Bride")
    q = q + 1
print()
B = input("2.How many people from her old team did kiddo kill? ")
if B == "4":
    print("Correct")
    score = score + 1
    q = q + 1
elif B == "5":
    print("Kiddo didn't kill Buck. Answer: 4")
    q = q + 1
else:
    print("Incorrect. Answer: 4")
    q = q + 1
print()
print("3.What was kiddo's codename from her old team")
print("A:Cottonmouth")
print("B:Copperhead")
print("C:Black Mamba")
print("D:Rattlesnake")
C = input("Answer:")
if C == "C" or C ==  "c":
    print("Correct")
    score = score + 1
    q = q + 1
else:
    print("incorrect. Answer: C")
    q = q + 1
print()
print("What was the name of the mafia group that Kiddo single handedly took down?")
print("Final Score:",score,"/", q)
print((score * 100) // q,"%")