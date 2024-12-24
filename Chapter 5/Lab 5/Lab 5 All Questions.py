#Lab 5 All Questions.py
#This program will print the outputs of all discussion questions (1-3) and the programming exercise (#4) for lab 5!
#by Awais Razaque 9/22/23

print ()
print ("Welcome to this program!\nThis program will print the outputs of all discussion questions (1-3) and the programming exercise (#4) for lab 5!")
print ()
print ("Discussion Questions:")
print ()
print ("Question 1:")

#initial statements
s1 = "spam"
s2 = "ni!"
print ("The Knights who say, " + s2)
print (3 * s1 + 2 * s2)
print (s1 [1])
print (s1 [1:3])
print (s1 [2] + s2 [:2])
print (s1 + s2 [-1])
print (s1.upper())
print (s2.upper().ljust(4) * 3)
print()
print("Question 2:")
print (s2 [0:2].upper())
print (s2 + s1 + s2)
print (s1 [0].upper() + s1[1:4] + " " + s2[0].upper() + s2[1:3] + " " + s1 [0].upper() + s1[1:4] + " " + s2[0].upper() + s2[1:3] + " " + s1 [0].upper() + s1[1:4] + " " + s2[0].upper() + s2[1:3])
print (s1)
print ("[" + s1[0:2] + "," + s1[-1] + "]")
print (s1[0:2] + s1[-1])
print()
print ("Question 3:")

for ch in "aardvark":
    print (ch)
print()

for w in "Now is the winter of our discontent...".split():
    print (w)
print()

for w in "Mississippi".split("i"):
    print (w, end=" ")
print()

msg = ""
for s in "secret".split("e"):
    msg = msg + s
print(msg)
print()

msg = ""
for ch in "secret":
    msg = msg + chr(ord(ch)+1)
print (msg)
print()

print("Programming Exercise #4:")
userinput = input("Please enter an input string like 'random access memory' that you want the acronym for: " )
print ()
print ("The acronym for your phrase is:")
for i in userinput.split():
    print (i[0].upper(), end="")

print ()
print ()
print ("Thank you for using this program.")
input ("Press <Enter> to end this program!")
