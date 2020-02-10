#!/usr/bin/env python3
## Version to automate through a number of hands
import random
import os

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*24
random.shuffle(deck)
result = ""
score = []

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def deal(deck):
    hand = []
    for i in range(2):
	    card = deck.pop()
	    if card == 11:card = "J"
	    if card == 12:card = "Q"
	    if card == 13:card = "K"
	    if card == 14:card = "A"
	    hand.append(card)
    return hand

def scoreHand(hand):
	total = 0
	card = 0
	for card in hand:
		if card == "J" or card == "Q" or card == "K":
			card = 10
		elif card == "A":
			if total >= 11:
				card = 1
			else:
				card = 11
		total += card
	return total

def hit(hand):
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
	return hand

def game():
	choice = ""
	global score
	playerHand=deal(deck)
	dealerHand=deal(deck)
	playerScore=scoreHand(playerHand)
	dealerScore=scoreHand(dealerHand)
	print("You have: " + str(playerHand) + " for a total of: " + str(playerScore))
	if dealerScore == 21 and playerScore == 21:
		print("The dealer has: " + str(dealerHand) + " for a total of: " + str(dealerScore))
		print("You and the dealer both have a BlackJack! It's a Push.")
		score.append("push")
		return
	elif dealerScore == 21:
		print("The dealer has: " + str(dealerHand) + " for a total of: " + str(dealerScore))
		print("The dealer has a BlackJack! You lose.")
		score.append("loss")
		return
	elif playerScore == 21:
		print("The dealer has: " + str(dealerHand) + " for a total of: " + str(dealerScore))
		print("You have a BlackJack and you Win!")
		score.append("win")
		return
	else:
		print("The dealer is showing: " + str(dealerHand[0]))
		while choice != "s":
			choice = input("Would you like to [H]it or [S]tand?").lower()
			print(choice)
			if choice == "h":
				playerHand = hit(playerHand)
				playerScore=scoreHand(playerHand)
				if playerScore <= 21:
					print("You have: " + str(playerHand) + " for a total of: " + str(playerScore))
					continue
				else:
					print("You have: " + str(playerHand) + " for a total of: " + str(playerScore))
					print("You have busted!")
					score.append("loss")
					return
			if choice == "s":
				break
		print("The dealer has: " + str(dealerHand) + " for a total of: " + str(dealerScore))
		while dealerScore <= 17:
			if "A" in dealerHand and dealerScore == 17:
				print("Dealer must hit on a soft 17")
				dealerHand = hit(dealerHand)
				dealerScore = scoreHand(dealerHand)
				print("The dealer has: " + str(dealerHand) + " for a total of: " + str(dealerScore))
				continue
			elif dealerScore < 17:
				print("The Dealer hits")
				dealerHand = hit(dealerHand)
				dealerScore = scoreHand(dealerHand)
				print("The dealer has: " + str(dealerHand) + " for a total of: " + str(dealerScore))
				continue
			else:
				break
		if dealerScore > 21:
			print("The dealer has busted! You Win!")
			score.append("win")
			return
		elif dealerScore == playerScore:
			print("It's a Push!")
			score.append("push")
			return
		elif dealerScore > playerScore:
			print("The Dealer Wins!")
			score.append("loss")
			return
		elif dealerScore < playerScore:
			print("You Win!")
			score.append("win")
			return


def main():
	choice = ""
	global deck
	global result
	while choice != "n":
		clear()
		if len(deck) < 15:
			print("Shuffling the cards...")
			deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
			random.shuffle(deck)
		game()
		score.append(result)
		print("The results are Win: " + str(score.count("win")) + " Loss: " 
			+ str(score.count("loss")) + " Push: " 
			+ str(score.count("push")))
		choice = input("Would you like to play again? [Y]es or [N]o: ").lower()

main()
