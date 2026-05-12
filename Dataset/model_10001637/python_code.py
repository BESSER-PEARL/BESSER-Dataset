from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Auftrag:

    def __init__(self, name: str, keks: str, anzahl: str, dateiEA19: "DateiEA" = None, plaetzchen221: "Plaetzchen" = None, plaetzchenDesignerForm23: "PlaetzchenDesignerForm" = None):
        self.name = name
        self.keks = keks
        self.anzahl = anzahl
        self.dateiEA19 = dateiEA19
        self.plaetzchen221 = plaetzchen221
        self.plaetzchenDesignerForm23 = plaetzchenDesignerForm23
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def keks(self):
        return self.__keks
    @keks.setter
    def keks(self, keks: str):
        self.__keks = keks

    @property
    def anzahl(self):
        return self.__anzahl
    @anzahl.setter
    def anzahl(self, anzahl: str):
        self.__anzahl = anzahl

    @property
    def plaetzchen221(self):
        return self.__plaetzchen221
    @plaetzchen221.setter
    def plaetzchen221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Auftrag__plaetzchen221", None)
        self.__plaetzchen221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag20"):
                opp_val = getattr(old_value, "auftrag20", None)
                if opp_val == self:
                    setattr(old_value, "auftrag20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag20"):
                opp_val = getattr(value, "auftrag20", None)
                setattr(value, "auftrag20", self)

    @property
    def dateiEA19(self):
        return self.__dateiEA19
    @dateiEA19.setter
    def dateiEA19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Auftrag__dateiEA19", None)
        self.__dateiEA19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag18"):
                opp_val = getattr(old_value, "auftrag18", None)
                if opp_val == self:
                    setattr(old_value, "auftrag18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag18"):
                opp_val = getattr(value, "auftrag18", None)
                setattr(value, "auftrag18", self)

    @property
    def plaetzchenDesignerForm23(self):
        return self.__plaetzchenDesignerForm23
    @plaetzchenDesignerForm23.setter
    def plaetzchenDesignerForm23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Auftrag__plaetzchenDesignerForm23", None)
        self.__plaetzchenDesignerForm23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag22"):
                opp_val = getattr(old_value, "auftrag22", None)
                if opp_val == self:
                    setattr(old_value, "auftrag22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag22"):
                opp_val = getattr(value, "auftrag22", None)
                setattr(value, "auftrag22", self)



class ZutatenEingabeForm:

    def __init__(self, neueZutat: str, plaetzchenDesignerForm14: "PlaetzchenDesignerForm" = None, zutat16: "Zutat" = None):
        self.neueZutat = neueZutat
        self.plaetzchenDesignerForm14 = plaetzchenDesignerForm14
        self.zutat16 = zutat16
        
        pass
    @property
    def neueZutat(self):
        return self.__neueZutat
    @neueZutat.setter
    def neueZutat(self, neueZutat: str):
        self.__neueZutat = neueZutat

    @property
    def plaetzchenDesignerForm14(self):
        return self.__plaetzchenDesignerForm14
    @plaetzchenDesignerForm14.setter
    def plaetzchenDesignerForm14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZutatenEingabeForm__plaetzchenDesignerForm14", None)
        self.__plaetzchenDesignerForm14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutatenEingabe15"):
                opp_val = getattr(old_value, "zutatenEingabe15", None)
                if opp_val == self:
                    setattr(old_value, "zutatenEingabe15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutatenEingabe15"):
                opp_val = getattr(value, "zutatenEingabe15", None)
                setattr(value, "zutatenEingabe15", self)

    @property
    def zutat16(self):
        return self.__zutat16
    @zutat16.setter
    def zutat16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZutatenEingabeForm__zutat16", None)
        self.__zutat16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutatenEingabe17"):
                opp_val = getattr(old_value, "zutatenEingabe17", None)
                if opp_val == self:
                    setattr(old_value, "zutatenEingabe17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutatenEingabe17"):
                opp_val = getattr(value, "zutatenEingabe17", None)
                setattr(value, "zutatenEingabe17", self)



