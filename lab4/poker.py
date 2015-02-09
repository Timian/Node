#	Poker game by Node
#
#
#	We are going to use representants for all the 52 cards we use in poker
#		Suit: S = Spare, H = Hearts, D = Dames, C = Clubs 
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


def test(): 
	"test cases for the function in poker program"
	sf = "6C 7C 8C 9C TC".SPLIT() # Straight Flush
	fk =
	fh =
	assert poker ([sf, fk, fh]) = sf
	return "tests pass"


