from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SwineBreed(Enum):
    BK = "BK"
    CW = "CW"
    DU = "DU"
    HA = "HA"
    LC = "LC"
    LA = "LA"
    LB = "LB"
    LW = "LW"
    PE = "PE"
    PC = "PC"
    RW = "RW"
    SO = "SO"
    TM = "TM"
    WS = "WS"
    YO = "YO"
    Unspecified = "Unspecified"
class Sex(Enum):
    Unspecified = "Unspecified"
    F = "F"
    M = "M"
    C = "C"
    S = "S"
class BeefBreed(Enum):
    NS = "NS"
    BO = "BO"
    BR = "BR"
    BH = "BH"
    BI = "BI"
    BL = "BL"
    AN = "AN"
    AB = "AB"
    AF = "AF"
    AL = "AL"
    AE = "AE"
    AM = "AM"
    AK = "AK"
    AW = "AW"
    AU = "AU"
    BA = "BA"
    BF = "BF"
    BE = "BE"
    BM = "BM"
    BB = "BB"
    BG = "BG"
    BD = "BD"
    FA = "FA"
    FL = "FL"
    FC = "FC"
    FR = "FR"
    FB = "FB"
    BN = "BN"
    BU = "BU"
    BW = "BW"
    SB = "SB"
    BQ = "BQ"
    CP = "CP"
    CN = "CN"
    CB = "CB"
    CH = "CH"
    CG = "CG"
    CM = "CM"
    CA = "CA"
    XX = "XX"
    XT = "XT"
    CU = "CU"
    DB = "DB"
    DJ = "DJ"
    RW = "RW"
    DE = "DE"
    DR = "DR"
    DL = "DL"
    FP = "FP"
    ER = "ER"
    MA = "MA"
    MH = "MH"
    ML = "ML"
    MR = "MR"
    ME = "ME"
    DF = "DF"
    GA = "GA"
    GS = "GS"
    GE = "GE"
    GV = "GV"
    GI = "GI"
    GR = "GR"
    GZ = "GZ"
    GY = "GY"
    HC = "HC"
    HB = "HB"
    HH = "HH"
    HP = "HP"
    SH = "SH"
    HY = "HY"
    IB = "IB"
    KY = "KY"
    KB = "KB"
    LM = "LM"
    LR = "LR"
    LO = "LO"
    LU = "LU"
    RO = "RO"
    DN = "DN"
    SW = "SW"
    SA = "SA"
    MI = "MI"
    MC = "MC"
    MO = "MO"
    MU = "MU"
    MG = "MG"
    NE = "NE"
    NM = "NM"
    NR = "NR"
    PA = "PA"
    PR = "PR"
    PI = "PI"
    PZ = "PZ"
    RA = "RA"
    AR = "AR"
    RR = "RR"
    RB = "RB"
    RD = "RD"
    RP = "RP"
    RN = "RN"
    RS = "RS"
    YA = "YA"
    Unspecified = "Unspecified"
    SG = "SG"
    SL = "SL"
    SE = "SE"
    SV = "SV"
    SS = "SS"
    IS = "IS"
    SP = "SP"
    SI = "SI"
    SM = "SM"
    DS = "DS"
    SX = "SX"
    TP = "TP"
    TA = "TA"
    TG = "TG"
    TN = "TN"
    TL = "TL"
    TI = "TI"
    WB = "WB"
    WF = "WF"
    WP = "WP"
class OneToTen(Enum):
    Unspecified = "Unspecified"
    One = "One"
    Two = "Two"
    Three = "Three"
    Four = "Four"
    Five = "Five"
    Six = "Six"
    Seven = "Seven"
    Eight = "Eight"
    Nine = "Nine"
    Ten = "Ten"
class Treatment(Enum):
    Unspecified = "Unspecified"
    Vaccination = "Vaccination"
    Vitamin = "Vitamin"
    Hormone = "Hormone"
    Prevention = "Prevention"
class DairyBreed(Enum):
    LD = "LD"
    AY = "AY"
    BS = "BS"
    GD = "GD"
    GU = "GU"
    HO = "HO"
    JE = "JE"
    WW = "WW"
    FM = "FM"
    MS = "MS"
    Unspecified = "Unspecified"
class USBeefYieldGrade(Enum):
    One = "One"
    Two = "Two"
    Three = "Three"
    Four = "Four"
    Five = "Five"
    Unspecified = "Unspecified"
class BisonBreed(Enum):
    Unspecified = "Unspecified"
    WO = "WO"
    PB = "PB"
class Level(Enum):
    Unspecified = "Unspecified"
    Low = "Low"
    Average = "Average"
    High = "High"
class USQualityGrade(Enum):
    Unspecified = "Unspecified"
    Standard = "Standard"
    Select = "Select"
    Choice = "Choice"
    Prime = "Prime"
