from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class G:

    pass


class E:

    def __init__(self, attE: str, g13: "G" = None):
        self.attE = attE
        self.g13 = g13
        
        pass
    @property
    def attE(self):
        return self.__attE
    @attE.setter
    def attE(self, attE: str):
        self.__attE = attE

    @property
    def g13(self):
        return self.__g13
    @g13.setter
    def g13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_E__g13", None)
        self.__g13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e12"):
                opp_val = getattr(old_value, "e12", None)
                if opp_val == self:
                    setattr(old_value, "e12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e12"):
                opp_val = getattr(value, "e12", None)
                setattr(value, "e12", self)



class F:

    def __init__(self, attF: str):
        self.attF = attF
        
        pass
    @property
    def attF(self):
        return self.__attF
    @attF.setter
    def attF(self, attF: str):
        self.__attF = attF



class PACS:

    pass


class Mariage:

    pass


class Personne:

    pass


class Union:

    def __init__(self, dateUnion: str, pers6: set["Personne"] = None, personne8: set["Personne"] = None):
        self.dateUnion = dateUnion
        self.pers6 = pers6 if pers6 is not None else set()
        self.personne8 = personne8 if personne8 is not None else set()
        
        pass
    @property
    def dateUnion(self):
        return self.__dateUnion
    @dateUnion.setter
    def dateUnion(self, dateUnion: str):
        self.__dateUnion = dateUnion

    @property
    def pers6(self):
        return self.__pers6
    @pers6.setter
    def pers6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Union__pers6", None)
        self.__pers6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "union7"):
                    opp_val = getattr(item, "union7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "union7"):
                    opp_val = getattr(item, "union7", None)
                    
                    if opp_val is None:
                        setattr(item, "union7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def personne8(self):
        return self.__personne8
    @personne8.setter
    def personne8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Union__personne8", None)
        self.__personne8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "unionActuelle9"):
                    opp_val = getattr(item, "unionActuelle9", None)
                    
                    if opp_val == self:
                        setattr(item, "unionActuelle9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "unionActuelle9"):
                    opp_val = getattr(item, "unionActuelle9", None)
                    
                    setattr(item, "unionActuelle9", self)
                    



class C3:

    pass


class C2:

    pass


class R:

    pass


class Z:

    pass


class Y:

    pass


class C:

    def __init__(self, attC1: int, attC2: bool, b1: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b1 = b1
        
        pass
    @property
    def attC1(self):
        return self.__attC1
    @attC1.setter
    def attC1(self, attC1: int):
        self.__attC1 = attC1

    @property
    def attC2(self):
        return self.__attC2
    @attC2.setter
    def attC2(self, attC2: bool):
        self.__attC2 = attC2

    @property
    def b1(self):
        return self.__b1
    @b1.setter
    def b1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b1", None)
        self.__b1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c0"):
                opp_val = getattr(old_value, "c0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c0"):
                opp_val = getattr(value, "c0", None)
                if opp_val is None:
                    setattr(value, "c0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B:

    def __init__(self, attB: int, c0: set["C"] = None, a5: "A" = None):
        self.attB = attB
        self.c0 = c0 if c0 is not None else set()
        self.a5 = a5
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def c0(self):
        return self.__c0
    @c0.setter
    def c0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c0", None)
        self.__c0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b1"):
                    opp_val = getattr(item, "b1", None)
                    
                    if opp_val == self:
                        setattr(item, "b1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b1"):
                    opp_val = getattr(item, "b1", None)
                    
                    setattr(item, "b1", self)
                    

    @property
    def a5(self):
        return self.__a5
    @a5.setter
    def a5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__a5", None)
        self.__a5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b4"):
                opp_val = getattr(old_value, "b4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b4"):
                opp_val = getattr(value, "b4", None)
                if opp_val is None:
                    setattr(value, "b4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class A(ABC):

    def __init__(self, attA: str, r3: "R" = None, b4: set["B"] = None):
        self.attA = attA
        self.r3 = r3
        self.b4 = b4 if b4 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def r3(self):
        return self.__r3
    @r3.setter
    def r3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__r3", None)
        self.__r3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aR2"):
                opp_val = getattr(old_value, "aR2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR2"):
                opp_val = getattr(value, "aR2", None)
                if opp_val is None:
                    setattr(value, "aR2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b4(self):
        return self.__b4
    @b4.setter
    def b4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b4", None)
        self.__b4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a5"):
                    opp_val = getattr(item, "a5", None)
                    
                    if opp_val == self:
                        setattr(item, "a5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a5"):
                    opp_val = getattr(item, "a5", None)
                    
                    setattr(item, "a5", self)
                    

