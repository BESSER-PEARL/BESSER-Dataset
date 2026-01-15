from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class UML_14_Benanntes(ABC):

    def __init__(self, beschreibung: str, UML_14_Benanntes: set["UML_14_Kommentar"] = None, UML_14_Benanntes54: set["UML_14_Einschraenkung"] = None):
        self.beschreibung = beschreibung
        self.UML_14_Benanntes = UML_14_Benanntes if UML_14_Benanntes is not None else set()
        self.UML_14_Benanntes54 = UML_14_Benanntes54 if UML_14_Benanntes54 is not None else set()
        
    @property
    def beschreibung(self) -> str:
        return self.__beschreibung

    @beschreibung.setter
    def beschreibung(self, beschreibung: str):
        self.__beschreibung = beschreibung

    @property
    def UML_14_Benanntes(self):
        return self.__UML_14_Benanntes

    @UML_14_Benanntes.setter
    def UML_14_Benanntes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Benanntes__UML_14_Benanntes", None)
        self.__UML_14_Benanntes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Kommentar"):
                    opp_val = getattr(item, "UML_14_Kommentar", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Kommentar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Kommentar"):
                    opp_val = getattr(item, "UML_14_Kommentar", None)
                    
                    setattr(item, "UML_14_Kommentar", self)
                    

    @property
    def UML_14_Benanntes54(self):
        return self.__UML_14_Benanntes54

    @UML_14_Benanntes54.setter
    def UML_14_Benanntes54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Benanntes__UML_14_Benanntes54", None)
        self.__UML_14_Benanntes54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Einschraenkung"):
                    opp_val = getattr(item, "UML_14_Einschraenkung", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Einschraenkung", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Einschraenkung"):
                    opp_val = getattr(item, "UML_14_Einschraenkung", None)
                    
                    setattr(item, "UML_14_Einschraenkung", self)
                    

class UML_14_root:

    pass
class UML_14_Kommentar:

    def __init__(self, inhalt: str, UML_14_Kommentar: "UML_14_Benanntes" = None):
        self.inhalt = inhalt
        self.UML_14_Kommentar = UML_14_Kommentar
        
    @property
    def inhalt(self) -> str:
        return self.__inhalt

    @inhalt.setter
    def inhalt(self, inhalt: str):
        self.__inhalt = inhalt

    @property
    def UML_14_Kommentar(self):
        return self.__UML_14_Kommentar

    @UML_14_Kommentar.setter
    def UML_14_Kommentar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Kommentar__UML_14_Kommentar", None)
        self.__UML_14_Kommentar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Benanntes"):
                opp_val = getattr(old_value, "UML_14_Benanntes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Benanntes"):
                opp_val = getattr(value, "UML_14_Benanntes", None)
                if opp_val is None:
                    setattr(value, "UML_14_Benanntes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_Aufzaehlungswert:

    def __init__(self, wert: str, UML_14_Aufzaehlungswert: "UML_14_Aufzaehlung" = None):
        self.wert = wert
        self.UML_14_Aufzaehlungswert = UML_14_Aufzaehlungswert
        
    @property
    def wert(self) -> str:
        return self.__wert

    @wert.setter
    def wert(self, wert: str):
        self.__wert = wert

    @property
    def UML_14_Aufzaehlungswert(self):
        return self.__UML_14_Aufzaehlungswert

    @UML_14_Aufzaehlungswert.setter
    def UML_14_Aufzaehlungswert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Aufzaehlungswert__UML_14_Aufzaehlungswert", None)
        self.__UML_14_Aufzaehlungswert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Aufzaehlung33"):
                opp_val = getattr(old_value, "UML_14_Aufzaehlung33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Aufzaehlung33"):
                opp_val = getattr(value, "UML_14_Aufzaehlung33", None)
                if opp_val is None:
                    setattr(value, "UML_14_Aufzaehlung33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_Vererbung:

    def __init__(self, unterscheidung: str, UML_14_Vererbung: set["UML_14_Konzept"] = None, UML_14_Vererbung14: set["UML_14_Konzept"] = None, UML_14_Vererbung46: "UML_14_Schachtel" = None):
        self.unterscheidung = unterscheidung
        self.UML_14_Vererbung = UML_14_Vererbung if UML_14_Vererbung is not None else set()
        self.UML_14_Vererbung14 = UML_14_Vererbung14 if UML_14_Vererbung14 is not None else set()
        self.UML_14_Vererbung46 = UML_14_Vererbung46
        
    @property
    def unterscheidung(self) -> str:
        return self.__unterscheidung

    @unterscheidung.setter
    def unterscheidung(self, unterscheidung: str):
        self.__unterscheidung = unterscheidung

    @property
    def UML_14_Vererbung(self):
        return self.__UML_14_Vererbung

    @UML_14_Vererbung.setter
    def UML_14_Vererbung(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Vererbung__UML_14_Vererbung", None)
        self.__UML_14_Vererbung = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Konzept"):
                    opp_val = getattr(item, "UML_14_Konzept", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Konzept", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Konzept"):
                    opp_val = getattr(item, "UML_14_Konzept", None)
                    
                    setattr(item, "UML_14_Konzept", self)
                    

    @property
    def UML_14_Vererbung14(self):
        return self.__UML_14_Vererbung14

    @UML_14_Vererbung14.setter
    def UML_14_Vererbung14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Vererbung__UML_14_Vererbung14", None)
        self.__UML_14_Vererbung14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Konzept15"):
                    opp_val = getattr(item, "UML_14_Konzept15", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Konzept15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Konzept15"):
                    opp_val = getattr(item, "UML_14_Konzept15", None)
                    
                    setattr(item, "UML_14_Konzept15", self)
                    

    @property
    def UML_14_Vererbung46(self):
        return self.__UML_14_Vererbung46

    @UML_14_Vererbung46.setter
    def UML_14_Vererbung46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Vererbung__UML_14_Vererbung46", None)
        self.__UML_14_Vererbung46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Schachtel45"):
                opp_val = getattr(old_value, "UML_14_Schachtel45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Schachtel45"):
                opp_val = getattr(value, "UML_14_Schachtel45", None)
                if opp_val is None:
                    setattr(value, "UML_14_Schachtel45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Benanntes:

    pass
class UML_14_Einfach(Benanntes):

    pass
class UML_14_Aufzaehlung(Benanntes):

    pass
class UML_14_Verbindung(Benanntes):

    pass
class UML_14_Konzept(Benanntes):

    def __init__(self, istAktiev: str, UML_14_Konzept: "UML_14_Vererbung" = None, UML_14_Konzept15: "UML_14_Vererbung" = None, UML_14_Konzept27: set["UML_14_Eigenschaft"] = None, UML_14_Konzept30: set["UML_14_Verhalten"] = None, UML_14_Konzept19: "UML_14_Verbindungsende" = None, UML_14_Konzept37: "UML_14_Schachtel" = None):
        self.istAktiev = istAktiev
        self.UML_14_Konzept = UML_14_Konzept
        self.UML_14_Konzept15 = UML_14_Konzept15
        self.UML_14_Konzept27 = UML_14_Konzept27 if UML_14_Konzept27 is not None else set()
        self.UML_14_Konzept30 = UML_14_Konzept30 if UML_14_Konzept30 is not None else set()
        self.UML_14_Konzept19 = UML_14_Konzept19
        self.UML_14_Konzept37 = UML_14_Konzept37
        
    @property
    def istAktiev(self) -> str:
        return self.__istAktiev

    @istAktiev.setter
    def istAktiev(self, istAktiev: str):
        self.__istAktiev = istAktiev

    @property
    def UML_14_Konzept27(self):
        return self.__UML_14_Konzept27

    @UML_14_Konzept27.setter
    def UML_14_Konzept27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Konzept__UML_14_Konzept27", None)
        self.__UML_14_Konzept27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Eigenschaft28"):
                    opp_val = getattr(item, "UML_14_Eigenschaft28", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Eigenschaft28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Eigenschaft28"):
                    opp_val = getattr(item, "UML_14_Eigenschaft28", None)
                    
                    setattr(item, "UML_14_Eigenschaft28", self)
                    

    @property
    def UML_14_Konzept37(self):
        return self.__UML_14_Konzept37

    @UML_14_Konzept37.setter
    def UML_14_Konzept37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Konzept__UML_14_Konzept37", None)
        self.__UML_14_Konzept37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Schachtel36"):
                opp_val = getattr(old_value, "UML_14_Schachtel36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Schachtel36"):
                opp_val = getattr(value, "UML_14_Schachtel36", None)
                if opp_val is None:
                    setattr(value, "UML_14_Schachtel36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_14_Konzept19(self):
        return self.__UML_14_Konzept19

    @UML_14_Konzept19.setter
    def UML_14_Konzept19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Konzept__UML_14_Konzept19", None)
        self.__UML_14_Konzept19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Verbindungsende"):
                opp_val = getattr(old_value, "UML_14_Verbindungsende", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Verbindungsende", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Verbindungsende"):
                opp_val = getattr(value, "UML_14_Verbindungsende", None)
                setattr(value, "UML_14_Verbindungsende", self)

    @property
    def UML_14_Konzept30(self):
        return self.__UML_14_Konzept30

    @UML_14_Konzept30.setter
    def UML_14_Konzept30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Konzept__UML_14_Konzept30", None)
        self.__UML_14_Konzept30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_14_Verhalten31"):
                    opp_val = getattr(item, "UML_14_Verhalten31", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_14_Verhalten31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_14_Verhalten31"):
                    opp_val = getattr(item, "UML_14_Verhalten31", None)
                    
                    setattr(item, "UML_14_Verhalten31", self)
                    

    @property
    def UML_14_Konzept(self):
        return self.__UML_14_Konzept

    @UML_14_Konzept.setter
    def UML_14_Konzept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Konzept__UML_14_Konzept", None)
        self.__UML_14_Konzept = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Vererbung"):
                opp_val = getattr(old_value, "UML_14_Vererbung", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Vererbung"):
                opp_val = getattr(value, "UML_14_Vererbung", None)
                if opp_val is None:
                    setattr(value, "UML_14_Vererbung", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_14_Konzept15(self):
        return self.__UML_14_Konzept15

    @UML_14_Konzept15.setter
    def UML_14_Konzept15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Konzept__UML_14_Konzept15", None)
        self.__UML_14_Konzept15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Vererbung14"):
                opp_val = getattr(old_value, "UML_14_Vererbung14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Vererbung14"):
                opp_val = getattr(value, "UML_14_Vererbung14", None)
                if opp_val is None:
                    setattr(value, "UML_14_Vererbung14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_Schachtel(Benanntes):

    pass
class UML_14_Verbindungsende(Benanntes):

    def __init__(self, istNavigierbar: str, sichtbarkeit: str, UML_14_Verbindungsende: "UML_14_Konzept" = None, UML_14_Verbindungsende21: "UML_14_InstanzAnzahl" = None, UML_14_Verbindungsende24: "UML_14_Eigenschaft" = None, Verbindungsende: "UML_14_Verbindung" = None, verbinder: "UML_14_Verbindung" = None):
        self.istNavigierbar = istNavigierbar
        self.sichtbarkeit = sichtbarkeit
        self.UML_14_Verbindungsende = UML_14_Verbindungsende
        self.UML_14_Verbindungsende21 = UML_14_Verbindungsende21
        self.UML_14_Verbindungsende24 = UML_14_Verbindungsende24
        self.Verbindungsende = Verbindungsende
        self.verbinder = verbinder
        
    @property
    def istNavigierbar(self) -> str:
        return self.__istNavigierbar

    @istNavigierbar.setter
    def istNavigierbar(self, istNavigierbar: str):
        self.__istNavigierbar = istNavigierbar

    @property
    def sichtbarkeit(self) -> str:
        return self.__sichtbarkeit

    @sichtbarkeit.setter
    def sichtbarkeit(self, sichtbarkeit: str):
        self.__sichtbarkeit = sichtbarkeit

    @property
    def Verbindungsende(self):
        return self.__Verbindungsende

    @Verbindungsende.setter
    def Verbindungsende(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Verbindungsende__Verbindungsende", None)
        self.__Verbindungsende = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "link"):
                opp_val = getattr(old_value, "link", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "link"):
                opp_val = getattr(value, "link", None)
                if opp_val is None:
                    setattr(value, "link", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_14_Verbindungsende(self):
        return self.__UML_14_Verbindungsende

    @UML_14_Verbindungsende.setter
    def UML_14_Verbindungsende(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Verbindungsende__UML_14_Verbindungsende", None)
        self.__UML_14_Verbindungsende = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Konzept19"):
                opp_val = getattr(old_value, "UML_14_Konzept19", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Konzept19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Konzept19"):
                opp_val = getattr(value, "UML_14_Konzept19", None)
                setattr(value, "UML_14_Konzept19", self)

    @property
    def UML_14_Verbindungsende24(self):
        return self.__UML_14_Verbindungsende24

    @UML_14_Verbindungsende24.setter
    def UML_14_Verbindungsende24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Verbindungsende__UML_14_Verbindungsende24", None)
        self.__UML_14_Verbindungsende24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Eigenschaft25"):
                opp_val = getattr(old_value, "UML_14_Eigenschaft25", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Eigenschaft25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Eigenschaft25"):
                opp_val = getattr(value, "UML_14_Eigenschaft25", None)
                setattr(value, "UML_14_Eigenschaft25", self)

    @property
    def UML_14_Verbindungsende21(self):
        return self.__UML_14_Verbindungsende21

    @UML_14_Verbindungsende21.setter
    def UML_14_Verbindungsende21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Verbindungsende__UML_14_Verbindungsende21", None)
        self.__UML_14_Verbindungsende21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_InstanzAnzahl22"):
                opp_val = getattr(old_value, "UML_14_InstanzAnzahl22", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_InstanzAnzahl22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_InstanzAnzahl22"):
                opp_val = getattr(value, "UML_14_InstanzAnzahl22", None)
                setattr(value, "UML_14_InstanzAnzahl22", self)

    @property
    def verbinder(self):
        return self.__verbinder

    @verbinder.setter
    def verbinder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Verbindungsende__verbinder", None)
        self.__verbinder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Verbindung"):
                opp_val = getattr(old_value, "Verbindung", None)
                if opp_val == self:
                    setattr(old_value, "Verbindung", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Verbindung"):
                opp_val = getattr(value, "Verbindung", None)
                setattr(value, "Verbindung", self)

class UML_14_MethodenWert(Benanntes):

    def __init__(self, art: str, standartWert: str, UML_14_MethodenWert4: "UML_14_Verhalten" = None, UML_14_MethodenWert: "UML_14_Aufzaehlung" = None, UML_14_MethodenWert2: "UML_14_Einfach" = None):
        self.art = art
        self.standartWert = standartWert
        self.UML_14_MethodenWert4 = UML_14_MethodenWert4
        self.UML_14_MethodenWert = UML_14_MethodenWert
        self.UML_14_MethodenWert2 = UML_14_MethodenWert2
        
    @property
    def art(self) -> str:
        return self.__art

    @art.setter
    def art(self, art: str):
        self.__art = art

    @property
    def standartWert(self) -> str:
        return self.__standartWert

    @standartWert.setter
    def standartWert(self, standartWert: str):
        self.__standartWert = standartWert

    @property
    def UML_14_MethodenWert2(self):
        return self.__UML_14_MethodenWert2

    @UML_14_MethodenWert2.setter
    def UML_14_MethodenWert2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_MethodenWert__UML_14_MethodenWert2", None)
        self.__UML_14_MethodenWert2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Einfach"):
                opp_val = getattr(old_value, "UML_14_Einfach", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Einfach", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Einfach"):
                opp_val = getattr(value, "UML_14_Einfach", None)
                setattr(value, "UML_14_Einfach", self)

    @property
    def UML_14_MethodenWert4(self):
        return self.__UML_14_MethodenWert4

    @UML_14_MethodenWert4.setter
    def UML_14_MethodenWert4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_MethodenWert__UML_14_MethodenWert4", None)
        self.__UML_14_MethodenWert4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Verhalten"):
                opp_val = getattr(old_value, "UML_14_Verhalten", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Verhalten", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Verhalten"):
                opp_val = getattr(value, "UML_14_Verhalten", None)
                setattr(value, "UML_14_Verhalten", self)

    @property
    def UML_14_MethodenWert(self):
        return self.__UML_14_MethodenWert

    @UML_14_MethodenWert.setter
    def UML_14_MethodenWert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_MethodenWert__UML_14_MethodenWert", None)
        self.__UML_14_MethodenWert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Aufzaehlung"):
                opp_val = getattr(old_value, "UML_14_Aufzaehlung", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Aufzaehlung", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Aufzaehlung"):
                opp_val = getattr(value, "UML_14_Aufzaehlung", None)
                setattr(value, "UML_14_Aufzaehlung", self)

class UML_14_Eigenschaft(Benanntes):

    def __init__(self, initialWert: str, sichtbarkeit: str, UML_14_Eigenschaft: "UML_14_InstanzAnzahl" = None, UML_14_Eigenschaft7: "UML_14_Aufzaehlung" = None, UML_14_Eigenschaft10: "UML_14_Einfach" = None, UML_14_Eigenschaft25: "UML_14_Verbindungsende" = None, UML_14_Eigenschaft28: "UML_14_Konzept" = None):
        self.initialWert = initialWert
        self.sichtbarkeit = sichtbarkeit
        self.UML_14_Eigenschaft = UML_14_Eigenschaft
        self.UML_14_Eigenschaft7 = UML_14_Eigenschaft7
        self.UML_14_Eigenschaft10 = UML_14_Eigenschaft10
        self.UML_14_Eigenschaft25 = UML_14_Eigenschaft25
        self.UML_14_Eigenschaft28 = UML_14_Eigenschaft28
        
    @property
    def sichtbarkeit(self) -> str:
        return self.__sichtbarkeit

    @sichtbarkeit.setter
    def sichtbarkeit(self, sichtbarkeit: str):
        self.__sichtbarkeit = sichtbarkeit

    @property
    def initialWert(self) -> str:
        return self.__initialWert

    @initialWert.setter
    def initialWert(self, initialWert: str):
        self.__initialWert = initialWert

    @property
    def UML_14_Eigenschaft10(self):
        return self.__UML_14_Eigenschaft10

    @UML_14_Eigenschaft10.setter
    def UML_14_Eigenschaft10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Eigenschaft__UML_14_Eigenschaft10", None)
        self.__UML_14_Eigenschaft10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Einfach11"):
                opp_val = getattr(old_value, "UML_14_Einfach11", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Einfach11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Einfach11"):
                opp_val = getattr(value, "UML_14_Einfach11", None)
                setattr(value, "UML_14_Einfach11", self)

    @property
    def UML_14_Eigenschaft28(self):
        return self.__UML_14_Eigenschaft28

    @UML_14_Eigenschaft28.setter
    def UML_14_Eigenschaft28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Eigenschaft__UML_14_Eigenschaft28", None)
        self.__UML_14_Eigenschaft28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Konzept27"):
                opp_val = getattr(old_value, "UML_14_Konzept27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Konzept27"):
                opp_val = getattr(value, "UML_14_Konzept27", None)
                if opp_val is None:
                    setattr(value, "UML_14_Konzept27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_14_Eigenschaft25(self):
        return self.__UML_14_Eigenschaft25

    @UML_14_Eigenschaft25.setter
    def UML_14_Eigenschaft25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Eigenschaft__UML_14_Eigenschaft25", None)
        self.__UML_14_Eigenschaft25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Verbindungsende24"):
                opp_val = getattr(old_value, "UML_14_Verbindungsende24", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Verbindungsende24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Verbindungsende24"):
                opp_val = getattr(value, "UML_14_Verbindungsende24", None)
                setattr(value, "UML_14_Verbindungsende24", self)

    @property
    def UML_14_Eigenschaft(self):
        return self.__UML_14_Eigenschaft

    @UML_14_Eigenschaft.setter
    def UML_14_Eigenschaft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Eigenschaft__UML_14_Eigenschaft", None)
        self.__UML_14_Eigenschaft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_InstanzAnzahl"):
                opp_val = getattr(old_value, "UML_14_InstanzAnzahl", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_InstanzAnzahl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_InstanzAnzahl"):
                opp_val = getattr(value, "UML_14_InstanzAnzahl", None)
                setattr(value, "UML_14_InstanzAnzahl", self)

    @property
    def UML_14_Eigenschaft7(self):
        return self.__UML_14_Eigenschaft7

    @UML_14_Eigenschaft7.setter
    def UML_14_Eigenschaft7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Eigenschaft__UML_14_Eigenschaft7", None)
        self.__UML_14_Eigenschaft7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Aufzaehlung8"):
                opp_val = getattr(old_value, "UML_14_Aufzaehlung8", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Aufzaehlung8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Aufzaehlung8"):
                opp_val = getattr(value, "UML_14_Aufzaehlung8", None)
                setattr(value, "UML_14_Aufzaehlung8", self)

class UML_14_Verhalten(Benanntes):

    def __init__(self, inhlat: str, sichtbarkeit: str, UML_14_Verhalten: "UML_14_MethodenWert" = None, UML_14_Verhalten31: "UML_14_Konzept" = None):
        self.inhlat = inhlat
        self.sichtbarkeit = sichtbarkeit
        self.UML_14_Verhalten = UML_14_Verhalten
        self.UML_14_Verhalten31 = UML_14_Verhalten31
        
    @property
    def inhlat(self) -> str:
        return self.__inhlat

    @inhlat.setter
    def inhlat(self, inhlat: str):
        self.__inhlat = inhlat

    @property
    def sichtbarkeit(self) -> str:
        return self.__sichtbarkeit

    @sichtbarkeit.setter
    def sichtbarkeit(self, sichtbarkeit: str):
        self.__sichtbarkeit = sichtbarkeit

    @property
    def UML_14_Verhalten(self):
        return self.__UML_14_Verhalten

    @UML_14_Verhalten.setter
    def UML_14_Verhalten(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Verhalten__UML_14_Verhalten", None)
        self.__UML_14_Verhalten = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_MethodenWert4"):
                opp_val = getattr(old_value, "UML_14_MethodenWert4", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_MethodenWert4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_MethodenWert4"):
                opp_val = getattr(value, "UML_14_MethodenWert4", None)
                setattr(value, "UML_14_MethodenWert4", self)

    @property
    def UML_14_Verhalten31(self):
        return self.__UML_14_Verhalten31

    @UML_14_Verhalten31.setter
    def UML_14_Verhalten31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Verhalten__UML_14_Verhalten31", None)
        self.__UML_14_Verhalten31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Konzept30"):
                opp_val = getattr(old_value, "UML_14_Konzept30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Konzept30"):
                opp_val = getattr(value, "UML_14_Konzept30", None)
                if opp_val is None:
                    setattr(value, "UML_14_Konzept30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_14_InstanzAnzahl:

    def __init__(self, untergrenze: str, obergrenze: str, UML_14_InstanzAnzahl: "UML_14_Eigenschaft" = None, UML_14_InstanzAnzahl22: "UML_14_Verbindungsende" = None):
        self.untergrenze = untergrenze
        self.obergrenze = obergrenze
        self.UML_14_InstanzAnzahl = UML_14_InstanzAnzahl
        self.UML_14_InstanzAnzahl22 = UML_14_InstanzAnzahl22
        
    @property
    def untergrenze(self) -> str:
        return self.__untergrenze

    @untergrenze.setter
    def untergrenze(self, untergrenze: str):
        self.__untergrenze = untergrenze

    @property
    def obergrenze(self) -> str:
        return self.__obergrenze

    @obergrenze.setter
    def obergrenze(self, obergrenze: str):
        self.__obergrenze = obergrenze

    @property
    def UML_14_InstanzAnzahl(self):
        return self.__UML_14_InstanzAnzahl

    @UML_14_InstanzAnzahl.setter
    def UML_14_InstanzAnzahl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_InstanzAnzahl__UML_14_InstanzAnzahl", None)
        self.__UML_14_InstanzAnzahl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Eigenschaft"):
                opp_val = getattr(old_value, "UML_14_Eigenschaft", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Eigenschaft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Eigenschaft"):
                opp_val = getattr(value, "UML_14_Eigenschaft", None)
                setattr(value, "UML_14_Eigenschaft", self)

    @property
    def UML_14_InstanzAnzahl22(self):
        return self.__UML_14_InstanzAnzahl22

    @UML_14_InstanzAnzahl22.setter
    def UML_14_InstanzAnzahl22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_InstanzAnzahl__UML_14_InstanzAnzahl22", None)
        self.__UML_14_InstanzAnzahl22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Verbindungsende21"):
                opp_val = getattr(old_value, "UML_14_Verbindungsende21", None)
                if opp_val == self:
                    setattr(old_value, "UML_14_Verbindungsende21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Verbindungsende21"):
                opp_val = getattr(value, "UML_14_Verbindungsende21", None)
                setattr(value, "UML_14_Verbindungsende21", self)

class UML_14_Einschraenkung:

    def __init__(self, beschreibung: str, UML_14_Einschraenkung: "UML_14_Benanntes" = None):
        self.beschreibung = beschreibung
        self.UML_14_Einschraenkung = UML_14_Einschraenkung
        
    @property
    def beschreibung(self) -> str:
        return self.__beschreibung

    @beschreibung.setter
    def beschreibung(self, beschreibung: str):
        self.__beschreibung = beschreibung

    @property
    def UML_14_Einschraenkung(self):
        return self.__UML_14_Einschraenkung

    @UML_14_Einschraenkung.setter
    def UML_14_Einschraenkung(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_14_Einschraenkung__UML_14_Einschraenkung", None)
        self.__UML_14_Einschraenkung = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_14_Benanntes54"):
                opp_val = getattr(old_value, "UML_14_Benanntes54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_14_Benanntes54"):
                opp_val = getattr(value, "UML_14_Benanntes54", None)
                if opp_val is None:
                    setattr(value, "UML_14_Benanntes54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
