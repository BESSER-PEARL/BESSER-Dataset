from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Card:

    def __init__(self, id: int, name: str, strength: str, deck5: "Deck" = None):
        self.id = id
        self.name = name
        self.strength = strength
        self.deck5 = deck5
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def strength(self):
        return self.__strength
    @strength.setter
    def strength(self, strength: str):
        self.__strength = strength

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def deck5(self):
        return self.__deck5
    @deck5.setter
    def deck5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck5", None)
        self.__deck5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card4"):
                opp_val = getattr(old_value, "card4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card4"):
                opp_val = getattr(value, "card4", None)
                if opp_val is None:
                    setattr(value, "card4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Deck:

    def __init__(self, id: int, cards: str, players: str, attribute: str, attribute2: str, card4: set["Card"] = None, hand7: set["Hand"] = None, game9: "Game" = None):
        self.id = id
        self.cards = cards
        self.players = players
        self.attribute = attribute
        self.attribute2 = attribute2
        self.card4 = card4 if card4 is not None else set()
        self.hand7 = hand7 if hand7 is not None else set()
        self.game9 = game9
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: str):
        self.__players = players

    @property
    def card4(self):
        return self.__card4
    @card4.setter
    def card4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card4", None)
        self.__card4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck5"):
                    opp_val = getattr(item, "deck5", None)
                    
                    if opp_val == self:
                        setattr(item, "deck5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck5"):
                    opp_val = getattr(item, "deck5", None)
                    
                    setattr(item, "deck5", self)
                    

    @property
    def game9(self):
        return self.__game9
    @game9.setter
    def game9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__game9", None)
        self.__game9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck28"):
                opp_val = getattr(old_value, "deck28", None)
                if opp_val == self:
                    setattr(old_value, "deck28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck28"):
                opp_val = getattr(value, "deck28", None)
                setattr(value, "deck28", self)

    @property
    def hand7(self):
        return self.__hand7
    @hand7.setter
    def hand7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__hand7", None)
        self.__hand7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck6"):
                    opp_val = getattr(item, "deck6", None)
                    
                    if opp_val == self:
                        setattr(item, "deck6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck6"):
                    opp_val = getattr(item, "deck6", None)
                    
                    setattr(item, "deck6", self)
                    



class Hand:

    def __init__(self, id: int, player: Player, game: Game, cards: str, player3: "Player" = None, deck6: "Deck" = None):
        self.id = id
        self.player = player
        self.game = game
        self.cards = cards
        self.player3 = player3
        self.deck6 = deck6
        
        pass
    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player: Player):
        self.__player = player

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def game(self):
        return self.__game
    @game.setter
    def game(self, game: Game):
        self.__game = game

    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards

    @property
    def deck6(self):
        return self.__deck6
    @deck6.setter
    def deck6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__deck6", None)
        self.__deck6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand7"):
                opp_val = getattr(old_value, "hand7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand7"):
                opp_val = getattr(value, "hand7", None)
                if opp_val is None:
                    setattr(value, "hand7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def player3(self):
        return self.__player3
    @player3.setter
    def player3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__player3", None)
        self.__player3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand2"):
                opp_val = getattr(old_value, "hand2", None)
                if opp_val == self:
                    setattr(old_value, "hand2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand2"):
                opp_val = getattr(value, "hand2", None)
                setattr(value, "hand2", self)



class Player:

    def __init__(self, id: int, name: str, hand: Hand, game: Game, cards: str, game1: "Game" = None, hand2: "Hand" = None):
        self.id = id
        self.name = name
        self.hand = hand
        self.game = game
        self.cards = cards
        self.game1 = game1
        self.hand2 = hand2
        
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

    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards

    @property
    def game(self):
        return self.__game
    @game.setter
    def game(self, game: Game):
        self.__game = game

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def hand2(self):
        return self.__hand2
    @hand2.setter
    def hand2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__hand2", None)
        self.__hand2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player3"):
                opp_val = getattr(old_value, "player3", None)
                if opp_val == self:
                    setattr(old_value, "player3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player3"):
                opp_val = getattr(value, "player3", None)
                setattr(value, "player3", self)

    @property
    def game1(self):
        return self.__game1
    @game1.setter
    def game1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__game1", None)
        self.__game1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player0"):
                opp_val = getattr(old_value, "player0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player0"):
                opp_val = getattr(value, "player0", None)
                if opp_val is None:
                    setattr(value, "player0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Game:

    def __init__(self, id: str, name: str, players: str, status: str, deck: Deck, player0: set["Player"] = None, deck28: "Deck" = None):
        self.id = id
        self.name = name
        self.players = players
        self.status = status
        self.deck = deck
        self.player0 = player0 if player0 is not None else set()
        self.deck28 = deck28
        
        pass
    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: str):
        self.__players = players

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Deck):
        self.__deck = deck

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def player0(self):
        return self.__player0
    @player0.setter
    def player0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__player0", None)
        self.__player0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game1"):
                    opp_val = getattr(item, "game1", None)
                    
                    if opp_val == self:
                        setattr(item, "game1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game1"):
                    opp_val = getattr(item, "game1", None)
                    
                    setattr(item, "game1", self)
                    

    @property
    def deck28(self):
        return self.__deck28
    @deck28.setter
    def deck28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__deck28", None)
        self.__deck28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game9"):
                opp_val = getattr(old_value, "game9", None)
                if opp_val == self:
                    setattr(old_value, "game9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game9"):
                opp_val = getattr(value, "game9", None)
                setattr(value, "game9", self)

