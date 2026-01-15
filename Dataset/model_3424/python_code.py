from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Sex(Enum):
    Female = "Female"
    Male = "Male"
    GenderUnknown = "GenderUnknown"
    SpayedFemale = "SpayedFemale"
    NeuteredMale = "NeuteredMale"
    TrueHermaphrodite = "TrueHermaphrodite"
    Other = "Other"
class PhoneDevice(Enum):
    Landline = "Landline"
    Cellphone = "Cellphone"
    Fax = "Fax"
    Unknown = "Unknown"
class ResultName(Enum):
    RESULT = "RESULT"
    COMMENT = "COMMENT"
class MovementPurpose(Enum):
    slaughter = "slaughter"
    medicalTreatment = "medicalTreatment"
    other = "other"
    show = "show"
    race = "race"
    rodeo = "rodeo"
    sale = "sale"
    pet = "pet"
    breeding = "breeding"
    feeding = "feeding"
    grazing = "grazing"
    training = "training"
class ProgramStatusName(Enum):
    BovineTuberculosis = "BovineTuberculosis"
    BrucellosisState = "BrucellosisState"
    BrucellosisHerd = "BrucellosisHerd"
class SpeciesCode(Enum):
    OVI = "OVI"
    POR = "POR"
    UNK = "UNK"
    BOV = "BOV"
    CAP = "CAP"
    CER = "CER"
    EQU = "EQU"
class ProgramStatusValue(Enum):
    Free = "Free"
    ModifiedAccredited = "ModifiedAccredited"
    ModifiedAdvancedAccredited = "ModifiedAdvancedAccredited"
    Other = "Other"
class DocType(Enum):
    ScannedPaperCVI = "ScannedPaperCVI"
    ScannedTestChart = "ScannedTestChart"
    PDFCVI = "PDFCVI"
    PDFTestChart = "PDFTestChart"
    Other = "Other"
class TagType(Enum):
    UN = "UN"
    AIN = "AIN"
    AMID = "AMID"
    BRAND = "BRAND"
    BRANDIMAGE = "BRANDIMAGE"
    BT = "BT"
    IMP = "IMP"
    MGT = "MGT"
    N840RFID = "N840RFID"
    NUES8 = "NUES8"
    NUES9 = "NUES9"
    OFORID = "OFORID"
    OTH = "OTH"
    NAME = "NAME"
    SGFLID = "SGFLID"
    NPIN = "NPIN"
    TAT = "TAT"
class ISO3166Country(Enum):
    USA = "USA"
class UsState(Enum):
    CA = "CA"
    CO = "CO"
    CT = "CT"
    DC = "DC"
    DE = "DE"
    FL = "FL"
    AA = "AA"
    AE = "AE"
    AK = "AK"
    AL = "AL"
    AP = "AP"
    AR = "AR"
    AS = "AS"
    AZ = "AZ"
    NM = "NM"
    NV = "NV"
    NY = "NY"
    OH = "OH"
    OK = "OK"
    OR = "OR"
    FM = "FM"
    GA = "GA"
    GU = "GU"
    HI = "HI"
    IA = "IA"
    ID = "ID"
    IL = "IL"
    IN = "IN"
    KS = "KS"
    KY = "KY"
    LA = "LA"
    MA = "MA"
    MD = "MD"
    ME = "ME"
    MH = "MH"
    MI = "MI"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MS = "MS"
    MT = "MT"
    NC = "NC"
    ND = "ND"
    NE = "NE"
    NH = "NH"
    NJ = "NJ"
    PA = "PA"
    PR = "PR"
    PW = "PW"
    RI = "RI"
    SC = "SC"
    SD = "SD"
    TN = "TN"
    TX = "TX"
    UT = "UT"
    VA = "VA"
    VI = "VI"
    VT = "VT"
    WA = "WA"
    WI = "WI"
    WV = "WV"
    WY = "WY"


############################################
# Definition of Classes
############################################

