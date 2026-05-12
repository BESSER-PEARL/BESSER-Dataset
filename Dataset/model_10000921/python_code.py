from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PL_Groesse(Enum):
    pass
class PL_Form(Enum):
    pass

############################################
# Definition of Classes
############################################










class KeyPressEventArgs_:

    pass


class myException:

    pass


class Font_2:

    pass


class Font_:

    pass


class ThreadExceptionEventArgs_:

    pass


class Object_:

    pass


class App:

    pass


class Groesse_:

    pass


class PL_Form_:

    pass


class PL_Groesse_:

    pass


class List_TeigRezept___:

    pass


class Array_Zutat___:

    pass


class List_DekorRezept___:

    pass


class List_PlaetzchenForm___:

    pass


class List_Zutat___:

    pass


class GussRezept:

    def __init__(self, basismenge: int, zutat: Zutat, basis: PlaetzchenForm_):
        self.basismenge = basismenge
        self.zutat = zutat
        self.basis = basis
        
        pass
    @property
    def basismenge(self):
        return self.__basismenge
    @basismenge.setter
    def basismenge(self, basismenge: int):
        self.__basismenge = basismenge

    @property
    def basis(self):
        return self.__basis
    @basis.setter
    def basis(self, basis: PlaetzchenForm_):
        self.__basis = basis

    @property
    def zutat(self):
        return self.__zutat
    @zutat.setter
    def zutat(self, zutat: Zutat):
        self.__zutat = zutat



class Zutat_:

    pass


class Rezept:

    def __init__(self, rezeptname: String_, basis: PlaetzchenForm_, basismenge: int, attribute: str, attribute2: str, plaetzchenForm9: "PlaetzchenForm" = None):
        self.rezeptname = rezeptname
        self.basis = basis
        self.basismenge = basismenge
        self.attribute = attribute
        self.attribute2 = attribute2
        self.plaetzchenForm9 = plaetzchenForm9
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def basismenge(self):
        return self.__basismenge
    @basismenge.setter
    def basismenge(self, basismenge: int):
        self.__basismenge = basismenge

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def rezeptname(self):
        return self.__rezeptname
    @rezeptname.setter
    def rezeptname(self, rezeptname: String_):
        self.__rezeptname = rezeptname

    @property
    def basis(self):
        return self.__basis
    @basis.setter
    def basis(self, basis: PlaetzchenForm_):
        self.__basis = basis

    @property
    def plaetzchenForm9(self):
        return self.__plaetzchenForm9
    @plaetzchenForm9.setter
    def plaetzchenForm9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rezept__plaetzchenForm9", None)
        self.__plaetzchenForm9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teigRezept8"):
                opp_val = getattr(old_value, "teigRezept8", None)
                if opp_val == self:
                    setattr(old_value, "teigRezept8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teigRezept8"):
                opp_val = getattr(value, "teigRezept8", None)
                setattr(value, "teigRezept8", self)



class DekorRezept:

    def __init__(self, basismenge: int, zutaten: List_Zutat___, basis: PlaetzchenForm_, dekor: Zutat_, zutat22: "Zutat" = None, gUI24: "GUI" = None):
        self.basismenge = basismenge
        self.zutaten = zutaten
        self.basis = basis
        self.dekor = dekor
        self.zutat22 = zutat22
        self.gUI24 = gUI24
        
        pass
    @property
    def dekor(self):
        return self.__dekor
    @dekor.setter
    def dekor(self, dekor: Zutat_):
        self.__dekor = dekor

    @property
    def basismenge(self):
        return self.__basismenge
    @basismenge.setter
    def basismenge(self, basismenge: int):
        self.__basismenge = basismenge

    @property
    def basis(self):
        return self.__basis
    @basis.setter
    def basis(self, basis: PlaetzchenForm_):
        self.__basis = basis

    @property
    def zutaten(self):
        return self.__zutaten
    @zutaten.setter
    def zutaten(self, zutaten: List_Zutat___):
        self.__zutaten = zutaten

    @property
    def zutat22(self):
        return self.__zutat22
    @zutat22.setter
    def zutat22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DekorRezept__zutat22", None)
        self.__zutat22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dekorRezept23"):
                opp_val = getattr(old_value, "dekorRezept23", None)
                if opp_val == self:
                    setattr(old_value, "dekorRezept23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dekorRezept23"):
                opp_val = getattr(value, "dekorRezept23", None)
                setattr(value, "dekorRezept23", self)

    @property
    def gUI24(self):
        return self.__gUI24
    @gUI24.setter
    def gUI24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DekorRezept__gUI24", None)
        self.__gUI24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dekorRezept25"):
                opp_val = getattr(old_value, "dekorRezept25", None)
                if opp_val == self:
                    setattr(old_value, "dekorRezept25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dekorRezept25"):
                opp_val = getattr(value, "dekorRezept25", None)
                setattr(value, "dekorRezept25", self)



