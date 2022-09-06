#import statements
import os
import math
EXITCODE = "xxx"
proceed = ""
#functions go here
#Function 1: main_menu was created by Thomas Gardner on the 28/07/2022 to greet the user and inform them of the purpose of this program
def main_menu():
  #clear screen
  os.system("clear")
  #introduce user to the program and allow them to continue when ready; give them options on how to proceed
  proceed = input("Welcome to Triangle Calculator V1.0! \n\nThis calculator was designed to make your trigonometry homework a breeze!\n\nWhen you're finished with your session, input {} to leave.\n\ninput (e)xplanations to read about the processes involved in calculating the dimensions of a triangle, or press <enter> to calculate your triangle:\n ".format(EXITCODE)).lower()
  #clear screen
  os.system("clear")
  #check for exit code and exit program if it's entered.
  if proceed == EXITCODE:
    exit_code()
  #if the user wanted an explanation of how the program calculates triangles, give them it
  elif proceed == "e" or proceed == "explanation" or proceed == "explanations":
    explanations()
  #otherwise, exit function
  return
#Function 2: Explanations was created by Thomas Gardner on the 4/09/2022 to explain to the user the methods used within the program
def explanations():
  #Explain necessary information to user
  proceed = input("A triangle can be completely described and its dimensions calculated from 2 inputs, so long as one of those inputs is a length.\n\nThere are three trigonometric functions that can be applied: sine, cosine or tangent. Depending on the given data, different combinations of these can be utilized to describe the whole triangle.\n\nThis can be done by taking a length and a length or an angle and applying these functions to them.\n\nThis program takes input from you, the user, on different parts of your triangles and uses this knowledge to calculate the dimensions of the rest of your triangle.\n\nIt should be noted that due to possible rounding errors results may not be 100% accurate; however they will never have an error of more than a few decimal places.\n\npress <enter> to return to main menu")
  #clear screen
  os.system("clear")
  #Check for exit code
  if proceed == EXITCODE:
    exit_code()
  #return to main menu
  main_menu()
#function 3: input_length was created by Thomas Gardner on the 31/07/2022 to find from the user the length of a side of a triangle.
def input_length(known_hypotenuse, lengthF):
  #set up loop and exit code
  while True:
    #set up variables
    error = "This is not a valid length. Please enter a real number greater than 0.\n\nPress <enter> to proceed:\n"
    #get length input
    length = input("Please enter the length of a side of your triangle:\n").lower()
    #clear screen
    os.system("clear")
    #check for exit code
    if length == EXITCODE:
      exit_code()
    #attempt to change input to number; if it doesn't work, catch error
    try:
      #convert the input gathered before to a number and round it to 3dp
      rounded_length = round(float(length), 3)
      #check that length is a valid input
      if rounded_length >= lengthF and known_hypotenuse == True:
        #if the input length is greater than a previously input hypotenuse, give an error message
        proceed = input("This length is greater than the length you have named your hypotenuse. This is not a possible triangle, your hypotenuse must be the longest length.\n").lower()
        #clear screen
        os.system("clear")
        #check for exit code
        if proceed == EXITCODE:
          exit_code()
      #If the rounded length is valid, return it
      elif rounded_length > 0:
        return rounded_length
      #if length is invalid, print error message
      else:
        proceed = input(error).lower()
        #clear screen
        os.system('clear')
        #check for exit code
        if proceed == EXITCODE:
          exit_code()
        #clear screen
    #if the user entered a value that wasn't a number
    except ValueError:
      #print error message
      proceed = input(error).lower()
      #clear screen
      os.system("clear")
      #check for exit code
      if proceed == EXITCODE:
        exit_code()
