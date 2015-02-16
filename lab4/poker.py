# -*- coding: utf-8 -*-

#	Poker game by Node
#
#
#	We are going to use representants for all the 52 cards we use in poker
#		Suit: S = Spades, H = Hearts, D = Diamonds, C = Clubs 
#		Rank: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
#
#	Notater til Node (Fjernes for innlevering):
#		Les Lab4 oppgavetekst noye
#		Folg Udacity kurset som Janis la ut og snakker om i oppgaveteksten
#		Importer random. Vi kan bruke funksjoner som shuffle() som stokker
#		innehold i en variabel
#		Texas hold em regler, med 5 kort pa en hand
#		Bruke max() funksjon: max("A", 3) = A
#								max('6C', 'QC') = 'QC'
#							tuples: 	max((3, 2), (11, 2)) = (11, 2)
#
#		Skriv en funksjon for å bestemme hvordan max() skal sortere input.
#		Default er ascii men man kan lage en egen funksjon for hvordan input
#		skal bli prioritert. 
#				print max([3, 4, -5, 0], key = abs) max will 
#												sort according to the abs function
#
#		join() og split() funksjoner
#		
#		


import random
						#Ranks:					Suits:
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

random.shuffle(mydeck)

print mydeck

hand = 5 # how many cards per hand

amount_hands = 3 # how many hands you want to be in the play

[mydeck[hand*i:hand*(i+1)] for i in range(amount_hands)]


def poker(hands):
	"Return the best hand: poker([hand, ...]) => hand"
	return max(hands, key=hand_rank)


def hand_rank(hand):
	return pass 
	# SA, SK, SQ, SJ, S10, S9, S8, S7, S6, S5, S4, S3, S2
	# HA, HK, HQ, HJ, H10, H9, H8, H7, H6, H5, H4, H3, H2
	# DA, DK, DQ, DJ, D10, D9, D8, D7, D6, D5, D4, D3, D2
	# CA, CK, CQ, CJ, C10, C9, C8, C7, C6, C5, C4, C3, C2
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):
		return (8, max(ranks))
	elif kind(4, ranks):
		return (7, kind(4, ranks), kind(1, ranks))
	elif ...
	
def card_ranks(cards):
	"return a list of the ranks, sorted with higher first"
	ranks = [r for r,s in cards]
	ranks.sort(reverse=True)
	return ranks

def straight(ranks):
	"Return True if the ordered ranks form a 5-card straight"
	return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
	"Return True if all the cards have the same suit"
	suits = [s for r,s in hand]
	return len(set(suits)) == 1

def kind(n, ranks):
	"Return the first rank that this hand has exactly n of"
	"Return None if there is no n-of-a-kind in the hand"
	for r in  ranks:
		if ranks.count(r) == n: return r
	return None

def two_pair(ranks):
	"If there are two pair, return the two ranks as a"
	"tuple: (highest, lowest); otherwise return None"


def test(): 
	"test cases for the function in poker program"
	sf = "6C 7C 8C 9C TC".SPLIT() # Straight Flush
	fk = "9D 9H 9S 9C 7D".split() #Four of a kind
	fh = "TD TC TH 7C 7D".split() #Full house
	assert poker ([sf, fk, fh]) = sf
	return "tests pass"
print test()


