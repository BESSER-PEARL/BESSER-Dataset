from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SheepBreed(Enum):
    CD = "CD"
    OU = "OU"
    RI = "RI"
    LY = "LY"
    FB = "FB"
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
    ST = "ST"
    SU = "SU"
    TA = "TA"
    TX = "TX"
    TU = "TU"
    XL = "XL"
    XM = "XM"
    ZS = "ZS"
    Unspecified = "Unspecified"
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
    FN = "FN"
    HS = "HS"
    HY = "HY"
    IL = "IL"
    KK = "KK"
    KA = "KA"
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
class Sex(Enum):
    F = "F"
    M = "M"
    C = "C"
    S = "S"
    Unspecified = "Unspecified"
class SwineBreed(Enum):
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
    BK = "BK"
    CW = "CW"
    DU = "DU"
class BeefBreed(Enum):
    AN = "AN"
    AB = "AB"
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
    DR = "DR"
    DL = "DL"
    FP = "FP"
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
    NS = "NS"
    BO = "BO"
    BR = "BR"
    BH = "BH"
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
    RB = "RB"
    RD = "RD"
    RP = "RP"
    RN = "RN"
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
    MA = "MA"
    MH = "MH"
    YA = "YA"
    Unspecified = "Unspecified"
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
class BisonBreed(Enum):
    WO = "WO"
    PB = "PB"
    Unspecified = "Unspecified"


############################################
# Definition of Classes
############################################

class Bovine:

    pass
class tracker_BovineDairy(Bovine):

    def __init__(self, dairyBreed: str):
        self.dairyBreed = dairyBreed
        
        pass
    @property
    def dairyBreed(self):
        return self.__dairyBreed

    @dairyBreed.setter
    def dairyBreed(self, dairyBreed: str):
        self.__dairyBreed = dairyBreed


class tracker_BovineBison(Bovine):

    def __init__(self, buffaloBreed: str):
        self.buffaloBreed = buffaloBreed
        
        pass
    @property
    def buffaloBreed(self):
        return self.__buffaloBreed

    @buffaloBreed.setter
    def buffaloBreed(self, buffaloBreed: str):
        self.__buffaloBreed = buffaloBreed


class tracker_BovineBeef(Bovine):

    def __init__(self, beefBreed: str):
        self.beefBreed = beefBreed
        
        pass
    @property
    def beefBreed(self):
        return self.__beefBreed

    @beefBreed.setter
    def beefBreed(self, beefBreed: str):
        self.__beefBreed = beefBreed


class Animal:

    pass
class tracker_Swine(Animal):

    def __init__(self, swineBreed: str):
        self.swineBreed = swineBreed
        
        pass
    @property
    def swineBreed(self):
        return self.__swineBreed

    @swineBreed.setter
    def swineBreed(self, swineBreed: str):
        self.__swineBreed = swineBreed


class tracker_Ovine(Animal):

    def __init__(self, sheepBreed: str):
        self.sheepBreed = sheepBreed
        
        pass
    @property
    def sheepBreed(self):
        return self.__sheepBreed

    @sheepBreed.setter
    def sheepBreed(self, sheepBreed: str):
        self.__sheepBreed = sheepBreed


class tracker_Bovine(Animal):

    pass
class tracker_Event(ABC):

    def __init__(self, id: str, dateTime: str, eventCode: int, electronicallyRead: bool, correction: bool, comments: str, idNumber: str, events: "tracker_Tag" = None, Event: "tracker_Tag" = None):
        self.id = id
        self.dateTime = dateTime
        self.eventCode = eventCode
        self.electronicallyRead = electronicallyRead
        self.correction = correction
        self.comments = comments
        self.idNumber = idNumber
        self.events = events
        self.Event = Event
        
        pass
    @property
    def correction(self):
        return self.__correction

    @correction.setter
    def correction(self, correction: bool):
        self.__correction = correction


    @property
    def electronicallyRead(self):
        return self.__electronicallyRead

    @electronicallyRead.setter
    def electronicallyRead(self, electronicallyRead: bool):
        self.__electronicallyRead = electronicallyRead


    @property
    def idNumber(self):
        return self.__idNumber

    @idNumber.setter
    def idNumber(self, idNumber: str):
        self.__idNumber = idNumber


    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def dateTime(self):
        return self.__dateTime

    @dateTime.setter
    def dateTime(self, dateTime: str):
        self.__dateTime = dateTime


    @property
    def eventCode(self):
        return self.__eventCode

    @eventCode.setter
    def eventCode(self, eventCode: int):
        self.__eventCode = eventCode


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

