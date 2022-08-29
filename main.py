#import statements
import os
import time
import math
import turtle
EXITCODE = "xxx"
proceed = ""
#functions go here
#Function 1: main_menu was created by Thomas Gardner on the 28/07/2022 to greet the user and inform them of the purpose of this program
def main_menu():
  #clear screen
  os.system("clear")
  #introduce user to the program and allow them to continue when ready
  proceed = input("Welcome to Triangle Calculator V1.0! \n\nThis calculator was designed to make your trigonometry homework a breeze!\n\nPress <enter> to continue:\n ")
  if proceed == EXITCODE:
    exit_code()
  #clear screen
  os.system('clear')
  #exit function
  return
#get input for lengths
def input_length(known_hypotenuse, lengthF):
  #set up loop and exit code
  while True:
    #set up variables
    error = "This is not a valid length. Please enter a real number greater than 0.\n\nPress <enter> to proceed:\n"
    #get length input
    length = input("Please enter the length of a side of your triangle:\n")
    if length == EXITCODE:
      exit_code()
    os.system("clear")
    try:
      rounded_length = round(float(length), 3)
      #check that length is valid
      if rounded_length >= lengthF and known_hypotenuse == True:
        proceed = input("This length is greater than the length you have named your hypotenuse. This is not a possible triangle, your hypotenuse must be the longest length.\n")
        if proceed == EXITCODE:
          exit_code()
        os.system("clear")
      elif rounded_length > 0:
        return rounded_length
      #if length is invalid, print error message
      else:
        proceed = input(error)
        if proceed == EXITCODE:
          exit_code()
        #clear screen
        os.system('clear')
    #if the user entered a value that wasn't a number
    except ValueError:
      #print error message
      proceed = input(error)
      if proceed == EXITCODE:
        exit_code()
      #clear screen
      os.system("clear")
#find out if the input length is the hypotenuse
def is_hypotenuse(length):
  #set up error message
  error = "Invalid input. please input 'y', 'n', or 'h'."
  #loop, set up exit code
  while True:
    #Ask the user if their value is the hypotenuse, or if they know what a hypotenuse is
    input_is_hypotenuse = input("Is the value {} the hypotenuse?\n\nIf you don't know what a hypotenuse is, enter 'h':\n".format(length)).lower()
    if input_is_hypotenuse == EXITCODE:
      exit_code()
    os.system("clear")
    #If the user doesn't know what a hypotenuse is, inform them
    if input_is_hypotenuse == "h" or input_is_hypotenuse == "help":
      print("A hypotenuse is the longest side of a right angled triangle. It is also the side that does not at any point come into contact with the right angle. See the illustration above.\n")
      proceed = input("Once you understand this, press <enter> to continue:\n")
      if proceed == EXITCODE:
        exit_code()
      os.system("clear")
      continue
    #if the length is the hypotenuse return True
    elif input_is_hypotenuse == "y" or input_is_hypotenuse == "yes":
      os.system("clear")
      return True
    #If the length is not the hypotenuse return False
    elif input_is_hypotenuse == "n" or input_is_hypotenuse == "no":
      os.system("clear")
      return False
    #If the user inputs an invalid statement print error message
    else:
      proceed = input(error)
      if proceed == EXITCODE:
        exit_code()
      os.system("clear")
#get input for angles
def input_angle(proceed):
  #Set up loop and exit code
  while proceed != 'xxx':
    #Set up variables and error message
    angle = 0
    error = "This is not a valid angle. Please enter a real number greater than 0° and less than 90°\n\nPress <enter> to proceed:\n"
    #get an input for the angle in degrees
    try:
      angle = round(float(input("Please enter the value of an angle in degrees:\n")), 3)
      #check the input angle is valid and return it
      if angle > 0 and angle < 90:
        return angle
        #If the angle is invalid print error message
      else:
        proceed = input(error)
        if proceed == EXITCODE:
          exit_code()
        #clear screen
        os.system("clear")
    #if the user inputs an invalid value
    except ValueError:
      #Check if the input value is the exit code
      if angle == EXITCODE:
        break
      #print error message
      proceed = input(error)
      if proceed == EXITCODE:
        exit_code()
      #Clear screen
      os.system("clear")
