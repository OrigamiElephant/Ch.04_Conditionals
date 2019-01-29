'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score = 0
q = 0
A = input("1.Who was kiddo introduced as in the first Kill Bill? ")
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
    print("incorrect. Answer is: C")
    q = q + 1
print()
print("4.What was the name of the mafia group that Kiddo single handedly took down?")
print("A:Nifty Fifty")
print("B:Sublime Twenty-Nine")
print("C:Mentally Unstable Seven-Eleven")
print("D:Crazy Eighty-Eight")
D = input("Answer:")
if D == "D" or D == "d":
    print("Correct")
    score = score + 1
    q = q + 1
else:
    print("incorrect. Answer is: D")
    q = q + 1
print()
e = input("5.If Kiddo were to Kill Bill 30 times over and cut off all his limbs, how many more limbs would she have than Bills?")
if e == "90":
    print("Correct")
    score = score + 1
    q = q + 1
elif e == "120":
    print("Hint: limbs - Bills")
    q = q + 1
else:
    print("Incorrect. Answer: limbs - Bills")
    q = q +1
print()
f = input("Bonus Question: What was the technique Kiddo used to finally Kill Bill?")
if f == "five point palm exploding heart technique":
    print("Correct")
    score = score + 1
else:
    print("Sorry, Incorrect")
print("Final Score:",score,"/", q)
print((score * 100) // q,"%")
overall = (score * 100) // q
if overall < 60:
    letter = "F"
elif overall <= 62:
    letter = "D-"
elif overall <= 66:
    letter = "D"
elif overall <= 69:
    letter = "D+"
elif overall <= 72:
    letter = "C-"
elif overall <= 76:
    letter = "C"
elif overall <= 79:
    letter = "C+"
elif overall <= 82:
    letter = "B-"
elif overall <= 86:
    letter = "B"
elif overall <= 89:
    letter = "B+"
elif overall <= 92:
    letter = "A-"
elif overall <= 96:
    letter = "A"
else:
    letter = "A+"
print("Grade:",letter)
