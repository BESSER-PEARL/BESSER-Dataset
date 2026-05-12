from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Suits(Enum):
    pass

############################################
# Definition of Classes
############################################










class Bot:

    def __init__(self, name: str, hand: Hand):
        self.name = name
        self.hand = hand
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: Hand):
        self.__hand = hand



class Player_Interface:

    pass


class Deck_Interface:

    pass


class Cards:

    def __init__(self, num: int, suit: Suits, power: int, value: int):
        self.num = num
        self.suit = suit
        self.power = power
        self.value = value
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Suits):
        self.__suit = suit

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def power(self):
        return self.__power
    @power.setter
    def power(self, power: int):
        self.__power = power



class Hand:

    def __init__(self, cards_6_: str, card4: "Card_Interface" = None):
        self.cards_6_ = cards_6_
        self.card4 = card4
        
        pass
    @property
    def cards_6_(self):
        return self.__cards_6_
    @cards_6_.setter
    def cards_6_(self, cards_6_: str):
        self.__cards_6_ = cards_6_

    @property
    def card4(self):
        return self.__card4
    @card4.setter
    def card4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__card4", None)
        self.__card4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand5"):
                opp_val = getattr(old_value, "hand5", None)
                if opp_val == self:
                    setattr(old_value, "hand5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand5"):
                opp_val = getattr(value, "hand5", None)
                setattr(value, "hand5", self)



class Human:

    def __init__(self, name: str, hand: Hand):
        self.name = name
        self.hand = hand
        
        pass
    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: Hand):
        self.__hand = hand

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Table:

    def __init__(self, players_5_: Player_Interface, Games_6___: Game, scoreSheet: ScoreSheet_Interface, dealer: Player_Interface, numOfGames: int, game1: "Game" = None):
        self.players_5_ = players_5_
        self.Games_6___ = Games_6___
        self.scoreSheet = scoreSheet
        self.dealer = dealer
        self.numOfGames = numOfGames
        self.game1 = game1
        
        pass
    @property
    def players_5_(self):
        return self.__players_5_
    @players_5_.setter
    def players_5_(self, players_5_: Player_Interface):
        self.__players_5_ = players_5_

    @property
    def dealer(self):
        return self.__dealer
    @dealer.setter
    def dealer(self, dealer: Player_Interface):
        self.__dealer = dealer

    @property
    def scoreSheet(self):
        return self.__scoreSheet
    @scoreSheet.setter
    def scoreSheet(self, scoreSheet: ScoreSheet_Interface):
        self.__scoreSheet = scoreSheet

    @property
    def numOfGames(self):
        return self.__numOfGames
    @numOfGames.setter
    def numOfGames(self, numOfGames: int):
        self.__numOfGames = numOfGames

    @property
    def Games_6___(self):
        return self.__Games_6___
    @Games_6___.setter
    def Games_6___(self, Games_6___: Game):
        self.__Games_6___ = Games_6___

    @property
    def game1(self):
        return self.__game1
    @game1.setter
    def game1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__game1", None)
        self.__game1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table0"):
                opp_val = getattr(old_value, "table0", None)
                if opp_val == self:
                    setattr(old_value, "table0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table0"):
                opp_val = getattr(value, "table0", None)
                setattr(value, "table0", self)



class IBlind_Interface:

    pass


class Scores:

    pass


class Trick:

    def __init__(self, Card_5_: str, trickWinner: Player_Interface, round6: "Round" = None):
        self.Card_5_ = Card_5_
        self.trickWinner = trickWinner
        self.round6 = round6
        
        pass
    @property
    def Card_5_(self):
        return self.__Card_5_
    @Card_5_.setter
    def Card_5_(self, Card_5_: str):
        self.__Card_5_ = Card_5_

    @property
    def trickWinner(self):
        return self.__trickWinner
    @trickWinner.setter
    def trickWinner(self, trickWinner: Player_Interface):
        self.__trickWinner = trickWinner

    @property
    def round6(self):
        return self.__round6
    @round6.setter
    def round6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trick__round6", None)
        self.__round6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trick27"):
                opp_val = getattr(old_value, "trick27", None)
                if opp_val == self:
                    setattr(old_value, "trick27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trick27"):
                opp_val = getattr(value, "trick27", None)
                setattr(value, "trick27", self)



class ScoreSheet_Interface:

    pass


