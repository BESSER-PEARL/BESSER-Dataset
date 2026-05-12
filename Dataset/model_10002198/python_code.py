from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Blackjack:

    def __init__(self, joueurs: str, croupier: Croupier, dealer2: "Croupier" = None, player8: set["Joueur"] = None):
        self.joueurs = joueurs
        self.croupier = croupier
        self.dealer2 = dealer2
        self.player8 = player8 if player8 is not None else set()
        
        pass
    @property
    def joueurs(self):
        return self.__joueurs
    @joueurs.setter
    def joueurs(self, joueurs: str):
        self.__joueurs = joueurs

    @property
    def croupier(self):
        return self.__croupier
    @croupier.setter
    def croupier(self, croupier: Croupier):
        self.__croupier = croupier

    @property
    def player8(self):
        return self.__player8
    @player8.setter
    def player8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Blackjack__player8", None)
        self.__player8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "blackjack9"):
                    opp_val = getattr(item, "blackjack9", None)
                    
                    if opp_val == self:
                        setattr(item, "blackjack9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "blackjack9"):
                    opp_val = getattr(item, "blackjack9", None)
                    
                    setattr(item, "blackjack9", self)
                    

    @property
    def dealer2(self):
        return self.__dealer2
    @dealer2.setter
    def dealer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Blackjack__dealer2", None)
        self.__dealer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack3"):
                opp_val = getattr(old_value, "blackjack3", None)
                if opp_val == self:
                    setattr(old_value, "blackjack3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack3"):
                opp_val = getattr(value, "blackjack3", None)
                setattr(value, "blackjack3", self)



class Joueur:

    def __init__(self, main: str, nom: str, playerbank: int, hand6: set["Main"] = None, blackjack9: "Blackjack" = None):
        self.main = main
        self.nom = nom
        self.playerbank = playerbank
        self.hand6 = hand6 if hand6 is not None else set()
        self.blackjack9 = blackjack9
        
        pass
    @property
    def playerbank(self):
        return self.__playerbank
    @playerbank.setter
    def playerbank(self, playerbank: int):
        self.__playerbank = playerbank

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
    def hand6(self):
        return self.__hand6
    @hand6.setter
    def hand6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Joueur__hand6", None)
        self.__hand6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player7"):
                    opp_val = getattr(item, "player7", None)
                    
                    if opp_val == self:
                        setattr(item, "player7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player7"):
                    opp_val = getattr(item, "player7", None)
                    
                    setattr(item, "player7", self)
                    

    @property
    def blackjack9(self):
        return self.__blackjack9
    @blackjack9.setter
    def blackjack9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Joueur__blackjack9", None)
        self.__blackjack9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player8"):
                opp_val = getattr(old_value, "player8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player8"):
                opp_val = getattr(value, "player8", None)
                if opp_val is None:
                    setattr(value, "player8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Main:

    def __init__(self, cartes: str, value: int, bet: str, card1: set["Carte"] = None, dealer5: "Croupier" = None, player7: "Joueur" = None):
        self.cartes = cartes
        self.value = value
        self.bet = bet
        self.card1 = card1 if card1 is not None else set()
        self.dealer5 = dealer5
        self.player7 = player7
        
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
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Main__card1", None)
        self.__card1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hand0"):
                    opp_val = getattr(item, "hand0", None)
                    
                    if opp_val == self:
                        setattr(item, "hand0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hand0"):
                    opp_val = getattr(item, "hand0", None)
                    
                    setattr(item, "hand0", self)
                    

    @property
    def player7(self):
        return self.__player7
    @player7.setter
    def player7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Main__player7", None)
        self.__player7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand6"):
                opp_val = getattr(old_value, "hand6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand6"):
                opp_val = getattr(value, "hand6", None)
                if opp_val is None:
                    setattr(value, "hand6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dealer5(self):
        return self.__dealer5
    @dealer5.setter
    def dealer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Main__dealer5", None)
        self.__dealer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand4"):
                opp_val = getattr(old_value, "hand4", None)
                if opp_val == self:
                    setattr(old_value, "hand4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand4"):
                opp_val = getattr(value, "hand4", None)
                setattr(value, "hand4", self)



class Croupier:

    def __init__(self, main: str, blackjack3: "Blackjack" = None, hand4: "Main" = None):
        self.main = main
        self.blackjack3 = blackjack3
        self.hand4 = hand4
        
        pass
    @property
    def main(self):
        return self.__main
    @main.setter
    def main(self, main: str):
        self.__main = main

    @property
    def blackjack3(self):
        return self.__blackjack3
    @blackjack3.setter
    def blackjack3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Croupier__blackjack3", None)
        self.__blackjack3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer2"):
                opp_val = getattr(old_value, "dealer2", None)
                if opp_val == self:
                    setattr(old_value, "dealer2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer2"):
                opp_val = getattr(value, "dealer2", None)
                setattr(value, "dealer2", self)

    @property
    def hand4(self):
        return self.__hand4
    @hand4.setter
    def hand4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Croupier__hand4", None)
        self.__hand4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer5"):
                opp_val = getattr(old_value, "dealer5", None)
                if opp_val == self:
                    setattr(old_value, "dealer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer5"):
                opp_val = getattr(value, "dealer5", None)
                setattr(value, "dealer5", self)



class Carte:

    def __init__(self, ordre: str, suit: int, hand0: "Main" = None):
        self.ordre = ordre
        self.suit = suit
        self.hand0 = hand0
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: int):
        self.__suit = suit

    @property
    def ordre(self):
        return self.__ordre
    @ordre.setter
    def ordre(self, ordre: str):
        self.__ordre = ordre

    @property
    def hand0(self):
        return self.__hand0
    @hand0.setter
    def hand0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Carte__hand0", None)
        self.__hand0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card1"):
                opp_val = getattr(old_value, "card1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card1"):
                opp_val = getattr(value, "card1", None)
                if opp_val is None:
                    setattr(value, "card1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