class ecvi_ResultValue:

    def __init__(self, resultFloat: str, resultInteger: str, resultString: str, resultName: str, ecvi_ResultValue: "ecvi_Test" = None):
        self.resultFloat = resultFloat
        self.resultInteger = resultInteger
        self.resultString = resultString
        self.resultName = resultName
        self.ecvi_ResultValue = ecvi_ResultValue
        
    @property
    def resultFloat(self) -> str:
        return self.__resultFloat

    @resultFloat.setter
    def resultFloat(self, resultFloat: str):
        self.__resultFloat = resultFloat

    @property
    def resultInteger(self) -> str:
        return self.__resultInteger

    @resultInteger.setter
    def resultInteger(self, resultInteger: str):
        self.__resultInteger = resultInteger

    @property
    def resultString(self) -> str:
        return self.__resultString

    @resultString.setter
    def resultString(self, resultString: str):
        self.__resultString = resultString

    @property
    def resultName(self) -> str:
        return self.__resultName

    @resultName.setter
    def resultName(self, resultName: str):
        self.__resultName = resultName

    @property
    def ecvi_ResultValue(self):
        return self.__ecvi_ResultValue

    @ecvi_ResultValue.setter
    def ecvi_ResultValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_ResultValue__ecvi_ResultValue", None)
        self.__ecvi_ResultValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Test56"):
                opp_val = getattr(old_value, "ecvi_Test56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Test56"):
                opp_val = getattr(value, "ecvi_Test56", None)
                if opp_val is None:
                    setattr(value, "ecvi_Test56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecvi_ProgramStatus:

    def __init__(self, name: str, value: str, valueOther: str, ecvi_ProgramStatus: "ecvi_Premises" = None):
        self.name = name
        self.value = value
        self.valueOther = valueOther
        self.ecvi_ProgramStatus = ecvi_ProgramStatus
        
    @property
    def valueOther(self) -> str:
        return self.__valueOther

    @valueOther.setter
    def valueOther(self, valueOther: str):
        self.__valueOther = valueOther

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecvi_ProgramStatus(self):
        return self.__ecvi_ProgramStatus

    @ecvi_ProgramStatus.setter
    def ecvi_ProgramStatus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_ProgramStatus__ecvi_ProgramStatus", None)
        self.__ecvi_ProgramStatus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Premises51"):
                opp_val = getattr(old_value, "ecvi_Premises51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Premises51"):
                opp_val = getattr(value, "ecvi_Premises51", None)
                if opp_val is None:
                    setattr(value, "ecvi_Premises51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecvi_PhoneNum:

    def __init__(self, comment: str, number: str, type: str, ecvi_PhoneNum: "ecvi_Person" = None):
        self.comment = comment
        self.number = number
        self.type = type
        self.ecvi_PhoneNum = ecvi_PhoneNum
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def ecvi_PhoneNum(self):
        return self.__ecvi_PhoneNum

    @ecvi_PhoneNum.setter
    def ecvi_PhoneNum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_PhoneNum__ecvi_PhoneNum", None)
        self.__ecvi_PhoneNum = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Person46"):
                opp_val = getattr(old_value, "ecvi_Person46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Person46"):
                opp_val = getattr(value, "ecvi_Person46", None)
                if opp_val is None:
                    setattr(value, "ecvi_Person46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecvi_GroupLot:

    def __init__(self, sex: str, age: str, breed: str, description: str, quantity: str, sexDetail: str, species: str, unit: str, ecvi_GroupLot: "ecvi_Ecvi" = None):
        self.sex = sex
        self.age = age
        self.breed = breed
        self.description = description
        self.quantity = quantity
        self.sexDetail = sexDetail
        self.species = species
        self.unit = unit
        self.ecvi_GroupLot = ecvi_GroupLot
        
    @property
    def quantity(self) -> str:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: str):
        self.__quantity = quantity

    @property
    def species(self) -> str:
        return self.__species

    @species.setter
    def species(self, species: str):
        self.__species = species

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age

    @property
    def sexDetail(self) -> str:
        return self.__sexDetail

    @sexDetail.setter
    def sexDetail(self, sexDetail: str):
        self.__sexDetail = sexDetail

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
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def ecvi_GroupLot(self):
        return self.__ecvi_GroupLot

    @ecvi_GroupLot.setter
    def ecvi_GroupLot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_GroupLot__ecvi_GroupLot", None)
        self.__ecvi_GroupLot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Ecvi39"):
                opp_val = getattr(old_value, "ecvi_Ecvi39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Ecvi39"):
                opp_val = getattr(value, "ecvi_Ecvi39", None)
                if opp_val is None:
                    setattr(value, "ecvi_Ecvi39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecvi_Veterinarian:

    def __init__(self, licenseIssueState: str, licenseNumber: str, nationalAccreditationNumber: str, ecvi_Veterinarian: "ecvi_Ecvi" = None, ecvi_Veterinarian61: "ecvi_Address" = None, ecvi_Veterinarian58: "ecvi_Person" = None):
        self.licenseIssueState = licenseIssueState
        self.licenseNumber = licenseNumber
        self.nationalAccreditationNumber = nationalAccreditationNumber
        self.ecvi_Veterinarian = ecvi_Veterinarian
        self.ecvi_Veterinarian61 = ecvi_Veterinarian61
        self.ecvi_Veterinarian58 = ecvi_Veterinarian58
        
    @property
    def licenseNumber(self) -> str:
        return self.__licenseNumber

    @licenseNumber.setter
    def licenseNumber(self, licenseNumber: str):
        self.__licenseNumber = licenseNumber

    @property
    def nationalAccreditationNumber(self) -> str:
        return self.__nationalAccreditationNumber

    @nationalAccreditationNumber.setter
    def nationalAccreditationNumber(self, nationalAccreditationNumber: str):
        self.__nationalAccreditationNumber = nationalAccreditationNumber

    @property
    def licenseIssueState(self) -> str:
        return self.__licenseIssueState

    @licenseIssueState.setter
    def licenseIssueState(self, licenseIssueState: str):
        self.__licenseIssueState = licenseIssueState

    @property
    def ecvi_Veterinarian58(self):
        return self.__ecvi_Veterinarian58

    @ecvi_Veterinarian58.setter
    def ecvi_Veterinarian58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Veterinarian__ecvi_Veterinarian58", None)
        self.__ecvi_Veterinarian58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Person59"):
                opp_val = getattr(old_value, "ecvi_Person59", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Person59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Person59"):
                opp_val = getattr(value, "ecvi_Person59", None)
                setattr(value, "ecvi_Person59", self)

    @property
    def ecvi_Veterinarian(self):
        return self.__ecvi_Veterinarian

    @ecvi_Veterinarian.setter
    def ecvi_Veterinarian(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Veterinarian__ecvi_Veterinarian", None)
        self.__ecvi_Veterinarian = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Ecvi18"):
                opp_val = getattr(old_value, "ecvi_Ecvi18", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Ecvi18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Ecvi18"):
                opp_val = getattr(value, "ecvi_Ecvi18", None)
                setattr(value, "ecvi_Ecvi18", self)

    @property
    def ecvi_Veterinarian61(self):
        return self.__ecvi_Veterinarian61

    @ecvi_Veterinarian61.setter
    def ecvi_Veterinarian61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Veterinarian__ecvi_Veterinarian61", None)
        self.__ecvi_Veterinarian61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Address62"):
                opp_val = getattr(old_value, "ecvi_Address62", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Address62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Address62"):
                opp_val = getattr(value, "ecvi_Address62", None)
                setattr(value, "ecvi_Address62", self)

class ecvi_Premises:

    def __init__(self, premId: str, premName: str, ecvi_Premises: "ecvi_Ecvi" = None, ecvi_Premises25: "ecvi_Ecvi" = None, ecvi_Premises53: set["ecvi_Person"] = None, ecvi_Premises48: "ecvi_Address" = None, ecvi_Premises51: set["ecvi_ProgramStatus"] = None):
        self.premId = premId
        self.premName = premName
        self.ecvi_Premises = ecvi_Premises
        self.ecvi_Premises25 = ecvi_Premises25
        self.ecvi_Premises53 = ecvi_Premises53 if ecvi_Premises53 is not None else set()
        self.ecvi_Premises48 = ecvi_Premises48
        self.ecvi_Premises51 = ecvi_Premises51 if ecvi_Premises51 is not None else set()
        
    @property
    def premName(self) -> str:
        return self.__premName

    @premName.setter
    def premName(self, premName: str):
        self.__premName = premName

    @property
    def premId(self) -> str:
        return self.__premId

    @premId.setter
    def premId(self, premId: str):
        self.__premId = premId

    @property
    def ecvi_Premises25(self):
        return self.__ecvi_Premises25

    @ecvi_Premises25.setter
    def ecvi_Premises25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Premises__ecvi_Premises25", None)
        self.__ecvi_Premises25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Ecvi24"):
                opp_val = getattr(old_value, "ecvi_Ecvi24", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Ecvi24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Ecvi24"):
                opp_val = getattr(value, "ecvi_Ecvi24", None)
                setattr(value, "ecvi_Ecvi24", self)

    @property
    def ecvi_Premises53(self):
        return self.__ecvi_Premises53

    @ecvi_Premises53.setter
    def ecvi_Premises53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Premises__ecvi_Premises53", None)
        self.__ecvi_Premises53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_Person54"):
                    opp_val = getattr(item, "ecvi_Person54", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_Person54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_Person54"):
                    opp_val = getattr(item, "ecvi_Person54", None)
                    
                    setattr(item, "ecvi_Person54", self)
                    

    @property
    def ecvi_Premises48(self):
        return self.__ecvi_Premises48

    @ecvi_Premises48.setter
    def ecvi_Premises48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Premises__ecvi_Premises48", None)
        self.__ecvi_Premises48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Address49"):
                opp_val = getattr(old_value, "ecvi_Address49", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Address49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Address49"):
                opp_val = getattr(value, "ecvi_Address49", None)
                setattr(value, "ecvi_Address49", self)

    @property
    def ecvi_Premises(self):
        return self.__ecvi_Premises

    @ecvi_Premises.setter
    def ecvi_Premises(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Premises__ecvi_Premises", None)
        self.__ecvi_Premises = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Ecvi22"):
                opp_val = getattr(old_value, "ecvi_Ecvi22", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Ecvi22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Ecvi22"):
                opp_val = getattr(value, "ecvi_Ecvi22", None)
                setattr(value, "ecvi_Ecvi22", self)

    @property
    def ecvi_Premises51(self):
        return self.__ecvi_Premises51

    @ecvi_Premises51.setter
    def ecvi_Premises51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Premises__ecvi_Premises51", None)
        self.__ecvi_Premises51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_ProgramStatus"):
                    opp_val = getattr(item, "ecvi_ProgramStatus", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_ProgramStatus", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_ProgramStatus"):
                    opp_val = getattr(item, "ecvi_ProgramStatus", None)
                    
                    setattr(item, "ecvi_ProgramStatus", self)
                    

class ecvi_MovementPurposes:

    def __init__(self, movementPurpose: str, ecvi_MovementPurposes: "ecvi_Ecvi" = None):
        self.movementPurpose = movementPurpose
        self.ecvi_MovementPurposes = ecvi_MovementPurposes
        
    @property
    def movementPurpose(self) -> str:
        return self.__movementPurpose

    @movementPurpose.setter
    def movementPurpose(self, movementPurpose: str):
        self.__movementPurpose = movementPurpose

    @property
    def ecvi_MovementPurposes(self):
        return self.__ecvi_MovementPurposes

    @ecvi_MovementPurposes.setter
    def ecvi_MovementPurposes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_MovementPurposes__ecvi_MovementPurposes", None)
        self.__ecvi_MovementPurposes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Ecvi20"):
                opp_val = getattr(old_value, "ecvi_Ecvi20", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Ecvi20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Ecvi20"):
                opp_val = getattr(value, "ecvi_Ecvi20", None)
                setattr(value, "ecvi_Ecvi20", self)

class ecvi_DocumentRoot:

    def __init__(self, mixed: str, ecvi_DocumentRoot: set["ecvi_EStringToStringMapEntry"] = None, ecvi_DocumentRoot13: set["ecvi_EStringToStringMapEntry"] = None, ecvi_DocumentRoot16: set["ecvi_Ecvi"] = None):
        self.mixed = mixed
        self.ecvi_DocumentRoot = ecvi_DocumentRoot if ecvi_DocumentRoot is not None else set()
        self.ecvi_DocumentRoot13 = ecvi_DocumentRoot13 if ecvi_DocumentRoot13 is not None else set()
        self.ecvi_DocumentRoot16 = ecvi_DocumentRoot16 if ecvi_DocumentRoot16 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def ecvi_DocumentRoot13(self):
        return self.__ecvi_DocumentRoot13

    @ecvi_DocumentRoot13.setter
    def ecvi_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_DocumentRoot__ecvi_DocumentRoot13", None)
        self.__ecvi_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_EStringToStringMapEntry14"):
                    opp_val = getattr(item, "ecvi_EStringToStringMapEntry14", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_EStringToStringMapEntry14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_EStringToStringMapEntry14"):
                    opp_val = getattr(item, "ecvi_EStringToStringMapEntry14", None)
                    
                    setattr(item, "ecvi_EStringToStringMapEntry14", self)
                    

    @property
    def ecvi_DocumentRoot(self):
        return self.__ecvi_DocumentRoot

    @ecvi_DocumentRoot.setter
    def ecvi_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_DocumentRoot__ecvi_DocumentRoot", None)
        self.__ecvi_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_EStringToStringMapEntry"):
                    opp_val = getattr(item, "ecvi_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_EStringToStringMapEntry"):
                    opp_val = getattr(item, "ecvi_EStringToStringMapEntry", None)
                    
                    setattr(item, "ecvi_EStringToStringMapEntry", self)
                    

    @property
    def ecvi_DocumentRoot16(self):
        return self.__ecvi_DocumentRoot16

    @ecvi_DocumentRoot16.setter
    def ecvi_DocumentRoot16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_DocumentRoot__ecvi_DocumentRoot16", None)
        self.__ecvi_DocumentRoot16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_Ecvi"):
                    opp_val = getattr(item, "ecvi_Ecvi", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_Ecvi", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_Ecvi"):
                    opp_val = getattr(item, "ecvi_Ecvi", None)
                    
                    setattr(item, "ecvi_Ecvi", self)
                    

class ecvi_Ecvi:

    def __init__(self, group: str, group1: str, cviNumber: str, entryPermitNumber: str, expirationDate: str, issueDate: str, shipmentDate: str, speciesCode: str, ecvi_Ecvi: "ecvi_DocumentRoot" = None, ecvi_Ecvi20: "ecvi_MovementPurposes" = None, ecvi_Ecvi22: "ecvi_Premises" = None, ecvi_Ecvi24: "ecvi_Premises" = None, ecvi_Ecvi18: "ecvi_Veterinarian" = None, ecvi_Ecvi33: "ecvi_Accessions" = None, ecvi_Ecvi36: set["ecvi_Animal"] = None, ecvi_Ecvi27: "ecvi_Contact" = None, ecvi_Ecvi30: "ecvi_Contact" = None, ecvi_Ecvi39: set["ecvi_GroupLot"] = None, ecvi_Ecvi41: set["ecvi_Attachement"] = None):
        self.group = group
        self.group1 = group1
        self.cviNumber = cviNumber
        self.entryPermitNumber = entryPermitNumber
        self.expirationDate = expirationDate
        self.issueDate = issueDate
        self.shipmentDate = shipmentDate
        self.speciesCode = speciesCode
        self.ecvi_Ecvi = ecvi_Ecvi
        self.ecvi_Ecvi20 = ecvi_Ecvi20
        self.ecvi_Ecvi22 = ecvi_Ecvi22
        self.ecvi_Ecvi24 = ecvi_Ecvi24
        self.ecvi_Ecvi18 = ecvi_Ecvi18
        self.ecvi_Ecvi33 = ecvi_Ecvi33
        self.ecvi_Ecvi36 = ecvi_Ecvi36 if ecvi_Ecvi36 is not None else set()
        self.ecvi_Ecvi27 = ecvi_Ecvi27
        self.ecvi_Ecvi30 = ecvi_Ecvi30
        self.ecvi_Ecvi39 = ecvi_Ecvi39 if ecvi_Ecvi39 is not None else set()
        self.ecvi_Ecvi41 = ecvi_Ecvi41 if ecvi_Ecvi41 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def group1(self) -> str:
        return self.__group1

    @group1.setter
    def group1(self, group1: str):
        self.__group1 = group1

    @property
    def shipmentDate(self) -> str:
        return self.__shipmentDate

    @shipmentDate.setter
    def shipmentDate(self, shipmentDate: str):
        self.__shipmentDate = shipmentDate

    @property
    def cviNumber(self) -> str:
        return self.__cviNumber

    @cviNumber.setter
    def cviNumber(self, cviNumber: str):
        self.__cviNumber = cviNumber

    @property
    def speciesCode(self) -> str:
        return self.__speciesCode

    @speciesCode.setter
    def speciesCode(self, speciesCode: str):
        self.__speciesCode = speciesCode

    @property
    def expirationDate(self) -> str:
        return self.__expirationDate

    @expirationDate.setter
    def expirationDate(self, expirationDate: str):
        self.__expirationDate = expirationDate

    @property
    def issueDate(self) -> str:
        return self.__issueDate

    @issueDate.setter
    def issueDate(self, issueDate: str):
        self.__issueDate = issueDate

    @property
    def entryPermitNumber(self) -> str:
        return self.__entryPermitNumber

    @entryPermitNumber.setter
    def entryPermitNumber(self, entryPermitNumber: str):
        self.__entryPermitNumber = entryPermitNumber

    @property
    def ecvi_Ecvi20(self):
        return self.__ecvi_Ecvi20

    @ecvi_Ecvi20.setter
    def ecvi_Ecvi20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Ecvi__ecvi_Ecvi20", None)
        self.__ecvi_Ecvi20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_MovementPurposes"):
                opp_val = getattr(old_value, "ecvi_MovementPurposes", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_MovementPurposes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_MovementPurposes"):
                opp_val = getattr(value, "ecvi_MovementPurposes", None)
                setattr(value, "ecvi_MovementPurposes", self)

    @property
    def ecvi_Ecvi24(self):
        return self.__ecvi_Ecvi24

    @ecvi_Ecvi24.setter
    def ecvi_Ecvi24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Ecvi__ecvi_Ecvi24", None)
        self.__ecvi_Ecvi24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Premises25"):
                opp_val = getattr(old_value, "ecvi_Premises25", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Premises25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Premises25"):
                opp_val = getattr(value, "ecvi_Premises25", None)
                setattr(value, "ecvi_Premises25", self)

    @property
    def ecvi_Ecvi27(self):
        return self.__ecvi_Ecvi27

    @ecvi_Ecvi27.setter
    def ecvi_Ecvi27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Ecvi__ecvi_Ecvi27", None)
        self.__ecvi_Ecvi27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Contact28"):
                opp_val = getattr(old_value, "ecvi_Contact28", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Contact28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Contact28"):
                opp_val = getattr(value, "ecvi_Contact28", None)
                setattr(value, "ecvi_Contact28", self)

    @property
    def ecvi_Ecvi41(self):
        return self.__ecvi_Ecvi41

    @ecvi_Ecvi41.setter
    def ecvi_Ecvi41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Ecvi__ecvi_Ecvi41", None)
        self.__ecvi_Ecvi41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_Attachement"):
                    opp_val = getattr(item, "ecvi_Attachement", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_Attachement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_Attachement"):
                    opp_val = getattr(item, "ecvi_Attachement", None)
                    
                    setattr(item, "ecvi_Attachement", self)
                    

    @property
    def ecvi_Ecvi36(self):
        return self.__ecvi_Ecvi36

    @ecvi_Ecvi36.setter
    def ecvi_Ecvi36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Ecvi__ecvi_Ecvi36", None)
        self.__ecvi_Ecvi36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_Animal37"):
                    opp_val = getattr(item, "ecvi_Animal37", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_Animal37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_Animal37"):
                    opp_val = getattr(item, "ecvi_Animal37", None)
                    
                    setattr(item, "ecvi_Animal37", self)
                    

    @property
    def ecvi_Ecvi(self):
        return self.__ecvi_Ecvi

    @ecvi_Ecvi.setter
    def ecvi_Ecvi(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Ecvi__ecvi_Ecvi", None)
        self.__ecvi_Ecvi = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_DocumentRoot16"):
                opp_val = getattr(old_value, "ecvi_DocumentRoot16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_DocumentRoot16"):
                opp_val = getattr(value, "ecvi_DocumentRoot16", None)
                if opp_val is None:
                    setattr(value, "ecvi_DocumentRoot16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecvi_Ecvi39(self):
        return self.__ecvi_Ecvi39

    @ecvi_Ecvi39.setter
    def ecvi_Ecvi39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Ecvi__ecvi_Ecvi39", None)
        self.__ecvi_Ecvi39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_GroupLot"):
                    opp_val = getattr(item, "ecvi_GroupLot", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_GroupLot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_GroupLot"):
                    opp_val = getattr(item, "ecvi_GroupLot", None)
                    
                    setattr(item, "ecvi_GroupLot", self)
                    

    @property
    def ecvi_Ecvi30(self):
        return self.__ecvi_Ecvi30

    @ecvi_Ecvi30.setter
    def ecvi_Ecvi30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Ecvi__ecvi_Ecvi30", None)
        self.__ecvi_Ecvi30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Contact31"):
                opp_val = getattr(old_value, "ecvi_Contact31", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Contact31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Contact31"):
                opp_val = getattr(value, "ecvi_Contact31", None)
                setattr(value, "ecvi_Contact31", self)

    @property
    def ecvi_Ecvi33(self):
        return self.__ecvi_Ecvi33

    @ecvi_Ecvi33.setter
    def ecvi_Ecvi33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Ecvi__ecvi_Ecvi33", None)
        self.__ecvi_Ecvi33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Accessions34"):
                opp_val = getattr(old_value, "ecvi_Accessions34", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Accessions34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Accessions34"):
                opp_val = getattr(value, "ecvi_Accessions34", None)
                setattr(value, "ecvi_Accessions34", self)

    @property
    def ecvi_Ecvi22(self):
        return self.__ecvi_Ecvi22

    @ecvi_Ecvi22.setter
    def ecvi_Ecvi22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Ecvi__ecvi_Ecvi22", None)
        self.__ecvi_Ecvi22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Premises"):
                opp_val = getattr(old_value, "ecvi_Premises", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Premises", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Premises"):
                opp_val = getattr(value, "ecvi_Premises", None)
                setattr(value, "ecvi_Premises", self)

    @property
    def ecvi_Ecvi18(self):
        return self.__ecvi_Ecvi18

    @ecvi_Ecvi18.setter
    def ecvi_Ecvi18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Ecvi__ecvi_Ecvi18", None)
        self.__ecvi_Ecvi18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Veterinarian"):
                opp_val = getattr(old_value, "ecvi_Veterinarian", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Veterinarian", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Veterinarian"):
                opp_val = getattr(value, "ecvi_Veterinarian", None)
                setattr(value, "ecvi_Veterinarian", self)

class ecvi_EStringToStringMapEntry:

    pass
class ecvi_Person:

    def __init__(self, name: str, ecvi_Person: "ecvi_Contact" = None, ecvi_Person46: set["ecvi_PhoneNum"] = None, ecvi_Person54: "ecvi_Premises" = None, ecvi_Person59: "ecvi_Veterinarian" = None):
        self.name = name
        self.ecvi_Person = ecvi_Person
        self.ecvi_Person46 = ecvi_Person46 if ecvi_Person46 is not None else set()
        self.ecvi_Person54 = ecvi_Person54
        self.ecvi_Person59 = ecvi_Person59
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecvi_Person46(self):
        return self.__ecvi_Person46

    @ecvi_Person46.setter
    def ecvi_Person46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Person__ecvi_Person46", None)
        self.__ecvi_Person46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_PhoneNum"):
                    opp_val = getattr(item, "ecvi_PhoneNum", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_PhoneNum", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_PhoneNum"):
                    opp_val = getattr(item, "ecvi_PhoneNum", None)
                    
                    setattr(item, "ecvi_PhoneNum", self)
                    

    @property
    def ecvi_Person(self):
        return self.__ecvi_Person

    @ecvi_Person.setter
    def ecvi_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Person__ecvi_Person", None)
        self.__ecvi_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Contact10"):
                opp_val = getattr(old_value, "ecvi_Contact10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Contact10"):
                opp_val = getattr(value, "ecvi_Contact10", None)
                if opp_val is None:
                    setattr(value, "ecvi_Contact10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecvi_Person54(self):
        return self.__ecvi_Person54

    @ecvi_Person54.setter
    def ecvi_Person54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Person__ecvi_Person54", None)
        self.__ecvi_Person54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Premises53"):
                opp_val = getattr(old_value, "ecvi_Premises53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Premises53"):
                opp_val = getattr(value, "ecvi_Premises53", None)
                if opp_val is None:
                    setattr(value, "ecvi_Premises53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecvi_Person59(self):
        return self.__ecvi_Person59

    @ecvi_Person59.setter
    def ecvi_Person59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Person__ecvi_Person59", None)
        self.__ecvi_Person59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Veterinarian58"):
                opp_val = getattr(old_value, "ecvi_Veterinarian58", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Veterinarian58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Veterinarian58"):
                opp_val = getattr(value, "ecvi_Veterinarian58", None)
                setattr(value, "ecvi_Veterinarian58", self)

class ecvi_Contact:

    def __init__(self, premId: str, premName: str, ecvi_Contact10: set["ecvi_Person"] = None, ecvi_Contact: "ecvi_Address" = None, ecvi_Contact28: "ecvi_Ecvi" = None, ecvi_Contact31: "ecvi_Ecvi" = None):
        self.premId = premId
        self.premName = premName
        self.ecvi_Contact10 = ecvi_Contact10 if ecvi_Contact10 is not None else set()
        self.ecvi_Contact = ecvi_Contact
        self.ecvi_Contact28 = ecvi_Contact28
        self.ecvi_Contact31 = ecvi_Contact31
        
    @property
    def premId(self) -> str:
        return self.__premId

    @premId.setter
    def premId(self, premId: str):
        self.__premId = premId

    @property
    def premName(self) -> str:
        return self.__premName

    @premName.setter
    def premName(self, premName: str):
        self.__premName = premName

    @property
    def ecvi_Contact(self):
        return self.__ecvi_Contact

    @ecvi_Contact.setter
    def ecvi_Contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Contact__ecvi_Contact", None)
        self.__ecvi_Contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Address8"):
                opp_val = getattr(old_value, "ecvi_Address8", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Address8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Address8"):
                opp_val = getattr(value, "ecvi_Address8", None)
                setattr(value, "ecvi_Address8", self)

    @property
    def ecvi_Contact10(self):
        return self.__ecvi_Contact10

    @ecvi_Contact10.setter
    def ecvi_Contact10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Contact__ecvi_Contact10", None)
        self.__ecvi_Contact10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_Person"):
                    opp_val = getattr(item, "ecvi_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_Person"):
                    opp_val = getattr(item, "ecvi_Person", None)
                    
                    setattr(item, "ecvi_Person", self)
                    

    @property
    def ecvi_Contact31(self):
        return self.__ecvi_Contact31

    @ecvi_Contact31.setter
    def ecvi_Contact31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Contact__ecvi_Contact31", None)
        self.__ecvi_Contact31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Ecvi30"):
                opp_val = getattr(old_value, "ecvi_Ecvi30", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Ecvi30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Ecvi30"):
                opp_val = getattr(value, "ecvi_Ecvi30", None)
                setattr(value, "ecvi_Ecvi30", self)

    @property
    def ecvi_Contact28(self):
        return self.__ecvi_Contact28

    @ecvi_Contact28.setter
    def ecvi_Contact28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Contact__ecvi_Contact28", None)
        self.__ecvi_Contact28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Ecvi27"):
                opp_val = getattr(old_value, "ecvi_Ecvi27", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Ecvi27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Ecvi27"):
                opp_val = getattr(value, "ecvi_Ecvi27", None)
                setattr(value, "ecvi_Ecvi27", self)

class ecvi_Attachement:

    def __init__(self, filename: str, mimeType: str, payload: str, comment: str, docType: str, ecvi_Attachement: "ecvi_Ecvi" = None):
        self.filename = filename
        self.mimeType = mimeType
        self.payload = payload
        self.comment = comment
        self.docType = docType
        self.ecvi_Attachement = ecvi_Attachement
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def mimeType(self) -> str:
        return self.__mimeType

    @mimeType.setter
    def mimeType(self, mimeType: str):
        self.__mimeType = mimeType

    @property
    def payload(self) -> str:
        return self.__payload

    @payload.setter
    def payload(self, payload: str):
        self.__payload = payload

    @property
    def docType(self) -> str:
        return self.__docType

    @docType.setter
    def docType(self, docType: str):
        self.__docType = docType

    @property
    def ecvi_Attachement(self):
        return self.__ecvi_Attachement

    @ecvi_Attachement.setter
    def ecvi_Attachement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Attachement__ecvi_Attachement", None)
        self.__ecvi_Attachement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Ecvi41"):
                opp_val = getattr(old_value, "ecvi_Ecvi41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Ecvi41"):
                opp_val = getattr(value, "ecvi_Ecvi41", None)
                if opp_val is None:
                    setattr(value, "ecvi_Ecvi41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecvi_AnimalTag:

    def __init__(self, brandImage: str, number: str, type: str, ecvi_AnimalTag: "ecvi_Animal" = None):
        self.brandImage = brandImage
        self.number = number
        self.type = type
        self.ecvi_AnimalTag = ecvi_AnimalTag
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def brandImage(self) -> str:
        return self.__brandImage

    @brandImage.setter
    def brandImage(self, brandImage: str):
        self.__brandImage = brandImage

    @property
    def ecvi_AnimalTag(self):
        return self.__ecvi_AnimalTag

    @ecvi_AnimalTag.setter
    def ecvi_AnimalTag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_AnimalTag__ecvi_AnimalTag", None)
        self.__ecvi_AnimalTag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Animal"):
                opp_val = getattr(old_value, "ecvi_Animal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Animal"):
                opp_val = getattr(value, "ecvi_Animal", None)
                if opp_val is None:
                    setattr(value, "ecvi_Animal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecvi_Animal:

    def __init__(self, age: str, breed: str, inspectionDate: str, sex: str, sexDetail: str, ecvi_Animal6: set["ecvi_Test"] = None, ecvi_Animal: set["ecvi_AnimalTag"] = None, ecvi_Animal37: "ecvi_Ecvi" = None):
        self.age = age
        self.breed = breed
        self.inspectionDate = inspectionDate
        self.sex = sex
        self.sexDetail = sexDetail
        self.ecvi_Animal6 = ecvi_Animal6 if ecvi_Animal6 is not None else set()
        self.ecvi_Animal = ecvi_Animal if ecvi_Animal is not None else set()
        self.ecvi_Animal37 = ecvi_Animal37
        
    @property
    def breed(self) -> str:
        return self.__breed

    @breed.setter
    def breed(self, breed: str):
        self.__breed = breed

    @property
    def sexDetail(self) -> str:
        return self.__sexDetail

    @sexDetail.setter
    def sexDetail(self, sexDetail: str):
        self.__sexDetail = sexDetail

    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age

    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

    @property
    def inspectionDate(self) -> str:
        return self.__inspectionDate

    @inspectionDate.setter
    def inspectionDate(self, inspectionDate: str):
        self.__inspectionDate = inspectionDate

    @property
    def ecvi_Animal(self):
        return self.__ecvi_Animal

    @ecvi_Animal.setter
    def ecvi_Animal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Animal__ecvi_Animal", None)
        self.__ecvi_Animal = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_AnimalTag"):
                    opp_val = getattr(item, "ecvi_AnimalTag", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_AnimalTag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_AnimalTag"):
                    opp_val = getattr(item, "ecvi_AnimalTag", None)
                    
                    setattr(item, "ecvi_AnimalTag", self)
                    

    @property
    def ecvi_Animal37(self):
        return self.__ecvi_Animal37

    @ecvi_Animal37.setter
    def ecvi_Animal37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Animal__ecvi_Animal37", None)
        self.__ecvi_Animal37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Ecvi36"):
                opp_val = getattr(old_value, "ecvi_Ecvi36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Ecvi36"):
                opp_val = getattr(value, "ecvi_Ecvi36", None)
                if opp_val is None:
                    setattr(value, "ecvi_Ecvi36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecvi_Animal6(self):
        return self.__ecvi_Animal6

    @ecvi_Animal6.setter
    def ecvi_Animal6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Animal__ecvi_Animal6", None)
        self.__ecvi_Animal6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_Test"):
                    opp_val = getattr(item, "ecvi_Test", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_Test", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_Test"):
                    opp_val = getattr(item, "ecvi_Test", None)
                    
                    setattr(item, "ecvi_Test", self)
                    

class ecvi_Test:

    def __init__(self, idref: str, testCode: str, ecvi_Test: "ecvi_Animal" = None, ecvi_Test56: set["ecvi_ResultValue"] = None):
        self.idref = idref
        self.testCode = testCode
        self.ecvi_Test = ecvi_Test
        self.ecvi_Test56 = ecvi_Test56 if ecvi_Test56 is not None else set()
        
    @property
    def idref(self) -> str:
        return self.__idref

    @idref.setter
    def idref(self, idref: str):
        self.__idref = idref

    @property
    def testCode(self) -> str:
        return self.__testCode

    @testCode.setter
    def testCode(self, testCode: str):
        self.__testCode = testCode

    @property
    def ecvi_Test56(self):
        return self.__ecvi_Test56

    @ecvi_Test56.setter
    def ecvi_Test56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Test__ecvi_Test56", None)
        self.__ecvi_Test56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecvi_ResultValue"):
                    opp_val = getattr(item, "ecvi_ResultValue", None)
                    
                    if opp_val == self:
                        setattr(item, "ecvi_ResultValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecvi_ResultValue"):
                    opp_val = getattr(item, "ecvi_ResultValue", None)
                    
                    setattr(item, "ecvi_ResultValue", self)
                    

    @property
    def ecvi_Test(self):
        return self.__ecvi_Test

    @ecvi_Test.setter
    def ecvi_Test(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Test__ecvi_Test", None)
        self.__ecvi_Test = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Animal6"):
                opp_val = getattr(old_value, "ecvi_Animal6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Animal6"):
                opp_val = getattr(value, "ecvi_Animal6", None)
                if opp_val is None:
                    setattr(value, "ecvi_Animal6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecvi_GeoPoint:

    def __init__(self, lat: str, lng: str, ecvi_GeoPoint: "ecvi_Address" = None):
        self.lat = lat
        self.lng = lng
        self.ecvi_GeoPoint = ecvi_GeoPoint
        
    @property
    def lng(self) -> str:
        return self.__lng

    @lng.setter
    def lng(self, lng: str):
        self.__lng = lng

    @property
    def lat(self) -> str:
        return self.__lat

    @lat.setter
    def lat(self, lat: str):
        self.__lat = lat

    @property
    def ecvi_GeoPoint(self):
        return self.__ecvi_GeoPoint

    @ecvi_GeoPoint.setter
    def ecvi_GeoPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_GeoPoint__ecvi_GeoPoint", None)
        self.__ecvi_GeoPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Address"):
                opp_val = getattr(old_value, "ecvi_Address", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Address"):
                opp_val = getattr(value, "ecvi_Address", None)
                setattr(value, "ecvi_Address", self)

class ecvi_Address:

    def __init__(self, line2: str, town: str, county: str, line1: str, state: str, zIP: str, country: str, ecvi_Address: "ecvi_GeoPoint" = None, ecvi_Address8: "ecvi_Contact" = None, ecvi_Address44: "ecvi_Laboratory" = None, ecvi_Address49: "ecvi_Premises" = None, ecvi_Address62: "ecvi_Veterinarian" = None):
        self.line2 = line2
        self.town = town
        self.county = county
        self.line1 = line1
        self.state = state
        self.zIP = zIP
        self.country = country
        self.ecvi_Address = ecvi_Address
        self.ecvi_Address8 = ecvi_Address8
        self.ecvi_Address44 = ecvi_Address44
        self.ecvi_Address49 = ecvi_Address49
        self.ecvi_Address62 = ecvi_Address62
        
    @property
    def line1(self) -> str:
        return self.__line1

    @line1.setter
    def line1(self, line1: str):
        self.__line1 = line1

    @property
    def line2(self) -> str:
        return self.__line2

    @line2.setter
    def line2(self, line2: str):
        self.__line2 = line2

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def zIP(self) -> str:
        return self.__zIP

    @zIP.setter
    def zIP(self, zIP: str):
        self.__zIP = zIP

    @property
    def county(self) -> str:
        return self.__county

    @county.setter
    def county(self, county: str):
        self.__county = county

    @property
    def town(self) -> str:
        return self.__town

    @town.setter
    def town(self, town: str):
        self.__town = town

    @property
    def ecvi_Address8(self):
        return self.__ecvi_Address8

    @ecvi_Address8.setter
    def ecvi_Address8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Address__ecvi_Address8", None)
        self.__ecvi_Address8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Contact"):
                opp_val = getattr(old_value, "ecvi_Contact", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Contact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Contact"):
                opp_val = getattr(value, "ecvi_Contact", None)
                setattr(value, "ecvi_Contact", self)

    @property
    def ecvi_Address44(self):
        return self.__ecvi_Address44

    @ecvi_Address44.setter
    def ecvi_Address44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Address__ecvi_Address44", None)
        self.__ecvi_Address44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Laboratory43"):
                opp_val = getattr(old_value, "ecvi_Laboratory43", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Laboratory43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Laboratory43"):
                opp_val = getattr(value, "ecvi_Laboratory43", None)
                setattr(value, "ecvi_Laboratory43", self)

    @property
    def ecvi_Address49(self):
        return self.__ecvi_Address49

    @ecvi_Address49.setter
    def ecvi_Address49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Address__ecvi_Address49", None)
        self.__ecvi_Address49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Premises48"):
                opp_val = getattr(old_value, "ecvi_Premises48", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Premises48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Premises48"):
                opp_val = getattr(value, "ecvi_Premises48", None)
                setattr(value, "ecvi_Premises48", self)

    @property
    def ecvi_Address(self):
        return self.__ecvi_Address

    @ecvi_Address.setter
    def ecvi_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Address__ecvi_Address", None)
        self.__ecvi_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_GeoPoint"):
                opp_val = getattr(old_value, "ecvi_GeoPoint", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_GeoPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_GeoPoint"):
                opp_val = getattr(value, "ecvi_GeoPoint", None)
                setattr(value, "ecvi_GeoPoint", self)

    @property
    def ecvi_Address62(self):
        return self.__ecvi_Address62

    @ecvi_Address62.setter
    def ecvi_Address62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Address__ecvi_Address62", None)
        self.__ecvi_Address62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Veterinarian61"):
                opp_val = getattr(old_value, "ecvi_Veterinarian61", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Veterinarian61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Veterinarian61"):
                opp_val = getattr(value, "ecvi_Veterinarian61", None)
                setattr(value, "ecvi_Veterinarian61", self)

class ecvi_Laboratory:

    def __init__(self, labName: str, premId: str, accessionDate: str, accessionNumber: str, ecvi_Laboratory: "ecvi_Accession" = None, ecvi_Laboratory43: "ecvi_Address" = None):
        self.labName = labName
        self.premId = premId
        self.accessionDate = accessionDate
        self.accessionNumber = accessionNumber
        self.ecvi_Laboratory = ecvi_Laboratory
        self.ecvi_Laboratory43 = ecvi_Laboratory43
        
    @property
    def labName(self) -> str:
        return self.__labName

    @labName.setter
    def labName(self, labName: str):
        self.__labName = labName

    @property
    def premId(self) -> str:
        return self.__premId

    @premId.setter
    def premId(self, premId: str):
        self.__premId = premId

    @property
    def accessionNumber(self) -> str:
        return self.__accessionNumber

    @accessionNumber.setter
    def accessionNumber(self, accessionNumber: str):
        self.__accessionNumber = accessionNumber

    @property
    def accessionDate(self) -> str:
        return self.__accessionDate

    @accessionDate.setter
    def accessionDate(self, accessionDate: str):
        self.__accessionDate = accessionDate

    @property
    def ecvi_Laboratory(self):
        return self.__ecvi_Laboratory

    @ecvi_Laboratory.setter
    def ecvi_Laboratory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Laboratory__ecvi_Laboratory", None)
        self.__ecvi_Laboratory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Accession"):
                opp_val = getattr(old_value, "ecvi_Accession", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Accession", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Accession"):
                opp_val = getattr(value, "ecvi_Accession", None)
                setattr(value, "ecvi_Accession", self)

    @property
    def ecvi_Laboratory43(self):
        return self.__ecvi_Laboratory43

    @ecvi_Laboratory43.setter
    def ecvi_Laboratory43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Laboratory__ecvi_Laboratory43", None)
        self.__ecvi_Laboratory43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Address44"):
                opp_val = getattr(old_value, "ecvi_Address44", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Address44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Address44"):
                opp_val = getattr(value, "ecvi_Address44", None)
                setattr(value, "ecvi_Address44", self)

class ecvi_Accession:

    def __init__(self, id: str, infieldTest: str, ecvi_Accession: "ecvi_Laboratory" = None, ecvi_Accession2: "ecvi_Accessions" = None):
        self.id = id
        self.infieldTest = infieldTest
        self.ecvi_Accession = ecvi_Accession
        self.ecvi_Accession2 = ecvi_Accession2
        
    @property
    def infieldTest(self) -> str:
        return self.__infieldTest

    @infieldTest.setter
    def infieldTest(self, infieldTest: str):
        self.__infieldTest = infieldTest

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ecvi_Accession(self):
        return self.__ecvi_Accession

    @ecvi_Accession.setter
    def ecvi_Accession(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Accession__ecvi_Accession", None)
        self.__ecvi_Accession = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Laboratory"):
                opp_val = getattr(old_value, "ecvi_Laboratory", None)
                if opp_val == self:
                    setattr(old_value, "ecvi_Laboratory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Laboratory"):
                opp_val = getattr(value, "ecvi_Laboratory", None)
                setattr(value, "ecvi_Laboratory", self)

    @property
    def ecvi_Accession2(self):
        return self.__ecvi_Accession2

    @ecvi_Accession2.setter
    def ecvi_Accession2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecvi_Accession__ecvi_Accession2", None)
        self.__ecvi_Accession2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecvi_Accessions"):
                opp_val = getattr(old_value, "ecvi_Accessions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecvi_Accessions"):
                opp_val = getattr(value, "ecvi_Accessions", None)
                if opp_val is None:
                    setattr(value, "ecvi_Accessions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecvi_Accessions:

    pass