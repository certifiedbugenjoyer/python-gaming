#jackblack
import random

# data structures for suits ranks and values
suits = ["spades", "diamonds", "hearts", "clubs"]
ranks = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
values = {'ace': 1, '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'jack': 10,'queen': 10,'king': 10}

#define clas objects: card, deck, player, and hand
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"



class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)
        print('THE DECK HATH BEEN SHUFFLED')

    def deal(self):
        return self.cards.pop()


class Player:
    def __init__(self, bank=100):
        self.bank = bank
        self.bet = 0

    def sub_bank(self, amount):
        self.bank -= amount
        self.bet += amount

    def add_bank(self):
        self.bank += self.bet * 2


class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0

    def draw(self, card):
        self.hand.append(card)
        if (card.rank == 'ace' and self.value < 12):
            self.value += (values[card.rank] + 10)
    
        else:
            self.value += values[card.rank]
    def show(self):
        for card in self.hand:
            print(card)

    def __del__(self):
        pass


# functions: win_check(), replay(), power_button()

def win_check():
    if player_hand.value == 21:
        print("CONGRADULATIONS! U WON! GOOD JOB! YIPPIEEEEEEEE!")
        player.add_bank()
        player_hand.__del__()
        dealer_hand.__del__()
    elif player_hand.value > 21:
        print("u busted lol")
        player_hand.__del__()
        dealer_hand.__del__()
    elif dealer_hand.value == 21:
        print("dealer won L")
        dealer_hand.show
        player_hand.__del__()
        dealer_hand.__del__()
    elif dealer_hand.value > 21:
        print("u won! neat! L dealer")
        player.add_bank
        player_hand.__del__()
        dealer_hand.__del__()
    elif dealer_hand.value == player_hand.value:
        print("u tied L")
        dealer_hand.show
        player_hand.__del__()
        dealer_hand.__del__()  
    elif dealer_hand.value < player_hand.value:
        print("ur hand is higher, so u won! neat!")
        player.add_bank
        player_hand.__del__()
        dealer_hand.__del__()
    else:
        print("dealer won, u lost L + ratio")
        player_hand.__del__()
        dealer_hand.__del__()


def replay_check():
    global replay, game_on
    player_replay = str(input("u want to keep playing? ye or no "))
    player_replay.lower()
    if player_replay[0] == "y":
        print("new round, yay!")
    else:
        print("L quitter")
        replay = False
        game_on = False 

def power_button():
    global replay, game_on
    if player.bank <= 0:
        print("ur broke L")
        replay = False
        game_on = False 


# game state variables

replay = True
game_on = True 

# game loop

while power_button:
    print ("welcome to Erics blackjack game that i copied!")

    player = Player()
    dealer = Player()

    while replay: 
        game_deck = Deck()
        game_deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.draw(game_deck.deal())
        dealer_hand.draw(game_deck.deal())
        player_hand.draw(game_deck.deal())
        dealer_hand.draw(game_deck.deal())
        print(f"the dealer is showing: {dealer_hand.hand[0].__str__()}")
        print("ur hand:")
        player_hand.show()
        print(f"count: {str(player_hand.value)}")
        print(f"u have {str(player.bank)} cash moneys")
        amount = int(input("how much do u want to bet?"))
        player.sub_bank(amount)
        hitorstay = str(input("hit or stay (h or s) "))
        hitorstay.lower()
        while hitorstay == "h" and player_hand.value < 21:
            player_hand.draw(game_deck.deal())
            print("ur hand: ")
            player_hand.show()
            print(f"count: {str(player_hand.value)}")
            hitorstay = str(input("hit or stay (h or s) "))
            hitorstay.lower()
        while dealer_hand.value < 17:
            dealer_hand.draw(game_deck.deal())
        win_check()
        player.bet = 0
        replay_check()
        power_button()

        