#Check angle relation to length
def angle_checker(angle, length):
  #Set up loop and exit code
  while proceed != EXITCODE:
    #ask the user if the angle is the adjacent; if it is touching the one known length
    is_adjacent = input("Is the angle {}° touching the length {}?:\n ".format(angle, length)).lower()
    if is_adjacent == EXITCODE:
      exit_code()
    os.system("clear")
    #If the length is the adjacent, inform user and return "a"
    if is_adjacent == "yes" or is_adjacent == "y":
      print("This angle is the adjacent to the length {}".format(length))
      return "a"
    #If the length is not the adjacent (the opposite), inform user and return "o"
    elif is_adjacent == "no" or is_adjacent == "n":
      print("This angle is the opposite to the length {}".format(length))
      return "o"
    #if the user enters an invalid value, print error message
    else:
      proceed = input("Invalid input. Please enter yes (y) or no (n)\n\nPress <enter> to proceed:\n")
      if proceed == EXITCODE:
        exit_code()
      os.system("clear")
def sin_tan(angleA, angleB, angleC, lengthD, lengthE, lengthF):
  angleB = (math.pi / 2) - angleA
  lengthF = round(lengthD / math.sin(angleA), 3)
  lengthE = round(lengthD / math.tan(angleA), 3)
  return angleA, angleB, angleC, lengthD, lengthE, lengthF
def cos_tan(angleA, angleB, angleC, lengthD, lengthE, lengthF):
  angleA = (math.pi / 2) - angleB
  lengthF = round(lengthD / math.cos(angleB), 3)
  lengthE = round(lengthD * math.tan(angleB), 3)
  return angleA, angleB, angleC, lengthD, lengthE, lengthF
def sin_cos(angleA, angleB, angleC, lengthD, lengthE, lengthF):
  angleB = (math.pi / 2) - angleA
  lengthD = round(lengthF * math.sin(angleA), 3)
  lengthE = round(lengthF * math.cos(angleA), 3)
  return angleA, angleB, angleC, lengthD, lengthE, lengthF
def cot_sin(angleA, angleB, angleC, lengthD, lengthE, lengthF):
  angleA = round(math.atan(lengthD / lengthE), 3)
  angleB = (math.pi / 2) - angleA
  lengthF = round(lengthD / math.sin(angleA), 3)
  return angleA, angleB, angleC, lengthD, lengthE, lengthF
def sec_sin(angleA, angleB, angleC, lengthD, lengthE, lengthF):
  angleA = round(math.acos(lengthD / lengthF), 3)
  angleB = (math.pi / 2) - angleA
  lengthE = round(lengthF * math.sin(angleA), 3)
  return angleA, angleB, angleC, lengthD, lengthE, lengthF
#*******Main Routine********
#Set up variables
def exit_code():
  print("Exit code has been entered. Session ceasing\nHistory:\n")
  history = open("history.txt", "r")
  history_items = history.readlines()
  history_lines = len(history_items)
  history.close()
  history_number = 0
  if history_lines == 0:
    print("No history found")
  else:
    for i in history_items:
      print(history_items[history_number])
      history_number += 1
  input()
  main()
    
