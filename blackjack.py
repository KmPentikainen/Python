import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True



class Card:

	def __init__(self,suit,rank):

		self.suit = suit
		self.rank = rank

	def __str__(self):	
		return self.rank+ " of " +self.suit


class Deck:
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))
	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp +='\n'+ card._str_()
		return "The deck Has: "+deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

class Hand:

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value += values[card.rank]

		if card.rank == 'Ace':
			self.aces +=1

	def adjust_for_ace(self):
		
		while self.value > 21 and self.aces > 0:
			self.value -= 10
			self.aces -= 1

#	def split(self):

#		assert self.pair()
#		card = self.cards.pop()
#		hand = Hand(self.bet)
#		hand.add_card(card)
#		return hand

	def double_down_available(self, hand):

		return (self.player_chips)(take.bet) and (len.hand.cards) == 2 and hand.value() in (9, 10, 11)

	def surrender(self):
		pass
			
class Chips:

	def __init__(self, total=1000):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total +=self.bet

	def lose_bet(self):
		self.total -= self.bet

def take_bet(chips):

	while True:

		try:
			chips.bet = int(input("How many chips you want to bet? "))
		except:
			print("Sorry please provide an integer.")
		else:
			if chips.bet > chips.total:
				print('Sorry, you do not have enought chips')
			else:
				break

def hit(deck, hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace() 

def hit_or_stand(deck, hand):
	global playing

	while True:
		x=input('Hit(h) or stand(s)? ')

		if x[0].lower() == 'h':
			hit(deck,hand)

		elif x[0].lower() == 's':
			print()
			print("Player stands, Dealers turn")
			playing = False

		else:
			print("Error")
			continue
		break

#def split_hand(self, player, hand):
#	if hand.pair():
#		prompt_split = input("Would you like to split? (Y/N) ")
#		if prompt_split =="Y":
#			new_hand = hand.split()
#			player.bet(take.bet)
#			self.add_card(hand, player)
#			self.add_card(new_hand, player)
#			player.hand.append(new_hand)
#			self.show_some(player_hand, split_hand)

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def double_down(self, player, hand):
	player_chips(take.bet)
	take.bet += take_bet
	if player_busts:
		self.player_busts(player, hand)

def player_busts(player, dealer, chips):

	print("BUST PLAYER!")
	chips.lose_bet()

def player_wins(player, dealer, chips):

	print("PLAYER WINS!")
	chips.win_bet()

def dealer_busts(player, dealer, chips):

	print("DEALER BUST!")
	chips.win_bet()

def dealer_wins(player, dealer, chips):

	print("DEALER WINS")
	chips.lose_bet()

def push(player,dealer):
	print("Dealer and player tie! PUSH")

while True:
	print('Welcome to play BlackJack! Try to get as close as 21 as possible! Dealer must stand on 17 ')
	print()


	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	player_chips = Chips()

	take_bet(player_chips)

	show_some(player_hand, dealer_hand)

	while playing:

		hit_or_stand(deck, player_hand)
		time.sleep(2)
		show_some(player_hand, dealer_hand)
		time.sleep(2)


		if player_hand.value > 21:
			player_busts(player_hand, dealer_hand, player_chips)

			break

		if double_down_available(hand):
			double_down()

	if player_hand.value < 21:

		while dealer_hand.value < 17:
			hit(deck, dealer_hand)

		show_all(player_hand, dealer_hand)

		if dealer_hand.value > 21:
			dealer_busts(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)
		else:
			push(player_hand, dealer_hand)

	print("\nPlayer's winnings stand at",player_chips.total)
	print()
    
    
	new_game = input("Would you like to play another hand? Continue(y) or Goodbye(n)")
	if new_game[0].lower()=='y':
		playing=True
		continue
	else:
		print("Thanks for playing!")
		break 