#Function 4: is_hypotenuse was created by Thomas Gardner on the 2/08/2022 to derive from the user whether a previously input length is the hypotenuse of a triangle
def is_hypotenuse(length):
  #set up error message
  error = "Invalid input. please input 'y', 'n', or 'h'.\n\nPress <enter> to continue:"
  #loop, set up exit code
  while True:
    #Ask the user if their value is the hypotenuse, or if they know what a hypotenuse is
    input_is_hypotenuse = input("Is the value {} the hypotenuse?\n\nIf you don't know what a hypotenuse is, enter 'h':\n".format(length)).lower()
    #clear screen
    os.system("clear")
    #check for exit code
    if input_is_hypotenuse == EXITCODE:
      exit_code()
    #If the user doesn't know what a hypotenuse is, inform them
    if input_is_hypotenuse == "h" or input_is_hypotenuse == "help":
      print("A hypotenuse is the longest side of a right angled triangle. It is also the side that does not at any point come into contact with the right angle.\n")
      proceed = input("Once you understand this, press <enter> to continue:\n").lower()
      #clear screen
      os.system("clear")
      #Check for exit code
      if proceed == EXITCODE:
        exit_code()
    #if the length is the hypotenuse return True
    elif input_is_hypotenuse == "y" or input_is_hypotenuse == "yes":
      #clear screen
      os.system("clear")
      return True
    #If the length is not the hypotenuse return False
    elif input_is_hypotenuse == "n" or input_is_hypotenuse == "no":
      #clear screen
      os.system("clear")
      return False
    #If the user inputs an invalid statement print error message
    else:
      proceed = input(error).lower()
      #clear screen
      os.system("clear")
      #check for exit code
      if proceed == EXITCODE:
        exit_code()
#Function 5: input_angle was created on the 3/08/2022 by Thomas Gardner to get an angle input from the user.
def input_angle():
  #Set up loop and exit code
  while True:
    #Set up variables and error message
    angle = 0
    error = "This is not a valid angle. Please enter a real number greater than 0° and less than 90°\n\nPress <enter> to proceed:\n"
    #get an input for the angle in degrees
    angle = input("Please enter the value of an angle in degrees:\n").lower()
    #clear screen
    os.system("clear")
    #attempt to convert the input to a number and round it to 3dp; catch any errors that might occur.
    try:
      rounded_angle = round(float(angle), 3)
      #check the input angle is valid and return it
      if rounded_angle > 0 and rounded_angle < 90:
        return rounded_angle
      #If the angle is invalid print error message
      else:
        proceed = input(error).lower()
        #clear screen
        os.system("clear")
        #check for exit code
        if proceed == EXITCODE:
          exit_code()
    #if the user inputs an invalid value
    except ValueError:
      #Check if the input value is the exit code
      if angle == EXITCODE:
        exit_code()
      #print error message
      proceed = input(error).lower()
      #clear screen
      os.system("clear")
#Function 6: angle_checker was created on the 6/08/2022 by Thomas Gardner to derive from the user an angles relation to a known length.
def angle_checker(angle, length):
  #Set up loop
  while True:
    #ask the user if the angle is the adjacent; if it is touching the one known length
    is_adjacent = input("Is the angle {}° touching the length {}?:\n ".format(angle, length)).lower()
    #clear screen
    os.system("clear")
    #check for exit code
    if is_adjacent == EXITCODE:
      exit_code()
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
      proceed = input("Invalid input. Please enter yes (y) or no (n)\n\nPress <enter> to proceed:\n").lower()
      #clear screen
      os.system("clear")
      #check for exit code
      if proceed == EXITCODE:
        exit_code()
#function 7: sin_tan was developed on the 20/08/2022 by Thomas Gardner to perform trigonometric calculations for one specific case
def sin_tan(angleA, angleB, angleC, lengthD, lengthE, lengthF):
  #calculte the unknown angle
  angleB = (math.pi / 2) - angleA
  #calculate the first unknown length
  lengthF = round(lengthD / math.sin(angleA), 3)
  #calculate the second unknown length
  lengthE = round(lengthD / math.tan(angleA), 3)
  #return values
  return angleA, angleB, angleC, lengthD, lengthE, lengthF
#function 8: cos_tan was developed on the 20/08/2022 by Thomas Gardner to perform trigonometric calculations for one specific case
def cos_tan(angleA, angleB, angleC, lengthD, lengthE, lengthF):
  #calculate the unknown angle
  angleA = (math.pi / 2) - angleB
  #calculate the first unknown length
  lengthF = round(lengthD / math.cos(angleB), 3)
  #calculate the second unknown length
  lengthE = round(lengthD * math.tan(angleB), 3)
  #return valuesw
  return angleA, angleB, angleC, lengthD, lengthE, lengthF
