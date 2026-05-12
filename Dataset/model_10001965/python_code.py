from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CardName1(Enum):
    pass
class Suit(Enum):
    pass
class CardName(Enum):
    pass

############################################
# Definition of Classes
############################################










class StandCard:

    pass


class PlayingCard:

    def __init__(self, faceUp: bool, deck7: "Deck" = None):
        self.faceUp = faceUp
        self.deck7 = deck7
        
        pass
    @property
    def faceUp(self):
        return self.__faceUp
    @faceUp.setter
    def faceUp(self, faceUp: bool):
        self.__faceUp = faceUp

    @property
    def deck7(self):
        return self.__deck7
    @deck7.setter
    def deck7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlayingCard__deck7", None)
        self.__deck7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playingCard6"):
                opp_val = getattr(old_value, "playingCard6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playingCard6"):
                opp_val = getattr(value, "playingCard6", None)
                if opp_val is None:
                    setattr(value, "playingCard6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class TEGambler:

    pass


class Banker:

    pass


class TEHandDeck:

    def __init__(self, TE_MAX_SCORE: int):
        self.TE_MAX_SCORE = TE_MAX_SCORE
        
        pass
    @property
    def TE_MAX_SCORE(self):
        return self.__TE_MAX_SCORE
    @TE_MAX_SCORE.setter
    def TE_MAX_SCORE(self, TE_MAX_SCORE: int):
        self.__TE_MAX_SCORE = TE_MAX_SCORE



class HandDeck:

    def __init__(self, owner: GameRole):
        self.owner = owner
        
        pass
    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, owner: GameRole):
        self.__owner = owner



class Player1:

    def __init__(self, name: str, pocket: int, gameRole1: "GameRole" = None):
        self.name = name
        self.pocket = pocket
        self.gameRole1 = gameRole1
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pocket(self):
        return self.__pocket
    @pocket.setter
    def pocket(self, pocket: int):
        self.__pocket = pocket

    @property
    def gameRole1(self):
        return self.__gameRole1
    @gameRole1.setter
    def gameRole1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player1__gameRole1", None)
        self.__gameRole1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player20"):
                opp_val = getattr(old_value, "player20", None)
                if opp_val == self:
                    setattr(old_value, "player20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player20"):
                opp_val = getattr(value, "player20", None)
                setattr(value, "player20", self)



class Dealer:

    def __init__(self, hand: BlackJackHandDeck, handDeck2: "BlackJackHandDeck" = None):
        self.hand = hand
        self.handDeck2 = handDeck2
        
        pass
    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: BlackJackHandDeck):
        self.__hand = hand

    @property
    def handDeck2(self):
        return self.__handDeck2
    @handDeck2.setter
    def handDeck2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__handDeck2", None)
        self.__handDeck2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer3"):
                opp_val = getattr(old_value, "dealer3", None)
                if opp_val == self:
                    setattr(old_value, "dealer3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer3"):
                opp_val = getattr(value, "dealer3", None)
                setattr(value, "dealer3", self)



class Player:

    pass


class Gambler:

    def __init__(self, bet: int, hands: str, hasSplit: bool, handDeck4: set["BlackJackHandDeck"] = None):
        self.bet = bet
        self.hands = hands
        self.hasSplit = hasSplit
        self.handDeck4 = handDeck4 if handDeck4 is not None else set()
        
        pass
    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: int):
        self.__bet = bet

    @property
    def hands(self):
        return self.__hands
    @hands.setter
    def hands(self, hands: str):
        self.__hands = hands

    @property
    def hasSplit(self):
        return self.__hasSplit
    @hasSplit.setter
    def hasSplit(self, hasSplit: bool):
        self.__hasSplit = hasSplit

    @property
    def handDeck4(self):
        return self.__handDeck4
    @handDeck4.setter
    def handDeck4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Gambler__handDeck4", None)
        self.__handDeck4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gambler5"):
                    opp_val = getattr(item, "gambler5", None)
                    
                    if opp_val == self:
                        setattr(item, "gambler5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gambler5"):
                    opp_val = getattr(item, "gambler5", None)
                    
                    setattr(item, "gambler5", self)
                    



class GameRole:

    def __init__(self, player: Player, player20: "Player1" = None):
        self.player = player
        self.player20 = player20
        
        pass
    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player: Player):
        self.__player = player

    @property
    def player20(self):
        return self.__player20
    @player20.setter
    def player20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameRole__player20", None)
        self.__player20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gameRole1"):
                opp_val = getattr(old_value, "gameRole1", None)
                if opp_val == self:
                    setattr(old_value, "gameRole1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gameRole1"):
                opp_val = getattr(value, "gameRole1", None)
                setattr(value, "gameRole1", self)



class BlackJackHandDeck:

    def __init__(self, stand: bool, wager: int, MAX_SCORE: int, dealer3: "Dealer" = None, gambler5: "Gambler" = None):
        self.stand = stand
        self.wager = wager
        self.MAX_SCORE = MAX_SCORE
        self.dealer3 = dealer3
        self.gambler5 = gambler5
        
        pass
    @property
    def wager(self):
        return self.__wager
    @wager.setter
    def wager(self, wager: int):
        self.__wager = wager

    @property
    def stand(self):
        return self.__stand
    @stand.setter
    def stand(self, stand: bool):
        self.__stand = stand

    @property
    def MAX_SCORE(self):
        return self.__MAX_SCORE
    @MAX_SCORE.setter
    def MAX_SCORE(self, MAX_SCORE: int):
        self.__MAX_SCORE = MAX_SCORE

    @property
    def dealer3(self):
        return self.__dealer3
    @dealer3.setter
    def dealer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJackHandDeck__dealer3", None)
        self.__dealer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "handDeck2"):
                opp_val = getattr(old_value, "handDeck2", None)
                if opp_val == self:
                    setattr(old_value, "handDeck2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "handDeck2"):
                opp_val = getattr(value, "handDeck2", None)
                setattr(value, "handDeck2", self)

    @property
    def gambler5(self):
        return self.__gambler5
    @gambler5.setter
    def gambler5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJackHandDeck__gambler5", None)
        self.__gambler5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "handDeck4"):
                opp_val = getattr(old_value, "handDeck4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "handDeck4"):
                opp_val = getattr(value, "handDeck4", None)
                if opp_val is None:
                    setattr(value, "handDeck4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Deck:

    pass


class StandardCard:

    def __init__(self, suit: str, cardName: CardName):
        self.suit = suit
        self.cardName = cardName
        
        pass
    @property
    def cardName(self):
        return self.__cardName
    @cardName.setter
    def cardName(self, cardName: CardName):
        self.__cardName = cardName

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit



class JokerCard:

    def __init__(self, isRed: bool):
        self.isRed = isRed
        
        pass
    @property
    def isRed(self):
        return self.__isRed
    @isRed.setter
    def isRed(self, isRed: bool):
        self.__isRed = isRed

