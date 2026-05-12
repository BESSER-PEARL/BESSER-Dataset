from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class utils_Parser:

    pass


class classes_Hand:

    pass


class combinations_QuinteFlush:

    def __init__(self, start: classes_Card):
        self.start = start
        
        pass
    @property
    def start(self):
        return self.__start
    @start.setter
    def start(self, start: classes_Card):
        self.__start = start



class combinations_Carre:

    def __init__(self, quartet: classes_Card):
        self.quartet = quartet
        
        pass
    @property
    def quartet(self):
        return self.__quartet
    @quartet.setter
    def quartet(self, quartet: classes_Card):
        self.__quartet = quartet



class combinations_Full:

    def __init__(self, paire: classes_Card, triplet: classes_Card):
        self.paire = paire
        self.triplet = triplet
        
        pass
    @property
    def triplet(self):
        return self.__triplet
    @triplet.setter
    def triplet(self, triplet: classes_Card):
        self.__triplet = triplet

    @property
    def paire(self):
        return self.__paire
    @paire.setter
    def paire(self, paire: classes_Card):
        self.__paire = paire



class combinations_Couleur:

    pass


class combinations_Suite:

    def __init__(self, start: classes_Card):
        self.start = start
        
        pass
    @property
    def start(self):
        return self.__start
    @start.setter
    def start(self, start: classes_Card):
        self.__start = start



class combinations_Brelan:

    def __init__(self, triplet: classes_Card):
        self.triplet = triplet
        
        pass
    @property
    def triplet(self):
        return self.__triplet
    @triplet.setter
    def triplet(self, triplet: classes_Card):
        self.__triplet = triplet



class combinations_DoublePaire:

    def __init__(self, strongPaire: classes_Card, weakPaire: classes_Card):
        self.strongPaire = strongPaire
        self.weakPaire = weakPaire
        
        pass
    @property
    def strongPaire(self):
        return self.__strongPaire
    @strongPaire.setter
    def strongPaire(self, strongPaire: classes_Card):
        self.__strongPaire = strongPaire

    @property
    def weakPaire(self):
        return self.__weakPaire
    @weakPaire.setter
    def weakPaire(self, weakPaire: classes_Card):
        self.__weakPaire = weakPaire



class combinations_Paire:

    def __init__(self, paire: classes_Card):
        self.paire = paire
        
        pass
    @property
    def paire(self):
        return self.__paire
    @paire.setter
    def paire(self, paire: classes_Card):
        self.__paire = paire



class combinations_PlusHauteCarte:

    pass


class combinations_Combination(ABC):

    def __init__(self, name: str, value: int, cards0: set["classes_Card"] = None):
        self.name = name
        self.value = value
        self.cards0 = cards0 if cards0 is not None else set()
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cards0(self):
        return self.__cards0
    @cards0.setter
    def cards0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_combinations_Combination__cards0", None)
        self.__cards0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hand1"):
                    opp_val = getattr(item, "hand1", None)
                    
                    if opp_val == self:
                        setattr(item, "hand1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hand1"):
                    opp_val = getattr(item, "hand1", None)
                    
                    setattr(item, "hand1", self)
                    



class classes_Card:

    def __init__(self, name: str, value: int, hand1: "combinations_Combination" = None, hand3: "classes_Hand" = None):
        self.name = name
        self.value = value
        self.hand1 = hand1
        self.hand3 = hand3
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hand3(self):
        return self.__hand3
    @hand3.setter
    def hand3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Card__hand3", None)
        self.__hand3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand2"):
                opp_val = getattr(old_value, "hand2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand2"):
                opp_val = getattr(value, "hand2", None)
                if opp_val is None:
                    setattr(value, "hand2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hand1(self):
        return self.__hand1
    @hand1.setter
    def hand1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Card__hand1", None)
        self.__hand1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards0"):
                opp_val = getattr(old_value, "cards0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards0"):
                opp_val = getattr(value, "cards0", None)
                if opp_val is None:
                    setattr(value, "cards0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class int:

    pass
