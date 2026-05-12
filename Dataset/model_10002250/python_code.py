from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Zdravstveni_karton:

    def __init__(self, BrKart: int, pregled2: "Pregled" = None):
        self.BrKart = BrKart
        self.pregled2 = pregled2
        
        pass
    @property
    def BrKart(self):
        return self.__BrKart
    @BrKart.setter
    def BrKart(self, BrKart: int):
        self.__BrKart = BrKart

    @property
    def pregled2(self):
        return self.__pregled2
    @pregled2.setter
    def pregled2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Zdravstveni_karton__pregled2", None)
        self.__pregled2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zdravstveni_karton3"):
                opp_val = getattr(old_value, "zdravstveni_karton3", None)
                if opp_val == self:
                    setattr(old_value, "zdravstveni_karton3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zdravstveni_karton3"):
                opp_val = getattr(value, "zdravstveni_karton3", None)
                setattr(value, "zdravstveni_karton3", self)



class Pregled:

    def __init__(self, BrPregled: int, DatumP: str, lekar1: set["Lekar"] = None, zdravstveni_karton3: "Zdravstveni_karton" = None):
        self.BrPregled = BrPregled
        self.DatumP = DatumP
        self.lekar1 = lekar1 if lekar1 is not None else set()
        self.zdravstveni_karton3 = zdravstveni_karton3
        
        pass
    @property
    def BrPregled(self):
        return self.__BrPregled
    @BrPregled.setter
    def BrPregled(self, BrPregled: int):
        self.__BrPregled = BrPregled

    @property
    def DatumP(self):
        return self.__DatumP
    @DatumP.setter
    def DatumP(self, DatumP: str):
        self.__DatumP = DatumP

    @property
    def lekar1(self):
        return self.__lekar1
    @lekar1.setter
    def lekar1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pregled__lekar1", None)
        self.__lekar1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pregled0"):
                    opp_val = getattr(item, "pregled0", None)
                    
                    if opp_val == self:
                        setattr(item, "pregled0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pregled0"):
                    opp_val = getattr(item, "pregled0", None)
                    
                    setattr(item, "pregled0", self)
                    

    @property
    def zdravstveni_karton3(self):
        return self.__zdravstveni_karton3
    @zdravstveni_karton3.setter
    def zdravstveni_karton3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pregled__zdravstveni_karton3", None)
        self.__zdravstveni_karton3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pregled2"):
                opp_val = getattr(old_value, "pregled2", None)
                if opp_val == self:
                    setattr(old_value, "pregled2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pregled2"):
                opp_val = getattr(value, "pregled2", None)
                setattr(value, "pregled2", self)



class Lekar:

    def __init__(self, Zaposleni_ID: str, ImeZap: str, PrzZap: str, AdrZap: str, BrTelZap: str, Fakultet: str, DatZavSk: str, RadStaz: int, pregled0: "Pregled" = None):
        self.Zaposleni_ID = Zaposleni_ID
        self.ImeZap = ImeZap
        self.PrzZap = PrzZap
        self.AdrZap = AdrZap
        self.BrTelZap = BrTelZap
        self.Fakultet = Fakultet
        self.DatZavSk = DatZavSk
        self.RadStaz = RadStaz
        self.pregled0 = pregled0
        
        pass
    @property
    def AdrZap(self):
        return self.__AdrZap
    @AdrZap.setter
    def AdrZap(self, AdrZap: str):
        self.__AdrZap = AdrZap

    @property
    def PrzZap(self):
        return self.__PrzZap
    @PrzZap.setter
    def PrzZap(self, PrzZap: str):
        self.__PrzZap = PrzZap

    @property
    def ImeZap(self):
        return self.__ImeZap
    @ImeZap.setter
    def ImeZap(self, ImeZap: str):
        self.__ImeZap = ImeZap

    @property
    def BrTelZap(self):
        return self.__BrTelZap
    @BrTelZap.setter
    def BrTelZap(self, BrTelZap: str):
        self.__BrTelZap = BrTelZap

    @property
    def Fakultet(self):
        return self.__Fakultet
    @Fakultet.setter
    def Fakultet(self, Fakultet: str):
        self.__Fakultet = Fakultet

    @property
    def RadStaz(self):
        return self.__RadStaz
    @RadStaz.setter
    def RadStaz(self, RadStaz: int):
        self.__RadStaz = RadStaz

    @property
    def DatZavSk(self):
        return self.__DatZavSk
    @DatZavSk.setter
    def DatZavSk(self, DatZavSk: str):
        self.__DatZavSk = DatZavSk

    @property
    def Zaposleni_ID(self):
        return self.__Zaposleni_ID
    @Zaposleni_ID.setter
    def Zaposleni_ID(self, Zaposleni_ID: str):
        self.__Zaposleni_ID = Zaposleni_ID

    @property
    def pregled0(self):
        return self.__pregled0
    @pregled0.setter
    def pregled0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lekar__pregled0", None)
        self.__pregled0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lekar1"):
                opp_val = getattr(old_value, "lekar1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lekar1"):
                opp_val = getattr(value, "lekar1", None)
                if opp_val is None:
                    setattr(value, "lekar1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

