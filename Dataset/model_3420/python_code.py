from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SwineBreed(Enum):
    WS = "WS"
    YO = "YO"
    Unspecified = "Unspecified"
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
class BisonBreed(Enum):
    WO = "WO"
    PB = "PB"
    Unspecified = "Unspecified"
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
class BeefBreed(Enum):
    BM = "BM"
    BB = "BB"
    BG = "BG"
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
    DR = "DR"
    DL = "DL"
    FP = "FP"
    BD = "BD"
    NS = "NS"
    BO = "BO"
    BR = "BR"
    BH = "BH"
    BI = "BI"
    BL = "BL"
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
    KB = "KB"
    ER = "ER"
    FA = "FA"
    FL = "FL"
    FC = "FC"
    FR = "FR"
    FB = "FB"
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
    RB = "RB"
    LM = "LM"
    RD = "RD"
    LR = "LR"
    RP = "RP"
    LO = "LO"
    RN = "RN"
    LU = "LU"
    MA = "MA"
    MH = "MH"
    ML = "ML"
    MR = "MR"
    ME = "ME"
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
    TN = "TN"
    TL = "TL"
    TI = "TI"
    RS = "RS"
    RO = "RO"
    DN = "DN"
    SW = "SW"
    SA = "SA"
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
    WB = "WB"
    WF = "WF"
    WP = "WP"
    YA = "YA"
    Unspecified = "Unspecified"
class SheepBreed(Enum):
    DL = "DL"
    ER = "ER"
    CD = "CD"
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
    ST = "ST"
    SU = "SU"
    FN = "FN"
    HS = "HS"
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
    MT = "MT"
    NL = "NL"
    NC = "NC"
    OX = "OX"
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
    TA = "TA"
    TX = "TX"
    TU = "TU"
    XL = "XL"
    XM = "XM"
    ZS = "ZS"
    Unspecified = "Unspecified"
class Sex(Enum):
    F = "F"
    M = "M"
    C = "C"
    S = "S"
    Unspecified = "Unspecified"


############################################
# Definition of Classes
############################################

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

class tracker_UnAppliedTags:

    pass
class tracker_EventHistory:

    pass
class tracker_Animals:

    pass