class tracker_Premises:

    def __init__(self, premisesId: str, emailContact: str, tracker_Premises: set["tracker_Animal"] = None, tracker_Premises6: set["tracker_Tag"] = None):
        self.premisesId = premisesId
        self.emailContact = emailContact
        self.tracker_Premises = tracker_Premises if tracker_Premises is not None else set()
        self.tracker_Premises6 = tracker_Premises6 if tracker_Premises6 is not None else set()
        
        pass
    @property
    def emailContact(self):
        return self.__emailContact

    @emailContact.setter
    def emailContact(self, emailContact: str):
        self.__emailContact = emailContact


    @property
    def premisesId(self):
        return self.__premisesId

    @premisesId.setter
    def premisesId(self, premisesId: str):
        self.__premisesId = premisesId


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
                if hasattr(item, "tracker_Animal4"):
                    opp_val = getattr(item, "tracker_Animal4", None)
                    
                    if opp_val == self:
                        setattr(item, "tracker_Animal4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tracker_Animal4"):
                    opp_val = getattr(item, "tracker_Animal4", None)
                    
                    setattr(item, "tracker_Animal4", self)
                    

    @property
    def tracker_Premises6(self):
        return self.__tracker_Premises6

    @tracker_Premises6.setter
    def tracker_Premises6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Premises__tracker_Premises6", None)
        self.__tracker_Premises6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tracker_Tag7"):
                    opp_val = getattr(item, "tracker_Tag7", None)
                    
                    if opp_val == self:
                        setattr(item, "tracker_Tag7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tracker_Tag7"):
                    opp_val = getattr(item, "tracker_Tag7", None)
                    
                    setattr(item, "tracker_Tag7", self)
                    

    def findAnimal(self, tracker_ains) :
        # TODO: Implement findAnimal method
        pass

    def addTemplate(self, tracker_animalTemplate, tracker_ains):
        # TODO: Implement addTemplate method
        pass

    def eventHistory(self) :
        # TODO: Implement eventHistory method
        pass

class Event:

    pass
class tracker_ICVI(Event):

    pass
class tracker_TagApplied(Event):

    pass
class tracker_WeighIn(Event):

    def __init__(self, weight: int):
        self.weight = weight
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight


class tracker_MovedOut(Event):

    def __init__(self, destinationPin: str):
        self.destinationPin = destinationPin
        
        pass
    @property
    def destinationPin(self):
        return self.__destinationPin

    @destinationPin.setter
    def destinationPin(self, destinationPin: str):
        self.__destinationPin = destinationPin


class tracker_MovedIn(Event):

    def __init__(self, sourcePin: str):
        self.sourcePin = sourcePin
        
        pass
    @property
    def sourcePin(self):
        return self.__sourcePin

    @sourcePin.setter
    def sourcePin(self, sourcePin: str):
        self.__sourcePin = sourcePin


class tracker_Imported(Event):

    pass
class tracker_LostTag(Event):

    pass
class tracker_Exported(Event):

    pass
class tracker_Sighting(Event):

    pass
class tracker_AnimalMissing(Event):

    pass
class tracker_TagRetired(Event):

    pass
class tracker_Slaughtered(Event):

    pass
class tracker_Died(Event):

    pass
