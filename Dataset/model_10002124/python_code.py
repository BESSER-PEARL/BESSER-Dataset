from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Hand:

    def __init__(self, num_card: int, max_cards: int, hand: str, addcard: str, blackjack: bool, under: str, bestscore: str, must_hit: bool, busted: str):
        self.num_card = num_card
        self.max_cards = max_cards
        self.hand = hand
        self.addcard = addcard
        self.blackjack = blackjack
        self.under = under
        self.bestscore = bestscore
        self.must_hit = must_hit
        self.busted = busted
        
        pass
    @property
    def bestscore(self):
        return self.__bestscore
    @bestscore.setter
    def bestscore(self, bestscore: str):
        self.__bestscore = bestscore

    @property
    def addcard(self):
        return self.__addcard
    @addcard.setter
    def addcard(self, addcard: str):
        self.__addcard = addcard

    @property
    def max_cards(self):
        return self.__max_cards
    @max_cards.setter
    def max_cards(self, max_cards: int):
        self.__max_cards = max_cards

    @property
    def must_hit(self):
        return self.__must_hit
    @must_hit.setter
    def must_hit(self, must_hit: bool):
        self.__must_hit = must_hit

    @property
    def num_card(self):
        return self.__num_card
    @num_card.setter
    def num_card(self, num_card: int):
        self.__num_card = num_card

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: str):
        self.__hand = hand

    @property
    def blackjack(self):
        return self.__blackjack
    @blackjack.setter
    def blackjack(self, blackjack: bool):
        self.__blackjack = blackjack

    @property
    def busted(self):
        return self.__busted
    @busted.setter
    def busted(self, busted: str):
        self.__busted = busted

    @property
    def under(self):
        return self.__under
    @under.setter
    def under(self, under: str):
        self.__under = under



class Card:

    def __init__(self, value: int, suit: str, cards: str):
        self.value = value
        self.suit = suit
        self.cards = cards
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards



class Deck:

    def __init__(self, cards: str, top_card: str, random: str, deck: str, shuffle: str, random_cards: str, deal_card: str):
        self.cards = cards
        self.top_card = top_card
        self.random = random
        self.deck = deck
        self.shuffle = shuffle
        self.random_cards = random_cards
        self.deal_card = deal_card
        
        pass
    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards

    @property
    def random_cards(self):
        return self.__random_cards
    @random_cards.setter
    def random_cards(self, random_cards: str):
        self.__random_cards = random_cards

    @property
    def random(self):
        return self.__random
    @random.setter
    def random(self, random: str):
        self.__random = random

    @property
    def top_card(self):
        return self.__top_card
    @top_card.setter
    def top_card(self, top_card: str):
        self.__top_card = top_card

    @property
    def shuffle(self):
        return self.__shuffle
    @shuffle.setter
    def shuffle(self, shuffle: str):
        self.__shuffle = shuffle

    @property
    def deal_card(self):
        return self.__deal_card
    @deal_card.setter
    def deal_card(self, deal_card: str):
        self.__deal_card = deal_card



class BlackJack_Hra:

    def __init__(self, bet: str, money: str, deck: str, players_hand: str, dealers_hand: str, play: str, placebet: str, deal: str, player_wins: str, dealer_wins: str, tie: str, player_asks_for_card: str, show_result: str, blackJackApp1: "BlackJackApp" = None):
        self.bet = bet
        self.money = money
        self.deck = deck
        self.players_hand = players_hand
        self.dealers_hand = dealers_hand
        self.play = play
        self.placebet = placebet
        self.deal = deal
        self.player_wins = player_wins
        self.dealer_wins = dealer_wins
        self.tie = tie
        self.player_asks_for_card = player_asks_for_card
        self.show_result = show_result
        self.blackJackApp1 = blackJackApp1
        
        pass
    @property
    def player_asks_for_card(self):
        return self.__player_asks_for_card
    @player_asks_for_card.setter
    def player_asks_for_card(self, player_asks_for_card: str):
        self.__player_asks_for_card = player_asks_for_card

    @property
    def players_hand(self):
        return self.__players_hand
    @players_hand.setter
    def players_hand(self, players_hand: str):
        self.__players_hand = players_hand

    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: str):
        self.__bet = bet

    @property
    def tie(self):
        return self.__tie
    @tie.setter
    def tie(self, tie: str):
        self.__tie = tie

    @property
    def dealer_wins(self):
        return self.__dealer_wins
    @dealer_wins.setter
    def dealer_wins(self, dealer_wins: str):
        self.__dealer_wins = dealer_wins

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money: str):
        self.__money = money

    @property
    def show_result(self):
        return self.__show_result
    @show_result.setter
    def show_result(self, show_result: str):
        self.__show_result = show_result

    @property
    def placebet(self):
        return self.__placebet
    @placebet.setter
    def placebet(self, placebet: str):
        self.__placebet = placebet

    @property
    def player_wins(self):
        return self.__player_wins
    @player_wins.setter
    def player_wins(self, player_wins: str):
        self.__player_wins = player_wins

    @property
    def deal(self):
        return self.__deal
    @deal.setter
    def deal(self, deal: str):
        self.__deal = deal

    @property
    def dealers_hand(self):
        return self.__dealers_hand
    @dealers_hand.setter
    def dealers_hand(self, dealers_hand: str):
        self.__dealers_hand = dealers_hand

    @property
    def play(self):
        return self.__play
    @play.setter
    def play(self, play: str):
        self.__play = play

    @property
    def blackJackApp1(self):
        return self.__blackJackApp1
    @blackJackApp1.setter
    def blackJackApp1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack_Hra__blackJackApp1", None)
        self.__blackJackApp1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackJack_Hra0"):
                opp_val = getattr(old_value, "blackJack_Hra0", None)
                if opp_val == self:
                    setattr(old_value, "blackJack_Hra0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackJack_Hra0"):
                opp_val = getattr(value, "blackJack_Hra0", None)
                setattr(value, "blackJack_Hra0", self)



class BlackJackApp:

    pass
