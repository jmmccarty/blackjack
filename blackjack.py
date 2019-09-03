#!/usr/bin/env python3
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
random.shuffle(deck)

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
	playerHand=deal(deck)
	dealerHand=deal(deck)
	playerScore=scoreHand(playerHand)
	dealerScore=scoreHand(dealerHand)
	print("You have: " + str(playerHand) + " for a total of: " + str(playerScore))
	if dealerScore == 21 and playerScore == 21:
		print("The dealer has: " + str(dealerHand) + " for a total of: " + str(dealerScore))
		print("You and the dealer both have a BlackJack! It's a Push.")
		result = "push"
		return result
	elif dealerScore == 21:
		print("The dealer has: " + str(dealerHand) + " for a total of: " + str(dealerScore))
		print("The dealer has a BlackJack! You lose.")
		result = "lose"
		return result
	elif playerScore == 21:
		print("The dealer has: " + str(dealerHand) + " for a total of: " + str(dealerScore))
		print("You have a BlackJack and you Win!")
		result = "win"
		return result
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
					result = "lose"
					return result
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
			result = "win"
			return result
		elif dealerScore == playerScore:
			print("It's a Push!")
			result = "push"
			return result
		elif dealerScore > playerScore:
			print("The Dealer Wins!")
			result = "lose"
			return result
		elif dealerScore < playerScore:
			print("You Win!")
			result = "win"
			return result




		


game()

#pph = str(playerHand)
#pdh = str(dealerHand)
#pps = str(playerScore)
#pds = str(dealerScore)
#print("player hand:" + pph + "dealer hand" + pdh)
#print("player score: " + pps + " dealer hand " + pds)

#playerHand = hit(playerHand)
#dealerHand = hit(dealerHand)
#playerScore = scoreHand(playerHand)
#dealerScore = scoreHand(dealerHand)

#print("player hand:" + str(playerHand) + "dealer hand" + str(dealerHand))
#print("player score: " + str(playerScore) + " dealer hand " + str(dealerScore))
