from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class PACS:

    pass


class Mariage:

    pass


class Union:

    def __init__(self, dateUnion: int, pers9: set["Personne"] = None, personne11: set["Personne"] = None):
        self.dateUnion = dateUnion
        self.pers9 = pers9 if pers9 is not None else set()
        self.personne11 = personne11 if personne11 is not None else set()
        
        pass
    @property
    def dateUnion(self):
        return self.__dateUnion
    @dateUnion.setter
    def dateUnion(self, dateUnion: int):
        self.__dateUnion = dateUnion

    @property
    def pers9(self):
        return self.__pers9
    @pers9.setter
    def pers9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Union__pers9", None)
        self.__pers9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "union8"):
                    opp_val = getattr(item, "union8", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "union8"):
                    opp_val = getattr(item, "union8", None)
                    
                    if opp_val is None:
                        setattr(item, "union8", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def personne11(self):
        return self.__personne11
    @personne11.setter
    def personne11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Union__personne11", None)
        self.__personne11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "unionActuelle10"):
                    opp_val = getattr(item, "unionActuelle10", None)
                    
                    if opp_val == self:
                        setattr(item, "unionActuelle10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "unionActuelle10"):
                    opp_val = getattr(item, "unionActuelle10", None)
                    
                    setattr(item, "unionActuelle10", self)
                    



class Personne:

    pass


class C2:

    pass


class C:

    def __init__(self, attC1: int, attC2: bool, b1: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b1 = b1
        
        pass
    @property
    def attC2(self):
        return self.__attC2
    @attC2.setter
    def attC2(self, attC2: bool):
        self.__attC2 = attC2

    @property
    def attC1(self):
        return self.__attC1
    @attC1.setter
    def attC1(self, attC1: int):
        self.__attC1 = attC1

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

    def __init__(self, attB: int, c0: set["C"] = None, y3: "Y" = None):
        self.attB = attB
        self.c0 = c0 if c0 is not None else set()
        self.y3 = y3
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def y3(self):
        return self.__y3
    @y3.setter
    def y3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__y3", None)
        self.__y3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b2"):
                opp_val = getattr(old_value, "b2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b2"):
                opp_val = getattr(value, "b2", None)
                if opp_val is None:
                    setattr(value, "b2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    



class C1:

    pass


class Z:

    pass


class A:

    def __init__(self, attA: str, r5: "R" = None):
        self.attA = attA
        self.r5 = r5
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def r5(self):
        return self.__r5
    @r5.setter
    def r5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__r5", None)
        self.__r5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aR4"):
                opp_val = getattr(old_value, "aR4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR4"):
                opp_val = getattr(value, "aR4", None)
                if opp_val is None:
                    setattr(value, "aR4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class R:

    pass


class Y:

    def __init__(self, attY: str, b2: set["B"] = None):
        self.attY = attY
        self.b2 = b2 if b2 is not None else set()
        
        pass
    @property
    def attY(self):
        return self.__attY
    @attY.setter
    def attY(self, attY: str):
        self.__attY = attY

    @property
    def b2(self):
        return self.__b2
    @b2.setter
    def b2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Y__b2", None)
        self.__b2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "y3"):
                    opp_val = getattr(item, "y3", None)
                    
                    if opp_val == self:
                        setattr(item, "y3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "y3"):
                    opp_val = getattr(item, "y3", None)
                    
                    setattr(item, "y3", self)
                    

