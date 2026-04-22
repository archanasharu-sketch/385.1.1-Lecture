# Using import statement to import a module
import sys
import math # packages give us access to prebuilt functions
from math import pi # importing specific functions from a module
import os

print('Python version:', sys.version)
print(math.sqrt(16))
print(math.pi)
print(os.listdir())
print(os.getcwd())
# print(os.listdir('/Volumes/ExtHD'))
print(os.environ)
print(os.name)
print(sys.path)
print(sys.modules)
for path in sys.path:
    print(path)

# # Single line/block comments
# print('Hello, World!') # inline comment


# """
# For Multi line comments use EITHER three single or three double quotes
# """

print('Per Scholas is Unlocking Potential and Changing the Face of Tech')

print(10+90)

print(300.5 + 0.5)

# # sep= attribute/parameter puts a separator of choice betwenn the comma separated value
print (12, 24, -2, sep=':')
print('but', 'not', 'including', sep='**')
print('but', 'not', 'including', sep='')

# # Saving response into variable
name = input('What is your name?')
print('Hello', name, ' what is up?')

# # Get numbers from the user
mb = input('Enter your mobile num:')
hp = input('Enter your home number:')

print('Mobile number is ', mb)
print('Home number is ', hp)