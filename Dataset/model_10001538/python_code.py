from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class zutaten:

    def __init__(self, zutatenListe: str, plaetzchen9: "plaetzchen" = None, zutat10: "zutat" = None):
        self.zutatenListe = zutatenListe
        self.plaetzchen9 = plaetzchen9
        self.zutat10 = zutat10
        
        pass
    @property
    def zutatenListe(self):
        return self.__zutatenListe
    @zutatenListe.setter
    def zutatenListe(self, zutatenListe: str):
        self.__zutatenListe = zutatenListe

    @property
    def zutat10(self):
        return self.__zutat10
    @zutat10.setter
    def zutat10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zutaten__zutat10", None)
        self.__zutat10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teig11"):
                opp_val = getattr(old_value, "teig11", None)
                if opp_val == self:
                    setattr(old_value, "teig11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teig11"):
                opp_val = getattr(value, "teig11", None)
                setattr(value, "teig11", self)

    @property
    def plaetzchen9(self):
        return self.__plaetzchen9
    @plaetzchen9.setter
    def plaetzchen9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zutaten__plaetzchen9", None)
        self.__plaetzchen9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teig28"):
                opp_val = getattr(old_value, "teig28", None)
                if opp_val == self:
                    setattr(old_value, "teig28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teig28"):
                opp_val = getattr(value, "teig28", None)
                setattr(value, "teig28", self)



class ea_helfer:

    pass


class backstrasse:

    def __init__(self, BLECHBREITE: str, BLECHLAENGE: str, eingabeAusgabe: str, zutatenVorrat: str, backAuftrag: str, geschwindigkeit: str, ofenlaenge: str, temperatur: str, gestoppt: str, auftrag24: "auftrag" = None, eaHelfer6: "ea_helfer" = None, zutat12: "zutat" = None):
        self.BLECHBREITE = BLECHBREITE
        self.BLECHLAENGE = BLECHLAENGE
        self.eingabeAusgabe = eingabeAusgabe
        self.zutatenVorrat = zutatenVorrat
        self.backAuftrag = backAuftrag
        self.geschwindigkeit = geschwindigkeit
        self.ofenlaenge = ofenlaenge
        self.temperatur = temperatur
        self.gestoppt = gestoppt
        self.auftrag24 = auftrag24
        self.eaHelfer6 = eaHelfer6
        self.zutat12 = zutat12
        
        pass
    @property
    def backAuftrag(self):
        return self.__backAuftrag
    @backAuftrag.setter
    def backAuftrag(self, backAuftrag: str):
        self.__backAuftrag = backAuftrag

    @property
    def BLECHBREITE(self):
        return self.__BLECHBREITE
    @BLECHBREITE.setter
    def BLECHBREITE(self, BLECHBREITE: str):
        self.__BLECHBREITE = BLECHBREITE

    @property
    def zutatenVorrat(self):
        return self.__zutatenVorrat
    @zutatenVorrat.setter
    def zutatenVorrat(self, zutatenVorrat: str):
        self.__zutatenVorrat = zutatenVorrat

    @property
    def BLECHLAENGE(self):
        return self.__BLECHLAENGE
    @BLECHLAENGE.setter
    def BLECHLAENGE(self, BLECHLAENGE: str):
        self.__BLECHLAENGE = BLECHLAENGE

    @property
    def geschwindigkeit(self):
        return self.__geschwindigkeit
    @geschwindigkeit.setter
    def geschwindigkeit(self, geschwindigkeit: str):
        self.__geschwindigkeit = geschwindigkeit

    @property
    def temperatur(self):
        return self.__temperatur
    @temperatur.setter
    def temperatur(self, temperatur: str):
        self.__temperatur = temperatur

    @property
    def ofenlaenge(self):
        return self.__ofenlaenge
    @ofenlaenge.setter
    def ofenlaenge(self, ofenlaenge: str):
        self.__ofenlaenge = ofenlaenge

    @property
    def eingabeAusgabe(self):
        return self.__eingabeAusgabe
    @eingabeAusgabe.setter
    def eingabeAusgabe(self, eingabeAusgabe: str):
        self.__eingabeAusgabe = eingabeAusgabe

    @property
    def gestoppt(self):
        return self.__gestoppt
    @gestoppt.setter
    def gestoppt(self, gestoppt: str):
        self.__gestoppt = gestoppt

    @property
    def auftrag24(self):
        return self.__auftrag24
    @auftrag24.setter
    def auftrag24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backstrasse__auftrag24", None)
        self.__auftrag24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backstrasse5"):
                opp_val = getattr(old_value, "backstrasse5", None)
                if opp_val == self:
                    setattr(old_value, "backstrasse5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backstrasse5"):
                opp_val = getattr(value, "backstrasse5", None)
                setattr(value, "backstrasse5", self)

    @property
    def zutat12(self):
        return self.__zutat12
    @zutat12.setter
    def zutat12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backstrasse__zutat12", None)
        self.__zutat12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backstrasse13"):
                opp_val = getattr(old_value, "backstrasse13", None)
                if opp_val == self:
                    setattr(old_value, "backstrasse13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backstrasse13"):
                opp_val = getattr(value, "backstrasse13", None)
                setattr(value, "backstrasse13", self)

    @property
    def eaHelfer6(self):
        return self.__eaHelfer6
    @eaHelfer6.setter
    def eaHelfer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backstrasse__eaHelfer6", None)
        self.__eaHelfer6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backstrasse7"):
                opp_val = getattr(old_value, "backstrasse7", None)
                if opp_val == self:
                    setattr(old_value, "backstrasse7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backstrasse7"):
                opp_val = getattr(value, "backstrasse7", None)
                setattr(value, "backstrasse7", self)



