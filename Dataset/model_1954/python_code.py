from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SubstanceVector(Enum):
    contact = "contact"
    inhalation = "inhalation"
    ingestion = "ingestion"
    injection = "injection"
class AddictionType(Enum):
    psychological = "psychological"
    physiological = "physiological"
    both = "both"
class InterfaceModus(Enum):
    augmentedReality = "augmentedReality"
    coldSim = "coldSim"
    hotSim = "hotSim"
class armorModificationType(Enum):
    ChemicalProtection = "ChemicalProtection"
    ChemicalSeal = "ChemicalSeal"
    FireResistance = "FireResistance"
    Insulation = "Insulation"
    Nonconductivity = "Nonconductivity"
    ShockFrills = "ShockFrills"
    ThermalDamping = "ThermalDamping"
class CyberwareType(Enum):
    cyberlimb = "cyberlimb"
    earware = "earware"
    eyeware = "eyeware"
    headware = "headware"
    bodyware = "bodyware"
class ZauberDauer(Enum):
    Sofort = "Sofort"
    Aufrechterhalten = "Aufrechterhalten"
    Permanent = "Permanent"
class MagazinTyp(Enum):
    Clip = "Clip"
    Trommel = "Trommel"
    Gurt = "Gurt"
    Streifen = "Streifen"
class ResonanzZiel(Enum):
    datei = "datei"
    geraet = "geraet"
    selbst = "selbst"
    persona = "persona"
    sprite = "sprite"
class SubstanceEffect(Enum):
    disorientation = "disorientation"
    nausea = "nausea"
    paralysis = "paralysis"
    stunDamage = "stunDamage"
class SmartgunType(Enum):
    SmartBrille = "SmartBrille"
    SmartGun = "SmartGun"
    SmatgunII = "SmatgunII"
class CritterHandlung(Enum):
    komplex = "komplex"
    auto = "auto"
class SchadensTyp(Enum):
    koerperlich = "koerperlich"
    geistig = "geistig"
    speziell = "speziell"
class ModifikatorType(Enum):
    Natural = "Natural"
    Cyber = "Cyber"
    Bio = "Bio"
class TimeUnits(Enum):
    sec = "sec"
    min = "min"
    hour = "hour"
    day = "day"
    week = "week"
    month = "month"
    year = "year"
class ProgramType(Enum):
    defaultSoft = "defaultSoft"
    dataSoft = "dataSoft"
    shopSoft = "shopSoft"
class MatrixProgramType(Enum):
    defaultProgram = "defaultProgram"
    hackingProgram = "hackingProgram"
class ZauberReichweite(Enum):
    Blickfeld = "Blickfeld"
    Begrenzt = "Begrenzt"
    Selbst = "Selbst"
    Beruehrung = "Beruehrung"
class CritterReichweite(Enum):
    blickfeld = "blickfeld"
    beruehrung = "beruehrung"
    selbst = "selbst"
    speziell = "speziell"
class CritterDauer(Enum):
    immer = "immer"
    sofort = "sofort"
    aufrechterhalten = "aufrechterhalten"
    permanent = "permanent"
    speziell = "speziell"
class FeuwerwaffenErweiterung(Enum):
    Lauf = "Lauf"
    Unten = "Unten"
    Oben = "Oben"
class FeuerModus(Enum):
    EM = "EM"
    HM = "HM"
    SM = "SM"
    AM = "AM"
class ZauberArt(Enum):
    Mana = "Mana"
    Physisch = "Physisch"
class Enzug(Enum):
    wil_log = "wil_log"
    wil_cha = "wil_cha"
    wil_int = "wil_int"


############################################
# Definition of Classes
############################################

class Wurfwaffe:

    pass
class AbtraktGranate:

    pass
class shr5_Granate(AbtraktGranate, Wurfwaffe):

    pass
class Munition:

    pass
class shr5_MiniGrenate(AbtraktGranate, Munition):

    pass
