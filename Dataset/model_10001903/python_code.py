from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class enum_form(Enum):
    pass
class form(Enum):
    pass

############################################
# Definition of Classes
############################################










class const_zutat:

    pass


class ostream_1:

    pass


class ostream_:

    pass


class teigmaschine_:

    pass


class lager_:

    pass


class array_int_3_:

    pass


class groesse_:

    pass


class array_int__:

    pass


class myException:

    pass


class string_:

    pass


class plaetzchenForm_:

    pass


class teig_2:

    pass


class teig_:

    pass


class list_zutat__:

    pass


class zutat_:

    pass


class Blech:

    pass


class belagmaschine:

    pass


class teigmaschine:

    def __init__(self, blechgroesse: groesse_, abstand: str, anzBleche: str, anzBlechePlaetzchen: array_int_3_, anzPlaetzchenLetzesBlech: str, groesse7: "groesse" = None, auftrag23: "auftrag" = None):
        self.blechgroesse = blechgroesse
        self.abstand = abstand
        self.anzBleche = anzBleche
        self.anzBlechePlaetzchen = anzBlechePlaetzchen
        self.anzPlaetzchenLetzesBlech = anzPlaetzchenLetzesBlech
        self.groesse7 = groesse7
        self.auftrag23 = auftrag23
        
        pass
    @property
    def anzBleche(self):
        return self.__anzBleche
    @anzBleche.setter
    def anzBleche(self, anzBleche: str):
        self.__anzBleche = anzBleche

    @property
    def anzPlaetzchenLetzesBlech(self):
        return self.__anzPlaetzchenLetzesBlech
    @anzPlaetzchenLetzesBlech.setter
    def anzPlaetzchenLetzesBlech(self, anzPlaetzchenLetzesBlech: str):
        self.__anzPlaetzchenLetzesBlech = anzPlaetzchenLetzesBlech

    @property
    def blechgroesse(self):
        return self.__blechgroesse
    @blechgroesse.setter
    def blechgroesse(self, blechgroesse: groesse_):
        self.__blechgroesse = blechgroesse

    @property
    def anzBlechePlaetzchen(self):
        return self.__anzBlechePlaetzchen
    @anzBlechePlaetzchen.setter
    def anzBlechePlaetzchen(self, anzBlechePlaetzchen: array_int_3_):
        self.__anzBlechePlaetzchen = anzBlechePlaetzchen

    @property
    def abstand(self):
        return self.__abstand
    @abstand.setter
    def abstand(self, abstand: str):
        self.__abstand = abstand

    @property
    def groesse7(self):
        return self.__groesse7
    @groesse7.setter
    def groesse7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_teigmaschine__groesse7", None)
        self.__groesse7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "belch6"):
                opp_val = getattr(old_value, "belch6", None)
                if opp_val == self:
                    setattr(old_value, "belch6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "belch6"):
                opp_val = getattr(value, "belch6", None)
                setattr(value, "belch6", self)

    @property
    def auftrag23(self):
        return self.__auftrag23
    @auftrag23.setter
    def auftrag23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_teigmaschine__auftrag23", None)
        self.__auftrag23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teigmaschine22"):
                opp_val = getattr(old_value, "teigmaschine22", None)
                if opp_val == self:
                    setattr(old_value, "teigmaschine22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teigmaschine22"):
                opp_val = getattr(value, "teigmaschine22", None)
                setattr(value, "teigmaschine22", self)



class prozessBand:

    def __init__(self, geschwindigkeit_ist: str, backstrasse4: "backofen" = None):
        self.geschwindigkeit_ist = geschwindigkeit_ist
        self.backstrasse4 = backstrasse4
        
        pass
    @property
    def geschwindigkeit_ist(self):
        return self.__geschwindigkeit_ist
    @geschwindigkeit_ist.setter
    def geschwindigkeit_ist(self, geschwindigkeit_ist: str):
        self.__geschwindigkeit_ist = geschwindigkeit_ist

    @property
    def backstrasse4(self):
        return self.__backstrasse4
    @backstrasse4.setter
    def backstrasse4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prozessBand__backstrasse4", None)
        self.__backstrasse4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prozessBand5"):
                opp_val = getattr(old_value, "prozessBand5", None)
                if opp_val == self:
                    setattr(old_value, "prozessBand5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prozessBand5"):
                opp_val = getattr(value, "prozessBand5", None)
                setattr(value, "prozessBand5", self)



class prozessHeizen:

    def __init__(self, temperatur_ist: str, attribute: str, backstrasse2: "backofen" = None):
        self.temperatur_ist = temperatur_ist
        self.attribute = attribute
        self.backstrasse2 = backstrasse2
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def temperatur_ist(self):
        return self.__temperatur_ist
    @temperatur_ist.setter
    def temperatur_ist(self, temperatur_ist: str):
        self.__temperatur_ist = temperatur_ist

    @property
    def backstrasse2(self):
        return self.__backstrasse2
    @backstrasse2.setter
    def backstrasse2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prozessHeizen__backstrasse2", None)
        self.__backstrasse2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prozessHeizen3"):
                opp_val = getattr(old_value, "prozessHeizen3", None)
                if opp_val == self:
                    setattr(old_value, "prozessHeizen3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prozessHeizen3"):
                opp_val = getattr(value, "prozessHeizen3", None)
                setattr(value, "prozessHeizen3", self)



class backofen:

    def __init__(self, ofenlaenge: str, backzeit: str, backtemp: str, teigmaschine: teigmaschine, bandgeschwindigkeit: str, myException34: "myException" = None, prozessHeizen3: "prozessHeizen" = None, prozessBand5: "prozessBand" = None, auftrag25: "auftrag" = None):
        self.ofenlaenge = ofenlaenge
        self.backzeit = backzeit
        self.backtemp = backtemp
        self.teigmaschine = teigmaschine
        self.bandgeschwindigkeit = bandgeschwindigkeit
        self.myException34 = myException34
        self.prozessHeizen3 = prozessHeizen3
        self.prozessBand5 = prozessBand5
        self.auftrag25 = auftrag25
        
        pass
    @property
    def backzeit(self):
        return self.__backzeit
    @backzeit.setter
    def backzeit(self, backzeit: str):
        self.__backzeit = backzeit

    @property
    def backtemp(self):
        return self.__backtemp
    @backtemp.setter
    def backtemp(self, backtemp: str):
        self.__backtemp = backtemp

    @property
    def teigmaschine(self):
        return self.__teigmaschine
    @teigmaschine.setter
    def teigmaschine(self, teigmaschine: teigmaschine):
        self.__teigmaschine = teigmaschine

    @property
    def ofenlaenge(self):
        return self.__ofenlaenge
    @ofenlaenge.setter
    def ofenlaenge(self, ofenlaenge: str):
        self.__ofenlaenge = ofenlaenge

    @property
    def bandgeschwindigkeit(self):
        return self.__bandgeschwindigkeit
    @bandgeschwindigkeit.setter
    def bandgeschwindigkeit(self, bandgeschwindigkeit: str):
        self.__bandgeschwindigkeit = bandgeschwindigkeit

    @property
    def auftrag25(self):
        return self.__auftrag25
    @auftrag25.setter
    def auftrag25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backofen__auftrag25", None)
        self.__auftrag25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backofen224"):
                opp_val = getattr(old_value, "backofen224", None)
                if opp_val == self:
                    setattr(old_value, "backofen224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backofen224"):
                opp_val = getattr(value, "backofen224", None)
                setattr(value, "backofen224", self)

    @property
    def prozessHeizen3(self):
        return self.__prozessHeizen3
    @prozessHeizen3.setter
    def prozessHeizen3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backofen__prozessHeizen3", None)
        self.__prozessHeizen3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backstrasse2"):
                opp_val = getattr(old_value, "backstrasse2", None)
                if opp_val == self:
                    setattr(old_value, "backstrasse2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backstrasse2"):
                opp_val = getattr(value, "backstrasse2", None)
                setattr(value, "backstrasse2", self)

    @property
    def myException34(self):
        return self.__myException34
    @myException34.setter
    def myException34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backofen__myException34", None)
        self.__myException34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backofen35"):
                opp_val = getattr(old_value, "backofen35", None)
                if opp_val == self:
                    setattr(old_value, "backofen35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backofen35"):
                opp_val = getattr(value, "backofen35", None)
                setattr(value, "backofen35", self)

    @property
    def prozessBand5(self):
        return self.__prozessBand5
    @prozessBand5.setter
    def prozessBand5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backofen__prozessBand5", None)
        self.__prozessBand5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backstrasse4"):
                opp_val = getattr(old_value, "backstrasse4", None)
                if opp_val == self:
                    setattr(old_value, "backstrasse4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backstrasse4"):
                opp_val = getattr(value, "backstrasse4", None)
                setattr(value, "backstrasse4", self)



class groesse:

    def __init__(self, name: str, breite: str, laenge: str, name1: str, plaetzchenForm1: "plaetzchenForm" = None, belch6: "teigmaschine" = None):
        self.name = name
        self.breite = breite
        self.laenge = laenge
        self.name1 = name1
        self.plaetzchenForm1 = plaetzchenForm1
        self.belch6 = belch6
        
        pass
    @property
    def laenge(self):
        return self.__laenge
    @laenge.setter
    def laenge(self, laenge: str):
        self.__laenge = laenge

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def name1(self):
        return self.__name1
    @name1.setter
    def name1(self, name1: str):
        self.__name1 = name1

    @property
    def breite(self):
        return self.__breite
    @breite.setter
    def breite(self, breite: str):
        self.__breite = breite

    @property
    def plaetzchenForm1(self):
        return self.__plaetzchenForm1
    @plaetzchenForm1.setter
    def plaetzchenForm1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_groesse__plaetzchenForm1", None)
        self.__plaetzchenForm1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groesse20"):
                opp_val = getattr(old_value, "groesse20", None)
                if opp_val == self:
                    setattr(old_value, "groesse20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groesse20"):
                opp_val = getattr(value, "groesse20", None)
                setattr(value, "groesse20", self)

    @property
    def belch6(self):
        return self.__belch6
    @belch6.setter
    def belch6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_groesse__belch6", None)
        self.__belch6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groesse7"):
                opp_val = getattr(old_value, "groesse7", None)
                if opp_val == self:
                    setattr(old_value, "groesse7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groesse7"):
                opp_val = getattr(value, "groesse7", None)
                setattr(value, "groesse7", self)



class plaetzchenForm:

    def __init__(self, form: enum_form, groesse: groesse, groesse20: "groesse" = None, auftrag30: "auftrag" = None):
        self.form = form
        self.groesse = groesse
        self.groesse20 = groesse20
        self.auftrag30 = auftrag30
        
        pass
    @property
    def form(self):
        return self.__form
    @form.setter
    def form(self, form: enum_form):
        self.__form = form

    @property
    def groesse(self):
        return self.__groesse
    @groesse.setter
    def groesse(self, groesse: groesse):
        self.__groesse = groesse

    @property
    def groesse20(self):
        return self.__groesse20
    @groesse20.setter
    def groesse20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plaetzchenForm__groesse20", None)
        self.__groesse20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenForm1"):
                opp_val = getattr(old_value, "plaetzchenForm1", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenForm1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenForm1"):
                opp_val = getattr(value, "plaetzchenForm1", None)
                setattr(value, "plaetzchenForm1", self)

    @property
    def auftrag30(self):
        return self.__auftrag30
    @auftrag30.setter
    def auftrag30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plaetzchenForm__auftrag30", None)
        self.__auftrag30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchenForm31"):
                opp_val = getattr(old_value, "plaetzchenForm31", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchenForm31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchenForm31"):
                opp_val = getattr(value, "plaetzchenForm31", None)
                setattr(value, "plaetzchenForm31", self)



class zutat:

    def __init__(self, name: str, menge: str, einheit: str, plaetzchen39: "plaetzchen" = None, lager11: "lager" = None, auftrag20: "auftrag" = None, teig33: "teig" = None):
        self.name = name
        self.menge = menge
        self.einheit = einheit
        self.plaetzchen39 = plaetzchen39
        self.lager11 = lager11
        self.auftrag20 = auftrag20
        self.teig33 = teig33
        
        pass
    @property
    def menge(self):
        return self.__menge
    @menge.setter
    def menge(self, menge: str):
        self.__menge = menge

    @property
    def einheit(self):
        return self.__einheit
    @einheit.setter
    def einheit(self, einheit: str):
        self.__einheit = einheit

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lager11(self):
        return self.__lager11
    @lager11.setter
    def lager11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zutat__lager11", None)
        self.__lager11 = value
        
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
    def plaetzchen39(self):
        return self.__plaetzchen39
    @plaetzchen39.setter
    def plaetzchen39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zutat__plaetzchen39", None)
        self.__plaetzchen39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat38"):
                opp_val = getattr(old_value, "zutat38", None)
                if opp_val == self:
                    setattr(old_value, "zutat38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat38"):
                opp_val = getattr(value, "zutat38", None)
                setattr(value, "zutat38", self)

    @property
    def teig33(self):
        return self.__teig33
    @teig33.setter
    def teig33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zutat__teig33", None)
        self.__teig33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat32"):
                opp_val = getattr(old_value, "zutat32", None)
                if opp_val == self:
                    setattr(old_value, "zutat32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat32"):
                opp_val = getattr(value, "zutat32", None)
                setattr(value, "zutat32", self)

    @property
    def auftrag20(self):
        return self.__auftrag20
    @auftrag20.setter
    def auftrag20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_zutat__auftrag20", None)
        self.__auftrag20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zutat21"):
                opp_val = getattr(old_value, "zutat21", None)
                if opp_val == self:
                    setattr(old_value, "zutat21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zutat21"):
                opp_val = getattr(value, "zutat21", None)
                setattr(value, "zutat21", self)



class auftrag:

    def __init__(self, pform: plaetzchenForm_, pteig: teig_, pguss: zutat_, pdeko: zutat_, pteigmaschine: teigmaschine_, menge: str, name: str, backtemp: str, backzeit: str, attribute: str, backofen: backofen, belagmaschine: belagmaschine, lager8: "lager" = None, myException16: "myException" = None, teig19: "teig" = None, zutat21: "zutat" = None, teigmaschine22: "teigmaschine" = None, backofen224: "backofen" = None, belagmaschine226: "belagmaschine" = None, plaetzchen29: "plaetzchen" = None, plaetzchenForm31: "plaetzchenForm" = None):
        self.pform = pform
        self.pteig = pteig
        self.pguss = pguss
        self.pdeko = pdeko
        self.pteigmaschine = pteigmaschine
        self.menge = menge
        self.name = name
        self.backtemp = backtemp
        self.backzeit = backzeit
        self.attribute = attribute
        self.backofen = backofen
        self.belagmaschine = belagmaschine
        self.lager8 = lager8
        self.myException16 = myException16
        self.teig19 = teig19
        self.zutat21 = zutat21
        self.teigmaschine22 = teigmaschine22
        self.backofen224 = backofen224
        self.belagmaschine226 = belagmaschine226
        self.plaetzchen29 = plaetzchen29
        self.plaetzchenForm31 = plaetzchenForm31
        
        pass
    @property
    def pguss(self):
        return self.__pguss
    @pguss.setter
    def pguss(self, pguss: zutat_):
        self.__pguss = pguss

    @property
    def menge(self):
        return self.__menge
    @menge.setter
    def menge(self, menge: str):
        self.__menge = menge

    @property
    def backtemp(self):
        return self.__backtemp
    @backtemp.setter
    def backtemp(self, backtemp: str):
        self.__backtemp = backtemp

    @property
    def pdeko(self):
        return self.__pdeko
    @pdeko.setter
    def pdeko(self, pdeko: zutat_):
        self.__pdeko = pdeko

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pteig(self):
        return self.__pteig
    @pteig.setter
    def pteig(self, pteig: teig_):
        self.__pteig = pteig

    @property
    def backofen(self):
        return self.__backofen
    @backofen.setter
    def backofen(self, backofen: backofen):
        self.__backofen = backofen

    @property
    def pform(self):
        return self.__pform
    @pform.setter
    def pform(self, pform: plaetzchenForm_):
        self.__pform = pform

    @property
    def backzeit(self):
        return self.__backzeit
    @backzeit.setter
    def backzeit(self, backzeit: str):
        self.__backzeit = backzeit

    @property
    def belagmaschine(self):
        return self.__belagmaschine
    @belagmaschine.setter
    def belagmaschine(self, belagmaschine: belagmaschine):
        self.__belagmaschine = belagmaschine

    @property
    def pteigmaschine(self):
        return self.__pteigmaschine
    @pteigmaschine.setter
    def pteigmaschine(self, pteigmaschine: teigmaschine_):
        self.__pteigmaschine = pteigmaschine

    @property
    def plaetzchenForm31(self):
        return self.__plaetzchenForm31
    @plaetzchenForm31.setter
    def plaetzchenForm31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_auftrag__plaetzchenForm31", None)
        self.__plaetzchenForm31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag30"):
                opp_val = getattr(old_value, "auftrag30", None)
                if opp_val == self:
                    setattr(old_value, "auftrag30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag30"):
                opp_val = getattr(value, "auftrag30", None)
                setattr(value, "auftrag30", self)

    @property
    def teigmaschine22(self):
        return self.__teigmaschine22
    @teigmaschine22.setter
    def teigmaschine22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_auftrag__teigmaschine22", None)
        self.__teigmaschine22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag23"):
                opp_val = getattr(old_value, "auftrag23", None)
                if opp_val == self:
                    setattr(old_value, "auftrag23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag23"):
                opp_val = getattr(value, "auftrag23", None)
                setattr(value, "auftrag23", self)

    @property
    def lager8(self):
        return self.__lager8
    @lager8.setter
    def lager8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_auftrag__lager8", None)
        self.__lager8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag9"):
                opp_val = getattr(old_value, "auftrag9", None)
                if opp_val == self:
                    setattr(old_value, "auftrag9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag9"):
                opp_val = getattr(value, "auftrag9", None)
                setattr(value, "auftrag9", self)

    @property
    def zutat21(self):
        return self.__zutat21
    @zutat21.setter
    def zutat21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_auftrag__zutat21", None)
        self.__zutat21 = value
        
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
    def teig19(self):
        return self.__teig19
    @teig19.setter
    def teig19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_auftrag__teig19", None)
        self.__teig19 = value
        
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
    def belagmaschine226(self):
        return self.__belagmaschine226
    @belagmaschine226.setter
    def belagmaschine226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_auftrag__belagmaschine226", None)
        self.__belagmaschine226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag27"):
                opp_val = getattr(old_value, "auftrag27", None)
                if opp_val == self:
                    setattr(old_value, "auftrag27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag27"):
                opp_val = getattr(value, "auftrag27", None)
                setattr(value, "auftrag27", self)

    @property
    def plaetzchen29(self):
        return self.__plaetzchen29
    @plaetzchen29.setter
    def plaetzchen29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_auftrag__plaetzchen29", None)
        self.__plaetzchen29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag28"):
                opp_val = getattr(old_value, "auftrag28", None)
                if opp_val == self:
                    setattr(old_value, "auftrag28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag28"):
                opp_val = getattr(value, "auftrag28", None)
                setattr(value, "auftrag28", self)

    @property
    def myException16(self):
        return self.__myException16
    @myException16.setter
    def myException16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_auftrag__myException16", None)
        self.__myException16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag17"):
                opp_val = getattr(old_value, "auftrag17", None)
                if opp_val == self:
                    setattr(old_value, "auftrag17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag17"):
                opp_val = getattr(value, "auftrag17", None)
                setattr(value, "auftrag17", self)

    @property
    def backofen224(self):
        return self.__backofen224
    @backofen224.setter
    def backofen224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_auftrag__backofen224", None)
        self.__backofen224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auftrag25"):
                opp_val = getattr(old_value, "auftrag25", None)
                if opp_val == self:
                    setattr(old_value, "auftrag25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auftrag25"):
                opp_val = getattr(value, "auftrag25", None)
                setattr(value, "auftrag25", self)



class plaetzchen:

    def __init__(self, name: str, pteig: teig_, pguss: zutat_, pdeko: zutat_, teig36: "teig" = None, zutat38: "zutat" = None, auftrag28: "auftrag" = None):
        self.name = name
        self.pteig = pteig
        self.pguss = pguss
        self.pdeko = pdeko
        self.teig36 = teig36
        self.zutat38 = zutat38
        self.auftrag28 = auftrag28
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pguss(self):
        return self.__pguss
    @pguss.setter
    def pguss(self, pguss: zutat_):
        self.__pguss = pguss

    @property
    def pdeko(self):
        return self.__pdeko
    @pdeko.setter
    def pdeko(self, pdeko: zutat_):
        self.__pdeko = pdeko

    @property
    def pteig(self):
        return self.__pteig
    @pteig.setter
    def pteig(self, pteig: teig_):
        self.__pteig = pteig

    @property
    def zutat38(self):
        return self.__zutat38
    @zutat38.setter
    def zutat38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plaetzchen__zutat38", None)
        self.__zutat38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchen39"):
                opp_val = getattr(old_value, "plaetzchen39", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchen39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchen39"):
                opp_val = getattr(value, "plaetzchen39", None)
                setattr(value, "plaetzchen39", self)

    @property
    def auftrag28(self):
        return self.__auftrag28
    @auftrag28.setter
    def auftrag28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plaetzchen__auftrag28", None)
        self.__auftrag28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchen29"):
                opp_val = getattr(old_value, "plaetzchen29", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchen29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchen29"):
                opp_val = getattr(value, "plaetzchen29", None)
                setattr(value, "plaetzchen29", self)

    @property
    def teig36(self):
        return self.__teig36
    @teig36.setter
    def teig36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_plaetzchen__teig36", None)
        self.__teig36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plaetzchen37"):
                opp_val = getattr(old_value, "plaetzchen37", None)
                if opp_val == self:
                    setattr(old_value, "plaetzchen37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plaetzchen37"):
                opp_val = getattr(value, "plaetzchen37", None)
                setattr(value, "plaetzchen37", self)



class teig:

    def __init__(self, attribute: str, name: str, zutaten: str, form: plaetzchenForm, menge: str, plaetzchen37: "plaetzchen" = None, lager13: "lager" = None, auftrag18: "auftrag" = None, zutat32: "zutat" = None):
        self.attribute = attribute
        self.name = name
        self.zutaten = zutaten
        self.form = form
        self.menge = menge
        self.plaetzchen37 = plaetzchen37
        self.lager13 = lager13
        self.auftrag18 = auftrag18
        self.zutat32 = zutat32
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def zutaten(self):
        return self.__zutaten
    @zutaten.setter
    def zutaten(self, zutaten: str):
        self.__zutaten = zutaten

    @property
    def menge(self):
        return self.__menge
    @menge.setter
    def menge(self, menge: str):
        self.__menge = menge

    @property
    def form(self):
        return self.__form
    @form.setter
    def form(self, form: plaetzchenForm):
        self.__form = form

    @property
    def lager13(self):
        return self.__lager13
    @lager13.setter
    def lager13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_teig__lager13", None)
        self.__lager13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teig12"):
                opp_val = getattr(old_value, "teig12", None)
                if opp_val == self:
                    setattr(old_value, "teig12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teig12"):
                opp_val = getattr(value, "teig12", None)
                setattr(value, "teig12", self)

    @property
    def auftrag18(self):
        return self.__auftrag18
    @auftrag18.setter
    def auftrag18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_teig__auftrag18", None)
        self.__auftrag18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teig19"):
                opp_val = getattr(old_value, "teig19", None)
                if opp_val == self:
                    setattr(old_value, "teig19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teig19"):
                opp_val = getattr(value, "teig19", None)
                setattr(value, "teig19", self)

    @property
    def plaetzchen37(self):
        return self.__plaetzchen37
    @plaetzchen37.setter
    def plaetzchen37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_teig__plaetzchen37", None)
        self.__plaetzchen37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teig36"):
                opp_val = getattr(old_value, "teig36", None)
                if opp_val == self:
                    setattr(old_value, "teig36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teig36"):
                opp_val = getattr(value, "teig36", None)
                setattr(value, "teig36", self)

    @property
    def zutat32(self):
        return self.__zutat32
    @zutat32.setter
    def zutat32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_teig__zutat32", None)
        self.__zutat32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teig33"):
                opp_val = getattr(old_value, "teig33", None)
                if opp_val == self:
                    setattr(old_value, "teig33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teig33"):
                opp_val = getattr(value, "teig33", None)
                setattr(value, "teig33", self)



class lager:

    def __init__(self, bestandZutaten: str, attribute: str, auftrag9: "auftrag" = None, zutat10: "zutat" = None, teig12: "teig" = None, myException14: "myException" = None):
        self.bestandZutaten = bestandZutaten
        self.attribute = attribute
        self.auftrag9 = auftrag9
        self.zutat10 = zutat10
        self.teig12 = teig12
        self.myException14 = myException14
        
        pass
    @property
    def bestandZutaten(self):
        return self.__bestandZutaten
    @bestandZutaten.setter
    def bestandZutaten(self, bestandZutaten: str):
        self.__bestandZutaten = bestandZutaten

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def teig12(self):
        return self.__teig12
    @teig12.setter
    def teig12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lager__teig12", None)
        self.__teig12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lager13"):
                opp_val = getattr(old_value, "lager13", None)
                if opp_val == self:
                    setattr(old_value, "lager13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lager13"):
                opp_val = getattr(value, "lager13", None)
                setattr(value, "lager13", self)

    @property
    def zutat10(self):
        return self.__zutat10
    @zutat10.setter
    def zutat10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lager__zutat10", None)
        self.__zutat10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lager11"):
                opp_val = getattr(old_value, "lager11", None)
                if opp_val == self:
                    setattr(old_value, "lager11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lager11"):
                opp_val = getattr(value, "lager11", None)
                setattr(value, "lager11", self)

    @property
    def myException14(self):
        return self.__myException14
    @myException14.setter
    def myException14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lager__myException14", None)
        self.__myException14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lager15"):
                opp_val = getattr(old_value, "lager15", None)
                if opp_val == self:
                    setattr(old_value, "lager15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lager15"):
                opp_val = getattr(value, "lager15", None)
                setattr(value, "lager15", self)

    @property
    def auftrag9(self):
        return self.__auftrag9
    @auftrag9.setter
    def auftrag9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lager__auftrag9", None)
        self.__auftrag9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lager8"):
                opp_val = getattr(old_value, "lager8", None)
                if opp_val == self:
                    setattr(old_value, "lager8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lager8"):
                opp_val = getattr(value, "lager8", None)
                setattr(value, "lager8", self)

