#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)
import random
from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'
cards = []

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self, suite=['H','D','S','C'], ranks=['2','3','4','5','6','7','8','9','10','J','Q','K','A']):
        self.suite = suite
        self.ranks = ranks
        self.cards = cards

    #создать DEck (все Ranks * все SUITE)
    def createDeck(self):
        for r in self.ranks:
            for s in self.suite:
                c = (r+s)
                #print("Card:", c)
                self.cards.append(c)
        print("Колода создана, в колоде ", len(self.cards),"карт.", "Колода: ", self.cards)
        return self.cards

    #перемешать колоду
    def shufDeck(self):
        print(self.cards)
        random.shuffle(self.cards)
        print("Колода перемешана: ", self.cards)
        return self.cards

    #разделить колоду
    def cutDeck(self):
        h1=self.cards[:26]
        h2=self.cards[26:]
        hands=(h1,h2)
        return hands

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def __len__(self):
        return len(self.cards)

    #добавить карту
    def add_card(self,added_cards):
        self.cards.extend(added_cards)

    #удалить карту
    def remove_card(self):
        return self.cards.pop()




class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return "Игор: {}, имеет на руках: {}".format(self.name,self.hand)

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} сыграл: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        for x in range(3):
            war_cards.append(self.hand.remove_card())
        return war_cards

    def still_has_cards(self):
        """
        Возвращает True, если у игрока остались карты
        """
        return len(self.hand.cards) != 0
    #имя игрока
    #Hand игрока


#логика игры
def round():
    i=0
    while (player1.hand != []) or (player2.hand != []):
        print("Раунд: ", i+1)
        card1=player1.play_card()
        card2=player2.play_card()

        if card1 != card2:
            if card1>card2:
                added_cards=[card1,card2]
                player1.hand.add_card(added_cards)
                print("Победил", player1.name,"Он забирает карты,теперь у него", len(player1.hand.cards),"карт в колоде")
                i=i+1
            else:
                added_cards=[card1,card2]
                player2.hand.add_card(added_cards)
                print("Победил", player2.name,"Он забирает карты,теперь у него", len(player2.hand.cards),"карт в колоде")
                i=i+1
        else: godraw()

def godraw():
    print("Ешки матрешки, у нас ничья, каждый игрок добавляет по три карты")
    card1=player1.hand.remove_war_cards()
    card2=player2.hand.remove_war_cards()
    drawcards1=player.play_card()
    drawcards2=player.play_card()
    print(player1.name," Выкладывает карту: ", card1, "и еще три сверху")
    print(player2.name," Выкладывает карту: ", card2, "и еще три сверху")
    if card1 != card2:
        if card1>card2:
            added_cards=[card1,card2,drawcards1, drawcards2]
            player1.add_card()
            print("Победил", player1.name,"Он забирает карты,теперь у него", len(player1.hand.cards),"карт в колоде")
            i=i+1
        else:
            added_cards=[card1,card2,drawcards1, drawcards2]
            player2.add_card()
            print("Победил", player2.name,"Он забирает карты,теперь у него", len(player2.hand.cards),"карт в колоде")
            i=i+1
    else: print("Пошли нахуй, карты уходят в банк")

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

my_deck = Deck()
print("Создаю колоду:" ,my_deck.createDeck())
print("Перемешиваю колоду:",my_deck.shufDeck())
h1,h2=my_deck.cutDeck()
# print("Handtup:",handtup)
# print(handtup[0])
# hc1=handtup[0]
# h1=Hand()
# print("h1: ",h1)
# h2=Hand(handtup[1])
p1 = input("Игрок №1, введи имя:")
player1 = Player(p1,Hand(h1))
print(player1)
p2 = input("Игрок №2, введи имя:")
player2 = Player(p2,Hand(h2))
print(player2)
print("У", player1.name, "На руках ", len(player1.hand),"карт:")
# print("У", player1.name, "На руках ", len(player1.hand),"карт:",player1.hand)
print("У", player2.name, "На руках ", len(player2.hand),"карт:")
# print("У", player2.name, "На руках ", len(player2.hand),"карт:",player2.hand)
round()
