from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

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

    def __init__(self, attE: str, g17: "G" = None):
        self.attE = attE
        self.g17 = g17
        
        pass
    @property
    def attE(self):
        return self.__attE
    @attE.setter
    def attE(self, attE: str):
        self.__attE = attE

    @property
    def g17(self):
        return self.__g17
    @g17.setter
    def g17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_E__g17", None)
        self.__g17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e16"):
                opp_val = getattr(old_value, "e16", None)
                if opp_val == self:
                    setattr(old_value, "e16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e16"):
                opp_val = getattr(value, "e16", None)
                setattr(value, "e16", self)



class Vehicule:

    def __init__(self, rang: int, standing: str, chauffeur12: "Chauffeur" = None, reservation15: "Reservation" = None):
        self.rang = rang
        self.standing = standing
        self.chauffeur12 = chauffeur12
        self.reservation15 = reservation15
        
        pass
    @property
    def standing(self):
        return self.__standing
    @standing.setter
    def standing(self, standing: str):
        self.__standing = standing

    @property
    def rang(self):
        return self.__rang
    @rang.setter
    def rang(self, rang: int):
        self.__rang = rang

    @property
    def reservation15(self):
        return self.__reservation15
    @reservation15.setter
    def reservation15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vehicule__reservation15", None)
        self.__reservation15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vehicule14"):
                opp_val = getattr(old_value, "vehicule14", None)
                if opp_val == self:
                    setattr(old_value, "vehicule14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vehicule14"):
                opp_val = getattr(value, "vehicule14", None)
                setattr(value, "vehicule14", self)

    @property
    def chauffeur12(self):
        return self.__chauffeur12
    @chauffeur12.setter
    def chauffeur12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vehicule__chauffeur12", None)
        self.__chauffeur12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vehicule13"):
                opp_val = getattr(old_value, "vehicule13", None)
                if opp_val == self:
                    setattr(old_value, "vehicule13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vehicule13"):
                opp_val = getattr(value, "vehicule13", None)
                setattr(value, "vehicule13", self)



class Permis:

    pass


class Reservation:

    pass


class Groupe:

    def __init__(self, rang: str, reservation8: "Reservation" = None, client7: set["Client"] = None):
        self.rang = rang
        self.reservation8 = reservation8
        self.client7 = client7 if client7 is not None else set()
        
        pass
    @property
    def rang(self):
        return self.__rang
    @rang.setter
    def rang(self, rang: str):
        self.__rang = rang

    @property
    def reservation8(self):
        return self.__reservation8
    @reservation8.setter
    def reservation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Groupe__reservation8", None)
        self.__reservation8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groupe9"):
                opp_val = getattr(old_value, "groupe9", None)
                if opp_val == self:
                    setattr(old_value, "groupe9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groupe9"):
                opp_val = getattr(value, "groupe9", None)
                setattr(value, "groupe9", self)

    @property
    def client7(self):
        return self.__client7
    @client7.setter
    def client7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Groupe__client7", None)
        self.__client7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "groupe6"):
                    opp_val = getattr(item, "groupe6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "groupe6"):
                    opp_val = getattr(item, "groupe6", None)
                    
                    if opp_val is None:
                        setattr(item, "groupe6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Chauffeur:

    def __init__(self, position: str, permis10: "Permis" = None, vehicule13: "Vehicule" = None):
        self.position = position
        self.permis10 = permis10
        self.vehicule13 = vehicule13
        
        pass
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def permis10(self):
        return self.__permis10
    @permis10.setter
    def permis10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Chauffeur__permis10", None)
        self.__permis10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chauffeur11"):
                opp_val = getattr(old_value, "chauffeur11", None)
                if opp_val == self:
                    setattr(old_value, "chauffeur11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chauffeur11"):
                opp_val = getattr(value, "chauffeur11", None)
                setattr(value, "chauffeur11", self)

    @property
    def vehicule13(self):
        return self.__vehicule13
    @vehicule13.setter
    def vehicule13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Chauffeur__vehicule13", None)
        self.__vehicule13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chauffeur12"):
                opp_val = getattr(old_value, "chauffeur12", None)
                if opp_val == self:
                    setattr(old_value, "chauffeur12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chauffeur12"):
                opp_val = getattr(value, "chauffeur12", None)
                setattr(value, "chauffeur12", self)



class Client:

    def __init__(self, fonction: str, nom: str, groupe6: set["Groupe"] = None):
        self.fonction = fonction
        self.nom = nom
        self.groupe6 = groupe6 if groupe6 is not None else set()
        
        pass
    @property
    def fonction(self):
        return self.__fonction
    @fonction.setter
    def fonction(self, fonction: str):
        self.__fonction = fonction

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def groupe6(self):
        return self.__groupe6
    @groupe6.setter
    def groupe6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Client__groupe6", None)
        self.__groupe6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "client7"):
                    opp_val = getattr(item, "client7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "client7"):
                    opp_val = getattr(item, "client7", None)
                    
                    if opp_val is None:
                        setattr(item, "client7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Z:

    pass


class B:

    def __init__(self, attb: str, c0: set["C"] = None, a3: "A" = None):
        self.attb = attb
        self.c0 = c0 if c0 is not None else set()
        self.a3 = a3
        
        pass
    @property
    def attb(self):
        return self.__attb
    @attb.setter
    def attb(self, attb: str):
        self.__attb = attb

    @property
    def a3(self):
        return self.__a3
    @a3.setter
    def a3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__a3", None)
        self.__a3 = value
        
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


class C2:

    pass


class Y:

    def __init__(self, atty: str):
        self.atty = atty
        
        pass
    @property
    def atty(self):
        return self.__atty
    @atty.setter
    def atty(self, atty: str):
        self.__atty = atty



class R:

    pass


class A(ABC):

    def __init__(self, atta: str, b2: set["B"] = None, r5: "R" = None):
        self.atta = atta
        self.b2 = b2 if b2 is not None else set()
        self.r5 = r5
        
        pass
    @property
    def atta(self):
        return self.__atta
    @atta.setter
    def atta(self, atta: str):
        self.__atta = atta

    @property
    def b2(self):
        return self.__b2
    @b2.setter
    def b2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b2", None)
        self.__b2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a3"):
                    opp_val = getattr(item, "a3", None)
                    
                    if opp_val == self:
                        setattr(item, "a3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a3"):
                    opp_val = getattr(item, "a3", None)
                    
                    setattr(item, "a3", self)
                    

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



class C(ABC):

    def __init__(self, attc1: int, attc2: bool, b1: "B" = None):
        self.attc1 = attc1
        self.attc2 = attc2
        self.b1 = b1
        
        pass
    @property
    def attc2(self):
        return self.__attc2
    @attc2.setter
    def attc2(self, attc2: bool):
        self.__attc2 = attc2

    @property
    def attc1(self):
        return self.__attc1
    @attc1.setter
    def attc1(self, attc1: int):
        self.__attc1 = attc1

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