class Piquet:

    def __init__(self, cards_32_: Card_Interface):
        self.cards_32_ = cards_32_
        
        pass
    @property
    def cards_32_(self):
        return self.__cards_32_
    @cards_32_.setter
    def cards_32_(self, cards_32_: Card_Interface):
        self.__cards_32_ = cards_32_



class Round:

    def __init__(self, roundNum: int, turnToPlay: Player_Interface, trick: Trick, RoundStarter: Player_Interface, game3: "Game" = None, trick27: "Trick" = None):
        self.roundNum = roundNum
        self.turnToPlay = turnToPlay
        self.trick = trick
        self.RoundStarter = RoundStarter
        self.game3 = game3
        self.trick27 = trick27
        
        pass
    @property
    def RoundStarter(self):
        return self.__RoundStarter
    @RoundStarter.setter
    def RoundStarter(self, RoundStarter: Player_Interface):
        self.__RoundStarter = RoundStarter

    @property
    def trick(self):
        return self.__trick
    @trick.setter
    def trick(self, trick: Trick):
        self.__trick = trick

    @property
    def roundNum(self):
        return self.__roundNum
    @roundNum.setter
    def roundNum(self, roundNum: int):
        self.__roundNum = roundNum

    @property
    def turnToPlay(self):
        return self.__turnToPlay
    @turnToPlay.setter
    def turnToPlay(self, turnToPlay: Player_Interface):
        self.__turnToPlay = turnToPlay

    @property
    def game3(self):
        return self.__game3
    @game3.setter
    def game3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Round__game3", None)
        self.__game3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "round2"):
                opp_val = getattr(old_value, "round2", None)
                if opp_val == self:
                    setattr(old_value, "round2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "round2"):
                opp_val = getattr(value, "round2", None)
                setattr(value, "round2", self)

    @property
    def trick27(self):
        return self.__trick27
    @trick27.setter
    def trick27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Round__trick27", None)
        self.__trick27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "round6"):
                opp_val = getattr(old_value, "round6", None)
                if opp_val == self:
                    setattr(old_value, "round6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "round6"):
                opp_val = getattr(value, "round6", None)
                setattr(value, "round6", self)



class Game:

    def __init__(self, rounds_6_: Round, deck: Deck_Interface, isCracked: bool, picker: Player_Interface, partner: Player_Interface, blind: IBlind_Interface, partnerCard: Card_Interface, table0: "Table" = None, round2: "Round" = None):
        self.rounds_6_ = rounds_6_
        self.deck = deck
        self.isCracked = isCracked
        self.picker = picker
        self.partner = partner
        self.blind = blind
        self.partnerCard = partnerCard
        self.table0 = table0
        self.round2 = round2
        
        pass
    @property
    def rounds_6_(self):
        return self.__rounds_6_
    @rounds_6_.setter
    def rounds_6_(self, rounds_6_: Round):
        self.__rounds_6_ = rounds_6_

    @property
    def picker(self):
        return self.__picker
    @picker.setter
    def picker(self, picker: Player_Interface):
        self.__picker = picker

    @property
    def partner(self):
        return self.__partner
    @partner.setter
    def partner(self, partner: Player_Interface):
        self.__partner = partner

    @property
    def blind(self):
        return self.__blind
    @blind.setter
    def blind(self, blind: IBlind_Interface):
        self.__blind = blind

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Deck_Interface):
        self.__deck = deck

    @property
    def partnerCard(self):
        return self.__partnerCard
    @partnerCard.setter
    def partnerCard(self, partnerCard: Card_Interface):
        self.__partnerCard = partnerCard

    @property
    def isCracked(self):
        return self.__isCracked
    @isCracked.setter
    def isCracked(self, isCracked: bool):
        self.__isCracked = isCracked

    @property
    def round2(self):
        return self.__round2
    @round2.setter
    def round2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__round2", None)
        self.__round2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game3"):
                opp_val = getattr(old_value, "game3", None)
                if opp_val == self:
                    setattr(old_value, "game3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game3"):
                opp_val = getattr(value, "game3", None)
                setattr(value, "game3", self)

    @property
    def table0(self):
        return self.__table0
    @table0.setter
    def table0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__table0", None)
        self.__table0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game1"):
                opp_val = getattr(old_value, "game1", None)
                if opp_val == self:
                    setattr(old_value, "game1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game1"):
                opp_val = getattr(value, "game1", None)
                setattr(value, "game1", self)



class Card_Interface:

    pass
