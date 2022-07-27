#import statements
import os
import time
import math
#functions go here
#Function 1: main_menu was created by Thomas Gardner on the 28/07/2022 to greet the user and inform them of the purpose of this program
def main_menu(proceed):
  #CLEAR SCREEN
  proceed = input("Welcome to Triangle Calculator V1.0! \n\nThis calculator was designed to make your trigonometry homework a breeze!\n\nPress <enter> to continue: ")
  os.system('clear')
  return proceed
#*******Main Routine********
proceed = ""
#Create loop
while proceed != "xxx":
  #Reset Variables
  angleA = 0
  angleB = 0
  #This is the right angle
  angleC = math.pi / 2
  lengthD = 0
  lengthE = 0
  #This is the hypotenuse
  lengthF = 0
  #Main Menu
  proceed = main_menu(proceed)
  #Get inputs for all known lengths
  
  #Get inputs for all known variables if needed
  
  #Decide on trigonometric functions to apply
  
  #Calculate 3 unknowns
  
  #Return triangle dimensions to user
  
  #Save triangle dimensions to text document
  
  #End loop
  
  #Return calculation history
print("Program ceased with exit code 0")