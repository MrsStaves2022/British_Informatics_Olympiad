#BIO 2019 Question 1a

#Input a positive number up to 20 digits

numReversed = ""
strnum = input("Please enter a number: ")

#Output the smallest palendromic number that is higher than the input
#Loop upwards, incrementing the number by 1 until we find a palendromic number
#If the variables match then the number is palemdromic
while strnum != numReversed:

    #Is the number palendromic?
    #reverse the number and save to a different variable

    num = int(strnum)
    num = num + 1
    strnum = str(num)
    numReversed = strnum[::-1]

#Output the palendromic number
print(num)


#Show efficiency by testing 123456789000000000
