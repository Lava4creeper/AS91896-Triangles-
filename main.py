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
#get input for lengths
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
#find out if the input length is the hypotenuse
def is_hypotenuse(proceed, length):
  error = "Invalid input. please input 'y', 'n', or 'h'."
  while proceed != "xxx":
    input_is_hypotenuse = input("Is the value {} the hypotenuse?\n\nIf you don't know what a hypotenuse is, enter 'h'".format(length)).lower()
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
      print(error)
#get input for angles
def input_angle(proceed):
  while proceed != 'xxx':
    angle = 0
    error = "This is not a valid angle. Please enter a real number greater than 0° and less than 90°\n\nPress <enter> to proceed"
    try:
      angle = float(input("Please enter the value of an angle in degrees"))
      if angle > 0 and angle < 90:
        return angle
      else:
        proceed = input(error)
        os.system("clear")
    except ValueError:
      if angle == EXITCODE:
        break
      proceed = input(error)
      os.system("clear")
#Check angle relation to length
def angle_checker(proceed, angle, length):
  while proceed != "xxx":
    is_adjacent = input("Is the angle {}° touching the length {}? ".format(angle, length)).lower()
    if is_adjacent == "yes" or is_adjacent == "y":
      print("This angle is the adjacent to the length {}".format(length))
      return "a"
    elif is_adjacent == "no" or is_adjacent == "n":
      print("This angle is the opposite to the length {}".format(length))
      return "o"
    else:
      proceed = input("Invalid input. Please enter yes (y) or no (n)\n\nPress <enter> to proceed")
#*******Main Routine********
proceed = ""
EXITCODE = "xxx"
#Create loop
while proceed != EXITCODE:
  #Reset Variables
  #if only lengthD is known, this is the opposite
  angleA = 0
  #If only lengthD is known, this is the adjacent
  angleB = 0
  #This is the right angle
  angleC = math.pi / 2
  lengthD = 0
  lengthE = 0
  known_hypotenuse = False
  more_lengths = True
  known_lengths = 0
  known_angles = 0
  temp_length = 0
  #This is the hypotenuse
  lengthF = 0
  #Main Menu
  proceed = main_menu(proceed)
  #Get inputs for all known lengths
  while more_lengths == True and known_lengths < 2:
    temp_length = input_length(proceed)
    if known_hypotenuse == False:
      known_hypotenuse = is_hypotenuse(proceed, temp_length)
      if known_hypotenuse == True:
        lengthF = temp_length
      elif known_hypotenuse == False:
        if lengthD == 0:
          lengthD = temp_length 
        elif lengthE == 0:
          lengthE = temp_length 
      temp_length = 0
    else:
      if lengthD == 0:
        lengthD = temp_length
      elif lengthE == 0:
        lengthE = temp_length
    temp_length = 0
    known_lengths += 1
    if known_lengths < 2:
      break_loop = False
      while break_loop != True:
        more_lengths_input = input("Do you have more lengths to input?").lower()
        if more_lengths_input == "y" or more_lengths_input == "yes":
          break_loop = True
        elif more_lengths_input == "n" or more_lengths_input == "no":
          break_Loop = True
          more_lengths = False
        else:
          print("Invalid input. Please try again.")
    else:
      print("with the given values the entire triangle can now be described. Thankyou for your input.")
  print("Lengths: [{}, {}, {}]".format(lengthD, lengthE, lengthF))
  input()
  #Get inputs for all known angles if needed
  if known_lengths < 2:
    while known_angles < 1:
      print("To calculate the dimensions of the right angled triangle with only one known length, you must input 1 angle that is not the 90° angle to proceed.")
      temp_angle = input_angle(proceed)
      if known_hypotenuse == False:
        angle_relation = angle_checker(proceed, temp_angle, lengthD)
        input(angle_relation)
        
      
  #Decide on trigonometric functions to apply
  
  #Calculate 3 unknowns
  
  #Return triangle dimensions to user
  
  #Save triangle dimensions to text document
  
  #End loop
  
  #Return calculation history
print("Program ceased with exit code 0")