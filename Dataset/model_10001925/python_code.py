from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class A:

    def __init__(self, attA: str, b0: set["B"] = None):
        self.attA = attA
        self.b0 = b0 if b0 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

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

    def __init__(self, attE: str, g21: "G" = None):
        self.attE = attE
        self.g21 = g21
        
        pass
    @property
    def attE(self):
        return self.__attE
    @attE.setter
    def attE(self, attE: str):
        self.__attE = attE

    @property
    def g21(self):
        return self.__g21
    @g21.setter
    def g21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_E__g21", None)
        self.__g21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e20"):
                opp_val = getattr(old_value, "e20", None)
                if opp_val == self:
                    setattr(old_value, "e20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e20"):
                opp_val = getattr(value, "e20", None)
                setattr(value, "e20", self)



class Date:

    pass


class PACS:

    pass


class Mariage:

    pass


class Union:

    def __init__(self, dateUnion: Date, pers17: set["Personne"] = None, personnes19: set["Personne"] = None):
        self.dateUnion = dateUnion
        self.pers17 = pers17 if pers17 is not None else set()
        self.personnes19 = personnes19 if personnes19 is not None else set()
        
        pass
    @property
    def dateUnion(self):
        return self.__dateUnion
    @dateUnion.setter
    def dateUnion(self, dateUnion: Date):
        self.__dateUnion = dateUnion

    @property
    def personnes19(self):
        return self.__personnes19
    @personnes19.setter
    def personnes19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Union__personnes19", None)
        self.__personnes19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "unionActuelle18"):
                    opp_val = getattr(item, "unionActuelle18", None)
                    
                    if opp_val == self:
                        setattr(item, "unionActuelle18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "unionActuelle18"):
                    opp_val = getattr(item, "unionActuelle18", None)
                    
                    setattr(item, "unionActuelle18", self)
                    

    @property
    def pers17(self):
        return self.__pers17
    @pers17.setter
    def pers17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Union__pers17", None)
        self.__pers17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "union16"):
                    opp_val = getattr(item, "union16", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "union16"):
                    opp_val = getattr(item, "union16", None)
                    
                    if opp_val is None:
                        setattr(item, "union16", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Personne:

    pass


class B21:

    pass


class A3:

    pass


class A21:

    def __init__(self, b: bool):
        self.b = b
        
        pass
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, b: bool):
        self.__b = b



class A2(ABC):

    def __init__(self, d: int, c12: "B2" = None):
        self.d = d
        self.c12 = c12
        
        pass
    @property
    def d(self):
        return self.__d
    @d.setter
    def d(self, d: int):
        self.__d = d

    @property
    def c12(self):
        return self.__c12
    @c12.setter
    def c12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A2__c12", None)
        self.__c12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a13"):
                opp_val = getattr(old_value, "a13", None)
                if opp_val == self:
                    setattr(old_value, "a13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a13"):
                opp_val = getattr(value, "a13", None)
                setattr(value, "a13", self)



class B2:

    pass


class B1:

    def __init__(self, attB: int, a7: "A1" = None, c8: "C1" = None, c10: set["C1"] = None):
        self.attB = attB
        self.a7 = a7
        self.c8 = c8
        self.c10 = c10 if c10 is not None else set()
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def c8(self):
        return self.__c8
    @c8.setter
    def c8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__c8", None)
        self.__c8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b9"):
                opp_val = getattr(old_value, "b9", None)
                if opp_val == self:
                    setattr(old_value, "b9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b9"):
                opp_val = getattr(value, "b9", None)
                setattr(value, "b9", self)

    @property
    def c10(self):
        return self.__c10
    @c10.setter
    def c10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__c10", None)
        self.__c10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b11"):
                    opp_val = getattr(item, "b11", None)
                    
                    if opp_val == self:
                        setattr(item, "b11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b11"):
                    opp_val = getattr(item, "b11", None)
                    
                    setattr(item, "b11", self)
                    

    @property
    def a7(self):
        return self.__a7
    @a7.setter
    def a7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__a7", None)
        self.__a7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b6"):
                opp_val = getattr(old_value, "b6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b6"):
                opp_val = getattr(value, "b6", None)
                if opp_val is None:
                    setattr(value, "b6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class C2:

    pass


class C11:

    pass


class C1(ABC):

    def __init__(self, attC1: int, attC2: bool, b9: "B1" = None, b11: "B1" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b9 = b9
        self.b11 = b11
        
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
    def b11(self):
        return self.__b11
    @b11.setter
    def b11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C1__b11", None)
        self.__b11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c10"):
                opp_val = getattr(old_value, "c10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c10"):
                opp_val = getattr(value, "c10", None)
                if opp_val is None:
                    setattr(value, "c10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b9(self):
        return self.__b9
    @b9.setter
    def b9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C1__b9", None)
        self.__b9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c8"):
                opp_val = getattr(old_value, "c8", None)
                if opp_val == self:
                    setattr(old_value, "c8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c8"):
                opp_val = getattr(value, "c8", None)
                setattr(value, "c8", self)



class Z:

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



class R:

    pass


class A1(ABC):

    def __init__(self, attA: str, r5: "R" = None, b6: set["B1"] = None):
        self.attA = attA
        self.r5 = r5
        self.b6 = b6 if b6 is not None else set()
        
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
        old_value = getattr(self, f"_A1__r5", None)
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
    def b6(self):
        return self.__b6
    @b6.setter
    def b6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__b6", None)
        self.__b6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a7"):
                    opp_val = getattr(item, "a7", None)
                    
                    if opp_val == self:
                        setattr(item, "a7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a7"):
                    opp_val = getattr(item, "a7", None)
                    
                    setattr(item, "a7", self)
                    



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