class auftrag:

    def __init__(self, name: str, auftragsPlaetzchen: str, anzahl: str, plaetzchen22: "plaetzchen" = None, backstrasse5: "backstrasse" = None, zutat15: "zutat" = None):
        self.name = name
        self.auftragsPlaetzchen = auftragsPlaetzchen
        self.anzahl = anzahl
        self.plaetzchen22 = plaetzchen22
        self.backstrasse5 = backstrasse5
        self.zutat15 = zutat15
        
        pass
    @property
    def auftragsPlaetzchen(self):
        return self.__auftragsPlaetzchen
    @auftragsPlaetzchen.setter
    def auftragsPlaetzchen(self, auftragsPlaetzchen: str):
        self.__auftragsPlaetzchen = auftragsPlaetzchen

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def anzahl(self):
        return self.__anzahl
    @anzahl.setter
    def anzahl(self, anzahl: str):
        self.__anzahl = anzahl

    @property
    def backstrasse5(self):
        return self.__backstrasse5
    @backstrasse5.setter
    def backstrasse5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_auftrag__backstrasse5", None)
        self.__backstrasse5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag24"):
                opp_val = getattr(old_value, "auftrag24", None)
                if opp_val == self:
                    setattr(old_value, "auftrag24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag24"):
                opp_val = getattr(value, "auftrag24", None)
                setattr(value, "auftrag24", self)

    @property
    def zutat15(self):
        return self.__zutat15
    @zutat15.setter
    def zutat15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_auftrag__zutat15", None)
        self.__zutat15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag14"):
                opp_val = getattr(old_value, "auftrag14", None)
                if opp_val == self:
                    setattr(old_value, "auftrag14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag14"):
                opp_val = getattr(value, "auftrag14", None)
                setattr(value, "auftrag14", self)

    @property
    def plaetzchen22(self):
        return self.__plaetzchen22
    @plaetzchen22.setter
    def plaetzchen22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_auftrag__plaetzchen22", None)
        self.__plaetzchen22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag3"):
                opp_val = getattr(old_value, "auftrag3", None)
                if opp_val == self:
                    setattr(old_value, "auftrag3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag3"):
                opp_val = getattr(value, "auftrag3", None)
                setattr(value, "auftrag3", self)