class GUIRezept:

    def __init__(self, name: str, gUI17: "GUI" = None, teigRezept18: "TeigRezept" = None):
        self.name = name
        self.gUI17 = gUI17
        self.teigRezept18 = teigRezept18
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def teigRezept18(self):
        return self.__teigRezept18
    @teigRezept18.setter
    def teigRezept18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUIRezept__teigRezept18", None)
        self.__teigRezept18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUIRezept19"):
                opp_val = getattr(old_value, "gUIRezept19", None)
                if opp_val == self:
                    setattr(old_value, "gUIRezept19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUIRezept19"):
                opp_val = getattr(value, "gUIRezept19", None)
                setattr(value, "gUIRezept19", self)

    @property
    def gUI17(self):
        return self.__gUI17
    @gUI17.setter
    def gUI17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUIRezept__gUI17", None)
        self.__gUI17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUIRezept16"):
                opp_val = getattr(old_value, "gUIRezept16", None)
                if opp_val == self:
                    setattr(old_value, "gUIRezept16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUIRezept16"):
                opp_val = getattr(value, "gUIRezept16", None)
                setattr(value, "gUIRezept16", self)



class String_:

    pass


class PlaetzchenForm_:

    pass


class ComboBox:

    pass


class Plaetzchen_:

    pass


