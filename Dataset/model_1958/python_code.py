from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SchadensTyp(Enum):
    koerperlich = "koerperlich"
    geistig = "geistig"
    speziell = "speziell"
class ZauberReichweite(Enum):
    Blickfeld = "Blickfeld"
    Begrenzt = "Begrenzt"
    Selbst = "Selbst"
    Beruehrung = "Beruehrung"
class ZauberArt(Enum):
    Mana = "Mana"
    Physisch = "Physisch"
class ModifikatorType(Enum):
    Natural = "Natural"
    Cyber = "Cyber"
    Bio = "Bio"
class MagazinTyp(Enum):
    Streifen = "Streifen"
    Clip = "Clip"
    Trommel = "Trommel"
    Gurt = "Gurt"
class ZauberDauer(Enum):
    Sofort = "Sofort"
    Aufrechterhalten = "Aufrechterhalten"
    Permanent = "Permanent"
class Tragbar(Enum):
    einhaendig = "einhaendig"
    zweihaendig = "zweihaendig"
class FeuerModus(Enum):
    EM = "EM"
    HM = "HM"
    SM = "SM"
    AM = "AM"
class SmartgunType(Enum):
    SmartBrille = "SmartBrille"
    SmartGun = "SmartGun"
    SmatgunII = "SmatgunII"
class Koerperteil(Enum):
    Rumpf = "Rumpf"
    Kopf = "Kopf"
    Arme = "Arme"
    Beine = "Beine"


############################################
# Definition of Classes
############################################

class shadowrun_Schadenswiederstand(ABC):

    def __init__(self, ruestungsSchutzStoss: int, ruestungsSchutzBalistisch: int):
        self.ruestungsSchutzStoss = ruestungsSchutzStoss
        self.ruestungsSchutzBalistisch = ruestungsSchutzBalistisch
        
    @property
    def ruestungsSchutzBalistisch(self) -> int:
        return self.__ruestungsSchutzBalistisch

    @ruestungsSchutzBalistisch.setter
    def ruestungsSchutzBalistisch(self, ruestungsSchutzBalistisch: int):
        self.__ruestungsSchutzBalistisch = ruestungsSchutzBalistisch

    @property
    def ruestungsSchutzStoss(self) -> int:
        return self.__ruestungsSchutzStoss

    @ruestungsSchutzStoss.setter
    def ruestungsSchutzStoss(self, ruestungsSchutzStoss: int):
        self.__ruestungsSchutzStoss = ruestungsSchutzStoss

class shadowrun_GegenstandStufen(ABC):

    def __init__(self, Computer: int, Elektronik: int, Tracing: int, AntiTracing: int, Protection: int, AntiProtection: int):
        self.Computer = Computer
        self.Elektronik = Elektronik
        self.Tracing = Tracing
        self.AntiTracing = AntiTracing
        self.Protection = Protection
        self.AntiProtection = AntiProtection
        
    @property
    def Protection(self) -> int:
        return self.__Protection

    @Protection.setter
    def Protection(self, Protection: int):
        self.__Protection = Protection

    @property
    def Elektronik(self) -> int:
        return self.__Elektronik

    @Elektronik.setter
    def Elektronik(self, Elektronik: int):
        self.__Elektronik = Elektronik

    @property
    def AntiProtection(self) -> int:
        return self.__AntiProtection

    @AntiProtection.setter
    def AntiProtection(self, AntiProtection: int):
        self.__AntiProtection = AntiProtection

    @property
    def Tracing(self) -> int:
        return self.__Tracing

    @Tracing.setter
    def Tracing(self, Tracing: int):
        self.__Tracing = Tracing

    @property
    def AntiTracing(self) -> int:
        return self.__AntiTracing

    @AntiTracing.setter
    def AntiTracing(self, AntiTracing: int):
        self.__AntiTracing = AntiTracing

    @property
    def Computer(self) -> int:
        return self.__Computer

    @Computer.setter
    def Computer(self, Computer: int):
        self.__Computer = Computer

class shadowrun_BodyIndex(ABC):

    def __init__(self, bodyIndex: int):
        self.bodyIndex = bodyIndex
        
    @property
    def bodyIndex(self) -> int:
        return self.__bodyIndex

    @bodyIndex.setter
    def bodyIndex(self, bodyIndex: int):
        self.__bodyIndex = bodyIndex

class shadowrun_Essenz(ABC):

    def __init__(self, Essenz: int):
        self.Essenz = Essenz
        
    @property
    def Essenz(self) -> int:
        return self.__Essenz

    @Essenz.setter
    def Essenz(self, Essenz: int):
        self.__Essenz = Essenz

class shadowrun_GeistigeAttribute(ABC):

    def __init__(self, Inteligenz: int, Charisma: int, Willenskraft: int):
        self.Inteligenz = Inteligenz
        self.Charisma = Charisma
        self.Willenskraft = Willenskraft
        
    @property
    def Charisma(self) -> int:
        return self.__Charisma

    @Charisma.setter
    def Charisma(self, Charisma: int):
        self.__Charisma = Charisma

    @property
    def Inteligenz(self) -> int:
        return self.__Inteligenz

    @Inteligenz.setter
    def Inteligenz(self, Inteligenz: int):
        self.__Inteligenz = Inteligenz

    @property
    def Willenskraft(self) -> int:
        return self.__Willenskraft

    @Willenskraft.setter
    def Willenskraft(self, Willenskraft: int):
        self.__Willenskraft = Willenskraft

class MagiePersona:

    pass
class shadowrun_Shamane(MagiePersona):

    pass
class shadowrun_NahkampfReichweite(ABC):

    def __init__(self, reichweite: int):
        self.reichweite = reichweite
        
    @property
    def reichweite(self) -> int:
        return self.__reichweite

    @reichweite.setter
    def reichweite(self, reichweite: int):
        self.__reichweite = reichweite

class shadowrun_FernkampfwaffenModifikatoren(ABC):

    def __init__(self, Rueckstoss: int, lasterPointer: bool, Schalldaempfer: bool, Vergroesserung: int, Smartgun: str):
        self.Rueckstoss = Rueckstoss
        self.lasterPointer = lasterPointer
        self.Schalldaempfer = Schalldaempfer
        self.Vergroesserung = Vergroesserung
        self.Smartgun = Smartgun
        
    @property
    def lasterPointer(self) -> bool:
        return self.__lasterPointer

    @lasterPointer.setter
    def lasterPointer(self, lasterPointer: bool):
        self.__lasterPointer = lasterPointer

    @property
    def Vergroesserung(self) -> int:
        return self.__Vergroesserung

    @Vergroesserung.setter
    def Vergroesserung(self, Vergroesserung: int):
        self.__Vergroesserung = Vergroesserung

    @property
    def Schalldaempfer(self) -> bool:
        return self.__Schalldaempfer

    @Schalldaempfer.setter
    def Schalldaempfer(self, Schalldaempfer: bool):
        self.__Schalldaempfer = Schalldaempfer

    @property
    def Smartgun(self) -> str:
        return self.__Smartgun

    @Smartgun.setter
    def Smartgun(self, Smartgun: str):
        self.__Smartgun = Smartgun

    @property
    def Rueckstoss(self) -> int:
        return self.__Rueckstoss

    @Rueckstoss.setter
    def Rueckstoss(self, Rueckstoss: int):
        self.__Rueckstoss = Rueckstoss

class shadowrun_EObject:

    pass
class shadowrun_Bemerkbar(ABC):

    def __init__(self, tarnstufe: int):
        self.tarnstufe = tarnstufe
        
    @property
    def tarnstufe(self) -> int:
        return self.__tarnstufe

    @tarnstufe.setter
    def tarnstufe(self, tarnstufe: int):
        self.__tarnstufe = tarnstufe

class AbstraktNahkampfwaffe:

    pass
class shadowrun_Nahkampfwaffe(AbstraktNahkampfwaffe):

    pass
class shadowrun_BerechneteAttribute(ABC):

    def __init__(self, Reaktion: int, ReaktionW: int, Kampfpool: int):
        self.Reaktion = Reaktion
        self.ReaktionW = ReaktionW
        self.Kampfpool = Kampfpool
        
    @property
    def Reaktion(self) -> int:
        return self.__Reaktion

    @Reaktion.setter
    def Reaktion(self, Reaktion: int):
        self.__Reaktion = Reaktion

    @property
    def ReaktionW(self) -> int:
        return self.__ReaktionW

    @ReaktionW.setter
    def ReaktionW(self, ReaktionW: int):
        self.__ReaktionW = ReaktionW

    @property
    def Kampfpool(self) -> int:
        return self.__Kampfpool

    @Kampfpool.setter
    def Kampfpool(self, Kampfpool: int):
        self.__Kampfpool = Kampfpool

class Schadenswiederstand:

    pass
class shadowrun_KoerperlicheAtribute(Schadenswiederstand):

    def __init__(self, Konsitution: int, Staerke: int, Schnelligkeit: int):
        self.Konsitution = Konsitution
        self.Staerke = Staerke
        self.Schnelligkeit = Schnelligkeit
        
    @property
    def Konsitution(self) -> int:
        return self.__Konsitution

    @Konsitution.setter
    def Konsitution(self, Konsitution: int):
        self.__Konsitution = Konsitution

    @property
    def Schnelligkeit(self) -> int:
        return self.__Schnelligkeit

    @Schnelligkeit.setter
    def Schnelligkeit(self, Schnelligkeit: int):
        self.__Schnelligkeit = Schnelligkeit

    @property
    def Staerke(self) -> int:
        return self.__Staerke

    @Staerke.setter
    def Staerke(self, Staerke: int):
        self.__Staerke = Staerke

