#Create an empty array called left
left = []

#Create variable to store middle digits
middle = None

#Carry to store whether a 1 needs to be added to the outside of the number
carry = None

#Function to get the left half of the number
def getLeft(i):
    global left

    #global middle
    global middle

    for x in i[: len(i)//2]:
        left.append(int(x))

    #Check if even number of digits
    if len(i) % 2 == 0:

        # If so make Middle = None
        middle =  None
    else:
        #store the middle number in middle
        middle = i[len(i)//2]





#Create the palindrome
def makePal():

    global left

    #Global middle
    global middle


    #if middle == None just reverse left and add on
    if middle == None:
        l = left +  list(reversed(left))
    else:
        #else add middle into the middle
        l = left +  [middle] + list(reversed(left))


    return int("".join(str(x) for x in l))


#Function to create the next palindrome
def nextPal():
    global left

    #global middle
    global middle

    #if middle == None
    if middle == None:

        #We need change this to loop through each char in left

        carry()

    else:


        #Check whether middle is a 9
        if middle == "9":
            #If it is change to 0 and check next number in left
            middle = "0"

            carry()

        else:
            #else add one to middle
            middle = int(middle) + 1


def carry():

    #Global variables
    global carry
    global left
    global middle


    for pointer in range(len(left)-1, -1, -1):


        #If the character is a 9
        if left[pointer] == 9:

            #Make it a 0
            left[pointer] = 0
            #Add carry = True
            carry = True

        #else Add one to it
        else:
            left[pointer] = left[pointer] + 1
            #Add Carry = False
            carry = False

            #break out of loop
            break

    #if carry and middle is none
    if carry and middle == None:

        #Set middle to 0
        middle ="0"

        #set left[0] to 1
        left[0] = 1


    #if carry and middle is not none
    elif carry and middle != None:

        #set left[0] to 1
        left = [1] + left


        #set middle to none
        middle = None






strUserInput = input("Please enter a number: ")
intUserInput = int(strUserInput)
getLeft(strUserInput)
pal = makePal()

if pal > intUserInput:
    print(pal)
else:
    print("Look for the next pal")
    nextPal()
    pal = makePal ()
    print(pal)


