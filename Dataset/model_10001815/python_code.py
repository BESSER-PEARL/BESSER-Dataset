from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class C2:

    pass


class C11:

    pass


class C1:

    def __init__(self, attC2: bool, attC1: int):
        self.attC2 = attC2
        self.attC1 = attC1
        
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



class B1:

    def __init__(self, attB: int):
        self.attB = attB
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB



class Z:

    pass


class A1:

    def __init__(self, attA: str):
        self.attA = attA
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA



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

    def __init__(self, attC1: int, attC2: bool, b9: "B" = None):
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
        old_value = getattr(self, f"_C__b9", None)
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



class B:

    def __init__(self, attB: int, a7: "A" = None, c8: set["C"] = None):
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
        old_value = getattr(self, f"_B__c8", None)
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
        old_value = getattr(self, f"_B__a7", None)
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



class A:

    def __init__(self, attA: str, b6: set["B"] = None):
        self.attA = attA
        self.b6 = b6 if b6 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def b6(self):
        return self.__b6
    @b6.setter
    def b6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b6", None)
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
                    



class RESERVATION:

    pass


class CHAUFFEUR:

    def __init__(self, nomPersonnel: str, prenomPersonnel: str, pERMIS0: set["PERMIS"] = None, rESERVATION4: set["RESERVATION"] = None):
        self.nomPersonnel = nomPersonnel
        self.prenomPersonnel = prenomPersonnel
        self.pERMIS0 = pERMIS0 if pERMIS0 is not None else set()
        self.rESERVATION4 = rESERVATION4 if rESERVATION4 is not None else set()
        
        pass
    @property
    def prenomPersonnel(self):
        return self.__prenomPersonnel
    @prenomPersonnel.setter
    def prenomPersonnel(self, prenomPersonnel: str):
        self.__prenomPersonnel = prenomPersonnel

    @property
    def nomPersonnel(self):
        return self.__nomPersonnel
    @nomPersonnel.setter
    def nomPersonnel(self, nomPersonnel: str):
        self.__nomPersonnel = nomPersonnel

    @property
    def pERMIS0(self):
        return self.__pERMIS0
    @pERMIS0.setter
    def pERMIS0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CHAUFFEUR__pERMIS0", None)
        self.__pERMIS0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cHAUFFEUR1"):
                    opp_val = getattr(item, "cHAUFFEUR1", None)
                    
                    if opp_val == self:
                        setattr(item, "cHAUFFEUR1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cHAUFFEUR1"):
                    opp_val = getattr(item, "cHAUFFEUR1", None)
                    
                    setattr(item, "cHAUFFEUR1", self)
                    

    @property
    def rESERVATION4(self):
        return self.__rESERVATION4
    @rESERVATION4.setter
    def rESERVATION4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CHAUFFEUR__rESERVATION4", None)
        self.__rESERVATION4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cHAUFFEUR5"):
                    opp_val = getattr(item, "cHAUFFEUR5", None)
                    
                    if opp_val == self:
                        setattr(item, "cHAUFFEUR5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cHAUFFEUR5"):
                    opp_val = getattr(item, "cHAUFFEUR5", None)
                    
                    setattr(item, "cHAUFFEUR5", self)
                    



class PERMIS:

    def __init__(self, libPermis: str, cHAUFFEUR1: "CHAUFFEUR" = None):
        self.libPermis = libPermis
        self.cHAUFFEUR1 = cHAUFFEUR1
        
        pass
    @property
    def libPermis(self):
        return self.__libPermis
    @libPermis.setter
    def libPermis(self, libPermis: str):
        self.__libPermis = libPermis

    @property
    def cHAUFFEUR1(self):
        return self.__cHAUFFEUR1
    @cHAUFFEUR1.setter
    def cHAUFFEUR1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PERMIS__cHAUFFEUR1", None)
        self.__cHAUFFEUR1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pERMIS0"):
                opp_val = getattr(old_value, "pERMIS0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pERMIS0"):
                opp_val = getattr(value, "pERMIS0", None)
                if opp_val is None:
                    setattr(value, "pERMIS0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class PERSONNEL:

    def __init__(self, nomPersonnel: str, prenomPersonnel: str, unPrivate: bool, rESERVATION2: set["RESERVATION"] = None):
        self.nomPersonnel = nomPersonnel
        self.prenomPersonnel = prenomPersonnel
        self.unPrivate = unPrivate
        self.rESERVATION2 = rESERVATION2 if rESERVATION2 is not None else set()
        
        pass
    @property
    def prenomPersonnel(self):
        return self.__prenomPersonnel
    @prenomPersonnel.setter
    def prenomPersonnel(self, prenomPersonnel: str):
        self.__prenomPersonnel = prenomPersonnel

    @property
    def unPrivate(self):
        return self.__unPrivate
    @unPrivate.setter
    def unPrivate(self, unPrivate: bool):
        self.__unPrivate = unPrivate

    @property
    def nomPersonnel(self):
        return self.__nomPersonnel
    @nomPersonnel.setter
    def nomPersonnel(self, nomPersonnel: str):
        self.__nomPersonnel = nomPersonnel

    @property
    def rESERVATION2(self):
        return self.__rESERVATION2
    @rESERVATION2.setter
    def rESERVATION2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PERSONNEL__rESERVATION2", None)
        self.__rESERVATION2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pERSONNEL3"):
                    opp_val = getattr(item, "pERSONNEL3", None)
                    
                    if opp_val == self:
                        setattr(item, "pERSONNEL3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pERSONNEL3"):
                    opp_val = getattr(item, "pERSONNEL3", None)
                    
                    setattr(item, "pERSONNEL3", self)
                    

