#BIO 2022 Question 1
newString = []

#Read in a sting with 1 to 10 characters inclusive
cipherText = input("Please enter your encrypted text: ")

while len(cipherText)<1 or len(cipherText)> 10:
    cipherText = input("Please enter your encrypted text: ")

cipherText = cipherText.upper()

#Convert string into numbers by  converting to ASCii and subtracting 64 and save into a list
for i in cipherText:
    newString.append(ord(i)-64)


#Save the first letter
decryptedText = cipherText[0]

#Loop through each letter in the list and subtract the value of the letter before from the current letter
for x in range(1,len(newString)):

    #Create a new string by subtracting the first number from the 2nd
    newLetter = newString[x] - newString[x-1]
    #What if the new letter number is less than 0....
    if newLetter <=0:
        newLetter = 26 + newLetter

    #Add 64 and convert to char
    newLetter = chr(newLetter + 64)

    decryptedText = decryptedText + newLetter


#print the new string
print(decryptedText)



