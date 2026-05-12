from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Kupac:

    def __init__(self, KupacID: int, ImeKup: str, PrezimeKup: str, JMBG: str, Grad: str, Adresa: str, Mobilni: int, eMail: str, OsigID: int, osiguranje5: "Osiguranje" = None, aran_man6: set["Aran_man"] = None):
        self.KupacID = KupacID
        self.ImeKup = ImeKup
        self.PrezimeKup = PrezimeKup
        self.JMBG = JMBG
        self.Grad = Grad
        self.Adresa = Adresa
        self.Mobilni = Mobilni
        self.eMail = eMail
        self.OsigID = OsigID
        self.osiguranje5 = osiguranje5
        self.aran_man6 = aran_man6 if aran_man6 is not None else set()
        
        pass
    @property
    def OsigID(self):
        return self.__OsigID
    @OsigID.setter
    def OsigID(self, OsigID: int):
        self.__OsigID = OsigID

    @property
    def Grad(self):
        return self.__Grad
    @Grad.setter
    def Grad(self, Grad: str):
        self.__Grad = Grad

    @property
    def Adresa(self):
        return self.__Adresa
    @Adresa.setter
    def Adresa(self, Adresa: str):
        self.__Adresa = Adresa

    @property
    def ImeKup(self):
        return self.__ImeKup
    @ImeKup.setter
    def ImeKup(self, ImeKup: str):
        self.__ImeKup = ImeKup

    @property
    def Mobilni(self):
        return self.__Mobilni
    @Mobilni.setter
    def Mobilni(self, Mobilni: int):
        self.__Mobilni = Mobilni

    @property
    def eMail(self):
        return self.__eMail
    @eMail.setter
    def eMail(self, eMail: str):
        self.__eMail = eMail

    @property
    def KupacID(self):
        return self.__KupacID
    @KupacID.setter
    def KupacID(self, KupacID: int):
        self.__KupacID = KupacID

    @property
    def PrezimeKup(self):
        return self.__PrezimeKup
    @PrezimeKup.setter
    def PrezimeKup(self, PrezimeKup: str):
        self.__PrezimeKup = PrezimeKup

    @property
    def JMBG(self):
        return self.__JMBG
    @JMBG.setter
    def JMBG(self, JMBG: str):
        self.__JMBG = JMBG

    @property
    def osiguranje5(self):
        return self.__osiguranje5
    @osiguranje5.setter
    def osiguranje5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kupac__osiguranje5", None)
        self.__osiguranje5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kupac4"):
                opp_val = getattr(old_value, "kupac4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kupac4"):
                opp_val = getattr(value, "kupac4", None)
                if opp_val is None:
                    setattr(value, "kupac4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aran_man6(self):
        return self.__aran_man6
    @aran_man6.setter
    def aran_man6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kupac__aran_man6", None)
        self.__aran_man6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kupac7"):
                    opp_val = getattr(item, "kupac7", None)
                    
                    if opp_val == self:
                        setattr(item, "kupac7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kupac7"):
                    opp_val = getattr(item, "kupac7", None)
                    
                    setattr(item, "kupac7", self)
                    



class Osiguranje:

    def __init__(self, OsigID: int, KucaOsiguranje: str, PaketPokri_a: str, kupac4: set["Kupac"] = None):
        self.OsigID = OsigID
        self.KucaOsiguranje = KucaOsiguranje
        self.PaketPokri_a = PaketPokri_a
        self.kupac4 = kupac4 if kupac4 is not None else set()
        
        pass
    @property
    def OsigID(self):
        return self.__OsigID
    @OsigID.setter
    def OsigID(self, OsigID: int):
        self.__OsigID = OsigID

    @property
    def KucaOsiguranje(self):
        return self.__KucaOsiguranje
    @KucaOsiguranje.setter
    def KucaOsiguranje(self, KucaOsiguranje: str):
        self.__KucaOsiguranje = KucaOsiguranje

    @property
    def PaketPokri_a(self):
        return self.__PaketPokri_a
    @PaketPokri_a.setter
    def PaketPokri_a(self, PaketPokri_a: str):
        self.__PaketPokri_a = PaketPokri_a

    @property
    def kupac4(self):
        return self.__kupac4
    @kupac4.setter
    def kupac4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Osiguranje__kupac4", None)
        self.__kupac4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "osiguranje5"):
                    opp_val = getattr(item, "osiguranje5", None)
                    
                    if opp_val == self:
                        setattr(item, "osiguranje5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "osiguranje5"):
                    opp_val = getattr(item, "osiguranje5", None)
                    
                    setattr(item, "osiguranje5", self)
                    



class Sme_taj:

    def __init__(self, Sme_tajID: int, ImeSme_taja: str, LokacijaSme_taja: str, UslugaSme_taja: str, DuzinaBoravka: int, CenaSmestaja: str, PutovID: int, putovanje1: "Putovanje" = None):
        self.Sme_tajID = Sme_tajID
        self.ImeSme_taja = ImeSme_taja
        self.LokacijaSme_taja = LokacijaSme_taja
        self.UslugaSme_taja = UslugaSme_taja
        self.DuzinaBoravka = DuzinaBoravka
        self.CenaSmestaja = CenaSmestaja
        self.PutovID = PutovID
        self.putovanje1 = putovanje1
        
        pass
    @property
    def UslugaSme_taja(self):
        return self.__UslugaSme_taja
    @UslugaSme_taja.setter
    def UslugaSme_taja(self, UslugaSme_taja: str):
        self.__UslugaSme_taja = UslugaSme_taja

    @property
    def Sme_tajID(self):
        return self.__Sme_tajID
    @Sme_tajID.setter
    def Sme_tajID(self, Sme_tajID: int):
        self.__Sme_tajID = Sme_tajID

    @property
    def CenaSmestaja(self):
        return self.__CenaSmestaja
    @CenaSmestaja.setter
    def CenaSmestaja(self, CenaSmestaja: str):
        self.__CenaSmestaja = CenaSmestaja

    @property
    def PutovID(self):
        return self.__PutovID
    @PutovID.setter
    def PutovID(self, PutovID: int):
        self.__PutovID = PutovID

    @property
    def LokacijaSme_taja(self):
        return self.__LokacijaSme_taja
    @LokacijaSme_taja.setter
    def LokacijaSme_taja(self, LokacijaSme_taja: str):
        self.__LokacijaSme_taja = LokacijaSme_taja

    @property
    def ImeSme_taja(self):
        return self.__ImeSme_taja
    @ImeSme_taja.setter
    def ImeSme_taja(self, ImeSme_taja: str):
        self.__ImeSme_taja = ImeSme_taja

    @property
    def DuzinaBoravka(self):
        return self.__DuzinaBoravka
    @DuzinaBoravka.setter
    def DuzinaBoravka(self, DuzinaBoravka: int):
        self.__DuzinaBoravka = DuzinaBoravka

    @property
    def putovanje1(self):
        return self.__putovanje1
    @putovanje1.setter
    def putovanje1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sme_taj__putovanje1", None)
        self.__putovanje1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sme_taj0"):
                opp_val = getattr(old_value, "sme_taj0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sme_taj0"):
                opp_val = getattr(value, "sme_taj0", None)
                if opp_val is None:
                    setattr(value, "sme_taj0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Aran_man:

    def __init__(self, Aran_manID: int, SlobMesto: bool, DatumPolaska: str, DatumDolaska: str, Cena: str, PutovID: int, KupacID: int, KorisnikID: int, putovanje2: "Putovanje" = None, kupac7: "Kupac" = None, korisnik_IS8: "Korisnik_IS" = None):
        self.Aran_manID = Aran_manID
        self.SlobMesto = SlobMesto
        self.DatumPolaska = DatumPolaska
        self.DatumDolaska = DatumDolaska
        self.Cena = Cena
        self.PutovID = PutovID
        self.KupacID = KupacID
        self.KorisnikID = KorisnikID
        self.putovanje2 = putovanje2
        self.kupac7 = kupac7
        self.korisnik_IS8 = korisnik_IS8
        
        pass
    @property
    def DatumDolaska(self):
        return self.__DatumDolaska
    @DatumDolaska.setter
    def DatumDolaska(self, DatumDolaska: str):
        self.__DatumDolaska = DatumDolaska

    @property
    def Cena(self):
        return self.__Cena
    @Cena.setter
    def Cena(self, Cena: str):
        self.__Cena = Cena

    @property
    def PutovID(self):
        return self.__PutovID
    @PutovID.setter
    def PutovID(self, PutovID: int):
        self.__PutovID = PutovID

    @property
    def Aran_manID(self):
        return self.__Aran_manID
    @Aran_manID.setter
    def Aran_manID(self, Aran_manID: int):
        self.__Aran_manID = Aran_manID

    @property
    def DatumPolaska(self):
        return self.__DatumPolaska
    @DatumPolaska.setter
    def DatumPolaska(self, DatumPolaska: str):
        self.__DatumPolaska = DatumPolaska

    @property
    def KupacID(self):
        return self.__KupacID
    @KupacID.setter
    def KupacID(self, KupacID: int):
        self.__KupacID = KupacID

    @property
    def KorisnikID(self):
        return self.__KorisnikID
    @KorisnikID.setter
    def KorisnikID(self, KorisnikID: int):
        self.__KorisnikID = KorisnikID

    @property
    def SlobMesto(self):
        return self.__SlobMesto
    @SlobMesto.setter
    def SlobMesto(self, SlobMesto: bool):
        self.__SlobMesto = SlobMesto

    @property
    def putovanje2(self):
        return self.__putovanje2
    @putovanje2.setter
    def putovanje2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aran_man__putovanje2", None)
        self.__putovanje2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aran_man3"):
                opp_val = getattr(old_value, "aran_man3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aran_man3"):
                opp_val = getattr(value, "aran_man3", None)
                if opp_val is None:
                    setattr(value, "aran_man3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def korisnik_IS8(self):
        return self.__korisnik_IS8
    @korisnik_IS8.setter
    def korisnik_IS8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aran_man__korisnik_IS8", None)
        self.__korisnik_IS8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aran_man9"):
                opp_val = getattr(old_value, "aran_man9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aran_man9"):
                opp_val = getattr(value, "aran_man9", None)
                if opp_val is None:
                    setattr(value, "aran_man9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kupac7(self):
        return self.__kupac7
    @kupac7.setter
    def kupac7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aran_man__kupac7", None)
        self.__kupac7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aran_man6"):
                opp_val = getattr(old_value, "aran_man6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aran_man6"):
                opp_val = getattr(value, "aran_man6", None)
                if opp_val is None:
                    setattr(value, "aran_man6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Putovanje:

    def __init__(self, PutovID: int, Dr_ava: str, Grad: str, sme_taj0: set["Sme_taj"] = None, aran_man3: set["Aran_man"] = None):
        self.PutovID = PutovID
        self.Dr_ava = Dr_ava
        self.Grad = Grad
        self.sme_taj0 = sme_taj0 if sme_taj0 is not None else set()
        self.aran_man3 = aran_man3 if aran_man3 is not None else set()
        
        pass
    @property
    def PutovID(self):
        return self.__PutovID
    @PutovID.setter
    def PutovID(self, PutovID: int):
        self.__PutovID = PutovID

    @property
    def Grad(self):
        return self.__Grad
    @Grad.setter
    def Grad(self, Grad: str):
        self.__Grad = Grad

    @property
    def Dr_ava(self):
        return self.__Dr_ava
    @Dr_ava.setter
    def Dr_ava(self, Dr_ava: str):
        self.__Dr_ava = Dr_ava

    @property
    def sme_taj0(self):
        return self.__sme_taj0
    @sme_taj0.setter
    def sme_taj0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Putovanje__sme_taj0", None)
        self.__sme_taj0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "putovanje1"):
                    opp_val = getattr(item, "putovanje1", None)
                    
                    if opp_val == self:
                        setattr(item, "putovanje1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "putovanje1"):
                    opp_val = getattr(item, "putovanje1", None)
                    
                    setattr(item, "putovanje1", self)
                    

    @property
    def aran_man3(self):
        return self.__aran_man3
    @aran_man3.setter
    def aran_man3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Putovanje__aran_man3", None)
        self.__aran_man3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "putovanje2"):
                    opp_val = getattr(item, "putovanje2", None)
                    
                    if opp_val == self:
                        setattr(item, "putovanje2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "putovanje2"):
                    opp_val = getattr(item, "putovanje2", None)
                    
                    setattr(item, "putovanje2", self)
                    



class Korisnik_IS:

    def __init__(self, KorisnikID: int, UserName: str, Password: str, ImeKorisnika: str, PrezimeKorisnika: str, aran_man9: set["Aran_man"] = None):
        self.KorisnikID = KorisnikID
        self.UserName = UserName
        self.Password = Password
        self.ImeKorisnika = ImeKorisnika
        self.PrezimeKorisnika = PrezimeKorisnika
        self.aran_man9 = aran_man9 if aran_man9 is not None else set()
        
        pass
    @property
    def ImeKorisnika(self):
        return self.__ImeKorisnika
    @ImeKorisnika.setter
    def ImeKorisnika(self, ImeKorisnika: str):
        self.__ImeKorisnika = ImeKorisnika

    @property
    def KorisnikID(self):
        return self.__KorisnikID
    @KorisnikID.setter
    def KorisnikID(self, KorisnikID: int):
        self.__KorisnikID = KorisnikID

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def PrezimeKorisnika(self):
        return self.__PrezimeKorisnika
    @PrezimeKorisnika.setter
    def PrezimeKorisnika(self, PrezimeKorisnika: str):
        self.__PrezimeKorisnika = PrezimeKorisnika

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def aran_man9(self):
        return self.__aran_man9
    @aran_man9.setter
    def aran_man9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Korisnik_IS__aran_man9", None)
        self.__aran_man9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "korisnik_IS8"):
                    opp_val = getattr(item, "korisnik_IS8", None)
                    
                    if opp_val == self:
                        setattr(item, "korisnik_IS8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "korisnik_IS8"):
                    opp_val = getattr(item, "korisnik_IS8", None)
                    
                    setattr(item, "korisnik_IS8", self)
                    

