from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class model_Value(Enum):
    pass
class model_Color(Enum):
    pass

############################################
# Definition of Classes
############################################










class BlackJack_Program:

    pass


class genmymodelreverse_C1:

    pass


class genmymodelreverse_java_lang_Iterable_Interface(ABC):

    pass


class view_SwedishView:

    pass


class view_SimpleView:

    pass


class view_IView_Interface:

    pass


class rules_RulesFactory:

    pass


class rules_InternationalNewGameStrategy:

    pass


class rules_INewGameStrategy_Interface:

    pass


class rules_IHitStrategy_Interface:

    pass


class rules_BasicHitStrategy:

    def __init__(self, g_hitLimit: int):
        self.g_hitLimit = g_hitLimit
        
        pass
    @property
    def g_hitLimit(self):
        return self.__g_hitLimit
    @g_hitLimit.setter
    def g_hitLimit(self, g_hitLimit: int):
        self.__g_hitLimit = g_hitLimit



class rules_AmericanNewGameStrategy:

    pass


class model_Player:

    def __init__(self, g_maxScore: int, game4: "model_Game" = None, m_hand11: set["model_Card"] = None):
        self.g_maxScore = g_maxScore
        self.game4 = game4
        self.m_hand11 = m_hand11 if m_hand11 is not None else set()
        
        pass
    @property
    def g_maxScore(self):
        return self.__g_maxScore
    @g_maxScore.setter
    def g_maxScore(self, g_maxScore: int):
        self.__g_maxScore = g_maxScore

    @property
    def game4(self):
        return self.__game4
    @game4.setter
    def game4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Player__game4", None)
        self.__game4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "m_player5"):
                opp_val = getattr(old_value, "m_player5", None)
                if opp_val == self:
                    setattr(old_value, "m_player5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "m_player5"):
                opp_val = getattr(value, "m_player5", None)
                setattr(value, "m_player5", self)

    @property
    def m_hand11(self):
        return self.__m_hand11
    @m_hand11.setter
    def m_hand11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Player__m_hand11", None)
        self.__m_hand11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player10"):
                    opp_val = getattr(item, "player10", None)
                    
                    if opp_val == self:
                        setattr(item, "player10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player10"):
                    opp_val = getattr(item, "player10", None)
                    
                    setattr(item, "player10", self)
                    



class model_Game:

    pass


class model_Deck:

    pass


class model_Dealer:

    pass


class model_Card:

    def __init__(self, m_color: model_Color, m_value: model_Value, m_isHidden: bool, deck0: "model_Deck" = None, player10: "model_Player" = None):
        self.m_color = m_color
        self.m_value = m_value
        self.m_isHidden = m_isHidden
        self.deck0 = deck0
        self.player10 = player10
        
        pass
    @property
    def m_color(self):
        return self.__m_color
    @m_color.setter
    def m_color(self, m_color: model_Color):
        self.__m_color = m_color

    @property
    def m_isHidden(self):
        return self.__m_isHidden
    @m_isHidden.setter
    def m_isHidden(self, m_isHidden: bool):
        self.__m_isHidden = m_isHidden

    @property
    def m_value(self):
        return self.__m_value
    @m_value.setter
    def m_value(self, m_value: model_Value):
        self.__m_value = m_value

    @property
    def deck0(self):
        return self.__deck0
    @deck0.setter
    def deck0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Card__deck0", None)
        self.__deck0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "m_cards1"):
                opp_val = getattr(old_value, "m_cards1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "m_cards1"):
                opp_val = getattr(value, "m_cards1", None)
                if opp_val is None:
                    setattr(value, "m_cards1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def player10(self):
        return self.__player10
    @player10.setter
    def player10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Card__player10", None)
        self.__player10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "m_hand11"):
                opp_val = getattr(old_value, "m_hand11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "m_hand11"):
                opp_val = getattr(value, "m_hand11", None)
                if opp_val is None:
                    setattr(value, "m_hand11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class controller_PlayGame:

    pass