class Plaetzchen:

    def __init__(self, name: String_, teig: List_Zutat___, form: PlaetzchenForm_, guss: Zutat_, deko: Zutat_, menge: int, rezeptTeig: TeigRezept_, rezeptGuss: str, rezeptDeko: str, plaetzchenForm3: "PlaetzchenForm" = None):
        self.name = name
        self.teig = teig
        self.form = form
        self.guss = guss
        self.deko = deko
        self.menge = menge
        self.rezeptTeig = rezeptTeig
        self.rezeptGuss = rezeptGuss
        self.rezeptDeko = rezeptDeko
        self.plaetzchenForm3 = plaetzchenForm3
        
        pass
    @property
    def rezeptDeko(self):
        return self.__rezeptDeko
    @rezeptDeko.setter
    def rezeptDeko(self, rezeptDeko: str):
        self.__rezeptDeko = rezeptDeko

    @property
    def teig(self):
        return self.__teig
    @teig.setter
    def teig(self, teig: List_Zutat___):
        self.__teig = teig

    @property
    def menge(self):
        return self.__menge
    @menge.setter
    def menge(self, menge: int):
        self.__menge = menge

    @property
    def rezeptGuss(self):
        return self.__rezeptGuss
    @rezeptGuss.setter
    def rezeptGuss(self, rezeptGuss: str):
        self.__rezeptGuss = rezeptGuss

    @property
    def guss(self):
        return self.__guss
    @guss.setter
    def guss(self, guss: Zutat_):
        self.__guss = guss

    @property
    def form(self):
        return self.__form
    @form.setter
    def form(self, form: PlaetzchenForm_):
        self.__form = form

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: String_):
        self.__name = name

    @property
    def rezeptTeig(self):
        return self.__rezeptTeig
    @rezeptTeig.setter
    def rezeptTeig(self, rezeptTeig: TeigRezept_):
        self.__rezeptTeig = rezeptTeig

    @property
    def deko(self):
        return self.__deko
    @deko.setter
    def deko(self, deko: Zutat_):
        self.__deko = deko

    @property
    def plaetzchenForm3(self):
        return self.__plaetzchenForm3
    @plaetzchenForm3.setter
    def plaetzchenForm3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plaetzchen__plaetzchenForm3", None)
        self.__plaetzchenForm3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchen2"):
                opp_val = getattr(old_value, "plaetzchen2", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchen2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchen2"):
                opp_val = getattr(value, "plaetzchen2", None)
                setattr(value, "plaetzchen2", self)



class TeigRezept_:

    pass


class TeigRezept:

    def __init__(self, backtemp: int, backzeit: int, zutaten: List_Zutat___, basismenge: int, basis: PlaetzchenForm_, zutat5: "Zutat" = None, gUI12: "GUI" = None, gUIRezept19: "GUIRezept" = None):
        self.backtemp = backtemp
        self.backzeit = backzeit
        self.zutaten = zutaten
        self.basismenge = basismenge
        self.basis = basis
        self.zutat5 = zutat5
        self.gUI12 = gUI12
        self.gUIRezept19 = gUIRezept19
        
        pass
    @property
    def backzeit(self):
        return self.__backzeit
    @backzeit.setter
    def backzeit(self, backzeit: int):
        self.__backzeit = backzeit

    @property
    def backtemp(self):
        return self.__backtemp
    @backtemp.setter
    def backtemp(self, backtemp: int):
        self.__backtemp = backtemp

    @property
    def zutaten(self):
        return self.__zutaten
    @zutaten.setter
    def zutaten(self, zutaten: List_Zutat___):
        self.__zutaten = zutaten

    @property
    def basismenge(self):
        return self.__basismenge
    @basismenge.setter
    def basismenge(self, basismenge: int):
        self.__basismenge = basismenge

    @property
    def basis(self):
        return self.__basis
    @basis.setter
    def basis(self, basis: PlaetzchenForm_):
        self.__basis = basis

    @property
    def zutat5(self):
        return self.__zutat5
    @zutat5.setter
    def zutat5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TeigRezept__zutat5", None)
        self.__zutat5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teigRezept4"):
                opp_val = getattr(old_value, "teigRezept4", None)
                if opp_val == self:
                    setattr(old_value, "teigRezept4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teigRezept4"):
                opp_val = getattr(value, "teigRezept4", None)
                setattr(value, "teigRezept4", self)

    @property
    def gUI12(self):
        return self.__gUI12
    @gUI12.setter
    def gUI12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TeigRezept__gUI12", None)
        self.__gUI12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teigRezept13"):
                opp_val = getattr(old_value, "teigRezept13", None)
                if opp_val == self:
                    setattr(old_value, "teigRezept13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teigRezept13"):
                opp_val = getattr(value, "teigRezept13", None)
                setattr(value, "teigRezept13", self)

    @property
    def gUIRezept19(self):
        return self.__gUIRezept19
    @gUIRezept19.setter
    def gUIRezept19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TeigRezept__gUIRezept19", None)
        self.__gUIRezept19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teigRezept18"):
                opp_val = getattr(old_value, "teigRezept18", None)
                if opp_val == self:
                    setattr(old_value, "teigRezept18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teigRezept18"):
                opp_val = getattr(value, "teigRezept18", None)
                setattr(value, "teigRezept18", self)



class KonfigDatei_:

    pass


class KonfigDatei:

    def __init__(self, name: String_, menge: int, backzeit: int, backtemp: int, menge1: int, plaetzchen: Plaetzchen_, attribute: str, attribute2: str, gUI15: "GUI" = None):
        self.name = name
        self.menge = menge
        self.backzeit = backzeit
        self.backtemp = backtemp
        self.menge1 = menge1
        self.plaetzchen = plaetzchen
        self.attribute = attribute
        self.attribute2 = attribute2
        self.gUI15 = gUI15
        
        pass
    @property
    def backtemp(self):
        return self.__backtemp
    @backtemp.setter
    def backtemp(self, backtemp: int):
        self.__backtemp = backtemp

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def menge1(self):
        return self.__menge1
    @menge1.setter
    def menge1(self, menge1: int):
        self.__menge1 = menge1

    @property
    def backzeit(self):
        return self.__backzeit
    @backzeit.setter
    def backzeit(self, backzeit: int):
        self.__backzeit = backzeit

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: String_):
        self.__name = name

    @property
    def plaetzchen(self):
        return self.__plaetzchen
    @plaetzchen.setter
    def plaetzchen(self, plaetzchen: Plaetzchen_):
        self.__plaetzchen = plaetzchen

    @property
    def menge(self):
        return self.__menge
    @menge.setter
    def menge(self, menge: int):
        self.__menge = menge

    @property
    def gUI15(self):
        return self.__gUI15
    @gUI15.setter
    def gUI15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_KonfigDatei__gUI15", None)
        self.__gUI15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "konfigDatei14"):
                opp_val = getattr(old_value, "konfigDatei14", None)
                if opp_val == self:
                    setattr(old_value, "konfigDatei14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "konfigDatei14"):
                opp_val = getattr(value, "konfigDatei14", None)
                setattr(value, "konfigDatei14", self)



class GUIKeksform:

    def __init__(self, name: str, pl__f: PL_Form_, breite: int, laenge: int, gUI11: "GUI" = None, plaetzchenForm21: "PlaetzchenForm" = None):
        self.name = name
        self.pl__f = pl__f
        self.breite = breite
        self.laenge = laenge
        self.gUI11 = gUI11
        self.plaetzchenForm21 = plaetzchenForm21
        
        pass
    @property
    def laenge(self):
        return self.__laenge
    @laenge.setter
    def laenge(self, laenge: int):
        self.__laenge = laenge

    @property
    def breite(self):
        return self.__breite
    @breite.setter
    def breite(self, breite: int):
        self.__breite = breite

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pl__f(self):
        return self.__pl__f
    @pl__f.setter
    def pl__f(self, pl__f: PL_Form_):
        self.__pl__f = pl__f

    @property
    def plaetzchenForm21(self):
        return self.__plaetzchenForm21
    @plaetzchenForm21.setter
    def plaetzchenForm21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUIKeksform__plaetzchenForm21", None)
        self.__plaetzchenForm21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUIKeksform20"):
                opp_val = getattr(old_value, "gUIKeksform20", None)
                if opp_val == self:
                    setattr(old_value, "gUIKeksform20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUIKeksform20"):
                opp_val = getattr(value, "gUIKeksform20", None)
                setattr(value, "gUIKeksform20", self)

    @property
    def gUI11(self):
        return self.__gUI11
    @gUI11.setter
    def gUI11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUIKeksform__gUI11", None)
        self.__gUI11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUIPlaetzchen10"):
                opp_val = getattr(old_value, "gUIPlaetzchen10", None)
                if opp_val == self:
                    setattr(old_value, "gUIPlaetzchen10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUIPlaetzchen10"):
                opp_val = getattr(value, "gUIPlaetzchen10", None)
                setattr(value, "gUIPlaetzchen10", self)



class GUI:

    def __init__(self, dateiname: str, plaetzchenname: str, teigsorte: ComboBox, form: ComboBox, groesse: ComboBox, guss: ComboBox, deko: ComboBox, stueckzahl: str, datei: KonfigDatei_, plaetzchen: Plaetzchen_, teigList: List_TeigRezept___, plformList: List_PlaetzchenForm___, gussList: List_DekorRezept___, dekorList: List_DekorRezept___, attribute: str, zutatenList: List_Zutat___, plaetzchenForm7: "PlaetzchenForm" = None, gUIPlaetzchen10: "GUIKeksform" = None, teigRezept13: "TeigRezept" = None, konfigDatei14: "KonfigDatei" = None, gUIRezept16: "GUIRezept" = None, dekorRezept25: "DekorRezept" = None, myException26: "myException" = None, zutat29: "Zutat" = None):
        self.dateiname = dateiname
        self.plaetzchenname = plaetzchenname
        self.teigsorte = teigsorte
        self.form = form
        self.groesse = groesse
        self.guss = guss
        self.deko = deko
        self.stueckzahl = stueckzahl
        self.datei = datei
        self.plaetzchen = plaetzchen
        self.teigList = teigList
        self.plformList = plformList
        self.gussList = gussList
        self.dekorList = dekorList
        self.attribute = attribute
        self.zutatenList = zutatenList
        self.plaetzchenForm7 = plaetzchenForm7
        self.gUIPlaetzchen10 = gUIPlaetzchen10
        self.teigRezept13 = teigRezept13
        self.konfigDatei14 = konfigDatei14
        self.gUIRezept16 = gUIRezept16
        self.dekorRezept25 = dekorRezept25
        self.myException26 = myException26
        self.zutat29 = zutat29
        
        pass
    @property
    def form(self):
        return self.__form
    @form.setter
    def form(self, form: ComboBox):
        self.__form = form

    @property
    def gussList(self):
        return self.__gussList
    @gussList.setter
    def gussList(self, gussList: List_DekorRezept___):
        self.__gussList = gussList

    @property
    def teigsorte(self):
        return self.__teigsorte
    @teigsorte.setter
    def teigsorte(self, teigsorte: ComboBox):
        self.__teigsorte = teigsorte

    @property
    def plformList(self):
        return self.__plformList
    @plformList.setter
    def plformList(self, plformList: List_PlaetzchenForm___):
        self.__plformList = plformList

    @property
    def groesse(self):
        return self.__groesse
    @groesse.setter
    def groesse(self, groesse: ComboBox):
        self.__groesse = groesse

    @property
    def zutatenList(self):
        return self.__zutatenList
    @zutatenList.setter
    def zutatenList(self, zutatenList: List_Zutat___):
        self.__zutatenList = zutatenList

    @property
    def dateiname(self):
        return self.__dateiname
    @dateiname.setter
    def dateiname(self, dateiname: str):
        self.__dateiname = dateiname

    @property
    def teigList(self):
        return self.__teigList
    @teigList.setter
    def teigList(self, teigList: List_TeigRezept___):
        self.__teigList = teigList

    @property
    def datei(self):
        return self.__datei
    @datei.setter
    def datei(self, datei: KonfigDatei_):
        self.__datei = datei

    @property
    def guss(self):
        return self.__guss
    @guss.setter
    def guss(self, guss: ComboBox):
        self.__guss = guss

    @property
    def plaetzchenname(self):
        return self.__plaetzchenname
    @plaetzchenname.setter
    def plaetzchenname(self, plaetzchenname: str):
        self.__plaetzchenname = plaetzchenname

    @property
    def stueckzahl(self):
        return self.__stueckzahl
    @stueckzahl.setter
    def stueckzahl(self, stueckzahl: str):
        self.__stueckzahl = stueckzahl

    @property
    def deko(self):
        return self.__deko
    @deko.setter
    def deko(self, deko: ComboBox):
        self.__deko = deko

    @property
    def plaetzchen(self):
        return self.__plaetzchen
    @plaetzchen.setter
    def plaetzchen(self, plaetzchen: Plaetzchen_):
        self.__plaetzchen = plaetzchen

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def dekorList(self):
        return self.__dekorList
    @dekorList.setter
    def dekorList(self, dekorList: List_DekorRezept___):
        self.__dekorList = dekorList

    @property
    def konfigDatei14(self):
        return self.__konfigDatei14
    @konfigDatei14.setter
    def konfigDatei14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUI__konfigDatei14", None)
        self.__konfigDatei14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUI15"):
                opp_val = getattr(old_value, "gUI15", None)
                if opp_val == self:
                    setattr(old_value, "gUI15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUI15"):
                opp_val = getattr(value, "gUI15", None)
                setattr(value, "gUI15", self)

    @property
    def zutat29(self):
        return self.__zutat29
    @zutat29.setter
    def zutat29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUI__zutat29", None)
        self.__zutat29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUI28"):
                opp_val = getattr(old_value, "gUI28", None)
                if opp_val == self:
                    setattr(old_value, "gUI28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUI28"):
                opp_val = getattr(value, "gUI28", None)
                setattr(value, "gUI28", self)

    @property
    def dekorRezept25(self):
        return self.__dekorRezept25
    @dekorRezept25.setter
    def dekorRezept25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUI__dekorRezept25", None)
        self.__dekorRezept25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUI24"):
                opp_val = getattr(old_value, "gUI24", None)
                if opp_val == self:
                    setattr(old_value, "gUI24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUI24"):
                opp_val = getattr(value, "gUI24", None)
                setattr(value, "gUI24", self)

    @property
    def gUIRezept16(self):
        return self.__gUIRezept16
    @gUIRezept16.setter
    def gUIRezept16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUI__gUIRezept16", None)
        self.__gUIRezept16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUI17"):
                opp_val = getattr(old_value, "gUI17", None)
                if opp_val == self:
                    setattr(old_value, "gUI17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUI17"):
                opp_val = getattr(value, "gUI17", None)
                setattr(value, "gUI17", self)

    @property
    def myException26(self):
        return self.__myException26
    @myException26.setter
    def myException26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUI__myException26", None)
        self.__myException26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUI27"):
                opp_val = getattr(old_value, "gUI27", None)
                if opp_val == self:
                    setattr(old_value, "gUI27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUI27"):
                opp_val = getattr(value, "gUI27", None)
                setattr(value, "gUI27", self)

    @property
    def gUIPlaetzchen10(self):
        return self.__gUIPlaetzchen10
    @gUIPlaetzchen10.setter
    def gUIPlaetzchen10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUI__gUIPlaetzchen10", None)
        self.__gUIPlaetzchen10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUI11"):
                opp_val = getattr(old_value, "gUI11", None)
                if opp_val == self:
                    setattr(old_value, "gUI11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUI11"):
                opp_val = getattr(value, "gUI11", None)
                setattr(value, "gUI11", self)

    @property
    def plaetzchenForm7(self):
        return self.__plaetzchenForm7
    @plaetzchenForm7.setter
    def plaetzchenForm7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUI__plaetzchenForm7", None)
        self.__plaetzchenForm7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUI6"):
                opp_val = getattr(old_value, "gUI6", None)
                if opp_val == self:
                    setattr(old_value, "gUI6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUI6"):
                opp_val = getattr(value, "gUI6", None)
                setattr(value, "gUI6", self)

    @property
    def teigRezept13(self):
        return self.__teigRezept13
    @teigRezept13.setter
    def teigRezept13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GUI__teigRezept13", None)
        self.__teigRezept13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gUI12"):
                opp_val = getattr(old_value, "gUI12", None)
                if opp_val == self:
                    setattr(old_value, "gUI12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gUI12"):
                opp_val = getattr(value, "gUI12", None)
                setattr(value, "gUI12", self)



class Groesse:

    def __init__(self, name: str, name1: PL_Groesse_, breite: int, laenge: int, plaetzchenForm0: "PlaetzchenForm" = None):
        self.name = name
        self.name1 = name1
        self.breite = breite
        self.laenge = laenge
        self.plaetzchenForm0 = plaetzchenForm0
        
        pass
    @property
    def name1(self):
        return self.__name1
    @name1.setter
    def name1(self, name1: PL_Groesse_):
        self.__name1 = name1

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def breite(self):
        return self.__breite
    @breite.setter
    def breite(self, breite: int):
        self.__breite = breite

    @property
    def laenge(self):
        return self.__laenge
    @laenge.setter
    def laenge(self, laenge: int):
        self.__laenge = laenge

    @property
    def plaetzchenForm0(self):
        return self.__plaetzchenForm0
    @plaetzchenForm0.setter
    def plaetzchenForm0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Groesse__plaetzchenForm0", None)
        self.__plaetzchenForm0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groesse21"):
                opp_val = getattr(old_value, "groesse21", None)
                if opp_val == self:
                    setattr(old_value, "groesse21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groesse21"):
                opp_val = getattr(value, "groesse21", None)
                setattr(value, "groesse21", self)



class PlaetzchenForm:

    def __init__(self, pl_groesse: Groesse_, pl_form: PL_Form_, faktor: str, groesse21: "Groesse" = None, plaetzchen2: "Plaetzchen" = None, gUI6: "GUI" = None, teigRezept8: "Rezept" = None, gUIKeksform20: "GUIKeksform" = None):
        self.pl_groesse = pl_groesse
        self.pl_form = pl_form
        self.faktor = faktor
        self.groesse21 = groesse21
        self.plaetzchen2 = plaetzchen2
        self.gUI6 = gUI6
        self.teigRezept8 = teigRezept8
        self.gUIKeksform20 = gUIKeksform20
        
        pass
    @property
    def faktor(self):
        return self.__faktor
    @faktor.setter
    def faktor(self, faktor: str):
        self.__faktor = faktor

    @property
    def pl_groesse(self):
        return self.__pl_groesse
    @pl_groesse.setter
    def pl_groesse(self, pl_groesse: Groesse_):
        self.__pl_groesse = pl_groesse

    @property
    def pl_form(self):
        return self.__pl_form
    @pl_form.setter
    def pl_form(self, pl_form: PL_Form_):
        self.__pl_form = pl_form

    @property
    def groesse21(self):
        return self.__groesse21
    @groesse21.setter
    def groesse21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlaetzchenForm__groesse21", None)
        self.__groesse21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenForm0"):
                opp_val = getattr(old_value, "plaetzchenForm0", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenForm0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenForm0"):
                opp_val = getattr(value, "plaetzchenForm0", None)
                setattr(value, "plaetzchenForm0", self)

    @property
    def plaetzchen2(self):
        return self.__plaetzchen2
    @plaetzchen2.setter
    def plaetzchen2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlaetzchenForm__plaetzchen2", None)
        self.__plaetzchen2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenForm3"):
                opp_val = getattr(old_value, "plaetzchenForm3", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenForm3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenForm3"):
                opp_val = getattr(value, "plaetzchenForm3", None)
                setattr(value, "plaetzchenForm3", self)

    @property
    def gUIKeksform20(self):
        return self.__gUIKeksform20
    @gUIKeksform20.setter
    def gUIKeksform20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlaetzchenForm__gUIKeksform20", None)
        self.__gUIKeksform20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenForm21"):
                opp_val = getattr(old_value, "plaetzchenForm21", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenForm21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenForm21"):
                opp_val = getattr(value, "plaetzchenForm21", None)
                setattr(value, "plaetzchenForm21", self)

    @property
    def gUI6(self):
        return self.__gUI6
    @gUI6.setter
    def gUI6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlaetzchenForm__gUI6", None)
        self.__gUI6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenForm7"):
                opp_val = getattr(old_value, "plaetzchenForm7", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenForm7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenForm7"):
                opp_val = getattr(value, "plaetzchenForm7", None)
                setattr(value, "plaetzchenForm7", self)

    @property
    def teigRezept8(self):
        return self.__teigRezept8
    @teigRezept8.setter
    def teigRezept8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlaetzchenForm__teigRezept8", None)
        self.__teigRezept8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenForm9"):
                opp_val = getattr(old_value, "plaetzchenForm9", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenForm9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenForm9"):
                opp_val = getattr(value, "plaetzchenForm9", None)
                setattr(value, "plaetzchenForm9", self)



class Zutat:

    def __init__(self, name: String_, menge: int, einheit: String_, teigRezept4: "TeigRezept" = None, dekorRezept23: "DekorRezept" = None, gUI28: "GUI" = None):
        self.name = name
        self.menge = menge
        self.einheit = einheit
        self.teigRezept4 = teigRezept4
        self.dekorRezept23 = dekorRezept23
        self.gUI28 = gUI28
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: String_):
        self.__name = name

    @property
    def einheit(self):
        return self.__einheit
    @einheit.setter
    def einheit(self, einheit: String_):
        self.__einheit = einheit

    @property
    def menge(self):
        return self.__menge
    @menge.setter
    def menge(self, menge: int):
        self.__menge = menge

    @property
    def gUI28(self):
        return self.__gUI28
    @gUI28.setter
    def gUI28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Zutat__gUI28", None)
        self.__gUI28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat29"):
                opp_val = getattr(old_value, "zutat29", None)
                if opp_val == self:
                    setattr(old_value, "zutat29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat29"):
                opp_val = getattr(value, "zutat29", None)
                setattr(value, "zutat29", self)

    @property
    def teigRezept4(self):
        return self.__teigRezept4
    @teigRezept4.setter
    def teigRezept4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Zutat__teigRezept4", None)
        self.__teigRezept4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat5"):
                opp_val = getattr(old_value, "zutat5", None)
                if opp_val == self:
                    setattr(old_value, "zutat5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat5"):
                opp_val = getattr(value, "zutat5", None)
                setattr(value, "zutat5", self)

    @property
    def dekorRezept23(self):
        return self.__dekorRezept23
    @dekorRezept23.setter
    def dekorRezept23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Zutat__dekorRezept23", None)
        self.__dekorRezept23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat22"):
                opp_val = getattr(old_value, "zutat22", None)
                if opp_val == self:
                    setattr(old_value, "zutat22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat22"):
                opp_val = getattr(value, "zutat22", None)
                setattr(value, "zutat22", self)

