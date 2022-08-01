#import statements
import os
import time
import math
import turtle
#functions go here
#Function 1: main_menu was created by Thomas Gardner on the 28/07/2022 to greet the user and inform them of the purpose of this program
def main_menu(proceed):
  #CLEAR SCREEN
  proceed = input("Welcome to Triangle Calculator V1.0! \n\nThis calculator was designed to make your trigonometry homework a breeze!\n\nPress <enter> to continue: ")
  os.system('clear')
  return proceed
def input_length(proceed):
  while proceed != 'xxx':
    length = 0
    error = "This is not a valid length. Please enter a real number greater than 0.\n\nPress <enter> to proceed:"
    try:
      length = float(input("Please enter the length of a side of a side of your triangle:\n"))
      if length > 0:
        return length
      else:
        proceed = input(error)
        os.system('clear')
    except ValueError:
      if length == EXITCODE:
        break
      proceed = input(error)
      os.system("clear")
def is_hypotenuse(proceed):
  while proceed != "xxx":
    input_is_hypotenuse = input("Is this value the hypotenuse?\n\nIf you don't know what a hypotenuse is, enter 'h'").lower()
    if input_is_hypotenuse == "h" or input_is_hypotenuse == "help":
      print("A hypotenuse is the longest side of a right angled triangle. It is also the side that does not at any point come into contact with the right angle. See the illustration above.\n")
      proceed = input("Once you understand this, press <enter> to continue:")
      os.system("clear")
      continue
    elif input_is_hypotenuse == "y" or input_is_hypotenuse == "yes":
      os.system("clear")
      return True
    elif input_is_hypotenuse == "n" or input_is_hypotenuse == "no":
      os.system("clear")
      return False
    else:
      print("error")
#*******Main Routine********
proceed = ""
EXITCODE = "xxx"
#Create loop
while proceed != EXITCODE:
  #Reset Variables
  angleA = 0
  angleB = 0
  #This is the right angle
  angleC = math.pi / 2
  lengthD = 0
  lengthE = 0
  known_hypotenuse = False
  more_lengths = True
  known_lengths = 0
  #This is the hypotenuse
  lengthF = 0
  #Main Menu
  proceed = main_menu(proceed)
  #Get inputs for all known lengths
  while more_lengths == True or known_lengths < 2:
    temp_length = input_length(proceed)
    if known_hypotenuse == False:
      known_hypotenuse = is_hypotenuse(proceed)
      if known_hypotenuse == True:
        lengthF = temp_length
        temp_length = 0
    
    print(temp_length)
  
  #Get inputs for all known variables if needed
  
  #Decide on trigonometric functions to apply
  
  #Calculate 3 unknowns
  
  #Return triangle dimensions to user
  
  #Save triangle dimensions to text document
  
  #End loop
  
  #Return calculation history
print("Program ceased with exit code 0")