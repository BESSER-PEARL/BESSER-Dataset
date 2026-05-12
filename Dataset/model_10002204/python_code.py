from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class A:

    def __init__(self, attA: str, b0: set["B"] = None, r5: "R" = None):
        self.attA = attA
        self.b0 = b0 if b0 is not None else set()
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

    @property
    def b0(self):
        return self.__b0
    @b0.setter
    def b0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b0", None)
        self.__b0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a1"):
                    opp_val = getattr(item, "a1", None)
                    
                    if opp_val == self:
                        setattr(item, "a1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a1"):
                    opp_val = getattr(item, "a1", None)
                    
                    setattr(item, "a1", self)
                    



class B2:

    pass


class A3:

    pass


class A1:

    def __init__(self, b: bool, d: int, c13: "B1" = None):
        self.b = b
        self.d = d
        self.c13 = c13
        
        pass
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, b: bool):
        self.__b = b

    @property
    def d(self):
        return self.__d
    @d.setter
    def d(self, d: int):
        self.__d = d

    @property
    def c13(self):
        return self.__c13
    @c13.setter
    def c13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__c13", None)
        self.__c13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_A_012"):
                opp_val = getattr(old_value, "B_A_012", None)
                if opp_val == self:
                    setattr(old_value, "B_A_012", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_A_012"):
                opp_val = getattr(value, "B_A_012", None)
                setattr(value, "B_A_012", self)



class A2:

    pass


class B1:

    pass


class PACS:

    pass


class Marriage:

    pass


class Union:

    def __init__(self, dateUnion: str, pers6: set["Personne"] = None, personnes9: set["Personne"] = None):
        self.dateUnion = dateUnion
        self.pers6 = pers6 if pers6 is not None else set()
        self.personnes9 = personnes9 if personnes9 is not None else set()
        
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
    def personnes9(self):
        return self.__personnes9
    @personnes9.setter
    def personnes9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Union__personnes9", None)
        self.__personnes9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "unionActuelle8"):
                    opp_val = getattr(item, "unionActuelle8", None)
                    
                    if opp_val == self:
                        setattr(item, "unionActuelle8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "unionActuelle8"):
                    opp_val = getattr(item, "unionActuelle8", None)
                    
                    setattr(item, "unionActuelle8", self)
                    



class Personne:

    pass


class C3:

    pass


class C2:

    pass


class R:

    pass


class Y:

    def __init__(self, attY: str):
        self.attY = attY
        
        pass
    @property
    def attY(self):
        return self.__attY
    @attY.setter
    def attY(self, attY: str):
        self.__attY = attY



class Z:

    pass


class C:

    def __init__(self, attC1: int, attC2: bool, b3: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b3 = b3
        
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
    def b3(self):
        return self.__b3
    @b3.setter
    def b3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b3", None)
        self.__b3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c2"):
                opp_val = getattr(old_value, "c2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c2"):
                opp_val = getattr(value, "c2", None)
                if opp_val is None:
                    setattr(value, "c2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B:

    def __init__(self, attB: int, a1: "A" = None, c2: set["C"] = None):
        self.attB = attB
        self.a1 = a1
        self.c2 = c2 if c2 is not None else set()
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def a1(self):
        return self.__a1
    @a1.setter
    def a1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__a1", None)
        self.__a1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b0"):
                opp_val = getattr(old_value, "b0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b0"):
                opp_val = getattr(value, "b0", None)
                if opp_val is None:
                    setattr(value, "b0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def c2(self):
        return self.__c2
    @c2.setter
    def c2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c2", None)
        self.__c2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b3"):
                    opp_val = getattr(item, "b3", None)
                    
                    if opp_val == self:
                        setattr(item, "b3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b3"):
                    opp_val = getattr(item, "b3", None)
                    
                    setattr(item, "b3", self)
                    

