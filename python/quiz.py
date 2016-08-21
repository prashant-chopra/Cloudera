
import sys
import random

data_dict={}

if len(sys.argv) < 2:
      print("Please provide file name")
      exit(1)

data_file = open(sys.argv[1],"r")
for line in data_file:
      line=line.strip().split(",")
      data_dict[line[0]]=line[1]

for i in range(1,6):
    state=random.choice(data_dict.keys())
    capital=input("What is the capital of " + state + " > ")

    if capital==data_dict[state]:
        print("Correct")
    else:
        print("Please try again")
