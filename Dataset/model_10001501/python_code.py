from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class TarotCard___Card:

    def __init__(self, _id: int, _fileName: str, _fortunes: str):
        self._id = _id
        self._fileName = _fileName
        self._fortunes = _fortunes
        
        pass
    @property
    def _fortunes(self):
        return self.___fortunes
    @_fortunes.setter
    def _fortunes(self, _fortunes: str):
        self.___fortunes = _fortunes

    @property
    def _fileName(self):
        return self.___fileName
    @_fileName.setter
    def _fileName(self, _fileName: str):
        self.___fileName = _fileName

    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: int):
        self.___id = _id



class Card___Abstract__:

    def __init__(self, _id: int, deck0: "Deck" = None):
        self._id = _id
        self.deck0 = deck0
        
        pass
    @property
    def _id(self):
        return self.___id
    @_id.setter
    def _id(self, _id: int):
        self.___id = _id

    @property
    def deck0(self):
        return self.__deck0
    @deck0.setter
    def deck0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card___Abstract____deck0", None)
        self.__deck0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card___Abstract__1"):
                opp_val = getattr(old_value, "card___Abstract__1", None)
                if opp_val == self:
                    setattr(old_value, "card___Abstract__1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card___Abstract__1"):
                opp_val = getattr(value, "card___Abstract__1", None)
                setattr(value, "card___Abstract__1", self)



class FortuneTeller:

    def __init__(self, _tarotDeck: Deck, deck2: "Deck" = None):
        self._tarotDeck = _tarotDeck
        self.deck2 = deck2
        
        pass
    @property
    def _tarotDeck(self):
        return self.___tarotDeck
    @_tarotDeck.setter
    def _tarotDeck(self, _tarotDeck: Deck):
        self.___tarotDeck = _tarotDeck

    @property
    def deck2(self):
        return self.__deck2
    @deck2.setter
    def deck2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FortuneTeller__deck2", None)
        self.__deck2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fortuneTeller3"):
                opp_val = getattr(old_value, "fortuneTeller3", None)
                if opp_val == self:
                    setattr(old_value, "fortuneTeller3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fortuneTeller3"):
                opp_val = getattr(value, "fortuneTeller3", None)
                setattr(value, "fortuneTeller3", self)



class Deck:

    def __init__(self, _deck: str, card___Abstract__1: "Card___Abstract__" = None, fortuneTeller3: "FortuneTeller" = None):
        self._deck = _deck
        self.card___Abstract__1 = card___Abstract__1
        self.fortuneTeller3 = fortuneTeller3
        
        pass
    @property
    def _deck(self):
        return self.___deck
    @_deck.setter
    def _deck(self, _deck: str):
        self.___deck = _deck

    @property
    def fortuneTeller3(self):
        return self.__fortuneTeller3
    @fortuneTeller3.setter
    def fortuneTeller3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__fortuneTeller3", None)
        self.__fortuneTeller3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck2"):
                opp_val = getattr(old_value, "deck2", None)
                if opp_val == self:
                    setattr(old_value, "deck2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck2"):
                opp_val = getattr(value, "deck2", None)
                setattr(value, "deck2", self)

    @property
    def card___Abstract__1(self):
        return self.__card___Abstract__1
    @card___Abstract__1.setter
    def card___Abstract__1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card___Abstract__1", None)
        self.__card___Abstract__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck0"):
                opp_val = getattr(old_value, "deck0", None)
                if opp_val == self:
                    setattr(old_value, "deck0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck0"):
                opp_val = getattr(value, "deck0", None)
                setattr(value, "deck0", self)