class PlaetzchenAnzeigeForm:

    def __init__(self, form: str, breite: str, laenge: str, plaetzchenDesignerForm9: "PlaetzchenDesignerForm" = None):
        self.form = form
        self.breite = breite
        self.laenge = laenge
        self.plaetzchenDesignerForm9 = plaetzchenDesignerForm9
        
        pass
    @property
    def form(self):
        return self.__form
    @form.setter
    def form(self, form: str):
        self.__form = form

    @property
    def laenge(self):
        return self.__laenge
    @laenge.setter
    def laenge(self, laenge: str):
        self.__laenge = laenge

    @property
    def breite(self):
        return self.__breite
    @breite.setter
    def breite(self, breite: str):
        self.__breite = breite

    @property
    def plaetzchenDesignerForm9(self):
        return self.__plaetzchenDesignerForm9
    @plaetzchenDesignerForm9.setter
    def plaetzchenDesignerForm9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlaetzchenAnzeigeForm__plaetzchenDesignerForm9", None)
        self.__plaetzchenDesignerForm9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenAnzeigeForm8"):
                opp_val = getattr(old_value, "plaetzchenAnzeigeForm8", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenAnzeigeForm8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenAnzeigeForm8"):
                opp_val = getattr(value, "plaetzchenAnzeigeForm8", None)
                setattr(value, "plaetzchenAnzeigeForm8", self)



class DateiEA:

    pass


class PlaetzchenDesignerForm:

    def __init__(self, BLECHBREITE: str, BLECHLAENGE: str, datei: str, neuerAuftrag: str, neuesPlaetzchen: str, plaetzchenGeaendert: bool, dateiEA6: "DateiEA" = None, plaetzchenAnzeigeForm8: "PlaetzchenAnzeigeForm" = None, plaetzchen10: "Plaetzchen" = None, zutatenEingabe15: "ZutatenEingabeForm" = None, auftrag22: "Auftrag" = None):
        self.BLECHBREITE = BLECHBREITE
        self.BLECHLAENGE = BLECHLAENGE
        self.datei = datei
        self.neuerAuftrag = neuerAuftrag
        self.neuesPlaetzchen = neuesPlaetzchen
        self.plaetzchenGeaendert = plaetzchenGeaendert
        self.dateiEA6 = dateiEA6
        self.plaetzchenAnzeigeForm8 = plaetzchenAnzeigeForm8
        self.plaetzchen10 = plaetzchen10
        self.zutatenEingabe15 = zutatenEingabe15
        self.auftrag22 = auftrag22
        
        pass
    @property
    def neuesPlaetzchen(self):
        return self.__neuesPlaetzchen
    @neuesPlaetzchen.setter
    def neuesPlaetzchen(self, neuesPlaetzchen: str):
        self.__neuesPlaetzchen = neuesPlaetzchen

    @property
    def BLECHBREITE(self):
        return self.__BLECHBREITE
    @BLECHBREITE.setter
    def BLECHBREITE(self, BLECHBREITE: str):
        self.__BLECHBREITE = BLECHBREITE

    @property
    def BLECHLAENGE(self):
        return self.__BLECHLAENGE
    @BLECHLAENGE.setter
    def BLECHLAENGE(self, BLECHLAENGE: str):
        self.__BLECHLAENGE = BLECHLAENGE

    @property
    def neuerAuftrag(self):
        return self.__neuerAuftrag
    @neuerAuftrag.setter
    def neuerAuftrag(self, neuerAuftrag: str):
        self.__neuerAuftrag = neuerAuftrag

    @property
    def plaetzchenGeaendert(self):
        return self.__plaetzchenGeaendert
    @plaetzchenGeaendert.setter
    def plaetzchenGeaendert(self, plaetzchenGeaendert: bool):
        self.__plaetzchenGeaendert = plaetzchenGeaendert

    @property
    def datei(self):
        return self.__datei
    @datei.setter
    def datei(self, datei: str):
        self.__datei = datei

    @property
    def zutatenEingabe15(self):
        return self.__zutatenEingabe15
    @zutatenEingabe15.setter
    def zutatenEingabe15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlaetzchenDesignerForm__zutatenEingabe15", None)
        self.__zutatenEingabe15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenDesignerForm14"):
                opp_val = getattr(old_value, "plaetzchenDesignerForm14", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenDesignerForm14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenDesignerForm14"):
                opp_val = getattr(value, "plaetzchenDesignerForm14", None)
                setattr(value, "plaetzchenDesignerForm14", self)

    @property
    def plaetzchen10(self):
        return self.__plaetzchen10
    @plaetzchen10.setter
    def plaetzchen10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlaetzchenDesignerForm__plaetzchen10", None)
        self.__plaetzchen10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenDesignerForm11"):
                opp_val = getattr(old_value, "plaetzchenDesignerForm11", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenDesignerForm11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenDesignerForm11"):
                opp_val = getattr(value, "plaetzchenDesignerForm11", None)
                setattr(value, "plaetzchenDesignerForm11", self)

    @property
    def dateiEA6(self):
        return self.__dateiEA6
    @dateiEA6.setter
    def dateiEA6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlaetzchenDesignerForm__dateiEA6", None)
        self.__dateiEA6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenDesignerForm7"):
                opp_val = getattr(old_value, "plaetzchenDesignerForm7", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenDesignerForm7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenDesignerForm7"):
                opp_val = getattr(value, "plaetzchenDesignerForm7", None)
                setattr(value, "plaetzchenDesignerForm7", self)

    @property
    def plaetzchenAnzeigeForm8(self):
        return self.__plaetzchenAnzeigeForm8
    @plaetzchenAnzeigeForm8.setter
    def plaetzchenAnzeigeForm8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlaetzchenDesignerForm__plaetzchenAnzeigeForm8", None)
        self.__plaetzchenAnzeigeForm8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenDesignerForm9"):
                opp_val = getattr(old_value, "plaetzchenDesignerForm9", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenDesignerForm9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenDesignerForm9"):
                opp_val = getattr(value, "plaetzchenDesignerForm9", None)
                setattr(value, "plaetzchenDesignerForm9", self)

    @property
    def auftrag22(self):
        return self.__auftrag22
    @auftrag22.setter
    def auftrag22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlaetzchenDesignerForm__auftrag22", None)
        self.__auftrag22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenDesignerForm23"):
                opp_val = getattr(old_value, "plaetzchenDesignerForm23", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenDesignerForm23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenDesignerForm23"):
                opp_val = getattr(value, "plaetzchenDesignerForm23", None)
                setattr(value, "plaetzchenDesignerForm23", self)



class Plaetzchen:

    def __init__(self, breite: str, laenge: str, form: str, backzeit: str, temperatur: str, teig: str, belag: str, plaetzchenDesignerForm11: "PlaetzchenDesignerForm" = None, dateiEA13: "DateiEA" = None, auftrag20: "Auftrag" = None, teig20: "Zutaten" = None, zutat2: "Zutat" = None):
        self.breite = breite
        self.laenge = laenge
        self.form = form
        self.backzeit = backzeit
        self.temperatur = temperatur
        self.teig = teig
        self.belag = belag
        self.plaetzchenDesignerForm11 = plaetzchenDesignerForm11
        self.dateiEA13 = dateiEA13
        self.auftrag20 = auftrag20
        self.teig20 = teig20
        self.zutat2 = zutat2
        
        pass
    @property
    def teig(self):
        return self.__teig
    @teig.setter
    def teig(self, teig: str):
        self.__teig = teig

    @property
    def temperatur(self):
        return self.__temperatur
    @temperatur.setter
    def temperatur(self, temperatur: str):
        self.__temperatur = temperatur

    @property
    def laenge(self):
        return self.__laenge
    @laenge.setter
    def laenge(self, laenge: str):
        self.__laenge = laenge

    @property
    def breite(self):
        return self.__breite
    @breite.setter
    def breite(self, breite: str):
        self.__breite = breite

    @property
    def form(self):
        return self.__form
    @form.setter
    def form(self, form: str):
        self.__form = form

    @property
    def backzeit(self):
        return self.__backzeit
    @backzeit.setter
    def backzeit(self, backzeit: str):
        self.__backzeit = backzeit

    @property
    def belag(self):
        return self.__belag
    @belag.setter
    def belag(self, belag: str):
        self.__belag = belag

    @property
    def dateiEA13(self):
        return self.__dateiEA13
    @dateiEA13.setter
    def dateiEA13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plaetzchen__dateiEA13", None)
        self.__dateiEA13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchen12"):
                opp_val = getattr(old_value, "plaetzchen12", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchen12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchen12"):
                opp_val = getattr(value, "plaetzchen12", None)
                setattr(value, "plaetzchen12", self)

    @property
    def auftrag20(self):
        return self.__auftrag20
    @auftrag20.setter
    def auftrag20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plaetzchen__auftrag20", None)
        self.__auftrag20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchen221"):
                opp_val = getattr(old_value, "plaetzchen221", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchen221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchen221"):
                opp_val = getattr(value, "plaetzchen221", None)
                setattr(value, "plaetzchen221", self)

    @property
    def zutat2(self):
        return self.__zutat2
    @zutat2.setter
    def zutat2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plaetzchen__zutat2", None)
        self.__zutat2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchen3"):
                opp_val = getattr(old_value, "plaetzchen3", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchen3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchen3"):
                opp_val = getattr(value, "plaetzchen3", None)
                setattr(value, "plaetzchen3", self)

    @property
    def teig20(self):
        return self.__teig20
    @teig20.setter
    def teig20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plaetzchen__teig20", None)
        self.__teig20 = value
        
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

    @property
    def plaetzchenDesignerForm11(self):
        return self.__plaetzchenDesignerForm11
    @plaetzchenDesignerForm11.setter
    def plaetzchenDesignerForm11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plaetzchen__plaetzchenDesignerForm11", None)
        self.__plaetzchenDesignerForm11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchen10"):
                opp_val = getattr(old_value, "plaetzchen10", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchen10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchen10"):
                opp_val = getattr(value, "plaetzchen10", None)
                setattr(value, "plaetzchen10", self)



class Zutat:

    def __init__(self, name: str, einheit: str, menge: str, teig5: "Zutaten" = None, zutatenEingabe17: "ZutatenEingabeForm" = None, plaetzchen3: "Plaetzchen" = None):
        self.name = name
        self.einheit = einheit
        self.menge = menge
        self.teig5 = teig5
        self.zutatenEingabe17 = zutatenEingabe17
        self.plaetzchen3 = plaetzchen3
        
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
    def zutatenEingabe17(self):
        return self.__zutatenEingabe17
    @zutatenEingabe17.setter
    def zutatenEingabe17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Zutat__zutatenEingabe17", None)
        self.__zutatenEingabe17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat16"):
                opp_val = getattr(old_value, "zutat16", None)
                if opp_val == self:
                    setattr(old_value, "zutat16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat16"):
                opp_val = getattr(value, "zutat16", None)
                setattr(value, "zutat16", self)

    @property
    def plaetzchen3(self):
        return self.__plaetzchen3
    @plaetzchen3.setter
    def plaetzchen3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Zutat__plaetzchen3", None)
        self.__plaetzchen3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat2"):
                opp_val = getattr(old_value, "zutat2", None)
                if opp_val == self:
                    setattr(old_value, "zutat2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat2"):
                opp_val = getattr(value, "zutat2", None)
                setattr(value, "zutat2", self)

    @property
    def teig5(self):
        return self.__teig5
    @teig5.setter
    def teig5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Zutat__teig5", None)
        self.__teig5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat4"):
                opp_val = getattr(old_value, "zutat4", None)
                if opp_val == self:
                    setattr(old_value, "zutat4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat4"):
                opp_val = getattr(value, "zutat4", None)
                setattr(value, "zutat4", self)



class Zutaten:

    def __init__(self, zutaten: str, zutat4: "Zutat" = None, plaetzchen1: "Plaetzchen" = None):
        self.zutaten = zutaten
        self.zutat4 = zutat4
        self.plaetzchen1 = plaetzchen1
        
        pass
    @property
    def zutaten(self):
        return self.__zutaten
    @zutaten.setter
    def zutaten(self, zutaten: str):
        self.__zutaten = zutaten

    @property
    def zutat4(self):
        return self.__zutat4
    @zutat4.setter
    def zutat4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Zutaten__zutat4", None)
        self.__zutat4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teig5"):
                opp_val = getattr(old_value, "teig5", None)
                if opp_val == self:
                    setattr(old_value, "teig5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teig5"):
                opp_val = getattr(value, "teig5", None)
                setattr(value, "teig5", self)

    @property
    def plaetzchen1(self):
        return self.__plaetzchen1
    @plaetzchen1.setter
    def plaetzchen1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Zutaten__plaetzchen1", None)
        self.__plaetzchen1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teig20"):
                opp_val = getattr(old_value, "teig20", None)
                if opp_val == self:
                    setattr(old_value, "teig20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teig20"):
                opp_val = getattr(value, "teig20", None)
                setattr(value, "teig20", self)