class zutat:

    def __init__(self, name: str, menge: str, einheit: str, plaetzchen1: "plaetzchen" = None, teig11: "zutaten" = None, backstrasse13: "backstrasse" = None, auftrag14: "auftrag" = None):
        self.name = name
        self.menge = menge
        self.einheit = einheit
        self.plaetzchen1 = plaetzchen1
        self.teig11 = teig11
        self.backstrasse13 = backstrasse13
        self.auftrag14 = auftrag14
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def einheit(self):
        return self.__einheit
    @einheit.setter
    def einheit(self, einheit: str):
        self.__einheit = einheit

    @property
    def menge(self):
        return self.__menge
    @menge.setter
    def menge(self, menge: str):
        self.__menge = menge

    @property
    def auftrag14(self):
        return self.__auftrag14
    @auftrag14.setter
    def auftrag14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zutat__auftrag14", None)
        self.__auftrag14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat15"):
                opp_val = getattr(old_value, "zutat15", None)
                if opp_val == self:
                    setattr(old_value, "zutat15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat15"):
                opp_val = getattr(value, "zutat15", None)
                setattr(value, "zutat15", self)

    @property
    def teig11(self):
        return self.__teig11
    @teig11.setter
    def teig11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zutat__teig11", None)
        self.__teig11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat10"):
                opp_val = getattr(old_value, "zutat10", None)
                if opp_val == self:
                    setattr(old_value, "zutat10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat10"):
                opp_val = getattr(value, "zutat10", None)
                setattr(value, "zutat10", self)

    @property
    def plaetzchen1(self):
        return self.__plaetzchen1
    @plaetzchen1.setter
    def plaetzchen1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zutat__plaetzchen1", None)
        self.__plaetzchen1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat0"):
                opp_val = getattr(old_value, "zutat0", None)
                if opp_val == self:
                    setattr(old_value, "zutat0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat0"):
                opp_val = getattr(value, "zutat0", None)
                setattr(value, "zutat0", self)

    @property
    def backstrasse13(self):
        return self.__backstrasse13
    @backstrasse13.setter
    def backstrasse13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zutat__backstrasse13", None)
        self.__backstrasse13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat12"):
                opp_val = getattr(old_value, "zutat12", None)
                if opp_val == self:
                    setattr(old_value, "zutat12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat12"):
                opp_val = getattr(value, "zutat12", None)
                setattr(value, "zutat12", self)



class plaetzchen:

    def __init__(self, breite: str, laenge: str, form: str, backzeit: str, temperatur: str, teig: str, belag: str, zutat0: "zutat" = None, auftrag3: "auftrag" = None, teig28: "zutaten" = None):
        self.breite = breite
        self.laenge = laenge
        self.form = form
        self.backzeit = backzeit
        self.temperatur = temperatur
        self.teig = teig
        self.belag = belag
        self.zutat0 = zutat0
        self.auftrag3 = auftrag3
        self.teig28 = teig28
        
        pass
    @property
    def temperatur(self):
        return self.__temperatur
    @temperatur.setter
    def temperatur(self, temperatur: str):
        self.__temperatur = temperatur

    @property
    def form(self):
        return self.__form
    @form.setter
    def form(self, form: str):
        self.__form = form

    @property
    def teig(self):
        return self.__teig
    @teig.setter
    def teig(self, teig: str):
        self.__teig = teig

    @property
    def belag(self):
        return self.__belag
    @belag.setter
    def belag(self, belag: str):
        self.__belag = belag

    @property
    def breite(self):
        return self.__breite
    @breite.setter
    def breite(self, breite: str):
        self.__breite = breite

    @property
    def laenge(self):
        return self.__laenge
    @laenge.setter
    def laenge(self, laenge: str):
        self.__laenge = laenge

    @property
    def backzeit(self):
        return self.__backzeit
    @backzeit.setter
    def backzeit(self, backzeit: str):
        self.__backzeit = backzeit

    @property
    def auftrag3(self):
        return self.__auftrag3
    @auftrag3.setter
    def auftrag3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plaetzchen__auftrag3", None)
        self.__auftrag3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchen22"):
                opp_val = getattr(old_value, "plaetzchen22", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchen22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchen22"):
                opp_val = getattr(value, "plaetzchen22", None)
                setattr(value, "plaetzchen22", self)

    @property
    def teig28(self):
        return self.__teig28
    @teig28.setter
    def teig28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plaetzchen__teig28", None)
        self.__teig28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchen9"):
                opp_val = getattr(old_value, "plaetzchen9", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchen9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchen9"):
                opp_val = getattr(value, "plaetzchen9", None)
                setattr(value, "plaetzchen9", self)

    @property
    def zutat0(self):
        return self.__zutat0
    @zutat0.setter
    def zutat0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plaetzchen__zutat0", None)
        self.__zutat0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchen1"):
                opp_val = getattr(old_value, "plaetzchen1", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchen1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchen1"):
                opp_val = getattr(value, "plaetzchen1", None)
                setattr(value, "plaetzchen1", self)