class SheepBreed(Enum):
    FN = "FN"
    CD = "CD"
    HS = "HS"
    OU = "OU"
    RI = "RI"
    LY = "LY"
    FB = "FB"
    BW = "BW"
    BF = "BF"
    BO = "BO"
    BC = "BC"
    CO = "CO"
    CF = "CF"
    CL = "CL"
    CP = "CP"
    CR = "CR"
    DH = "DH"
    DP = "DP"
    DL = "DL"
    ER = "ER"
    MT = "MT"
    NL = "NL"
    NC = "NC"
    OX = "OX"
    HY = "HY"
    IL = "IL"
    KK = "KK"
    KA = "KA"
    KH = "KH"
    BL = "BL"
    LE = "LE"
    HL = "HL"
    LI = "LI"
    MM = "MM"
    MP = "MP"
    Unspecified = "Unspecified"
    PE = "PE"
    PO = "PO"
    RG = "RG"
    RV = "RV"
    RM = "RM"
    RY = "RY"
    SX = "SX"
    SC = "SC"
    SL = "SL"
    SR = "SR"
    ST = "ST"
    SU = "SU"
    TA = "TA"
    TX = "TX"
    TU = "TU"
    XL = "XL"
    XM = "XM"
    ZS = "ZS"
class TreatmentMethod(Enum):
    Unspecified = "Unspecified"
    Intramuscular = "Intramuscular"
    Nasal = "Nasal"
    Salve = "Salve"
class GoatBreed(Enum):
    TO = "TO"
    Unspecified = "Unspecified"
    AI = "AI"
    AG = "AG"
    BZ = "BZ"
    CS = "CS"
    LN = "LN"
    ND = "ND"
    NU = "NU"
    OH = "OH"
    PY = "PY"
    EN = "EN"
class EventDataType(Enum):
    String = "String"
    Integer = "Integer"
    Boolean = "Boolean"
class HorseBreed(Enum):
    HN = "HN"
    HK = "HK"
    HF = "HF"
    HV = "HV"
    HG = "HG"
    AC = "AC"
    AS = "AS"
    AA = "AA"
    AO = "AO"
    NO = "NO"
    AP = "AP"
    AD = "AD"
    BW = "BW"
    BY = "BY"
    BU = "BU"
    CI = "CI"
    FC = "FC"
    CV = "CV"
    CY = "CY"
    CM = "CM"
    DT = "DT"
    DW = "DW"
    EX = "EX"
    FE = "FE"
    FJ = "FJ"
    FH = "FH"
    FR = "FR"
    GL = "GL"
    WG = "WG"
    SN = "SN"
    SF = "SF"
    WW = "WW"
    WI = "WI"
    TP = "TP"
    HT = "HT"
    TW = "TW"
    HW = "HW"
    HU = "HU"
    IC = "IC"
    LZ = "LZ"
    MU = "MU"
    MF = "MF"
    MN = "MN"
    NF = "NF"
    NK = "NK"
    OB = "OB"
    PT = "PT"
    PL = "PL"
    PF = "PF"
    PH = "PH"
    PV = "PV"
    PN = "PN"
    PW = "PW"
    OL = "OL"
    QH = "QH"
    RH = "RH"
    RU = "RU"
    SE = "SE"
    SY = "SY"
    TH = "TH"
    TR = "TR"
    TF = "TF"
    VK = "VK"
    WE = "WE"
    WF = "WF"
    WU = "WU"
    Unspecified = "Unspecified"
class AnimalType(Enum):
    Unspecified = "Unspecified"
    Swine = "Swine"
    Equine = "Equine"
    Caprine = "Caprine"
    Ovine = "Ovine"
    BovineBeef = "BovineBeef"
    BovineDairy = "BovineDairy"
    BovineBison = "BovineBison"
class USSwineQualityGrade(Enum):
    Three = "Three"
    Four = "Four"
    Unspecified = "Unspecified"
    One = "One"
    Two = "Two"


############################################
# Definition of Classes
############################################

