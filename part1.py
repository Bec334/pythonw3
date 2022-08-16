
#https://www.w3resource.com/python-exercises/python-basic-exercises.php 

"""
1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
"""

#print("Twinkle, twinkle, little star, \n \t How I wonder what you are!\n \t \tUp above the world so high,\n \t \tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n \tHow I wonder what you are") 

'''2. Write a Python program to get the Python version you are using. Go to the editor
'''
# import sys 
# print(sys.version)

'''3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14'''

# import datetime
# x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(x) 

'''4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504'''

# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


'''5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.'''

# firstName = input("What is your first name?")
# lastName = input("What is your last name?")
# print (lastName, firstName)

'''6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')'''

# userNumbers = input("enter numbers seperated by space:")
# thisList = list(userNumbers.split()) 
# thisTuple = tuple(userNumbers.split())
# print(thisList)
# print(thisTuple)


'''7. Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java'''

# fileName = input("what is the file name with extension?")
# fileExt = fileName.split('.')
# print(fileExt)
# print(repr(fileExt[-1])) 
# print(fileExt[-1])



