from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Date:

    pass


class Racun:

    def __init__(self, RacunID: int, Placeno: bool, Iznos: Double, rezervacija12: "Rezervacija" = None):
        self.RacunID = RacunID
        self.Placeno = Placeno
        self.Iznos = Iznos
        self.rezervacija12 = rezervacija12
        
        pass
    @property
    def RacunID(self):
        return self.__RacunID
    @RacunID.setter
    def RacunID(self, RacunID: int):
        self.__RacunID = RacunID

    @property
    def Placeno(self):
        return self.__Placeno
    @Placeno.setter
    def Placeno(self, Placeno: bool):
        self.__Placeno = Placeno

    @property
    def Iznos(self):
        return self.__Iznos
    @Iznos.setter
    def Iznos(self, Iznos: Double):
        self.__Iznos = Iznos

    @property
    def rezervacija12(self):
        return self.__rezervacija12
    @rezervacija12.setter
    def rezervacija12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Racun__rezervacija12", None)
        self.__rezervacija12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "racun13"):
                opp_val = getattr(old_value, "racun13", None)
                if opp_val == self:
                    setattr(old_value, "racun13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "racun13"):
                opp_val = getattr(value, "racun13", None)
                setattr(value, "racun13", self)



class Termin:

    def __init__(self, TerminID: int, DatumPolaska: Date, DatumPovratka: Date, aranzman10: "Aranzman" = None):
        self.TerminID = TerminID
        self.DatumPolaska = DatumPolaska
        self.DatumPovratka = DatumPovratka
        self.aranzman10 = aranzman10
        
        pass
    @property
    def TerminID(self):
        return self.__TerminID
    @TerminID.setter
    def TerminID(self, TerminID: int):
        self.__TerminID = TerminID

    @property
    def DatumPovratka(self):
        return self.__DatumPovratka
    @DatumPovratka.setter
    def DatumPovratka(self, DatumPovratka: Date):
        self.__DatumPovratka = DatumPovratka

    @property
    def DatumPolaska(self):
        return self.__DatumPolaska
    @DatumPolaska.setter
    def DatumPolaska(self, DatumPolaska: Date):
        self.__DatumPolaska = DatumPolaska

    @property
    def aranzman10(self):
        return self.__aranzman10
    @aranzman10.setter
    def aranzman10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Termin__aranzman10", None)
        self.__aranzman10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "termin11"):
                opp_val = getattr(old_value, "termin11", None)
                if opp_val == self:
                    setattr(old_value, "termin11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "termin11"):
                opp_val = getattr(value, "termin11", None)
                setattr(value, "termin11", self)



class Osiguranje:

    def __init__(self, OsiguranjeID: int, OsigurKuca: str, putnik0: "Putnik" = None):
        self.OsiguranjeID = OsiguranjeID
        self.OsigurKuca = OsigurKuca
        self.putnik0 = putnik0
        
        pass
    @property
    def OsigurKuca(self):
        return self.__OsigurKuca
    @OsigurKuca.setter
    def OsigurKuca(self, OsigurKuca: str):
        self.__OsigurKuca = OsigurKuca

    @property
    def OsiguranjeID(self):
        return self.__OsiguranjeID
    @OsiguranjeID.setter
    def OsiguranjeID(self, OsiguranjeID: int):
        self.__OsiguranjeID = OsiguranjeID

    @property
    def putnik0(self):
        return self.__putnik0
    @putnik0.setter
    def putnik0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Osiguranje__putnik0", None)
        self.__putnik0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "osiguranje1"):
                opp_val = getattr(old_value, "osiguranje1", None)
                if opp_val == self:
                    setattr(old_value, "osiguranje1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "osiguranje1"):
                opp_val = getattr(value, "osiguranje1", None)
                setattr(value, "osiguranje1", self)



class Aranzman:

    def __init__(self, AranzmanID: int, NazivAranzmana: str, BrojMesta: int, Popunjeno: bool, Cena: Double, DestinacijaID: int, TerminID: int, rezervacija6: "Rezervacija" = None, destinacija8: "Destinacija" = None, termin11: "Termin" = None):
        self.AranzmanID = AranzmanID
        self.NazivAranzmana = NazivAranzmana
        self.BrojMesta = BrojMesta
        self.Popunjeno = Popunjeno
        self.Cena = Cena
        self.DestinacijaID = DestinacijaID
        self.TerminID = TerminID
        self.rezervacija6 = rezervacija6
        self.destinacija8 = destinacija8
        self.termin11 = termin11
        
        pass
    @property
    def Popunjeno(self):
        return self.__Popunjeno
    @Popunjeno.setter
    def Popunjeno(self, Popunjeno: bool):
        self.__Popunjeno = Popunjeno

    @property
    def NazivAranzmana(self):
        return self.__NazivAranzmana
    @NazivAranzmana.setter
    def NazivAranzmana(self, NazivAranzmana: str):
        self.__NazivAranzmana = NazivAranzmana

    @property
    def TerminID(self):
        return self.__TerminID
    @TerminID.setter
    def TerminID(self, TerminID: int):
        self.__TerminID = TerminID

    @property
    def DestinacijaID(self):
        return self.__DestinacijaID
    @DestinacijaID.setter
    def DestinacijaID(self, DestinacijaID: int):
        self.__DestinacijaID = DestinacijaID

    @property
    def BrojMesta(self):
        return self.__BrojMesta
    @BrojMesta.setter
    def BrojMesta(self, BrojMesta: int):
        self.__BrojMesta = BrojMesta

    @property
    def AranzmanID(self):
        return self.__AranzmanID
    @AranzmanID.setter
    def AranzmanID(self, AranzmanID: int):
        self.__AranzmanID = AranzmanID

    @property
    def Cena(self):
        return self.__Cena
    @Cena.setter
    def Cena(self, Cena: Double):
        self.__Cena = Cena

    @property
    def rezervacija6(self):
        return self.__rezervacija6
    @rezervacija6.setter
    def rezervacija6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aranzman__rezervacija6", None)
        self.__rezervacija6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aranzman7"):
                opp_val = getattr(old_value, "aranzman7", None)
                if opp_val == self:
                    setattr(old_value, "aranzman7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aranzman7"):
                opp_val = getattr(value, "aranzman7", None)
                setattr(value, "aranzman7", self)

    @property
    def destinacija8(self):
        return self.__destinacija8
    @destinacija8.setter
    def destinacija8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aranzman__destinacija8", None)
        self.__destinacija8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aranzman9"):
                opp_val = getattr(old_value, "aranzman9", None)
                if opp_val == self:
                    setattr(old_value, "aranzman9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aranzman9"):
                opp_val = getattr(value, "aranzman9", None)
                setattr(value, "aranzman9", self)

    @property
    def termin11(self):
        return self.__termin11
    @termin11.setter
    def termin11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aranzman__termin11", None)
        self.__termin11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aranzman10"):
                opp_val = getattr(old_value, "aranzman10", None)
                if opp_val == self:
                    setattr(old_value, "aranzman10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aranzman10"):
                opp_val = getattr(value, "aranzman10", None)
                setattr(value, "aranzman10", self)



class Agent:

    def __init__(self, AgentID: int, ImeAgent: str, PrezimeAgent: str, Email: str, BrojTele: str, Username: str, Password: str, rezervacija5: "Rezervacija" = None):
        self.AgentID = AgentID
        self.ImeAgent = ImeAgent
        self.PrezimeAgent = PrezimeAgent
        self.Email = Email
        self.BrojTele = BrojTele
        self.Username = Username
        self.Password = Password
        self.rezervacija5 = rezervacija5
        
        pass
    @property
    def ImeAgent(self):
        return self.__ImeAgent
    @ImeAgent.setter
    def ImeAgent(self, ImeAgent: str):
        self.__ImeAgent = ImeAgent

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def BrojTele(self):
        return self.__BrojTele
    @BrojTele.setter
    def BrojTele(self, BrojTele: str):
        self.__BrojTele = BrojTele

    @property
    def AgentID(self):
        return self.__AgentID
    @AgentID.setter
    def AgentID(self, AgentID: int):
        self.__AgentID = AgentID

    @property
    def PrezimeAgent(self):
        return self.__PrezimeAgent
    @PrezimeAgent.setter
    def PrezimeAgent(self, PrezimeAgent: str):
        self.__PrezimeAgent = PrezimeAgent

    @property
    def rezervacija5(self):
        return self.__rezervacija5
    @rezervacija5.setter
    def rezervacija5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Agent__rezervacija5", None)
        self.__rezervacija5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agent4"):
                opp_val = getattr(old_value, "agent4", None)
                if opp_val == self:
                    setattr(old_value, "agent4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agent4"):
                opp_val = getattr(value, "agent4", None)
                setattr(value, "agent4", self)



class Rezervacija:

    def __init__(self, ReyervacijaID: int, DatumKreiranja: Date, PutnikID: int, AgentID: int, AranzmanID: int, RacunID: int, putnik3: "Putnik" = None, agent4: "Agent" = None, aranzman7: "Aranzman" = None, racun13: "Racun" = None):
        self.ReyervacijaID = ReyervacijaID
        self.DatumKreiranja = DatumKreiranja
        self.PutnikID = PutnikID
        self.AgentID = AgentID
        self.AranzmanID = AranzmanID
        self.RacunID = RacunID
        self.putnik3 = putnik3
        self.agent4 = agent4
        self.aranzman7 = aranzman7
        self.racun13 = racun13
        
        pass
    @property
    def ReyervacijaID(self):
        return self.__ReyervacijaID
    @ReyervacijaID.setter
    def ReyervacijaID(self, ReyervacijaID: int):
        self.__ReyervacijaID = ReyervacijaID

    @property
    def PutnikID(self):
        return self.__PutnikID
    @PutnikID.setter
    def PutnikID(self, PutnikID: int):
        self.__PutnikID = PutnikID

    @property
    def RacunID(self):
        return self.__RacunID
    @RacunID.setter
    def RacunID(self, RacunID: int):
        self.__RacunID = RacunID

    @property
    def AranzmanID(self):
        return self.__AranzmanID
    @AranzmanID.setter
    def AranzmanID(self, AranzmanID: int):
        self.__AranzmanID = AranzmanID

    @property
    def DatumKreiranja(self):
        return self.__DatumKreiranja
    @DatumKreiranja.setter
    def DatumKreiranja(self, DatumKreiranja: Date):
        self.__DatumKreiranja = DatumKreiranja

    @property
    def AgentID(self):
        return self.__AgentID
    @AgentID.setter
    def AgentID(self, AgentID: int):
        self.__AgentID = AgentID

    @property
    def aranzman7(self):
        return self.__aranzman7
    @aranzman7.setter
    def aranzman7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rezervacija__aranzman7", None)
        self.__aranzman7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rezervacija6"):
                opp_val = getattr(old_value, "rezervacija6", None)
                if opp_val == self:
                    setattr(old_value, "rezervacija6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rezervacija6"):
                opp_val = getattr(value, "rezervacija6", None)
                setattr(value, "rezervacija6", self)

    @property
    def agent4(self):
        return self.__agent4
    @agent4.setter
    def agent4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rezervacija__agent4", None)
        self.__agent4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rezervacija5"):
                opp_val = getattr(old_value, "rezervacija5", None)
                if opp_val == self:
                    setattr(old_value, "rezervacija5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rezervacija5"):
                opp_val = getattr(value, "rezervacija5", None)
                setattr(value, "rezervacija5", self)

    @property
    def racun13(self):
        return self.__racun13
    @racun13.setter
    def racun13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rezervacija__racun13", None)
        self.__racun13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rezervacija12"):
                opp_val = getattr(old_value, "rezervacija12", None)
                if opp_val == self:
                    setattr(old_value, "rezervacija12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rezervacija12"):
                opp_val = getattr(value, "rezervacija12", None)
                setattr(value, "rezervacija12", self)

    @property
    def putnik3(self):
        return self.__putnik3
    @putnik3.setter
    def putnik3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rezervacija__putnik3", None)
        self.__putnik3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rezervacija2"):
                opp_val = getattr(old_value, "rezervacija2", None)
                if opp_val == self:
                    setattr(old_value, "rezervacija2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rezervacija2"):
                opp_val = getattr(value, "rezervacija2", None)
                setattr(value, "rezervacija2", self)



class Putnik:

    def __init__(self, PutnikID: int, ImePutnik: str, PrezimePutnik: str, JMBG: str, Adresa: str, Grad: str, Email: str, BrojTel: str, OsiguranjeID: int, osiguranje1: "Osiguranje" = None, rezervacija2: "Rezervacija" = None):
        self.PutnikID = PutnikID
        self.ImePutnik = ImePutnik
        self.PrezimePutnik = PrezimePutnik
        self.JMBG = JMBG
        self.Adresa = Adresa
        self.Grad = Grad
        self.Email = Email
        self.BrojTel = BrojTel
        self.OsiguranjeID = OsiguranjeID
        self.osiguranje1 = osiguranje1
        self.rezervacija2 = rezervacija2
        
        pass
    @property
    def JMBG(self):
        return self.__JMBG
    @JMBG.setter
    def JMBG(self, JMBG: str):
        self.__JMBG = JMBG

    @property
    def OsiguranjeID(self):
        return self.__OsiguranjeID
    @OsiguranjeID.setter
    def OsiguranjeID(self, OsiguranjeID: int):
        self.__OsiguranjeID = OsiguranjeID

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def PrezimePutnik(self):
        return self.__PrezimePutnik
    @PrezimePutnik.setter
    def PrezimePutnik(self, PrezimePutnik: str):
        self.__PrezimePutnik = PrezimePutnik

    @property
    def Adresa(self):
        return self.__Adresa
    @Adresa.setter
    def Adresa(self, Adresa: str):
        self.__Adresa = Adresa

    @property
    def PutnikID(self):
        return self.__PutnikID
    @PutnikID.setter
    def PutnikID(self, PutnikID: int):
        self.__PutnikID = PutnikID

    @property
    def ImePutnik(self):
        return self.__ImePutnik
    @ImePutnik.setter
    def ImePutnik(self, ImePutnik: str):
        self.__ImePutnik = ImePutnik

    @property
    def BrojTel(self):
        return self.__BrojTel
    @BrojTel.setter
    def BrojTel(self, BrojTel: str):
        self.__BrojTel = BrojTel

    @property
    def Grad(self):
        return self.__Grad
    @Grad.setter
    def Grad(self, Grad: str):
        self.__Grad = Grad

    @property
    def rezervacija2(self):
        return self.__rezervacija2
    @rezervacija2.setter
    def rezervacija2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Putnik__rezervacija2", None)
        self.__rezervacija2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "putnik3"):
                opp_val = getattr(old_value, "putnik3", None)
                if opp_val == self:
                    setattr(old_value, "putnik3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "putnik3"):
                opp_val = getattr(value, "putnik3", None)
                setattr(value, "putnik3", self)

    @property
    def osiguranje1(self):
        return self.__osiguranje1
    @osiguranje1.setter
    def osiguranje1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Putnik__osiguranje1", None)
        self.__osiguranje1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "putnik0"):
                opp_val = getattr(old_value, "putnik0", None)
                if opp_val == self:
                    setattr(old_value, "putnik0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "putnik0"):
                opp_val = getattr(value, "putnik0", None)
                setattr(value, "putnik0", self)



class string:

    pass


class Destinacija:

    def __init__(self, DestinacijaID: int, Drzava: str, Grad: str, Hotel: str, aranzman9: "Aranzman" = None):
        self.DestinacijaID = DestinacijaID
        self.Drzava = Drzava
        self.Grad = Grad
        self.Hotel = Hotel
        self.aranzman9 = aranzman9
        
        pass
    @property
    def Hotel(self):
        return self.__Hotel
    @Hotel.setter
    def Hotel(self, Hotel: str):
        self.__Hotel = Hotel

    @property
    def Grad(self):
        return self.__Grad
    @Grad.setter
    def Grad(self, Grad: str):
        self.__Grad = Grad

    @property
    def Drzava(self):
        return self.__Drzava
    @Drzava.setter
    def Drzava(self, Drzava: str):
        self.__Drzava = Drzava

    @property
    def DestinacijaID(self):
        return self.__DestinacijaID
    @DestinacijaID.setter
    def DestinacijaID(self, DestinacijaID: int):
        self.__DestinacijaID = DestinacijaID

    @property
    def aranzman9(self):
        return self.__aranzman9
    @aranzman9.setter
    def aranzman9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Destinacija__aranzman9", None)
        self.__aranzman9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "destinacija8"):
                opp_val = getattr(old_value, "destinacija8", None)
                if opp_val == self:
                    setattr(old_value, "destinacija8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "destinacija8"):
                opp_val = getattr(value, "destinacija8", None)
                setattr(value, "destinacija8", self)



class Double:

    pass