class shadowrun_Quelle(ABC):

    def __init__(self, page: str, shadowrun_Quelle: "shadowrun_SourceBook" = None):
        self.page = page
        self.shadowrun_Quelle = shadowrun_Quelle
        
    @property
    def page(self) -> str:
        return self.__page

    @page.setter
    def page(self, page: str):
        self.__page = page

    @property
    def shadowrun_Quelle(self):
        return self.__shadowrun_Quelle

    @shadowrun_Quelle.setter
    def shadowrun_Quelle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Quelle__shadowrun_Quelle", None)
        self.__shadowrun_Quelle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_SourceBook"):
                opp_val = getattr(old_value, "shadowrun_SourceBook", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_SourceBook", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_SourceBook"):
                opp_val = getattr(value, "shadowrun_SourceBook", None)
                setattr(value, "shadowrun_SourceBook", self)

class shadowrun_WarenListe:

    def __init__(self, listenWert: str, strassenWert: str, shadowrun_WarenListe: set["shadowrun_AbstaktGegenstand"] = None):
        self.listenWert = listenWert
        self.strassenWert = strassenWert
        self.shadowrun_WarenListe = shadowrun_WarenListe if shadowrun_WarenListe is not None else set()
        
    @property
    def strassenWert(self) -> str:
        return self.__strassenWert

    @strassenWert.setter
    def strassenWert(self, strassenWert: str):
        self.__strassenWert = strassenWert

    @property
    def listenWert(self) -> str:
        return self.__listenWert

    @listenWert.setter
    def listenWert(self, listenWert: str):
        self.__listenWert = listenWert

    @property
    def shadowrun_WarenListe(self):
        return self.__shadowrun_WarenListe

    @shadowrun_WarenListe.setter
    def shadowrun_WarenListe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_WarenListe__shadowrun_WarenListe", None)
        self.__shadowrun_WarenListe = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shadowrun_AbstaktGegenstand67"):
                    opp_val = getattr(item, "shadowrun_AbstaktGegenstand67", None)
                    
                    if opp_val == self:
                        setattr(item, "shadowrun_AbstaktGegenstand67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shadowrun_AbstaktGegenstand67"):
                    opp_val = getattr(item, "shadowrun_AbstaktGegenstand67", None)
                    
                    setattr(item, "shadowrun_AbstaktGegenstand67", self)
                    

class shadowrun_Sichtverhaeltnisse(ABC):

    def __init__(self, Restlichtverstaerkung: str, Infrarot: str, Ultrasound: str):
        self.Restlichtverstaerkung = Restlichtverstaerkung
        self.Infrarot = Infrarot
        self.Ultrasound = Ultrasound
        
    @property
    def Ultrasound(self) -> str:
        return self.__Ultrasound

    @Ultrasound.setter
    def Ultrasound(self, Ultrasound: str):
        self.__Ultrasound = Ultrasound

    @property
    def Restlichtverstaerkung(self) -> str:
        return self.__Restlichtverstaerkung

    @Restlichtverstaerkung.setter
    def Restlichtverstaerkung(self, Restlichtverstaerkung: str):
        self.__Restlichtverstaerkung = Restlichtverstaerkung

    @property
    def Infrarot(self) -> str:
        return self.__Infrarot

    @Infrarot.setter
    def Infrarot(self, Infrarot: str):
        self.__Infrarot = Infrarot