#function 9: sin_cos was developed on the 20/08/2022 by Thomas Gardner to perform trigonometric calculations for one specific case
def sin_cos(angleA, angleB, angleC, lengthD, lengthE, lengthF):
  #calculate the unknown angle
  angleB = (math.pi / 2) - angleA
  #calculate the first unknown length
  lengthD = round(lengthF * math.sin(angleA), 3)
  #calculate the second unknown length
  lengthE = round(lengthF * math.cos(angleA), 3)
  #return values
  return angleA, angleB, angleC, lengthD, lengthE, lengthF
#function 10: cot_sin was developed on the 20/08/2022 by Thomas Gardner to perform trigonometric calculations for one specific case
def cot_sin(angleA, angleB, angleC, lengthD, lengthE, lengthF):
  #calculate the first unknown angle
  angleA = round(math.atan(lengthD / lengthE), 3)
  #calculat the second unknown angle
  angleB = (math.pi / 2) - angleA
  #calculate the unknown length
  lengthF = round(lengthD / math.sin(angleA), 3)
  #return values
  return angleA, angleB, angleC, lengthD, lengthE, lengthF
#function 11: sec_sin was developed on the 20/08/2022 by Thomas Gardner to perform trigonometric calculations for one specific case
def sec_sin(angleA, angleB, angleC, lengthD, lengthE, lengthF):
  #calculate the first unknown angle
  angleA = round(math.acos(lengthD / lengthF), 3)
  #calculate the second unknown angle
  angleB = (math.pi / 2) - angleA
  #calculate the unknown length
  lengthE = round(lengthF * math.sin(angleA), 3)
  #return values
  return angleA, angleB, angleC, lengthD, lengthE, lengthF
#function 12: exit_code was developed on the 30/08/2022 to allow the user to exit their session whenever they need
def exit_code():
  #inform the user they have entered the exit code and their session is ceasing
  print("Exit code has been entered. Session ceasing\nHistory:\n")
  #get history
  history = open("history.txt", "r")
  #create a list for items in history
  history_items = history.readlines()
  #find the length of the list of history
  history_lines = len(history_items)
  #close the text file
  history.close()
  #create a variable for informing user of history number
  history_number = 0
  #if there is no history, inform the user
  if history_lines == 0:
    print("No history found")
  #if there is history, print all of it in a loop
  else:
    for i in history_items:
      print(history_items[history_number])
      history_number += 1
  #wait for input to proceed
  proceed = input().lower()
  #clear screen
  os.system("clear")
  #check for exit code
  if proceed == EXITCODE:
    exit_code()
  #go to continue_or_exit function
  continue_or_exit()
#function 13: continue_or_exit was created on the 3/09/2022 by Thomas Gardner to give users the option of saving their current history and continuing or wiping it and starting from scratch
def continue_or_exit():
  #establish error code
  error = "Invalid input; Please input either (y)es or (n)o.\n\n Press <enter> to continue:\n"
  #open history text file
  history = open("history.txt", "r")
  #If there is history
  if len(history.readlines()) > 0:
    #close the text file
    history.close()
    #loop, ask the user if they'd like to continue with saved history
    while True:
      finish_or_continue = input("Would you like to continue with your current history?\n").lower()
      #clear screen
      os.system("clear")
      #check for exit code
      if finish_or_continue == EXITCODE:
        exit_code()
      #if the user does want to continue with saved data, continue
      elif finish_or_continue == "y" or finish_or_continue == "yes" or finish_or_continue == "(y)es":
        proceed = input("continuing with current data\n\npress <enter> to continue:")
        #clear screen
        os.system("clear")
        #check for exit code
        if proceed == EXITCODE:
          exit_code()
        #exit loop
        break
      #if the user doesn't want to continue with current saved data, delete it and inform them it's been deleted.
      elif finish_or_continue == "n" or finish_or_continue == "no" or finish_or_continue == "(n)o":
        print("deleting current history...")
        #overwrite history with blank line
        history = open("history.txt", "w")
        history.write("")
        #inform user of deleted history
        proceed = input("History deleted.\n\nPress <enter> to continue:")
        #clear screen
        os.system("clear")
        #check for exit code
        if proceed == EXITCODE:
          exit_code()
        #exit loop
        break
      #if user inputs invalid value, print error message
      else:
        print(error)
    #return to main routine
    main()
  #if there is no saved data, close text file and return to main routine
  else:
    history.close()
