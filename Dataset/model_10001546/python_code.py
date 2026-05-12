from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class G:

    pass


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



class PACS:

    pass


class Mariage:

    pass


class Union:

    def __init__(self, dateUnion: str, pers9: set["Personne"] = None, personne11: set["Personne"] = None):
        self.dateUnion = dateUnion
        self.pers9 = pers9 if pers9 is not None else set()
        self.personne11 = personne11 if personne11 is not None else set()
        
        pass
    @property
    def dateUnion(self):
        return self.__dateUnion
    @dateUnion.setter
    def dateUnion(self, dateUnion: str):
        self.__dateUnion = dateUnion

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
                    



class Personne:

    pass


class C3:

    pass


class C2:

    pass


class Z:

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

    def __init__(self, attB: int, c2: set["C"] = None, a5: "A" = None):
        self.attB = attB
        self.c2 = c2 if c2 is not None else set()
        self.a5 = a5
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

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
                    



class A:

    def __init__(self, attA: str, r1: "R" = None, b4: set["B"] = None):
        self.attA = attA
        self.r1 = r1
        self.b4 = b4 if b4 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

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
                    

    @property
    def r1(self):
        return self.__r1
    @r1.setter
    def r1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__r1", None)
        self.__r1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a0"):
                opp_val = getattr(old_value, "a0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a0"):
                opp_val = getattr(value, "a0", None)
                if opp_val is None:
                    setattr(value, "a0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

