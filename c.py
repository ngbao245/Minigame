


print ("choose bao bua keo")

from random import randint

player = input()
computer = randint(0,2) 


# ----------------------------------------------------------

if computer == 0:
	computer = "Keo"

if computer == 1:
	computer = "Bua"

if computer == 2:
	computer = "Bao"

print("----")
print("You choose: " + player)
print("computer chooses: " + computer)
print("----")



if player == "Keo":
	if computer == "Keo":
		print ("Draw")

if player == "Keo":
	if computer == "Bua":
		print ("Lose")

if player == "Keo":
	if computer == "Bao":
		print ("Win")

if player == "Bua":
	if computer == "Keo":
		print ("Win")

if player == "Bua":
	if computer == "Bua":
		print ("Draw")

if player == "Bua":
	if computer == "Bao":
		print ("Lose")

if player == "Bao":
	if computer == "Keo":
		print ("Lose")

if player == "Bao":
	if computer == "Bua":
		print ("Win")

if player == "Bao":
	if computer == "Bao":
		print ("Draw")

