#function 14: main was developed on the 28/07/2022 by Thomas Gardner to house the main routine and call functions within the running of the program.
def main():
  #establish loop
  while True:
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
    #this is whether the hypotenuse is known
    known_hypotenuse = False
    #this is whether there are more lengths to input
    more_lengths = True
    #this is the known lengths
    known_lengths = 0
    #this is the known angles
    known_angles = 0
    #this is a temporary length
    temp_length = 0
    #this is a temporary angle
    temp_angle = 0
    #This is the trignonmetric function to apply
    function = ""
    #call main menu function
    main_menu()
    #Get inputs for all known lengths
    while more_lengths == True and known_lengths < 2:
      #input length function assigned to temporary variable
      temp_length = input_length(known_hypotenuse, lengthF)
      #work out which variable to assign length to
      #if the hypotenuse is unknown
      if known_hypotenuse == False:
        #check if the length is the hypotenuse
        known_hypotenuse = is_hypotenuse(temp_length)
        #if the hypotenuse is now known, assign the temporary length to the hypotenuse length
        if known_hypotenuse == True:
          lengthF = temp_length
        #if the hypotenuse is still unknown, assign the temporary length to an unknown length
        elif known_hypotenuse == False:
          if lengthD == 0:
            lengthD = temp_length 
          elif lengthE == 0:
            lengthE = temp_length 
      #if the hypotenuse is already known, assign temporary length to an unknown length
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
          #clear screen
          os.system("clear")
          #check for exit code
          if more_lengths_input == EXITCODE:
            exit_code()
          #If the user does have more lengths to input, exit loop and continue
          if more_lengths_input == "y" or more_lengths_input == "yes":
            break_loop = True
          #If the user has no more lengths to input, exit loop and get an angle
          elif more_lengths_input == "n" or more_lengths_input == "no":
            more_lengths = False
            break_loop = True
          #if the user inputs an invalid value, print error and retry
          else:
            proceed = input("Invalid input. Please try again.\n\nPress <enter> to continue").lower()
            #clear screen
            os.system("clear")
            #exit code
            if proceed == EXITCODE:
              exit_code()
      #If the user has enough lengths to derive the entire triangle, continue to trigonometric functions
      else:
        #inform the user their triangle can now be described
        print("with the given values the entire triangle can now be described. Thankyou for your input.")
        #inform user of the input lengths
    proceed = input("Lengths: \nFirst length: {}\nSecond length: {}\nHypotenuse length: {}\n\nPress <enter> to continue".format(lengthD, lengthE, lengthF)).lower()
    #clear screen
    os.system("clear")
    #check for exit code
    if proceed == EXITCODE:
      exit_code()
    #Get inputs for all known angles if needed
    if known_lengths < 2:
      #Loop, inform user that they don't have enough lengths to derive the entire triangle, get an angle
      while known_angles < 1:
        print("To calculate the dimensions of the right angled triangle with only one known length, you must input 1 angle that is not the 90° angle to proceed.")
        temp_angle = input_angle()
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
    #Save triangle dimensions to text document
    history = open("history.txt", "a")
    history.write("Angles: {}, {}. Right Angle: {}. Lengths: {}, {}. Hypotenuse: {}. Functions: {}\n".format(round(math.degrees(angleA), 2), round(math.degrees(angleB), 2), round(math.degrees(angleC), 2), lengthD, lengthE, lengthF, function))
    history.close()
    #Return triangle dimensions to user
    proceed = input("Values:\n\nAngles:\n\nFirst angle: {}° \nSecond angle: {}°\nRight angle: {}°\n\nLengths:\n\nFirst length: {}\nSecond length: {}\nHypotenuse: {}\n\nFunctions performed: {}\n\nPress <enter> to continue".format(round(math.degrees(angleA), 2), round(math.degrees(angleB), 2), round(math.degrees(angleC), 2), lengthD, lengthE, lengthF, function)).lower()
    #clear screen
    os.system("clear")
    #check for exit code
    if proceed == EXITCODE:
      exit_code()
    #End loop
#open history text document to read
history = open("history.txt", "r")
#if there is any history, ask user if they want to continue with it. otherwise go to main routine.
if len(history.readlines()) > 0:
  history.close()
  print("Previous data found.")
  continue_or_exit()
else:
  history.close()
  main()