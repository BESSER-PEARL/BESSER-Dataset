from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Ask_Player_to_Cut_Deck_UseCase:

    pass


class Reveal_Last_Card_UseCase:

    pass


class Call_for_Last_Bets_UseCase:

    pass


class Deal_UseCase:

    pass


class Cut_Deck_UseCase:

    pass


class Shuffle_Shoe_UseCase:

    pass


class Pay_Chips_UseCase:

    pass


class Take_Chips_UseCase:

    pass


class Leave_Table_UseCase:

    pass


class Sit_at_Table_UseCase:

    pass


class Hit_UseCase:

    pass


class Stand_UseCase:

    pass


class Double_Down_UseCase:

    pass


class Split_Hand_UseCase:

    pass


class Place_Bet_UseCase:

    pass


class Dealer__automated__Actor:

    pass


class Player_Actor:

    pass





class Card:

    def __init__(self, rank: str, suit: int, hand40: "Main" = None):
        self.rank = rank
        self.suit = suit
        self.hand40 = hand40
        
        pass
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: str):
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: int):
        self.__suit = suit

    @property
    def hand40(self):
        return self.__hand40
    @hand40.setter
    def hand40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__hand40", None)
        self.__hand40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card41"):
                opp_val = getattr(old_value, "card41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card41"):
                opp_val = getattr(value, "card41", None)
                if opp_val is None:
                    setattr(value, "card41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Main:

    def __init__(self, cartes: str, value: int, bet: str, player33: "Joueur" = None, dealer39: "Croupier" = None, card41: set["Card"] = None):
        self.cartes = cartes
        self.value = value
        self.bet = bet
        self.player33 = player33
        self.dealer39 = dealer39
        self.card41 = card41 if card41 is not None else set()
        
        pass
    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: str):
        self.__bet = bet

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def cartes(self):
        return self.__cartes
    @cartes.setter
    def cartes(self, cartes: str):
        self.__cartes = cartes

    @property
    def card41(self):
        return self.__card41
    @card41.setter
    def card41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Main__card41", None)
        self.__card41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hand40"):
                    opp_val = getattr(item, "hand40", None)
                    
                    if opp_val == self:
                        setattr(item, "hand40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hand40"):
                    opp_val = getattr(item, "hand40", None)
                    
                    setattr(item, "hand40", self)
                    

    @property
    def dealer39(self):
        return self.__dealer39
    @dealer39.setter
    def dealer39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Main__dealer39", None)
        self.__dealer39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand38"):
                opp_val = getattr(old_value, "hand38", None)
                if opp_val == self:
                    setattr(old_value, "hand38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand38"):
                opp_val = getattr(value, "hand38", None)
                setattr(value, "hand38", self)

    @property
    def player33(self):
        return self.__player33
    @player33.setter
    def player33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Main__player33", None)
        self.__player33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand32"):
                opp_val = getattr(old_value, "hand32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand32"):
                opp_val = getattr(value, "hand32", None)
                if opp_val is None:
                    setattr(value, "hand32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Croupier:

    def __init__(self, main: str, blackjack37: "Blackjack" = None, hand38: "Main" = None):
        self.main = main
        self.blackjack37 = blackjack37
        self.hand38 = hand38
        
        pass
    @property
    def main(self):
        return self.__main
    @main.setter
    def main(self, main: str):
        self.__main = main

    @property
    def hand38(self):
        return self.__hand38
    @hand38.setter
    def hand38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Croupier__hand38", None)
        self.__hand38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer39"):
                opp_val = getattr(old_value, "dealer39", None)
                if opp_val == self:
                    setattr(old_value, "dealer39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer39"):
                opp_val = getattr(value, "dealer39", None)
                setattr(value, "dealer39", self)

    @property
    def blackjack37(self):
        return self.__blackjack37
    @blackjack37.setter
    def blackjack37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Croupier__blackjack37", None)
        self.__blackjack37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer36"):
                opp_val = getattr(old_value, "dealer36", None)
                if opp_val == self:
                    setattr(old_value, "dealer36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer36"):
                opp_val = getattr(value, "dealer36", None)
                setattr(value, "dealer36", self)



class Joueur:

    def __init__(self, main: str, nom: str, playerbank: int, hand32: set["Main"] = None, blackjack35: "Blackjack" = None):
        self.main = main
        self.nom = nom
        self.playerbank = playerbank
        self.hand32 = hand32 if hand32 is not None else set()
        self.blackjack35 = blackjack35
        
        pass
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def main(self):
        return self.__main
    @main.setter
    def main(self, main: str):
        self.__main = main

    @property
    def playerbank(self):
        return self.__playerbank
    @playerbank.setter
    def playerbank(self, playerbank: int):
        self.__playerbank = playerbank

    @property
    def hand32(self):
        return self.__hand32
    @hand32.setter
    def hand32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Joueur__hand32", None)
        self.__hand32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player33"):
                    opp_val = getattr(item, "player33", None)
                    
                    if opp_val == self:
                        setattr(item, "player33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player33"):
                    opp_val = getattr(item, "player33", None)
                    
                    setattr(item, "player33", self)
                    

    @property
    def blackjack35(self):
        return self.__blackjack35
    @blackjack35.setter
    def blackjack35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Joueur__blackjack35", None)
        self.__blackjack35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player34"):
                opp_val = getattr(old_value, "player34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player34"):
                opp_val = getattr(value, "player34", None)
                if opp_val is None:
                    setattr(value, "player34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Blackjack:

    def __init__(self, joueurs: str, croupier: Croupier, player34: set["Joueur"] = None, dealer36: "Croupier" = None):
        self.joueurs = joueurs
        self.croupier = croupier
        self.player34 = player34 if player34 is not None else set()
        self.dealer36 = dealer36
        
        pass
    @property
    def croupier(self):
        return self.__croupier
    @croupier.setter
    def croupier(self, croupier: Croupier):
        self.__croupier = croupier

    @property
    def joueurs(self):
        return self.__joueurs
    @joueurs.setter
    def joueurs(self, joueurs: str):
        self.__joueurs = joueurs

    @property
    def player34(self):
        return self.__player34
    @player34.setter
    def player34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Blackjack__player34", None)
        self.__player34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "blackjack35"):
                    opp_val = getattr(item, "blackjack35", None)
                    
                    if opp_val == self:
                        setattr(item, "blackjack35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "blackjack35"):
                    opp_val = getattr(item, "blackjack35", None)
                    
                    setattr(item, "blackjack35", self)
                    

    @property
    def dealer36(self):
        return self.__dealer36
    @dealer36.setter
    def dealer36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Blackjack__dealer36", None)
        self.__dealer36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack37"):
                opp_val = getattr(old_value, "blackjack37", None)
                if opp_val == self:
                    setattr(old_value, "blackjack37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack37"):
                opp_val = getattr(value, "blackjack37", None)
                setattr(value, "blackjack37", self)



class Stand_UseCase1:

    pass


class Hit_UseCase1:

    pass
