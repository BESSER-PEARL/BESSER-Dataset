from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ExemplarStatus(Enum):
    pass

############################################
# Definition of Classes
############################################










class Reservierung:

    def __init__(self, reservierungsDatum: str, reservierungsEnde: str, geh_rt_zu7: "Kunde" = None, anzahl_Exem_8: set["Exemplar"] = None):
        self.reservierungsDatum = reservierungsDatum
        self.reservierungsEnde = reservierungsEnde
        self.geh_rt_zu7 = geh_rt_zu7
        self.anzahl_Exem_8 = anzahl_Exem_8 if anzahl_Exem_8 is not None else set()
        
        pass
    @property
    def reservierungsEnde(self):
        return self.__reservierungsEnde
    @reservierungsEnde.setter
    def reservierungsEnde(self, reservierungsEnde: str):
        self.__reservierungsEnde = reservierungsEnde

    @property
    def reservierungsDatum(self):
        return self.__reservierungsDatum
    @reservierungsDatum.setter
    def reservierungsDatum(self, reservierungsDatum: str):
        self.__reservierungsDatum = reservierungsDatum

    @property
    def anzahl_Exem_8(self):
        return self.__anzahl_Exem_8
    @anzahl_Exem_8.setter
    def anzahl_Exem_8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reservierung__anzahl_Exem_8", None)
        self.__anzahl_Exem_8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wir_reserviert9"):
                    opp_val = getattr(item, "wir_reserviert9", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wir_reserviert9"):
                    opp_val = getattr(item, "wir_reserviert9", None)
                    
                    if opp_val is None:
                        setattr(item, "wir_reserviert9", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def geh_rt_zu7(self):
        return self.__geh_rt_zu7
    @geh_rt_zu7.setter
    def geh_rt_zu7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reservierung__geh_rt_zu7", None)
        self.__geh_rt_zu7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anzahl6"):
                opp_val = getattr(old_value, "anzahl6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anzahl6"):
                opp_val = getattr(value, "anzahl6", None)
                if opp_val is None:
                    setattr(value, "anzahl6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Entlehnausweis:

    def __init__(self, id: int, g_ltigKeitsDatum: str, geh_rt_zu5: "Kunde" = None):
        self.id = id
        self.g_ltigKeitsDatum = g_ltigKeitsDatum
        self.geh_rt_zu5 = geh_rt_zu5
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def g_ltigKeitsDatum(self):
        return self.__g_ltigKeitsDatum
    @g_ltigKeitsDatum.setter
    def g_ltigKeitsDatum(self, g_ltigKeitsDatum: str):
        self.__g_ltigKeitsDatum = g_ltigKeitsDatum

    @property
    def geh_rt_zu5(self):
        return self.__geh_rt_zu5
    @geh_rt_zu5.setter
    def geh_rt_zu5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entlehnausweis__geh_rt_zu5", None)
        self.__geh_rt_zu5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hat_einen4"):
                opp_val = getattr(old_value, "hat_einen4", None)
                if opp_val == self:
                    setattr(old_value, "hat_einen4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hat_einen4"):
                opp_val = getattr(value, "hat_einen4", None)
                setattr(value, "hat_einen4", self)



class Kunde:

    def __init__(self, Anschrift: str, Name: str, anzahl2: set["Entlehnung"] = None, hat_einen4: "Entlehnausweis" = None, anzahl6: set["Reservierung"] = None):
        self.Anschrift = Anschrift
        self.Name = Name
        self.anzahl2 = anzahl2 if anzahl2 is not None else set()
        self.hat_einen4 = hat_einen4
        self.anzahl6 = anzahl6 if anzahl6 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Anschrift(self):
        return self.__Anschrift
    @Anschrift.setter
    def Anschrift(self, Anschrift: str):
        self.__Anschrift = Anschrift

    @property
    def anzahl6(self):
        return self.__anzahl6
    @anzahl6.setter
    def anzahl6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kunde__anzahl6", None)
        self.__anzahl6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "geh_rt_zu7"):
                    opp_val = getattr(item, "geh_rt_zu7", None)
                    
                    if opp_val == self:
                        setattr(item, "geh_rt_zu7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "geh_rt_zu7"):
                    opp_val = getattr(item, "geh_rt_zu7", None)
                    
                    setattr(item, "geh_rt_zu7", self)
                    

    @property
    def hat_einen4(self):
        return self.__hat_einen4
    @hat_einen4.setter
    def hat_einen4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kunde__hat_einen4", None)
        self.__hat_einen4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "geh_rt_zu5"):
                opp_val = getattr(old_value, "geh_rt_zu5", None)
                if opp_val == self:
                    setattr(old_value, "geh_rt_zu5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "geh_rt_zu5"):
                opp_val = getattr(value, "geh_rt_zu5", None)
                setattr(value, "geh_rt_zu5", self)

    @property
    def anzahl2(self):
        return self.__anzahl2
    @anzahl2.setter
    def anzahl2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kunde__anzahl2", None)
        self.__anzahl2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "geh_rt_zu3"):
                    opp_val = getattr(item, "geh_rt_zu3", None)
                    
                    if opp_val == self:
                        setattr(item, "geh_rt_zu3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "geh_rt_zu3"):
                    opp_val = getattr(item, "geh_rt_zu3", None)
                    
                    setattr(item, "geh_rt_zu3", self)
                    



class Entlehnung:

    def __init__(self, ausLeihDatun: str, rueckGDatum: str, ausLeihFrist: str, maxAnzahlFristTage: int, anzahl_Exem_1: set["Exemplar"] = None, geh_rt_zu3: "Kunde" = None):
        self.ausLeihDatun = ausLeihDatun
        self.rueckGDatum = rueckGDatum
        self.ausLeihFrist = ausLeihFrist
        self.maxAnzahlFristTage = maxAnzahlFristTage
        self.anzahl_Exem_1 = anzahl_Exem_1 if anzahl_Exem_1 is not None else set()
        self.geh_rt_zu3 = geh_rt_zu3
        
        pass
    @property
    def ausLeihFrist(self):
        return self.__ausLeihFrist
    @ausLeihFrist.setter
    def ausLeihFrist(self, ausLeihFrist: str):
        self.__ausLeihFrist = ausLeihFrist

    @property
    def maxAnzahlFristTage(self):
        return self.__maxAnzahlFristTage
    @maxAnzahlFristTage.setter
    def maxAnzahlFristTage(self, maxAnzahlFristTage: int):
        self.__maxAnzahlFristTage = maxAnzahlFristTage

    @property
    def rueckGDatum(self):
        return self.__rueckGDatum
    @rueckGDatum.setter
    def rueckGDatum(self, rueckGDatum: str):
        self.__rueckGDatum = rueckGDatum

    @property
    def ausLeihDatun(self):
        return self.__ausLeihDatun
    @ausLeihDatun.setter
    def ausLeihDatun(self, ausLeihDatun: str):
        self.__ausLeihDatun = ausLeihDatun

    @property
    def geh_rt_zu3(self):
        return self.__geh_rt_zu3
    @geh_rt_zu3.setter
    def geh_rt_zu3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entlehnung__geh_rt_zu3", None)
        self.__geh_rt_zu3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anzahl2"):
                opp_val = getattr(old_value, "anzahl2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anzahl2"):
                opp_val = getattr(value, "anzahl2", None)
                if opp_val is None:
                    setattr(value, "anzahl2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def anzahl_Exem_1(self):
        return self.__anzahl_Exem_1
    @anzahl_Exem_1.setter
    def anzahl_Exem_1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entlehnung__anzahl_Exem_1", None)
        self.__anzahl_Exem_1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wird_Entlehnt0"):
                    opp_val = getattr(item, "wird_Entlehnt0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wird_Entlehnt0"):
                    opp_val = getattr(item, "wird_Entlehnt0", None)
                    
                    if opp_val is None:
                        setattr(item, "wird_Entlehnt0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Exemplar:

    def __init__(self, exemplarNummer: str, wird_Entlehnt0: set["Entlehnung"] = None, wir_reserviert9: set["Reservierung"] = None, hat11: "Entleihungsgegenstand" = None):
        self.exemplarNummer = exemplarNummer
        self.wird_Entlehnt0 = wird_Entlehnt0 if wird_Entlehnt0 is not None else set()
        self.wir_reserviert9 = wir_reserviert9 if wir_reserviert9 is not None else set()
        self.hat11 = hat11
        
        pass
    @property
    def exemplarNummer(self):
        return self.__exemplarNummer
    @exemplarNummer.setter
    def exemplarNummer(self, exemplarNummer: str):
        self.__exemplarNummer = exemplarNummer

    @property
    def wird_Entlehnt0(self):
        return self.__wird_Entlehnt0
    @wird_Entlehnt0.setter
    def wird_Entlehnt0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Exemplar__wird_Entlehnt0", None)
        self.__wird_Entlehnt0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "anzahl_Exem_1"):
                    opp_val = getattr(item, "anzahl_Exem_1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "anzahl_Exem_1"):
                    opp_val = getattr(item, "anzahl_Exem_1", None)
                    
                    if opp_val is None:
                        setattr(item, "anzahl_Exem_1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def hat11(self):
        return self.__hat11
    @hat11.setter
    def hat11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Exemplar__hat11", None)
        self.__hat11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "geh_rt_zu10"):
                opp_val = getattr(old_value, "geh_rt_zu10", None)
                if opp_val == self:
                    setattr(old_value, "geh_rt_zu10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "geh_rt_zu10"):
                opp_val = getattr(value, "geh_rt_zu10", None)
                setattr(value, "geh_rt_zu10", self)

    @property
    def wir_reserviert9(self):
        return self.__wir_reserviert9
    @wir_reserviert9.setter
    def wir_reserviert9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Exemplar__wir_reserviert9", None)
        self.__wir_reserviert9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "anzahl_Exem_8"):
                    opp_val = getattr(item, "anzahl_Exem_8", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "anzahl_Exem_8"):
                    opp_val = getattr(item, "anzahl_Exem_8", None)
                    
                    if opp_val is None:
                        setattr(item, "anzahl_Exem_8", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Entleihungsgegenstand(ABC):

    def __init__(self, einkaufspreis: str, kurzbeschreibung: str, titel: str, geh_rt_zu10: "Exemplar" = None):
        self.einkaufspreis = einkaufspreis
        self.kurzbeschreibung = kurzbeschreibung
        self.titel = titel
        self.geh_rt_zu10 = geh_rt_zu10
        
        pass
    @property
    def einkaufspreis(self):
        return self.__einkaufspreis
    @einkaufspreis.setter
    def einkaufspreis(self, einkaufspreis: str):
        self.__einkaufspreis = einkaufspreis

    @property
    def titel(self):
        return self.__titel
    @titel.setter
    def titel(self, titel: str):
        self.__titel = titel

    @property
    def kurzbeschreibung(self):
        return self.__kurzbeschreibung
    @kurzbeschreibung.setter
    def kurzbeschreibung(self, kurzbeschreibung: str):
        self.__kurzbeschreibung = kurzbeschreibung

    @property
    def geh_rt_zu10(self):
        return self.__geh_rt_zu10
    @geh_rt_zu10.setter
    def geh_rt_zu10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Entleihungsgegenstand__geh_rt_zu10", None)
        self.__geh_rt_zu10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hat11"):
                opp_val = getattr(old_value, "hat11", None)
                if opp_val == self:
                    setattr(old_value, "hat11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hat11"):
                opp_val = getattr(value, "hat11", None)
                setattr(value, "hat11", self)



class Zeitschrift:

    def __init__(self, Ausgabe: str, Jahrgang: int):
        self.Ausgabe = Ausgabe
        self.Jahrgang = Jahrgang
        
        pass
    @property
    def Jahrgang(self):
        return self.__Jahrgang
    @Jahrgang.setter
    def Jahrgang(self, Jahrgang: int):
        self.__Jahrgang = Jahrgang

    @property
    def Ausgabe(self):
        return self.__Ausgabe
    @Ausgabe.setter
    def Ausgabe(self, Ausgabe: str):
        self.__Ausgabe = Ausgabe



class Videos_DVDS:

    def __init__(self, Laufzeit: int, Regisseur: str, entLeihungsGeb_hr: str, AnzahlEntlehnungen: int):
        self.Laufzeit = Laufzeit
        self.Regisseur = Regisseur
        self.entLeihungsGeb_hr = entLeihungsGeb_hr
        self.AnzahlEntlehnungen = AnzahlEntlehnungen
        
        pass
    @property
    def AnzahlEntlehnungen(self):
        return self.__AnzahlEntlehnungen
    @AnzahlEntlehnungen.setter
    def AnzahlEntlehnungen(self, AnzahlEntlehnungen: int):
        self.__AnzahlEntlehnungen = AnzahlEntlehnungen

    @property
    def Laufzeit(self):
        return self.__Laufzeit
    @Laufzeit.setter
    def Laufzeit(self, Laufzeit: int):
        self.__Laufzeit = Laufzeit

    @property
    def Regisseur(self):
        return self.__Regisseur
    @Regisseur.setter
    def Regisseur(self, Regisseur: str):
        self.__Regisseur = Regisseur

    @property
    def entLeihungsGeb_hr(self):
        return self.__entLeihungsGeb_hr
    @entLeihungsGeb_hr.setter
    def entLeihungsGeb_hr(self, entLeihungsGeb_hr: str):
        self.__entLeihungsGeb_hr = entLeihungsGeb_hr



class Buch:

    def __init__(self, ISBN: str, Autor: str):
        self.ISBN = ISBN
        self.Autor = Autor
        
        pass
    @property
    def Autor(self):
        return self.__Autor
    @Autor.setter
    def Autor(self, Autor: str):
        self.__Autor = Autor

    @property
    def ISBN(self):
        return self.__ISBN
    @ISBN.setter
    def ISBN(self, ISBN: str):
        self.__ISBN = ISBN