class shr5_AbtraktGranate(ABC):

    def __init__(self, blast: str, shr5_AbtraktGranate: "shr5_Substance" = None):
        self.blast = blast
        self.shr5_AbtraktGranate = shr5_AbtraktGranate
        
    @property
    def blast(self) -> str:
        return self.__blast

    @blast.setter
    def blast(self, blast: str):
        self.__blast = blast

    @property
    def shr5_AbtraktGranate(self):
        return self.__shr5_AbtraktGranate

    @shr5_AbtraktGranate.setter
    def shr5_AbtraktGranate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AbtraktGranate__shr5_AbtraktGranate", None)
        self.__shr5_AbtraktGranate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Substance174"):
                opp_val = getattr(old_value, "shr5_Substance174", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Substance174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Substance174"):
                opp_val = getattr(value, "shr5_Substance174", None)
                setattr(value, "shr5_Substance174", self)

class Spezialisierung:

    pass
class Sensor:

    pass
class CredstickTransaction:

    pass
class shr5_TransferAmount(CredstickTransaction):

    def __init__(self, amountToTransfer: str, shr5_TransferAmount: "shr5_Credstick" = None, shr5_TransferAmount158: "shr5_Credstick" = None):
        self.amountToTransfer = amountToTransfer
        self.shr5_TransferAmount = shr5_TransferAmount
        self.shr5_TransferAmount158 = shr5_TransferAmount158
        
    @property
    def amountToTransfer(self) -> str:
        return self.__amountToTransfer

    @amountToTransfer.setter
    def amountToTransfer(self, amountToTransfer: str):
        self.__amountToTransfer = amountToTransfer

    @property
    def shr5_TransferAmount(self):
        return self.__shr5_TransferAmount

    @shr5_TransferAmount.setter
    def shr5_TransferAmount(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_TransferAmount__shr5_TransferAmount", None)
        self.__shr5_TransferAmount = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Credstick156"):
                opp_val = getattr(old_value, "shr5_Credstick156", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Credstick156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Credstick156"):
                opp_val = getattr(value, "shr5_Credstick156", None)
                setattr(value, "shr5_Credstick156", self)

    @property
    def shr5_TransferAmount158(self):
        return self.__shr5_TransferAmount158

    @shr5_TransferAmount158.setter
    def shr5_TransferAmount158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_TransferAmount__shr5_TransferAmount158", None)
        self.__shr5_TransferAmount158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Credstick159"):
                opp_val = getattr(old_value, "shr5_Credstick159", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Credstick159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Credstick159"):
                opp_val = getattr(value, "shr5_Credstick159", None)
                setattr(value, "shr5_Credstick159", self)

class shr5_ShoppingTransaction(CredstickTransaction):

    def __init__(self, fee: float, caculatedCosts: str, shr5_ShoppingTransaction: set["shr5_GeldWert"] = None):
        self.fee = fee
        self.caculatedCosts = caculatedCosts
        self.shr5_ShoppingTransaction = shr5_ShoppingTransaction if shr5_ShoppingTransaction is not None else set()
        
    @property
    def caculatedCosts(self) -> str:
        return self.__caculatedCosts

    @caculatedCosts.setter
    def caculatedCosts(self, caculatedCosts: str):
        self.__caculatedCosts = caculatedCosts

    @property
    def fee(self) -> float:
        return self.__fee

    @fee.setter
    def fee(self, fee: float):
        self.__fee = fee

    @property
    def shr5_ShoppingTransaction(self):
        return self.__shr5_ShoppingTransaction

    @shr5_ShoppingTransaction.setter
    def shr5_ShoppingTransaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_ShoppingTransaction__shr5_ShoppingTransaction", None)
        self.__shr5_ShoppingTransaction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_GeldWert"):
                    opp_val = getattr(item, "shr5_GeldWert", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_GeldWert", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_GeldWert"):
                    opp_val = getattr(item, "shr5_GeldWert", None)
                    
                    setattr(item, "shr5_GeldWert", self)
                    

class CyberwareEnhancement:

    pass
class shr5_CyberImplantWeapon(CyberwareEnhancement):

    pass
class shr5_EReference:

    pass
class shr5_Capacity(ABC):

    def __init__(self, capacity: int, capacityRemains: int, shr5_Capacity: "shr5_EReference" = None):
        self.capacity = capacity
        self.capacityRemains = capacityRemains
        self.shr5_Capacity = shr5_Capacity
        
    @property
    def capacityRemains(self) -> int:
        return self.__capacityRemains

    @capacityRemains.setter
    def capacityRemains(self, capacityRemains: int):
        self.__capacityRemains = capacityRemains

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def shr5_Capacity(self):
        return self.__shr5_Capacity

    @shr5_Capacity.setter
    def shr5_Capacity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Capacity__shr5_Capacity", None)
        self.__shr5_Capacity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_EReference"):
                opp_val = getattr(old_value, "shr5_EReference", None)
                if opp_val == self:
                    setattr(old_value, "shr5_EReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_EReference"):
                opp_val = getattr(value, "shr5_EReference", None)
                setattr(value, "shr5_EReference", self)

    def canAdd(self, object: str) -> bool:
        # TODO: Implement canAdd method
        pass

class shr5_BerechneteAttribute(ABC):

    def __init__(self, menschenkenntnis: int, selbstbeherrschung: int, errinerungsvermoegen: int):
        self.menschenkenntnis = menschenkenntnis
        self.selbstbeherrschung = selbstbeherrschung
        self.errinerungsvermoegen = errinerungsvermoegen
        
    @property
    def menschenkenntnis(self) -> int:
        return self.__menschenkenntnis

    @menschenkenntnis.setter
    def menschenkenntnis(self, menschenkenntnis: int):
        self.__menschenkenntnis = menschenkenntnis

    @property
    def errinerungsvermoegen(self) -> int:
        return self.__errinerungsvermoegen

    @errinerungsvermoegen.setter
    def errinerungsvermoegen(self, errinerungsvermoegen: int):
        self.__errinerungsvermoegen = errinerungsvermoegen

    @property
    def selbstbeherrschung(self) -> int:
        return self.__selbstbeherrschung

    @selbstbeherrschung.setter
    def selbstbeherrschung(self, selbstbeherrschung: int):
        self.__selbstbeherrschung = selbstbeherrschung

class Substance:

    pass
class shr5_Toxin(Substance):

    def __init__(self, power: int, penetration: int, effect: str):
        self.power = power
        self.penetration = penetration
        self.effect = effect
        
    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def power(self) -> int:
        return self.__power

    @power.setter
    def power(self, power: int):
        self.__power = power

    @property
    def penetration(self) -> int:
        return self.__penetration

    @penetration.setter
    def penetration(self, penetration: int):
        self.__penetration = penetration

class Nahkampfwaffe:

    pass
class AbstraktFokus:

    pass
class shr5_MagieFokus(AbstraktFokus):

    def __init__(self, bindungsFaktor: int):
        self.bindungsFaktor = bindungsFaktor
        
    @property
    def bindungsFaktor(self) -> int:
        return self.__bindungsFaktor

    @bindungsFaktor.setter
    def bindungsFaktor(self, bindungsFaktor: int):
        self.__bindungsFaktor = bindungsFaktor

class shr5_QiFokus(AbstraktFokus):

    pass
class Fokus:

    pass
class shr5_WaffenFokus(Nahkampfwaffe, Fokus):

    pass
class MagischeStufe:

    pass
class shr5_MagischeStufe(ABC):

    def __init__(self, stufe: int):
        self.stufe = stufe
        
    @property
    def stufe(self) -> int:
        return self.__stufe

    @stufe.setter
    def stufe(self, stufe: int):
        self.__stufe = stufe

class shr5_FahrzeugZustand(ABC):

    def __init__(self, zustandMax: int):
        self.zustandMax = zustandMax
        
    @property
    def zustandMax(self) -> int:
        return self.__zustandMax

    @zustandMax.setter
    def zustandMax(self, zustandMax: int):
        self.__zustandMax = zustandMax

class LifestyleOption:

    pass
class shr5_PercentLifestyleOption(LifestyleOption):

    pass
class FahrzeugModifikation:

    pass
class shr5_FahrzeugErweiterung(FahrzeugModifikation):

    pass
class shr5_WeaponMount(FahrzeugModifikation):

    pass
class shr5_PersonalAreaNetwork:

    def __init__(self, slaveMax: int, shr5_PersonalAreaNetwork: set["shr5_MatrixDevice"] = None, pan: "shr5_MatrixDevice" = None, PersonalAreaNetwork: "shr5_MatrixDevice" = None):
        self.slaveMax = slaveMax
        self.shr5_PersonalAreaNetwork = shr5_PersonalAreaNetwork if shr5_PersonalAreaNetwork is not None else set()
        self.pan = pan
        self.PersonalAreaNetwork = PersonalAreaNetwork
        
    @property
    def slaveMax(self) -> int:
        return self.__slaveMax

    @slaveMax.setter
    def slaveMax(self, slaveMax: int):
        self.__slaveMax = slaveMax

    @property
    def pan(self):
        return self.__pan

    @pan.setter
    def pan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_PersonalAreaNetwork__pan", None)
        self.__pan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MatrixDevice"):
                opp_val = getattr(old_value, "MatrixDevice", None)
                if opp_val == self:
                    setattr(old_value, "MatrixDevice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MatrixDevice"):
                opp_val = getattr(value, "MatrixDevice", None)
                setattr(value, "MatrixDevice", self)

    @property
    def PersonalAreaNetwork(self):
        return self.__PersonalAreaNetwork

    @PersonalAreaNetwork.setter
    def PersonalAreaNetwork(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_PersonalAreaNetwork__PersonalAreaNetwork", None)
        self.__PersonalAreaNetwork = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "master"):
                opp_val = getattr(old_value, "master", None)
                if opp_val == self:
                    setattr(old_value, "master", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "master"):
                opp_val = getattr(value, "master", None)
                setattr(value, "master", self)

    @property
    def shr5_PersonalAreaNetwork(self):
        return self.__shr5_PersonalAreaNetwork

    @shr5_PersonalAreaNetwork.setter
    def shr5_PersonalAreaNetwork(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_PersonalAreaNetwork__shr5_PersonalAreaNetwork", None)
        self.__shr5_PersonalAreaNetwork = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_MatrixDevice131"):
                    opp_val = getattr(item, "shr5_MatrixDevice131", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_MatrixDevice131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_MatrixDevice131"):
                    opp_val = getattr(item, "shr5_MatrixDevice131", None)
                    
                    setattr(item, "shr5_MatrixDevice131", self)
                    

class BasicProgram:

    pass
class shr5_Datasoft(BasicProgram):

    pass
class shr5_ConsumerSoft(BasicProgram):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class shr5_Tutorsoft(BasicProgram):

    def __init__(self, rating: int, shr5_Tutorsoft: "shr5_Fertigkeit" = None):
        self.rating = rating
        self.shr5_Tutorsoft = shr5_Tutorsoft
        
    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def shr5_Tutorsoft(self):
        return self.__shr5_Tutorsoft

    @shr5_Tutorsoft.setter
    def shr5_Tutorsoft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Tutorsoft__shr5_Tutorsoft", None)
        self.__shr5_Tutorsoft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Fertigkeit127"):
                opp_val = getattr(old_value, "shr5_Fertigkeit127", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Fertigkeit127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Fertigkeit127"):
                opp_val = getattr(value, "shr5_Fertigkeit127", None)
                setattr(value, "shr5_Fertigkeit127", self)

class Software:

    pass
class shr5_SkillSoft(Software):

    def __init__(self, rating: int, shr5_SkillSoft: "shr5_Fertigkeit" = None):
        self.rating = rating
        self.shr5_SkillSoft = shr5_SkillSoft
        
    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def shr5_SkillSoft(self):
        return self.__shr5_SkillSoft

    @shr5_SkillSoft.setter
    def shr5_SkillSoft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_SkillSoft__shr5_SkillSoft", None)
        self.__shr5_SkillSoft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Fertigkeit129"):
                opp_val = getattr(old_value, "shr5_Fertigkeit129", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Fertigkeit129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Fertigkeit129"):
                opp_val = getattr(value, "shr5_Fertigkeit129", None)
                setattr(value, "shr5_Fertigkeit129", self)

class RiggerProgram:

    pass
class shr5_AutoSoft(RiggerProgram):

    def __init__(self, rating: int, shr5_AutoSoft: "shr5_Fertigkeit" = None, shr5_AutoSoft122: "shr5_AbstaktWaffe" = None, shr5_AutoSoft124: "shr5_Drohne" = None):
        self.rating = rating
        self.shr5_AutoSoft = shr5_AutoSoft
        self.shr5_AutoSoft122 = shr5_AutoSoft122
        self.shr5_AutoSoft124 = shr5_AutoSoft124
        
    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def shr5_AutoSoft122(self):
        return self.__shr5_AutoSoft122

    @shr5_AutoSoft122.setter
    def shr5_AutoSoft122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AutoSoft__shr5_AutoSoft122", None)
        self.__shr5_AutoSoft122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_AbstaktWaffe"):
                opp_val = getattr(old_value, "shr5_AbstaktWaffe", None)
                if opp_val == self:
                    setattr(old_value, "shr5_AbstaktWaffe", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_AbstaktWaffe"):
                opp_val = getattr(value, "shr5_AbstaktWaffe", None)
                setattr(value, "shr5_AbstaktWaffe", self)

    @property
    def shr5_AutoSoft(self):
        return self.__shr5_AutoSoft

    @shr5_AutoSoft.setter
    def shr5_AutoSoft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AutoSoft__shr5_AutoSoft", None)
        self.__shr5_AutoSoft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Fertigkeit120"):
                opp_val = getattr(old_value, "shr5_Fertigkeit120", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Fertigkeit120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Fertigkeit120"):
                opp_val = getattr(value, "shr5_Fertigkeit120", None)
                setattr(value, "shr5_Fertigkeit120", self)

    @property
    def shr5_AutoSoft124(self):
        return self.__shr5_AutoSoft124

    @shr5_AutoSoft124.setter
    def shr5_AutoSoft124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AutoSoft__shr5_AutoSoft124", None)
        self.__shr5_AutoSoft124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Drohne125"):
                opp_val = getattr(old_value, "shr5_Drohne125", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Drohne125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Drohne125"):
                opp_val = getattr(value, "shr5_Drohne125", None)
                setattr(value, "shr5_Drohne125", self)

class MatrixProgram:

    pass
class shr5_CommonProgram(MatrixProgram, RiggerProgram):

    def __init__(self, programType: str):
        self.programType = programType
        
    @property
    def programType(self) -> str:
        return self.__programType

    @programType.setter
    def programType(self, programType: str):
        self.__programType = programType

class shr5_SoftwareAgent(MatrixProgram):

    def __init__(self, rating: int):
        self.rating = rating
        
    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

class MatrixDevice:

    pass
class shr5_MatixConditionMonitor(ABC):

    def __init__(self, matrixZustandMax: int):
        self.matrixZustandMax = matrixZustandMax
        
    @property
    def matrixZustandMax(self) -> int:
        return self.__matrixZustandMax

    @matrixZustandMax.setter
    def matrixZustandMax(self, matrixZustandMax: int):
        self.__matrixZustandMax = matrixZustandMax

class shr5_BasicProgram(Software):

    pass
class AbstractMatrixDevice:

    pass
class shr5_RiggerCommandConsole(AbstractMatrixDevice):

    def __init__(self, rauschunterdrueckung: int, zugriff: int, datenverarbeitungBasis: int, firewallBasis: int, zugriffBasis: int, shr5_RiggerCommandConsole: set["shr5_RiggerProgram"] = None, shr5_RiggerCommandConsole117: set["shr5_RiggerProgram"] = None):
        self.rauschunterdrueckung = rauschunterdrueckung
        self.zugriff = zugriff
        self.datenverarbeitungBasis = datenverarbeitungBasis
        self.firewallBasis = firewallBasis
        self.zugriffBasis = zugriffBasis
        self.shr5_RiggerCommandConsole = shr5_RiggerCommandConsole if shr5_RiggerCommandConsole is not None else set()
        self.shr5_RiggerCommandConsole117 = shr5_RiggerCommandConsole117 if shr5_RiggerCommandConsole117 is not None else set()
        
    @property
    def zugriff(self) -> int:
        return self.__zugriff

    @zugriff.setter
    def zugriff(self, zugriff: int):
        self.__zugriff = zugriff

    @property
    def datenverarbeitungBasis(self) -> int:
        return self.__datenverarbeitungBasis

    @datenverarbeitungBasis.setter
    def datenverarbeitungBasis(self, datenverarbeitungBasis: int):
        self.__datenverarbeitungBasis = datenverarbeitungBasis

    @property
    def rauschunterdrueckung(self) -> int:
        return self.__rauschunterdrueckung

    @rauschunterdrueckung.setter
    def rauschunterdrueckung(self, rauschunterdrueckung: int):
        self.__rauschunterdrueckung = rauschunterdrueckung

    @property
    def zugriffBasis(self) -> int:
        return self.__zugriffBasis

    @zugriffBasis.setter
    def zugriffBasis(self, zugriffBasis: int):
        self.__zugriffBasis = zugriffBasis

    @property
    def firewallBasis(self) -> int:
        return self.__firewallBasis

    @firewallBasis.setter
    def firewallBasis(self, firewallBasis: int):
        self.__firewallBasis = firewallBasis

    @property
    def shr5_RiggerCommandConsole(self):
        return self.__shr5_RiggerCommandConsole

    @shr5_RiggerCommandConsole.setter
    def shr5_RiggerCommandConsole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_RiggerCommandConsole__shr5_RiggerCommandConsole", None)
        self.__shr5_RiggerCommandConsole = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_RiggerProgram115"):
                    opp_val = getattr(item, "shr5_RiggerProgram115", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_RiggerProgram115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_RiggerProgram115"):
                    opp_val = getattr(item, "shr5_RiggerProgram115", None)
                    
                    setattr(item, "shr5_RiggerProgram115", self)
                    

    @property
    def shr5_RiggerCommandConsole117(self):
        return self.__shr5_RiggerCommandConsole117

    @shr5_RiggerCommandConsole117.setter
    def shr5_RiggerCommandConsole117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_RiggerCommandConsole__shr5_RiggerCommandConsole117", None)
        self.__shr5_RiggerCommandConsole117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_RiggerProgram118"):
                    opp_val = getattr(item, "shr5_RiggerProgram118", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_RiggerProgram118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_RiggerProgram118"):
                    opp_val = getattr(item, "shr5_RiggerProgram118", None)
                    
                    setattr(item, "shr5_RiggerProgram118", self)
                    

class shr5_Commlink(AbstractMatrixDevice):

    pass
class MatixConditionMonitor:

    pass
class shr5_MatrixAttributes(MatixConditionMonitor):

    def __init__(self, geraetestufe: int, firewall: int, datenverarbeitung: int, currentModus: str):
        self.geraetestufe = geraetestufe
        self.firewall = firewall
        self.datenverarbeitung = datenverarbeitung
        self.currentModus = currentModus
        
    @property
    def firewall(self) -> int:
        return self.__firewall

    @firewall.setter
    def firewall(self, firewall: int):
        self.__firewall = firewall

    @property
    def currentModus(self) -> str:
        return self.__currentModus

    @currentModus.setter
    def currentModus(self, currentModus: str):
        self.__currentModus = currentModus

    @property
    def geraetestufe(self) -> int:
        return self.__geraetestufe

    @geraetestufe.setter
    def geraetestufe(self, geraetestufe: int):
        self.__geraetestufe = geraetestufe

    @property
    def datenverarbeitung(self) -> int:
        return self.__datenverarbeitung

    @datenverarbeitung.setter
    def datenverarbeitung(self, datenverarbeitung: int):
        self.__datenverarbeitung = datenverarbeitung

class shr5_Localization:

    def __init__(self, local: str, name: str, page: int, shr5_Localization: "shr5_Identifiable" = None):
        self.local = local
        self.name = name
        self.page = page
        self.shr5_Localization = shr5_Localization
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def page(self) -> int:
        return self.__page

    @page.setter
    def page(self, page: int):
        self.__page = page

    @property
    def local(self) -> str:
        return self.__local

    @local.setter
    def local(self, local: str):
        self.__local = local

    @property
    def shr5_Localization(self):
        return self.__shr5_Localization

    @shr5_Localization.setter
    def shr5_Localization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Localization__shr5_Localization", None)
        self.__shr5_Localization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Identifiable"):
                opp_val = getattr(old_value, "shr5_Identifiable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Identifiable"):
                opp_val = getattr(value, "shr5_Identifiable", None)
                if opp_val is None:
                    setattr(value, "shr5_Identifiable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5_Identifiable(ABC):

    def __init__(self, parentId: str, shr5_Identifiable: set["shr5_Localization"] = None):
        self.parentId = parentId
        self.shr5_Identifiable = shr5_Identifiable if shr5_Identifiable is not None else set()
        
    @property
    def parentId(self) -> str:
        return self.__parentId

    @parentId.setter
    def parentId(self, parentId: str):
        self.__parentId = parentId

    @property
    def shr5_Identifiable(self):
        return self.__shr5_Identifiable

    @shr5_Identifiable.setter
    def shr5_Identifiable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Identifiable__shr5_Identifiable", None)
        self.__shr5_Identifiable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_Localization"):
                    opp_val = getattr(item, "shr5_Localization", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_Localization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_Localization"):
                    opp_val = getattr(item, "shr5_Localization", None)
                    
                    setattr(item, "shr5_Localization", self)
                    

class StufenPersona:

    pass
class shr5_ModifikatorAttribute(ABC):

    pass
class shr5_Menge(ABC):

    def __init__(self, anzahl: int, proAnzahl: int):
        self.anzahl = anzahl
        self.proAnzahl = proAnzahl
        
    @property
    def proAnzahl(self) -> int:
        return self.__proAnzahl

    @proAnzahl.setter
    def proAnzahl(self, proAnzahl: int):
        self.__proAnzahl = proAnzahl

    @property
    def anzahl(self) -> int:
        return self.__anzahl

    @anzahl.setter
    def anzahl(self, anzahl: int):
        self.__anzahl = anzahl

class shr5_CredstickTransaction:

    def __init__(self, amount: str, date: str, description: str, shr5_CredstickTransaction: "shr5_Credstick" = None):
        self.amount = amount
        self.date = date
        self.description = description
        self.shr5_CredstickTransaction = shr5_CredstickTransaction
        
    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def amount(self) -> str:
        return self.__amount

    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def shr5_CredstickTransaction(self):
        return self.__shr5_CredstickTransaction

    @shr5_CredstickTransaction.setter
    def shr5_CredstickTransaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_CredstickTransaction__shr5_CredstickTransaction", None)
        self.__shr5_CredstickTransaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Credstick"):
                opp_val = getattr(old_value, "shr5_Credstick", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Credstick"):
                opp_val = getattr(value, "shr5_Credstick", None)
                if opp_val is None:
                    setattr(value, "shr5_Credstick", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5_Erlernbar(ABC):

    pass
class Fakeable:

    pass
class shr5_Lizenz(Fakeable):

    def __init__(self, lizenGegenstand: str, Lizenz: "shr5_Sin" = None, licences: "shr5_Sin" = None):
        self.lizenGegenstand = lizenGegenstand
        self.Lizenz = Lizenz
        self.licences = licences
        
    @property
    def lizenGegenstand(self) -> str:
        return self.__lizenGegenstand

    @lizenGegenstand.setter
    def lizenGegenstand(self, lizenGegenstand: str):
        self.__lizenGegenstand = lizenGegenstand

    @property
    def licences(self):
        return self.__licences

    @licences.setter
    def licences(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Lizenz__licences", None)
        self.__licences = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sin"):
                opp_val = getattr(old_value, "Sin", None)
                if opp_val == self:
                    setattr(old_value, "Sin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sin"):
                opp_val = getattr(value, "Sin", None)
                setattr(value, "Sin", self)

    @property
    def Lizenz(self):
        return self.__Lizenz

    @Lizenz.setter
    def Lizenz(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Lizenz__Lizenz", None)
        self.__Lizenz = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lizenzTraeger"):
                opp_val = getattr(old_value, "lizenzTraeger", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lizenzTraeger"):
                opp_val = getattr(value, "lizenzTraeger", None)
                if opp_val is None:
                    setattr(value, "lizenzTraeger", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5_Sin(Fakeable):

    pass
class Vertrag:

    pass
class shr5_Fakeable(Vertrag):

    def __init__(self, stufe: int, gefaelscht: bool):
        self.stufe = stufe
        self.gefaelscht = gefaelscht
        
    @property
    def gefaelscht(self) -> bool:
        return self.__gefaelscht

    @gefaelscht.setter
    def gefaelscht(self, gefaelscht: bool):
        self.__gefaelscht = gefaelscht

    @property
    def stufe(self) -> int:
        return self.__stufe

    @stufe.setter
    def stufe(self, stufe: int):
        self.__stufe = stufe

class shr5_IntervallVertrag(Vertrag):

    def __init__(self, unit: str, begin: str, faelligkeitsIntervall: int):
        self.unit = unit
        self.begin = begin
        self.faelligkeitsIntervall = faelligkeitsIntervall
        
    @property
    def faelligkeitsIntervall(self) -> int:
        return self.__faelligkeitsIntervall

    @faelligkeitsIntervall.setter
    def faelligkeitsIntervall(self, faelligkeitsIntervall: int):
        self.__faelligkeitsIntervall = faelligkeitsIntervall

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def begin(self) -> str:
        return self.__begin

    @begin.setter
    def begin(self, begin: str):
        self.__begin = begin

class Spezies:

    pass
class shr5_Critter(Spezies):

    pass
class shr5_PersonaZustand(ABC):

    def __init__(self, zustandKoerperlichMax: int, zustandGeistigMax: int, zustandGrenze: int):
        self.zustandKoerperlichMax = zustandKoerperlichMax
        self.zustandGeistigMax = zustandGeistigMax
        self.zustandGrenze = zustandGrenze
        
    @property
    def zustandGrenze(self) -> int:
        return self.__zustandGrenze

    @zustandGrenze.setter
    def zustandGrenze(self, zustandGrenze: int):
        self.__zustandGrenze = zustandGrenze

    @property
    def zustandKoerperlichMax(self) -> int:
        return self.__zustandKoerperlichMax

    @zustandKoerperlichMax.setter
    def zustandKoerperlichMax(self, zustandKoerperlichMax: int):
        self.__zustandKoerperlichMax = zustandKoerperlichMax

    @property
    def zustandGeistigMax(self) -> int:
        return self.__zustandGeistigMax

    @zustandGeistigMax.setter
    def zustandGeistigMax(self, zustandGeistigMax: int):
        self.__zustandGeistigMax = zustandGeistigMax

class Wissensfertigkeit:

    pass
class shr5_Sprachfertigkeit(Wissensfertigkeit):

    pass
class Fertigkeit:

    pass
class shr5_Wissensfertigkeit(Fertigkeit):

    pass
class IntervallVertrag:

    pass
class shr5_Lifestyle(IntervallVertrag):

    def __init__(self, owned: bool, shr5_Lifestyle: set["shr5_LifestyleOption"] = None):
        self.owned = owned
        self.shr5_Lifestyle = shr5_Lifestyle if shr5_Lifestyle is not None else set()
        
    @property
    def owned(self) -> bool:
        return self.__owned

    @owned.setter
    def owned(self, owned: bool):
        self.__owned = owned

    @property
    def shr5_Lifestyle(self):
        return self.__shr5_Lifestyle

    @shr5_Lifestyle.setter
    def shr5_Lifestyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Lifestyle__shr5_Lifestyle", None)
        self.__shr5_Lifestyle = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_LifestyleOption"):
                    opp_val = getattr(item, "shr5_LifestyleOption", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_LifestyleOption", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_LifestyleOption"):
                    opp_val = getattr(item, "shr5_LifestyleOption", None)
                    
                    setattr(item, "shr5_LifestyleOption", self)
                    

class ActiveMatixDevice:

    pass
class shr5_ResonanzPersona(ActiveMatixDevice):

    def __init__(self, resonanz: int, resonanzBasis: int):
        self.resonanz = resonanz
        self.resonanzBasis = resonanzBasis
        
    @property
    def resonanzBasis(self) -> int:
        return self.__resonanzBasis

    @resonanzBasis.setter
    def resonanzBasis(self, resonanzBasis: int):
        self.__resonanzBasis = resonanzBasis

    @property
    def resonanz(self) -> int:
        return self.__resonanz

    @resonanz.setter
    def resonanz(self, resonanz: int):
        self.__resonanz = resonanz

class ResonanzPersona:

    pass
class shr5_RiggerProgram(Software):

    pass
class MatrixAttributes:

    pass
class shr5_ActiveMatixDevice(MatrixAttributes):

    def __init__(self, angriff: int, schleicher: int):
        self.angriff = angriff
        self.schleicher = schleicher
        
    @property
    def schleicher(self) -> int:
        return self.__schleicher

    @schleicher.setter
    def schleicher(self, schleicher: int):
        self.__schleicher = schleicher

    @property
    def angriff(self) -> int:
        return self.__angriff

    @angriff.setter
    def angriff(self, angriff: int):
        self.__angriff = angriff

class Fahrzeug:

    pass
class shr5_Drohne(MatrixAttributes, Fahrzeug):

    def __init__(self, programSlotCount: int, shr5_Drohne: set["shr5_RiggerProgram"] = None, shr5_Drohne75: set["shr5_RiggerProgram"] = None, shr5_Drohne125: "shr5_AutoSoft" = None):
        self.programSlotCount = programSlotCount
        self.shr5_Drohne = shr5_Drohne if shr5_Drohne is not None else set()
        self.shr5_Drohne75 = shr5_Drohne75 if shr5_Drohne75 is not None else set()
        self.shr5_Drohne125 = shr5_Drohne125
        
    @property
    def programSlotCount(self) -> int:
        return self.__programSlotCount

    @programSlotCount.setter
    def programSlotCount(self, programSlotCount: int):
        self.__programSlotCount = programSlotCount

    @property
    def shr5_Drohne75(self):
        return self.__shr5_Drohne75

    @shr5_Drohne75.setter
    def shr5_Drohne75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Drohne__shr5_Drohne75", None)
        self.__shr5_Drohne75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_RiggerProgram76"):
                    opp_val = getattr(item, "shr5_RiggerProgram76", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_RiggerProgram76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_RiggerProgram76"):
                    opp_val = getattr(item, "shr5_RiggerProgram76", None)
                    
                    setattr(item, "shr5_RiggerProgram76", self)
                    

    @property
    def shr5_Drohne125(self):
        return self.__shr5_Drohne125

    @shr5_Drohne125.setter
    def shr5_Drohne125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Drohne__shr5_Drohne125", None)
        self.__shr5_Drohne125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_AutoSoft124"):
                opp_val = getattr(old_value, "shr5_AutoSoft124", None)
                if opp_val == self:
                    setattr(old_value, "shr5_AutoSoft124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_AutoSoft124"):
                opp_val = getattr(value, "shr5_AutoSoft124", None)
                setattr(value, "shr5_AutoSoft124", self)

    @property
    def shr5_Drohne(self):
        return self.__shr5_Drohne

    @shr5_Drohne.setter
    def shr5_Drohne(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Drohne__shr5_Drohne", None)
        self.__shr5_Drohne = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_RiggerProgram"):
                    opp_val = getattr(item, "shr5_RiggerProgram", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_RiggerProgram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_RiggerProgram"):
                    opp_val = getattr(item, "shr5_RiggerProgram", None)
                    
                    setattr(item, "shr5_RiggerProgram", self)
                    

class shr5_PassagierFahrzeug(Fahrzeug):

    def __init__(self, sitze: int):
        self.sitze = sitze
        
    @property
    def sitze(self) -> int:
        return self.__sitze

    @sitze.setter
    def sitze(self, sitze: int):
        self.__sitze = sitze

class PassagierFahrzeug:

    pass
class shr5_Bodenfahrzeug(PassagierFahrzeug):

    def __init__(self, handlingGelaende: int, geschwindigkeitGelaende: int):
        self.handlingGelaende = handlingGelaende
        self.geschwindigkeitGelaende = geschwindigkeitGelaende
        
    @property
    def geschwindigkeitGelaende(self) -> int:
        return self.__geschwindigkeitGelaende

    @geschwindigkeitGelaende.setter
    def geschwindigkeitGelaende(self, geschwindigkeitGelaende: int):
        self.__geschwindigkeitGelaende = geschwindigkeitGelaende

    @property
    def handlingGelaende(self) -> int:
        return self.__handlingGelaende

    @handlingGelaende.setter
    def handlingGelaende(self, handlingGelaende: int):
        self.__handlingGelaende = handlingGelaende

class shr5_SensorArray(Sensor):

    pass
class shr5_AstraleProjektion(ABC):

    def __init__(self, astralesLimit: int, astraleKonstitution: int, astraleGeschicklichkeit: int, astraleReaktion: int, astraleStaerke: int, astraleInitative: int, astraleInitativWuerfel: int, astralePanzerung: int):
        self.astralesLimit = astralesLimit
        self.astraleKonstitution = astraleKonstitution
        self.astraleGeschicklichkeit = astraleGeschicklichkeit
        self.astraleReaktion = astraleReaktion
        self.astraleStaerke = astraleStaerke
        self.astraleInitative = astraleInitative
        self.astraleInitativWuerfel = astraleInitativWuerfel
        self.astralePanzerung = astralePanzerung
        
    @property
    def astraleInitative(self) -> int:
        return self.__astraleInitative

    @astraleInitative.setter
    def astraleInitative(self, astraleInitative: int):
        self.__astraleInitative = astraleInitative

    @property
    def astraleStaerke(self) -> int:
        return self.__astraleStaerke

    @astraleStaerke.setter
    def astraleStaerke(self, astraleStaerke: int):
        self.__astraleStaerke = astraleStaerke

    @property
    def astralePanzerung(self) -> int:
        return self.__astralePanzerung

    @astralePanzerung.setter
    def astralePanzerung(self, astralePanzerung: int):
        self.__astralePanzerung = astralePanzerung

    @property
    def astraleKonstitution(self) -> int:
        return self.__astraleKonstitution

    @astraleKonstitution.setter
    def astraleKonstitution(self, astraleKonstitution: int):
        self.__astraleKonstitution = astraleKonstitution

    @property
    def astraleInitativWuerfel(self) -> int:
        return self.__astraleInitativWuerfel

    @astraleInitativWuerfel.setter
    def astraleInitativWuerfel(self, astraleInitativWuerfel: int):
        self.__astraleInitativWuerfel = astraleInitativWuerfel

    @property
    def astraleReaktion(self) -> int:
        return self.__astraleReaktion

    @astraleReaktion.setter
    def astraleReaktion(self, astraleReaktion: int):
        self.__astraleReaktion = astraleReaktion

    @property
    def astraleGeschicklichkeit(self) -> int:
        return self.__astraleGeschicklichkeit

    @astraleGeschicklichkeit.setter
    def astraleGeschicklichkeit(self, astraleGeschicklichkeit: int):
        self.__astraleGeschicklichkeit = astraleGeschicklichkeit

    @property
    def astralesLimit(self) -> int:
        return self.__astralesLimit

    @astralesLimit.setter
    def astralesLimit(self, astralesLimit: int):
        self.__astralesLimit = astralesLimit

class FahrzeugZustand:

    pass
class shr5_Panzerung(ABC):

    def __init__(self, panzer: int):
        self.panzer = panzer
        
    @property
    def panzer(self) -> int:
        return self.__panzer

    @panzer.setter
    def panzer(self, panzer: int):
        self.__panzer = panzer

class shr5_ChrakterLimits(ABC):

    def __init__(self, koerperlich: int, geistig: int, sozial: int):
        self.koerperlich = koerperlich
        self.geistig = geistig
        self.sozial = sozial
        
    @property
    def geistig(self) -> int:
        return self.__geistig

    @geistig.setter
    def geistig(self, geistig: int):
        self.__geistig = geistig

    @property
    def koerperlich(self) -> int:
        return self.__koerperlich

    @koerperlich.setter
    def koerperlich(self, koerperlich: int):
        self.__koerperlich = koerperlich

    @property
    def sozial(self) -> int:
        return self.__sozial

    @sozial.setter
    def sozial(self, sozial: int):
        self.__sozial = sozial

class KiAdept:

    pass
class shr5_GebundenerGeist:

    def __init__(self, dienste: int, shr5_GebundenerGeist: "shr5_Zauberer" = None, shr5_GebundenerGeist61: "shr5_Zauberer" = None, shr5_GebundenerGeist90: "shr5_Geist" = None):
        self.dienste = dienste
        self.shr5_GebundenerGeist = shr5_GebundenerGeist
        self.shr5_GebundenerGeist61 = shr5_GebundenerGeist61
        self.shr5_GebundenerGeist90 = shr5_GebundenerGeist90
        
    @property
    def dienste(self) -> int:
        return self.__dienste

    @dienste.setter
    def dienste(self, dienste: int):
        self.__dienste = dienste

    @property
    def shr5_GebundenerGeist90(self):
        return self.__shr5_GebundenerGeist90

    @shr5_GebundenerGeist90.setter
    def shr5_GebundenerGeist90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_GebundenerGeist__shr5_GebundenerGeist90", None)
        self.__shr5_GebundenerGeist90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Geist"):
                opp_val = getattr(old_value, "shr5_Geist", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Geist", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Geist"):
                opp_val = getattr(value, "shr5_Geist", None)
                setattr(value, "shr5_Geist", self)

    @property
    def shr5_GebundenerGeist(self):
        return self.__shr5_GebundenerGeist

    @shr5_GebundenerGeist.setter
    def shr5_GebundenerGeist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_GebundenerGeist__shr5_GebundenerGeist", None)
        self.__shr5_GebundenerGeist = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Zauberer58"):
                opp_val = getattr(old_value, "shr5_Zauberer58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Zauberer58"):
                opp_val = getattr(value, "shr5_Zauberer58", None)
                if opp_val is None:
                    setattr(value, "shr5_Zauberer58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5_GebundenerGeist61(self):
        return self.__shr5_GebundenerGeist61

    @shr5_GebundenerGeist61.setter
    def shr5_GebundenerGeist61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_GebundenerGeist__shr5_GebundenerGeist61", None)
        self.__shr5_GebundenerGeist61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Zauberer60"):
                opp_val = getattr(old_value, "shr5_Zauberer60", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Zauberer60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Zauberer60"):
                opp_val = getattr(value, "shr5_Zauberer60", None)
                setattr(value, "shr5_Zauberer60", self)

class shr5_Zauberer(ABC):

    def __init__(self, enzug: int, shr5_Zauberer: set["shr5_PersonaZauber"] = None, shr5_Zauberer58: set["shr5_GebundenerGeist"] = None, shr5_Zauberer60: "shr5_GebundenerGeist" = None, shr5_Zauberer63: "shr5_MagischeTradition" = None):
        self.enzug = enzug
        self.shr5_Zauberer = shr5_Zauberer if shr5_Zauberer is not None else set()
        self.shr5_Zauberer58 = shr5_Zauberer58 if shr5_Zauberer58 is not None else set()
        self.shr5_Zauberer60 = shr5_Zauberer60
        self.shr5_Zauberer63 = shr5_Zauberer63
        
    @property
    def enzug(self) -> int:
        return self.__enzug

    @enzug.setter
    def enzug(self, enzug: int):
        self.__enzug = enzug

    @property
    def shr5_Zauberer(self):
        return self.__shr5_Zauberer

    @shr5_Zauberer.setter
    def shr5_Zauberer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Zauberer__shr5_Zauberer", None)
        self.__shr5_Zauberer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_PersonaZauber"):
                    opp_val = getattr(item, "shr5_PersonaZauber", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_PersonaZauber", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_PersonaZauber"):
                    opp_val = getattr(item, "shr5_PersonaZauber", None)
                    
                    setattr(item, "shr5_PersonaZauber", self)
                    

    @property
    def shr5_Zauberer60(self):
        return self.__shr5_Zauberer60

    @shr5_Zauberer60.setter
    def shr5_Zauberer60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Zauberer__shr5_Zauberer60", None)
        self.__shr5_Zauberer60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_GebundenerGeist61"):
                opp_val = getattr(old_value, "shr5_GebundenerGeist61", None)
                if opp_val == self:
                    setattr(old_value, "shr5_GebundenerGeist61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_GebundenerGeist61"):
                opp_val = getattr(value, "shr5_GebundenerGeist61", None)
                setattr(value, "shr5_GebundenerGeist61", self)

    @property
    def shr5_Zauberer58(self):
        return self.__shr5_Zauberer58

    @shr5_Zauberer58.setter
    def shr5_Zauberer58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Zauberer__shr5_Zauberer58", None)
        self.__shr5_Zauberer58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_GebundenerGeist"):
                    opp_val = getattr(item, "shr5_GebundenerGeist", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_GebundenerGeist", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_GebundenerGeist"):
                    opp_val = getattr(item, "shr5_GebundenerGeist", None)
                    
                    setattr(item, "shr5_GebundenerGeist", self)
                    

    @property
    def shr5_Zauberer63(self):
        return self.__shr5_Zauberer63

    @shr5_Zauberer63.setter
    def shr5_Zauberer63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Zauberer__shr5_Zauberer63", None)
        self.__shr5_Zauberer63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_MagischeTradition"):
                opp_val = getattr(old_value, "shr5_MagischeTradition", None)
                if opp_val == self:
                    setattr(old_value, "shr5_MagischeTradition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_MagischeTradition"):
                opp_val = getattr(value, "shr5_MagischeTradition", None)
                setattr(value, "shr5_MagischeTradition", self)

class AstraleProjektion:

    pass
class shr5_Geist(StufenPersona, AstraleProjektion):

    def __init__(self, intuitionBasis: int, logikBasis: int, konstitutionBasis: int, geschicklichkeitBasis: int, reaktionBasis: int, staerkeBasis: int, charismaBasis: int, willenskraftBasis: int, shr5_Geist: "shr5_GebundenerGeist" = None, shr5_Geist97: set["shr5_CritterKraft"] = None, shr5_Geist100: set["shr5_CritterKraft"] = None, shr5_Geist153: "shr5_MagischeTradition" = None):
        self.intuitionBasis = intuitionBasis
        self.logikBasis = logikBasis
        self.konstitutionBasis = konstitutionBasis
        self.geschicklichkeitBasis = geschicklichkeitBasis
        self.reaktionBasis = reaktionBasis
        self.staerkeBasis = staerkeBasis
        self.charismaBasis = charismaBasis
        self.willenskraftBasis = willenskraftBasis
        self.shr5_Geist = shr5_Geist
        self.shr5_Geist97 = shr5_Geist97 if shr5_Geist97 is not None else set()
        self.shr5_Geist100 = shr5_Geist100 if shr5_Geist100 is not None else set()
        self.shr5_Geist153 = shr5_Geist153
        
    @property
    def intuitionBasis(self) -> int:
        return self.__intuitionBasis

    @intuitionBasis.setter
    def intuitionBasis(self, intuitionBasis: int):
        self.__intuitionBasis = intuitionBasis

    @property
    def willenskraftBasis(self) -> int:
        return self.__willenskraftBasis

    @willenskraftBasis.setter
    def willenskraftBasis(self, willenskraftBasis: int):
        self.__willenskraftBasis = willenskraftBasis

    @property
    def logikBasis(self) -> int:
        return self.__logikBasis

    @logikBasis.setter
    def logikBasis(self, logikBasis: int):
        self.__logikBasis = logikBasis

    @property
    def reaktionBasis(self) -> int:
        return self.__reaktionBasis

    @reaktionBasis.setter
    def reaktionBasis(self, reaktionBasis: int):
        self.__reaktionBasis = reaktionBasis

    @property
    def staerkeBasis(self) -> int:
        return self.__staerkeBasis

    @staerkeBasis.setter
    def staerkeBasis(self, staerkeBasis: int):
        self.__staerkeBasis = staerkeBasis

    @property
    def charismaBasis(self) -> int:
        return self.__charismaBasis

    @charismaBasis.setter
    def charismaBasis(self, charismaBasis: int):
        self.__charismaBasis = charismaBasis

    @property
    def konstitutionBasis(self) -> int:
        return self.__konstitutionBasis

    @konstitutionBasis.setter
    def konstitutionBasis(self, konstitutionBasis: int):
        self.__konstitutionBasis = konstitutionBasis

    @property
    def geschicklichkeitBasis(self) -> int:
        return self.__geschicklichkeitBasis

    @geschicklichkeitBasis.setter
    def geschicklichkeitBasis(self, geschicklichkeitBasis: int):
        self.__geschicklichkeitBasis = geschicklichkeitBasis

    @property
    def shr5_Geist97(self):
        return self.__shr5_Geist97

    @shr5_Geist97.setter
    def shr5_Geist97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Geist__shr5_Geist97", None)
        self.__shr5_Geist97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_CritterKraft98"):
                    opp_val = getattr(item, "shr5_CritterKraft98", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_CritterKraft98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_CritterKraft98"):
                    opp_val = getattr(item, "shr5_CritterKraft98", None)
                    
                    setattr(item, "shr5_CritterKraft98", self)
                    

    @property
    def shr5_Geist153(self):
        return self.__shr5_Geist153

    @shr5_Geist153.setter
    def shr5_Geist153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Geist__shr5_Geist153", None)
        self.__shr5_Geist153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_MagischeTradition152"):
                opp_val = getattr(old_value, "shr5_MagischeTradition152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_MagischeTradition152"):
                opp_val = getattr(value, "shr5_MagischeTradition152", None)
                if opp_val is None:
                    setattr(value, "shr5_MagischeTradition152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5_Geist100(self):
        return self.__shr5_Geist100

    @shr5_Geist100.setter
    def shr5_Geist100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Geist__shr5_Geist100", None)
        self.__shr5_Geist100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_CritterKraft101"):
                    opp_val = getattr(item, "shr5_CritterKraft101", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_CritterKraft101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_CritterKraft101"):
                    opp_val = getattr(item, "shr5_CritterKraft101", None)
                    
                    setattr(item, "shr5_CritterKraft101", self)
                    

    @property
    def shr5_Geist(self):
        return self.__shr5_Geist

    @shr5_Geist.setter
    def shr5_Geist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Geist__shr5_Geist", None)
        self.__shr5_Geist = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_GebundenerGeist90"):
                opp_val = getattr(old_value, "shr5_GebundenerGeist90", None)
                if opp_val == self:
                    setattr(old_value, "shr5_GebundenerGeist90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_GebundenerGeist90"):
                opp_val = getattr(value, "shr5_GebundenerGeist90", None)
                setattr(value, "shr5_GebundenerGeist90", self)

class Zauberer:

    pass
class shr5_MysticAdept(Zauberer, KiAdept):

    pass
class shr5_Anwendbar(ABC):

    pass
class MagischePersona:

    pass
class shr5_Magier(Zauberer, AstraleProjektion, MagischePersona):

    pass
class shr5_AspektMagier(Zauberer, MagischePersona):

    pass
class shr5_KiAdept(MagischePersona):

    pass
class shr5_FokusBinding:

    def __init__(self, active: bool, shr5_FokusBinding: "shr5_BaseMagischePersona" = None, shr5_FokusBinding140: "shr5_Fokus" = None):
        self.active = active
        self.shr5_FokusBinding = shr5_FokusBinding
        self.shr5_FokusBinding140 = shr5_FokusBinding140
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def shr5_FokusBinding(self):
        return self.__shr5_FokusBinding

    @shr5_FokusBinding.setter
    def shr5_FokusBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_FokusBinding__shr5_FokusBinding", None)
        self.__shr5_FokusBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_BaseMagischePersona46"):
                opp_val = getattr(old_value, "shr5_BaseMagischePersona46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_BaseMagischePersona46"):
                opp_val = getattr(value, "shr5_BaseMagischePersona46", None)
                if opp_val is None:
                    setattr(value, "shr5_BaseMagischePersona46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5_FokusBinding140(self):
        return self.__shr5_FokusBinding140

    @shr5_FokusBinding140.setter
    def shr5_FokusBinding140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_FokusBinding__shr5_FokusBinding140", None)
        self.__shr5_FokusBinding140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Fokus"):
                opp_val = getattr(old_value, "shr5_Fokus", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Fokus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Fokus"):
                opp_val = getattr(value, "shr5_Fokus", None)
                setattr(value, "shr5_Fokus", self)

class shr5_BaseMagischePersona(ABC):

    def __init__(self, magie: int, magieBasis: int, shr5_BaseMagischePersona: set["shr5_Initation"] = None, shr5_BaseMagischePersona46: set["shr5_FokusBinding"] = None):
        self.magie = magie
        self.magieBasis = magieBasis
        self.shr5_BaseMagischePersona = shr5_BaseMagischePersona if shr5_BaseMagischePersona is not None else set()
        self.shr5_BaseMagischePersona46 = shr5_BaseMagischePersona46 if shr5_BaseMagischePersona46 is not None else set()
        
    @property
    def magieBasis(self) -> int:
        return self.__magieBasis

    @magieBasis.setter
    def magieBasis(self, magieBasis: int):
        self.__magieBasis = magieBasis

    @property
    def magie(self) -> int:
        return self.__magie

    @magie.setter
    def magie(self, magie: int):
        self.__magie = magie

    @property
    def shr5_BaseMagischePersona(self):
        return self.__shr5_BaseMagischePersona

    @shr5_BaseMagischePersona.setter
    def shr5_BaseMagischePersona(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_BaseMagischePersona__shr5_BaseMagischePersona", None)
        self.__shr5_BaseMagischePersona = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_Initation"):
                    opp_val = getattr(item, "shr5_Initation", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_Initation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_Initation"):
                    opp_val = getattr(item, "shr5_Initation", None)
                    
                    setattr(item, "shr5_Initation", self)
                    

    @property
    def shr5_BaseMagischePersona46(self):
        return self.__shr5_BaseMagischePersona46

    @shr5_BaseMagischePersona46.setter
    def shr5_BaseMagischePersona46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_BaseMagischePersona__shr5_BaseMagischePersona46", None)
        self.__shr5_BaseMagischePersona46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_FokusBinding"):
                    opp_val = getattr(item, "shr5_FokusBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_FokusBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_FokusBinding"):
                    opp_val = getattr(item, "shr5_FokusBinding", None)
                    
                    setattr(item, "shr5_FokusBinding", self)
                    

class BaseMagischePersona:

    pass
class Erlernbar:

    pass
class shr5_PersonaMartialartTechnique(Erlernbar):

    pass
class shr5_PersonaKomplexForm(Erlernbar):

    def __init__(self, stufe: int, shr5_PersonaKomplexForm: "shr5_Technomancer" = None, shr5_PersonaKomplexForm81: "shr5_KomplexeForm" = None):
        self.stufe = stufe
        self.shr5_PersonaKomplexForm = shr5_PersonaKomplexForm
        self.shr5_PersonaKomplexForm81 = shr5_PersonaKomplexForm81
        
    @property
    def stufe(self) -> int:
        return self.__stufe

    @stufe.setter
    def stufe(self, stufe: int):
        self.__stufe = stufe

    @property
    def shr5_PersonaKomplexForm(self):
        return self.__shr5_PersonaKomplexForm

    @shr5_PersonaKomplexForm.setter
    def shr5_PersonaKomplexForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_PersonaKomplexForm__shr5_PersonaKomplexForm", None)
        self.__shr5_PersonaKomplexForm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Technomancer"):
                opp_val = getattr(old_value, "shr5_Technomancer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Technomancer"):
                opp_val = getattr(value, "shr5_Technomancer", None)
                if opp_val is None:
                    setattr(value, "shr5_Technomancer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5_PersonaKomplexForm81(self):
        return self.__shr5_PersonaKomplexForm81

    @shr5_PersonaKomplexForm81.setter
    def shr5_PersonaKomplexForm81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_PersonaKomplexForm__shr5_PersonaKomplexForm81", None)
        self.__shr5_PersonaKomplexForm81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_KomplexeForm"):
                opp_val = getattr(old_value, "shr5_KomplexeForm", None)
                if opp_val == self:
                    setattr(old_value, "shr5_KomplexeForm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_KomplexeForm"):
                opp_val = getattr(value, "shr5_KomplexeForm", None)
                setattr(value, "shr5_KomplexeForm", self)

class shr5_PersonaZauber(Erlernbar):

    def __init__(self, stufe: int, shr5_PersonaZauber: "shr5_Zauberer" = None, shr5_PersonaZauber65: "shr5_Zauber" = None):
        self.stufe = stufe
        self.shr5_PersonaZauber = shr5_PersonaZauber
        self.shr5_PersonaZauber65 = shr5_PersonaZauber65
        
    @property
    def stufe(self) -> int:
        return self.__stufe

    @stufe.setter
    def stufe(self, stufe: int):
        self.__stufe = stufe

    @property
    def shr5_PersonaZauber65(self):
        return self.__shr5_PersonaZauber65

    @shr5_PersonaZauber65.setter
    def shr5_PersonaZauber65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_PersonaZauber__shr5_PersonaZauber65", None)
        self.__shr5_PersonaZauber65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Zauber"):
                opp_val = getattr(old_value, "shr5_Zauber", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Zauber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Zauber"):
                opp_val = getattr(value, "shr5_Zauber", None)
                setattr(value, "shr5_Zauber", self)

    @property
    def shr5_PersonaZauber(self):
        return self.__shr5_PersonaZauber

    @shr5_PersonaZauber.setter
    def shr5_PersonaZauber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_PersonaZauber__shr5_PersonaZauber", None)
        self.__shr5_PersonaZauber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Zauberer"):
                opp_val = getattr(old_value, "shr5_Zauberer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Zauberer"):
                opp_val = getattr(value, "shr5_Zauberer", None)
                if opp_val is None:
                    setattr(value, "shr5_Zauberer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5_Fokus(MagischeStufe, Erlernbar):

    def __init__(self, bindungskosten: int, shr5_Fokus: "shr5_FokusBinding" = None):
        self.bindungskosten = bindungskosten
        self.shr5_Fokus = shr5_Fokus
        
    @property
    def bindungskosten(self) -> int:
        return self.__bindungskosten

    @bindungskosten.setter
    def bindungskosten(self, bindungskosten: int):
        self.__bindungskosten = bindungskosten

    @property
    def shr5_Fokus(self):
        return self.__shr5_Fokus

    @shr5_Fokus.setter
    def shr5_Fokus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fokus__shr5_Fokus", None)
        self.__shr5_Fokus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_FokusBinding140"):
                opp_val = getattr(old_value, "shr5_FokusBinding140", None)
                if opp_val == self:
                    setattr(old_value, "shr5_FokusBinding140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_FokusBinding140"):
                opp_val = getattr(value, "shr5_FokusBinding140", None)
                setattr(value, "shr5_FokusBinding140", self)

class shr5_Steigerbar(Erlernbar):

    def __init__(self, stufe: int):
        self.stufe = stufe
        
    @property
    def stufe(self) -> int:
        return self.__stufe

    @stufe.setter
    def stufe(self, stufe: int):
        self.__stufe = stufe

class MagischeMods:

    pass
class shr5_Schutzgeist(MagischeMods):

    def __init__(self, vorteile: str, nachteile: str, shr5_Schutzgeist: "shr5_MagischePersona" = None):
        self.vorteile = vorteile
        self.nachteile = nachteile
        self.shr5_Schutzgeist = shr5_Schutzgeist
        
    @property
    def vorteile(self) -> str:
        return self.__vorteile

    @vorteile.setter
    def vorteile(self, vorteile: str):
        self.__vorteile = vorteile

    @property
    def nachteile(self) -> str:
        return self.__nachteile

    @nachteile.setter
    def nachteile(self, nachteile: str):
        self.__nachteile = nachteile

    @property
    def shr5_Schutzgeist(self):
        return self.__shr5_Schutzgeist

    @shr5_Schutzgeist.setter
    def shr5_Schutzgeist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Schutzgeist__shr5_Schutzgeist", None)
        self.__shr5_Schutzgeist = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_MagischePersona"):
                opp_val = getattr(old_value, "shr5_MagischePersona", None)
                if opp_val == self:
                    setattr(old_value, "shr5_MagischePersona", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_MagischePersona"):
                opp_val = getattr(value, "shr5_MagischePersona", None)
                setattr(value, "shr5_MagischePersona", self)

class shr5_CritterKraft(MagischeMods):

    def __init__(self, art: str, handlung: str, reichweite: str, dauer: str, shr5_CritterKraft: "shr5_Critter" = None, shr5_CritterKraft98: "shr5_Geist" = None, shr5_CritterKraft101: "shr5_Geist" = None):
        self.art = art
        self.handlung = handlung
        self.reichweite = reichweite
        self.dauer = dauer
        self.shr5_CritterKraft = shr5_CritterKraft
        self.shr5_CritterKraft98 = shr5_CritterKraft98
        self.shr5_CritterKraft101 = shr5_CritterKraft101
        
    @property
    def handlung(self) -> str:
        return self.__handlung

    @handlung.setter
    def handlung(self, handlung: str):
        self.__handlung = handlung

    @property
    def reichweite(self) -> str:
        return self.__reichweite

    @reichweite.setter
    def reichweite(self, reichweite: str):
        self.__reichweite = reichweite

    @property
    def art(self) -> str:
        return self.__art

    @art.setter
    def art(self, art: str):
        self.__art = art

    @property
    def dauer(self) -> str:
        return self.__dauer

    @dauer.setter
    def dauer(self, dauer: str):
        self.__dauer = dauer

    @property
    def shr5_CritterKraft(self):
        return self.__shr5_CritterKraft

    @shr5_CritterKraft.setter
    def shr5_CritterKraft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_CritterKraft__shr5_CritterKraft", None)
        self.__shr5_CritterKraft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Critter"):
                opp_val = getattr(old_value, "shr5_Critter", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Critter"):
                opp_val = getattr(value, "shr5_Critter", None)
                if opp_val is None:
                    setattr(value, "shr5_Critter", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5_CritterKraft101(self):
        return self.__shr5_CritterKraft101

    @shr5_CritterKraft101.setter
    def shr5_CritterKraft101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_CritterKraft__shr5_CritterKraft101", None)
        self.__shr5_CritterKraft101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Geist100"):
                opp_val = getattr(old_value, "shr5_Geist100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Geist100"):
                opp_val = getattr(value, "shr5_Geist100", None)
                if opp_val is None:
                    setattr(value, "shr5_Geist100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5_CritterKraft98(self):
        return self.__shr5_CritterKraft98

    @shr5_CritterKraft98.setter
    def shr5_CritterKraft98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_CritterKraft__shr5_CritterKraft98", None)
        self.__shr5_CritterKraft98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Geist97"):
                opp_val = getattr(old_value, "shr5_Geist97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Geist97"):
                opp_val = getattr(value, "shr5_Geist97", None)
                if opp_val is None:
                    setattr(value, "shr5_Geist97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5_KiKraft(Erlernbar, MagischeMods):

    def __init__(self, kraftpunkte: int, shr5_KiKraft: "shr5_KiAdept" = None, shr5_KiKraft138: "shr5_QiFokus" = None):
        self.kraftpunkte = kraftpunkte
        self.shr5_KiKraft = shr5_KiKraft
        self.shr5_KiKraft138 = shr5_KiKraft138
        
    @property
    def kraftpunkte(self) -> int:
        return self.__kraftpunkte

    @kraftpunkte.setter
    def kraftpunkte(self, kraftpunkte: int):
        self.__kraftpunkte = kraftpunkte

    @property
    def shr5_KiKraft138(self):
        return self.__shr5_KiKraft138

    @shr5_KiKraft138.setter
    def shr5_KiKraft138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_KiKraft__shr5_KiKraft138", None)
        self.__shr5_KiKraft138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_QiFokus"):
                opp_val = getattr(old_value, "shr5_QiFokus", None)
                if opp_val == self:
                    setattr(old_value, "shr5_QiFokus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_QiFokus"):
                opp_val = getattr(value, "shr5_QiFokus", None)
                setattr(value, "shr5_QiFokus", self)

    @property
    def shr5_KiKraft(self):
        return self.__shr5_KiKraft

    @shr5_KiKraft.setter
    def shr5_KiKraft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_KiKraft__shr5_KiKraft", None)
        self.__shr5_KiKraft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_KiAdept"):
                opp_val = getattr(old_value, "shr5_KiAdept", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_KiAdept"):
                opp_val = getattr(value, "shr5_KiAdept", None)
                if opp_val is None:
                    setattr(value, "shr5_KiAdept", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BerechneteAttribute:

    pass
class PersonaZustand:

    pass
class Panzerung:

    pass
class AbstraktPersona:

    pass
class shr5_KoerperPersona(PersonaZustand, Panzerung, BerechneteAttribute, AbstraktPersona):

    def __init__(self, zustandKoerperlich: int, zustandGeistig: int, shr5_KoerperPersona: set["shr5_Koerpermods"] = None, shr5_KoerperPersona42: set["shr5_PersonaEigenschaft"] = None):
        self.zustandKoerperlich = zustandKoerperlich
        self.zustandGeistig = zustandGeistig
        self.shr5_KoerperPersona = shr5_KoerperPersona if shr5_KoerperPersona is not None else set()
        self.shr5_KoerperPersona42 = shr5_KoerperPersona42 if shr5_KoerperPersona42 is not None else set()
        
    @property
    def zustandKoerperlich(self) -> int:
        return self.__zustandKoerperlich

    @zustandKoerperlich.setter
    def zustandKoerperlich(self, zustandKoerperlich: int):
        self.__zustandKoerperlich = zustandKoerperlich

    @property
    def zustandGeistig(self) -> int:
        return self.__zustandGeistig

    @zustandGeistig.setter
    def zustandGeistig(self, zustandGeistig: int):
        self.__zustandGeistig = zustandGeistig

    @property
    def shr5_KoerperPersona42(self):
        return self.__shr5_KoerperPersona42

    @shr5_KoerperPersona42.setter
    def shr5_KoerperPersona42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_KoerperPersona__shr5_KoerperPersona42", None)
        self.__shr5_KoerperPersona42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_PersonaEigenschaft"):
                    opp_val = getattr(item, "shr5_PersonaEigenschaft", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_PersonaEigenschaft", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_PersonaEigenschaft"):
                    opp_val = getattr(item, "shr5_PersonaEigenschaft", None)
                    
                    setattr(item, "shr5_PersonaEigenschaft", self)
                    

    @property
    def shr5_KoerperPersona(self):
        return self.__shr5_KoerperPersona

    @shr5_KoerperPersona.setter
    def shr5_KoerperPersona(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_KoerperPersona__shr5_KoerperPersona", None)
        self.__shr5_KoerperPersona = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_Koerpermods"):
                    opp_val = getattr(item, "shr5_Koerpermods", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_Koerpermods", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_Koerpermods"):
                    opp_val = getattr(item, "shr5_Koerpermods", None)
                    
                    setattr(item, "shr5_Koerpermods", self)
                    

class KoerperPersona:

    pass
class shr5_Technomancer(ResonanzPersona, KoerperPersona):

    pass
class shr5_MagischePersona(BaseMagischePersona, KoerperPersona):

    pass
class shr5_MudanPersona(KoerperPersona):

    pass
class AbstraktModifikatoren:

    pass
class shr5_Echo(AbstraktModifikatoren):

    pass
class shr5_PersonaEigenschaft(Erlernbar, AbstraktModifikatoren):

    def __init__(self, karmaKosten: int, shr5_PersonaEigenschaft: "shr5_KoerperPersona" = None):
        self.karmaKosten = karmaKosten
        self.shr5_PersonaEigenschaft = shr5_PersonaEigenschaft
        
    @property
    def karmaKosten(self) -> int:
        return self.__karmaKosten

    @karmaKosten.setter
    def karmaKosten(self, karmaKosten: int):
        self.__karmaKosten = karmaKosten

    @property
    def shr5_PersonaEigenschaft(self):
        return self.__shr5_PersonaEigenschaft

    @shr5_PersonaEigenschaft.setter
    def shr5_PersonaEigenschaft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_PersonaEigenschaft__shr5_PersonaEigenschaft", None)
        self.__shr5_PersonaEigenschaft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_KoerperPersona42"):
                opp_val = getattr(old_value, "shr5_KoerperPersona42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_KoerperPersona42"):
                opp_val = getattr(value, "shr5_KoerperPersona42", None)
                if opp_val is None:
                    setattr(value, "shr5_KoerperPersona42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5_MagischeMods(AbstraktModifikatoren):

    pass
class shr5_Koerpermods(AbstraktModifikatoren):

    pass
class shr5_DefaultWifi(AbstractMatrixDevice):

    pass
class Capacity:

    pass
class shr5_Cyberdeck(MatrixDevice, AbstractMatrixDevice, ActiveMatixDevice, Capacity):

    def __init__(self, programSlots: int, attribute1: int, attribute2: int, attribute3: int, attribute4: int, modManager: str, shr5_Cyberdeck: set["shr5_EAttribute"] = None, shr5_Cyberdeck110: set["shr5_MatrixProgram"] = None, shr5_Cyberdeck112: set["shr5_MatrixProgram"] = None):
        self.programSlots = programSlots
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.attribute4 = attribute4
        self.modManager = modManager
        self.shr5_Cyberdeck = shr5_Cyberdeck if shr5_Cyberdeck is not None else set()
        self.shr5_Cyberdeck110 = shr5_Cyberdeck110 if shr5_Cyberdeck110 is not None else set()
        self.shr5_Cyberdeck112 = shr5_Cyberdeck112 if shr5_Cyberdeck112 is not None else set()
        
    @property
    def attribute1(self) -> int:
        return self.__attribute1

    @attribute1.setter
    def attribute1(self, attribute1: int):
        self.__attribute1 = attribute1

    @property
    def modManager(self) -> str:
        return self.__modManager

    @modManager.setter
    def modManager(self, modManager: str):
        self.__modManager = modManager

    @property
    def programSlots(self) -> int:
        return self.__programSlots

    @programSlots.setter
    def programSlots(self, programSlots: int):
        self.__programSlots = programSlots

    @property
    def attribute2(self) -> int:
        return self.__attribute2

    @attribute2.setter
    def attribute2(self, attribute2: int):
        self.__attribute2 = attribute2

    @property
    def attribute4(self) -> int:
        return self.__attribute4

    @attribute4.setter
    def attribute4(self, attribute4: int):
        self.__attribute4 = attribute4

    @property
    def attribute3(self) -> int:
        return self.__attribute3

    @attribute3.setter
    def attribute3(self, attribute3: int):
        self.__attribute3 = attribute3

    @property
    def shr5_Cyberdeck112(self):
        return self.__shr5_Cyberdeck112

    @shr5_Cyberdeck112.setter
    def shr5_Cyberdeck112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Cyberdeck__shr5_Cyberdeck112", None)
        self.__shr5_Cyberdeck112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_MatrixProgram113"):
                    opp_val = getattr(item, "shr5_MatrixProgram113", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_MatrixProgram113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_MatrixProgram113"):
                    opp_val = getattr(item, "shr5_MatrixProgram113", None)
                    
                    setattr(item, "shr5_MatrixProgram113", self)
                    

    @property
    def shr5_Cyberdeck(self):
        return self.__shr5_Cyberdeck

    @shr5_Cyberdeck.setter
    def shr5_Cyberdeck(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Cyberdeck__shr5_Cyberdeck", None)
        self.__shr5_Cyberdeck = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_EAttribute108"):
                    opp_val = getattr(item, "shr5_EAttribute108", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_EAttribute108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_EAttribute108"):
                    opp_val = getattr(item, "shr5_EAttribute108", None)
                    
                    setattr(item, "shr5_EAttribute108", self)
                    

    @property
    def shr5_Cyberdeck110(self):
        return self.__shr5_Cyberdeck110

    @shr5_Cyberdeck110.setter
    def shr5_Cyberdeck110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Cyberdeck__shr5_Cyberdeck110", None)
        self.__shr5_Cyberdeck110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_MatrixProgram"):
                    opp_val = getattr(item, "shr5_MatrixProgram", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_MatrixProgram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_MatrixProgram"):
                    opp_val = getattr(item, "shr5_MatrixProgram", None)
                    
                    setattr(item, "shr5_MatrixProgram", self)
                    

class Koerpermods:

    pass
class Steigerbar:

    pass
class shr5_Initation(Steigerbar):

    pass
class Modifyable:

    pass
class shr5_EObject:

    pass
class Menge:

    pass
class AbstaktFernKampfwaffe:

    pass
class shr5_Wurfwaffe(Menge, AbstaktFernKampfwaffe):

    pass
class shr5_Projektilwaffe(AbstaktFernKampfwaffe):

    pass
class shr5_Feuerwaffe(AbstaktFernKampfwaffe):

    def __init__(self, munitionstyp: str, modie: str, kapazitaet: int, erweiterung: str, rueckstoss: int, shr5_Feuerwaffe: set["shr5_FernkampfwaffeModifikator"] = None, shr5_Feuerwaffe17: "shr5_Magazin" = None, shr5_Feuerwaffe143: "shr5_Magazin" = None):
        self.munitionstyp = munitionstyp
        self.modie = modie
        self.kapazitaet = kapazitaet
        self.erweiterung = erweiterung
        self.rueckstoss = rueckstoss
        self.shr5_Feuerwaffe = shr5_Feuerwaffe if shr5_Feuerwaffe is not None else set()
        self.shr5_Feuerwaffe17 = shr5_Feuerwaffe17
        self.shr5_Feuerwaffe143 = shr5_Feuerwaffe143
        
    @property
    def kapazitaet(self) -> int:
        return self.__kapazitaet

    @kapazitaet.setter
    def kapazitaet(self, kapazitaet: int):
        self.__kapazitaet = kapazitaet

    @property
    def rueckstoss(self) -> int:
        return self.__rueckstoss

    @rueckstoss.setter
    def rueckstoss(self, rueckstoss: int):
        self.__rueckstoss = rueckstoss

    @property
    def munitionstyp(self) -> str:
        return self.__munitionstyp

    @munitionstyp.setter
    def munitionstyp(self, munitionstyp: str):
        self.__munitionstyp = munitionstyp

    @property
    def modie(self) -> str:
        return self.__modie

    @modie.setter
    def modie(self, modie: str):
        self.__modie = modie

    @property
    def erweiterung(self) -> str:
        return self.__erweiterung

    @erweiterung.setter
    def erweiterung(self, erweiterung: str):
        self.__erweiterung = erweiterung

    @property
    def shr5_Feuerwaffe143(self):
        return self.__shr5_Feuerwaffe143

    @shr5_Feuerwaffe143.setter
    def shr5_Feuerwaffe143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Feuerwaffe__shr5_Feuerwaffe143", None)
        self.__shr5_Feuerwaffe143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Magazin142"):
                opp_val = getattr(old_value, "shr5_Magazin142", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Magazin142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Magazin142"):
                opp_val = getattr(value, "shr5_Magazin142", None)
                setattr(value, "shr5_Magazin142", self)

    @property
    def shr5_Feuerwaffe(self):
        return self.__shr5_Feuerwaffe

    @shr5_Feuerwaffe.setter
    def shr5_Feuerwaffe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Feuerwaffe__shr5_Feuerwaffe", None)
        self.__shr5_Feuerwaffe = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_FernkampfwaffeModifikator"):
                    opp_val = getattr(item, "shr5_FernkampfwaffeModifikator", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_FernkampfwaffeModifikator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_FernkampfwaffeModifikator"):
                    opp_val = getattr(item, "shr5_FernkampfwaffeModifikator", None)
                    
                    setattr(item, "shr5_FernkampfwaffeModifikator", self)
                    

    @property
    def shr5_Feuerwaffe17(self):
        return self.__shr5_Feuerwaffe17

    @shr5_Feuerwaffe17.setter
    def shr5_Feuerwaffe17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Feuerwaffe__shr5_Feuerwaffe17", None)
        self.__shr5_Feuerwaffe17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Magazin"):
                opp_val = getattr(old_value, "shr5_Magazin", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Magazin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Magazin"):
                opp_val = getattr(value, "shr5_Magazin", None)
                setattr(value, "shr5_Magazin", self)

class AbstaktWaffe:

    pass
class shr5_Nahkampfwaffe(AbstaktWaffe):

    def __init__(self, reichweite: int, shr5_Nahkampfwaffe: "shr5_Spezies" = None):
        self.reichweite = reichweite
        self.shr5_Nahkampfwaffe = shr5_Nahkampfwaffe
        
    @property
    def reichweite(self) -> int:
        return self.__reichweite

    @reichweite.setter
    def reichweite(self, reichweite: int):
        self.__reichweite = reichweite

    @property
    def shr5_Nahkampfwaffe(self):
        return self.__shr5_Nahkampfwaffe

    @shr5_Nahkampfwaffe.setter
    def shr5_Nahkampfwaffe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Nahkampfwaffe__shr5_Nahkampfwaffe", None)
        self.__shr5_Nahkampfwaffe = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Spezies48"):
                opp_val = getattr(old_value, "shr5_Spezies48", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Spezies48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Spezies48"):
                opp_val = getattr(value, "shr5_Spezies48", None)
                setattr(value, "shr5_Spezies48", self)

class shr5_AbstaktFernKampfwaffe(AbstaktWaffe):

    pass
class shr5_MatrixDevice(MatrixAttributes):

    pass
class Anwendbar:

    pass
class Modifizierbar:

    pass
class shr5_Drug(Substance, Modifizierbar):

    def __init__(self, addictionType: str, duration: str):
        self.addictionType = addictionType
        self.duration = duration
        
    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def addictionType(self) -> str:
        return self.__addictionType

    @addictionType.setter
    def addictionType(self, addictionType: str):
        self.__addictionType = addictionType

class shr5_MatrixProgram(Software, Modifizierbar):

    pass
class GeldWert:

    pass
class shr5_CyberwareEnhancement(GeldWert, AbstraktModifikatoren):

    def __init__(self, capacityUse: int, type: str, shr5_CyberwareEnhancement: "shr5_Cyberware" = None):
        self.capacityUse = capacityUse
        self.type = type
        self.shr5_CyberwareEnhancement = shr5_CyberwareEnhancement
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def capacityUse(self) -> int:
        return self.__capacityUse

    @capacityUse.setter
    def capacityUse(self, capacityUse: int):
        self.__capacityUse = capacityUse

    @property
    def shr5_CyberwareEnhancement(self):
        return self.__shr5_CyberwareEnhancement

    @shr5_CyberwareEnhancement.setter
    def shr5_CyberwareEnhancement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_CyberwareEnhancement__shr5_CyberwareEnhancement", None)
        self.__shr5_CyberwareEnhancement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Cyberware35"):
                opp_val = getattr(old_value, "shr5_Cyberware35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Cyberware35"):
                opp_val = getattr(value, "shr5_Cyberware35", None)
                if opp_val is None:
                    setattr(value, "shr5_Cyberware35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5_FernkampfwaffeModifikator(GeldWert, AbstraktModifikatoren):

    def __init__(self, ep: str, shr5_FernkampfwaffeModifikator: "shr5_Feuerwaffe" = None):
        self.ep = ep
        self.shr5_FernkampfwaffeModifikator = shr5_FernkampfwaffeModifikator
        
    @property
    def ep(self) -> str:
        return self.__ep

    @ep.setter
    def ep(self, ep: str):
        self.__ep = ep

    @property
    def shr5_FernkampfwaffeModifikator(self):
        return self.__shr5_FernkampfwaffeModifikator

    @shr5_FernkampfwaffeModifikator.setter
    def shr5_FernkampfwaffeModifikator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_FernkampfwaffeModifikator__shr5_FernkampfwaffeModifikator", None)
        self.__shr5_FernkampfwaffeModifikator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Feuerwaffe"):
                opp_val = getattr(old_value, "shr5_Feuerwaffe", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Feuerwaffe"):
                opp_val = getattr(value, "shr5_Feuerwaffe", None)
                if opp_val is None:
                    setattr(value, "shr5_Feuerwaffe", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5_Cyberware(Koerpermods, GeldWert, Capacity):

    def __init__(self, cyberwareCapacity: int, type: str, shr5_Cyberware: "shr5_AbstraktPersona" = None, shr5_Cyberware35: set["shr5_CyberwareEnhancement"] = None, shr5_Cyberware37: set["shr5_DefaultWifi"] = None):
        self.cyberwareCapacity = cyberwareCapacity
        self.type = type
        self.shr5_Cyberware = shr5_Cyberware
        self.shr5_Cyberware35 = shr5_Cyberware35 if shr5_Cyberware35 is not None else set()
        self.shr5_Cyberware37 = shr5_Cyberware37 if shr5_Cyberware37 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def cyberwareCapacity(self) -> int:
        return self.__cyberwareCapacity

    @cyberwareCapacity.setter
    def cyberwareCapacity(self, cyberwareCapacity: int):
        self.__cyberwareCapacity = cyberwareCapacity

    @property
    def shr5_Cyberware(self):
        return self.__shr5_Cyberware

    @shr5_Cyberware.setter
    def shr5_Cyberware(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Cyberware__shr5_Cyberware", None)
        self.__shr5_Cyberware = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_AbstraktPersona33"):
                opp_val = getattr(old_value, "shr5_AbstraktPersona33", None)
                if opp_val == self:
                    setattr(old_value, "shr5_AbstraktPersona33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_AbstraktPersona33"):
                opp_val = getattr(value, "shr5_AbstraktPersona33", None)
                setattr(value, "shr5_AbstraktPersona33", self)

    @property
    def shr5_Cyberware37(self):
        return self.__shr5_Cyberware37

    @shr5_Cyberware37.setter
    def shr5_Cyberware37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Cyberware__shr5_Cyberware37", None)
        self.__shr5_Cyberware37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_DefaultWifi"):
                    opp_val = getattr(item, "shr5_DefaultWifi", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_DefaultWifi", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_DefaultWifi"):
                    opp_val = getattr(item, "shr5_DefaultWifi", None)
                    
                    setattr(item, "shr5_DefaultWifi", self)
                    

    @property
    def shr5_Cyberware35(self):
        return self.__shr5_Cyberware35

    @shr5_Cyberware35.setter
    def shr5_Cyberware35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Cyberware__shr5_Cyberware35", None)
        self.__shr5_Cyberware35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_CyberwareEnhancement"):
                    opp_val = getattr(item, "shr5_CyberwareEnhancement", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_CyberwareEnhancement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_CyberwareEnhancement"):
                    opp_val = getattr(item, "shr5_CyberwareEnhancement", None)
                    
                    setattr(item, "shr5_CyberwareEnhancement", self)
                    

class shr5_BioWare(Koerpermods, GeldWert):

    pass
class Quelle:

    pass
class shr5_GeldWert(ABC):

    def __init__(self, wert: str, verfuegbarkeit: str, wertValue: str, shr5_GeldWert: "shr5_ShoppingTransaction" = None):
        self.wert = wert
        self.verfuegbarkeit = verfuegbarkeit
        self.wertValue = wertValue
        self.shr5_GeldWert = shr5_GeldWert
        
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
    def wertValue(self) -> str:
        return self.__wertValue

    @wertValue.setter
    def wertValue(self, wertValue: str):
        self.__wertValue = wertValue

    @property
    def shr5_GeldWert(self):
        return self.__shr5_GeldWert

    @shr5_GeldWert.setter
    def shr5_GeldWert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_GeldWert__shr5_GeldWert", None)
        self.__shr5_GeldWert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_ShoppingTransaction"):
                opp_val = getattr(old_value, "shr5_ShoppingTransaction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_ShoppingTransaction"):
                opp_val = getattr(value, "shr5_ShoppingTransaction", None)
                if opp_val is None:
                    setattr(value, "shr5_ShoppingTransaction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ModifikatorAttribute:

    pass
class shr5_SpezielleAttribute(ModifikatorAttribute):

    def __init__(self, initative: int, initativWuerfel: int, ausweichen: int, essenz: int, edgeBasis: int, edge: int):
        self.initative = initative
        self.initativWuerfel = initativWuerfel
        self.ausweichen = ausweichen
        self.essenz = essenz
        self.edgeBasis = edgeBasis
        self.edge = edge
        
    @property
    def edgeBasis(self) -> int:
        return self.__edgeBasis

    @edgeBasis.setter
    def edgeBasis(self, edgeBasis: int):
        self.__edgeBasis = edgeBasis

    @property
    def initative(self) -> int:
        return self.__initative

    @initative.setter
    def initative(self, initative: int):
        self.__initative = initative

    @property
    def initativWuerfel(self) -> int:
        return self.__initativWuerfel

    @initativWuerfel.setter
    def initativWuerfel(self, initativWuerfel: int):
        self.__initativWuerfel = initativWuerfel

    @property
    def ausweichen(self) -> int:
        return self.__ausweichen

    @ausweichen.setter
    def ausweichen(self, ausweichen: int):
        self.__ausweichen = ausweichen

    @property
    def essenz(self) -> int:
        return self.__essenz

    @essenz.setter
    def essenz(self, essenz: int):
        self.__essenz = essenz

    @property
    def edge(self) -> int:
        return self.__edge

    @edge.setter
    def edge(self, edge: int):
        self.__edge = edge

class shr5_ProbenModifikatoren(ModifikatorAttribute):

    def __init__(self, schadenswiederstand: int, heilung: int):
        self.schadenswiederstand = schadenswiederstand
        self.heilung = heilung
        
    @property
    def schadenswiederstand(self) -> int:
        return self.__schadenswiederstand

    @schadenswiederstand.setter
    def schadenswiederstand(self, schadenswiederstand: int):
        self.__schadenswiederstand = schadenswiederstand

    @property
    def heilung(self) -> int:
        return self.__heilung

    @heilung.setter
    def heilung(self, heilung: int):
        self.__heilung = heilung

class shr5_FernkampfwaffenModifikatoren(ModifikatorAttribute):

    def __init__(self, rueckstoss: int, lasterPointer: bool, schalldaempfer: bool, vergroesserung: int, sichtverbesserung: int, smartgun: str):
        self.rueckstoss = rueckstoss
        self.lasterPointer = lasterPointer
        self.schalldaempfer = schalldaempfer
        self.vergroesserung = vergroesserung
        self.sichtverbesserung = sichtverbesserung
        self.smartgun = smartgun
        
    @property
    def schalldaempfer(self) -> bool:
        return self.__schalldaempfer

    @schalldaempfer.setter
    def schalldaempfer(self, schalldaempfer: bool):
        self.__schalldaempfer = schalldaempfer

    @property
    def rueckstoss(self) -> int:
        return self.__rueckstoss

    @rueckstoss.setter
    def rueckstoss(self, rueckstoss: int):
        self.__rueckstoss = rueckstoss

    @property
    def smartgun(self) -> str:
        return self.__smartgun

    @smartgun.setter
    def smartgun(self, smartgun: str):
        self.__smartgun = smartgun

    @property
    def sichtverbesserung(self) -> int:
        return self.__sichtverbesserung

    @sichtverbesserung.setter
    def sichtverbesserung(self, sichtverbesserung: int):
        self.__sichtverbesserung = sichtverbesserung

    @property
    def vergroesserung(self) -> int:
        return self.__vergroesserung

    @vergroesserung.setter
    def vergroesserung(self, vergroesserung: int):
        self.__vergroesserung = vergroesserung

    @property
    def lasterPointer(self) -> bool:
        return self.__lasterPointer

    @lasterPointer.setter
    def lasterPointer(self, lasterPointer: bool):
        self.__lasterPointer = lasterPointer

class shr5_Sichtverhaeltnisse(ModifikatorAttribute):

    def __init__(self, restlichtverstaerkung: str, infrarot: str, ultrasound: str):
        self.restlichtverstaerkung = restlichtverstaerkung
        self.infrarot = infrarot
        self.ultrasound = ultrasound
        
    @property
    def infrarot(self) -> str:
        return self.__infrarot

    @infrarot.setter
    def infrarot(self, infrarot: str):
        self.__infrarot = infrarot

    @property
    def ultrasound(self) -> str:
        return self.__ultrasound

    @ultrasound.setter
    def ultrasound(self, ultrasound: str):
        self.__ultrasound = ultrasound

    @property
    def restlichtverstaerkung(self) -> str:
        return self.__restlichtverstaerkung

    @restlichtverstaerkung.setter
    def restlichtverstaerkung(self, restlichtverstaerkung: str):
        self.__restlichtverstaerkung = restlichtverstaerkung

class shr5_GeistigeAttribute(ModifikatorAttribute):

    def __init__(self, charisma: int, willenskraft: int, intuition: int, logik: int):
        self.charisma = charisma
        self.willenskraft = willenskraft
        self.intuition = intuition
        self.logik = logik
        
    @property
    def willenskraft(self) -> int:
        return self.__willenskraft

    @willenskraft.setter
    def willenskraft(self, willenskraft: int):
        self.__willenskraft = willenskraft

    @property
    def logik(self) -> int:
        return self.__logik

    @logik.setter
    def logik(self, logik: int):
        self.__logik = logik

    @property
    def charisma(self) -> int:
        return self.__charisma

    @charisma.setter
    def charisma(self, charisma: int):
        self.__charisma = charisma

    @property
    def intuition(self) -> int:
        return self.__intuition

    @intuition.setter
    def intuition(self, intuition: int):
        self.__intuition = intuition

class shr5_CyberwareModifikatioren(ModifikatorAttribute):

    def __init__(self, simRig: int, riggerInterface: bool, directNeuralInterface: bool, universalDataConnector: bool, controlRig: int):
        self.simRig = simRig
        self.riggerInterface = riggerInterface
        self.directNeuralInterface = directNeuralInterface
        self.universalDataConnector = universalDataConnector
        self.controlRig = controlRig
        
    @property
    def riggerInterface(self) -> bool:
        return self.__riggerInterface

    @riggerInterface.setter
    def riggerInterface(self, riggerInterface: bool):
        self.__riggerInterface = riggerInterface

    @property
    def simRig(self) -> int:
        return self.__simRig

    @simRig.setter
    def simRig(self, simRig: int):
        self.__simRig = simRig

    @property
    def directNeuralInterface(self) -> bool:
        return self.__directNeuralInterface

    @directNeuralInterface.setter
    def directNeuralInterface(self, directNeuralInterface: bool):
        self.__directNeuralInterface = directNeuralInterface

    @property
    def controlRig(self) -> int:
        return self.__controlRig

    @controlRig.setter
    def controlRig(self, controlRig: int):
        self.__controlRig = controlRig

    @property
    def universalDataConnector(self) -> bool:
        return self.__universalDataConnector

    @universalDataConnector.setter
    def universalDataConnector(self, universalDataConnector: bool):
        self.__universalDataConnector = universalDataConnector

class shr5_GegenstandStufen(ModifikatorAttribute):

    def __init__(self, computer: int, elektronik: int, tracing: int, antiTracing: int, protection: int, antiProtection: int):
        self.computer = computer
        self.elektronik = elektronik
        self.tracing = tracing
        self.antiTracing = antiTracing
        self.protection = protection
        self.antiProtection = antiProtection
        
    @property
    def antiTracing(self) -> int:
        return self.__antiTracing

    @antiTracing.setter
    def antiTracing(self, antiTracing: int):
        self.__antiTracing = antiTracing

    @property
    def tracing(self) -> int:
        return self.__tracing

    @tracing.setter
    def tracing(self, tracing: int):
        self.__tracing = tracing

    @property
    def elektronik(self) -> int:
        return self.__elektronik

    @elektronik.setter
    def elektronik(self, elektronik: int):
        self.__elektronik = elektronik

    @property
    def protection(self) -> int:
        return self.__protection

    @protection.setter
    def protection(self, protection: int):
        self.__protection = protection

    @property
    def antiProtection(self) -> int:
        return self.__antiProtection

    @antiProtection.setter
    def antiProtection(self, antiProtection: int):
        self.__antiProtection = antiProtection

    @property
    def computer(self) -> int:
        return self.__computer

    @computer.setter
    def computer(self, computer: int):
        self.__computer = computer

class shr5_KoerperlicheAttribute(ModifikatorAttribute):

    def __init__(self, konstitution: int, geschicklichkeit: int, reaktion: int, staerke: int):
        self.konstitution = konstitution
        self.geschicklichkeit = geschicklichkeit
        self.reaktion = reaktion
        self.staerke = staerke
        
    @property
    def geschicklichkeit(self) -> int:
        return self.__geschicklichkeit

    @geschicklichkeit.setter
    def geschicklichkeit(self, geschicklichkeit: int):
        self.__geschicklichkeit = geschicklichkeit

    @property
    def reaktion(self) -> int:
        return self.__reaktion

    @reaktion.setter
    def reaktion(self, reaktion: int):
        self.__reaktion = reaktion

    @property
    def staerke(self) -> int:
        return self.__staerke

    @staerke.setter
    def staerke(self, staerke: int):
        self.__staerke = staerke

    @property
    def konstitution(self) -> int:
        return self.__konstitution

    @konstitution.setter
    def konstitution(self, konstitution: int):
        self.__konstitution = konstitution

class shr5_Modifyable(ABC):

    pass
class shr5_Modifizierbar(ABC):

    pass
class shr5_EAttribute:

    pass
class shr5_AttributModifikatorWert:

    def __init__(self, wert: int, shr5_AttributModifikatorWert: "shr5_EAttribute" = None, mods: "shr5_Modifizierbar" = None, shr5_AttributModifikatorWert11: "shr5_Modifyable" = None, AttributModifikatorWert: "shr5_Modifizierbar" = None):
        self.wert = wert
        self.shr5_AttributModifikatorWert = shr5_AttributModifikatorWert
        self.mods = mods
        self.shr5_AttributModifikatorWert11 = shr5_AttributModifikatorWert11
        self.AttributModifikatorWert = AttributModifikatorWert
        
    @property
    def wert(self) -> int:
        return self.__wert

    @wert.setter
    def wert(self, wert: int):
        self.__wert = wert

    @property
    def shr5_AttributModifikatorWert(self):
        return self.__shr5_AttributModifikatorWert

    @shr5_AttributModifikatorWert.setter
    def shr5_AttributModifikatorWert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AttributModifikatorWert__shr5_AttributModifikatorWert", None)
        self.__shr5_AttributModifikatorWert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_EAttribute"):
                opp_val = getattr(old_value, "shr5_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "shr5_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_EAttribute"):
                opp_val = getattr(value, "shr5_EAttribute", None)
                setattr(value, "shr5_EAttribute", self)

    @property
    def shr5_AttributModifikatorWert11(self):
        return self.__shr5_AttributModifikatorWert11

    @shr5_AttributModifikatorWert11.setter
    def shr5_AttributModifikatorWert11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AttributModifikatorWert__shr5_AttributModifikatorWert11", None)
        self.__shr5_AttributModifikatorWert11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Modifyable"):
                opp_val = getattr(old_value, "shr5_Modifyable", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Modifyable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Modifyable"):
                opp_val = getattr(value, "shr5_Modifyable", None)
                setattr(value, "shr5_Modifyable", self)

    @property
    def mods(self):
        return self.__mods

    @mods.setter
    def mods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AttributModifikatorWert__mods", None)
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
    def AttributModifikatorWert(self):
        return self.__AttributModifikatorWert

    @AttributModifikatorWert.setter
    def AttributModifikatorWert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AttributModifikatorWert__AttributModifikatorWert", None)
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

class AbstraktGegenstand:

    pass
class shr5_SubstanceContainer(AbstraktGegenstand):

    pass
class shr5_AbstraktFokus(AbstraktGegenstand, Fokus):

    pass
class shr5_AbstaktWaffe(AbstraktGegenstand):

    def __init__(self, schadenscode: str, schadesTyp: str, praezision: int, durchschlagsKraft: int, shr5_AbstaktWaffe: "shr5_AutoSoft" = None, shr5_AbstaktWaffe136: "shr5_WeaponMount" = None, shr5_AbstaktWaffe150: "shr5_CyberImplantWeapon" = None):
        self.schadenscode = schadenscode
        self.schadesTyp = schadesTyp
        self.praezision = praezision
        self.durchschlagsKraft = durchschlagsKraft
        self.shr5_AbstaktWaffe = shr5_AbstaktWaffe
        self.shr5_AbstaktWaffe136 = shr5_AbstaktWaffe136
        self.shr5_AbstaktWaffe150 = shr5_AbstaktWaffe150
        
    @property
    def schadenscode(self) -> str:
        return self.__schadenscode

    @schadenscode.setter
    def schadenscode(self, schadenscode: str):
        self.__schadenscode = schadenscode

    @property
    def durchschlagsKraft(self) -> int:
        return self.__durchschlagsKraft

    @durchschlagsKraft.setter
    def durchschlagsKraft(self, durchschlagsKraft: int):
        self.__durchschlagsKraft = durchschlagsKraft

    @property
    def schadesTyp(self) -> str:
        return self.__schadesTyp

    @schadesTyp.setter
    def schadesTyp(self, schadesTyp: str):
        self.__schadesTyp = schadesTyp

    @property
    def praezision(self) -> int:
        return self.__praezision

    @praezision.setter
    def praezision(self, praezision: int):
        self.__praezision = praezision

    @property
    def shr5_AbstaktWaffe150(self):
        return self.__shr5_AbstaktWaffe150

    @shr5_AbstaktWaffe150.setter
    def shr5_AbstaktWaffe150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AbstaktWaffe__shr5_AbstaktWaffe150", None)
        self.__shr5_AbstaktWaffe150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_CyberImplantWeapon"):
                opp_val = getattr(old_value, "shr5_CyberImplantWeapon", None)
                if opp_val == self:
                    setattr(old_value, "shr5_CyberImplantWeapon", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_CyberImplantWeapon"):
                opp_val = getattr(value, "shr5_CyberImplantWeapon", None)
                setattr(value, "shr5_CyberImplantWeapon", self)

    @property
    def shr5_AbstaktWaffe136(self):
        return self.__shr5_AbstaktWaffe136

    @shr5_AbstaktWaffe136.setter
    def shr5_AbstaktWaffe136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AbstaktWaffe__shr5_AbstaktWaffe136", None)
        self.__shr5_AbstaktWaffe136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_WeaponMount"):
                opp_val = getattr(old_value, "shr5_WeaponMount", None)
                if opp_val == self:
                    setattr(old_value, "shr5_WeaponMount", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_WeaponMount"):
                opp_val = getattr(value, "shr5_WeaponMount", None)
                setattr(value, "shr5_WeaponMount", self)

    @property
    def shr5_AbstaktWaffe(self):
        return self.__shr5_AbstaktWaffe

    @shr5_AbstaktWaffe.setter
    def shr5_AbstaktWaffe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AbstaktWaffe__shr5_AbstaktWaffe", None)
        self.__shr5_AbstaktWaffe = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_AutoSoft122"):
                opp_val = getattr(old_value, "shr5_AutoSoft122", None)
                if opp_val == self:
                    setattr(old_value, "shr5_AutoSoft122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_AutoSoft122"):
                opp_val = getattr(value, "shr5_AutoSoft122", None)
                setattr(value, "shr5_AutoSoft122", self)

class shr5_Munition(AbstraktGegenstand, Menge):

    def __init__(self, damageType: str, damageMod: int, armorMod: int, shr5_Munition: "shr5_Reichweite" = None, shr5_Munition146: "shr5_Magazin" = None):
        self.damageType = damageType
        self.damageMod = damageMod
        self.armorMod = armorMod
        self.shr5_Munition = shr5_Munition
        self.shr5_Munition146 = shr5_Munition146
        
    @property
    def damageMod(self) -> int:
        return self.__damageMod

    @damageMod.setter
    def damageMod(self, damageMod: int):
        self.__damageMod = damageMod

    @property
    def damageType(self) -> str:
        return self.__damageType

    @damageType.setter
    def damageType(self, damageType: str):
        self.__damageType = damageType

    @property
    def armorMod(self) -> int:
        return self.__armorMod

    @armorMod.setter
    def armorMod(self, armorMod: int):
        self.__armorMod = armorMod

    @property
    def shr5_Munition146(self):
        return self.__shr5_Munition146

    @shr5_Munition146.setter
    def shr5_Munition146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Munition__shr5_Munition146", None)
        self.__shr5_Munition146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Magazin145"):
                opp_val = getattr(old_value, "shr5_Magazin145", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Magazin145"):
                opp_val = getattr(value, "shr5_Magazin145", None)
                if opp_val is None:
                    setattr(value, "shr5_Magazin145", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5_Munition(self):
        return self.__shr5_Munition

    @shr5_Munition.setter
    def shr5_Munition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Munition__shr5_Munition", None)
        self.__shr5_Munition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Reichweite88"):
                opp_val = getattr(old_value, "shr5_Reichweite88", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Reichweite88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Reichweite88"):
                opp_val = getattr(value, "shr5_Reichweite88", None)
                setattr(value, "shr5_Reichweite88", self)

class shr5_Magazin(AbstraktGegenstand, Capacity):

    pass
class shr5_AbstractMatrixDevice(AbstraktGegenstand, MatrixDevice):

    def __init__(self, deviceRating: int):
        self.deviceRating = deviceRating
        
    @property
    def deviceRating(self) -> int:
        return self.__deviceRating

    @deviceRating.setter
    def deviceRating(self, deviceRating: int):
        self.__deviceRating = deviceRating

class shr5_Kleidung(AbstraktGegenstand, Capacity):

    def __init__(self, ruestung: int, shr5_Kleidung: set["shr5_KleindungsModifikator"] = None):
        self.ruestung = ruestung
        self.shr5_Kleidung = shr5_Kleidung if shr5_Kleidung is not None else set()
        
    @property
    def ruestung(self) -> int:
        return self.__ruestung

    @ruestung.setter
    def ruestung(self, ruestung: int):
        self.__ruestung = ruestung

    @property
    def shr5_Kleidung(self):
        return self.__shr5_Kleidung

    @shr5_Kleidung.setter
    def shr5_Kleidung(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Kleidung__shr5_Kleidung", None)
        self.__shr5_Kleidung = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_KleindungsModifikator"):
                    opp_val = getattr(item, "shr5_KleindungsModifikator", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_KleindungsModifikator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_KleindungsModifikator"):
                    opp_val = getattr(item, "shr5_KleindungsModifikator", None)
                    
                    setattr(item, "shr5_KleindungsModifikator", self)
                    

class shr5_Credstick(AbstraktGegenstand):

    def __init__(self, maxValue: int, currentValue: str, shr5_Credstick: set["shr5_CredstickTransaction"] = None, shr5_Credstick156: "shr5_TransferAmount" = None, shr5_Credstick159: "shr5_TransferAmount" = None):
        self.maxValue = maxValue
        self.currentValue = currentValue
        self.shr5_Credstick = shr5_Credstick if shr5_Credstick is not None else set()
        self.shr5_Credstick156 = shr5_Credstick156
        self.shr5_Credstick159 = shr5_Credstick159
        
    @property
    def currentValue(self) -> str:
        return self.__currentValue

    @currentValue.setter
    def currentValue(self, currentValue: str):
        self.__currentValue = currentValue

    @property
    def maxValue(self) -> int:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: int):
        self.__maxValue = maxValue

    @property
    def shr5_Credstick(self):
        return self.__shr5_Credstick

    @shr5_Credstick.setter
    def shr5_Credstick(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Credstick__shr5_Credstick", None)
        self.__shr5_Credstick = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_CredstickTransaction"):
                    opp_val = getattr(item, "shr5_CredstickTransaction", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_CredstickTransaction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_CredstickTransaction"):
                    opp_val = getattr(item, "shr5_CredstickTransaction", None)
                    
                    setattr(item, "shr5_CredstickTransaction", self)
                    

    @property
    def shr5_Credstick156(self):
        return self.__shr5_Credstick156

    @shr5_Credstick156.setter
    def shr5_Credstick156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Credstick__shr5_Credstick156", None)
        self.__shr5_Credstick156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_TransferAmount"):
                opp_val = getattr(old_value, "shr5_TransferAmount", None)
                if opp_val == self:
                    setattr(old_value, "shr5_TransferAmount", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_TransferAmount"):
                opp_val = getattr(value, "shr5_TransferAmount", None)
                setattr(value, "shr5_TransferAmount", self)

    @property
    def shr5_Credstick159(self):
        return self.__shr5_Credstick159

    @shr5_Credstick159.setter
    def shr5_Credstick159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Credstick__shr5_Credstick159", None)
        self.__shr5_Credstick159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_TransferAmount158"):
                opp_val = getattr(old_value, "shr5_TransferAmount158", None)
                if opp_val == self:
                    setattr(old_value, "shr5_TransferAmount158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_TransferAmount158"):
                opp_val = getattr(value, "shr5_TransferAmount158", None)
                setattr(value, "shr5_TransferAmount158", self)

class shr5_Gegenstand(AbstraktGegenstand):

    def __init__(self, kategorie: str, stufe: int):
        self.kategorie = kategorie
        self.stufe = stufe
        
    @property
    def kategorie(self) -> str:
        return self.__kategorie

    @kategorie.setter
    def kategorie(self, kategorie: str):
        self.__kategorie = kategorie

    @property
    def stufe(self) -> int:
        return self.__stufe

    @stufe.setter
    def stufe(self, stufe: int):
        self.__stufe = stufe

class shr5_PersonaMartialartStyle(Spezialisierung):

    pass
class shr5_PersonaFertigkeitsGruppe(Steigerbar):

    pass
class shr5_PersonaFertigkeit(Steigerbar):

    pass
class ChrakterLimits:

    pass
class GeistigeAttribute:

    pass
class SpezielleAttribute:

    pass
class KoerperlicheAttribute:

    pass
class Beschreibbar:

    pass
class shr5_AbstraktGegenstand(Anwendbar, Quelle, GeldWert, Modifizierbar, Beschreibbar):

    pass
class shr5_StufenPersona(KoerperlicheAttribute, ChrakterLimits, Quelle, GeistigeAttribute, Panzerung, SpezielleAttribute, Beschreibbar):

    def __init__(self, stufe: int, shr5_StufenPersona: set["shr5_FertigkeitsGruppe"] = None, shr5_StufenPersona94: set["shr5_Fertigkeit"] = None):
        self.stufe = stufe
        self.shr5_StufenPersona = shr5_StufenPersona if shr5_StufenPersona is not None else set()
        self.shr5_StufenPersona94 = shr5_StufenPersona94 if shr5_StufenPersona94 is not None else set()
        
    @property
    def stufe(self) -> int:
        return self.__stufe

    @stufe.setter
    def stufe(self, stufe: int):
        self.__stufe = stufe

    @property
    def shr5_StufenPersona94(self):
        return self.__shr5_StufenPersona94

    @shr5_StufenPersona94.setter
    def shr5_StufenPersona94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_StufenPersona__shr5_StufenPersona94", None)
        self.__shr5_StufenPersona94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_Fertigkeit95"):
                    opp_val = getattr(item, "shr5_Fertigkeit95", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_Fertigkeit95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_Fertigkeit95"):
                    opp_val = getattr(item, "shr5_Fertigkeit95", None)
                    
                    setattr(item, "shr5_Fertigkeit95", self)
                    

    @property
    def shr5_StufenPersona(self):
        return self.__shr5_StufenPersona

    @shr5_StufenPersona.setter
    def shr5_StufenPersona(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_StufenPersona__shr5_StufenPersona", None)
        self.__shr5_StufenPersona = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_FertigkeitsGruppe92"):
                    opp_val = getattr(item, "shr5_FertigkeitsGruppe92", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_FertigkeitsGruppe92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_FertigkeitsGruppe92"):
                    opp_val = getattr(item, "shr5_FertigkeitsGruppe92", None)
                    
                    setattr(item, "shr5_FertigkeitsGruppe92", self)
                    

class shr5_KomplexeForm(Quelle, Beschreibbar):

    def __init__(self, ziel: str, dauer: str, schwund: str, shr5_KomplexeForm: "shr5_PersonaKomplexForm" = None):
        self.ziel = ziel
        self.dauer = dauer
        self.schwund = schwund
        self.shr5_KomplexeForm = shr5_KomplexeForm
        
    @property
    def dauer(self) -> str:
        return self.__dauer

    @dauer.setter
    def dauer(self, dauer: str):
        self.__dauer = dauer

    @property
    def schwund(self) -> str:
        return self.__schwund

    @schwund.setter
    def schwund(self, schwund: str):
        self.__schwund = schwund

    @property
    def ziel(self) -> str:
        return self.__ziel

    @ziel.setter
    def ziel(self, ziel: str):
        self.__ziel = ziel

    @property
    def shr5_KomplexeForm(self):
        return self.__shr5_KomplexeForm

    @shr5_KomplexeForm.setter
    def shr5_KomplexeForm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_KomplexeForm__shr5_KomplexeForm", None)
        self.__shr5_KomplexeForm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_PersonaKomplexForm81"):
                opp_val = getattr(old_value, "shr5_PersonaKomplexForm81", None)
                if opp_val == self:
                    setattr(old_value, "shr5_PersonaKomplexForm81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_PersonaKomplexForm81"):
                opp_val = getattr(value, "shr5_PersonaKomplexForm81", None)
                setattr(value, "shr5_PersonaKomplexForm81", self)

class shr5_Spezies(Quelle, Modifizierbar, Beschreibbar):

    def __init__(self, konstitutionMin: int, geschicklichkeitMin: int, reaktionMin: int, staerkeMin: int, charismaMin: int, willenskraftMin: int, intuitionMin: int, logikMin: int, edgeMin: int, magieMin: int, resonanzMin: int, essenzMin: int, konstitutionMax: int, geschicklichkeitMax: int, reaktionMax: int, staerkeMax: int, charismaMax: int, willenskraftMax: int, intuitionMax: int, logikMax: int, edgeMax: int, magieMax: int, resonanzMax: int, essenzMax: int, laufen: int, rennen: int, sprinten: int, shr5_Spezies: "shr5_AbstraktPersona" = None, shr5_Spezies48: "shr5_Nahkampfwaffe" = None):
        self.konstitutionMin = konstitutionMin
        self.geschicklichkeitMin = geschicklichkeitMin
        self.reaktionMin = reaktionMin
        self.staerkeMin = staerkeMin
        self.charismaMin = charismaMin
        self.willenskraftMin = willenskraftMin
        self.intuitionMin = intuitionMin
        self.logikMin = logikMin
        self.edgeMin = edgeMin
        self.magieMin = magieMin
        self.resonanzMin = resonanzMin
        self.essenzMin = essenzMin
        self.konstitutionMax = konstitutionMax
        self.geschicklichkeitMax = geschicklichkeitMax
        self.reaktionMax = reaktionMax
        self.staerkeMax = staerkeMax
        self.charismaMax = charismaMax
        self.willenskraftMax = willenskraftMax
        self.intuitionMax = intuitionMax
        self.logikMax = logikMax
        self.edgeMax = edgeMax
        self.magieMax = magieMax
        self.resonanzMax = resonanzMax
        self.essenzMax = essenzMax
        self.laufen = laufen
        self.rennen = rennen
        self.sprinten = sprinten
        self.shr5_Spezies = shr5_Spezies
        self.shr5_Spezies48 = shr5_Spezies48
        
    @property
    def staerkeMin(self) -> int:
        return self.__staerkeMin

    @staerkeMin.setter
    def staerkeMin(self, staerkeMin: int):
        self.__staerkeMin = staerkeMin

    @property
    def logikMax(self) -> int:
        return self.__logikMax

    @logikMax.setter
    def logikMax(self, logikMax: int):
        self.__logikMax = logikMax

    @property
    def intuitionMin(self) -> int:
        return self.__intuitionMin

    @intuitionMin.setter
    def intuitionMin(self, intuitionMin: int):
        self.__intuitionMin = intuitionMin

    @property
    def resonanzMin(self) -> int:
        return self.__resonanzMin

    @resonanzMin.setter
    def resonanzMin(self, resonanzMin: int):
        self.__resonanzMin = resonanzMin

    @property
    def rennen(self) -> int:
        return self.__rennen

    @rennen.setter
    def rennen(self, rennen: int):
        self.__rennen = rennen

    @property
    def sprinten(self) -> int:
        return self.__sprinten

    @sprinten.setter
    def sprinten(self, sprinten: int):
        self.__sprinten = sprinten

    @property
    def willenskraftMin(self) -> int:
        return self.__willenskraftMin

    @willenskraftMin.setter
    def willenskraftMin(self, willenskraftMin: int):
        self.__willenskraftMin = willenskraftMin

    @property
    def resonanzMax(self) -> int:
        return self.__resonanzMax

    @resonanzMax.setter
    def resonanzMax(self, resonanzMax: int):
        self.__resonanzMax = resonanzMax

    @property
    def edgeMax(self) -> int:
        return self.__edgeMax

    @edgeMax.setter
    def edgeMax(self, edgeMax: int):
        self.__edgeMax = edgeMax

    @property
    def reaktionMin(self) -> int:
        return self.__reaktionMin

    @reaktionMin.setter
    def reaktionMin(self, reaktionMin: int):
        self.__reaktionMin = reaktionMin

    @property
    def intuitionMax(self) -> int:
        return self.__intuitionMax

    @intuitionMax.setter
    def intuitionMax(self, intuitionMax: int):
        self.__intuitionMax = intuitionMax

    @property
    def charismaMin(self) -> int:
        return self.__charismaMin

    @charismaMin.setter
    def charismaMin(self, charismaMin: int):
        self.__charismaMin = charismaMin

    @property
    def laufen(self) -> int:
        return self.__laufen

    @laufen.setter
    def laufen(self, laufen: int):
        self.__laufen = laufen

    @property
    def geschicklichkeitMin(self) -> int:
        return self.__geschicklichkeitMin

    @geschicklichkeitMin.setter
    def geschicklichkeitMin(self, geschicklichkeitMin: int):
        self.__geschicklichkeitMin = geschicklichkeitMin

    @property
    def staerkeMax(self) -> int:
        return self.__staerkeMax

    @staerkeMax.setter
    def staerkeMax(self, staerkeMax: int):
        self.__staerkeMax = staerkeMax

    @property
    def essenzMax(self) -> int:
        return self.__essenzMax

    @essenzMax.setter
    def essenzMax(self, essenzMax: int):
        self.__essenzMax = essenzMax

    @property
    def willenskraftMax(self) -> int:
        return self.__willenskraftMax

    @willenskraftMax.setter
    def willenskraftMax(self, willenskraftMax: int):
        self.__willenskraftMax = willenskraftMax

    @property
    def essenzMin(self) -> int:
        return self.__essenzMin

    @essenzMin.setter
    def essenzMin(self, essenzMin: int):
        self.__essenzMin = essenzMin

    @property
    def geschicklichkeitMax(self) -> int:
        return self.__geschicklichkeitMax

    @geschicklichkeitMax.setter
    def geschicklichkeitMax(self, geschicklichkeitMax: int):
        self.__geschicklichkeitMax = geschicklichkeitMax

    @property
    def charismaMax(self) -> int:
        return self.__charismaMax

    @charismaMax.setter
    def charismaMax(self, charismaMax: int):
        self.__charismaMax = charismaMax

    @property
    def edgeMin(self) -> int:
        return self.__edgeMin

    @edgeMin.setter
    def edgeMin(self, edgeMin: int):
        self.__edgeMin = edgeMin

    @property
    def konstitutionMax(self) -> int:
        return self.__konstitutionMax

    @konstitutionMax.setter
    def konstitutionMax(self, konstitutionMax: int):
        self.__konstitutionMax = konstitutionMax

    @property
    def konstitutionMin(self) -> int:
        return self.__konstitutionMin

    @konstitutionMin.setter
    def konstitutionMin(self, konstitutionMin: int):
        self.__konstitutionMin = konstitutionMin

    @property
    def magieMax(self) -> int:
        return self.__magieMax

    @magieMax.setter
    def magieMax(self, magieMax: int):
        self.__magieMax = magieMax

    @property
    def reaktionMax(self) -> int:
        return self.__reaktionMax

    @reaktionMax.setter
    def reaktionMax(self, reaktionMax: int):
        self.__reaktionMax = reaktionMax

    @property
    def logikMin(self) -> int:
        return self.__logikMin

    @logikMin.setter
    def logikMin(self, logikMin: int):
        self.__logikMin = logikMin

    @property
    def magieMin(self) -> int:
        return self.__magieMin

    @magieMin.setter
    def magieMin(self, magieMin: int):
        self.__magieMin = magieMin

    @property
    def shr5_Spezies48(self):
        return self.__shr5_Spezies48

    @shr5_Spezies48.setter
    def shr5_Spezies48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Spezies__shr5_Spezies48", None)
        self.__shr5_Spezies48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Nahkampfwaffe"):
                opp_val = getattr(old_value, "shr5_Nahkampfwaffe", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Nahkampfwaffe", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Nahkampfwaffe"):
                opp_val = getattr(value, "shr5_Nahkampfwaffe", None)
                setattr(value, "shr5_Nahkampfwaffe", self)

    @property
    def shr5_Spezies(self):
        return self.__shr5_Spezies

    @shr5_Spezies.setter
    def shr5_Spezies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Spezies__shr5_Spezies", None)
        self.__shr5_Spezies = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_AbstraktPersona5"):
                opp_val = getattr(old_value, "shr5_AbstraktPersona5", None)
                if opp_val == self:
                    setattr(old_value, "shr5_AbstraktPersona5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_AbstraktPersona5"):
                opp_val = getattr(value, "shr5_AbstraktPersona5", None)
                setattr(value, "shr5_AbstraktPersona5", self)

class shr5_Sensor(Beschreibbar, Quelle, GeldWert, Capacity):

    def __init__(self, rating: int, capacityValue: int, shr5_Sensor: set["shr5_SensorFunction"] = None):
        self.rating = rating
        self.capacityValue = capacityValue
        self.shr5_Sensor = shr5_Sensor if shr5_Sensor is not None else set()
        
    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def capacityValue(self) -> int:
        return self.__capacityValue

    @capacityValue.setter
    def capacityValue(self, capacityValue: int):
        self.__capacityValue = capacityValue

    @property
    def shr5_Sensor(self):
        return self.__shr5_Sensor

    @shr5_Sensor.setter
    def shr5_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Sensor__shr5_Sensor", None)
        self.__shr5_Sensor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_SensorFunction"):
                    opp_val = getattr(item, "shr5_SensorFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_SensorFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_SensorFunction"):
                    opp_val = getattr(item, "shr5_SensorFunction", None)
                    
                    setattr(item, "shr5_SensorFunction", self)
                    

class shr5_Sprite(ResonanzPersona, Quelle, Beschreibbar):

    def __init__(self, stufe: int, angriffMod: int, schleicherMod: int, datenverarbeitungMod: int, firewallMod: int, initativeMod: int):
        self.stufe = stufe
        self.angriffMod = angriffMod
        self.schleicherMod = schleicherMod
        self.datenverarbeitungMod = datenverarbeitungMod
        self.firewallMod = firewallMod
        self.initativeMod = initativeMod
        
    @property
    def firewallMod(self) -> int:
        return self.__firewallMod

    @firewallMod.setter
    def firewallMod(self, firewallMod: int):
        self.__firewallMod = firewallMod

    @property
    def datenverarbeitungMod(self) -> int:
        return self.__datenverarbeitungMod

    @datenverarbeitungMod.setter
    def datenverarbeitungMod(self, datenverarbeitungMod: int):
        self.__datenverarbeitungMod = datenverarbeitungMod

    @property
    def initativeMod(self) -> int:
        return self.__initativeMod

    @initativeMod.setter
    def initativeMod(self, initativeMod: int):
        self.__initativeMod = initativeMod

    @property
    def schleicherMod(self) -> int:
        return self.__schleicherMod

    @schleicherMod.setter
    def schleicherMod(self, schleicherMod: int):
        self.__schleicherMod = schleicherMod

    @property
    def angriffMod(self) -> int:
        return self.__angriffMod

    @angriffMod.setter
    def angriffMod(self, angriffMod: int):
        self.__angriffMod = angriffMod

    @property
    def stufe(self) -> int:
        return self.__stufe

    @stufe.setter
    def stufe(self, stufe: int):
        self.__stufe = stufe

class shr5_FertigkeitsGruppe(Quelle, Modifyable, Beschreibbar):

    pass
class shr5_Zauber(Quelle, Beschreibbar):

    def __init__(self, art: str, reichweite: str, schaden: str, dauer: str, entzug: str, kategorie: str, merkmale: str, shr5_Zauber: "shr5_PersonaZauber" = None):
        self.art = art
        self.reichweite = reichweite
        self.schaden = schaden
        self.dauer = dauer
        self.entzug = entzug
        self.kategorie = kategorie
        self.merkmale = merkmale
        self.shr5_Zauber = shr5_Zauber
        
    @property
    def kategorie(self) -> str:
        return self.__kategorie

    @kategorie.setter
    def kategorie(self, kategorie: str):
        self.__kategorie = kategorie

    @property
    def entzug(self) -> str:
        return self.__entzug

    @entzug.setter
    def entzug(self, entzug: str):
        self.__entzug = entzug

    @property
    def merkmale(self) -> str:
        return self.__merkmale

    @merkmale.setter
    def merkmale(self, merkmale: str):
        self.__merkmale = merkmale

    @property
    def dauer(self) -> str:
        return self.__dauer

    @dauer.setter
    def dauer(self, dauer: str):
        self.__dauer = dauer

    @property
    def art(self) -> str:
        return self.__art

    @art.setter
    def art(self, art: str):
        self.__art = art

    @property
    def reichweite(self) -> str:
        return self.__reichweite

    @reichweite.setter
    def reichweite(self, reichweite: str):
        self.__reichweite = reichweite

    @property
    def schaden(self) -> str:
        return self.__schaden

    @schaden.setter
    def schaden(self, schaden: str):
        self.__schaden = schaden

    @property
    def shr5_Zauber(self):
        return self.__shr5_Zauber

    @shr5_Zauber.setter
    def shr5_Zauber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Zauber__shr5_Zauber", None)
        self.__shr5_Zauber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_PersonaZauber65"):
                opp_val = getattr(old_value, "shr5_PersonaZauber65", None)
                if opp_val == self:
                    setattr(old_value, "shr5_PersonaZauber65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_PersonaZauber65"):
                opp_val = getattr(value, "shr5_PersonaZauber65", None)
                setattr(value, "shr5_PersonaZauber65", self)

class shr5_Spezialisierung(Beschreibbar, Erlernbar, Modifyable, Quelle):

    pass
class shr5_Fertigkeit(Quelle, Modifyable, Beschreibbar):

    def __init__(self, kategorie: str, ausweichen: bool, shr5_Fertigkeit: "shr5_FertigkeitsGruppe" = None, shr5_Fertigkeit21: "shr5_EAttribute" = None, fertigkeit: set["shr5_Spezialisierung"] = None, shr5_Fertigkeit26: "shr5_PersonaFertigkeit" = None, shr5_Fertigkeit52: "shr5_Anwendbar" = None, shr5_Fertigkeit95: "shr5_StufenPersona" = None, Fertigkeit: "shr5_Spezialisierung" = None, shr5_Fertigkeit120: "shr5_AutoSoft" = None, shr5_Fertigkeit127: "shr5_Tutorsoft" = None, shr5_Fertigkeit129: "shr5_SkillSoft" = None, shr5_Fertigkeit164: "shr5_MartialartStyle" = None):
        self.kategorie = kategorie
        self.ausweichen = ausweichen
        self.shr5_Fertigkeit = shr5_Fertigkeit
        self.shr5_Fertigkeit21 = shr5_Fertigkeit21
        self.fertigkeit = fertigkeit if fertigkeit is not None else set()
        self.shr5_Fertigkeit26 = shr5_Fertigkeit26
        self.shr5_Fertigkeit52 = shr5_Fertigkeit52
        self.shr5_Fertigkeit95 = shr5_Fertigkeit95
        self.Fertigkeit = Fertigkeit
        self.shr5_Fertigkeit120 = shr5_Fertigkeit120
        self.shr5_Fertigkeit127 = shr5_Fertigkeit127
        self.shr5_Fertigkeit129 = shr5_Fertigkeit129
        self.shr5_Fertigkeit164 = shr5_Fertigkeit164
        
    @property
    def kategorie(self) -> str:
        return self.__kategorie

    @kategorie.setter
    def kategorie(self, kategorie: str):
        self.__kategorie = kategorie

    @property
    def ausweichen(self) -> bool:
        return self.__ausweichen

    @ausweichen.setter
    def ausweichen(self, ausweichen: bool):
        self.__ausweichen = ausweichen

    @property
    def shr5_Fertigkeit95(self):
        return self.__shr5_Fertigkeit95

    @shr5_Fertigkeit95.setter
    def shr5_Fertigkeit95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fertigkeit__shr5_Fertigkeit95", None)
        self.__shr5_Fertigkeit95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_StufenPersona94"):
                opp_val = getattr(old_value, "shr5_StufenPersona94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_StufenPersona94"):
                opp_val = getattr(value, "shr5_StufenPersona94", None)
                if opp_val is None:
                    setattr(value, "shr5_StufenPersona94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fertigkeit(self):
        return self.__fertigkeit

    @fertigkeit.setter
    def fertigkeit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fertigkeit__fertigkeit", None)
        self.__fertigkeit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Spezialisierung"):
                    opp_val = getattr(item, "Spezialisierung", None)
                    
                    if opp_val == self:
                        setattr(item, "Spezialisierung", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Spezialisierung"):
                    opp_val = getattr(item, "Spezialisierung", None)
                    
                    setattr(item, "Spezialisierung", self)
                    

    @property
    def shr5_Fertigkeit120(self):
        return self.__shr5_Fertigkeit120

    @shr5_Fertigkeit120.setter
    def shr5_Fertigkeit120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fertigkeit__shr5_Fertigkeit120", None)
        self.__shr5_Fertigkeit120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_AutoSoft"):
                opp_val = getattr(old_value, "shr5_AutoSoft", None)
                if opp_val == self:
                    setattr(old_value, "shr5_AutoSoft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_AutoSoft"):
                opp_val = getattr(value, "shr5_AutoSoft", None)
                setattr(value, "shr5_AutoSoft", self)

    @property
    def shr5_Fertigkeit26(self):
        return self.__shr5_Fertigkeit26

    @shr5_Fertigkeit26.setter
    def shr5_Fertigkeit26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fertigkeit__shr5_Fertigkeit26", None)
        self.__shr5_Fertigkeit26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_PersonaFertigkeit25"):
                opp_val = getattr(old_value, "shr5_PersonaFertigkeit25", None)
                if opp_val == self:
                    setattr(old_value, "shr5_PersonaFertigkeit25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_PersonaFertigkeit25"):
                opp_val = getattr(value, "shr5_PersonaFertigkeit25", None)
                setattr(value, "shr5_PersonaFertigkeit25", self)

    @property
    def shr5_Fertigkeit129(self):
        return self.__shr5_Fertigkeit129

    @shr5_Fertigkeit129.setter
    def shr5_Fertigkeit129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fertigkeit__shr5_Fertigkeit129", None)
        self.__shr5_Fertigkeit129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_SkillSoft"):
                opp_val = getattr(old_value, "shr5_SkillSoft", None)
                if opp_val == self:
                    setattr(old_value, "shr5_SkillSoft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_SkillSoft"):
                opp_val = getattr(value, "shr5_SkillSoft", None)
                setattr(value, "shr5_SkillSoft", self)

    @property
    def shr5_Fertigkeit21(self):
        return self.__shr5_Fertigkeit21

    @shr5_Fertigkeit21.setter
    def shr5_Fertigkeit21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fertigkeit__shr5_Fertigkeit21", None)
        self.__shr5_Fertigkeit21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_EAttribute22"):
                opp_val = getattr(old_value, "shr5_EAttribute22", None)
                if opp_val == self:
                    setattr(old_value, "shr5_EAttribute22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_EAttribute22"):
                opp_val = getattr(value, "shr5_EAttribute22", None)
                setattr(value, "shr5_EAttribute22", self)

    @property
    def shr5_Fertigkeit52(self):
        return self.__shr5_Fertigkeit52

    @shr5_Fertigkeit52.setter
    def shr5_Fertigkeit52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fertigkeit__shr5_Fertigkeit52", None)
        self.__shr5_Fertigkeit52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Anwendbar"):
                opp_val = getattr(old_value, "shr5_Anwendbar", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Anwendbar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Anwendbar"):
                opp_val = getattr(value, "shr5_Anwendbar", None)
                setattr(value, "shr5_Anwendbar", self)

    @property
    def Fertigkeit(self):
        return self.__Fertigkeit

    @Fertigkeit.setter
    def Fertigkeit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fertigkeit__Fertigkeit", None)
        self.__Fertigkeit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spezialisierungen"):
                opp_val = getattr(old_value, "spezialisierungen", None)
                if opp_val == self:
                    setattr(old_value, "spezialisierungen", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spezialisierungen"):
                opp_val = getattr(value, "spezialisierungen", None)
                setattr(value, "spezialisierungen", self)

    @property
    def shr5_Fertigkeit(self):
        return self.__shr5_Fertigkeit

    @shr5_Fertigkeit.setter
    def shr5_Fertigkeit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fertigkeit__shr5_Fertigkeit", None)
        self.__shr5_Fertigkeit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_FertigkeitsGruppe"):
                opp_val = getattr(old_value, "shr5_FertigkeitsGruppe", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_FertigkeitsGruppe"):
                opp_val = getattr(value, "shr5_FertigkeitsGruppe", None)
                if opp_val is None:
                    setattr(value, "shr5_FertigkeitsGruppe", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5_Fertigkeit127(self):
        return self.__shr5_Fertigkeit127

    @shr5_Fertigkeit127.setter
    def shr5_Fertigkeit127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fertigkeit__shr5_Fertigkeit127", None)
        self.__shr5_Fertigkeit127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Tutorsoft"):
                opp_val = getattr(old_value, "shr5_Tutorsoft", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Tutorsoft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Tutorsoft"):
                opp_val = getattr(value, "shr5_Tutorsoft", None)
                setattr(value, "shr5_Tutorsoft", self)

    @property
    def shr5_Fertigkeit164(self):
        return self.__shr5_Fertigkeit164

    @shr5_Fertigkeit164.setter
    def shr5_Fertigkeit164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fertigkeit__shr5_Fertigkeit164", None)
        self.__shr5_Fertigkeit164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_MartialartStyle163"):
                opp_val = getattr(old_value, "shr5_MartialartStyle163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_MartialartStyle163"):
                opp_val = getattr(value, "shr5_MartialartStyle163", None)
                if opp_val is None:
                    setattr(value, "shr5_MartialartStyle163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5_SourceLink(Quelle, Beschreibbar):

    pass
class shr5_MagischeTradition(Quelle, Beschreibbar):

    def __init__(self, enzug: str, shr5_MagischeTradition: "shr5_Zauberer" = None, shr5_MagischeTradition152: set["shr5_Geist"] = None):
        self.enzug = enzug
        self.shr5_MagischeTradition = shr5_MagischeTradition
        self.shr5_MagischeTradition152 = shr5_MagischeTradition152 if shr5_MagischeTradition152 is not None else set()
        
    @property
    def enzug(self) -> str:
        return self.__enzug

    @enzug.setter
    def enzug(self, enzug: str):
        self.__enzug = enzug

    @property
    def shr5_MagischeTradition152(self):
        return self.__shr5_MagischeTradition152

    @shr5_MagischeTradition152.setter
    def shr5_MagischeTradition152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_MagischeTradition__shr5_MagischeTradition152", None)
        self.__shr5_MagischeTradition152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_Geist153"):
                    opp_val = getattr(item, "shr5_Geist153", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_Geist153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_Geist153"):
                    opp_val = getattr(item, "shr5_Geist153", None)
                    
                    setattr(item, "shr5_Geist153", self)
                    

    @property
    def shr5_MagischeTradition(self):
        return self.__shr5_MagischeTradition

    @shr5_MagischeTradition.setter
    def shr5_MagischeTradition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_MagischeTradition__shr5_MagischeTradition", None)
        self.__shr5_MagischeTradition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Zauberer63"):
                opp_val = getattr(old_value, "shr5_Zauberer63", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Zauberer63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Zauberer63"):
                opp_val = getattr(value, "shr5_Zauberer63", None)
                setattr(value, "shr5_Zauberer63", self)

class shr5_MartialartStyle(Quelle, Beschreibbar):

    pass
class shr5_LifestyleOption(Quelle, GeldWert, Beschreibbar):

    pass
class shr5_Host(MatrixDevice, ActiveMatixDevice, Beschreibbar):

    def __init__(self, hostRating: int, baseFirewall: int, baseDatenverarbeitung: int, baseAngriff: int, baseSchleicher: int):
        self.hostRating = hostRating
        self.baseFirewall = baseFirewall
        self.baseDatenverarbeitung = baseDatenverarbeitung
        self.baseAngriff = baseAngriff
        self.baseSchleicher = baseSchleicher
        
    @property
    def hostRating(self) -> int:
        return self.__hostRating

    @hostRating.setter
    def hostRating(self, hostRating: int):
        self.__hostRating = hostRating

    @property
    def baseFirewall(self) -> int:
        return self.__baseFirewall

    @baseFirewall.setter
    def baseFirewall(self, baseFirewall: int):
        self.__baseFirewall = baseFirewall

    @property
    def baseAngriff(self) -> int:
        return self.__baseAngriff

    @baseAngriff.setter
    def baseAngriff(self, baseAngriff: int):
        self.__baseAngriff = baseAngriff

    @property
    def baseDatenverarbeitung(self) -> int:
        return self.__baseDatenverarbeitung

    @baseDatenverarbeitung.setter
    def baseDatenverarbeitung(self, baseDatenverarbeitung: int):
        self.__baseDatenverarbeitung = baseDatenverarbeitung

    @property
    def baseSchleicher(self) -> int:
        return self.__baseSchleicher

    @baseSchleicher.setter
    def baseSchleicher(self, baseSchleicher: int):
        self.__baseSchleicher = baseSchleicher

class shr5_MetaMagie(Quelle, Beschreibbar):

    pass
class shr5_AbstraktModifikatoren(Quelle, Modifizierbar, Beschreibbar):

    pass
class shr5_KleindungsModifikator(Quelle, GeldWert, Beschreibbar):

    def __init__(self, rating: int, type: str, capacity: int, shr5_KleindungsModifikator: "shr5_Kleidung" = None):
        self.rating = rating
        self.type = type
        self.capacity = capacity
        self.shr5_KleindungsModifikator = shr5_KleindungsModifikator
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def shr5_KleindungsModifikator(self):
        return self.__shr5_KleindungsModifikator

    @shr5_KleindungsModifikator.setter
    def shr5_KleindungsModifikator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_KleindungsModifikator__shr5_KleindungsModifikator", None)
        self.__shr5_KleindungsModifikator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Kleidung"):
                opp_val = getattr(old_value, "shr5_Kleidung", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Kleidung"):
                opp_val = getattr(value, "shr5_Kleidung", None)
                if opp_val is None:
                    setattr(value, "shr5_Kleidung", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5_Vertrag(Quelle, GeldWert, Beschreibbar):

    pass
class shr5_Substance(Menge, Quelle, GeldWert, Beschreibbar):

    def __init__(self, vector: str, speed: str, shr5_Substance: "shr5_SubstanceContainer" = None, shr5_Substance174: "shr5_AbtraktGranate" = None):
        self.vector = vector
        self.speed = speed
        self.shr5_Substance = shr5_Substance
        self.shr5_Substance174 = shr5_Substance174
        
    @property
    def vector(self) -> str:
        return self.__vector

    @vector.setter
    def vector(self, vector: str):
        self.__vector = vector

    @property
    def speed(self) -> str:
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed

    @property
    def shr5_Substance(self):
        return self.__shr5_Substance

    @shr5_Substance.setter
    def shr5_Substance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Substance__shr5_Substance", None)
        self.__shr5_Substance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_SubstanceContainer"):
                opp_val = getattr(old_value, "shr5_SubstanceContainer", None)
                if opp_val == self:
                    setattr(old_value, "shr5_SubstanceContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_SubstanceContainer"):
                opp_val = getattr(value, "shr5_SubstanceContainer", None)
                setattr(value, "shr5_SubstanceContainer", self)

    @property
    def shr5_Substance174(self):
        return self.__shr5_Substance174

    @shr5_Substance174.setter
    def shr5_Substance174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Substance__shr5_Substance174", None)
        self.__shr5_Substance174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_AbtraktGranate"):
                opp_val = getattr(old_value, "shr5_AbtraktGranate", None)
                if opp_val == self:
                    setattr(old_value, "shr5_AbtraktGranate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_AbtraktGranate"):
                opp_val = getattr(value, "shr5_AbtraktGranate", None)
                setattr(value, "shr5_AbtraktGranate", self)

class shr5_Fahrzeug(Anwendbar, Quelle, GeldWert, FahrzeugZustand, Capacity, Modifizierbar, Beschreibbar):

    def __init__(self, beschleunigung: int, rumpf: int, pilot: int, sensor: int, fahrzeugTyp: str, panzer: int, weaponMounts: int, handling: int, geschwindigkeit: int, shr5_Fahrzeug: set["shr5_FahrzeugModifikation"] = None, shr5_Fahrzeug72: "shr5_SensorArray" = None):
        self.beschleunigung = beschleunigung
        self.rumpf = rumpf
        self.pilot = pilot
        self.sensor = sensor
        self.fahrzeugTyp = fahrzeugTyp
        self.panzer = panzer
        self.weaponMounts = weaponMounts
        self.handling = handling
        self.geschwindigkeit = geschwindigkeit
        self.shr5_Fahrzeug = shr5_Fahrzeug if shr5_Fahrzeug is not None else set()
        self.shr5_Fahrzeug72 = shr5_Fahrzeug72
        
    @property
    def sensor(self) -> int:
        return self.__sensor

    @sensor.setter
    def sensor(self, sensor: int):
        self.__sensor = sensor

    @property
    def fahrzeugTyp(self) -> str:
        return self.__fahrzeugTyp

    @fahrzeugTyp.setter
    def fahrzeugTyp(self, fahrzeugTyp: str):
        self.__fahrzeugTyp = fahrzeugTyp

    @property
    def geschwindigkeit(self) -> int:
        return self.__geschwindigkeit

    @geschwindigkeit.setter
    def geschwindigkeit(self, geschwindigkeit: int):
        self.__geschwindigkeit = geschwindigkeit

    @property
    def handling(self) -> int:
        return self.__handling

    @handling.setter
    def handling(self, handling: int):
        self.__handling = handling

    @property
    def panzer(self) -> int:
        return self.__panzer

    @panzer.setter
    def panzer(self, panzer: int):
        self.__panzer = panzer

    @property
    def weaponMounts(self) -> int:
        return self.__weaponMounts

    @weaponMounts.setter
    def weaponMounts(self, weaponMounts: int):
        self.__weaponMounts = weaponMounts

    @property
    def pilot(self) -> int:
        return self.__pilot

    @pilot.setter
    def pilot(self, pilot: int):
        self.__pilot = pilot

    @property
    def rumpf(self) -> int:
        return self.__rumpf

    @rumpf.setter
    def rumpf(self, rumpf: int):
        self.__rumpf = rumpf

    @property
    def beschleunigung(self) -> int:
        return self.__beschleunigung

    @beschleunigung.setter
    def beschleunigung(self, beschleunigung: int):
        self.__beschleunigung = beschleunigung

    @property
    def shr5_Fahrzeug(self):
        return self.__shr5_Fahrzeug

    @shr5_Fahrzeug.setter
    def shr5_Fahrzeug(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fahrzeug__shr5_Fahrzeug", None)
        self.__shr5_Fahrzeug = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_FahrzeugModifikation"):
                    opp_val = getattr(item, "shr5_FahrzeugModifikation", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_FahrzeugModifikation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_FahrzeugModifikation"):
                    opp_val = getattr(item, "shr5_FahrzeugModifikation", None)
                    
                    setattr(item, "shr5_FahrzeugModifikation", self)
                    

    @property
    def shr5_Fahrzeug72(self):
        return self.__shr5_Fahrzeug72

    @shr5_Fahrzeug72.setter
    def shr5_Fahrzeug72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Fahrzeug__shr5_Fahrzeug72", None)
        self.__shr5_Fahrzeug72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_SensorArray"):
                opp_val = getattr(old_value, "shr5_SensorArray", None)
                if opp_val == self:
                    setattr(old_value, "shr5_SensorArray", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_SensorArray"):
                opp_val = getattr(value, "shr5_SensorArray", None)
                setattr(value, "shr5_SensorArray", self)

class shr5_AbstraktPersona(KoerperlicheAttribute, ChrakterLimits, GeistigeAttribute, SpezielleAttribute, Beschreibbar):

    def __init__(self, konstitutionBasis: int, geschicklichkeitBasis: int, reaktionBasis: int, staerkeBasis: int, charismaBasis: int, willenskraftBasis: int, intuitionBasis: int, logikBasis: int, modManager: str, shr5_AbstraktPersona: set["shr5_PersonaFertigkeit"] = None, shr5_AbstraktPersona3: set["shr5_PersonaFertigkeitsGruppe"] = None, shr5_AbstraktPersona5: "shr5_Spezies" = None, shr5_AbstraktPersona7: set["shr5_PersonaMartialartStyle"] = None, shr5_AbstraktPersona33: "shr5_Cyberware" = None, shr5_AbstraktPersona39: "shr5_BioWare" = None):
        self.konstitutionBasis = konstitutionBasis
        self.geschicklichkeitBasis = geschicklichkeitBasis
        self.reaktionBasis = reaktionBasis
        self.staerkeBasis = staerkeBasis
        self.charismaBasis = charismaBasis
        self.willenskraftBasis = willenskraftBasis
        self.intuitionBasis = intuitionBasis
        self.logikBasis = logikBasis
        self.modManager = modManager
        self.shr5_AbstraktPersona = shr5_AbstraktPersona if shr5_AbstraktPersona is not None else set()
        self.shr5_AbstraktPersona3 = shr5_AbstraktPersona3 if shr5_AbstraktPersona3 is not None else set()
        self.shr5_AbstraktPersona5 = shr5_AbstraktPersona5
        self.shr5_AbstraktPersona7 = shr5_AbstraktPersona7 if shr5_AbstraktPersona7 is not None else set()
        self.shr5_AbstraktPersona33 = shr5_AbstraktPersona33
        self.shr5_AbstraktPersona39 = shr5_AbstraktPersona39
        
    @property
    def geschicklichkeitBasis(self) -> int:
        return self.__geschicklichkeitBasis

    @geschicklichkeitBasis.setter
    def geschicklichkeitBasis(self, geschicklichkeitBasis: int):
        self.__geschicklichkeitBasis = geschicklichkeitBasis

    @property
    def intuitionBasis(self) -> int:
        return self.__intuitionBasis

    @intuitionBasis.setter
    def intuitionBasis(self, intuitionBasis: int):
        self.__intuitionBasis = intuitionBasis

    @property
    def reaktionBasis(self) -> int:
        return self.__reaktionBasis

    @reaktionBasis.setter
    def reaktionBasis(self, reaktionBasis: int):
        self.__reaktionBasis = reaktionBasis

    @property
    def konstitutionBasis(self) -> int:
        return self.__konstitutionBasis

    @konstitutionBasis.setter
    def konstitutionBasis(self, konstitutionBasis: int):
        self.__konstitutionBasis = konstitutionBasis

    @property
    def willenskraftBasis(self) -> int:
        return self.__willenskraftBasis

    @willenskraftBasis.setter
    def willenskraftBasis(self, willenskraftBasis: int):
        self.__willenskraftBasis = willenskraftBasis

    @property
    def modManager(self) -> str:
        return self.__modManager

    @modManager.setter
    def modManager(self, modManager: str):
        self.__modManager = modManager

    @property
    def charismaBasis(self) -> int:
        return self.__charismaBasis

    @charismaBasis.setter
    def charismaBasis(self, charismaBasis: int):
        self.__charismaBasis = charismaBasis

    @property
    def staerkeBasis(self) -> int:
        return self.__staerkeBasis

    @staerkeBasis.setter
    def staerkeBasis(self, staerkeBasis: int):
        self.__staerkeBasis = staerkeBasis

    @property
    def logikBasis(self) -> int:
        return self.__logikBasis

    @logikBasis.setter
    def logikBasis(self, logikBasis: int):
        self.__logikBasis = logikBasis

    @property
    def shr5_AbstraktPersona7(self):
        return self.__shr5_AbstraktPersona7

    @shr5_AbstraktPersona7.setter
    def shr5_AbstraktPersona7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AbstraktPersona__shr5_AbstraktPersona7", None)
        self.__shr5_AbstraktPersona7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_PersonaMartialartStyle"):
                    opp_val = getattr(item, "shr5_PersonaMartialartStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_PersonaMartialartStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_PersonaMartialartStyle"):
                    opp_val = getattr(item, "shr5_PersonaMartialartStyle", None)
                    
                    setattr(item, "shr5_PersonaMartialartStyle", self)
                    

    @property
    def shr5_AbstraktPersona5(self):
        return self.__shr5_AbstraktPersona5

    @shr5_AbstraktPersona5.setter
    def shr5_AbstraktPersona5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AbstraktPersona__shr5_AbstraktPersona5", None)
        self.__shr5_AbstraktPersona5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Spezies"):
                opp_val = getattr(old_value, "shr5_Spezies", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Spezies", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Spezies"):
                opp_val = getattr(value, "shr5_Spezies", None)
                setattr(value, "shr5_Spezies", self)

    @property
    def shr5_AbstraktPersona3(self):
        return self.__shr5_AbstraktPersona3

    @shr5_AbstraktPersona3.setter
    def shr5_AbstraktPersona3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AbstraktPersona__shr5_AbstraktPersona3", None)
        self.__shr5_AbstraktPersona3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_PersonaFertigkeitsGruppe"):
                    opp_val = getattr(item, "shr5_PersonaFertigkeitsGruppe", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_PersonaFertigkeitsGruppe", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_PersonaFertigkeitsGruppe"):
                    opp_val = getattr(item, "shr5_PersonaFertigkeitsGruppe", None)
                    
                    setattr(item, "shr5_PersonaFertigkeitsGruppe", self)
                    

    @property
    def shr5_AbstraktPersona33(self):
        return self.__shr5_AbstraktPersona33

    @shr5_AbstraktPersona33.setter
    def shr5_AbstraktPersona33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AbstraktPersona__shr5_AbstraktPersona33", None)
        self.__shr5_AbstraktPersona33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Cyberware"):
                opp_val = getattr(old_value, "shr5_Cyberware", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Cyberware", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Cyberware"):
                opp_val = getattr(value, "shr5_Cyberware", None)
                setattr(value, "shr5_Cyberware", self)

    @property
    def shr5_AbstraktPersona39(self):
        return self.__shr5_AbstraktPersona39

    @shr5_AbstraktPersona39.setter
    def shr5_AbstraktPersona39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AbstraktPersona__shr5_AbstraktPersona39", None)
        self.__shr5_AbstraktPersona39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_BioWare"):
                opp_val = getattr(old_value, "shr5_BioWare", None)
                if opp_val == self:
                    setattr(old_value, "shr5_BioWare", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_BioWare"):
                opp_val = getattr(value, "shr5_BioWare", None)
                setattr(value, "shr5_BioWare", self)

    @property
    def shr5_AbstraktPersona(self):
        return self.__shr5_AbstraktPersona

    @shr5_AbstraktPersona.setter
    def shr5_AbstraktPersona(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_AbstraktPersona__shr5_AbstraktPersona", None)
        self.__shr5_AbstraktPersona = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5_PersonaFertigkeit"):
                    opp_val = getattr(item, "shr5_PersonaFertigkeit", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5_PersonaFertigkeit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5_PersonaFertigkeit"):
                    opp_val = getattr(item, "shr5_PersonaFertigkeit", None)
                    
                    setattr(item, "shr5_PersonaFertigkeit", self)
                    

class shr5_Software(Quelle, GeldWert, Beschreibbar):

    pass
class shr5_SensorFunction(Quelle, Beschreibbar):

    def __init__(self, maxRange: int, shr5_SensorFunction: "shr5_Sensor" = None):
        self.maxRange = maxRange
        self.shr5_SensorFunction = shr5_SensorFunction
        
    @property
    def maxRange(self) -> int:
        return self.__maxRange

    @maxRange.setter
    def maxRange(self, maxRange: int):
        self.__maxRange = maxRange

    @property
    def shr5_SensorFunction(self):
        return self.__shr5_SensorFunction

    @shr5_SensorFunction.setter
    def shr5_SensorFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_SensorFunction__shr5_SensorFunction", None)
        self.__shr5_SensorFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Sensor"):
                opp_val = getattr(old_value, "shr5_Sensor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Sensor"):
                opp_val = getattr(value, "shr5_Sensor", None)
                if opp_val is None:
                    setattr(value, "shr5_Sensor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5_FahrzeugModifikation(Quelle, GeldWert, Beschreibbar):

    def __init__(self, capacityUsed: int, shr5_FahrzeugModifikation: "shr5_Fahrzeug" = None):
        self.capacityUsed = capacityUsed
        self.shr5_FahrzeugModifikation = shr5_FahrzeugModifikation
        
    @property
    def capacityUsed(self) -> int:
        return self.__capacityUsed

    @capacityUsed.setter
    def capacityUsed(self, capacityUsed: int):
        self.__capacityUsed = capacityUsed

    @property
    def shr5_FahrzeugModifikation(self):
        return self.__shr5_FahrzeugModifikation

    @shr5_FahrzeugModifikation.setter
    def shr5_FahrzeugModifikation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_FahrzeugModifikation__shr5_FahrzeugModifikation", None)
        self.__shr5_FahrzeugModifikation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Fahrzeug"):
                opp_val = getattr(old_value, "shr5_Fahrzeug", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Fahrzeug"):
                opp_val = getattr(value, "shr5_Fahrzeug", None)
                if opp_val is None:
                    setattr(value, "shr5_Fahrzeug", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5_MartialartTechnique(Quelle, Beschreibbar):

    pass
class Identifiable:

    pass
class shr5_ShrList(Identifiable, Beschreibbar):

    pass
class shr5_SourceBook(Identifiable, Beschreibbar):

    def __init__(self, startShrTime: str, endShrTime: str, code: str, shr5_SourceBook: "shr5_Quelle" = None):
        self.startShrTime = startShrTime
        self.endShrTime = endShrTime
        self.code = code
        self.shr5_SourceBook = shr5_SourceBook
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def startShrTime(self) -> str:
        return self.__startShrTime

    @startShrTime.setter
    def startShrTime(self, startShrTime: str):
        self.__startShrTime = startShrTime

    @property
    def endShrTime(self) -> str:
        return self.__endShrTime

    @endShrTime.setter
    def endShrTime(self, endShrTime: str):
        self.__endShrTime = endShrTime

    @property
    def shr5_SourceBook(self):
        return self.__shr5_SourceBook

    @shr5_SourceBook.setter
    def shr5_SourceBook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_SourceBook__shr5_SourceBook", None)
        self.__shr5_SourceBook = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Quelle"):
                opp_val = getattr(old_value, "shr5_Quelle", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Quelle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Quelle"):
                opp_val = getattr(value, "shr5_Quelle", None)
                setattr(value, "shr5_Quelle", self)

class shr5_Reichweite(Identifiable, Beschreibbar):

    def __init__(self, min: int, kurz: int, mittel: int, weit: int, extrem: int, shr5_Reichweite: "shr5_AbstaktFernKampfwaffe" = None, shr5_Reichweite88: "shr5_Munition" = None):
        self.min = min
        self.kurz = kurz
        self.mittel = mittel
        self.weit = weit
        self.extrem = extrem
        self.shr5_Reichweite = shr5_Reichweite
        self.shr5_Reichweite88 = shr5_Reichweite88
        
    @property
    def extrem(self) -> int:
        return self.__extrem

    @extrem.setter
    def extrem(self, extrem: int):
        self.__extrem = extrem

    @property
    def weit(self) -> int:
        return self.__weit

    @weit.setter
    def weit(self, weit: int):
        self.__weit = weit

    @property
    def kurz(self) -> int:
        return self.__kurz

    @kurz.setter
    def kurz(self, kurz: int):
        self.__kurz = kurz

    @property
    def mittel(self) -> int:
        return self.__mittel

    @mittel.setter
    def mittel(self, mittel: int):
        self.__mittel = mittel

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def shr5_Reichweite(self):
        return self.__shr5_Reichweite

    @shr5_Reichweite.setter
    def shr5_Reichweite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Reichweite__shr5_Reichweite", None)
        self.__shr5_Reichweite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_AbstaktFernKampfwaffe"):
                opp_val = getattr(old_value, "shr5_AbstaktFernKampfwaffe", None)
                if opp_val == self:
                    setattr(old_value, "shr5_AbstaktFernKampfwaffe", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_AbstaktFernKampfwaffe"):
                opp_val = getattr(value, "shr5_AbstaktFernKampfwaffe", None)
                setattr(value, "shr5_AbstaktFernKampfwaffe", self)

    @property
    def shr5_Reichweite88(self):
        return self.__shr5_Reichweite88

    @shr5_Reichweite88.setter
    def shr5_Reichweite88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Reichweite__shr5_Reichweite88", None)
        self.__shr5_Reichweite88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_Munition"):
                opp_val = getattr(old_value, "shr5_Munition", None)
                if opp_val == self:
                    setattr(old_value, "shr5_Munition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_Munition"):
                opp_val = getattr(value, "shr5_Munition", None)
                setattr(value, "shr5_Munition", self)

class shr5_Quelle(Identifiable):

    def __init__(self, page: str, shr5_Quelle: "shr5_SourceBook" = None):
        self.page = page
        self.shr5_Quelle = shr5_Quelle
        
    @property
    def page(self) -> str:
        return self.__page

    @page.setter
    def page(self, page: str):
        self.__page = page

    @property
    def shr5_Quelle(self):
        return self.__shr5_Quelle

    @shr5_Quelle.setter
    def shr5_Quelle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5_Quelle__shr5_Quelle", None)
        self.__shr5_Quelle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5_SourceBook"):
                opp_val = getattr(old_value, "shr5_SourceBook", None)
                if opp_val == self:
                    setattr(old_value, "shr5_SourceBook", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5_SourceBook"):
                opp_val = getattr(value, "shr5_SourceBook", None)
                setattr(value, "shr5_SourceBook", self)

class shr5_Beschreibbar(ABC):

    def __init__(self, beschreibung: str, name: str, image: str):
        self.beschreibung = beschreibung
        self.name = name
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