class tracker_FairRegistration(Event):

    def __init__(self, participant: str, address: str, phone: str, parent: str, club: str):
        self.participant = participant
        self.address = address
        self.phone = phone
        self.parent = parent
        self.club = club
        
        pass
    @property
    def participant(self):
        return self.__participant

    @participant.setter
    def participant(self, participant: str):
        self.__participant = participant


    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent: str):
        self.__parent = parent


    @property
    def club(self):
        return self.__club

    @club.setter
    def club(self, club: str):
        self.__club = club


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone


class tracker_ReplacedTag(Event):

    def __init__(self, oldAin: str):
        self.oldAin = oldAin
        
        pass
    @property
    def oldAin(self):
        return self.__oldAin

    @oldAin.setter
    def oldAin(self, oldAin: str):
        self.__oldAin = oldAin


class tracker_TagAllocated(Event):

    pass
class tracker_Animal(ABC):

    def __init__(self, birthDate: str, sex: str, species: str, idNumber: str, breed: str, age: str, sexCode: str, speciesCode: str, id: str, tracker_Animal: set["tracker_Tag"] = None, tracker_Animal4: "tracker_Premises" = None):
        self.birthDate = birthDate
        self.sex = sex
        self.species = species
        self.idNumber = idNumber
        self.breed = breed
        self.age = age
        self.sexCode = sexCode
        self.speciesCode = speciesCode
        self.id = id
        self.tracker_Animal = tracker_Animal if tracker_Animal is not None else set()
        self.tracker_Animal4 = tracker_Animal4
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species: str):
        self.__species = species


    @property
    def breed(self):
        return self.__breed

    @breed.setter
    def breed(self, breed: str):
        self.__breed = breed


    @property
    def birthDate(self):
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, birthDate: str):
        self.__birthDate = birthDate


    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex


    @property
    def speciesCode(self):
        return self.__speciesCode

    @speciesCode.setter
    def speciesCode(self, speciesCode: str):
        self.__speciesCode = speciesCode


    @property
    def sexCode(self):
        return self.__sexCode

    @sexCode.setter
    def sexCode(self, sexCode: str):
        self.__sexCode = sexCode


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age


    @property
    def idNumber(self):
        return self.__idNumber

    @idNumber.setter
    def idNumber(self, idNumber: str):
        self.__idNumber = idNumber


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
                    

    def addTemplate(self, tracker_eventTemplate):
        # TODO: Implement addTemplate method
        pass

    def activeTag(self) :
        # TODO: Implement activeTag method
        pass

    def allEvents(self) :
        # TODO: Implement allEvents method
        pass

class tracker_Tag:

    def __init__(self, idNumber: str, usainNumberUsed: bool, id: str, tracker_Tag: "tracker_Animal" = None, Tag: "tracker_Event" = None, tracker_Tag7: "tracker_Premises" = None, tag: set["tracker_Event"] = None):
        self.idNumber = idNumber
        self.usainNumberUsed = usainNumberUsed
        self.id = id
        self.tracker_Tag = tracker_Tag
        self.Tag = Tag
        self.tracker_Tag7 = tracker_Tag7
        self.tag = tag if tag is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def usainNumberUsed(self):
        return self.__usainNumberUsed

    @usainNumberUsed.setter
    def usainNumberUsed(self, usainNumberUsed: bool):
        self.__usainNumberUsed = usainNumberUsed


    @property
    def idNumber(self):
        return self.__idNumber

    @idNumber.setter
    def idNumber(self, idNumber: str):
        self.__idNumber = idNumber


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
    def tracker_Tag7(self):
        return self.__tracker_Tag7

    @tracker_Tag7.setter
    def tracker_Tag7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracker_Tag__tracker_Tag7", None)
        self.__tracker_Tag7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracker_Premises6"):
                opp_val = getattr(old_value, "tracker_Premises6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracker_Premises6"):
                opp_val = getattr(value, "tracker_Premises6", None)
                if opp_val is None:
                    setattr(value, "tracker_Premises6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