history = open("history.txt", "w")
history.write("")
history.close()
#Create loop and establish exit code
def main():
  #Reset Variables
  #if only lengthD is known, this is the opposite
  angleA = 0
  #If only lengthD is known, this is the adjacent
  angleB = 0
  #This is the right angle (in radians)
  angleC = math.pi / 2
  #This is the first length
  lengthD = 0
  #This is the second length if two non-hypotenuse values are input
  lengthE = 0
  #This is the hypotenuse
  lengthF = 0
  known_hypotenuse = False
  more_lengths = True
  known_lengths = 0
  known_angles = 0
  temp_length = 0
  temp_angle = 0
  #This is the trignonmetric function to apply
  function = ""
  #Main Menu function
  main_menu()
  #Get inputs for all known lengths
  while more_lengths == True and known_lengths < 2:
    #input length function assigned to temporary variable
    temp_length = input_length(known_hypotenuse, lengthF)
    #work out which variable to assign length to
    if known_hypotenuse == False:
      known_hypotenuse = is_hypotenuse(temp_length)
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
    #reset temporary length
    temp_length = 0
    #increase the number of known lengths
    known_lengths += 1
    #if the user doesn't have enough lengths to derive the whole triangle
    if known_lengths < 2:
      #establish loop
      break_loop = False
      while break_loop != True:
        #ask user if they have more known lengths
        more_lengths_input = input("Do you have more lengths to input?:\n").lower()
        if more_lengths_input == EXITCODE:
          exit_code()
        os.system("clear")
        #If the user does have more lengths to input, exit loop and continue
        if more_lengths_input == "y" or more_lengths_input == "yes":
          break_loop = True
        #If the user has no more lengths to input, exit loop and get an angle
        elif more_lengths_input == "n" or more_lengths_input == "no":
          more_lengths = False
          break_loop = True
        #if the user inputs an invalid value, print error and retry
        else:
          proceed = input("Invalid input. Please try again.")
          if proceed == EXITCODE:
            exit_code()
          os.system("clear")
    #If the user has enough lengths to derive the entire triangle, continue to trigonometric functions
    else:
      print("with the given values the entire triangle can now be described. Thankyou for your input.")
      #inform user of the input lengths
  proceed = input("Lengths: \nFirst length: {}\nSecond length: {}\nHypotenuse length: {}\n\nPress <enter> to continue".format(lengthD, lengthE, lengthF))
  if proceed == EXITCODE:
    exit_code()
  os.system("clear")
  #Get inputs for all known angles if needed
  if known_lengths < 2:
    #Loop, inform user that they don't have enough lengths to derive the entire triangle, get an angle
    while known_angles < 1:
      print("To calculate the dimensions of the right angled triangle with only one known length, you must input 1 angle that is not the 90° angle to proceed.")
      temp_angle = input_angle(proceed)
      #if the length the user has isn't the hypotenuse, work out if the angle is opposite or adjacent
      if known_hypotenuse == False:
        angle_relation = angle_checker(temp_angle, lengthD)
        #Decide on trigonometric functions to apply
        if angle_relation == "o":
          #if the user has the opposite angle, function is sin then tan
          angleA = math.radians(temp_angle)
          function = "sin, tan"
        elif angle_relation == "a":
          #if the user has the adjacent angle, function is cos then tan
          angleB = math.radians(temp_angle)
          function = "cos, tan"
      else:
        #If the user has the hypotenuse, function is sin then cos
        angleA = math.radians(temp_angle)
        function = "sin, cos"
      #increase known angles by one
      known_angles += 1
  #if the user has two lengths, derive functions
  else:
    if lengthD != 0 and lengthE != 0:
      #if the user has no hypotenuse, function is cot then sin
      function = "cot, sin"
    elif lengthD != 0 and lengthF != 0:
      #if the user has the hypotenuse, function is sec then sin
      function = "sec, sin"
  #possible functions: sin, tan; cos, tan; sin, cos; cot, sin; sec, sin
  #Calculate 3 unknowns
  #sin_tan
  if function == "sin, tan":
    angleA, angleB, angleC, lengthD, lengthE, lengthF = sin_tan(angleA, angleB, angleC, lengthD, lengthE, lengthF)
  #cos_tan
  elif function == "cos, tan":
    angleA, angleB, angleC, lengthD, lengthE, lengthF = cos_tan(angleA, angleB, angleC, lengthD, lengthE, lengthF)
  #sin_cos
  elif function == "sin, cos":
    angleA, angleB, angleC, lengthD, lengthE, lengthF = sin_cos(angleA, angleB, angleC, lengthD, lengthE, lengthF)
  #cot_sin
  elif function == "cot, sin":
    angleA, angleB, angleC, lengthD, lengthE, lengthF = cot_sin(angleA, angleB, angleC, lengthD, lengthE, lengthF)
  #sec_sin
  elif function == "sec, sin":
    angleA, angleB, angleC, lengthD, lengthE, lengthF = sec_sin(angleA, angleB, angleC, lengthD, lengthE, lengthF)
  
  #Return triangle dimensions to user
  proceed = input("Values: [{}, {}, {}, {}, {}, {}, Functions: {}]\n".format(round(math.degrees(angleA), 2), round(math.degrees(angleB), 2), round(math.degrees(angleC), 2), lengthD, lengthE, lengthF, function))
  if proceed == EXITCODE:
    exit_code()
  os.system("clear")
  #Save triangle dimensions to text document
  history = open("history.txt", "a")
  history.write("Angles: {}, {}. Right Angle: {}. Lengths: {}, {}. Hypotenuse: {}. Functions: {}\n".format(round(math.degrees(angleA), 2), round(math.degrees(angleB), 2), round(math.degrees(angleC), 2), lengthD, lengthE, lengthF, function))
  history.close()
  #End loop
main()