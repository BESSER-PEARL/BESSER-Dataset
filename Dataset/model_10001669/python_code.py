from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################










class Vol:

    def __init__(self, numeroVol: str, etatVol: Enumeration, dateHeureDepart: str, dateHeureArrivee: str):
        self.numeroVol = numeroVol
        self.etatVol = etatVol
        self.dateHeureDepart = dateHeureDepart
        self.dateHeureArrivee = dateHeureArrivee
        
        pass
    @property
    def dateHeureArrivee(self):
        return self.__dateHeureArrivee
    @dateHeureArrivee.setter
    def dateHeureArrivee(self, dateHeureArrivee: str):
        self.__dateHeureArrivee = dateHeureArrivee

    @property
    def etatVol(self):
        return self.__etatVol
    @etatVol.setter
    def etatVol(self, etatVol: Enumeration):
        self.__etatVol = etatVol

    @property
    def dateHeureDepart(self):
        return self.__dateHeureDepart
    @dateHeureDepart.setter
    def dateHeureDepart(self, dateHeureDepart: str):
        self.__dateHeureDepart = dateHeureDepart

    @property
    def numeroVol(self):
        return self.__numeroVol
    @numeroVol.setter
    def numeroVol(self, numeroVol: str):
        self.__numeroVol = numeroVol



class Aeroport:

    def __init__(self, nomAeroport: str, altitude: int):
        self.nomAeroport = nomAeroport
        self.altitude = altitude
        
        pass
    @property
    def altitude(self):
        return self.__altitude
    @altitude.setter
    def altitude(self, altitude: int):
        self.__altitude = altitude

    @property
    def nomAeroport(self):
        return self.__nomAeroport
    @nomAeroport.setter
    def nomAeroport(self, nomAeroport: str):
        self.__nomAeroport = nomAeroport



class C:

    def __init__(self, attC1: int, attC2: bool):
        self.attC1 = attC1
        self.attC2 = attC2
        
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



class B:

    def __init__(self, attB: int, a1: "A" = None):
        self.attB = attB
        self.a1 = a1
        
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
                if opp_val == self:
                    setattr(old_value, "b0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b0"):
                opp_val = getattr(value, "b0", None)
                setattr(value, "b0", self)



class A:

    def __init__(self, attA: str, b0: "B" = None):
        self.attA = attA
        self.b0 = b0
        
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
        self.__b0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a1"):
                opp_val = getattr(old_value, "a1", None)
                if opp_val == self:
                    setattr(old_value, "a1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a1"):
                opp_val = getattr(value, "a1", None)
                setattr(value, "a1", self)

