from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Lieu:

    pass


class Sport:

    def __init__(self, id: int, nom: str, personne7: set["Personne"] = None, lieu10: set["Lieu"] = None):
        self.id = id
        self.nom = nom
        self.personne7 = personne7 if personne7 is not None else set()
        self.lieu10 = lieu10 if lieu10 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def lieu10(self):
        return self.__lieu10
    @lieu10.setter
    def lieu10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sport__lieu10", None)
        self.__lieu10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sport11"):
                    opp_val = getattr(item, "sport11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sport11"):
                    opp_val = getattr(item, "sport11", None)
                    
                    if opp_val is None:
                        setattr(item, "sport11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def personne7(self):
        return self.__personne7
    @personne7.setter
    def personne7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sport__personne7", None)
        self.__personne7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sport6"):
                    opp_val = getattr(item, "sport6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sport6"):
                    opp_val = getattr(item, "sport6", None)
                    
                    if opp_val is None:
                        setattr(item, "sport6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Personne:

    def __init__(self, id: int, nom: str, prenom: str, sport6: set["Sport"] = None, lieu9: set["Lieu"] = None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.sport6 = sport6 if sport6 is not None else set()
        self.lieu9 = lieu9 if lieu9 is not None else set()
        
        pass
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, prenom: str):
        self.__prenom = prenom

    @property
    def sport6(self):
        return self.__sport6
    @sport6.setter
    def sport6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personne__sport6", None)
        self.__sport6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "personne7"):
                    opp_val = getattr(item, "personne7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "personne7"):
                    opp_val = getattr(item, "personne7", None)
                    
                    if opp_val is None:
                        setattr(item, "personne7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def lieu9(self):
        return self.__lieu9
    @lieu9.setter
    def lieu9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personne__lieu9", None)
        self.__lieu9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "personne8"):
                    opp_val = getattr(item, "personne8", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "personne8"):
                    opp_val = getattr(item, "personne8", None)
                    
                    if opp_val is None:
                        setattr(item, "personne8", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class C3:

    pass


class C2:

    pass


class R:

    pass


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
                    



class A:

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
    def r3(self):
        return self.__r3
    @r3.setter
    def r3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__r3", None)
        self.__r3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a2"):
                opp_val = getattr(old_value, "a2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a2"):
                opp_val = getattr(value, "a2", None)
                if opp_val is None:
                    setattr(value, "a2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

