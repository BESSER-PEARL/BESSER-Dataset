from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Union1:

    def __init__(self, dateUnion: str, pers29: set["Personne"] = None, personne31: set["Personne"] = None):
        self.dateUnion = dateUnion
        self.pers29 = pers29 if pers29 is not None else set()
        self.personne31 = personne31 if personne31 is not None else set()
        
        pass
    @property
    def dateUnion(self):
        return self.__dateUnion
    @dateUnion.setter
    def dateUnion(self, dateUnion: str):
        self.__dateUnion = dateUnion

    @property
    def personne31(self):
        return self.__personne31
    @personne31.setter
    def personne31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Union1__personne31", None)
        self.__personne31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "unionActuelle30"):
                    opp_val = getattr(item, "unionActuelle30", None)
                    
                    if opp_val == self:
                        setattr(item, "unionActuelle30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "unionActuelle30"):
                    opp_val = getattr(item, "unionActuelle30", None)
                    
                    setattr(item, "unionActuelle30", self)
                    

    @property
    def pers29(self):
        return self.__pers29
    @pers29.setter
    def pers29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Union1__pers29", None)
        self.__pers29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "unions28"):
                    opp_val = getattr(item, "unions28", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "unions28"):
                    opp_val = getattr(item, "unions28", None)
                    
                    if opp_val is None:
                        setattr(item, "unions28", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class C5:

    def __init__(self, attC1: int, attC2: bool, b27: "B5" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b27 = b27
        
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
    def b27(self):
        return self.__b27
    @b27.setter
    def b27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C5__b27", None)
        self.__b27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c26"):
                opp_val = getattr(old_value, "c26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c26"):
                opp_val = getattr(value, "c26", None)
                if opp_val is None:
                    setattr(value, "c26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B5:

    def __init__(self, attB: int, a25: "A5" = None, c26: set["C5"] = None):
        self.attB = attB
        self.a25 = a25
        self.c26 = c26 if c26 is not None else set()
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def a25(self):
        return self.__a25
    @a25.setter
    def a25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B5__a25", None)
        self.__a25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b24"):
                opp_val = getattr(old_value, "b24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b24"):
                opp_val = getattr(value, "b24", None)
                if opp_val is None:
                    setattr(value, "b24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def c26(self):
        return self.__c26
    @c26.setter
    def c26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B5__c26", None)
        self.__c26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b27"):
                    opp_val = getattr(item, "b27", None)
                    
                    if opp_val == self:
                        setattr(item, "b27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b27"):
                    opp_val = getattr(item, "b27", None)
                    
                    setattr(item, "b27", self)
                    



class A5:

    def __init__(self, attA: str, b24: set["B5"] = None):
        self.attA = attA
        self.b24 = b24 if b24 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def b24(self):
        return self.__b24
    @b24.setter
    def b24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A5__b24", None)
        self.__b24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a25"):
                    opp_val = getattr(item, "a25", None)
                    
                    if opp_val == self:
                        setattr(item, "a25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a25"):
                    opp_val = getattr(item, "a25", None)
                    
                    setattr(item, "a25", self)
                    



class Mariage1:

    pass


class Personne:

    pass


class Union:

    pass


class Mariage:

    pass


class PACS:

    pass


class A31:

    pass


class A21:

    pass


class B21:

    pass


class C4:

    pass


class B3:

    pass


class A3:

    def __init__(self, b: bool, c: B, d: int, c16: "B3" = None, a219: "A21" = None):
        self.b = b
        self.c = c
        self.d = d
        self.c16 = c16
        self.a219 = a219
        
        pass
    @property
    def d(self):
        return self.__d
    @d.setter
    def d(self, d: int):
        self.__d = d

    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, b: bool):
        self.__b = b

    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, c: B):
        self.__c = c

    @property
    def c16(self):
        return self.__c16
    @c16.setter
    def c16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A3__c16", None)
        self.__c16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a17"):
                opp_val = getattr(old_value, "a17", None)
                if opp_val == self:
                    setattr(old_value, "a17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a17"):
                opp_val = getattr(value, "a17", None)
                setattr(value, "a17", self)

    @property
    def a219(self):
        return self.__a219
    @a219.setter
    def a219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A3__a219", None)
        self.__a219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a18"):
                opp_val = getattr(old_value, "a18", None)
                if opp_val == self:
                    setattr(old_value, "a18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a18"):
                opp_val = getattr(value, "a18", None)
                setattr(value, "a18", self)



class C3:

    pass


class C21:

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



class C1:

    def __init__(self, attC1: int, attC2: bool, b11: "B1" = None):
        self.attC1 = attC1
        self.attC2 = attC2
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



class B1:

    def __init__(self, attB: int, a15: "A1" = None, a9: "A1" = None, c10: set["C1"] = None):
        self.attB = attB
        self.a15 = a15
        self.a9 = a9
        self.c10 = c10 if c10 is not None else set()
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def a15(self):
        return self.__a15
    @a15.setter
    def a15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__a15", None)
        self.__a15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b14"):
                opp_val = getattr(old_value, "b14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b14"):
                opp_val = getattr(value, "b14", None)
                if opp_val is None:
                    setattr(value, "b14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def a9(self):
        return self.__a9
    @a9.setter
    def a9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__a9", None)
        self.__a9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b8"):
                opp_val = getattr(old_value, "b8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b8"):
                opp_val = getattr(value, "b8", None)
                if opp_val is None:
                    setattr(value, "b8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class A1:

    def __init__(self, attA: str, r13: "R" = None, b14: set["B1"] = None, b8: set["B1"] = None):
        self.attA = attA
        self.r13 = r13
        self.b14 = b14 if b14 is not None else set()
        self.b8 = b8 if b8 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def r13(self):
        return self.__r13
    @r13.setter
    def r13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__r13", None)
        self.__r13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aR12"):
                opp_val = getattr(old_value, "aR12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR12"):
                opp_val = getattr(value, "aR12", None)
                if opp_val is None:
                    setattr(value, "aR12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b8(self):
        return self.__b8
    @b8.setter
    def b8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__b8", None)
        self.__b8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a9"):
                    opp_val = getattr(item, "a9", None)
                    
                    if opp_val == self:
                        setattr(item, "a9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a9"):
                    opp_val = getattr(item, "a9", None)
                    
                    setattr(item, "a9", self)
                    

    @property
    def b14(self):
        return self.__b14
    @b14.setter
    def b14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__b14", None)
        self.__b14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a15"):
                    opp_val = getattr(item, "a15", None)
                    
                    if opp_val == self:
                        setattr(item, "a15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a15"):
                    opp_val = getattr(item, "a15", None)
                    
                    setattr(item, "a15", self)
                    



class C2:

    def __init__(self, attC1: int, attC2: bool, b7: "B2" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b7 = b7
        
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
    def b7(self):
        return self.__b7
    @b7.setter
    def b7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C2__b7", None)
        self.__b7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c6"):
                opp_val = getattr(old_value, "c6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c6"):
                opp_val = getattr(value, "c6", None)
                if opp_val is None:
                    setattr(value, "c6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B2:

    def __init__(self, attB: int, a5: "A2" = None, c6: set["C2"] = None):
        self.attB = attB
        self.a5 = a5
        self.c6 = c6 if c6 is not None else set()
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def c6(self):
        return self.__c6
    @c6.setter
    def c6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B2__c6", None)
        self.__c6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b7"):
                    opp_val = getattr(item, "b7", None)
                    
                    if opp_val == self:
                        setattr(item, "b7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b7"):
                    opp_val = getattr(item, "b7", None)
                    
                    setattr(item, "b7", self)
                    

    @property
    def a5(self):
        return self.__a5
    @a5.setter
    def a5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B2__a5", None)
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



class A2:

    def __init__(self, attA: str, b4: set["B2"] = None):
        self.attA = attA
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
        old_value = getattr(self, f"_A2__b4", None)
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
                    



class Interface_Interface:

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
                    