class shadowrun_PersonaZauber:

    def __init__(self, stufe: int, shadowrun_PersonaZauber: "shadowrun_MagiePersona" = None, shadowrun_PersonaZauber62: "shadowrun_Zauber" = None):
        self.stufe = stufe
        self.shadowrun_PersonaZauber = shadowrun_PersonaZauber
        self.shadowrun_PersonaZauber62 = shadowrun_PersonaZauber62
        
    @property
    def stufe(self) -> int:
        return self.__stufe

    @stufe.setter
    def stufe(self, stufe: int):
        self.__stufe = stufe

    @property
    def shadowrun_PersonaZauber62(self):
        return self.__shadowrun_PersonaZauber62

    @shadowrun_PersonaZauber62.setter
    def shadowrun_PersonaZauber62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_PersonaZauber__shadowrun_PersonaZauber62", None)
        self.__shadowrun_PersonaZauber62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Zauber"):
                opp_val = getattr(old_value, "shadowrun_Zauber", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_Zauber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Zauber"):
                opp_val = getattr(value, "shadowrun_Zauber", None)
                setattr(value, "shadowrun_Zauber", self)

    @property
    def shadowrun_PersonaZauber(self):
        return self.__shadowrun_PersonaZauber

    @shadowrun_PersonaZauber.setter
    def shadowrun_PersonaZauber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_PersonaZauber__shadowrun_PersonaZauber", None)
        self.__shadowrun_PersonaZauber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_MagiePersona"):
                opp_val = getattr(old_value, "shadowrun_MagiePersona", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_MagiePersona"):
                opp_val = getattr(value, "shadowrun_MagiePersona", None)
                if opp_val is None:
                    setattr(value, "shadowrun_MagiePersona", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractMagier:

    pass
class shadowrun_Legalitaet(ABC):

    def __init__(self, legalitaet: str):
        self.legalitaet = legalitaet
        
    @property
    def legalitaet(self) -> str:
        return self.__legalitaet

    @legalitaet.setter
    def legalitaet(self, legalitaet: str):
        self.__legalitaet = legalitaet

class shadowrun_Reichweiten:

    pass
class shadowrun_Beschreibbar(ABC):

    def __init__(self, name: str, beschreibung: str, image: str):
        self.name = name
        self.beschreibung = beschreibung
        self.image = image
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def beschreibung(self) -> str:
        return self.__beschreibung

    @beschreibung.setter
    def beschreibung(self, beschreibung: str):
        self.__beschreibung = beschreibung

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

class shadowrun_GengenstandListe:

    pass
class AbstractMagischePaersona:

    pass
class shadowrun_MagiePersona(AbstractMagischePaersona, AbstractMagier):

    pass
class BaseMagischePersona:

    pass
class shadowrun_AbstractMagier(BaseMagischePersona):

    def __init__(self, Astralpool: int, MagiePool: int, InitationsGrad: int):
        self.Astralpool = Astralpool
        self.MagiePool = MagiePool
        self.InitationsGrad = InitationsGrad
        
    @property
    def Astralpool(self) -> int:
        return self.__Astralpool

    @Astralpool.setter
    def Astralpool(self, Astralpool: int):
        self.__Astralpool = Astralpool

    @property
    def MagiePool(self) -> int:
        return self.__MagiePool

    @MagiePool.setter
    def MagiePool(self, MagiePool: int):
        self.__MagiePool = MagiePool

    @property
    def InitationsGrad(self) -> int:
        return self.__InitationsGrad

    @InitationsGrad.setter
    def InitationsGrad(self, InitationsGrad: int):
        self.__InitationsGrad = InitationsGrad

class shadowrun_BaseMagischePersona(ABC):

    def __init__(self, magie: int):
        self.magie = magie
        
    @property
    def magie(self) -> int:
        return self.__magie

    @magie.setter
    def magie(self, magie: int):
        self.__magie = magie

class AbstraktModifikatoren:

    pass
class shadowrun_MagischeMods(AbstraktModifikatoren):

    pass
class shadowrun_koerpermods(AbstraktModifikatoren):

    pass
class shadowrun_ModifikatorList:

    def __init__(self, name: str, shadowrun_ModifikatorList: set["shadowrun_AbstraktModifikatoren"] = None):
        self.name = name
        self.shadowrun_ModifikatorList = shadowrun_ModifikatorList if shadowrun_ModifikatorList is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shadowrun_ModifikatorList(self):
        return self.__shadowrun_ModifikatorList

    @shadowrun_ModifikatorList.setter
    def shadowrun_ModifikatorList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_ModifikatorList__shadowrun_ModifikatorList", None)
        self.__shadowrun_ModifikatorList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shadowrun_AbstraktModifikatoren"):
                    opp_val = getattr(item, "shadowrun_AbstraktModifikatoren", None)
                    
                    if opp_val == self:
                        setattr(item, "shadowrun_AbstraktModifikatoren", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shadowrun_AbstraktModifikatoren"):
                    opp_val = getattr(item, "shadowrun_AbstraktModifikatoren", None)
                    
                    setattr(item, "shadowrun_AbstraktModifikatoren", self)
                    

class AbstraktFertigkeit:

    pass
class shadowrun_KiAdept(AbstractMagischePaersona):

    pass
class MagischeMods:

    pass
class shadowrun_KiKraft(MagischeMods):

    pass
class shadowrun_Modifizierbar(ABC):

    pass
class shadowrun_EAttribute:

    pass
class shadowrun_AttributModifikatorWert:

    def __init__(self, wert: int, shadowrun_AttributModifikatorWert: "shadowrun_EAttribute" = None, mods: "shadowrun_Modifizierbar" = None, AttributModifikatorWert: "shadowrun_Modifizierbar" = None):
        self.wert = wert
        self.shadowrun_AttributModifikatorWert = shadowrun_AttributModifikatorWert
        self.mods = mods
        self.AttributModifikatorWert = AttributModifikatorWert
        
    @property
    def wert(self) -> int:
        return self.__wert

    @wert.setter
    def wert(self, wert: int):
        self.__wert = wert

    @property
    def mods(self):
        return self.__mods

    @mods.setter
    def mods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AttributModifikatorWert__mods", None)
        self.__mods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Modifizierbar"):
                opp_val = getattr(old_value, "Modifizierbar", None)
                if opp_val == self:
                    setattr(old_value, "Modifizierbar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Modifizierbar"):
                opp_val = getattr(value, "Modifizierbar", None)
                setattr(value, "Modifizierbar", self)

    @property
    def shadowrun_AttributModifikatorWert(self):
        return self.__shadowrun_AttributModifikatorWert

    @shadowrun_AttributModifikatorWert.setter
    def shadowrun_AttributModifikatorWert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AttributModifikatorWert__shadowrun_AttributModifikatorWert", None)
        self.__shadowrun_AttributModifikatorWert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_EAttribute"):
                opp_val = getattr(old_value, "shadowrun_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_EAttribute"):
                opp_val = getattr(value, "shadowrun_EAttribute", None)
                setattr(value, "shadowrun_EAttribute", self)

    @property
    def AttributModifikatorWert(self):
        return self.__AttributModifikatorWert

    @AttributModifikatorWert.setter
    def AttributModifikatorWert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AttributModifikatorWert__AttributModifikatorWert", None)
        self.__AttributModifikatorWert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modifiziertes"):
                opp_val = getattr(old_value, "modifiziertes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modifiziertes"):
                opp_val = getattr(value, "modifiziertes", None)
                if opp_val is None:
                    setattr(value, "modifiziertes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shadowrun_BasicList:

    pass
class shadowrun_GeldWert(ABC):

    def __init__(self, wert: str, strassenIndex: float, verfuegbarkeit: str):
        self.wert = wert
        self.strassenIndex = strassenIndex
        self.verfuegbarkeit = verfuegbarkeit
        
    @property
    def wert(self) -> str:
        return self.__wert

    @wert.setter
    def wert(self, wert: str):
        self.__wert = wert

    @property
    def verfuegbarkeit(self) -> str:
        return self.__verfuegbarkeit

    @verfuegbarkeit.setter
    def verfuegbarkeit(self, verfuegbarkeit: str):
        self.__verfuegbarkeit = verfuegbarkeit

    @property
    def strassenIndex(self) -> float:
        return self.__strassenIndex

    @strassenIndex.setter
    def strassenIndex(self, strassenIndex: float):
        self.__strassenIndex = strassenIndex

class koerpermods:

    pass
class shadowrun_FK:

    pass
class Gegenstand:

    pass
class shadowrun_Behaelter(Gegenstand):

    def __init__(self, kapazitaet: int, shadowrun_Behaelter: set["shadowrun_AbstaktGegenstand"] = None):
        self.kapazitaet = kapazitaet
        self.shadowrun_Behaelter = shadowrun_Behaelter if shadowrun_Behaelter is not None else set()
        
    @property
    def kapazitaet(self) -> int:
        return self.__kapazitaet

    @kapazitaet.setter
    def kapazitaet(self, kapazitaet: int):
        self.__kapazitaet = kapazitaet

    @property
    def shadowrun_Behaelter(self):
        return self.__shadowrun_Behaelter

    @shadowrun_Behaelter.setter
    def shadowrun_Behaelter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Behaelter__shadowrun_Behaelter", None)
        self.__shadowrun_Behaelter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shadowrun_AbstaktGegenstand27"):
                    opp_val = getattr(item, "shadowrun_AbstaktGegenstand27", None)
                    
                    if opp_val == self:
                        setattr(item, "shadowrun_AbstaktGegenstand27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shadowrun_AbstaktGegenstand27"):
                    opp_val = getattr(item, "shadowrun_AbstaktGegenstand27", None)
                    
                    setattr(item, "shadowrun_AbstaktGegenstand27", self)
                    

class NahkampfReichweite:

    pass
class AbstrakteRuestung:

    pass
class shadowrun_Ruestung(AbstrakteRuestung):

    pass
class AbstraktKleidung:

    pass
class shadowrun_AbstrakteRuestung(AbstraktKleidung):

    def __init__(self, ruestungsSchutzBalistisch: int, ruestungsSchutzStoss: int):
        self.ruestungsSchutzBalistisch = ruestungsSchutzBalistisch
        self.ruestungsSchutzStoss = ruestungsSchutzStoss
        
    @property
    def ruestungsSchutzBalistisch(self) -> int:
        return self.__ruestungsSchutzBalistisch

    @ruestungsSchutzBalistisch.setter
    def ruestungsSchutzBalistisch(self, ruestungsSchutzBalistisch: int):
        self.__ruestungsSchutzBalistisch = ruestungsSchutzBalistisch

    @property
    def ruestungsSchutzStoss(self) -> int:
        return self.__ruestungsSchutzStoss

    @ruestungsSchutzStoss.setter
    def ruestungsSchutzStoss(self, ruestungsSchutzStoss: int):
        self.__ruestungsSchutzStoss = ruestungsSchutzStoss

class shadowrun_PersonaKoerper:

    def __init__(self, gesamtZustand: int):
        self.gesamtZustand = gesamtZustand
        
    @property
    def gesamtZustand(self) -> int:
        return self.__gesamtZustand

    @gesamtZustand.setter
    def gesamtZustand(self, gesamtZustand: int):
        self.__gesamtZustand = gesamtZustand

class AbstaktPersona:

    pass
class shadowrun_AbstractMagischePaersona(AbstaktPersona, BaseMagischePersona):

    def __init__(self, magieBase: int):
        self.magieBase = magieBase
        
    @property
    def magieBase(self) -> int:
        return self.__magieBase

    @magieBase.setter
    def magieBase(self, magieBase: int):
        self.__magieBase = magieBase

class shadowrun_Persona(AbstaktPersona):

    pass
class shadowrun_Kleidung(AbstraktKleidung):

    pass
class shadowrun_MunitionsBehealter(Gegenstand):

    pass
class AbstaktFernKampfwaffe:

    pass
class shadowrun_Projektilwaffe(AbstaktFernKampfwaffe):

    pass
class shadowrun_Wurfwaffe(AbstaktFernKampfwaffe):

    pass
class shadowrun_Feuerwaffe(AbstaktFernKampfwaffe):

    def __init__(self, munitionstyp: str, modie: str, kapazitaet: int, shadowrun_Feuerwaffe: "shadowrun_MunitionsBehealter" = None):
        self.munitionstyp = munitionstyp
        self.modie = modie
        self.kapazitaet = kapazitaet
        self.shadowrun_Feuerwaffe = shadowrun_Feuerwaffe
        
    @property
    def modie(self) -> str:
        return self.__modie

    @modie.setter
    def modie(self, modie: str):
        self.__modie = modie

    @property
    def munitionstyp(self) -> str:
        return self.__munitionstyp

    @munitionstyp.setter
    def munitionstyp(self, munitionstyp: str):
        self.__munitionstyp = munitionstyp

    @property
    def kapazitaet(self) -> int:
        return self.__kapazitaet

    @kapazitaet.setter
    def kapazitaet(self, kapazitaet: int):
        self.__kapazitaet = kapazitaet

    @property
    def shadowrun_Feuerwaffe(self):
        return self.__shadowrun_Feuerwaffe

    @shadowrun_Feuerwaffe.setter
    def shadowrun_Feuerwaffe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Feuerwaffe__shadowrun_Feuerwaffe", None)
        self.__shadowrun_Feuerwaffe = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_MunitionsBehealter"):
                opp_val = getattr(old_value, "shadowrun_MunitionsBehealter", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_MunitionsBehealter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_MunitionsBehealter"):
                opp_val = getattr(value, "shadowrun_MunitionsBehealter", None)
                setattr(value, "shadowrun_MunitionsBehealter", self)

class shadowrun_RaumKoordinate:

    pass
class shadowrun_AbstrakRaumKoerper(ABC):

    def __init__(self, shadowrun_AbstrakRaumKoerper: "shadowrun_RaumKoordinate" = None):
        self.shadowrun_AbstrakRaumKoerper = shadowrun_AbstrakRaumKoerper
        
    @property
    def shadowrun_AbstrakRaumKoerper(self):
        return self.__shadowrun_AbstrakRaumKoerper

    @shadowrun_AbstrakRaumKoerper.setter
    def shadowrun_AbstrakRaumKoerper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstrakRaumKoerper__shadowrun_AbstrakRaumKoerper", None)
        self.__shadowrun_AbstrakRaumKoerper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_RaumKoordinate"):
                opp_val = getattr(old_value, "shadowrun_RaumKoordinate", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_RaumKoordinate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_RaumKoordinate"):
                opp_val = getattr(value, "shadowrun_RaumKoordinate", None)
                setattr(value, "shadowrun_RaumKoordinate", self)

    def ProcessWorldTick(self):
        # TODO: Implement ProcessWorldTick method
        pass

class shadowrun_Spezialisierung(AbstraktFertigkeit):

    pass
class shadowrun_Konzentration(AbstraktFertigkeit):

    pass
class shadowrun_Fertigkeit(AbstraktFertigkeit):

    pass
class AbstaktGegenstand:

    pass
class shadowrun_Gegenstand(AbstaktGegenstand):

    pass
class shadowrun_AbstraktKleidung(AbstaktGegenstand):

    def __init__(self, koeperTeil: str, shadowrun_AbstraktKleidung: "shadowrun_AbstaktPersona" = None):
        self.koeperTeil = koeperTeil
        self.shadowrun_AbstraktKleidung = shadowrun_AbstraktKleidung
        
    @property
    def koeperTeil(self) -> str:
        return self.__koeperTeil

    @koeperTeil.setter
    def koeperTeil(self, koeperTeil: str):
        self.__koeperTeil = koeperTeil

    @property
    def shadowrun_AbstraktKleidung(self):
        return self.__shadowrun_AbstraktKleidung

    @shadowrun_AbstraktKleidung.setter
    def shadowrun_AbstraktKleidung(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstraktKleidung__shadowrun_AbstraktKleidung", None)
        self.__shadowrun_AbstraktKleidung = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_AbstaktPersona14"):
                opp_val = getattr(old_value, "shadowrun_AbstaktPersona14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_AbstaktPersona14"):
                opp_val = getattr(value, "shadowrun_AbstaktPersona14", None)
                if opp_val is None:
                    setattr(value, "shadowrun_AbstaktPersona14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shadowrun_Munition(AbstaktGegenstand):

    def __init__(self, power: int, niveau: int, schadensTyp: str, shadowrun_Munition: "shadowrun_Reichweite" = None):
        self.power = power
        self.niveau = niveau
        self.schadensTyp = schadensTyp
        self.shadowrun_Munition = shadowrun_Munition
        
    @property
    def niveau(self) -> int:
        return self.__niveau

    @niveau.setter
    def niveau(self, niveau: int):
        self.__niveau = niveau

    @property
    def schadensTyp(self) -> str:
        return self.__schadensTyp

    @schadensTyp.setter
    def schadensTyp(self, schadensTyp: str):
        self.__schadensTyp = schadensTyp

    @property
    def power(self) -> int:
        return self.__power

    @power.setter
    def power(self, power: int):
        self.__power = power

    @property
    def shadowrun_Munition(self):
        return self.__shadowrun_Munition

    @shadowrun_Munition.setter
    def shadowrun_Munition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Munition__shadowrun_Munition", None)
        self.__shadowrun_Munition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Reichweite72"):
                opp_val = getattr(old_value, "shadowrun_Reichweite72", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_Reichweite72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Reichweite72"):
                opp_val = getattr(value, "shadowrun_Reichweite72", None)
                setattr(value, "shadowrun_Reichweite72", self)

class shadowrun_AbstaktWaffe(AbstaktGegenstand):

    def __init__(self, schadenscode: str, shadowrun_AbstaktWaffe: "shadowrun_Fertigkeit" = None, shadowrun_AbstaktWaffe22: "shadowrun_Konzentration" = None, shadowrun_AbstaktWaffe24: "shadowrun_Spezialisierung" = None):
        self.schadenscode = schadenscode
        self.shadowrun_AbstaktWaffe = shadowrun_AbstaktWaffe
        self.shadowrun_AbstaktWaffe22 = shadowrun_AbstaktWaffe22
        self.shadowrun_AbstaktWaffe24 = shadowrun_AbstaktWaffe24
        
    @property
    def schadenscode(self) -> str:
        return self.__schadenscode

    @schadenscode.setter
    def schadenscode(self, schadenscode: str):
        self.__schadenscode = schadenscode

    @property
    def shadowrun_AbstaktWaffe22(self):
        return self.__shadowrun_AbstaktWaffe22

    @shadowrun_AbstaktWaffe22.setter
    def shadowrun_AbstaktWaffe22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktWaffe__shadowrun_AbstaktWaffe22", None)
        self.__shadowrun_AbstaktWaffe22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Konzentration"):
                opp_val = getattr(old_value, "shadowrun_Konzentration", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_Konzentration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Konzentration"):
                opp_val = getattr(value, "shadowrun_Konzentration", None)
                setattr(value, "shadowrun_Konzentration", self)

    @property
    def shadowrun_AbstaktWaffe(self):
        return self.__shadowrun_AbstaktWaffe

    @shadowrun_AbstaktWaffe.setter
    def shadowrun_AbstaktWaffe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktWaffe__shadowrun_AbstaktWaffe", None)
        self.__shadowrun_AbstaktWaffe = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Fertigkeit"):
                opp_val = getattr(old_value, "shadowrun_Fertigkeit", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_Fertigkeit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Fertigkeit"):
                opp_val = getattr(value, "shadowrun_Fertigkeit", None)
                setattr(value, "shadowrun_Fertigkeit", self)

    @property
    def shadowrun_AbstaktWaffe24(self):
        return self.__shadowrun_AbstaktWaffe24

    @shadowrun_AbstaktWaffe24.setter
    def shadowrun_AbstaktWaffe24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktWaffe__shadowrun_AbstaktWaffe24", None)
        self.__shadowrun_AbstaktWaffe24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Spezialisierung"):
                opp_val = getattr(old_value, "shadowrun_Spezialisierung", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_Spezialisierung", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Spezialisierung"):
                opp_val = getattr(value, "shadowrun_Spezialisierung", None)
                setattr(value, "shadowrun_Spezialisierung", self)

class Modifizierbar:

    pass
class Quelle:

    pass
class Bemerkbar:

    pass
class Legalitaet:

    pass
class Beschreibbar:

    pass
class shadowrun_Spezies(Beschreibbar, Modifizierbar):

    def __init__(self, KonsitutionMax: int, StaerkeMax: int, SchnelligkeitMax: int, InteligenzMax: int, CharismaMax: int, WillenskraftMax: int, shadowrun_Spezies: "shadowrun_AbstaktPersona" = None):
        self.KonsitutionMax = KonsitutionMax
        self.StaerkeMax = StaerkeMax
        self.SchnelligkeitMax = SchnelligkeitMax
        self.InteligenzMax = InteligenzMax
        self.CharismaMax = CharismaMax
        self.WillenskraftMax = WillenskraftMax
        self.shadowrun_Spezies = shadowrun_Spezies
        
    @property
    def KonsitutionMax(self) -> int:
        return self.__KonsitutionMax

    @KonsitutionMax.setter
    def KonsitutionMax(self, KonsitutionMax: int):
        self.__KonsitutionMax = KonsitutionMax

    @property
    def WillenskraftMax(self) -> int:
        return self.__WillenskraftMax

    @WillenskraftMax.setter
    def WillenskraftMax(self, WillenskraftMax: int):
        self.__WillenskraftMax = WillenskraftMax

    @property
    def InteligenzMax(self) -> int:
        return self.__InteligenzMax

    @InteligenzMax.setter
    def InteligenzMax(self, InteligenzMax: int):
        self.__InteligenzMax = InteligenzMax

    @property
    def SchnelligkeitMax(self) -> int:
        return self.__SchnelligkeitMax

    @SchnelligkeitMax.setter
    def SchnelligkeitMax(self, SchnelligkeitMax: int):
        self.__SchnelligkeitMax = SchnelligkeitMax

    @property
    def CharismaMax(self) -> int:
        return self.__CharismaMax

    @CharismaMax.setter
    def CharismaMax(self, CharismaMax: int):
        self.__CharismaMax = CharismaMax

    @property
    def StaerkeMax(self) -> int:
        return self.__StaerkeMax

    @StaerkeMax.setter
    def StaerkeMax(self, StaerkeMax: int):
        self.__StaerkeMax = StaerkeMax

    @property
    def shadowrun_Spezies(self):
        return self.__shadowrun_Spezies

    @shadowrun_Spezies.setter
    def shadowrun_Spezies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Spezies__shadowrun_Spezies", None)
        self.__shadowrun_Spezies = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_AbstaktPersona19"):
                opp_val = getattr(old_value, "shadowrun_AbstaktPersona19", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_AbstaktPersona19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_AbstaktPersona19"):
                opp_val = getattr(value, "shadowrun_AbstaktPersona19", None)
                setattr(value, "shadowrun_AbstaktPersona19", self)

class shadowrun_Placement(Beschreibbar):

    def __init__(self, shadowrun_Placement: set["shadowrun_PersonaGruppe"] = None, shadowrun_Placement34: "shadowrun_Script" = None):
        self.shadowrun_Placement = shadowrun_Placement if shadowrun_Placement is not None else set()
        self.shadowrun_Placement34 = shadowrun_Placement34
        
    @property
    def shadowrun_Placement(self):
        return self.__shadowrun_Placement

    @shadowrun_Placement.setter
    def shadowrun_Placement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Placement__shadowrun_Placement", None)
        self.__shadowrun_Placement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shadowrun_PersonaGruppe32"):
                    opp_val = getattr(item, "shadowrun_PersonaGruppe32", None)
                    
                    if opp_val == self:
                        setattr(item, "shadowrun_PersonaGruppe32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shadowrun_PersonaGruppe32"):
                    opp_val = getattr(item, "shadowrun_PersonaGruppe32", None)
                    
                    setattr(item, "shadowrun_PersonaGruppe32", self)
                    

    @property
    def shadowrun_Placement34(self):
        return self.__shadowrun_Placement34

    @shadowrun_Placement34.setter
    def shadowrun_Placement34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Placement__shadowrun_Placement34", None)
        self.__shadowrun_Placement34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Script"):
                opp_val = getattr(old_value, "shadowrun_Script", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Script"):
                opp_val = getattr(value, "shadowrun_Script", None)
                if opp_val is None:
                    setattr(value, "shadowrun_Script", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getGruppeByName(self, ItemName: str):
        # TODO: Implement getGruppeByName method
        pass

class shadowrun_PersonaGruppe(Beschreibbar):

    def __init__(self, shadowrun_PersonaGruppe: set["shadowrun_AbstaktPersona"] = None, shadowrun_PersonaGruppe32: "shadowrun_Placement" = None, shadowrun_PersonaGruppe37: "shadowrun_Script" = None):
        self.shadowrun_PersonaGruppe = shadowrun_PersonaGruppe if shadowrun_PersonaGruppe is not None else set()
        self.shadowrun_PersonaGruppe32 = shadowrun_PersonaGruppe32
        self.shadowrun_PersonaGruppe37 = shadowrun_PersonaGruppe37
        
    @property
    def shadowrun_PersonaGruppe32(self):
        return self.__shadowrun_PersonaGruppe32

    @shadowrun_PersonaGruppe32.setter
    def shadowrun_PersonaGruppe32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_PersonaGruppe__shadowrun_PersonaGruppe32", None)
        self.__shadowrun_PersonaGruppe32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Placement"):
                opp_val = getattr(old_value, "shadowrun_Placement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Placement"):
                opp_val = getattr(value, "shadowrun_Placement", None)
                if opp_val is None:
                    setattr(value, "shadowrun_Placement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shadowrun_PersonaGruppe(self):
        return self.__shadowrun_PersonaGruppe

    @shadowrun_PersonaGruppe.setter
    def shadowrun_PersonaGruppe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_PersonaGruppe__shadowrun_PersonaGruppe", None)
        self.__shadowrun_PersonaGruppe = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shadowrun_AbstaktPersona30"):
                    opp_val = getattr(item, "shadowrun_AbstaktPersona30", None)
                    
                    if opp_val == self:
                        setattr(item, "shadowrun_AbstaktPersona30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shadowrun_AbstaktPersona30"):
                    opp_val = getattr(item, "shadowrun_AbstaktPersona30", None)
                    
                    setattr(item, "shadowrun_AbstaktPersona30", self)
                    

    @property
    def shadowrun_PersonaGruppe37(self):
        return self.__shadowrun_PersonaGruppe37

    @shadowrun_PersonaGruppe37.setter
    def shadowrun_PersonaGruppe37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_PersonaGruppe__shadowrun_PersonaGruppe37", None)
        self.__shadowrun_PersonaGruppe37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Script36"):
                opp_val = getattr(old_value, "shadowrun_Script36", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_Script36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Script36"):
                opp_val = getattr(value, "shadowrun_Script36", None)
                setattr(value, "shadowrun_Script36", self)

    def getPersonaByName(self, ItemName: str):
        # TODO: Implement getPersonaByName method
        pass

    def getPersonaCount(self) -> int:
        # TODO: Implement getPersonaCount method
        pass

    def getPersonas(self, Index: int):
        # TODO: Implement getPersonas method
        pass

class shadowrun_ShrList(Beschreibbar):

    pass
class shadowrun_Zauber(Beschreibbar):

    def __init__(self, art: str, reichweite: str, Mindestwurf: str, Schaden: str, Dauer: str, Enzug: str, shadowrun_Zauber: "shadowrun_PersonaZauber" = None):
        self.art = art
        self.reichweite = reichweite
        self.Mindestwurf = Mindestwurf
        self.Schaden = Schaden
        self.Dauer = Dauer
        self.Enzug = Enzug
        self.shadowrun_Zauber = shadowrun_Zauber
        
    @property
    def art(self) -> str:
        return self.__art

    @art.setter
    def art(self, art: str):
        self.__art = art

    @property
    def Schaden(self) -> str:
        return self.__Schaden

    @Schaden.setter
    def Schaden(self, Schaden: str):
        self.__Schaden = Schaden

    @property
    def Enzug(self) -> str:
        return self.__Enzug

    @Enzug.setter
    def Enzug(self, Enzug: str):
        self.__Enzug = Enzug

    @property
    def reichweite(self) -> str:
        return self.__reichweite

    @reichweite.setter
    def reichweite(self, reichweite: str):
        self.__reichweite = reichweite

    @property
    def Mindestwurf(self) -> str:
        return self.__Mindestwurf

    @Mindestwurf.setter
    def Mindestwurf(self, Mindestwurf: str):
        self.__Mindestwurf = Mindestwurf

    @property
    def Dauer(self) -> str:
        return self.__Dauer

    @Dauer.setter
    def Dauer(self, Dauer: str):
        self.__Dauer = Dauer

    @property
    def shadowrun_Zauber(self):
        return self.__shadowrun_Zauber

    @shadowrun_Zauber.setter
    def shadowrun_Zauber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Zauber__shadowrun_Zauber", None)
        self.__shadowrun_Zauber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_PersonaZauber62"):
                opp_val = getattr(old_value, "shadowrun_PersonaZauber62", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_PersonaZauber62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_PersonaZauber62"):
                opp_val = getattr(value, "shadowrun_PersonaZauber62", None)
                setattr(value, "shadowrun_PersonaZauber62", self)

class shadowrun_AbstraktModifikatoren(Beschreibbar, Quelle, Modifizierbar):

    pass
class shadowrun_Script(Beschreibbar):

    def __init__(self, shadowrun_Script: set["shadowrun_Placement"] = None, shadowrun_Script36: "shadowrun_PersonaGruppe" = None):
        self.shadowrun_Script = shadowrun_Script if shadowrun_Script is not None else set()
        self.shadowrun_Script36 = shadowrun_Script36
        
    @property
    def shadowrun_Script36(self):
        return self.__shadowrun_Script36

    @shadowrun_Script36.setter
    def shadowrun_Script36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Script__shadowrun_Script36", None)
        self.__shadowrun_Script36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_PersonaGruppe37"):
                opp_val = getattr(old_value, "shadowrun_PersonaGruppe37", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_PersonaGruppe37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_PersonaGruppe37"):
                opp_val = getattr(value, "shadowrun_PersonaGruppe37", None)
                setattr(value, "shadowrun_PersonaGruppe37", self)

    @property
    def shadowrun_Script(self):
        return self.__shadowrun_Script

    @shadowrun_Script.setter
    def shadowrun_Script(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Script__shadowrun_Script", None)
        self.__shadowrun_Script = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shadowrun_Placement34"):
                    opp_val = getattr(item, "shadowrun_Placement34", None)
                    
                    if opp_val == self:
                        setattr(item, "shadowrun_Placement34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shadowrun_Placement34"):
                    opp_val = getattr(item, "shadowrun_Placement34", None)
                    
                    setattr(item, "shadowrun_Placement34", self)
                    

    def getPlacementCount(self) -> int:
        # TODO: Implement getPlacementCount method
        pass

    def getPlacements(self, Index: int):
        # TODO: Implement getPlacements method
        pass

    def getPlacementByName(self, ItemName: str):
        # TODO: Implement getPlacementByName method
        pass

class shadowrun_Totem(Beschreibbar):

    pass
class shadowrun_SourceBook(Beschreibbar):

    def __init__(self, startShrTime: str, endShrTime: str, shadowrun_SourceBook: "shadowrun_Quelle" = None):
        self.startShrTime = startShrTime
        self.endShrTime = endShrTime
        self.shadowrun_SourceBook = shadowrun_SourceBook
        
    @property
    def endShrTime(self) -> str:
        return self.__endShrTime

    @endShrTime.setter
    def endShrTime(self, endShrTime: str):
        self.__endShrTime = endShrTime

    @property
    def startShrTime(self) -> str:
        return self.__startShrTime

    @startShrTime.setter
    def startShrTime(self, startShrTime: str):
        self.__startShrTime = startShrTime

    @property
    def shadowrun_SourceBook(self):
        return self.__shadowrun_SourceBook

    @shadowrun_SourceBook.setter
    def shadowrun_SourceBook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_SourceBook__shadowrun_SourceBook", None)
        self.__shadowrun_SourceBook = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Quelle"):
                opp_val = getattr(old_value, "shadowrun_Quelle", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_Quelle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Quelle"):
                opp_val = getattr(value, "shadowrun_Quelle", None)
                setattr(value, "shadowrun_Quelle", self)

class GeldWert:

    pass
class shadowrun_BioWare(GeldWert, koerpermods):

    pass
class FK:

    pass
class shadowrun_AbstraktFertigkeit(FK, Beschreibbar):

    pass
class shadowrun_FertigkeitsGruppe(FK, Beschreibbar):

    pass
class shadowrun_AbstaktGegenstand(Legalitaet, FK, GeldWert, Modifizierbar, Beschreibbar, Quelle, Bemerkbar):

    def __init__(self, tragbar: str, gewicht: float, raumKapazitaet: int, verbraucht: bool, inBenutzung: bool, shadowrun_AbstaktGegenstand17: "shadowrun_AbstaktPersona" = None, shadowrun_AbstaktGegenstand: "shadowrun_AbstaktPersona" = None, shadowrun_AbstaktGegenstand9: "shadowrun_AbstaktPersona" = None, shadowrun_AbstaktGegenstand12: "shadowrun_AbstaktPersona" = None, shadowrun_AbstaktGegenstand27: "shadowrun_Behaelter" = None, shadowrun_AbstaktGegenstand57: "shadowrun_GengenstandListe" = None, shadowrun_AbstaktGegenstand67: "shadowrun_WarenListe" = None):
        self.tragbar = tragbar
        self.gewicht = gewicht
        self.raumKapazitaet = raumKapazitaet
        self.verbraucht = verbraucht
        self.inBenutzung = inBenutzung
        self.shadowrun_AbstaktGegenstand17 = shadowrun_AbstaktGegenstand17
        self.shadowrun_AbstaktGegenstand = shadowrun_AbstaktGegenstand
        self.shadowrun_AbstaktGegenstand9 = shadowrun_AbstaktGegenstand9
        self.shadowrun_AbstaktGegenstand12 = shadowrun_AbstaktGegenstand12
        self.shadowrun_AbstaktGegenstand27 = shadowrun_AbstaktGegenstand27
        self.shadowrun_AbstaktGegenstand57 = shadowrun_AbstaktGegenstand57
        self.shadowrun_AbstaktGegenstand67 = shadowrun_AbstaktGegenstand67
        
    @property
    def tragbar(self) -> str:
        return self.__tragbar

    @tragbar.setter
    def tragbar(self, tragbar: str):
        self.__tragbar = tragbar

    @property
    def gewicht(self) -> float:
        return self.__gewicht

    @gewicht.setter
    def gewicht(self, gewicht: float):
        self.__gewicht = gewicht

    @property
    def raumKapazitaet(self) -> int:
        return self.__raumKapazitaet

    @raumKapazitaet.setter
    def raumKapazitaet(self, raumKapazitaet: int):
        self.__raumKapazitaet = raumKapazitaet

    @property
    def inBenutzung(self) -> bool:
        return self.__inBenutzung

    @inBenutzung.setter
    def inBenutzung(self, inBenutzung: bool):
        self.__inBenutzung = inBenutzung

    @property
    def verbraucht(self) -> bool:
        return self.__verbraucht

    @verbraucht.setter
    def verbraucht(self, verbraucht: bool):
        self.__verbraucht = verbraucht

    @property
    def shadowrun_AbstaktGegenstand67(self):
        return self.__shadowrun_AbstaktGegenstand67

    @shadowrun_AbstaktGegenstand67.setter
    def shadowrun_AbstaktGegenstand67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktGegenstand__shadowrun_AbstaktGegenstand67", None)
        self.__shadowrun_AbstaktGegenstand67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_WarenListe"):
                opp_val = getattr(old_value, "shadowrun_WarenListe", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_WarenListe"):
                opp_val = getattr(value, "shadowrun_WarenListe", None)
                if opp_val is None:
                    setattr(value, "shadowrun_WarenListe", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shadowrun_AbstaktGegenstand9(self):
        return self.__shadowrun_AbstaktGegenstand9

    @shadowrun_AbstaktGegenstand9.setter
    def shadowrun_AbstaktGegenstand9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktGegenstand__shadowrun_AbstaktGegenstand9", None)
        self.__shadowrun_AbstaktGegenstand9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_AbstaktPersona8"):
                opp_val = getattr(old_value, "shadowrun_AbstaktPersona8", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_AbstaktPersona8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_AbstaktPersona8"):
                opp_val = getattr(value, "shadowrun_AbstaktPersona8", None)
                setattr(value, "shadowrun_AbstaktPersona8", self)

    @property
    def shadowrun_AbstaktGegenstand27(self):
        return self.__shadowrun_AbstaktGegenstand27

    @shadowrun_AbstaktGegenstand27.setter
    def shadowrun_AbstaktGegenstand27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktGegenstand__shadowrun_AbstaktGegenstand27", None)
        self.__shadowrun_AbstaktGegenstand27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Behaelter"):
                opp_val = getattr(old_value, "shadowrun_Behaelter", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Behaelter"):
                opp_val = getattr(value, "shadowrun_Behaelter", None)
                if opp_val is None:
                    setattr(value, "shadowrun_Behaelter", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shadowrun_AbstaktGegenstand57(self):
        return self.__shadowrun_AbstaktGegenstand57

    @shadowrun_AbstaktGegenstand57.setter
    def shadowrun_AbstaktGegenstand57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktGegenstand__shadowrun_AbstaktGegenstand57", None)
        self.__shadowrun_AbstaktGegenstand57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_GengenstandListe"):
                opp_val = getattr(old_value, "shadowrun_GengenstandListe", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_GengenstandListe"):
                opp_val = getattr(value, "shadowrun_GengenstandListe", None)
                if opp_val is None:
                    setattr(value, "shadowrun_GengenstandListe", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shadowrun_AbstaktGegenstand(self):
        return self.__shadowrun_AbstaktGegenstand

    @shadowrun_AbstaktGegenstand.setter
    def shadowrun_AbstaktGegenstand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktGegenstand__shadowrun_AbstaktGegenstand", None)
        self.__shadowrun_AbstaktGegenstand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_AbstaktPersona6"):
                opp_val = getattr(old_value, "shadowrun_AbstaktPersona6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_AbstaktPersona6"):
                opp_val = getattr(value, "shadowrun_AbstaktPersona6", None)
                if opp_val is None:
                    setattr(value, "shadowrun_AbstaktPersona6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shadowrun_AbstaktGegenstand12(self):
        return self.__shadowrun_AbstaktGegenstand12

    @shadowrun_AbstaktGegenstand12.setter
    def shadowrun_AbstaktGegenstand12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktGegenstand__shadowrun_AbstaktGegenstand12", None)
        self.__shadowrun_AbstaktGegenstand12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_AbstaktPersona11"):
                opp_val = getattr(old_value, "shadowrun_AbstaktPersona11", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_AbstaktPersona11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_AbstaktPersona11"):
                opp_val = getattr(value, "shadowrun_AbstaktPersona11", None)
                setattr(value, "shadowrun_AbstaktPersona11", self)

    @property
    def shadowrun_AbstaktGegenstand17(self):
        return self.__shadowrun_AbstaktGegenstand17

    @shadowrun_AbstaktGegenstand17.setter
    def shadowrun_AbstaktGegenstand17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktGegenstand__shadowrun_AbstaktGegenstand17", None)
        self.__shadowrun_AbstaktGegenstand17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_AbstaktPersona16"):
                opp_val = getattr(old_value, "shadowrun_AbstaktPersona16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_AbstaktPersona16"):
                opp_val = getattr(value, "shadowrun_AbstaktPersona16", None)
                if opp_val is None:
                    setattr(value, "shadowrun_AbstaktPersona16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def Benutze(self):
        # TODO: Implement Benutze method
        pass

    def ErzeugePersonaHandlung(self):
        # TODO: Implement ErzeugePersonaHandlung method
        pass

class shadowrun_Reichweite(Beschreibbar):

    def __init__(self, reichweiteExtrem: int, reichweiteExtrem1: int, reichweiteKurz: int, reichweiteKurz1: int, reichweiteMittel: int, reichweiteMittel1: int, reichweiteWeit: int, reichweiteWeit1: int, shadowrun_Reichweite: "shadowrun_AbstaktFernKampfwaffe" = None, shadowrun_Reichweite59: "shadowrun_Reichweiten" = None, shadowrun_Reichweite72: "shadowrun_Munition" = None):
        self.reichweiteExtrem = reichweiteExtrem
        self.reichweiteExtrem1 = reichweiteExtrem1
        self.reichweiteKurz = reichweiteKurz
        self.reichweiteKurz1 = reichweiteKurz1
        self.reichweiteMittel = reichweiteMittel
        self.reichweiteMittel1 = reichweiteMittel1
        self.reichweiteWeit = reichweiteWeit
        self.reichweiteWeit1 = reichweiteWeit1
        self.shadowrun_Reichweite = shadowrun_Reichweite
        self.shadowrun_Reichweite59 = shadowrun_Reichweite59
        self.shadowrun_Reichweite72 = shadowrun_Reichweite72
        
    @property
    def reichweiteKurz1(self) -> int:
        return self.__reichweiteKurz1

    @reichweiteKurz1.setter
    def reichweiteKurz1(self, reichweiteKurz1: int):
        self.__reichweiteKurz1 = reichweiteKurz1

    @property
    def reichweiteExtrem1(self) -> int:
        return self.__reichweiteExtrem1

    @reichweiteExtrem1.setter
    def reichweiteExtrem1(self, reichweiteExtrem1: int):
        self.__reichweiteExtrem1 = reichweiteExtrem1

    @property
    def reichweiteWeit(self) -> int:
        return self.__reichweiteWeit

    @reichweiteWeit.setter
    def reichweiteWeit(self, reichweiteWeit: int):
        self.__reichweiteWeit = reichweiteWeit

    @property
    def reichweiteMittel1(self) -> int:
        return self.__reichweiteMittel1

    @reichweiteMittel1.setter
    def reichweiteMittel1(self, reichweiteMittel1: int):
        self.__reichweiteMittel1 = reichweiteMittel1

    @property
    def reichweiteMittel(self) -> int:
        return self.__reichweiteMittel

    @reichweiteMittel.setter
    def reichweiteMittel(self, reichweiteMittel: int):
        self.__reichweiteMittel = reichweiteMittel

    @property
    def reichweiteExtrem(self) -> int:
        return self.__reichweiteExtrem

    @reichweiteExtrem.setter
    def reichweiteExtrem(self, reichweiteExtrem: int):
        self.__reichweiteExtrem = reichweiteExtrem

    @property
    def reichweiteWeit1(self) -> int:
        return self.__reichweiteWeit1

    @reichweiteWeit1.setter
    def reichweiteWeit1(self, reichweiteWeit1: int):
        self.__reichweiteWeit1 = reichweiteWeit1

    @property
    def reichweiteKurz(self) -> int:
        return self.__reichweiteKurz

    @reichweiteKurz.setter
    def reichweiteKurz(self, reichweiteKurz: int):
        self.__reichweiteKurz = reichweiteKurz

    @property
    def shadowrun_Reichweite59(self):
        return self.__shadowrun_Reichweite59

    @shadowrun_Reichweite59.setter
    def shadowrun_Reichweite59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Reichweite__shadowrun_Reichweite59", None)
        self.__shadowrun_Reichweite59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Reichweiten"):
                opp_val = getattr(old_value, "shadowrun_Reichweiten", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Reichweiten"):
                opp_val = getattr(value, "shadowrun_Reichweiten", None)
                if opp_val is None:
                    setattr(value, "shadowrun_Reichweiten", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shadowrun_Reichweite(self):
        return self.__shadowrun_Reichweite

    @shadowrun_Reichweite.setter
    def shadowrun_Reichweite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Reichweite__shadowrun_Reichweite", None)
        self.__shadowrun_Reichweite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_AbstaktFernKampfwaffe"):
                opp_val = getattr(old_value, "shadowrun_AbstaktFernKampfwaffe", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_AbstaktFernKampfwaffe", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_AbstaktFernKampfwaffe"):
                opp_val = getattr(value, "shadowrun_AbstaktFernKampfwaffe", None)
                setattr(value, "shadowrun_AbstaktFernKampfwaffe", self)

    @property
    def shadowrun_Reichweite72(self):
        return self.__shadowrun_Reichweite72

    @shadowrun_Reichweite72.setter
    def shadowrun_Reichweite72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_Reichweite__shadowrun_Reichweite72", None)
        self.__shadowrun_Reichweite72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Munition"):
                opp_val = getattr(old_value, "shadowrun_Munition", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_Munition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Munition"):
                opp_val = getattr(value, "shadowrun_Munition", None)
                setattr(value, "shadowrun_Munition", self)

class shadowrun_Cyberware(GeldWert, koerpermods):

    pass
class shadowrun_PersonaFertigkeit:

    def __init__(self, stufe: int, shadowrun_PersonaFertigkeit: "shadowrun_AbstaktPersona" = None, shadowrun_PersonaFertigkeit50: "shadowrun_AbstraktFertigkeit" = None):
        self.stufe = stufe
        self.shadowrun_PersonaFertigkeit = shadowrun_PersonaFertigkeit
        self.shadowrun_PersonaFertigkeit50 = shadowrun_PersonaFertigkeit50
        
    @property
    def stufe(self) -> int:
        return self.__stufe

    @stufe.setter
    def stufe(self, stufe: int):
        self.__stufe = stufe

    @property
    def shadowrun_PersonaFertigkeit50(self):
        return self.__shadowrun_PersonaFertigkeit50

    @shadowrun_PersonaFertigkeit50.setter
    def shadowrun_PersonaFertigkeit50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_PersonaFertigkeit__shadowrun_PersonaFertigkeit50", None)
        self.__shadowrun_PersonaFertigkeit50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_AbstraktFertigkeit"):
                opp_val = getattr(old_value, "shadowrun_AbstraktFertigkeit", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_AbstraktFertigkeit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_AbstraktFertigkeit"):
                opp_val = getattr(value, "shadowrun_AbstraktFertigkeit", None)
                setattr(value, "shadowrun_AbstraktFertigkeit", self)

    @property
    def shadowrun_PersonaFertigkeit(self):
        return self.__shadowrun_PersonaFertigkeit

    @shadowrun_PersonaFertigkeit.setter
    def shadowrun_PersonaFertigkeit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_PersonaFertigkeit__shadowrun_PersonaFertigkeit", None)
        self.__shadowrun_PersonaFertigkeit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_AbstaktPersona"):
                opp_val = getattr(old_value, "shadowrun_AbstaktPersona", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_AbstaktPersona"):
                opp_val = getattr(value, "shadowrun_AbstaktPersona", None)
                if opp_val is None:
                    setattr(value, "shadowrun_AbstaktPersona", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GeistigeAttribute:

    pass
class BerechneteAttribute:

    pass
class KoerperlicheAtribute:

    pass
class BodyIndex:

    pass
class Essenz:

    pass
class shadowrun_AbstaktPersona(BerechneteAttribute, Essenz, Beschreibbar, GeistigeAttribute, BodyIndex, KoerperlicheAtribute):

    def __init__(self, KonsitutionBase: int, StaerkeBase: int, SchnelligkeitBase: int, InteligenzBase: int, CharismaBase: int, WillenskraftBase: int, ReaktionBase: int, ReaktionWBase: int, KampfpoolBase: int, EssenzBase: int, eigenGewicht: int, modsetter: str, shadowrun_AbstaktPersona: set["shadowrun_PersonaFertigkeit"] = None, persona: set["shadowrun_Cyberware"] = None, shadowrun_AbstaktPersona16: set["shadowrun_AbstaktGegenstand"] = None, shadowrun_AbstaktPersona19: "shadowrun_Spezies" = None, persona4: set["shadowrun_BioWare"] = None, shadowrun_AbstaktPersona6: set["shadowrun_AbstaktGegenstand"] = None, shadowrun_AbstaktPersona8: "shadowrun_AbstaktGegenstand" = None, shadowrun_AbstaktPersona11: "shadowrun_AbstaktGegenstand" = None, shadowrun_AbstaktPersona14: set["shadowrun_AbstraktKleidung"] = None, shadowrun_AbstaktPersona30: "shadowrun_PersonaGruppe" = None, AbstaktPersona: "shadowrun_Cyberware" = None, AbstaktPersona52: "shadowrun_BioWare" = None):
        self.KonsitutionBase = KonsitutionBase
        self.StaerkeBase = StaerkeBase
        self.SchnelligkeitBase = SchnelligkeitBase
        self.InteligenzBase = InteligenzBase
        self.CharismaBase = CharismaBase
        self.WillenskraftBase = WillenskraftBase
        self.ReaktionBase = ReaktionBase
        self.ReaktionWBase = ReaktionWBase
        self.KampfpoolBase = KampfpoolBase
        self.EssenzBase = EssenzBase
        self.eigenGewicht = eigenGewicht
        self.modsetter = modsetter
        self.shadowrun_AbstaktPersona = shadowrun_AbstaktPersona if shadowrun_AbstaktPersona is not None else set()
        self.persona = persona if persona is not None else set()
        self.shadowrun_AbstaktPersona16 = shadowrun_AbstaktPersona16 if shadowrun_AbstaktPersona16 is not None else set()
        self.shadowrun_AbstaktPersona19 = shadowrun_AbstaktPersona19
        self.persona4 = persona4 if persona4 is not None else set()
        self.shadowrun_AbstaktPersona6 = shadowrun_AbstaktPersona6 if shadowrun_AbstaktPersona6 is not None else set()
        self.shadowrun_AbstaktPersona8 = shadowrun_AbstaktPersona8
        self.shadowrun_AbstaktPersona11 = shadowrun_AbstaktPersona11
        self.shadowrun_AbstaktPersona14 = shadowrun_AbstaktPersona14 if shadowrun_AbstaktPersona14 is not None else set()
        self.shadowrun_AbstaktPersona30 = shadowrun_AbstaktPersona30
        self.AbstaktPersona = AbstaktPersona
        self.AbstaktPersona52 = AbstaktPersona52
        
    @property
    def KonsitutionBase(self) -> int:
        return self.__KonsitutionBase

    @KonsitutionBase.setter
    def KonsitutionBase(self, KonsitutionBase: int):
        self.__KonsitutionBase = KonsitutionBase

    @property
    def WillenskraftBase(self) -> int:
        return self.__WillenskraftBase

    @WillenskraftBase.setter
    def WillenskraftBase(self, WillenskraftBase: int):
        self.__WillenskraftBase = WillenskraftBase

    @property
    def EssenzBase(self) -> int:
        return self.__EssenzBase

    @EssenzBase.setter
    def EssenzBase(self, EssenzBase: int):
        self.__EssenzBase = EssenzBase

    @property
    def StaerkeBase(self) -> int:
        return self.__StaerkeBase

    @StaerkeBase.setter
    def StaerkeBase(self, StaerkeBase: int):
        self.__StaerkeBase = StaerkeBase

    @property
    def CharismaBase(self) -> int:
        return self.__CharismaBase

    @CharismaBase.setter
    def CharismaBase(self, CharismaBase: int):
        self.__CharismaBase = CharismaBase

    @property
    def ReaktionBase(self) -> int:
        return self.__ReaktionBase

    @ReaktionBase.setter
    def ReaktionBase(self, ReaktionBase: int):
        self.__ReaktionBase = ReaktionBase

    @property
    def KampfpoolBase(self) -> int:
        return self.__KampfpoolBase

    @KampfpoolBase.setter
    def KampfpoolBase(self, KampfpoolBase: int):
        self.__KampfpoolBase = KampfpoolBase

    @property
    def eigenGewicht(self) -> int:
        return self.__eigenGewicht

    @eigenGewicht.setter
    def eigenGewicht(self, eigenGewicht: int):
        self.__eigenGewicht = eigenGewicht

    @property
    def modsetter(self) -> str:
        return self.__modsetter

    @modsetter.setter
    def modsetter(self, modsetter: str):
        self.__modsetter = modsetter

    @property
    def SchnelligkeitBase(self) -> int:
        return self.__SchnelligkeitBase

    @SchnelligkeitBase.setter
    def SchnelligkeitBase(self, SchnelligkeitBase: int):
        self.__SchnelligkeitBase = SchnelligkeitBase

    @property
    def InteligenzBase(self) -> int:
        return self.__InteligenzBase

    @InteligenzBase.setter
    def InteligenzBase(self, InteligenzBase: int):
        self.__InteligenzBase = InteligenzBase

    @property
    def ReaktionWBase(self) -> int:
        return self.__ReaktionWBase

    @ReaktionWBase.setter
    def ReaktionWBase(self, ReaktionWBase: int):
        self.__ReaktionWBase = ReaktionWBase

    @property
    def shadowrun_AbstaktPersona30(self):
        return self.__shadowrun_AbstaktPersona30

    @shadowrun_AbstaktPersona30.setter
    def shadowrun_AbstaktPersona30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktPersona__shadowrun_AbstaktPersona30", None)
        self.__shadowrun_AbstaktPersona30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_PersonaGruppe"):
                opp_val = getattr(old_value, "shadowrun_PersonaGruppe", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_PersonaGruppe"):
                opp_val = getattr(value, "shadowrun_PersonaGruppe", None)
                if opp_val is None:
                    setattr(value, "shadowrun_PersonaGruppe", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shadowrun_AbstaktPersona8(self):
        return self.__shadowrun_AbstaktPersona8

    @shadowrun_AbstaktPersona8.setter
    def shadowrun_AbstaktPersona8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktPersona__shadowrun_AbstaktPersona8", None)
        self.__shadowrun_AbstaktPersona8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_AbstaktGegenstand9"):
                opp_val = getattr(old_value, "shadowrun_AbstaktGegenstand9", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_AbstaktGegenstand9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_AbstaktGegenstand9"):
                opp_val = getattr(value, "shadowrun_AbstaktGegenstand9", None)
                setattr(value, "shadowrun_AbstaktGegenstand9", self)

    @property
    def AbstaktPersona52(self):
        return self.__AbstaktPersona52

    @AbstaktPersona52.setter
    def AbstaktPersona52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktPersona__AbstaktPersona52", None)
        self.__AbstaktPersona52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bioware"):
                opp_val = getattr(old_value, "bioware", None)
                if opp_val == self:
                    setattr(old_value, "bioware", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bioware"):
                opp_val = getattr(value, "bioware", None)
                setattr(value, "bioware", self)

    @property
    def AbstaktPersona(self):
        return self.__AbstaktPersona

    @AbstaktPersona.setter
    def AbstaktPersona(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktPersona__AbstaktPersona", None)
        self.__AbstaktPersona = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cyberware"):
                opp_val = getattr(old_value, "cyberware", None)
                if opp_val == self:
                    setattr(old_value, "cyberware", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cyberware"):
                opp_val = getattr(value, "cyberware", None)
                setattr(value, "cyberware", self)

    @property
    def persona(self):
        return self.__persona

    @persona.setter
    def persona(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktPersona__persona", None)
        self.__persona = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cyberware"):
                    opp_val = getattr(item, "Cyberware", None)
                    
                    if opp_val == self:
                        setattr(item, "Cyberware", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cyberware"):
                    opp_val = getattr(item, "Cyberware", None)
                    
                    setattr(item, "Cyberware", self)
                    

    @property
    def shadowrun_AbstaktPersona6(self):
        return self.__shadowrun_AbstaktPersona6

    @shadowrun_AbstaktPersona6.setter
    def shadowrun_AbstaktPersona6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktPersona__shadowrun_AbstaktPersona6", None)
        self.__shadowrun_AbstaktPersona6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shadowrun_AbstaktGegenstand"):
                    opp_val = getattr(item, "shadowrun_AbstaktGegenstand", None)
                    
                    if opp_val == self:
                        setattr(item, "shadowrun_AbstaktGegenstand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shadowrun_AbstaktGegenstand"):
                    opp_val = getattr(item, "shadowrun_AbstaktGegenstand", None)
                    
                    setattr(item, "shadowrun_AbstaktGegenstand", self)
                    

    @property
    def shadowrun_AbstaktPersona11(self):
        return self.__shadowrun_AbstaktPersona11

    @shadowrun_AbstaktPersona11.setter
    def shadowrun_AbstaktPersona11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktPersona__shadowrun_AbstaktPersona11", None)
        self.__shadowrun_AbstaktPersona11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_AbstaktGegenstand12"):
                opp_val = getattr(old_value, "shadowrun_AbstaktGegenstand12", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_AbstaktGegenstand12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_AbstaktGegenstand12"):
                opp_val = getattr(value, "shadowrun_AbstaktGegenstand12", None)
                setattr(value, "shadowrun_AbstaktGegenstand12", self)

    @property
    def shadowrun_AbstaktPersona14(self):
        return self.__shadowrun_AbstaktPersona14

    @shadowrun_AbstaktPersona14.setter
    def shadowrun_AbstaktPersona14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktPersona__shadowrun_AbstaktPersona14", None)
        self.__shadowrun_AbstaktPersona14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shadowrun_AbstraktKleidung"):
                    opp_val = getattr(item, "shadowrun_AbstraktKleidung", None)
                    
                    if opp_val == self:
                        setattr(item, "shadowrun_AbstraktKleidung", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shadowrun_AbstraktKleidung"):
                    opp_val = getattr(item, "shadowrun_AbstraktKleidung", None)
                    
                    setattr(item, "shadowrun_AbstraktKleidung", self)
                    

    @property
    def shadowrun_AbstaktPersona19(self):
        return self.__shadowrun_AbstaktPersona19

    @shadowrun_AbstaktPersona19.setter
    def shadowrun_AbstaktPersona19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktPersona__shadowrun_AbstaktPersona19", None)
        self.__shadowrun_AbstaktPersona19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shadowrun_Spezies"):
                opp_val = getattr(old_value, "shadowrun_Spezies", None)
                if opp_val == self:
                    setattr(old_value, "shadowrun_Spezies", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shadowrun_Spezies"):
                opp_val = getattr(value, "shadowrun_Spezies", None)
                setattr(value, "shadowrun_Spezies", self)

    @property
    def shadowrun_AbstaktPersona(self):
        return self.__shadowrun_AbstaktPersona

    @shadowrun_AbstaktPersona.setter
    def shadowrun_AbstaktPersona(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktPersona__shadowrun_AbstaktPersona", None)
        self.__shadowrun_AbstaktPersona = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shadowrun_PersonaFertigkeit"):
                    opp_val = getattr(item, "shadowrun_PersonaFertigkeit", None)
                    
                    if opp_val == self:
                        setattr(item, "shadowrun_PersonaFertigkeit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shadowrun_PersonaFertigkeit"):
                    opp_val = getattr(item, "shadowrun_PersonaFertigkeit", None)
                    
                    setattr(item, "shadowrun_PersonaFertigkeit", self)
                    

    @property
    def persona4(self):
        return self.__persona4

    @persona4.setter
    def persona4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktPersona__persona4", None)
        self.__persona4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BioWare"):
                    opp_val = getattr(item, "BioWare", None)
                    
                    if opp_val == self:
                        setattr(item, "BioWare", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BioWare"):
                    opp_val = getattr(item, "BioWare", None)
                    
                    setattr(item, "BioWare", self)
                    

    @property
    def shadowrun_AbstaktPersona16(self):
        return self.__shadowrun_AbstaktPersona16

    @shadowrun_AbstaktPersona16.setter
    def shadowrun_AbstaktPersona16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shadowrun_AbstaktPersona__shadowrun_AbstaktPersona16", None)
        self.__shadowrun_AbstaktPersona16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shadowrun_AbstaktGegenstand17"):
                    opp_val = getattr(item, "shadowrun_AbstaktGegenstand17", None)
                    
                    if opp_val == self:
                        setattr(item, "shadowrun_AbstaktGegenstand17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shadowrun_AbstaktGegenstand17"):
                    opp_val = getattr(item, "shadowrun_AbstaktGegenstand17", None)
                    
                    setattr(item, "shadowrun_AbstaktGegenstand17", self)
                    

    def getGesamtGewicht(self) -> int:
        # TODO: Implement getGesamtGewicht method
        pass

class AbstaktWaffe:

    pass
class shadowrun_AbstraktNahkampfwaffe(NahkampfReichweite, AbstaktWaffe):

    pass
class shadowrun_Granate(AbstaktWaffe):

    def __init__(self, type: str, daempfung: str):
        self.type = type
        self.daempfung = daempfung
        
    @property
    def daempfung(self) -> str:
        return self.__daempfung

    @daempfung.setter
    def daempfung(self, daempfung: str):
        self.__daempfung = daempfung

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class shadowrun_AbstaktFernKampfwaffe(AbstaktWaffe):

    pass