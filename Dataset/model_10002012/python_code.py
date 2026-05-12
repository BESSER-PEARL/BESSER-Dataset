from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class C33:

    pass


class C23:

    pass


class C5:

    def __init__(self, attC1: int, attC2: bool, b25: "B4" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b25 = b25
        
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
    def b25(self):
        return self.__b25
    @b25.setter
    def b25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C5__b25", None)
        self.__b25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c24"):
                opp_val = getattr(old_value, "c24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c24"):
                opp_val = getattr(value, "c24", None)
                if opp_val is None:
                    setattr(value, "c24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B4:

    def __init__(self, attB: int, a23: "A4" = None, c24: set["C5"] = None):
        self.attB = attB
        self.a23 = a23
        self.c24 = c24 if c24 is not None else set()
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def c24(self):
        return self.__c24
    @c24.setter
    def c24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B4__c24", None)
        self.__c24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b25"):
                    opp_val = getattr(item, "b25", None)
                    
                    if opp_val == self:
                        setattr(item, "b25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b25"):
                    opp_val = getattr(item, "b25", None)
                    
                    setattr(item, "b25", self)
                    

    @property
    def a23(self):
        return self.__a23
    @a23.setter
    def a23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B4__a23", None)
        self.__a23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b22"):
                opp_val = getattr(old_value, "b22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b22"):
                opp_val = getattr(value, "b22", None)
                if opp_val is None:
                    setattr(value, "b22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Z3:

    pass


class A4:

    def __init__(self, attA: str, r21: "R3" = None, b22: set["B4"] = None):
        self.attA = attA
        self.r21 = r21
        self.b22 = b22 if b22 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def r21(self):
        return self.__r21
    @r21.setter
    def r21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A4__r21", None)
        self.__r21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aR20"):
                opp_val = getattr(old_value, "aR20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR20"):
                opp_val = getattr(value, "aR20", None)
                if opp_val is None:
                    setattr(value, "aR20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b22(self):
        return self.__b22
    @b22.setter
    def b22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A4__b22", None)
        self.__b22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a23"):
                    opp_val = getattr(item, "a23", None)
                    
                    if opp_val == self:
                        setattr(item, "a23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a23"):
                    opp_val = getattr(item, "a23", None)
                    
                    setattr(item, "a23", self)
                    



class R3:

    pass


class Y3:

    def __init__(self, attY: str):
        self.attY = attY
        
        pass
    @property
    def attY(self):
        return self.__attY
    @attY.setter
    def attY(self, attY: str):
        self.__attY = attY



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

    def __init__(self, attE: str, g19: "G" = None):
        self.attE = attE
        self.g19 = g19
        
        pass
    @property
    def attE(self):
        return self.__attE
    @attE.setter
    def attE(self, attE: str):
        self.__attE = attE

    @property
    def g19(self):
        return self.__g19
    @g19.setter
    def g19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_E__g19", None)
        self.__g19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e18"):
                opp_val = getattr(old_value, "e18", None)
                if opp_val == self:
                    setattr(old_value, "e18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e18"):
                opp_val = getattr(value, "e18", None)
                setattr(value, "e18", self)



class Mariage:

    pass


class PACS:

    pass


class Union:

    def __init__(self, dateUnion: str, personnes15: set["Personne"] = None, personnes17: set["Personne"] = None):
        self.dateUnion = dateUnion
        self.personnes15 = personnes15 if personnes15 is not None else set()
        self.personnes17 = personnes17 if personnes17 is not None else set()
        
        pass
    @property
    def dateUnion(self):
        return self.__dateUnion
    @dateUnion.setter
    def dateUnion(self, dateUnion: str):
        self.__dateUnion = dateUnion

    @property
    def personnes17(self):
        return self.__personnes17
    @personnes17.setter
    def personnes17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Union__personnes17", None)
        self.__personnes17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "unionActuelle16"):
                    opp_val = getattr(item, "unionActuelle16", None)
                    
                    if opp_val == self:
                        setattr(item, "unionActuelle16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "unionActuelle16"):
                    opp_val = getattr(item, "unionActuelle16", None)
                    
                    setattr(item, "unionActuelle16", self)
                    

    @property
    def personnes15(self):
        return self.__personnes15
    @personnes15.setter
    def personnes15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Union__personnes15", None)
        self.__personnes15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "union14"):
                    opp_val = getattr(item, "union14", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "union14"):
                    opp_val = getattr(item, "union14", None)
                    
                    if opp_val is None:
                        setattr(item, "union14", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Personne:

    pass


class B21:

    pass


class B2:

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



class A2:

    def __init__(self, d: int, c10: "B2" = None):
        self.d = d
        self.c10 = c10
        
        pass
    @property
    def d(self):
        return self.__d
    @d.setter
    def d(self, d: int):
        self.__d = d

    @property
    def c10(self):
        return self.__c10
    @c10.setter
    def c10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A2__c10", None)
        self.__c10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "A_B3_111"):
                opp_val = getattr(old_value, "A_B3_111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "A_B3_111"):
                opp_val = getattr(value, "A_B3_111", None)
                if opp_val is None:
                    setattr(value, "A_B3_111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class C3:

    pass


class C2:

    pass


class C1:

    def __init__(self, attC1: int, attC2: bool, b9: "B1" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b9 = b9
        
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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c8"):
                opp_val = getattr(value, "c8", None)
                if opp_val is None:
                    setattr(value, "c8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B1:

    def __init__(self, attB: int, a7: "A1" = None, c8: set["C1"] = None):
        self.attB = attB
        self.a7 = a7
        self.c8 = c8 if c8 is not None else set()
        
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
        self.__c8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b9"):
                    opp_val = getattr(item, "b9", None)
                    
                    if opp_val == self:
                        setattr(item, "b9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b9"):
                    opp_val = getattr(item, "b9", None)
                    
                    setattr(item, "b9", self)
                    

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



class Z:

    pass


class A1:

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
                    

