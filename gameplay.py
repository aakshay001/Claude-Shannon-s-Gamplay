#Put all the functions and variables of the Mind Reader game algorithm here.
import numpy as np
import random as rd 

inputs = np.zeros(shape=(2,2,2),dtype=int)

last_1 = 0
last_2 = 0

scores = [0, 0]


def update_inputs(current):
  global last_1, last_2
  if inputs[last_2][last_1][0] == current:
    inputs[last_2][last_1][1] = 1
    inputs[last_2][last_1][0] = current
  else:
    inputs[last_2][last_1][1] = 0
    inputs[last_2][last_1][0] = current  
  last_2 = last_1
  last_1 = current

def prediction():
  if inputs[last_2][last_1][1] == 1:
    predict =  inputs[last_2][last_1][0]
  else:
    predict = rd.randint(0,1)  
  return predict 

def update_scores(predicted, player_input):
  
  if predicted == player_input:
    scores[0] = scores[0] + 1
    print("Computer Score:",scores[0])
    print("Player Score:",scores[1])   

  else:
    scores[1] = scores[1] + 1
    print("Computer Score:",scores[0])
    print("Player Score:",scores[1]) 

def reset():
  inputs = [[[0 for items in range(2)]for row in range(2)]for blocks in range(2)]
  scores = [0,0]
  
# Student Action: Create the 'gameplay()' function.
def gameplay():
  reset()
  
  print(inputs)
  print(scores)
  valid_entries = ['0', '1']
  while True:
    predicted = prediction()
    player_input = input("Enter either 0 or 1:")

    while player_input not in valid_entries:
      print("Invalid Input")
      player_input = input("Please! Enter either 0 or 1:")
      
    player_input = int(player_input)  
    update_inputs(player_input)
    update_scores(predicted,player_input)

    if scores[0] == 10:
      print("Bad luck,AIbot Won.")
      break
    elif scores[1] == 10:
      print("Congrats!! You Won.")  
      break
      