class tracker_EventAttributeSchema:

    def __init__(self, name: str, dataType: str, description: str, tracker_EventAttributeSchema: "tracker_EventSchema" = None):
        self.name = name
        self.dataType = dataType
        self.description = description
        self.tracker_EventAttributeSchema = tracker_EventAttributeSchema
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tracker_EventAttributeSchema(self):
        return self.__tracker_EventAttributeSchema

    @tracker_EventAttributeSchema.setter
    def tracker_EventAttributeSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_EventAttributeSchema__tracker_EventAttributeSchema", None)
        self.__tracker_EventAttributeSchema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_EventSchema26"):
                opp_val = getattr(old_value, "tracker_EventSchema26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_EventSchema26"):
                opp_val = getattr(value, "tracker_EventSchema26", None)
                if opp_val is None:
                    setattr(value, "tracker_EventSchema26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tracker_EventSchema:

    def __init__(self, name: str, description: str, animalType: str, tracker_EventSchema: "tracker_GenericEvent" = None, tracker_EventSchema26: set["tracker_EventAttributeSchema"] = None, tracker_EventSchema29: "tracker_Schema" = None):
        self.name = name
        self.description = description
        self.animalType = animalType
        self.tracker_EventSchema = tracker_EventSchema
        self.tracker_EventSchema26 = tracker_EventSchema26 if tracker_EventSchema26 is not None else set()
        self.tracker_EventSchema29 = tracker_EventSchema29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def animalType(self) -> str:
        return self.__animalType

    @animalType.setter
    def animalType(self, animalType: str):
        self.__animalType = animalType

    @property
    def tracker_EventSchema26(self):
        return self.__tracker_EventSchema26

    @tracker_EventSchema26.setter
    def tracker_EventSchema26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_EventSchema__tracker_EventSchema26", None)
        self.__tracker_EventSchema26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tracker_EventAttributeSchema"):
                    opp_val = getattr(item, "tracker_EventAttributeSchema", None)
                    
                    if opp_val == self:
                        setattr(item, "tracker_EventAttributeSchema", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tracker_EventAttributeSchema"):
                    opp_val = getattr(item, "tracker_EventAttributeSchema", None)
                    
                    setattr(item, "tracker_EventAttributeSchema", self)
                    

    @property
    def tracker_EventSchema29(self):
        return self.__tracker_EventSchema29

    @tracker_EventSchema29.setter
    def tracker_EventSchema29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_EventSchema__tracker_EventSchema29", None)
        self.__tracker_EventSchema29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Schema28"):
                opp_val = getattr(old_value, "tracker_Schema28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Schema28"):
                opp_val = getattr(value, "tracker_Schema28", None)
                if opp_val is None:
                    setattr(value, "tracker_Schema28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tracker_EventSchema(self):
        return self.__tracker_EventSchema

    @tracker_EventSchema.setter
    def tracker_EventSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_EventSchema__tracker_EventSchema", None)
        self.__tracker_EventSchema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_GenericEvent24"):
                opp_val = getattr(old_value, "tracker_GenericEvent24", None)
                if opp_val == self:
                    setattr(old_value, "tracker_GenericEvent24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_GenericEvent24"):
                opp_val = getattr(value, "tracker_GenericEvent24", None)
                setattr(value, "tracker_GenericEvent24", self)

class tracker_EventAttribute:

    def __init__(self, key: str, value: str, tracker_EventAttribute: "tracker_GenericEvent" = None):
        self.key = key
        self.value = value
        self.tracker_EventAttribute = tracker_EventAttribute
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def tracker_EventAttribute(self):
        return self.__tracker_EventAttribute

    @tracker_EventAttribute.setter
    def tracker_EventAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_EventAttribute__tracker_EventAttribute", None)
        self.__tracker_EventAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_GenericEvent"):
                opp_val = getattr(old_value, "tracker_GenericEvent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_GenericEvent"):
                opp_val = getattr(value, "tracker_GenericEvent", None)
                if opp_val is None:
                    setattr(value, "tracker_GenericEvent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Birthing:

    pass
class tracker_Calving(Birthing):

    pass
class MedicalCondition:

    pass
class tracker_Mastitis(MedicalCondition):

    def __init__(self, location: str, origin: str):
        self.location = location
        self.origin = origin
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def origin(self) -> str:
        return self.__origin

    @origin.setter
    def origin(self, origin: str):
        self.__origin = origin

class Bovine:

    pass
class tracker_BovineDairy(Bovine):

    def __init__(self, dairyBreed: str):
        self.dairyBreed = dairyBreed
        
    @property
    def dairyBreed(self) -> str:
        return self.__dairyBreed

    @dairyBreed.setter
    def dairyBreed(self, dairyBreed: str):
        self.__dairyBreed = dairyBreed

class tracker_BovineBison(Bovine):

    def __init__(self, buffaloBreed: str):
        self.buffaloBreed = buffaloBreed
        
    @property
    def buffaloBreed(self) -> str:
        return self.__buffaloBreed

    @buffaloBreed.setter
    def buffaloBreed(self, buffaloBreed: str):
        self.__buffaloBreed = buffaloBreed

class tracker_BovineBeef(Bovine):

    def __init__(self, beefBreed: str):
        self.beefBreed = beefBreed
        
    @property
    def beefBreed(self) -> str:
        return self.__beefBreed

    @beefBreed.setter
    def beefBreed(self, beefBreed: str):
        self.__beefBreed = beefBreed

class tracker_Premises:

    def __init__(self, premisesId: str, emailContact: str, uri: str, name: str, tracker_Premises: set["tracker_Animal"] = None, tracker_Premises12: set["tracker_Tag"] = None, tracker_Premises15: set["tracker_Location"] = None, tracker_Premises17: "tracker_Schema" = None):
        self.premisesId = premisesId
        self.emailContact = emailContact
        self.uri = uri
        self.name = name
        self.tracker_Premises = tracker_Premises if tracker_Premises is not None else set()
        self.tracker_Premises12 = tracker_Premises12 if tracker_Premises12 is not None else set()
        self.tracker_Premises15 = tracker_Premises15 if tracker_Premises15 is not None else set()
        self.tracker_Premises17 = tracker_Premises17
        
    @property
    def emailContact(self) -> str:
        return self.__emailContact

    @emailContact.setter
    def emailContact(self, emailContact: str):
        self.__emailContact = emailContact

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def premisesId(self) -> str:
        return self.__premisesId

    @premisesId.setter
    def premisesId(self, premisesId: str):
        self.__premisesId = premisesId

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tracker_Premises(self):
        return self.__tracker_Premises

    @tracker_Premises.setter
    def tracker_Premises(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Premises__tracker_Premises", None)
        self.__tracker_Premises = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tracker_Animal10"):
                    opp_val = getattr(item, "tracker_Animal10", None)
                    
                    if opp_val == self:
                        setattr(item, "tracker_Animal10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tracker_Animal10"):
                    opp_val = getattr(item, "tracker_Animal10", None)
                    
                    setattr(item, "tracker_Animal10", self)
                    

    @property
    def tracker_Premises12(self):
        return self.__tracker_Premises12

    @tracker_Premises12.setter
    def tracker_Premises12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Premises__tracker_Premises12", None)
        self.__tracker_Premises12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tracker_Tag13"):
                    opp_val = getattr(item, "tracker_Tag13", None)
                    
                    if opp_val == self:
                        setattr(item, "tracker_Tag13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tracker_Tag13"):
                    opp_val = getattr(item, "tracker_Tag13", None)
                    
                    setattr(item, "tracker_Tag13", self)
                    

    @property
    def tracker_Premises15(self):
        return self.__tracker_Premises15

    @tracker_Premises15.setter
    def tracker_Premises15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Premises__tracker_Premises15", None)
        self.__tracker_Premises15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tracker_Location"):
                    opp_val = getattr(item, "tracker_Location", None)
                    
                    if opp_val == self:
                        setattr(item, "tracker_Location", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tracker_Location"):
                    opp_val = getattr(item, "tracker_Location", None)
                    
                    setattr(item, "tracker_Location", self)
                    

    @property
    def tracker_Premises17(self):
        return self.__tracker_Premises17

    @tracker_Premises17.setter
    def tracker_Premises17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Premises__tracker_Premises17", None)
        self.__tracker_Premises17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Schema"):
                opp_val = getattr(old_value, "tracker_Schema", None)
                if opp_val == self:
                    setattr(old_value, "tracker_Schema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Schema"):
                opp_val = getattr(value, "tracker_Schema", None)
                setattr(value, "tracker_Schema", self)

    def eventHistory(self) -> Event:
        # TODO: Implement eventHistory method
        pass

    def addTemplate(self, ains: str, animalTemplate: Animal):
        # TODO: Implement addTemplate method
        pass

    def findAnimal(self, id: str) -> Animal:
        # TODO: Implement findAnimal method
        pass

class Event:

    pass
class tracker_AnimalMissing(Event):

    pass
class tracker_Birthing(Event):

    def __init__(self, viability: bool, assisted: bool, difficulty: str):
        self.viability = viability
        self.assisted = assisted
        self.difficulty = difficulty
        
    @property
    def assisted(self) -> bool:
        return self.__assisted

    @assisted.setter
    def assisted(self, assisted: bool):
        self.__assisted = assisted

    @property
    def viability(self) -> bool:
        return self.__viability

    @viability.setter
    def viability(self, viability: bool):
        self.__viability = viability

    @property
    def difficulty(self) -> str:
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, difficulty: str):
        self.__difficulty = difficulty

class tracker_HerdTest(Event):

    def __init__(self, pregnant: bool, daysSinceBredEstimate: int, bredDateEstimate: date):
        self.pregnant = pregnant
        self.daysSinceBredEstimate = daysSinceBredEstimate
        self.bredDateEstimate = bredDateEstimate
        
    @property
    def bredDateEstimate(self) -> date:
        return self.__bredDateEstimate

    @bredDateEstimate.setter
    def bredDateEstimate(self, bredDateEstimate: date):
        self.__bredDateEstimate = bredDateEstimate

    @property
    def pregnant(self) -> bool:
        return self.__pregnant

    @pregnant.setter
    def pregnant(self, pregnant: bool):
        self.__pregnant = pregnant

    @property
    def daysSinceBredEstimate(self) -> int:
        return self.__daysSinceBredEstimate

    @daysSinceBredEstimate.setter
    def daysSinceBredEstimate(self, daysSinceBredEstimate: int):
        self.__daysSinceBredEstimate = daysSinceBredEstimate

class tracker_TagApplied(Event):

    pass
class tracker_GenericEvent(Event):

    def __init__(self, tracker_GenericEvent: set["tracker_EventAttribute"] = None, tracker_GenericEvent24: "tracker_EventSchema" = None):
        self.tracker_GenericEvent = tracker_GenericEvent if tracker_GenericEvent is not None else set()
        self.tracker_GenericEvent24 = tracker_GenericEvent24
        
    @property
    def tracker_GenericEvent(self):
        return self.__tracker_GenericEvent

    @tracker_GenericEvent.setter
    def tracker_GenericEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_GenericEvent__tracker_GenericEvent", None)
        self.__tracker_GenericEvent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tracker_EventAttribute"):
                    opp_val = getattr(item, "tracker_EventAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "tracker_EventAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tracker_EventAttribute"):
                    opp_val = getattr(item, "tracker_EventAttribute", None)
                    
                    setattr(item, "tracker_EventAttribute", self)
                    

    @property
    def tracker_GenericEvent24(self):
        return self.__tracker_GenericEvent24

    @tracker_GenericEvent24.setter
    def tracker_GenericEvent24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_GenericEvent__tracker_GenericEvent24", None)
        self.__tracker_GenericEvent24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_EventSchema"):
                opp_val = getattr(old_value, "tracker_EventSchema", None)
                if opp_val == self:
                    setattr(old_value, "tracker_EventSchema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_EventSchema"):
                opp_val = getattr(value, "tracker_EventSchema", None)
                setattr(value, "tracker_EventSchema", self)

    def findSchema(self, eventAttribute: str) -> str:
        # TODO: Implement findSchema method
        pass

class tracker_LostTag(Event):

    pass
class tracker_MedicalTreatment(Event):

    def __init__(self, name: str, product: str, manufacturer: str, lot: str, quantity: str, treatment: str, method: str):
        self.name = name
        self.product = product
        self.manufacturer = manufacturer
        self.lot = lot
        self.quantity = quantity
        self.treatment = treatment
        self.method = method
        
    @property
    def product(self) -> str:
        return self.__product

    @product.setter
    def product(self, product: str):
        self.__product = product

    @property
    def lot(self) -> str:
        return self.__lot

    @lot.setter
    def lot(self, lot: str):
        self.__lot = lot

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def treatment(self) -> str:
        return self.__treatment

    @treatment.setter
    def treatment(self, treatment: str):
        self.__treatment = treatment

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def quantity(self) -> str:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: str):
        self.__quantity = quantity

class tracker_WeighIn(Event):

    def __init__(self, weight: str, weightGainPerDay: str):
        self.weight = weight
        self.weightGainPerDay = weightGainPerDay
        
    @property
    def weightGainPerDay(self) -> str:
        return self.__weightGainPerDay

    @weightGainPerDay.setter
    def weightGainPerDay(self, weightGainPerDay: str):
        self.__weightGainPerDay = weightGainPerDay

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

    def previousWeighIn(self) -> str:
        # TODO: Implement previousWeighIn method
        pass

class tracker_TagRetired(Event):

    pass
class tracker_ICVI(Event):

    pass
class tracker_MovedOut(Event):

    def __init__(self, destinationPin: str):
        self.destinationPin = destinationPin
        
    @property
    def destinationPin(self) -> str:
        return self.__destinationPin

    @destinationPin.setter
    def destinationPin(self, destinationPin: str):
        self.__destinationPin = destinationPin

class tracker_Died(Event):

    pass
class tracker_Sighting(Event):

    pass
class tracker_MedicalCondition(Event):

    pass
class tracker_BirthDefect(Event):

    def __init__(self, freemartin: bool):
        self.freemartin = freemartin
        
    @property
    def freemartin(self) -> bool:
        return self.__freemartin

    @freemartin.setter
    def freemartin(self, freemartin: bool):
        self.__freemartin = freemartin

class tracker_MovedIn(Event):

    def __init__(self, sourcePin: str):
        self.sourcePin = sourcePin
        
    @property
    def sourcePin(self) -> str:
        return self.__sourcePin

    @sourcePin.setter
    def sourcePin(self, sourcePin: str):
        self.__sourcePin = sourcePin

class tracker_USOvineGrading(Event):

    def __init__(self, qualityGrade: str, qualityGradeLevel: str):
        self.qualityGrade = qualityGrade
        self.qualityGradeLevel = qualityGradeLevel
        
    @property
    def qualityGrade(self) -> str:
        return self.__qualityGrade

    @qualityGrade.setter
    def qualityGrade(self, qualityGrade: str):
        self.__qualityGrade = qualityGrade

    @property
    def qualityGradeLevel(self) -> str:
        return self.__qualityGradeLevel

    @qualityGradeLevel.setter
    def qualityGradeLevel(self, qualityGradeLevel: str):
        self.__qualityGradeLevel = qualityGradeLevel

class tracker_Exported(Event):

    pass
class tracker_Imported(Event):

    pass
class tracker_MilkTest(Event):

    def __init__(self, poundsProduced: float, percentButterFat: float, percentProtein: float, somaticCellCounts: int, otherSolids: float):
        self.poundsProduced = poundsProduced
        self.percentButterFat = percentButterFat
        self.percentProtein = percentProtein
        self.somaticCellCounts = somaticCellCounts
        self.otherSolids = otherSolids
        
    @property
    def somaticCellCounts(self) -> int:
        return self.__somaticCellCounts

    @somaticCellCounts.setter
    def somaticCellCounts(self, somaticCellCounts: int):
        self.__somaticCellCounts = somaticCellCounts

    @property
    def poundsProduced(self) -> float:
        return self.__poundsProduced

    @poundsProduced.setter
    def poundsProduced(self, poundsProduced: float):
        self.__poundsProduced = poundsProduced

    @property
    def percentButterFat(self) -> float:
        return self.__percentButterFat

    @percentButterFat.setter
    def percentButterFat(self, percentButterFat: float):
        self.__percentButterFat = percentButterFat

    @property
    def percentProtein(self) -> float:
        return self.__percentProtein

    @percentProtein.setter
    def percentProtein(self, percentProtein: float):
        self.__percentProtein = percentProtein

    @property
    def otherSolids(self) -> float:
        return self.__otherSolids

    @otherSolids.setter
    def otherSolids(self, otherSolids: float):
        self.__otherSolids = otherSolids

class tracker_ReplacedTag(Event):

    def __init__(self, oldId: str, usainNumberUsedForOldId: bool, tracker_ReplacedTag: "tracker_Tag" = None):
        self.oldId = oldId
        self.usainNumberUsedForOldId = usainNumberUsedForOldId
        self.tracker_ReplacedTag = tracker_ReplacedTag
        
    @property
    def oldId(self) -> str:
        return self.__oldId

    @oldId.setter
    def oldId(self, oldId: str):
        self.__oldId = oldId

    @property
    def usainNumberUsedForOldId(self) -> bool:
        return self.__usainNumberUsedForOldId

    @usainNumberUsedForOldId.setter
    def usainNumberUsedForOldId(self, usainNumberUsedForOldId: bool):
        self.__usainNumberUsedForOldId = usainNumberUsedForOldId

    @property
    def tracker_ReplacedTag(self):
        return self.__tracker_ReplacedTag

    @tracker_ReplacedTag.setter
    def tracker_ReplacedTag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_ReplacedTag__tracker_ReplacedTag", None)
        self.__tracker_ReplacedTag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Tag19"):
                opp_val = getattr(old_value, "tracker_Tag19", None)
                if opp_val == self:
                    setattr(old_value, "tracker_Tag19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Tag19"):
                opp_val = getattr(value, "tracker_Tag19", None)
                setattr(value, "tracker_Tag19", self)

class tracker_USBeefGrading(Event):

    def __init__(self, qualityGrade: str, qualityGradeLevel: str, yieldGrade: str):
        self.qualityGrade = qualityGrade
        self.qualityGradeLevel = qualityGradeLevel
        self.yieldGrade = yieldGrade
        
    @property
    def qualityGradeLevel(self) -> str:
        return self.__qualityGradeLevel

    @qualityGradeLevel.setter
    def qualityGradeLevel(self, qualityGradeLevel: str):
        self.__qualityGradeLevel = qualityGradeLevel

    @property
    def yieldGrade(self) -> str:
        return self.__yieldGrade

    @yieldGrade.setter
    def yieldGrade(self, yieldGrade: str):
        self.__yieldGrade = yieldGrade

    @property
    def qualityGrade(self) -> str:
        return self.__qualityGrade

    @qualityGrade.setter
    def qualityGrade(self, qualityGrade: str):
        self.__qualityGrade = qualityGrade

class tracker_USSwineGrading(Event):

    def __init__(self, qualityGrade: str):
        self.qualityGrade = qualityGrade
        
    @property
    def qualityGrade(self) -> str:
        return self.__qualityGrade

    @qualityGrade.setter
    def qualityGrade(self, qualityGrade: str):
        self.__qualityGrade = qualityGrade

class tracker_Slaughtered(Event):

    pass
class tracker_Schema:

    pass
class tracker_Location:

    def __init__(self, name: str, tracker_Location: "tracker_Premises" = None, tracker_Location21: "tracker_Sighting" = None):
        self.name = name
        self.tracker_Location = tracker_Location
        self.tracker_Location21 = tracker_Location21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tracker_Location(self):
        return self.__tracker_Location

    @tracker_Location.setter
    def tracker_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Location__tracker_Location", None)
        self.__tracker_Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Premises15"):
                opp_val = getattr(old_value, "tracker_Premises15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Premises15"):
                opp_val = getattr(value, "tracker_Premises15", None)
                if opp_val is None:
                    setattr(value, "tracker_Premises15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tracker_Location21(self):
        return self.__tracker_Location21

    @tracker_Location21.setter
    def tracker_Location21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Location__tracker_Location21", None)
        self.__tracker_Location21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Sighting"):
                opp_val = getattr(old_value, "tracker_Sighting", None)
                if opp_val == self:
                    setattr(old_value, "tracker_Sighting", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Sighting"):
                opp_val = getattr(value, "tracker_Sighting", None)
                setattr(value, "tracker_Sighting", self)

class tracker_TagAllocated(Event):

    pass
class Animal:

    pass
class tracker_Swine(Animal):

    def __init__(self, swineBreed: str, rightEarNotching: int, leftEarNotching: int):
        self.swineBreed = swineBreed
        self.rightEarNotching = rightEarNotching
        self.leftEarNotching = leftEarNotching
        
    @property
    def swineBreed(self) -> str:
        return self.__swineBreed

    @swineBreed.setter
    def swineBreed(self, swineBreed: str):
        self.__swineBreed = swineBreed

    @property
    def leftEarNotching(self) -> int:
        return self.__leftEarNotching

    @leftEarNotching.setter
    def leftEarNotching(self, leftEarNotching: int):
        self.__leftEarNotching = leftEarNotching

    @property
    def rightEarNotching(self) -> int:
        return self.__rightEarNotching

    @rightEarNotching.setter
    def rightEarNotching(self, rightEarNotching: int):
        self.__rightEarNotching = rightEarNotching

class tracker_Equine(Animal):

    def __init__(self, horseBreed: str):
        self.horseBreed = horseBreed
        
    @property
    def horseBreed(self) -> str:
        return self.__horseBreed

    @horseBreed.setter
    def horseBreed(self, horseBreed: str):
        self.__horseBreed = horseBreed

class tracker_Caprine(Animal):

    def __init__(self, goatBreed: str):
        self.goatBreed = goatBreed
        
    @property
    def goatBreed(self) -> str:
        return self.__goatBreed

    @goatBreed.setter
    def goatBreed(self, goatBreed: str):
        self.__goatBreed = goatBreed

class tracker_Ovine(Animal):

    def __init__(self, sheepBreed: str, scrapieTag: str):
        self.sheepBreed = sheepBreed
        self.scrapieTag = scrapieTag
        
    @property
    def scrapieTag(self) -> str:
        return self.__scrapieTag

    @scrapieTag.setter
    def scrapieTag(self, scrapieTag: str):
        self.__scrapieTag = scrapieTag

    @property
    def sheepBreed(self) -> str:
        return self.__sheepBreed

    @sheepBreed.setter
    def sheepBreed(self, sheepBreed: str):
        self.__sheepBreed = sheepBreed

class tracker_Bovine(Animal):

    pass
class tracker_Event(ABC):

    def __init__(self, dateTime: date, eventCode: int, electronicallyRead: bool, correction: bool, comments: str, id: str, Event: "tracker_Tag" = None, events: "tracker_Tag" = None):
        self.dateTime = dateTime
        self.eventCode = eventCode
        self.electronicallyRead = electronicallyRead
        self.correction = correction
        self.comments = comments
        self.id = id
        self.Event = Event
        self.events = events
        
    @property
    def eventCode(self) -> int:
        return self.__eventCode

    @eventCode.setter
    def eventCode(self, eventCode: int):
        self.__eventCode = eventCode

    @property
    def dateTime(self) -> date:
        return self.__dateTime

    @dateTime.setter
    def dateTime(self, dateTime: date):
        self.__dateTime = dateTime

    @property
    def correction(self) -> bool:
        return self.__correction

    @correction.setter
    def correction(self, correction: bool):
        self.__correction = correction

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def electronicallyRead(self) -> bool:
        return self.__electronicallyRead

    @electronicallyRead.setter
    def electronicallyRead(self, electronicallyRead: bool):
        self.__electronicallyRead = electronicallyRead

    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Event__events", None)
        self.__events = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tag"):
                opp_val = getattr(old_value, "Tag", None)
                if opp_val == self:
                    setattr(old_value, "Tag", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tag"):
                opp_val = getattr(value, "Tag", None)
                setattr(value, "Tag", self)

    @property
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Event__Event", None)
        self.__Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tag"):
                opp_val = getattr(old_value, "tag", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tag"):
                opp_val = getattr(value, "tag", None)
                if opp_val is None:
                    setattr(value, "tag", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tracker_Tag:

    def __init__(self, usainNumberUsed: bool, id: str, tracker_Tag: "tracker_Animal" = None, tag: set["tracker_Event"] = None, Tag: "tracker_Event" = None, tracker_Tag13: "tracker_Premises" = None, tracker_Tag19: "tracker_ReplacedTag" = None):
        self.usainNumberUsed = usainNumberUsed
        self.id = id
        self.tracker_Tag = tracker_Tag
        self.tag = tag if tag is not None else set()
        self.Tag = Tag
        self.tracker_Tag13 = tracker_Tag13
        self.tracker_Tag19 = tracker_Tag19
        
    @property
    def usainNumberUsed(self) -> bool:
        return self.__usainNumberUsed

    @usainNumberUsed.setter
    def usainNumberUsed(self, usainNumberUsed: bool):
        self.__usainNumberUsed = usainNumberUsed

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def tracker_Tag(self):
        return self.__tracker_Tag

    @tracker_Tag.setter
    def tracker_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Tag__tracker_Tag", None)
        self.__tracker_Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Animal"):
                opp_val = getattr(old_value, "tracker_Animal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Animal"):
                opp_val = getattr(value, "tracker_Animal", None)
                if opp_val is None:
                    setattr(value, "tracker_Animal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Tag(self):
        return self.__Tag

    @Tag.setter
    def Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Tag__Tag", None)
        self.__Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events"):
                opp_val = getattr(old_value, "events", None)
                if opp_val == self:
                    setattr(old_value, "events", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events"):
                opp_val = getattr(value, "events", None)
                setattr(value, "events", self)

    @property
    def tracker_Tag13(self):
        return self.__tracker_Tag13

    @tracker_Tag13.setter
    def tracker_Tag13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Tag__tracker_Tag13", None)
        self.__tracker_Tag13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Premises12"):
                opp_val = getattr(old_value, "tracker_Premises12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Premises12"):
                opp_val = getattr(value, "tracker_Premises12", None)
                if opp_val is None:
                    setattr(value, "tracker_Premises12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Tag__tag", None)
        self.__tag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    if opp_val == self:
                        setattr(item, "Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    setattr(item, "Event", self)
                    

    @property
    def tracker_Tag19(self):
        return self.__tracker_Tag19

    @tracker_Tag19.setter
    def tracker_Tag19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Tag__tracker_Tag19", None)
        self.__tracker_Tag19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_ReplacedTag"):
                opp_val = getattr(old_value, "tracker_ReplacedTag", None)
                if opp_val == self:
                    setattr(old_value, "tracker_ReplacedTag", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_ReplacedTag"):
                opp_val = getattr(value, "tracker_ReplacedTag", None)
                setattr(value, "tracker_ReplacedTag", self)

class tracker_Animal(ABC):

    def __init__(self, birthDate: date, sex: str, sexCode: str, speciesCode: str, id: str, comments: str, lastEventDateTime: date, weight: str, weightGainPerDay: str, type: str, visualID: str, ageInDays: int, alternativeID: str, species: str, breed: str, tracker_Animal3: "tracker_Animal" = None, tracker_Animal1: "tracker_Animal" = None, tracker_Animal6: "tracker_Animal" = None, tracker_Animal4: "tracker_Animal" = None, tracker_Animal: set["tracker_Tag"] = None, tracker_Animal10: "tracker_Premises" = None):
        self.birthDate = birthDate
        self.sex = sex
        self.sexCode = sexCode
        self.speciesCode = speciesCode
        self.id = id
        self.comments = comments
        self.lastEventDateTime = lastEventDateTime
        self.weight = weight
        self.weightGainPerDay = weightGainPerDay
        self.type = type
        self.visualID = visualID
        self.ageInDays = ageInDays
        self.alternativeID = alternativeID
        self.species = species
        self.breed = breed
        self.tracker_Animal3 = tracker_Animal3
        self.tracker_Animal1 = tracker_Animal1
        self.tracker_Animal6 = tracker_Animal6
        self.tracker_Animal4 = tracker_Animal4
        self.tracker_Animal = tracker_Animal if tracker_Animal is not None else set()
        self.tracker_Animal10 = tracker_Animal10
        
    @property
    def species(self) -> str:
        return self.__species

    @species.setter
    def species(self, species: str):
        self.__species = species

    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

    @property
    def breed(self) -> str:
        return self.__breed

    @breed.setter
    def breed(self, breed: str):
        self.__breed = breed

    @property
    def speciesCode(self) -> str:
        return self.__speciesCode

    @speciesCode.setter
    def speciesCode(self, speciesCode: str):
        self.__speciesCode = speciesCode

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def alternativeID(self) -> str:
        return self.__alternativeID

    @alternativeID.setter
    def alternativeID(self, alternativeID: str):
        self.__alternativeID = alternativeID

    @property
    def birthDate(self) -> date:
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, birthDate: date):
        self.__birthDate = birthDate

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def lastEventDateTime(self) -> date:
        return self.__lastEventDateTime

    @lastEventDateTime.setter
    def lastEventDateTime(self, lastEventDateTime: date):
        self.__lastEventDateTime = lastEventDateTime

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

    @property
    def ageInDays(self) -> int:
        return self.__ageInDays

    @ageInDays.setter
    def ageInDays(self, ageInDays: int):
        self.__ageInDays = ageInDays

    @property
    def sexCode(self) -> str:
        return self.__sexCode

    @sexCode.setter
    def sexCode(self, sexCode: str):
        self.__sexCode = sexCode

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def visualID(self) -> str:
        return self.__visualID

    @visualID.setter
    def visualID(self, visualID: str):
        self.__visualID = visualID

    @property
    def weightGainPerDay(self) -> str:
        return self.__weightGainPerDay

    @weightGainPerDay.setter
    def weightGainPerDay(self, weightGainPerDay: str):
        self.__weightGainPerDay = weightGainPerDay

    @property
    def tracker_Animal(self):
        return self.__tracker_Animal

    @tracker_Animal.setter
    def tracker_Animal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Animal__tracker_Animal", None)
        self.__tracker_Animal = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tracker_Tag"):
                    opp_val = getattr(item, "tracker_Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "tracker_Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tracker_Tag"):
                    opp_val = getattr(item, "tracker_Tag", None)
                    
                    setattr(item, "tracker_Tag", self)
                    

    @property
    def tracker_Animal4(self):
        return self.__tracker_Animal4

    @tracker_Animal4.setter
    def tracker_Animal4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Animal__tracker_Animal4", None)
        self.__tracker_Animal4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Animal6"):
                opp_val = getattr(old_value, "tracker_Animal6", None)
                if opp_val == self:
                    setattr(old_value, "tracker_Animal6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Animal6"):
                opp_val = getattr(value, "tracker_Animal6", None)
                setattr(value, "tracker_Animal6", self)

    @property
    def tracker_Animal6(self):
        return self.__tracker_Animal6

    @tracker_Animal6.setter
    def tracker_Animal6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Animal__tracker_Animal6", None)
        self.__tracker_Animal6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Animal4"):
                opp_val = getattr(old_value, "tracker_Animal4", None)
                if opp_val == self:
                    setattr(old_value, "tracker_Animal4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Animal4"):
                opp_val = getattr(value, "tracker_Animal4", None)
                setattr(value, "tracker_Animal4", self)

    @property
    def tracker_Animal10(self):
        return self.__tracker_Animal10

    @tracker_Animal10.setter
    def tracker_Animal10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Animal__tracker_Animal10", None)
        self.__tracker_Animal10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Premises"):
                opp_val = getattr(old_value, "tracker_Premises", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Premises"):
                opp_val = getattr(value, "tracker_Premises", None)
                if opp_val is None:
                    setattr(value, "tracker_Premises", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tracker_Animal1(self):
        return self.__tracker_Animal1

    @tracker_Animal1.setter
    def tracker_Animal1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Animal__tracker_Animal1", None)
        self.__tracker_Animal1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Animal3"):
                opp_val = getattr(old_value, "tracker_Animal3", None)
                if opp_val == self:
                    setattr(old_value, "tracker_Animal3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Animal3"):
                opp_val = getattr(value, "tracker_Animal3", None)
                setattr(value, "tracker_Animal3", self)

    @property
    def tracker_Animal3(self):
        return self.__tracker_Animal3

    @tracker_Animal3.setter
    def tracker_Animal3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Animal__tracker_Animal3", None)
        self.__tracker_Animal3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Animal1"):
                opp_val = getattr(old_value, "tracker_Animal1", None)
                if opp_val == self:
                    setattr(old_value, "tracker_Animal1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Animal1"):
                opp_val = getattr(value, "tracker_Animal1", None)
                setattr(value, "tracker_Animal1", self)

    def addTemplate(self, eventTemplate: str):
        # TODO: Implement addTemplate method
        pass

    def getAge(self) -> str:
        # TODO: Implement getAge method
        pass

    def allEvents(self) -> str:
        # TODO: Implement allEvents method
        pass

    def eventHistory(self) -> str:
        # TODO: Implement eventHistory method
        pass

    def activeTag(self) -> str:
        # TODO: Implement activeTag method
        pass

    def lastWeighIn(self) -> str:
        # TODO: Implement lastWeighIn method
        pass