class tracker_Premises:

    def __init__(self, premisesId: str, emailContact: str, tracker_Premises: "tracker_Animals" = None, tracker_Premises5: "tracker_EventHistory" = None, tracker_Premises7: "tracker_UnAppliedTags" = None):
        self.premisesId = premisesId
        self.emailContact = emailContact
        self.tracker_Premises = tracker_Premises
        self.tracker_Premises5 = tracker_Premises5
        self.tracker_Premises7 = tracker_Premises7
        
    @property
    def premisesId(self) -> str:
        return self.__premisesId

    @premisesId.setter
    def premisesId(self, premisesId: str):
        self.__premisesId = premisesId

    @property
    def emailContact(self) -> str:
        return self.__emailContact

    @emailContact.setter
    def emailContact(self, emailContact: str):
        self.__emailContact = emailContact

    @property
    def tracker_Premises7(self):
        return self.__tracker_Premises7

    @tracker_Premises7.setter
    def tracker_Premises7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Premises__tracker_Premises7", None)
        self.__tracker_Premises7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_UnAppliedTags"):
                opp_val = getattr(old_value, "tracker_UnAppliedTags", None)
                if opp_val == self:
                    setattr(old_value, "tracker_UnAppliedTags", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_UnAppliedTags"):
                opp_val = getattr(value, "tracker_UnAppliedTags", None)
                setattr(value, "tracker_UnAppliedTags", self)

    @property
    def tracker_Premises(self):
        return self.__tracker_Premises

    @tracker_Premises.setter
    def tracker_Premises(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Premises__tracker_Premises", None)
        self.__tracker_Premises = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Animals"):
                opp_val = getattr(old_value, "tracker_Animals", None)
                if opp_val == self:
                    setattr(old_value, "tracker_Animals", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Animals"):
                opp_val = getattr(value, "tracker_Animals", None)
                setattr(value, "tracker_Animals", self)

    @property
    def tracker_Premises5(self):
        return self.__tracker_Premises5

    @tracker_Premises5.setter
    def tracker_Premises5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Premises__tracker_Premises5", None)
        self.__tracker_Premises5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_EventHistory"):
                opp_val = getattr(old_value, "tracker_EventHistory", None)
                if opp_val == self:
                    setattr(old_value, "tracker_EventHistory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_EventHistory"):
                opp_val = getattr(value, "tracker_EventHistory", None)
                setattr(value, "tracker_EventHistory", self)

class Event:

    pass
class tracker_TagRetired(Event):

    pass
class tracker_ICVI(Event):

    pass
class tracker_ReplacedTag(Event):

    def __init__(self, oldAin: str):
        self.oldAin = oldAin
        
    @property
    def oldAin(self) -> str:
        return self.__oldAin

    @oldAin.setter
    def oldAin(self, oldAin: str):
        self.__oldAin = oldAin

class tracker_Exported(Event):

    pass
class tracker_MovedIn(Event):

    def __init__(self, sourcePin: str):
        self.sourcePin = sourcePin
        
    @property
    def sourcePin(self) -> str:
        return self.__sourcePin

    @sourcePin.setter
    def sourcePin(self, sourcePin: str):
        self.__sourcePin = sourcePin

class tracker_Slaughtered(Event):

    pass
class tracker_WeighIn(Event):

    def __init__(self, weight: int):
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

class tracker_AnimalMissing(Event):

    pass
class tracker_TagApplied(Event):

    pass
class tracker_Died(Event):

    pass
class tracker_Imported(Event):

    pass
class tracker_LostTag(Event):

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

class tracker_FairRegistration(Event):

    def __init__(self, participant: str, address: str, phone: str, parent: str, club: str):
        self.participant = participant
        self.address = address
        self.phone = phone
        self.parent = parent
        self.club = club
        
    @property
    def club(self) -> str:
        return self.__club

    @club.setter
    def club(self, club: str):
        self.__club = club

    @property
    def participant(self) -> str:
        return self.__participant

    @participant.setter
    def participant(self, participant: str):
        self.__participant = participant

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def parent(self) -> str:
        return self.__parent

    @parent.setter
    def parent(self, parent: str):
        self.__parent = parent

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class tracker_Sighting(Event):

    pass
class tracker_TagAllocated(Event):

    pass
class tracker_Event(ABC):

    def __init__(self, dateTime: str, eventCode: int, electronicallyRead: bool, correction: bool, comments: str, id: str, tracker_Event: "tracker_AnimalId" = None, tracker_Event10: "tracker_EventHistory" = None):
        self.dateTime = dateTime
        self.eventCode = eventCode
        self.electronicallyRead = electronicallyRead
        self.correction = correction
        self.comments = comments
        self.id = id
        self.tracker_Event = tracker_Event
        self.tracker_Event10 = tracker_Event10
        
    @property
    def correction(self) -> bool:
        return self.__correction

    @correction.setter
    def correction(self, correction: bool):
        self.__correction = correction

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dateTime(self) -> str:
        return self.__dateTime

    @dateTime.setter
    def dateTime(self, dateTime: str):
        self.__dateTime = dateTime

    @property
    def eventCode(self) -> int:
        return self.__eventCode

    @eventCode.setter
    def eventCode(self, eventCode: int):
        self.__eventCode = eventCode

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def electronicallyRead(self) -> bool:
        return self.__electronicallyRead

    @electronicallyRead.setter
    def electronicallyRead(self, electronicallyRead: bool):
        self.__electronicallyRead = electronicallyRead

    @property
    def tracker_Event(self):
        return self.__tracker_Event

    @tracker_Event.setter
    def tracker_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Event__tracker_Event", None)
        self.__tracker_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_AnimalId2"):
                opp_val = getattr(old_value, "tracker_AnimalId2", None)
                if opp_val == self:
                    setattr(old_value, "tracker_AnimalId2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_AnimalId2"):
                opp_val = getattr(value, "tracker_AnimalId2", None)
                setattr(value, "tracker_AnimalId2", self)

    @property
    def tracker_Event10(self):
        return self.__tracker_Event10

    @tracker_Event10.setter
    def tracker_Event10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Event__tracker_Event10", None)
        self.__tracker_Event10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_EventHistory9"):
                opp_val = getattr(old_value, "tracker_EventHistory9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_EventHistory9"):
                opp_val = getattr(value, "tracker_EventHistory9", None)
                if opp_val is None:
                    setattr(value, "tracker_EventHistory9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Animal:

    pass
class tracker_Ovine(Animal):

    def __init__(self, sheepBreed: str):
        self.sheepBreed = sheepBreed
        
    @property
    def sheepBreed(self) -> str:
        return self.__sheepBreed

    @sheepBreed.setter
    def sheepBreed(self, sheepBreed: str):
        self.__sheepBreed = sheepBreed

class tracker_Swine(Animal):

    def __init__(self, swineBreed: str):
        self.swineBreed = swineBreed
        
    @property
    def swineBreed(self) -> str:
        return self.__swineBreed

    @swineBreed.setter
    def swineBreed(self, swineBreed: str):
        self.__swineBreed = swineBreed

class tracker_Bovine(Animal):

    pass
class tracker_Animal(ABC):

    def __init__(self, birthDate: str, sex: str, species: str, idNumber: str, breed: str, age: str, sexCode: str, speciesCode: str, tracker_Animal: "tracker_AnimalId" = None, tracker_Animal13: "tracker_Animals" = None):
        self.birthDate = birthDate
        self.sex = sex
        self.species = species
        self.idNumber = idNumber
        self.breed = breed
        self.age = age
        self.sexCode = sexCode
        self.speciesCode = speciesCode
        self.tracker_Animal = tracker_Animal
        self.tracker_Animal13 = tracker_Animal13
        
    @property
    def idNumber(self) -> str:
        return self.__idNumber

    @idNumber.setter
    def idNumber(self, idNumber: str):
        self.__idNumber = idNumber

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
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age

    @property
    def breed(self) -> str:
        return self.__breed

    @breed.setter
    def breed(self, breed: str):
        self.__breed = breed

    @property
    def sexCode(self) -> str:
        return self.__sexCode

    @sexCode.setter
    def sexCode(self, sexCode: str):
        self.__sexCode = sexCode

    @property
    def birthDate(self) -> str:
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, birthDate: str):
        self.__birthDate = birthDate

    @property
    def speciesCode(self) -> str:
        return self.__speciesCode

    @speciesCode.setter
    def speciesCode(self, speciesCode: str):
        self.__speciesCode = speciesCode

    @property
    def tracker_Animal13(self):
        return self.__tracker_Animal13

    @tracker_Animal13.setter
    def tracker_Animal13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Animal__tracker_Animal13", None)
        self.__tracker_Animal13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Animals12"):
                opp_val = getattr(old_value, "tracker_Animals12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Animals12"):
                opp_val = getattr(value, "tracker_Animals12", None)
                if opp_val is None:
                    setattr(value, "tracker_Animals12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tracker_Animal(self):
        return self.__tracker_Animal

    @tracker_Animal.setter
    def tracker_Animal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Animal__tracker_Animal", None)
        self.__tracker_Animal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_AnimalId"):
                opp_val = getattr(old_value, "tracker_AnimalId", None)
                if opp_val == self:
                    setattr(old_value, "tracker_AnimalId", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_AnimalId"):
                opp_val = getattr(value, "tracker_AnimalId", None)
                setattr(value, "tracker_AnimalId", self)

class tracker_AnimalId:

    def __init__(self, idNumber: str, usainNumberUsed: bool, tracker_AnimalId: "tracker_Animal" = None, tracker_AnimalId2: "tracker_Event" = None, tracker_AnimalId16: "tracker_UnAppliedTags" = None):
        self.idNumber = idNumber
        self.usainNumberUsed = usainNumberUsed
        self.tracker_AnimalId = tracker_AnimalId
        self.tracker_AnimalId2 = tracker_AnimalId2
        self.tracker_AnimalId16 = tracker_AnimalId16
        
    @property
    def usainNumberUsed(self) -> bool:
        return self.__usainNumberUsed

    @usainNumberUsed.setter
    def usainNumberUsed(self, usainNumberUsed: bool):
        self.__usainNumberUsed = usainNumberUsed

    @property
    def idNumber(self) -> str:
        return self.__idNumber

    @idNumber.setter
    def idNumber(self, idNumber: str):
        self.__idNumber = idNumber

    @property
    def tracker_AnimalId2(self):
        return self.__tracker_AnimalId2

    @tracker_AnimalId2.setter
    def tracker_AnimalId2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_AnimalId__tracker_AnimalId2", None)
        self.__tracker_AnimalId2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Event"):
                opp_val = getattr(old_value, "tracker_Event", None)
                if opp_val == self:
                    setattr(old_value, "tracker_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Event"):
                opp_val = getattr(value, "tracker_Event", None)
                setattr(value, "tracker_Event", self)

    @property
    def tracker_AnimalId16(self):
        return self.__tracker_AnimalId16

    @tracker_AnimalId16.setter
    def tracker_AnimalId16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_AnimalId__tracker_AnimalId16", None)
        self.__tracker_AnimalId16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_UnAppliedTags15"):
                opp_val = getattr(old_value, "tracker_UnAppliedTags15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_UnAppliedTags15"):
                opp_val = getattr(value, "tracker_UnAppliedTags15", None)
                if opp_val is None:
                    setattr(value, "tracker_UnAppliedTags15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tracker_AnimalId(self):
        return self.__tracker_AnimalId

    @tracker_AnimalId.setter
    def tracker_AnimalId(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_AnimalId__tracker_AnimalId", None)
        self.__tracker_AnimalId = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Animal"):
                opp_val = getattr(old_value, "tracker_Animal", None)
                if opp_val == self:
                    setattr(old_value, "tracker_Animal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Animal"):
                opp_val = getattr(value, "tracker_Animal", None)
                setattr(value, "tracker_Animal", self)
