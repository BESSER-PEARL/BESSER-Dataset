from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Drzava:

    def __init__(self, DrzavaID: int, NazivDrzave: str, grad2: set["Grad"] = None):
        self.DrzavaID = DrzavaID
        self.NazivDrzave = NazivDrzave
        self.grad2 = grad2 if grad2 is not None else set()
        
        pass
    @property
    def DrzavaID(self):
        return self.__DrzavaID
    @DrzavaID.setter
    def DrzavaID(self, DrzavaID: int):
        self.__DrzavaID = DrzavaID

    @property
    def NazivDrzave(self):
        return self.__NazivDrzave
    @NazivDrzave.setter
    def NazivDrzave(self, NazivDrzave: str):
        self.__NazivDrzave = NazivDrzave

    @property
    def grad2(self):
        return self.__grad2
    @grad2.setter
    def grad2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Drzava__grad2", None)
        self.__grad2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drzava3"):
                    opp_val = getattr(item, "drzava3", None)
                    
                    if opp_val == self:
                        setattr(item, "drzava3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drzava3"):
                    opp_val = getattr(item, "drzava3", None)
                    
                    setattr(item, "drzava3", self)
                    



class Grad:

    def __init__(self, GradID: int, NazivGrada: str, DrzavaID: int, drzava3: "Drzava" = None, hotel4: set["Hotel"] = None):
        self.GradID = GradID
        self.NazivGrada = NazivGrada
        self.DrzavaID = DrzavaID
        self.drzava3 = drzava3
        self.hotel4 = hotel4 if hotel4 is not None else set()
        
        pass
    @property
    def GradID(self):
        return self.__GradID
    @GradID.setter
    def GradID(self, GradID: int):
        self.__GradID = GradID

    @property
    def NazivGrada(self):
        return self.__NazivGrada
    @NazivGrada.setter
    def NazivGrada(self, NazivGrada: str):
        self.__NazivGrada = NazivGrada

    @property
    def DrzavaID(self):
        return self.__DrzavaID
    @DrzavaID.setter
    def DrzavaID(self, DrzavaID: int):
        self.__DrzavaID = DrzavaID

    @property
    def hotel4(self):
        return self.__hotel4
    @hotel4.setter
    def hotel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Grad__hotel4", None)
        self.__hotel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "grad5"):
                    opp_val = getattr(item, "grad5", None)
                    
                    if opp_val == self:
                        setattr(item, "grad5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "grad5"):
                    opp_val = getattr(item, "grad5", None)
                    
                    setattr(item, "grad5", self)
                    

    @property
    def drzava3(self):
        return self.__drzava3
    @drzava3.setter
    def drzava3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Grad__drzava3", None)
        self.__drzava3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grad2"):
                opp_val = getattr(old_value, "grad2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grad2"):
                opp_val = getattr(value, "grad2", None)
                if opp_val is None:
                    setattr(value, "grad2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Hotel:

    def __init__(self, HotelID: int, NazivHotela: str, KontaktHotela: str, AdresaHotela: str, GradID: int, grad5: "Grad" = None, aranzman9: set["Aranzman"] = None):
        self.HotelID = HotelID
        self.NazivHotela = NazivHotela
        self.KontaktHotela = KontaktHotela
        self.AdresaHotela = AdresaHotela
        self.GradID = GradID
        self.grad5 = grad5
        self.aranzman9 = aranzman9 if aranzman9 is not None else set()
        
        pass
    @property
    def AdresaHotela(self):
        return self.__AdresaHotela
    @AdresaHotela.setter
    def AdresaHotela(self, AdresaHotela: str):
        self.__AdresaHotela = AdresaHotela

    @property
    def GradID(self):
        return self.__GradID
    @GradID.setter
    def GradID(self, GradID: int):
        self.__GradID = GradID

    @property
    def NazivHotela(self):
        return self.__NazivHotela
    @NazivHotela.setter
    def NazivHotela(self, NazivHotela: str):
        self.__NazivHotela = NazivHotela

    @property
    def KontaktHotela(self):
        return self.__KontaktHotela
    @KontaktHotela.setter
    def KontaktHotela(self, KontaktHotela: str):
        self.__KontaktHotela = KontaktHotela

    @property
    def HotelID(self):
        return self.__HotelID
    @HotelID.setter
    def HotelID(self, HotelID: int):
        self.__HotelID = HotelID

    @property
    def aranzman9(self):
        return self.__aranzman9
    @aranzman9.setter
    def aranzman9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__aranzman9", None)
        self.__aranzman9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hotel8"):
                    opp_val = getattr(item, "hotel8", None)
                    
                    if opp_val == self:
                        setattr(item, "hotel8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hotel8"):
                    opp_val = getattr(item, "hotel8", None)
                    
                    setattr(item, "hotel8", self)
                    

    @property
    def grad5(self):
        return self.__grad5
    @grad5.setter
    def grad5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__grad5", None)
        self.__grad5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotel4"):
                opp_val = getattr(old_value, "hotel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotel4"):
                opp_val = getattr(value, "hotel4", None)
                if opp_val is None:
                    setattr(value, "hotel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Vodic:

    def __init__(self, VodicID: int, ImeVodica: str, PrezimeVodica: str, JMBG: str, AdresaVodica: str, GradVodica: str, KontaktVodica: str, aranzman0: set["Aranzman"] = None):
        self.VodicID = VodicID
        self.ImeVodica = ImeVodica
        self.PrezimeVodica = PrezimeVodica
        self.JMBG = JMBG
        self.AdresaVodica = AdresaVodica
        self.GradVodica = GradVodica
        self.KontaktVodica = KontaktVodica
        self.aranzman0 = aranzman0 if aranzman0 is not None else set()
        
        pass
    @property
    def KontaktVodica(self):
        return self.__KontaktVodica
    @KontaktVodica.setter
    def KontaktVodica(self, KontaktVodica: str):
        self.__KontaktVodica = KontaktVodica

    @property
    def GradVodica(self):
        return self.__GradVodica
    @GradVodica.setter
    def GradVodica(self, GradVodica: str):
        self.__GradVodica = GradVodica

    @property
    def VodicID(self):
        return self.__VodicID
    @VodicID.setter
    def VodicID(self, VodicID: int):
        self.__VodicID = VodicID

    @property
    def AdresaVodica(self):
        return self.__AdresaVodica
    @AdresaVodica.setter
    def AdresaVodica(self, AdresaVodica: str):
        self.__AdresaVodica = AdresaVodica

    @property
    def PrezimeVodica(self):
        return self.__PrezimeVodica
    @PrezimeVodica.setter
    def PrezimeVodica(self, PrezimeVodica: str):
        self.__PrezimeVodica = PrezimeVodica

    @property
    def ImeVodica(self):
        return self.__ImeVodica
    @ImeVodica.setter
    def ImeVodica(self, ImeVodica: str):
        self.__ImeVodica = ImeVodica

    @property
    def JMBG(self):
        return self.__JMBG
    @JMBG.setter
    def JMBG(self, JMBG: str):
        self.__JMBG = JMBG

    @property
    def aranzman0(self):
        return self.__aranzman0
    @aranzman0.setter
    def aranzman0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vodic__aranzman0", None)
        self.__aranzman0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vodic1"):
                    opp_val = getattr(item, "vodic1", None)
                    
                    if opp_val == self:
                        setattr(item, "vodic1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vodic1"):
                    opp_val = getattr(item, "vodic1", None)
                    
                    setattr(item, "vodic1", self)
                    



class Aranzman:

    def __init__(self, AranzmanID: int, NazivAranzmana: str, DatumAranzmana: str, CenaAranzmana: str, OpisAranzmana: str, HotelID: int, VodicID: int, KorisnikID: int, vodic1: "Vodic" = None, korisnik7: "Korisnik" = None, hotel8: "Hotel" = None, putnik11: set["Putnik"] = None):
        self.AranzmanID = AranzmanID
        self.NazivAranzmana = NazivAranzmana
        self.DatumAranzmana = DatumAranzmana
        self.CenaAranzmana = CenaAranzmana
        self.OpisAranzmana = OpisAranzmana
        self.HotelID = HotelID
        self.VodicID = VodicID
        self.KorisnikID = KorisnikID
        self.vodic1 = vodic1
        self.korisnik7 = korisnik7
        self.hotel8 = hotel8
        self.putnik11 = putnik11 if putnik11 is not None else set()
        
        pass
    @property
    def OpisAranzmana(self):
        return self.__OpisAranzmana
    @OpisAranzmana.setter
    def OpisAranzmana(self, OpisAranzmana: str):
        self.__OpisAranzmana = OpisAranzmana

    @property
    def DatumAranzmana(self):
        return self.__DatumAranzmana
    @DatumAranzmana.setter
    def DatumAranzmana(self, DatumAranzmana: str):
        self.__DatumAranzmana = DatumAranzmana

    @property
    def CenaAranzmana(self):
        return self.__CenaAranzmana
    @CenaAranzmana.setter
    def CenaAranzmana(self, CenaAranzmana: str):
        self.__CenaAranzmana = CenaAranzmana

    @property
    def VodicID(self):
        return self.__VodicID
    @VodicID.setter
    def VodicID(self, VodicID: int):
        self.__VodicID = VodicID

    @property
    def KorisnikID(self):
        return self.__KorisnikID
    @KorisnikID.setter
    def KorisnikID(self, KorisnikID: int):
        self.__KorisnikID = KorisnikID

    @property
    def NazivAranzmana(self):
        return self.__NazivAranzmana
    @NazivAranzmana.setter
    def NazivAranzmana(self, NazivAranzmana: str):
        self.__NazivAranzmana = NazivAranzmana

    @property
    def HotelID(self):
        return self.__HotelID
    @HotelID.setter
    def HotelID(self, HotelID: int):
        self.__HotelID = HotelID

    @property
    def AranzmanID(self):
        return self.__AranzmanID
    @AranzmanID.setter
    def AranzmanID(self, AranzmanID: int):
        self.__AranzmanID = AranzmanID

    @property
    def putnik11(self):
        return self.__putnik11
    @putnik11.setter
    def putnik11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aranzman__putnik11", None)
        self.__putnik11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aranzman10"):
                    opp_val = getattr(item, "aranzman10", None)
                    
                    if opp_val == self:
                        setattr(item, "aranzman10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aranzman10"):
                    opp_val = getattr(item, "aranzman10", None)
                    
                    setattr(item, "aranzman10", self)
                    

    @property
    def hotel8(self):
        return self.__hotel8
    @hotel8.setter
    def hotel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aranzman__hotel8", None)
        self.__hotel8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aranzman9"):
                opp_val = getattr(old_value, "aranzman9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aranzman9"):
                opp_val = getattr(value, "aranzman9", None)
                if opp_val is None:
                    setattr(value, "aranzman9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def korisnik7(self):
        return self.__korisnik7
    @korisnik7.setter
    def korisnik7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aranzman__korisnik7", None)
        self.__korisnik7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aranzman6"):
                opp_val = getattr(old_value, "aranzman6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aranzman6"):
                opp_val = getattr(value, "aranzman6", None)
                if opp_val is None:
                    setattr(value, "aranzman6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vodic1(self):
        return self.__vodic1
    @vodic1.setter
    def vodic1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aranzman__vodic1", None)
        self.__vodic1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aranzman0"):
                opp_val = getattr(old_value, "aranzman0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aranzman0"):
                opp_val = getattr(value, "aranzman0", None)
                if opp_val is None:
                    setattr(value, "aranzman0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Uplata:

    def __init__(self, NazivUplate: str, DatumUplate: str, Iznos: str, PutnikID: int, UplataID: int, putnik12: "Putnik" = None):
        self.NazivUplate = NazivUplate
        self.DatumUplate = DatumUplate
        self.Iznos = Iznos
        self.PutnikID = PutnikID
        self.UplataID = UplataID
        self.putnik12 = putnik12
        
        pass
    @property
    def UplataID(self):
        return self.__UplataID
    @UplataID.setter
    def UplataID(self, UplataID: int):
        self.__UplataID = UplataID

    @property
    def PutnikID(self):
        return self.__PutnikID
    @PutnikID.setter
    def PutnikID(self, PutnikID: int):
        self.__PutnikID = PutnikID

    @property
    def Iznos(self):
        return self.__Iznos
    @Iznos.setter
    def Iznos(self, Iznos: str):
        self.__Iznos = Iznos

    @property
    def NazivUplate(self):
        return self.__NazivUplate
    @NazivUplate.setter
    def NazivUplate(self, NazivUplate: str):
        self.__NazivUplate = NazivUplate

    @property
    def DatumUplate(self):
        return self.__DatumUplate
    @DatumUplate.setter
    def DatumUplate(self, DatumUplate: str):
        self.__DatumUplate = DatumUplate

    @property
    def putnik12(self):
        return self.__putnik12
    @putnik12.setter
    def putnik12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Uplata__putnik12", None)
        self.__putnik12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uplata13"):
                opp_val = getattr(old_value, "uplata13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uplata13"):
                opp_val = getattr(value, "uplata13", None)
                if opp_val is None:
                    setattr(value, "uplata13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Korisnik:

    def __init__(self, KorisnikID: int, ImeKorisnika: str, PrezimeKorisnika: str, JMBG: str, AdresaKorisnika: str, GradKorisnika: str, KontaktKorisnika: str, Username: str, Password: str, aranzman6: set["Aranzman"] = None):
        self.KorisnikID = KorisnikID
        self.ImeKorisnika = ImeKorisnika
        self.PrezimeKorisnika = PrezimeKorisnika
        self.JMBG = JMBG
        self.AdresaKorisnika = AdresaKorisnika
        self.GradKorisnika = GradKorisnika
        self.KontaktKorisnika = KontaktKorisnika
        self.Username = Username
        self.Password = Password
        self.aranzman6 = aranzman6 if aranzman6 is not None else set()
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def ImeKorisnika(self):
        return self.__ImeKorisnika
    @ImeKorisnika.setter
    def ImeKorisnika(self, ImeKorisnika: str):
        self.__ImeKorisnika = ImeKorisnika

    @property
    def GradKorisnika(self):
        return self.__GradKorisnika
    @GradKorisnika.setter
    def GradKorisnika(self, GradKorisnika: str):
        self.__GradKorisnika = GradKorisnika

    @property
    def AdresaKorisnika(self):
        return self.__AdresaKorisnika
    @AdresaKorisnika.setter
    def AdresaKorisnika(self, AdresaKorisnika: str):
        self.__AdresaKorisnika = AdresaKorisnika

    @property
    def PrezimeKorisnika(self):
        return self.__PrezimeKorisnika
    @PrezimeKorisnika.setter
    def PrezimeKorisnika(self, PrezimeKorisnika: str):
        self.__PrezimeKorisnika = PrezimeKorisnika

    @property
    def KorisnikID(self):
        return self.__KorisnikID
    @KorisnikID.setter
    def KorisnikID(self, KorisnikID: int):
        self.__KorisnikID = KorisnikID

    @property
    def KontaktKorisnika(self):
        return self.__KontaktKorisnika
    @KontaktKorisnika.setter
    def KontaktKorisnika(self, KontaktKorisnika: str):
        self.__KontaktKorisnika = KontaktKorisnika

    @property
    def JMBG(self):
        return self.__JMBG
    @JMBG.setter
    def JMBG(self, JMBG: str):
        self.__JMBG = JMBG

    @property
    def aranzman6(self):
        return self.__aranzman6
    @aranzman6.setter
    def aranzman6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Korisnik__aranzman6", None)
        self.__aranzman6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "korisnik7"):
                    opp_val = getattr(item, "korisnik7", None)
                    
                    if opp_val == self:
                        setattr(item, "korisnik7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "korisnik7"):
                    opp_val = getattr(item, "korisnik7", None)
                    
                    setattr(item, "korisnik7", self)
                    



class Putnik:

    def __init__(self, PutnikID: int, BrojPasosa: int, ImePutnika: str, PrezimePutnika: str, JMBG: str, AdresaPutnika: str, GradPutnika: str, KontaktPutnika: str, AranzmanID: int, aranzman10: "Aranzman" = None, uplata13: set["Uplata"] = None):
        self.PutnikID = PutnikID
        self.BrojPasosa = BrojPasosa
        self.ImePutnika = ImePutnika
        self.PrezimePutnika = PrezimePutnika
        self.JMBG = JMBG
        self.AdresaPutnika = AdresaPutnika
        self.GradPutnika = GradPutnika
        self.KontaktPutnika = KontaktPutnika
        self.AranzmanID = AranzmanID
        self.aranzman10 = aranzman10
        self.uplata13 = uplata13 if uplata13 is not None else set()
        
        pass
    @property
    def PrezimePutnika(self):
        return self.__PrezimePutnika
    @PrezimePutnika.setter
    def PrezimePutnika(self, PrezimePutnika: str):
        self.__PrezimePutnika = PrezimePutnika

    @property
    def AdresaPutnika(self):
        return self.__AdresaPutnika
    @AdresaPutnika.setter
    def AdresaPutnika(self, AdresaPutnika: str):
        self.__AdresaPutnika = AdresaPutnika

    @property
    def PutnikID(self):
        return self.__PutnikID
    @PutnikID.setter
    def PutnikID(self, PutnikID: int):
        self.__PutnikID = PutnikID

    @property
    def AranzmanID(self):
        return self.__AranzmanID
    @AranzmanID.setter
    def AranzmanID(self, AranzmanID: int):
        self.__AranzmanID = AranzmanID

    @property
    def JMBG(self):
        return self.__JMBG
    @JMBG.setter
    def JMBG(self, JMBG: str):
        self.__JMBG = JMBG

    @property
    def ImePutnika(self):
        return self.__ImePutnika
    @ImePutnika.setter
    def ImePutnika(self, ImePutnika: str):
        self.__ImePutnika = ImePutnika

    @property
    def BrojPasosa(self):
        return self.__BrojPasosa
    @BrojPasosa.setter
    def BrojPasosa(self, BrojPasosa: int):
        self.__BrojPasosa = BrojPasosa

    @property
    def GradPutnika(self):
        return self.__GradPutnika
    @GradPutnika.setter
    def GradPutnika(self, GradPutnika: str):
        self.__GradPutnika = GradPutnika

    @property
    def KontaktPutnika(self):
        return self.__KontaktPutnika
    @KontaktPutnika.setter
    def KontaktPutnika(self, KontaktPutnika: str):
        self.__KontaktPutnika = KontaktPutnika

    @property
    def aranzman10(self):
        return self.__aranzman10
    @aranzman10.setter
    def aranzman10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Putnik__aranzman10", None)
        self.__aranzman10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "putnik11"):
                opp_val = getattr(old_value, "putnik11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "putnik11"):
                opp_val = getattr(value, "putnik11", None)
                if opp_val is None:
                    setattr(value, "putnik11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uplata13(self):
        return self.__uplata13
    @uplata13.setter
    def uplata13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Putnik__uplata13", None)
        self.__uplata13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "putnik12"):
                    opp_val = getattr(item, "putnik12", None)
                    
                    if opp_val == self:
                        setattr(item, "putnik12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "putnik12"):
                    opp_val = getattr(item, "putnik12", None)
                    
                    setattr(item, "putnik12", self)
                    

