from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Putnik:

    def __init__(self, PutnikID: int, ImePut: str, PrezimePut: str, JMBG: str, Grad: str, Adresa: str, Mobilni: int, eMail: str, OsigID: int, osiguranje5: "Osiguranje" = None, rezervisanje6: set["Rezervisanje"] = None):
        self.PutnikID = PutnikID
        self.ImePut = ImePut
        self.PrezimePut = PrezimePut
        self.JMBG = JMBG
        self.Grad = Grad
        self.Adresa = Adresa
        self.Mobilni = Mobilni
        self.eMail = eMail
        self.OsigID = OsigID
        self.osiguranje5 = osiguranje5
        self.rezervisanje6 = rezervisanje6 if rezervisanje6 is not None else set()
        
        pass
    @property
    def eMail(self):
        return self.__eMail
    @eMail.setter
    def eMail(self, eMail: str):
        self.__eMail = eMail

    @property
    def Mobilni(self):
        return self.__Mobilni
    @Mobilni.setter
    def Mobilni(self, Mobilni: int):
        self.__Mobilni = Mobilni

    @property
    def ImePut(self):
        return self.__ImePut
    @ImePut.setter
    def ImePut(self, ImePut: str):
        self.__ImePut = ImePut

    @property
    def PrezimePut(self):
        return self.__PrezimePut
    @PrezimePut.setter
    def PrezimePut(self, PrezimePut: str):
        self.__PrezimePut = PrezimePut

    @property
    def JMBG(self):
        return self.__JMBG
    @JMBG.setter
    def JMBG(self, JMBG: str):
        self.__JMBG = JMBG

    @property
    def Grad(self):
        return self.__Grad
    @Grad.setter
    def Grad(self, Grad: str):
        self.__Grad = Grad

    @property
    def PutnikID(self):
        return self.__PutnikID
    @PutnikID.setter
    def PutnikID(self, PutnikID: int):
        self.__PutnikID = PutnikID

    @property
    def Adresa(self):
        return self.__Adresa
    @Adresa.setter
    def Adresa(self, Adresa: str):
        self.__Adresa = Adresa

    @property
    def OsigID(self):
        return self.__OsigID
    @OsigID.setter
    def OsigID(self, OsigID: int):
        self.__OsigID = OsigID

    @property
    def rezervisanje6(self):
        return self.__rezervisanje6
    @rezervisanje6.setter
    def rezervisanje6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Putnik__rezervisanje6", None)
        self.__rezervisanje6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "putnik7"):
                    opp_val = getattr(item, "putnik7", None)
                    
                    if opp_val == self:
                        setattr(item, "putnik7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "putnik7"):
                    opp_val = getattr(item, "putnik7", None)
                    
                    setattr(item, "putnik7", self)
                    

    @property
    def osiguranje5(self):
        return self.__osiguranje5
    @osiguranje5.setter
    def osiguranje5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Putnik__osiguranje5", None)
        self.__osiguranje5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "putnik4"):
                opp_val = getattr(old_value, "putnik4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "putnik4"):
                opp_val = getattr(value, "putnik4", None)
                if opp_val is None:
                    setattr(value, "putnik4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Osiguranje:

    def __init__(self, OsigID: int, KucaOsiguranje: str, putnik4: set["Putnik"] = None):
        self.OsigID = OsigID
        self.KucaOsiguranje = KucaOsiguranje
        self.putnik4 = putnik4 if putnik4 is not None else set()
        
        pass
    @property
    def KucaOsiguranje(self):
        return self.__KucaOsiguranje
    @KucaOsiguranje.setter
    def KucaOsiguranje(self, KucaOsiguranje: str):
        self.__KucaOsiguranje = KucaOsiguranje

    @property
    def OsigID(self):
        return self.__OsigID
    @OsigID.setter
    def OsigID(self, OsigID: int):
        self.__OsigID = OsigID

    @property
    def putnik4(self):
        return self.__putnik4
    @putnik4.setter
    def putnik4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Osiguranje__putnik4", None)
        self.__putnik4 = value if value is not None else set()
        
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
                    



class Hotel:

    def __init__(self, HotelID: int, ImeHotela: str, AdresaHotela: str, SpratHotela: int, SobaHotela: int, UslugaHotela: str, DuzinaBoravka: int, CenaSmestaja: str, DestiID: int, destinacija1: "Destinacija" = None):
        self.HotelID = HotelID
        self.ImeHotela = ImeHotela
        self.AdresaHotela = AdresaHotela
        self.SpratHotela = SpratHotela
        self.SobaHotela = SobaHotela
        self.UslugaHotela = UslugaHotela
        self.DuzinaBoravka = DuzinaBoravka
        self.CenaSmestaja = CenaSmestaja
        self.DestiID = DestiID
        self.destinacija1 = destinacija1
        
        pass
    @property
    def CenaSmestaja(self):
        return self.__CenaSmestaja
    @CenaSmestaja.setter
    def CenaSmestaja(self, CenaSmestaja: str):
        self.__CenaSmestaja = CenaSmestaja

    @property
    def AdresaHotela(self):
        return self.__AdresaHotela
    @AdresaHotela.setter
    def AdresaHotela(self, AdresaHotela: str):
        self.__AdresaHotela = AdresaHotela

    @property
    def UslugaHotela(self):
        return self.__UslugaHotela
    @UslugaHotela.setter
    def UslugaHotela(self, UslugaHotela: str):
        self.__UslugaHotela = UslugaHotela

    @property
    def HotelID(self):
        return self.__HotelID
    @HotelID.setter
    def HotelID(self, HotelID: int):
        self.__HotelID = HotelID

    @property
    def DuzinaBoravka(self):
        return self.__DuzinaBoravka
    @DuzinaBoravka.setter
    def DuzinaBoravka(self, DuzinaBoravka: int):
        self.__DuzinaBoravka = DuzinaBoravka

    @property
    def SobaHotela(self):
        return self.__SobaHotela
    @SobaHotela.setter
    def SobaHotela(self, SobaHotela: int):
        self.__SobaHotela = SobaHotela

    @property
    def DestiID(self):
        return self.__DestiID
    @DestiID.setter
    def DestiID(self, DestiID: int):
        self.__DestiID = DestiID

    @property
    def SpratHotela(self):
        return self.__SpratHotela
    @SpratHotela.setter
    def SpratHotela(self, SpratHotela: int):
        self.__SpratHotela = SpratHotela

    @property
    def ImeHotela(self):
        return self.__ImeHotela
    @ImeHotela.setter
    def ImeHotela(self, ImeHotela: str):
        self.__ImeHotela = ImeHotela

    @property
    def destinacija1(self):
        return self.__destinacija1
    @destinacija1.setter
    def destinacija1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__destinacija1", None)
        self.__destinacija1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotel0"):
                opp_val = getattr(old_value, "hotel0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotel0"):
                opp_val = getattr(value, "hotel0", None)
                if opp_val is None:
                    setattr(value, "hotel0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Korisnik_IS:

    def __init__(self, KorisnikID: int, UserName: str, Password: str, ImeKorisnika: str, PrezimeKorisnika: str, rezervisanje9: set["Rezervisanje"] = None):
        self.KorisnikID = KorisnikID
        self.UserName = UserName
        self.Password = Password
        self.ImeKorisnika = ImeKorisnika
        self.PrezimeKorisnika = PrezimeKorisnika
        self.rezervisanje9 = rezervisanje9 if rezervisanje9 is not None else set()
        
        pass
    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def ImeKorisnika(self):
        return self.__ImeKorisnika
    @ImeKorisnika.setter
    def ImeKorisnika(self, ImeKorisnika: str):
        self.__ImeKorisnika = ImeKorisnika

    @property
    def PrezimeKorisnika(self):
        return self.__PrezimeKorisnika
    @PrezimeKorisnika.setter
    def PrezimeKorisnika(self, PrezimeKorisnika: str):
        self.__PrezimeKorisnika = PrezimeKorisnika

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def KorisnikID(self):
        return self.__KorisnikID
    @KorisnikID.setter
    def KorisnikID(self, KorisnikID: int):
        self.__KorisnikID = KorisnikID

    @property
    def rezervisanje9(self):
        return self.__rezervisanje9
    @rezervisanje9.setter
    def rezervisanje9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Korisnik_IS__rezervisanje9", None)
        self.__rezervisanje9 = value if value is not None else set()
        
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
                    



class Rezervisanje:

    def __init__(self, DatumPolaska: str, DatumDolaska: str, Cena: str, DestiID: int, PutnikID: int, KorisnikID: int, RezerID: int, SlobMesto: bool, destinacija2: "Destinacija" = None, putnik7: "Putnik" = None, korisnik_IS8: "Korisnik_IS" = None, karta11: set["Karta"] = None):
        self.DatumPolaska = DatumPolaska
        self.DatumDolaska = DatumDolaska
        self.Cena = Cena
        self.DestiID = DestiID
        self.PutnikID = PutnikID
        self.KorisnikID = KorisnikID
        self.RezerID = RezerID
        self.SlobMesto = SlobMesto
        self.destinacija2 = destinacija2
        self.putnik7 = putnik7
        self.korisnik_IS8 = korisnik_IS8
        self.karta11 = karta11 if karta11 is not None else set()
        
        pass
    @property
    def PutnikID(self):
        return self.__PutnikID
    @PutnikID.setter
    def PutnikID(self, PutnikID: int):
        self.__PutnikID = PutnikID

    @property
    def DatumPolaska(self):
        return self.__DatumPolaska
    @DatumPolaska.setter
    def DatumPolaska(self, DatumPolaska: str):
        self.__DatumPolaska = DatumPolaska

    @property
    def SlobMesto(self):
        return self.__SlobMesto
    @SlobMesto.setter
    def SlobMesto(self, SlobMesto: bool):
        self.__SlobMesto = SlobMesto

    @property
    def DestiID(self):
        return self.__DestiID
    @DestiID.setter
    def DestiID(self, DestiID: int):
        self.__DestiID = DestiID

    @property
    def KorisnikID(self):
        return self.__KorisnikID
    @KorisnikID.setter
    def KorisnikID(self, KorisnikID: int):
        self.__KorisnikID = KorisnikID

    @property
    def DatumDolaska(self):
        return self.__DatumDolaska
    @DatumDolaska.setter
    def DatumDolaska(self, DatumDolaska: str):
        self.__DatumDolaska = DatumDolaska

    @property
    def RezerID(self):
        return self.__RezerID
    @RezerID.setter
    def RezerID(self, RezerID: int):
        self.__RezerID = RezerID

    @property
    def Cena(self):
        return self.__Cena
    @Cena.setter
    def Cena(self, Cena: str):
        self.__Cena = Cena

    @property
    def putnik7(self):
        return self.__putnik7
    @putnik7.setter
    def putnik7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rezervisanje__putnik7", None)
        self.__putnik7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rezervisanje6"):
                opp_val = getattr(old_value, "rezervisanje6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rezervisanje6"):
                opp_val = getattr(value, "rezervisanje6", None)
                if opp_val is None:
                    setattr(value, "rezervisanje6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def destinacija2(self):
        return self.__destinacija2
    @destinacija2.setter
    def destinacija2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rezervisanje__destinacija2", None)
        self.__destinacija2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rezervisanje3"):
                opp_val = getattr(old_value, "rezervisanje3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rezervisanje3"):
                opp_val = getattr(value, "rezervisanje3", None)
                if opp_val is None:
                    setattr(value, "rezervisanje3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def karta11(self):
        return self.__karta11
    @karta11.setter
    def karta11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rezervisanje__karta11", None)
        self.__karta11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rezervisanje10"):
                    opp_val = getattr(item, "rezervisanje10", None)
                    
                    if opp_val == self:
                        setattr(item, "rezervisanje10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rezervisanje10"):
                    opp_val = getattr(item, "rezervisanje10", None)
                    
                    setattr(item, "rezervisanje10", self)
                    

    @property
    def korisnik_IS8(self):
        return self.__korisnik_IS8
    @korisnik_IS8.setter
    def korisnik_IS8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rezervisanje__korisnik_IS8", None)
        self.__korisnik_IS8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rezervisanje9"):
                opp_val = getattr(old_value, "rezervisanje9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rezervisanje9"):
                opp_val = getattr(value, "rezervisanje9", None)
                if opp_val is None:
                    setattr(value, "rezervisanje9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Destinacija:

    def __init__(self, DestiID: int, DesDrzava: str, DesGrad: str, hotel0: set["Hotel"] = None, rezervisanje3: set["Rezervisanje"] = None):
        self.DestiID = DestiID
        self.DesDrzava = DesDrzava
        self.DesGrad = DesGrad
        self.hotel0 = hotel0 if hotel0 is not None else set()
        self.rezervisanje3 = rezervisanje3 if rezervisanje3 is not None else set()
        
        pass
    @property
    def DestiID(self):
        return self.__DestiID
    @DestiID.setter
    def DestiID(self, DestiID: int):
        self.__DestiID = DestiID

    @property
    def DesDrzava(self):
        return self.__DesDrzava
    @DesDrzava.setter
    def DesDrzava(self, DesDrzava: str):
        self.__DesDrzava = DesDrzava

    @property
    def DesGrad(self):
        return self.__DesGrad
    @DesGrad.setter
    def DesGrad(self, DesGrad: str):
        self.__DesGrad = DesGrad

    @property
    def hotel0(self):
        return self.__hotel0
    @hotel0.setter
    def hotel0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Destinacija__hotel0", None)
        self.__hotel0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "destinacija1"):
                    opp_val = getattr(item, "destinacija1", None)
                    
                    if opp_val == self:
                        setattr(item, "destinacija1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "destinacija1"):
                    opp_val = getattr(item, "destinacija1", None)
                    
                    setattr(item, "destinacija1", self)
                    

    @property
    def rezervisanje3(self):
        return self.__rezervisanje3
    @rezervisanje3.setter
    def rezervisanje3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Destinacija__rezervisanje3", None)
        self.__rezervisanje3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "destinacija2"):
                    opp_val = getattr(item, "destinacija2", None)
                    
                    if opp_val == self:
                        setattr(item, "destinacija2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "destinacija2"):
                    opp_val = getattr(item, "destinacija2", None)
                    
                    setattr(item, "destinacija2", self)
                    



class Karta:

    def __init__(self, KartaID: int, OdlazakKarta: str, VremeOdlaska: str, PovratakKarta: str, VremePovratka: str, CenaKarte: str, RezerID: int, rezervisanje10: "Rezervisanje" = None):
        self.KartaID = KartaID
        self.OdlazakKarta = OdlazakKarta
        self.VremeOdlaska = VremeOdlaska
        self.PovratakKarta = PovratakKarta
        self.VremePovratka = VremePovratka
        self.CenaKarte = CenaKarte
        self.RezerID = RezerID
        self.rezervisanje10 = rezervisanje10
        
        pass
    @property
    def OdlazakKarta(self):
        return self.__OdlazakKarta
    @OdlazakKarta.setter
    def OdlazakKarta(self, OdlazakKarta: str):
        self.__OdlazakKarta = OdlazakKarta

    @property
    def VremePovratka(self):
        return self.__VremePovratka
    @VremePovratka.setter
    def VremePovratka(self, VremePovratka: str):
        self.__VremePovratka = VremePovratka

    @property
    def PovratakKarta(self):
        return self.__PovratakKarta
    @PovratakKarta.setter
    def PovratakKarta(self, PovratakKarta: str):
        self.__PovratakKarta = PovratakKarta

    @property
    def RezerID(self):
        return self.__RezerID
    @RezerID.setter
    def RezerID(self, RezerID: int):
        self.__RezerID = RezerID

    @property
    def VremeOdlaska(self):
        return self.__VremeOdlaska
    @VremeOdlaska.setter
    def VremeOdlaska(self, VremeOdlaska: str):
        self.__VremeOdlaska = VremeOdlaska

    @property
    def KartaID(self):
        return self.__KartaID
    @KartaID.setter
    def KartaID(self, KartaID: int):
        self.__KartaID = KartaID

    @property
    def CenaKarte(self):
        return self.__CenaKarte
    @CenaKarte.setter
    def CenaKarte(self, CenaKarte: str):
        self.__CenaKarte = CenaKarte

    @property
    def rezervisanje10(self):
        return self.__rezervisanje10
    @rezervisanje10.setter
    def rezervisanje10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Karta__rezervisanje10", None)
        self.__rezervisanje10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "karta11"):
                opp_val = getattr(old_value, "karta11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "karta11"):
                opp_val = getattr(value, "karta11", None)
                if opp_val is None:
                    setattr(value, "karta11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

