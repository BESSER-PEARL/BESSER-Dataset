from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Transakcija:

    def __init__(self, Trans_ID: str, datum_trans: str, tip: str, suma: str, Transakcija_Kupac_04: set["Kupac"] = None):
        self.Trans_ID = Trans_ID
        self.datum_trans = datum_trans
        self.tip = tip
        self.suma = suma
        self.Transakcija_Kupac_04 = Transakcija_Kupac_04 if Transakcija_Kupac_04 is not None else set()
        
        pass
    @property
    def suma(self):
        return self.__suma
    @suma.setter
    def suma(self, suma: str):
        self.__suma = suma

    @property
    def datum_trans(self):
        return self.__datum_trans
    @datum_trans.setter
    def datum_trans(self, datum_trans: str):
        self.__datum_trans = datum_trans

    @property
    def tip(self):
        return self.__tip
    @tip.setter
    def tip(self, tip: str):
        self.__tip = tip

    @property
    def Trans_ID(self):
        return self.__Trans_ID
    @Trans_ID.setter
    def Trans_ID(self, Trans_ID: str):
        self.__Trans_ID = Trans_ID

    @property
    def Transakcija_Kupac_04(self):
        return self.__Transakcija_Kupac_04
    @Transakcija_Kupac_04.setter
    def Transakcija_Kupac_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transakcija__Transakcija_Kupac_04", None)
        self.__Transakcija_Kupac_04 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transakcija_Kupac_15"):
                    opp_val = getattr(item, "Transakcija_Kupac_15", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transakcija_Kupac_15"):
                    opp_val = getattr(item, "Transakcija_Kupac_15", None)
                    
                    if opp_val is None:
                        setattr(item, "Transakcija_Kupac_15", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Kupac:

    def __init__(self, Kupac_ID: str, Ime: str, Prezime: str, JMBG: int, BrojPasosa: int, Mobilni: int, Grad: str, Osiguranje_Putnik_11: "Osiguranje" = None, Putnik_Rezervisanje_02: set["Aran_man"] = None, Transakcija_Kupac_15: set["Transakcija"] = None, Agent_Kupac_17: "Agent" = None):
        self.Kupac_ID = Kupac_ID
        self.Ime = Ime
        self.Prezime = Prezime
        self.JMBG = JMBG
        self.BrojPasosa = BrojPasosa
        self.Mobilni = Mobilni
        self.Grad = Grad
        self.Osiguranje_Putnik_11 = Osiguranje_Putnik_11
        self.Putnik_Rezervisanje_02 = Putnik_Rezervisanje_02 if Putnik_Rezervisanje_02 is not None else set()
        self.Transakcija_Kupac_15 = Transakcija_Kupac_15 if Transakcija_Kupac_15 is not None else set()
        self.Agent_Kupac_17 = Agent_Kupac_17
        
        pass
    @property
    def BrojPasosa(self):
        return self.__BrojPasosa
    @BrojPasosa.setter
    def BrojPasosa(self, BrojPasosa: int):
        self.__BrojPasosa = BrojPasosa

    @property
    def Mobilni(self):
        return self.__Mobilni
    @Mobilni.setter
    def Mobilni(self, Mobilni: int):
        self.__Mobilni = Mobilni

    @property
    def Ime(self):
        return self.__Ime
    @Ime.setter
    def Ime(self, Ime: str):
        self.__Ime = Ime

    @property
    def Grad(self):
        return self.__Grad
    @Grad.setter
    def Grad(self, Grad: str):
        self.__Grad = Grad

    @property
    def Prezime(self):
        return self.__Prezime
    @Prezime.setter
    def Prezime(self, Prezime: str):
        self.__Prezime = Prezime

    @property
    def JMBG(self):
        return self.__JMBG
    @JMBG.setter
    def JMBG(self, JMBG: int):
        self.__JMBG = JMBG

    @property
    def Kupac_ID(self):
        return self.__Kupac_ID
    @Kupac_ID.setter
    def Kupac_ID(self, Kupac_ID: str):
        self.__Kupac_ID = Kupac_ID

    @property
    def Transakcija_Kupac_15(self):
        return self.__Transakcija_Kupac_15
    @Transakcija_Kupac_15.setter
    def Transakcija_Kupac_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kupac__Transakcija_Kupac_15", None)
        self.__Transakcija_Kupac_15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transakcija_Kupac_04"):
                    opp_val = getattr(item, "Transakcija_Kupac_04", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transakcija_Kupac_04"):
                    opp_val = getattr(item, "Transakcija_Kupac_04", None)
                    
                    if opp_val is None:
                        setattr(item, "Transakcija_Kupac_04", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Agent_Kupac_17(self):
        return self.__Agent_Kupac_17
    @Agent_Kupac_17.setter
    def Agent_Kupac_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kupac__Agent_Kupac_17", None)
        self.__Agent_Kupac_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Agent_Kupac_06"):
                opp_val = getattr(old_value, "Agent_Kupac_06", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Agent_Kupac_06"):
                opp_val = getattr(value, "Agent_Kupac_06", None)
                if opp_val is None:
                    setattr(value, "Agent_Kupac_06", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Putnik_Rezervisanje_02(self):
        return self.__Putnik_Rezervisanje_02
    @Putnik_Rezervisanje_02.setter
    def Putnik_Rezervisanje_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kupac__Putnik_Rezervisanje_02", None)
        self.__Putnik_Rezervisanje_02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Putnik_Rezervisanje_13"):
                    opp_val = getattr(item, "Putnik_Rezervisanje_13", None)
                    
                    if opp_val == self:
                        setattr(item, "Putnik_Rezervisanje_13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Putnik_Rezervisanje_13"):
                    opp_val = getattr(item, "Putnik_Rezervisanje_13", None)
                    
                    setattr(item, "Putnik_Rezervisanje_13", self)
                    

    @property
    def Osiguranje_Putnik_11(self):
        return self.__Osiguranje_Putnik_11
    @Osiguranje_Putnik_11.setter
    def Osiguranje_Putnik_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kupac__Osiguranje_Putnik_11", None)
        self.__Osiguranje_Putnik_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Osiguranje_Putnik_00"):
                opp_val = getattr(old_value, "Osiguranje_Putnik_00", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Osiguranje_Putnik_00"):
                opp_val = getattr(value, "Osiguranje_Putnik_00", None)
                if opp_val is None:
                    setattr(value, "Osiguranje_Putnik_00", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Osiguranje:

    def __init__(self, Osiguranje_ID: str, OsigKuca: str, PaketPokri_a: str, BrojPolise: int, Cena: str, Osiguranje_Putnik_00: set["Kupac"] = None):
        self.Osiguranje_ID = Osiguranje_ID
        self.OsigKuca = OsigKuca
        self.PaketPokri_a = PaketPokri_a
        self.BrojPolise = BrojPolise
        self.Cena = Cena
        self.Osiguranje_Putnik_00 = Osiguranje_Putnik_00 if Osiguranje_Putnik_00 is not None else set()
        
        pass
    @property
    def Cena(self):
        return self.__Cena
    @Cena.setter
    def Cena(self, Cena: str):
        self.__Cena = Cena

    @property
    def BrojPolise(self):
        return self.__BrojPolise
    @BrojPolise.setter
    def BrojPolise(self, BrojPolise: int):
        self.__BrojPolise = BrojPolise

    @property
    def OsigKuca(self):
        return self.__OsigKuca
    @OsigKuca.setter
    def OsigKuca(self, OsigKuca: str):
        self.__OsigKuca = OsigKuca

    @property
    def Osiguranje_ID(self):
        return self.__Osiguranje_ID
    @Osiguranje_ID.setter
    def Osiguranje_ID(self, Osiguranje_ID: str):
        self.__Osiguranje_ID = Osiguranje_ID

    @property
    def PaketPokri_a(self):
        return self.__PaketPokri_a
    @PaketPokri_a.setter
    def PaketPokri_a(self, PaketPokri_a: str):
        self.__PaketPokri_a = PaketPokri_a

    @property
    def Osiguranje_Putnik_00(self):
        return self.__Osiguranje_Putnik_00
    @Osiguranje_Putnik_00.setter
    def Osiguranje_Putnik_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Osiguranje__Osiguranje_Putnik_00", None)
        self.__Osiguranje_Putnik_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Osiguranje_Putnik_11"):
                    opp_val = getattr(item, "Osiguranje_Putnik_11", None)
                    
                    if opp_val == self:
                        setattr(item, "Osiguranje_Putnik_11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Osiguranje_Putnik_11"):
                    opp_val = getattr(item, "Osiguranje_Putnik_11", None)
                    
                    setattr(item, "Osiguranje_Putnik_11", self)
                    



class Aran_man:

    def __init__(self, Aranzman_ID: str, NazivAran_: str, SlobMesto: bool, DatumPolaska: str, DatumPovratka: str, Cena: str, Putnik_Rezervisanje_13: "Kupac" = None, Agent_Aran_man_19: set["Agent"] = None):
        self.Aranzman_ID = Aranzman_ID
        self.NazivAran_ = NazivAran_
        self.SlobMesto = SlobMesto
        self.DatumPolaska = DatumPolaska
        self.DatumPovratka = DatumPovratka
        self.Cena = Cena
        self.Putnik_Rezervisanje_13 = Putnik_Rezervisanje_13
        self.Agent_Aran_man_19 = Agent_Aran_man_19 if Agent_Aran_man_19 is not None else set()
        
        pass
    @property
    def SlobMesto(self):
        return self.__SlobMesto
    @SlobMesto.setter
    def SlobMesto(self, SlobMesto: bool):
        self.__SlobMesto = SlobMesto

    @property
    def Aranzman_ID(self):
        return self.__Aranzman_ID
    @Aranzman_ID.setter
    def Aranzman_ID(self, Aranzman_ID: str):
        self.__Aranzman_ID = Aranzman_ID

    @property
    def NazivAran_(self):
        return self.__NazivAran_
    @NazivAran_.setter
    def NazivAran_(self, NazivAran_: str):
        self.__NazivAran_ = NazivAran_

    @property
    def Cena(self):
        return self.__Cena
    @Cena.setter
    def Cena(self, Cena: str):
        self.__Cena = Cena

    @property
    def DatumPovratka(self):
        return self.__DatumPovratka
    @DatumPovratka.setter
    def DatumPovratka(self, DatumPovratka: str):
        self.__DatumPovratka = DatumPovratka

    @property
    def DatumPolaska(self):
        return self.__DatumPolaska
    @DatumPolaska.setter
    def DatumPolaska(self, DatumPolaska: str):
        self.__DatumPolaska = DatumPolaska

    @property
    def Putnik_Rezervisanje_13(self):
        return self.__Putnik_Rezervisanje_13
    @Putnik_Rezervisanje_13.setter
    def Putnik_Rezervisanje_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aran_man__Putnik_Rezervisanje_13", None)
        self.__Putnik_Rezervisanje_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Putnik_Rezervisanje_02"):
                opp_val = getattr(old_value, "Putnik_Rezervisanje_02", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Putnik_Rezervisanje_02"):
                opp_val = getattr(value, "Putnik_Rezervisanje_02", None)
                if opp_val is None:
                    setattr(value, "Putnik_Rezervisanje_02", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Agent_Aran_man_19(self):
        return self.__Agent_Aran_man_19
    @Agent_Aran_man_19.setter
    def Agent_Aran_man_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aran_man__Agent_Aran_man_19", None)
        self.__Agent_Aran_man_19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Agent_Aran_man_08"):
                    opp_val = getattr(item, "Agent_Aran_man_08", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Agent_Aran_man_08"):
                    opp_val = getattr(item, "Agent_Aran_man_08", None)
                    
                    if opp_val is None:
                        setattr(item, "Agent_Aran_man_08", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Agent:

    def __init__(self, Agent_ID: str, Ime: str, Prezime: str, BrojAgenta: int, JMBG: int, Agent_Kupac_06: set["Kupac"] = None, Agent_Aran_man_08: set["Aran_man"] = None):
        self.Agent_ID = Agent_ID
        self.Ime = Ime
        self.Prezime = Prezime
        self.BrojAgenta = BrojAgenta
        self.JMBG = JMBG
        self.Agent_Kupac_06 = Agent_Kupac_06 if Agent_Kupac_06 is not None else set()
        self.Agent_Aran_man_08 = Agent_Aran_man_08 if Agent_Aran_man_08 is not None else set()
        
        pass
    @property
    def Agent_ID(self):
        return self.__Agent_ID
    @Agent_ID.setter
    def Agent_ID(self, Agent_ID: str):
        self.__Agent_ID = Agent_ID

    @property
    def JMBG(self):
        return self.__JMBG
    @JMBG.setter
    def JMBG(self, JMBG: int):
        self.__JMBG = JMBG

    @property
    def Prezime(self):
        return self.__Prezime
    @Prezime.setter
    def Prezime(self, Prezime: str):
        self.__Prezime = Prezime

    @property
    def Ime(self):
        return self.__Ime
    @Ime.setter
    def Ime(self, Ime: str):
        self.__Ime = Ime

    @property
    def BrojAgenta(self):
        return self.__BrojAgenta
    @BrojAgenta.setter
    def BrojAgenta(self, BrojAgenta: int):
        self.__BrojAgenta = BrojAgenta

    @property
    def Agent_Aran_man_08(self):
        return self.__Agent_Aran_man_08
    @Agent_Aran_man_08.setter
    def Agent_Aran_man_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Agent__Agent_Aran_man_08", None)
        self.__Agent_Aran_man_08 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Agent_Aran_man_19"):
                    opp_val = getattr(item, "Agent_Aran_man_19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Agent_Aran_man_19"):
                    opp_val = getattr(item, "Agent_Aran_man_19", None)
                    
                    if opp_val is None:
                        setattr(item, "Agent_Aran_man_19", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Agent_Kupac_06(self):
        return self.__Agent_Kupac_06
    @Agent_Kupac_06.setter
    def Agent_Kupac_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Agent__Agent_Kupac_06", None)
        self.__Agent_Kupac_06 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Agent_Kupac_17"):
                    opp_val = getattr(item, "Agent_Kupac_17", None)
                    
                    if opp_val == self:
                        setattr(item, "Agent_Kupac_17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Agent_Kupac_17"):
                    opp_val = getattr(item, "Agent_Kupac_17", None)
                    
                    setattr(item, "Agent_Kupac_17", self)
                    

