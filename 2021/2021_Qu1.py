"""
A pat is:

Single letter
OR a string that can be split into left and right string of at
least 1 letter

All the letters in the left string are later in the alphabet
than ALL the letters in the right string

Each string is the reverse of a pat i.e.



EXAMPLE:
BA is a pat because it splits into B and A which are single letters and therefore pats
B is after A

DEC is a pat as it splits into DE and C.  DE are both after C
in the alphabet
if we reverse DE it becomes ED which is a pat

CEDAB splits into CED and AB.  CED is after AB.
AB reversed becomes BA and B is after A in the alphabet
CED is a pat - see above.


INPUTS:
Two strings on one line e.g. DE C
strings are between 1 and 6 characters long

OUTPUT:
Three lines of YES / NO
Is S1 a pat?
Is S2 a pat?
Is S1S2 a pat?


Single letters are automatically pats
We don't need to prove that every way of splitting up the string follows
the rules - just one instance.

Start small
Is it one letter - it is a pat

Is it two letters?
        Split is the first letter after the second in the alphabet?

Is it three letters?
        split it into one and two
        Send the two to the twoLetter sub

Is it four letters
1 and 3
3 and 1
2 and 2

Is it five letters
1 and 4
4 and 1
2 and 3
3 and 2

6 letters
3 and 3
2 and 4
4 and 2
1 and 5
5 and 1

#Start be looking at first string
#Then second
#Then both
"""

#Reverse a string
def reverseString (myString):
    b = list(myString)
    b.reverse()
    c = "".join(b)
    return c


#Two  letters
def twoLettersCheck (x):
        if x[0] > x[1]:
                return "YES"
        else:
                return "NO"

#Three letters
def threeLetterCheck (x):
        #Loop to
        #Split into 1 and 2
        #Split into 2 and 1

        for i in range(1,len(x)):
            if min(x[:i])>max(x[i:]):
                #If the left string is 2 characters
                if len(x[:i])==2:
                    x = reverseString (x[:i])
                    return twoLettersCheck(x)
                #Else the right string must be two characters
                else:
                    x = reverseString (x[i:])
                    return twoLettersCheck(x)
        return "NO"


def fourLetterCheck (x):
        #Loop to
        #Split into 1 and 3
        #Split into 2 and 2
        #Split into 3 and 1

    patFlag = "NO"
    for i in range(1,len(x)):
        #If the left string is after the right string in the alphabet
        if min(x[:i])>max(x[i:]):

            if len(x[:i]) == 1:
                    #Split into 1 and 3

                    #Reverse the three characters
                    z = reverseString (x[i:])

                    if threeLetterCheck(z)=="YES":
                        return "YES"
            elif len(x[:i])==2:
                #Split into 2 and 2

                #Reverse the characters
                z = reverseString (x[:i])#Left string
                y = reverseString (x[i:])#Right string

                if twoLettersCheck(z) == "YES":
                    if twoLettersCheck(y)=="YES":
                        return "YES"

            elif len(x[:i]) == 3:
                    #Split into 3 and 1

                    #Reverse the three characters
                    z = reverseString (x[:i])

                    if threeLetterCheck(z)=="YES":
                        return "YES"

    return "NO"

def fiveLetterCheck (x):
    #split 1 and 4
    #split 2 and 3
    #split 3 and 2
    #split 4 and 1

    patFlag = "NO"
    for i in range(1,len(x)):

        #Is the left string is after the right string in the alphabet
        if min(x[:i])>max(x[i:]):

            if len(x[:i])==1:
                #split 1 and 4

                #Reverse characters
                z = reverseString (x[i:])

                if fourLetterCheck(z) == "YES":
                    return "YES"
            elif len(x[:i]) == 2:
                #split 2 and 3

                #Reverse characters
                z = reverseString (x[:i])
                y = reverseString (x[i:])

                if twoLettersCheck(z) == "YES":
                    if threeLetterCheck(y) == "YES":
                        return "YES"

            elif len(x[:i]) == 3:
                #split 3 and 2

                #Reverse the three characters
                z = reverseString (x[:i])
                y = reverseString (x[i:])

                if threeLetterCheck(z)=="YES":
                    if twoLettersCheck(y)=="YES":
                        return "YES"

            elif len(x[:i])==4:
                #split 4 and 1

                #Reverse the four characters
                z = reverseString (x[:i])
                if fourLetterCheck(z) == "YES":
                    return "YES"

    return "NO"

def sixLetterCheck(x):
    #split 1 and 5
    #split 2 and 4
    #split 3 and 3
    #split 4 and 2
    #split 5 and 1
    patFlag = "NO"
    for i in range(1,len(x)):
        #Is the left string is after the right string in the alphabet
        if min(x[:i])>max(x[i:]):

            if len(x[:i])==1:
                #split 1 and 5 - check the 5

                #Reverse the characters
                z = reverseString (x[i:]) #Right string

                if fiveLetterCheck(z) == "YES":
                    return "YES"
            elif len(x[:i]) == 2:
                #split 2 and 4 - check both

                #Reverse the characters
                z = reverseString (x[:i]) #Left string
                y = reverseString (x[i:]) #Right string

                if twoLettersCheck(z) == "YES":
                    if fourLetterCheck(y) == "YES":
                        return "YES"

            elif len(x[:i]) == 3:
                #split 3 and 3

                #Reverse the characters
                z = reverseString (x[:i]) #Left string
                y = reverseString (x[i:]) #Right sring

                if threeLetterCheck(z)=="YES":
                    if threeLetterCheck(y)=="YES":
                        return "YES"
            elif len(x[:i])==4:
                #split 4 and 2

                #Reverse the characters
                z = reverseString (x[:i]) #Left string
                y = reverseString (x[i:]) #Right string


                if fourLetterCheck(z) == "YES":
                    if twoLettersCheck(y) == "YES":
                        return "YES"

            elif len(x[:i])==5:
                #split 5 and 1

                #Reverse the characters
                z = reverseString (x[:i]) #Left string
                if fiveLetterCheck(z) == "YES":
                    return "YES"

    return "NO"


myInput = input("Please enter your string: ")

if len(myInput)==1:
    print("YES")
elif len(myInput)==2:
    #Reverse the parameters as in future the letters entered will be reveresed
    print(twoLettersCheck (myInput))
elif len(myInput)==3:
    print(threeLetterCheck (myInput))
elif len(myInput)==4:
    print(fourLetterCheck(myInput))
elif len(myInput)==5:
    print(fiveLetterCheck(myInput))
elif len(myInput)==6:
    print(sixLetterCheck(myInput))














