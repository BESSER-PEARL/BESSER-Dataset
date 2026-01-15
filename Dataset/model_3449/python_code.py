from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class StudyDeptExamLevel(Enum):
    ENTRANCE = "ENTRANCE"
    ELEMENTARY = "ELEMENTARY"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"
    GRADUATE = "GRADUATE"
    POSTGRADUATE = "POSTGRADUATE"
    OTHER = "OTHER"
class SchoolType(Enum):
    OTHER = "OTHER"
    ELEMENTARY = "ELEMENTARY"
    GRAMMER = "GRAMMER"
    JRHIGHSCHOOL = "JRHIGHSCHOOL"
    HIGHSCHOOL = "HIGHSCHOOL"
    COLLEGE = "COLLEGE"
    GRADUATE = "GRADUATE"
class SubDivision(Enum):
    STUDENT = "STUDENT"
    HIGHSCHOOL = "HIGHSCHOOL"
    JRHIGHSCHOOL = "JRHIGHSCHOOL"
    ELEMENTARYSCHOOL = "ELEMENTARYSCHOOL"
    CHILDREN = "CHILDREN"
    ALL = "ALL"
class ActivityGroup(Enum):
    NONE = "NONE"
    YOUTHMUSICCORP = "YOUTHMUSICCORP"
    FIFEANDDRUMCORP = "FIFEANDDRUMCORP"
    BYAKUREN = "BYAKUREN"
    SOKAGROUP = "SOKAGROUP"
    GAJOKAI = "GAJOKAI"
    CHORUSGROUP = "CHORUSGROUP"
    STUDYGROUP = "STUDYGROUP"
    PHONETOBAN = "PHONETOBAN"
    BOOKSTORETOBAN = "BOOKSTORETOBAN"
    CLEANUPCOMMITTEE = "CLEANUPCOMMITTEE"
    BUILDINGCOMMITTEE = "BUILDINGCOMMITTEE"
    WELCOMINGCOMMITTEE = "WELCOMINGCOMMITTEE"
    GOLDENSTAGECREW = "GOLDENSTAGECREW"
    YOUTHPEACEGROUP = "YOUTHPEACEGROUP"
    YOUTHSUPPORTGROUP = "YOUTHSUPPORTGROUP"
    SOKASPIRITGROUP = "SOKASPIRITGROUP"
    CULTUREDEPT = "CULTUREDEPT"
    SECRETARIET = "SECRETARIET"
    CENTRALEXECUTIVECOMMITTEE = "CENTRALEXECUTIVECOMMITTEE"
class RoleType(Enum):
    MANAGER = "MANAGER"
    USER = "USER"
    HOST = "HOST"
class Capability(Enum):
    ALL = "ALL"
    NONE = "NONE"
    READ = "READ"
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    EXPORT = "EXPORT"
    EMAIL = "EMAIL"
    PRINT = "PRINT"
class ActivityGroupName(Enum):
    ChorusGroup = "ChorusGroup"
    StudyGroup = "StudyGroup"
    PhoneToban = "PhoneToban"
    BookstoreToban = "BookstoreToban"
    CleanupCommittee = "CleanupCommittee"
    BuildingCommittee = "BuildingCommittee"
    WelcomingCommittee = "WelcomingCommittee"
    GoldenStageCrew = "GoldenStageCrew"
    YouthPeaceGroup = "YouthPeaceGroup"
    YouthSupportGroup = "YouthSupportGroup"
    none = "none"
    YouthMusicCorp = "YouthMusicCorp"
    FifeAndDrumCorp = "FifeAndDrumCorp"
    Byakuren = "Byakuren"
    SokaGroup = "SokaGroup"
    Gajokai = "Gajokai"
    SokaSpiritGroup = "SokaSpiritGroup"
    CultureDept = "CultureDept"
    Secretariet = "Secretariet"
    CentralExecutiveCommittee = "CentralExecutiveCommittee"
class PositionName(Enum):
    Leader = "Leader"
    ViceLeader = "ViceLeader"
    Guidance = "Guidance"
    Advisor = "Advisor"
    SeniorViceLeader = "SeniorViceLeader"
    GeneralDirector = "GeneralDirector"
    ViceGeneralDirector = "ViceGeneralDirector"
    SeniorViceGeneralDirector = "SeniorViceGeneralDirector"
    SokaSpiritCoordinator = "SokaSpiritCoordinator"
    CultureDeptCoordinator = "CultureDeptCoordinator"
    MemberCareAdvisor = "MemberCareAdvisor"
    MembershipStatisticsAdministrator = "MembershipStatisticsAdministrator"
    MembershipDatabaseAdministrator = "MembershipDatabaseAdministrator"
    PublicationsRepresentative = "PublicationsRepresentative"
class GohonzonType(Enum):
    REGULAR = "REGULAR"
    SMALL = "SMALL"
    LARGE = "LARGE"
    FAMILY = "FAMILY"
    OMOMORI = "OMOMORI"
    OKATAGI = "OKATAGI"
class ViewType(Enum):
    USERLIST = "USERLIST"
    MEMBERLIST = "MEMBERLIST"
    ORGANIZATIONNODE = "ORGANIZATIONNODE"
class FamilyRelation(Enum):
    MOTHER = "MOTHER"
    FATHER = "FATHER"
    SISTER = "SISTER"
    BROTHER = "BROTHER"
    STEPSISTER = "STEPSISTER"
    STEPBROTHER = "STEPBROTHER"
    HUSBAND = "HUSBAND"
    WIFE = "WIFE"
    SON = "SON"
    DAUGHTER = "DAUGHTER"
    GRANDMOTHER = "GRANDMOTHER"
    GRANDFATHER = "GRANDFATHER"
    GRANDSON = "GRANDSON"
    GRANDDAUGHTER = "GRANDDAUGHTER"
    MOTHERINLAW = "MOTHERINLAW"
    FATHERINLAW = "FATHERINLAW"
    SONINLAW = "SONINLAW"
    DAUGHTERINLAW = "DAUGHTERINLAW"
    AUNT = "AUNT"
    UNCLE = "UNCLE"
    COUSIN = "COUSIN"
    NIECE = "NIECE"
    NEPHEW = "NEPHEW"
    EXHUSBAND = "EXHUSBAND"
    EXWIFE = "EXWIFE"
    OTHER = "OTHER"
class Country(Enum):
    USA = "USA"
    CAN = "CAN"
    MEX = "MEX"
    PR = "PR"
class State(Enum):
    AL = "AL"
    AK = "AK"
    AZ = "AZ"
    AR = "AR"
    CA = "CA"
    CO = "CO"
    CT = "CT"
    DE = "DE"
    FL = "FL"
    GA = "GA"
    HI = "HI"
    ID = "ID"
    IL = "IL"
    ND = "ND"
    OH = "OH"
    OK = "OK"
    OR = "OR"
    PA = "PA"
    RI = "RI"
    SC = "SC"
    SD = "SD"
    TN = "TN"
    TX = "TX"
    UT = "UT"
    VT = "VT"
    IN = "IN"
    IA = "IA"
    KS = "KS"
    KY = "KY"
    LA = "LA"
    ME = "ME"
    MD = "MD"
    MA = "MA"
    MI = "MI"
    MN = "MN"
    MS = "MS"
    MO = "MO"
    MT = "MT"
    NE = "NE"
    NV = "NV"
    NH = "NH"
    NJ = "NJ"
    NM = "NM"
    NY = "NY"
    NC = "NC"
    VA = "VA"
    WA = "WA"
    WV = "WV"
    WI = "WI"
    WY = "WY"
class StudyDeptLanguage(Enum):
    ENGLISH = "ENGLISH"
    SPANISH = "SPANISH"
    FRENCH = "FRENCH"
    ITALIAN = "ITALIAN"
    GERMAN = "GERMAN"
    PORTUGUESE = "PORTUGUESE"
    JAPANESE = "JAPANESE"
    CHINESE = "CHINESE"
    KOREAN = "KOREAN"
    VIETNAMESE = "VIETNAMESE"
    THAI = "THAI"
    OTHER = "OTHER"
class PhoneNumberType(Enum):
    HOME = "HOME"
    WORK = "WORK"
    CELL = "CELL"
    FAX = "FAX"
    OTHER = "OTHER"
class Role(Enum):
    MANAGER = "MANAGER"
    USER = "USER"
    HOST = "HOST"
class OrganizationLevel(Enum):
    SGIUSA = "SGIUSA"
    TEAM = "TEAM"
    ZONE = "ZONE"
    REGION = "REGION"
    AREA = "AREA"
    CHAPTER = "CHAPTER"
    DISTRICT = "DISTRICT"
    GROUP = "GROUP"
    UNIT = "UNIT"
class Language(Enum):
    CHINESE = "CHINESE"
    KOREAN = "KOREAN"
    VIETNAMESE = "VIETNAMESE"
    THAI = "THAI"
    OTHER = "OTHER"
    ENGLISH = "ENGLISH"
    SPANISH = "SPANISH"
    FRENCH = "FRENCH"
    ITALIAN = "ITALIAN"
    GERMAN = "GERMAN"
    PORTUGUESE = "PORTUGUESE"
    JAPANESE = "JAPANESE"
class Division(Enum):
    NONE = "NONE"
    YWD = "YWD"
    YMD = "YMD"
    YD = "YD"
    WD = "WD"
    MD = "MD"
    ALL = "ALL"
class Status(Enum):
    INFO = "INFO"
    PROMPT = "PROMPT"
    WARNING = "WARNING"
    ERROR = "ERROR"
class EventStatus(Enum):
    MANAGER = "MANAGER"
    USER = "USER"
    HOST = "HOST"
class Position(Enum):
    LEADER = "LEADER"
    VICELEADER = "VICELEADER"
    GUIDANCE = "GUIDANCE"
    ADVISOR = "ADVISOR"
    SENIORVICELEADER = "SENIORVICELEADER"
    GENERALDIRECTOR = "GENERALDIRECTOR"
    VICEGENERALDIRECTOR = "VICEGENERALDIRECTOR"
    SENIORVICEGENERALDIRECTOR = "SENIORVICEGENERALDIRECTOR"
    SOKASPIRITCOORDINATOR = "SOKASPIRITCOORDINATOR"
    CULTUREDEPTCOORDINATOR = "CULTUREDEPTCOORDINATOR"
    MEMBERCAREADVISOR = "MEMBERCAREADVISOR"
    MEMBERSHIPSTATISTICSADMINISTRATOR = "MEMBERSHIPSTATISTICSADMINISTRATOR"
    MEMBERSHIPDATABASEADMINISTRATOR = "MEMBERSHIPDATABASEADMINISTRATOR"
    PUBLICATIONSREPRESENTATIVE = "PUBLICATIONSREPRESENTATIVE"
class SubDivisionName(Enum):
    StudentDivision = "StudentDivision"
    HighSchoolDivision = "HighSchoolDivision"
    JrHighSchoolDivision = "JrHighSchoolDivision"
    ElementarySchoolDivision = "ElementarySchoolDivision"
    ChildrenSDivision = "ChildrenSDivision"
    ALLSubDivisions = "ALLSubDivisions"
class DivisionName(Enum):
    none = "none"
    YoungWomenSDivision = "YoungWomenSDivision"
    YoungMenSDivision = "YoungMenSDivision"
    YouthDivision = "YouthDivision"
    WomanSDivision = "WomanSDivision"
    MenSDivision = "MenSDivision"
    AllDivisions = "AllDivisions"


############################################
# Definition of Classes
############################################

class org_sgiusa_model_View:

    def __init__(self, id: str, userId: str, viewType: str, org_sgiusa_model_View: "Organization" = None):
        self.id = id
        self.userId = userId
        self.viewType = viewType
        self.org_sgiusa_model_View = org_sgiusa_model_View
        
    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def viewType(self) -> str:
        return self.__viewType

    @viewType.setter
    def viewType(self, viewType: str):
        self.__viewType = viewType

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def org_sgiusa_model_View(self):
        return self.__org_sgiusa_model_View

    @org_sgiusa_model_View.setter
    def org_sgiusa_model_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_View__org_sgiusa_model_View", None)
        self.__org_sgiusa_model_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization243"):
                opp_val = getattr(old_value, "Organization243", None)
                if opp_val == self:
                    setattr(old_value, "Organization243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization243"):
                opp_val = getattr(value, "Organization243", None)
                setattr(value, "Organization243", self)

class org_sgiusa_model_Users:

    pass
class org_sgiusa_model_User:

    def __init__(self, password: str, enabled: str, firstName: str, id: str, userId: str, lastName: str, role: str, org_sgiusa_model_User226: "StreetAddress" = None, org_sgiusa_model_User229: "PhoneNumber" = None, org_sgiusa_model_User232: "PhoneNumber" = None, org_sgiusa_model_User: "EmailAccount" = None, org_sgiusa_model_User223: "EmailAddress" = None, org_sgiusa_model_User235: set["Permission"] = None, org_sgiusa_model_User238: "Preferences" = None):
        self.password = password
        self.enabled = enabled
        self.firstName = firstName
        self.id = id
        self.userId = userId
        self.lastName = lastName
        self.role = role
        self.org_sgiusa_model_User226 = org_sgiusa_model_User226
        self.org_sgiusa_model_User229 = org_sgiusa_model_User229
        self.org_sgiusa_model_User232 = org_sgiusa_model_User232
        self.org_sgiusa_model_User = org_sgiusa_model_User
        self.org_sgiusa_model_User223 = org_sgiusa_model_User223
        self.org_sgiusa_model_User235 = org_sgiusa_model_User235 if org_sgiusa_model_User235 is not None else set()
        self.org_sgiusa_model_User238 = org_sgiusa_model_User238
        
    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def enabled(self) -> str:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: str):
        self.__enabled = enabled

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def org_sgiusa_model_User226(self):
        return self.__org_sgiusa_model_User226

    @org_sgiusa_model_User226.setter
    def org_sgiusa_model_User226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_User__org_sgiusa_model_User226", None)
        self.__org_sgiusa_model_User226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StreetAddress227"):
                opp_val = getattr(old_value, "StreetAddress227", None)
                if opp_val == self:
                    setattr(old_value, "StreetAddress227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StreetAddress227"):
                opp_val = getattr(value, "StreetAddress227", None)
                setattr(value, "StreetAddress227", self)

    @property
    def org_sgiusa_model_User238(self):
        return self.__org_sgiusa_model_User238

    @org_sgiusa_model_User238.setter
    def org_sgiusa_model_User238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_User__org_sgiusa_model_User238", None)
        self.__org_sgiusa_model_User238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Preferences239"):
                opp_val = getattr(old_value, "Preferences239", None)
                if opp_val == self:
                    setattr(old_value, "Preferences239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Preferences239"):
                opp_val = getattr(value, "Preferences239", None)
                setattr(value, "Preferences239", self)

    @property
    def org_sgiusa_model_User223(self):
        return self.__org_sgiusa_model_User223

    @org_sgiusa_model_User223.setter
    def org_sgiusa_model_User223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_User__org_sgiusa_model_User223", None)
        self.__org_sgiusa_model_User223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmailAddress224"):
                opp_val = getattr(old_value, "EmailAddress224", None)
                if opp_val == self:
                    setattr(old_value, "EmailAddress224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmailAddress224"):
                opp_val = getattr(value, "EmailAddress224", None)
                setattr(value, "EmailAddress224", self)

    @property
    def org_sgiusa_model_User(self):
        return self.__org_sgiusa_model_User

    @org_sgiusa_model_User.setter
    def org_sgiusa_model_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_User__org_sgiusa_model_User", None)
        self.__org_sgiusa_model_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmailAccount221"):
                opp_val = getattr(old_value, "EmailAccount221", None)
                if opp_val == self:
                    setattr(old_value, "EmailAccount221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmailAccount221"):
                opp_val = getattr(value, "EmailAccount221", None)
                setattr(value, "EmailAccount221", self)

    @property
    def org_sgiusa_model_User235(self):
        return self.__org_sgiusa_model_User235

    @org_sgiusa_model_User235.setter
    def org_sgiusa_model_User235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_User__org_sgiusa_model_User235", None)
        self.__org_sgiusa_model_User235 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Permission236"):
                    opp_val = getattr(item, "Permission236", None)
                    
                    if opp_val == self:
                        setattr(item, "Permission236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Permission236"):
                    opp_val = getattr(item, "Permission236", None)
                    
                    setattr(item, "Permission236", self)
                    

    @property
    def org_sgiusa_model_User229(self):
        return self.__org_sgiusa_model_User229

    @org_sgiusa_model_User229.setter
    def org_sgiusa_model_User229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_User__org_sgiusa_model_User229", None)
        self.__org_sgiusa_model_User229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhoneNumber230"):
                opp_val = getattr(old_value, "PhoneNumber230", None)
                if opp_val == self:
                    setattr(old_value, "PhoneNumber230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhoneNumber230"):
                opp_val = getattr(value, "PhoneNumber230", None)
                setattr(value, "PhoneNumber230", self)

    @property
    def org_sgiusa_model_User232(self):
        return self.__org_sgiusa_model_User232

    @org_sgiusa_model_User232.setter
    def org_sgiusa_model_User232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_User__org_sgiusa_model_User232", None)
        self.__org_sgiusa_model_User232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhoneNumber233"):
                opp_val = getattr(old_value, "PhoneNumber233", None)
                if opp_val == self:
                    setattr(old_value, "PhoneNumber233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhoneNumber233"):
                opp_val = getattr(value, "PhoneNumber233", None)
                setattr(value, "PhoneNumber233", self)

class org_sgiusa_model_StudyDeptInfo:

    def __init__(self, id: str, lastUpdate: str, org_sgiusa_model_StudyDeptInfo: set["StudyDeptExam"] = None):
        self.id = id
        self.lastUpdate = lastUpdate
        self.org_sgiusa_model_StudyDeptInfo = org_sgiusa_model_StudyDeptInfo if org_sgiusa_model_StudyDeptInfo is not None else set()
        
    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def org_sgiusa_model_StudyDeptInfo(self):
        return self.__org_sgiusa_model_StudyDeptInfo

    @org_sgiusa_model_StudyDeptInfo.setter
    def org_sgiusa_model_StudyDeptInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_StudyDeptInfo__org_sgiusa_model_StudyDeptInfo", None)
        self.__org_sgiusa_model_StudyDeptInfo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyDeptExam219"):
                    opp_val = getattr(item, "StudyDeptExam219", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyDeptExam219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyDeptExam219"):
                    opp_val = getattr(item, "StudyDeptExam219", None)
                    
                    setattr(item, "StudyDeptExam219", self)
                    

class org_sgiusa_model_StudyDeptExam:

    def __init__(self, id: str, current: str, examDate: str, lastUpdate: str, examLevel: str, examLanguage: str, examLocation: str):
        self.id = id
        self.current = current
        self.examDate = examDate
        self.lastUpdate = lastUpdate
        self.examLevel = examLevel
        self.examLanguage = examLanguage
        self.examLocation = examLocation
        
    @property
    def current(self) -> str:
        return self.__current

    @current.setter
    def current(self, current: str):
        self.__current = current

    @property
    def examLocation(self) -> str:
        return self.__examLocation

    @examLocation.setter
    def examLocation(self, examLocation: str):
        self.__examLocation = examLocation

    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def examDate(self) -> str:
        return self.__examDate

    @examDate.setter
    def examDate(self, examDate: str):
        self.__examDate = examDate

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def examLanguage(self) -> str:
        return self.__examLanguage

    @examLanguage.setter
    def examLanguage(self, examLanguage: str):
        self.__examLanguage = examLanguage

    @property
    def examLevel(self) -> str:
        return self.__examLevel

    @examLevel.setter
    def examLevel(self, examLevel: str):
        self.__examLevel = examLevel

class org_sgiusa_model_SchoolInfo:

    def __init__(self, schoolName: str, schoolType: str, fieldOfStudy: str, startDate: str, id: str, endDate: str, lastUpdate: str):
        self.schoolName = schoolName
        self.schoolType = schoolType
        self.fieldOfStudy = fieldOfStudy
        self.startDate = startDate
        self.id = id
        self.endDate = endDate
        self.lastUpdate = lastUpdate
        
    @property
    def endDate(self) -> str:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate

    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def schoolName(self) -> str:
        return self.__schoolName

    @schoolName.setter
    def schoolName(self, schoolName: str):
        self.__schoolName = schoolName

    @property
    def startDate(self) -> str:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate

    @property
    def fieldOfStudy(self) -> str:
        return self.__fieldOfStudy

    @fieldOfStudy.setter
    def fieldOfStudy(self, fieldOfStudy: str):
        self.__fieldOfStudy = fieldOfStudy

    @property
    def schoolType(self) -> str:
        return self.__schoolType

    @schoolType.setter
    def schoolType(self, schoolType: str):
        self.__schoolType = schoolType

class org_sgiusa_model_Registration:

    def __init__(self, date: str, cancelled: str, id: str, aborted: str, org_sgiusa_model_Registration: "User" = None):
        self.date = date
        self.cancelled = cancelled
        self.id = id
        self.aborted = aborted
        self.org_sgiusa_model_Registration = org_sgiusa_model_Registration
        
    @property
    def cancelled(self) -> str:
        return self.__cancelled

    @cancelled.setter
    def cancelled(self, cancelled: str):
        self.__cancelled = cancelled

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aborted(self) -> str:
        return self.__aborted

    @aborted.setter
    def aborted(self, aborted: str):
        self.__aborted = aborted

    @property
    def org_sgiusa_model_Registration(self):
        return self.__org_sgiusa_model_Registration

    @org_sgiusa_model_Registration.setter
    def org_sgiusa_model_Registration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Registration__org_sgiusa_model_Registration", None)
        self.__org_sgiusa_model_Registration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User217"):
                opp_val = getattr(old_value, "User217", None)
                if opp_val == self:
                    setattr(old_value, "User217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User217"):
                opp_val = getattr(value, "User217", None)
                setattr(value, "User217", self)

class org_sgiusa_model_Preferences:

    def __init__(self, id: str, userId: str, themeId: str, selectedView: str, selectedNode: str, openViews: str, openNodes: str, enableTooltips: str):
        self.id = id
        self.userId = userId
        self.themeId = themeId
        self.selectedView = selectedView
        self.selectedNode = selectedNode
        self.openViews = openViews
        self.openNodes = openNodes
        self.enableTooltips = enableTooltips
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def enableTooltips(self) -> str:
        return self.__enableTooltips

    @enableTooltips.setter
    def enableTooltips(self, enableTooltips: str):
        self.__enableTooltips = enableTooltips

    @property
    def selectedView(self) -> str:
        return self.__selectedView

    @selectedView.setter
    def selectedView(self, selectedView: str):
        self.__selectedView = selectedView

    @property
    def selectedNode(self) -> str:
        return self.__selectedNode

    @selectedNode.setter
    def selectedNode(self, selectedNode: str):
        self.__selectedNode = selectedNode

    @property
    def openViews(self) -> str:
        return self.__openViews

    @openViews.setter
    def openViews(self, openViews: str):
        self.__openViews = openViews

    @property
    def openNodes(self) -> str:
        return self.__openNodes

    @openNodes.setter
    def openNodes(self, openNodes: str):
        self.__openNodes = openNodes

    @property
    def themeId(self) -> str:
        return self.__themeId

    @themeId.setter
    def themeId(self, themeId: str):
        self.__themeId = themeId

class org_sgiusa_model_Permission:

    def __init__(self, divisions: str, subDivisions: str, activityGroups: str, capabilities: str, id: str, userId: str, enabled: str, org_sgiusa_model_Permission: "Organization" = None):
        self.divisions = divisions
        self.subDivisions = subDivisions
        self.activityGroups = activityGroups
        self.capabilities = capabilities
        self.id = id
        self.userId = userId
        self.enabled = enabled
        self.org_sgiusa_model_Permission = org_sgiusa_model_Permission
        
    @property
    def enabled(self) -> str:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: str):
        self.__enabled = enabled

    @property
    def activityGroups(self) -> str:
        return self.__activityGroups

    @activityGroups.setter
    def activityGroups(self, activityGroups: str):
        self.__activityGroups = activityGroups

    @property
    def divisions(self) -> str:
        return self.__divisions

    @divisions.setter
    def divisions(self, divisions: str):
        self.__divisions = divisions

    @property
    def capabilities(self) -> str:
        return self.__capabilities

    @capabilities.setter
    def capabilities(self, capabilities: str):
        self.__capabilities = capabilities

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def subDivisions(self) -> str:
        return self.__subDivisions

    @subDivisions.setter
    def subDivisions(self, subDivisions: str):
        self.__subDivisions = subDivisions

    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def org_sgiusa_model_Permission(self):
        return self.__org_sgiusa_model_Permission

    @org_sgiusa_model_Permission.setter
    def org_sgiusa_model_Permission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Permission__org_sgiusa_model_Permission", None)
        self.__org_sgiusa_model_Permission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization215"):
                opp_val = getattr(old_value, "Organization215", None)
                if opp_val == self:
                    setattr(old_value, "Organization215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization215"):
                opp_val = getattr(value, "Organization215", None)
                setattr(value, "Organization215", self)

class org_sgiusa_model_Organization:

    def __init__(self, organizationId: str, permissionId: str, type: str, level: str, name: str, id: str, zipCodes: str, creationDate: str, lastUpdate: str, abbrv: str, label: str, org_sgiusa_model_Organization212: set["User"] = None, org_sgiusa_model_Organization: "Organization" = None, org_sgiusa_model_Organization203: set["Organization"] = None, org_sgiusa_model_Organization206: "User" = None, org_sgiusa_model_Organization209: "User" = None):
        self.organizationId = organizationId
        self.permissionId = permissionId
        self.type = type
        self.level = level
        self.name = name
        self.id = id
        self.zipCodes = zipCodes
        self.creationDate = creationDate
        self.lastUpdate = lastUpdate
        self.abbrv = abbrv
        self.label = label
        self.org_sgiusa_model_Organization212 = org_sgiusa_model_Organization212 if org_sgiusa_model_Organization212 is not None else set()
        self.org_sgiusa_model_Organization = org_sgiusa_model_Organization
        self.org_sgiusa_model_Organization203 = org_sgiusa_model_Organization203 if org_sgiusa_model_Organization203 is not None else set()
        self.org_sgiusa_model_Organization206 = org_sgiusa_model_Organization206
        self.org_sgiusa_model_Organization209 = org_sgiusa_model_Organization209
        
    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def abbrv(self) -> str:
        return self.__abbrv

    @abbrv.setter
    def abbrv(self, abbrv: str):
        self.__abbrv = abbrv

    @property
    def permissionId(self) -> str:
        return self.__permissionId

    @permissionId.setter
    def permissionId(self, permissionId: str):
        self.__permissionId = permissionId

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def zipCodes(self) -> str:
        return self.__zipCodes

    @zipCodes.setter
    def zipCodes(self, zipCodes: str):
        self.__zipCodes = zipCodes

    @property
    def creationDate(self) -> str:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: str):
        self.__creationDate = creationDate

    @property
    def organizationId(self) -> str:
        return self.__organizationId

    @organizationId.setter
    def organizationId(self, organizationId: str):
        self.__organizationId = organizationId

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def org_sgiusa_model_Organization203(self):
        return self.__org_sgiusa_model_Organization203

    @org_sgiusa_model_Organization203.setter
    def org_sgiusa_model_Organization203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Organization__org_sgiusa_model_Organization203", None)
        self.__org_sgiusa_model_Organization203 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Organization204"):
                    opp_val = getattr(item, "Organization204", None)
                    
                    if opp_val == self:
                        setattr(item, "Organization204", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Organization204"):
                    opp_val = getattr(item, "Organization204", None)
                    
                    setattr(item, "Organization204", self)
                    

    @property
    def org_sgiusa_model_Organization(self):
        return self.__org_sgiusa_model_Organization

    @org_sgiusa_model_Organization.setter
    def org_sgiusa_model_Organization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Organization__org_sgiusa_model_Organization", None)
        self.__org_sgiusa_model_Organization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization201"):
                opp_val = getattr(old_value, "Organization201", None)
                if opp_val == self:
                    setattr(old_value, "Organization201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization201"):
                opp_val = getattr(value, "Organization201", None)
                setattr(value, "Organization201", self)

    @property
    def org_sgiusa_model_Organization212(self):
        return self.__org_sgiusa_model_Organization212

    @org_sgiusa_model_Organization212.setter
    def org_sgiusa_model_Organization212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Organization__org_sgiusa_model_Organization212", None)
        self.__org_sgiusa_model_Organization212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User213"):
                    opp_val = getattr(item, "User213", None)
                    
                    if opp_val == self:
                        setattr(item, "User213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User213"):
                    opp_val = getattr(item, "User213", None)
                    
                    setattr(item, "User213", self)
                    

    @property
    def org_sgiusa_model_Organization206(self):
        return self.__org_sgiusa_model_Organization206

    @org_sgiusa_model_Organization206.setter
    def org_sgiusa_model_Organization206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Organization__org_sgiusa_model_Organization206", None)
        self.__org_sgiusa_model_Organization206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User207"):
                opp_val = getattr(old_value, "User207", None)
                if opp_val == self:
                    setattr(old_value, "User207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User207"):
                opp_val = getattr(value, "User207", None)
                setattr(value, "User207", self)

    @property
    def org_sgiusa_model_Organization209(self):
        return self.__org_sgiusa_model_Organization209

    @org_sgiusa_model_Organization209.setter
    def org_sgiusa_model_Organization209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Organization__org_sgiusa_model_Organization209", None)
        self.__org_sgiusa_model_Organization209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User210"):
                opp_val = getattr(old_value, "User210", None)
                if opp_val == self:
                    setattr(old_value, "User210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User210"):
                opp_val = getattr(value, "User210", None)
                setattr(value, "User210", self)

class org_sgiusa_model_MembershipInfo:

    def __init__(self, receivedCertificate: str, notActivated: str, notLocatable: str, lastUpdate: str, id: str, friendOfSgi: str, org_sgiusa_model_MembershipInfo: set["GohonzonInfo"] = None):
        self.receivedCertificate = receivedCertificate
        self.notActivated = notActivated
        self.notLocatable = notLocatable
        self.lastUpdate = lastUpdate
        self.id = id
        self.friendOfSgi = friendOfSgi
        self.org_sgiusa_model_MembershipInfo = org_sgiusa_model_MembershipInfo if org_sgiusa_model_MembershipInfo is not None else set()
        
    @property
    def notLocatable(self) -> str:
        return self.__notLocatable

    @notLocatable.setter
    def notLocatable(self, notLocatable: str):
        self.__notLocatable = notLocatable

    @property
    def friendOfSgi(self) -> str:
        return self.__friendOfSgi

    @friendOfSgi.setter
    def friendOfSgi(self, friendOfSgi: str):
        self.__friendOfSgi = friendOfSgi

    @property
    def notActivated(self) -> str:
        return self.__notActivated

    @notActivated.setter
    def notActivated(self, notActivated: str):
        self.__notActivated = notActivated

    @property
    def receivedCertificate(self) -> str:
        return self.__receivedCertificate

    @receivedCertificate.setter
    def receivedCertificate(self, receivedCertificate: str):
        self.__receivedCertificate = receivedCertificate

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def org_sgiusa_model_MembershipInfo(self):
        return self.__org_sgiusa_model_MembershipInfo

    @org_sgiusa_model_MembershipInfo.setter
    def org_sgiusa_model_MembershipInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_MembershipInfo__org_sgiusa_model_MembershipInfo", None)
        self.__org_sgiusa_model_MembershipInfo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GohonzonInfo197"):
                    opp_val = getattr(item, "GohonzonInfo197", None)
                    
                    if opp_val == self:
                        setattr(item, "GohonzonInfo197", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GohonzonInfo197"):
                    opp_val = getattr(item, "GohonzonInfo197", None)
                    
                    setattr(item, "GohonzonInfo197", self)
                    

class org_sgiusa_model_Note:

    def __init__(self, id: str, text: str, creationDate: str, lastUpdate: str, org_sgiusa_model_Note: "User" = None):
        self.id = id
        self.text = text
        self.creationDate = creationDate
        self.lastUpdate = lastUpdate
        self.org_sgiusa_model_Note = org_sgiusa_model_Note
        
    @property
    def creationDate(self) -> str:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: str):
        self.__creationDate = creationDate

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def org_sgiusa_model_Note(self):
        return self.__org_sgiusa_model_Note

    @org_sgiusa_model_Note.setter
    def org_sgiusa_model_Note(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Note__org_sgiusa_model_Note", None)
        self.__org_sgiusa_model_Note = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User199"):
                opp_val = getattr(old_value, "User199", None)
                if opp_val == self:
                    setattr(old_value, "User199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User199"):
                opp_val = getattr(value, "User199", None)
                setattr(value, "User199", self)

class org_sgiusa_model_MemberSearchCriteria:

    def __init__(self, divisions: str, subDivisions: str, activityGroups: str, org_sgiusa_model_MemberSearchCriteria: set["Organization"] = None):
        self.divisions = divisions
        self.subDivisions = subDivisions
        self.activityGroups = activityGroups
        self.org_sgiusa_model_MemberSearchCriteria = org_sgiusa_model_MemberSearchCriteria if org_sgiusa_model_MemberSearchCriteria is not None else set()
        
    @property
    def activityGroups(self) -> str:
        return self.__activityGroups

    @activityGroups.setter
    def activityGroups(self, activityGroups: str):
        self.__activityGroups = activityGroups

    @property
    def subDivisions(self) -> str:
        return self.__subDivisions

    @subDivisions.setter
    def subDivisions(self, subDivisions: str):
        self.__subDivisions = subDivisions

    @property
    def divisions(self) -> str:
        return self.__divisions

    @divisions.setter
    def divisions(self, divisions: str):
        self.__divisions = divisions

    @property
    def org_sgiusa_model_MemberSearchCriteria(self):
        return self.__org_sgiusa_model_MemberSearchCriteria

    @org_sgiusa_model_MemberSearchCriteria.setter
    def org_sgiusa_model_MemberSearchCriteria(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_MemberSearchCriteria__org_sgiusa_model_MemberSearchCriteria", None)
        self.__org_sgiusa_model_MemberSearchCriteria = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Organization195"):
                    opp_val = getattr(item, "Organization195", None)
                    
                    if opp_val == self:
                        setattr(item, "Organization195", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Organization195"):
                    opp_val = getattr(item, "Organization195", None)
                    
                    setattr(item, "Organization195", self)
                    

class org_sgiusa_model_Members:

    pass
class org_sgiusa_model_Member:

    def __init__(self, id: str, division: str, firstName: str, lastName: str, middleInitial: str, interests: str, languages: str, joinDate: str, birthDate: str, subDivision: str, activityGroups: str, statusProfile: str, archived: str, employer: str, occupation: str, extraField1: str, extraField2: str, visible: str, locatable: str, org_sgiusa_model_Member172: "PhoneNumber" = None, org_sgiusa_model_Member175: "PhoneNumber" = None, org_sgiusa_model_Member178: "Organization" = None, org_sgiusa_model_Member: "EmailAddress" = None, org_sgiusa_model_Member163: "StreetAddress" = None, org_sgiusa_model_Member166: "PhoneNumber" = None, org_sgiusa_model_Member169: "PhoneNumber" = None, org_sgiusa_model_Member190: "FamilyMember" = None, org_sgiusa_model_Member181: "LeadershipInfo" = None, org_sgiusa_model_Member184: "StudyDeptInfo" = None, org_sgiusa_model_Member187: set["Note"] = None):
        self.id = id
        self.division = division
        self.firstName = firstName
        self.lastName = lastName
        self.middleInitial = middleInitial
        self.interests = interests
        self.languages = languages
        self.joinDate = joinDate
        self.birthDate = birthDate
        self.subDivision = subDivision
        self.activityGroups = activityGroups
        self.statusProfile = statusProfile
        self.archived = archived
        self.employer = employer
        self.occupation = occupation
        self.extraField1 = extraField1
        self.extraField2 = extraField2
        self.visible = visible
        self.locatable = locatable
        self.org_sgiusa_model_Member172 = org_sgiusa_model_Member172
        self.org_sgiusa_model_Member175 = org_sgiusa_model_Member175
        self.org_sgiusa_model_Member178 = org_sgiusa_model_Member178
        self.org_sgiusa_model_Member = org_sgiusa_model_Member
        self.org_sgiusa_model_Member163 = org_sgiusa_model_Member163
        self.org_sgiusa_model_Member166 = org_sgiusa_model_Member166
        self.org_sgiusa_model_Member169 = org_sgiusa_model_Member169
        self.org_sgiusa_model_Member190 = org_sgiusa_model_Member190
        self.org_sgiusa_model_Member181 = org_sgiusa_model_Member181
        self.org_sgiusa_model_Member184 = org_sgiusa_model_Member184
        self.org_sgiusa_model_Member187 = org_sgiusa_model_Member187 if org_sgiusa_model_Member187 is not None else set()
        
    @property
    def visible(self) -> str:
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible

    @property
    def middleInitial(self) -> str:
        return self.__middleInitial

    @middleInitial.setter
    def middleInitial(self, middleInitial: str):
        self.__middleInitial = middleInitial

    @property
    def archived(self) -> str:
        return self.__archived

    @archived.setter
    def archived(self, archived: str):
        self.__archived = archived

    @property
    def birthDate(self) -> str:
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, birthDate: str):
        self.__birthDate = birthDate

    @property
    def interests(self) -> str:
        return self.__interests

    @interests.setter
    def interests(self, interests: str):
        self.__interests = interests

    @property
    def languages(self) -> str:
        return self.__languages

    @languages.setter
    def languages(self, languages: str):
        self.__languages = languages

    @property
    def locatable(self) -> str:
        return self.__locatable

    @locatable.setter
    def locatable(self, locatable: str):
        self.__locatable = locatable

    @property
    def employer(self) -> str:
        return self.__employer

    @employer.setter
    def employer(self, employer: str):
        self.__employer = employer

    @property
    def extraField1(self) -> str:
        return self.__extraField1

    @extraField1.setter
    def extraField1(self, extraField1: str):
        self.__extraField1 = extraField1

    @property
    def occupation(self) -> str:
        return self.__occupation

    @occupation.setter
    def occupation(self, occupation: str):
        self.__occupation = occupation

    @property
    def joinDate(self) -> str:
        return self.__joinDate

    @joinDate.setter
    def joinDate(self, joinDate: str):
        self.__joinDate = joinDate

    @property
    def subDivision(self) -> str:
        return self.__subDivision

    @subDivision.setter
    def subDivision(self, subDivision: str):
        self.__subDivision = subDivision

    @property
    def extraField2(self) -> str:
        return self.__extraField2

    @extraField2.setter
    def extraField2(self, extraField2: str):
        self.__extraField2 = extraField2

    @property
    def division(self) -> str:
        return self.__division

    @division.setter
    def division(self, division: str):
        self.__division = division

    @property
    def statusProfile(self) -> str:
        return self.__statusProfile

    @statusProfile.setter
    def statusProfile(self, statusProfile: str):
        self.__statusProfile = statusProfile

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def activityGroups(self) -> str:
        return self.__activityGroups

    @activityGroups.setter
    def activityGroups(self, activityGroups: str):
        self.__activityGroups = activityGroups

    @property
    def org_sgiusa_model_Member178(self):
        return self.__org_sgiusa_model_Member178

    @org_sgiusa_model_Member178.setter
    def org_sgiusa_model_Member178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Member__org_sgiusa_model_Member178", None)
        self.__org_sgiusa_model_Member178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization179"):
                opp_val = getattr(old_value, "Organization179", None)
                if opp_val == self:
                    setattr(old_value, "Organization179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization179"):
                opp_val = getattr(value, "Organization179", None)
                setattr(value, "Organization179", self)

    @property
    def org_sgiusa_model_Member(self):
        return self.__org_sgiusa_model_Member

    @org_sgiusa_model_Member.setter
    def org_sgiusa_model_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Member__org_sgiusa_model_Member", None)
        self.__org_sgiusa_model_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmailAddress161"):
                opp_val = getattr(old_value, "EmailAddress161", None)
                if opp_val == self:
                    setattr(old_value, "EmailAddress161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmailAddress161"):
                opp_val = getattr(value, "EmailAddress161", None)
                setattr(value, "EmailAddress161", self)

    @property
    def org_sgiusa_model_Member181(self):
        return self.__org_sgiusa_model_Member181

    @org_sgiusa_model_Member181.setter
    def org_sgiusa_model_Member181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Member__org_sgiusa_model_Member181", None)
        self.__org_sgiusa_model_Member181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LeadershipInfo182"):
                opp_val = getattr(old_value, "LeadershipInfo182", None)
                if opp_val == self:
                    setattr(old_value, "LeadershipInfo182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LeadershipInfo182"):
                opp_val = getattr(value, "LeadershipInfo182", None)
                setattr(value, "LeadershipInfo182", self)

    @property
    def org_sgiusa_model_Member172(self):
        return self.__org_sgiusa_model_Member172

    @org_sgiusa_model_Member172.setter
    def org_sgiusa_model_Member172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Member__org_sgiusa_model_Member172", None)
        self.__org_sgiusa_model_Member172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhoneNumber173"):
                opp_val = getattr(old_value, "PhoneNumber173", None)
                if opp_val == self:
                    setattr(old_value, "PhoneNumber173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhoneNumber173"):
                opp_val = getattr(value, "PhoneNumber173", None)
                setattr(value, "PhoneNumber173", self)

    @property
    def org_sgiusa_model_Member187(self):
        return self.__org_sgiusa_model_Member187

    @org_sgiusa_model_Member187.setter
    def org_sgiusa_model_Member187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Member__org_sgiusa_model_Member187", None)
        self.__org_sgiusa_model_Member187 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Note188"):
                    opp_val = getattr(item, "Note188", None)
                    
                    if opp_val == self:
                        setattr(item, "Note188", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Note188"):
                    opp_val = getattr(item, "Note188", None)
                    
                    setattr(item, "Note188", self)
                    

    @property
    def org_sgiusa_model_Member175(self):
        return self.__org_sgiusa_model_Member175

    @org_sgiusa_model_Member175.setter
    def org_sgiusa_model_Member175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Member__org_sgiusa_model_Member175", None)
        self.__org_sgiusa_model_Member175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhoneNumber176"):
                opp_val = getattr(old_value, "PhoneNumber176", None)
                if opp_val == self:
                    setattr(old_value, "PhoneNumber176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhoneNumber176"):
                opp_val = getattr(value, "PhoneNumber176", None)
                setattr(value, "PhoneNumber176", self)

    @property
    def org_sgiusa_model_Member166(self):
        return self.__org_sgiusa_model_Member166

    @org_sgiusa_model_Member166.setter
    def org_sgiusa_model_Member166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Member__org_sgiusa_model_Member166", None)
        self.__org_sgiusa_model_Member166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhoneNumber167"):
                opp_val = getattr(old_value, "PhoneNumber167", None)
                if opp_val == self:
                    setattr(old_value, "PhoneNumber167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhoneNumber167"):
                opp_val = getattr(value, "PhoneNumber167", None)
                setattr(value, "PhoneNumber167", self)

    @property
    def org_sgiusa_model_Member169(self):
        return self.__org_sgiusa_model_Member169

    @org_sgiusa_model_Member169.setter
    def org_sgiusa_model_Member169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Member__org_sgiusa_model_Member169", None)
        self.__org_sgiusa_model_Member169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhoneNumber170"):
                opp_val = getattr(old_value, "PhoneNumber170", None)
                if opp_val == self:
                    setattr(old_value, "PhoneNumber170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhoneNumber170"):
                opp_val = getattr(value, "PhoneNumber170", None)
                setattr(value, "PhoneNumber170", self)

    @property
    def org_sgiusa_model_Member190(self):
        return self.__org_sgiusa_model_Member190

    @org_sgiusa_model_Member190.setter
    def org_sgiusa_model_Member190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Member__org_sgiusa_model_Member190", None)
        self.__org_sgiusa_model_Member190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FamilyMember191"):
                opp_val = getattr(old_value, "FamilyMember191", None)
                if opp_val == self:
                    setattr(old_value, "FamilyMember191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FamilyMember191"):
                opp_val = getattr(value, "FamilyMember191", None)
                setattr(value, "FamilyMember191", self)

    @property
    def org_sgiusa_model_Member163(self):
        return self.__org_sgiusa_model_Member163

    @org_sgiusa_model_Member163.setter
    def org_sgiusa_model_Member163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Member__org_sgiusa_model_Member163", None)
        self.__org_sgiusa_model_Member163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StreetAddress164"):
                opp_val = getattr(old_value, "StreetAddress164", None)
                if opp_val == self:
                    setattr(old_value, "StreetAddress164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StreetAddress164"):
                opp_val = getattr(value, "StreetAddress164", None)
                setattr(value, "StreetAddress164", self)

    @property
    def org_sgiusa_model_Member184(self):
        return self.__org_sgiusa_model_Member184

    @org_sgiusa_model_Member184.setter
    def org_sgiusa_model_Member184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Member__org_sgiusa_model_Member184", None)
        self.__org_sgiusa_model_Member184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyDeptInfo185"):
                opp_val = getattr(old_value, "StudyDeptInfo185", None)
                if opp_val == self:
                    setattr(old_value, "StudyDeptInfo185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyDeptInfo185"):
                opp_val = getattr(value, "StudyDeptInfo185", None)
                setattr(value, "StudyDeptInfo185", self)

class org_sgiusa_model_LeadershipInfo:

    def __init__(self, manualSignedDate: str, lastUpdate: str, id: str, examPassed: str, examPassedDate: str, manualSigned: str, org_sgiusa_model_LeadershipInfo: set["LeadershipRole"] = None):
        self.manualSignedDate = manualSignedDate
        self.lastUpdate = lastUpdate
        self.id = id
        self.examPassed = examPassed
        self.examPassedDate = examPassedDate
        self.manualSigned = manualSigned
        self.org_sgiusa_model_LeadershipInfo = org_sgiusa_model_LeadershipInfo if org_sgiusa_model_LeadershipInfo is not None else set()
        
    @property
    def examPassedDate(self) -> str:
        return self.__examPassedDate

    @examPassedDate.setter
    def examPassedDate(self, examPassedDate: str):
        self.__examPassedDate = examPassedDate

    @property
    def manualSigned(self) -> str:
        return self.__manualSigned

    @manualSigned.setter
    def manualSigned(self, manualSigned: str):
        self.__manualSigned = manualSigned

    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def manualSignedDate(self) -> str:
        return self.__manualSignedDate

    @manualSignedDate.setter
    def manualSignedDate(self, manualSignedDate: str):
        self.__manualSignedDate = manualSignedDate

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def examPassed(self) -> str:
        return self.__examPassed

    @examPassed.setter
    def examPassed(self, examPassed: str):
        self.__examPassed = examPassed

    @property
    def org_sgiusa_model_LeadershipInfo(self):
        return self.__org_sgiusa_model_LeadershipInfo

    @org_sgiusa_model_LeadershipInfo.setter
    def org_sgiusa_model_LeadershipInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_LeadershipInfo__org_sgiusa_model_LeadershipInfo", None)
        self.__org_sgiusa_model_LeadershipInfo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LeadershipRole159"):
                    opp_val = getattr(item, "LeadershipRole159", None)
                    
                    if opp_val == self:
                        setattr(item, "LeadershipRole159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LeadershipRole159"):
                    opp_val = getattr(item, "LeadershipRole159", None)
                    
                    setattr(item, "LeadershipRole159", self)
                    

class org_sgiusa_model_LeadershipRole:

    def __init__(self, id: str, startDate: str, endDate: str, lastUpdate: str, active: str, level: str, position: str, division: str, subDivision: str, activityGroup: str):
        self.id = id
        self.startDate = startDate
        self.endDate = endDate
        self.lastUpdate = lastUpdate
        self.active = active
        self.level = level
        self.position = position
        self.division = division
        self.subDivision = subDivision
        self.activityGroup = activityGroup
        
    @property
    def startDate(self) -> str:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def subDivision(self) -> str:
        return self.__subDivision

    @subDivision.setter
    def subDivision(self, subDivision: str):
        self.__subDivision = subDivision

    @property
    def division(self) -> str:
        return self.__division

    @division.setter
    def division(self, division: str):
        self.__division = division

    @property
    def endDate(self) -> str:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate

    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def active(self) -> str:
        return self.__active

    @active.setter
    def active(self, active: str):
        self.__active = active

    @property
    def activityGroup(self) -> str:
        return self.__activityGroup

    @activityGroup.setter
    def activityGroup(self, activityGroup: str):
        self.__activityGroup = activityGroup

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

class org_sgiusa_model_GohonzonInfo:

    def __init__(self, gohonzonType: str, receiveDate: str, returned: str, returnDate: str, lastUpdate: str, id: str):
        self.gohonzonType = gohonzonType
        self.receiveDate = receiveDate
        self.returned = returned
        self.returnDate = returnDate
        self.lastUpdate = lastUpdate
        self.id = id
        
    @property
    def gohonzonType(self) -> str:
        return self.__gohonzonType

    @gohonzonType.setter
    def gohonzonType(self, gohonzonType: str):
        self.__gohonzonType = gohonzonType

    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def receiveDate(self) -> str:
        return self.__receiveDate

    @receiveDate.setter
    def receiveDate(self, receiveDate: str):
        self.__receiveDate = receiveDate

    @property
    def returnDate(self) -> str:
        return self.__returnDate

    @returnDate.setter
    def returnDate(self, returnDate: str):
        self.__returnDate = returnDate

    @property
    def returned(self) -> str:
        return self.__returned

    @returned.setter
    def returned(self, returned: str):
        self.__returned = returned

class org_sgiusa_model_FamilyMember:

    def __init__(self, familyRelation: str, personName: str, lastUpdate: str, id: str, sgiMember: str):
        self.familyRelation = familyRelation
        self.personName = personName
        self.lastUpdate = lastUpdate
        self.id = id
        self.sgiMember = sgiMember
        
    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def personName(self) -> str:
        return self.__personName

    @personName.setter
    def personName(self, personName: str):
        self.__personName = personName

    @property
    def sgiMember(self) -> str:
        return self.__sgiMember

    @sgiMember.setter
    def sgiMember(self, sgiMember: str):
        self.__sgiMember = sgiMember

    @property
    def familyRelation(self) -> str:
        return self.__familyRelation

    @familyRelation.setter
    def familyRelation(self, familyRelation: str):
        self.__familyRelation = familyRelation

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class org_sgiusa_model_EmailList:

    def __init__(self, id: str, enabled: str, divisions: str, subDivisions: str, activityGroups: str, org_sgiusa_model_EmailList: "Organization" = None, org_sgiusa_model_EmailList154: set["User"] = None):
        self.id = id
        self.enabled = enabled
        self.divisions = divisions
        self.subDivisions = subDivisions
        self.activityGroups = activityGroups
        self.org_sgiusa_model_EmailList = org_sgiusa_model_EmailList
        self.org_sgiusa_model_EmailList154 = org_sgiusa_model_EmailList154 if org_sgiusa_model_EmailList154 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def divisions(self) -> str:
        return self.__divisions

    @divisions.setter
    def divisions(self, divisions: str):
        self.__divisions = divisions

    @property
    def enabled(self) -> str:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: str):
        self.__enabled = enabled

    @property
    def subDivisions(self) -> str:
        return self.__subDivisions

    @subDivisions.setter
    def subDivisions(self, subDivisions: str):
        self.__subDivisions = subDivisions

    @property
    def activityGroups(self) -> str:
        return self.__activityGroups

    @activityGroups.setter
    def activityGroups(self, activityGroups: str):
        self.__activityGroups = activityGroups

    @property
    def org_sgiusa_model_EmailList154(self):
        return self.__org_sgiusa_model_EmailList154

    @org_sgiusa_model_EmailList154.setter
    def org_sgiusa_model_EmailList154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_EmailList__org_sgiusa_model_EmailList154", None)
        self.__org_sgiusa_model_EmailList154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User155"):
                    opp_val = getattr(item, "User155", None)
                    
                    if opp_val == self:
                        setattr(item, "User155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User155"):
                    opp_val = getattr(item, "User155", None)
                    
                    setattr(item, "User155", self)
                    

    @property
    def org_sgiusa_model_EmailList(self):
        return self.__org_sgiusa_model_EmailList

    @org_sgiusa_model_EmailList.setter
    def org_sgiusa_model_EmailList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_EmailList__org_sgiusa_model_EmailList", None)
        self.__org_sgiusa_model_EmailList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization152"):
                opp_val = getattr(old_value, "Organization152", None)
                if opp_val == self:
                    setattr(old_value, "Organization152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization152"):
                opp_val = getattr(value, "Organization152", None)
                setattr(value, "Organization152", self)

class org_sgiusa_model_Event:

    def __init__(self, id: str, userId: str, status: str, divisions: str, subDivisions: str, org_sgiusa_model_Event: "Organization" = None):
        self.id = id
        self.userId = userId
        self.status = status
        self.divisions = divisions
        self.subDivisions = subDivisions
        self.org_sgiusa_model_Event = org_sgiusa_model_Event
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def subDivisions(self) -> str:
        return self.__subDivisions

    @subDivisions.setter
    def subDivisions(self, subDivisions: str):
        self.__subDivisions = subDivisions

    @property
    def divisions(self) -> str:
        return self.__divisions

    @divisions.setter
    def divisions(self, divisions: str):
        self.__divisions = divisions

    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def org_sgiusa_model_Event(self):
        return self.__org_sgiusa_model_Event

    @org_sgiusa_model_Event.setter
    def org_sgiusa_model_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_Event__org_sgiusa_model_Event", None)
        self.__org_sgiusa_model_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization157"):
                opp_val = getattr(old_value, "Organization157", None)
                if opp_val == self:
                    setattr(old_value, "Organization157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization157"):
                opp_val = getattr(value, "Organization157", None)
                setattr(value, "Organization157", self)

class StudyDeptExam:

    pass
class SchoolInfo:

    pass
class Registration:

    pass
class Preferences:

    pass
class Permission:

    pass
class View:

    pass
class Users:

    pass
class StudyDeptInfo:

    pass
class MemberSearchCriteria:

    pass
class Members:

    pass
class Organization:

    pass
class MembershipInfo:

    pass
class LeadershipRole:

    pass
class LeadershipInfo:

    pass
class GohonzonInfo:

    pass
class Member:

    pass
class EmailList:

    pass
class FamilyMember:

    pass
class org_sgiusa_model_DocumentRoot:

    def __init__(self, mixed: str, org_sgiusa_model_DocumentRoot: set["org_sgiusa_model_EStringToStringMapEntry"] = None, org_sgiusa_model_DocumentRoot104: set["org_sgiusa_model_EStringToStringMapEntry"] = None, org_sgiusa_model_DocumentRoot112: set["FamilyMember"] = None, org_sgiusa_model_DocumentRoot107: set["EmailList"] = None, org_sgiusa_model_DocumentRoot109: set["Event"] = None, org_sgiusa_model_DocumentRoot120: set["Member"] = None, org_sgiusa_model_DocumentRoot114: set["GohonzonInfo"] = None, org_sgiusa_model_DocumentRoot116: set["LeadershipInfo"] = None, org_sgiusa_model_DocumentRoot118: set["LeadershipRole"] = None, org_sgiusa_model_DocumentRoot126: set["MembershipInfo"] = None, org_sgiusa_model_DocumentRoot128: set["Note"] = None, org_sgiusa_model_DocumentRoot131: set["Organization"] = None, org_sgiusa_model_DocumentRoot122: set["Members"] = None, org_sgiusa_model_DocumentRoot124: set["MemberSearchCriteria"] = None, org_sgiusa_model_DocumentRoot143: set["StudyDeptInfo"] = None, org_sgiusa_model_DocumentRoot145: set["User"] = None, org_sgiusa_model_DocumentRoot148: set["Users"] = None, org_sgiusa_model_DocumentRoot150: set["View"] = None, org_sgiusa_model_DocumentRoot133: set["Permission"] = None, org_sgiusa_model_DocumentRoot135: set["Preferences"] = None, org_sgiusa_model_DocumentRoot137: set["Registration"] = None, org_sgiusa_model_DocumentRoot139: set["SchoolInfo"] = None, org_sgiusa_model_DocumentRoot141: set["StudyDeptExam"] = None):
        self.mixed = mixed
        self.org_sgiusa_model_DocumentRoot = org_sgiusa_model_DocumentRoot if org_sgiusa_model_DocumentRoot is not None else set()
        self.org_sgiusa_model_DocumentRoot104 = org_sgiusa_model_DocumentRoot104 if org_sgiusa_model_DocumentRoot104 is not None else set()
        self.org_sgiusa_model_DocumentRoot112 = org_sgiusa_model_DocumentRoot112 if org_sgiusa_model_DocumentRoot112 is not None else set()
        self.org_sgiusa_model_DocumentRoot107 = org_sgiusa_model_DocumentRoot107 if org_sgiusa_model_DocumentRoot107 is not None else set()
        self.org_sgiusa_model_DocumentRoot109 = org_sgiusa_model_DocumentRoot109 if org_sgiusa_model_DocumentRoot109 is not None else set()
        self.org_sgiusa_model_DocumentRoot120 = org_sgiusa_model_DocumentRoot120 if org_sgiusa_model_DocumentRoot120 is not None else set()
        self.org_sgiusa_model_DocumentRoot114 = org_sgiusa_model_DocumentRoot114 if org_sgiusa_model_DocumentRoot114 is not None else set()
        self.org_sgiusa_model_DocumentRoot116 = org_sgiusa_model_DocumentRoot116 if org_sgiusa_model_DocumentRoot116 is not None else set()
        self.org_sgiusa_model_DocumentRoot118 = org_sgiusa_model_DocumentRoot118 if org_sgiusa_model_DocumentRoot118 is not None else set()
        self.org_sgiusa_model_DocumentRoot126 = org_sgiusa_model_DocumentRoot126 if org_sgiusa_model_DocumentRoot126 is not None else set()
        self.org_sgiusa_model_DocumentRoot128 = org_sgiusa_model_DocumentRoot128 if org_sgiusa_model_DocumentRoot128 is not None else set()
        self.org_sgiusa_model_DocumentRoot131 = org_sgiusa_model_DocumentRoot131 if org_sgiusa_model_DocumentRoot131 is not None else set()
        self.org_sgiusa_model_DocumentRoot122 = org_sgiusa_model_DocumentRoot122 if org_sgiusa_model_DocumentRoot122 is not None else set()
        self.org_sgiusa_model_DocumentRoot124 = org_sgiusa_model_DocumentRoot124 if org_sgiusa_model_DocumentRoot124 is not None else set()
        self.org_sgiusa_model_DocumentRoot143 = org_sgiusa_model_DocumentRoot143 if org_sgiusa_model_DocumentRoot143 is not None else set()
        self.org_sgiusa_model_DocumentRoot145 = org_sgiusa_model_DocumentRoot145 if org_sgiusa_model_DocumentRoot145 is not None else set()
        self.org_sgiusa_model_DocumentRoot148 = org_sgiusa_model_DocumentRoot148 if org_sgiusa_model_DocumentRoot148 is not None else set()
        self.org_sgiusa_model_DocumentRoot150 = org_sgiusa_model_DocumentRoot150 if org_sgiusa_model_DocumentRoot150 is not None else set()
        self.org_sgiusa_model_DocumentRoot133 = org_sgiusa_model_DocumentRoot133 if org_sgiusa_model_DocumentRoot133 is not None else set()
        self.org_sgiusa_model_DocumentRoot135 = org_sgiusa_model_DocumentRoot135 if org_sgiusa_model_DocumentRoot135 is not None else set()
        self.org_sgiusa_model_DocumentRoot137 = org_sgiusa_model_DocumentRoot137 if org_sgiusa_model_DocumentRoot137 is not None else set()
        self.org_sgiusa_model_DocumentRoot139 = org_sgiusa_model_DocumentRoot139 if org_sgiusa_model_DocumentRoot139 is not None else set()
        self.org_sgiusa_model_DocumentRoot141 = org_sgiusa_model_DocumentRoot141 if org_sgiusa_model_DocumentRoot141 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def org_sgiusa_model_DocumentRoot137(self):
        return self.__org_sgiusa_model_DocumentRoot137

    @org_sgiusa_model_DocumentRoot137.setter
    def org_sgiusa_model_DocumentRoot137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot137", None)
        self.__org_sgiusa_model_DocumentRoot137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Registration"):
                    opp_val = getattr(item, "Registration", None)
                    
                    if opp_val == self:
                        setattr(item, "Registration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Registration"):
                    opp_val = getattr(item, "Registration", None)
                    
                    setattr(item, "Registration", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot135(self):
        return self.__org_sgiusa_model_DocumentRoot135

    @org_sgiusa_model_DocumentRoot135.setter
    def org_sgiusa_model_DocumentRoot135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot135", None)
        self.__org_sgiusa_model_DocumentRoot135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Preferences"):
                    opp_val = getattr(item, "Preferences", None)
                    
                    if opp_val == self:
                        setattr(item, "Preferences", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Preferences"):
                    opp_val = getattr(item, "Preferences", None)
                    
                    setattr(item, "Preferences", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot133(self):
        return self.__org_sgiusa_model_DocumentRoot133

    @org_sgiusa_model_DocumentRoot133.setter
    def org_sgiusa_model_DocumentRoot133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot133", None)
        self.__org_sgiusa_model_DocumentRoot133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Permission"):
                    opp_val = getattr(item, "Permission", None)
                    
                    if opp_val == self:
                        setattr(item, "Permission", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Permission"):
                    opp_val = getattr(item, "Permission", None)
                    
                    setattr(item, "Permission", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot128(self):
        return self.__org_sgiusa_model_DocumentRoot128

    @org_sgiusa_model_DocumentRoot128.setter
    def org_sgiusa_model_DocumentRoot128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot128", None)
        self.__org_sgiusa_model_DocumentRoot128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Note129"):
                    opp_val = getattr(item, "Note129", None)
                    
                    if opp_val == self:
                        setattr(item, "Note129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Note129"):
                    opp_val = getattr(item, "Note129", None)
                    
                    setattr(item, "Note129", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot116(self):
        return self.__org_sgiusa_model_DocumentRoot116

    @org_sgiusa_model_DocumentRoot116.setter
    def org_sgiusa_model_DocumentRoot116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot116", None)
        self.__org_sgiusa_model_DocumentRoot116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LeadershipInfo"):
                    opp_val = getattr(item, "LeadershipInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "LeadershipInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LeadershipInfo"):
                    opp_val = getattr(item, "LeadershipInfo", None)
                    
                    setattr(item, "LeadershipInfo", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot141(self):
        return self.__org_sgiusa_model_DocumentRoot141

    @org_sgiusa_model_DocumentRoot141.setter
    def org_sgiusa_model_DocumentRoot141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot141", None)
        self.__org_sgiusa_model_DocumentRoot141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyDeptExam"):
                    opp_val = getattr(item, "StudyDeptExam", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyDeptExam", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyDeptExam"):
                    opp_val = getattr(item, "StudyDeptExam", None)
                    
                    setattr(item, "StudyDeptExam", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot143(self):
        return self.__org_sgiusa_model_DocumentRoot143

    @org_sgiusa_model_DocumentRoot143.setter
    def org_sgiusa_model_DocumentRoot143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot143", None)
        self.__org_sgiusa_model_DocumentRoot143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyDeptInfo"):
                    opp_val = getattr(item, "StudyDeptInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyDeptInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyDeptInfo"):
                    opp_val = getattr(item, "StudyDeptInfo", None)
                    
                    setattr(item, "StudyDeptInfo", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot124(self):
        return self.__org_sgiusa_model_DocumentRoot124

    @org_sgiusa_model_DocumentRoot124.setter
    def org_sgiusa_model_DocumentRoot124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot124", None)
        self.__org_sgiusa_model_DocumentRoot124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MemberSearchCriteria"):
                    opp_val = getattr(item, "MemberSearchCriteria", None)
                    
                    if opp_val == self:
                        setattr(item, "MemberSearchCriteria", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MemberSearchCriteria"):
                    opp_val = getattr(item, "MemberSearchCriteria", None)
                    
                    setattr(item, "MemberSearchCriteria", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot114(self):
        return self.__org_sgiusa_model_DocumentRoot114

    @org_sgiusa_model_DocumentRoot114.setter
    def org_sgiusa_model_DocumentRoot114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot114", None)
        self.__org_sgiusa_model_DocumentRoot114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GohonzonInfo"):
                    opp_val = getattr(item, "GohonzonInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "GohonzonInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GohonzonInfo"):
                    opp_val = getattr(item, "GohonzonInfo", None)
                    
                    setattr(item, "GohonzonInfo", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot148(self):
        return self.__org_sgiusa_model_DocumentRoot148

    @org_sgiusa_model_DocumentRoot148.setter
    def org_sgiusa_model_DocumentRoot148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot148", None)
        self.__org_sgiusa_model_DocumentRoot148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Users"):
                    opp_val = getattr(item, "Users", None)
                    
                    if opp_val == self:
                        setattr(item, "Users", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Users"):
                    opp_val = getattr(item, "Users", None)
                    
                    setattr(item, "Users", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot120(self):
        return self.__org_sgiusa_model_DocumentRoot120

    @org_sgiusa_model_DocumentRoot120.setter
    def org_sgiusa_model_DocumentRoot120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot120", None)
        self.__org_sgiusa_model_DocumentRoot120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member"):
                    opp_val = getattr(item, "Member", None)
                    
                    if opp_val == self:
                        setattr(item, "Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member"):
                    opp_val = getattr(item, "Member", None)
                    
                    setattr(item, "Member", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot145(self):
        return self.__org_sgiusa_model_DocumentRoot145

    @org_sgiusa_model_DocumentRoot145.setter
    def org_sgiusa_model_DocumentRoot145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot145", None)
        self.__org_sgiusa_model_DocumentRoot145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User146"):
                    opp_val = getattr(item, "User146", None)
                    
                    if opp_val == self:
                        setattr(item, "User146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User146"):
                    opp_val = getattr(item, "User146", None)
                    
                    setattr(item, "User146", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot107(self):
        return self.__org_sgiusa_model_DocumentRoot107

    @org_sgiusa_model_DocumentRoot107.setter
    def org_sgiusa_model_DocumentRoot107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot107", None)
        self.__org_sgiusa_model_DocumentRoot107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailList"):
                    opp_val = getattr(item, "EmailList", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailList", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailList"):
                    opp_val = getattr(item, "EmailList", None)
                    
                    setattr(item, "EmailList", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot139(self):
        return self.__org_sgiusa_model_DocumentRoot139

    @org_sgiusa_model_DocumentRoot139.setter
    def org_sgiusa_model_DocumentRoot139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot139", None)
        self.__org_sgiusa_model_DocumentRoot139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SchoolInfo"):
                    opp_val = getattr(item, "SchoolInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "SchoolInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SchoolInfo"):
                    opp_val = getattr(item, "SchoolInfo", None)
                    
                    setattr(item, "SchoolInfo", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot131(self):
        return self.__org_sgiusa_model_DocumentRoot131

    @org_sgiusa_model_DocumentRoot131.setter
    def org_sgiusa_model_DocumentRoot131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot131", None)
        self.__org_sgiusa_model_DocumentRoot131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Organization"):
                    opp_val = getattr(item, "Organization", None)
                    
                    if opp_val == self:
                        setattr(item, "Organization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Organization"):
                    opp_val = getattr(item, "Organization", None)
                    
                    setattr(item, "Organization", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot150(self):
        return self.__org_sgiusa_model_DocumentRoot150

    @org_sgiusa_model_DocumentRoot150.setter
    def org_sgiusa_model_DocumentRoot150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot150", None)
        self.__org_sgiusa_model_DocumentRoot150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "View"):
                    opp_val = getattr(item, "View", None)
                    
                    if opp_val == self:
                        setattr(item, "View", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "View"):
                    opp_val = getattr(item, "View", None)
                    
                    setattr(item, "View", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot126(self):
        return self.__org_sgiusa_model_DocumentRoot126

    @org_sgiusa_model_DocumentRoot126.setter
    def org_sgiusa_model_DocumentRoot126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot126", None)
        self.__org_sgiusa_model_DocumentRoot126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MembershipInfo"):
                    opp_val = getattr(item, "MembershipInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "MembershipInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MembershipInfo"):
                    opp_val = getattr(item, "MembershipInfo", None)
                    
                    setattr(item, "MembershipInfo", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot112(self):
        return self.__org_sgiusa_model_DocumentRoot112

    @org_sgiusa_model_DocumentRoot112.setter
    def org_sgiusa_model_DocumentRoot112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot112", None)
        self.__org_sgiusa_model_DocumentRoot112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FamilyMember"):
                    opp_val = getattr(item, "FamilyMember", None)
                    
                    if opp_val == self:
                        setattr(item, "FamilyMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FamilyMember"):
                    opp_val = getattr(item, "FamilyMember", None)
                    
                    setattr(item, "FamilyMember", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot109(self):
        return self.__org_sgiusa_model_DocumentRoot109

    @org_sgiusa_model_DocumentRoot109.setter
    def org_sgiusa_model_DocumentRoot109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot109", None)
        self.__org_sgiusa_model_DocumentRoot109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event110"):
                    opp_val = getattr(item, "Event110", None)
                    
                    if opp_val == self:
                        setattr(item, "Event110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event110"):
                    opp_val = getattr(item, "Event110", None)
                    
                    setattr(item, "Event110", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot(self):
        return self.__org_sgiusa_model_DocumentRoot

    @org_sgiusa_model_DocumentRoot.setter
    def org_sgiusa_model_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot", None)
        self.__org_sgiusa_model_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "org_sgiusa_model_EStringToStringMapEntry"):
                    opp_val = getattr(item, "org_sgiusa_model_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "org_sgiusa_model_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "org_sgiusa_model_EStringToStringMapEntry"):
                    opp_val = getattr(item, "org_sgiusa_model_EStringToStringMapEntry", None)
                    
                    setattr(item, "org_sgiusa_model_EStringToStringMapEntry", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot118(self):
        return self.__org_sgiusa_model_DocumentRoot118

    @org_sgiusa_model_DocumentRoot118.setter
    def org_sgiusa_model_DocumentRoot118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot118", None)
        self.__org_sgiusa_model_DocumentRoot118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LeadershipRole"):
                    opp_val = getattr(item, "LeadershipRole", None)
                    
                    if opp_val == self:
                        setattr(item, "LeadershipRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LeadershipRole"):
                    opp_val = getattr(item, "LeadershipRole", None)
                    
                    setattr(item, "LeadershipRole", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot104(self):
        return self.__org_sgiusa_model_DocumentRoot104

    @org_sgiusa_model_DocumentRoot104.setter
    def org_sgiusa_model_DocumentRoot104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot104", None)
        self.__org_sgiusa_model_DocumentRoot104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "org_sgiusa_model_EStringToStringMapEntry105"):
                    opp_val = getattr(item, "org_sgiusa_model_EStringToStringMapEntry105", None)
                    
                    if opp_val == self:
                        setattr(item, "org_sgiusa_model_EStringToStringMapEntry105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "org_sgiusa_model_EStringToStringMapEntry105"):
                    opp_val = getattr(item, "org_sgiusa_model_EStringToStringMapEntry105", None)
                    
                    setattr(item, "org_sgiusa_model_EStringToStringMapEntry105", self)
                    

    @property
    def org_sgiusa_model_DocumentRoot122(self):
        return self.__org_sgiusa_model_DocumentRoot122

    @org_sgiusa_model_DocumentRoot122.setter
    def org_sgiusa_model_DocumentRoot122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_sgiusa_model_DocumentRoot__org_sgiusa_model_DocumentRoot122", None)
        self.__org_sgiusa_model_DocumentRoot122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Members"):
                    opp_val = getattr(item, "Members", None)
                    
                    if opp_val == self:
                        setattr(item, "Members", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Members"):
                    opp_val = getattr(item, "Members", None)
                    
                    setattr(item, "Members", self)
                    

class org_sgiusa_model_EStringToStringMapEntry:

    pass
class org_aries_common_ZipCode:

    def __init__(self, country: str, extension: str, number: str):
        self.country = country
        self.extension = extension
        self.number = number
        
    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

class org_aries_common_User:

    def __init__(self, id: str, userId: str, password: str, firstName: str, lastName: str, enabled: str, org_aries_common_User: "PhoneNumber" = None, org_aries_common_User100: "EmailAddress" = None):
        self.id = id
        self.userId = userId
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.enabled = enabled
        self.org_aries_common_User = org_aries_common_User
        self.org_aries_common_User100 = org_aries_common_User100
        
    @property
    def enabled(self) -> str:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: str):
        self.__enabled = enabled

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def org_aries_common_User(self):
        return self.__org_aries_common_User

    @org_aries_common_User.setter
    def org_aries_common_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_User__org_aries_common_User", None)
        self.__org_aries_common_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhoneNumber98"):
                opp_val = getattr(old_value, "PhoneNumber98", None)
                if opp_val == self:
                    setattr(old_value, "PhoneNumber98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhoneNumber98"):
                opp_val = getattr(value, "PhoneNumber98", None)
                setattr(value, "PhoneNumber98", self)

    @property
    def org_aries_common_User100(self):
        return self.__org_aries_common_User100

    @org_aries_common_User100.setter
    def org_aries_common_User100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_User__org_aries_common_User100", None)
        self.__org_aries_common_User100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmailAddress101"):
                opp_val = getattr(old_value, "EmailAddress101", None)
                if opp_val == self:
                    setattr(old_value, "EmailAddress101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmailAddress101"):
                opp_val = getattr(value, "EmailAddress101", None)
                setattr(value, "EmailAddress101", self)

class org_aries_common_StreetAddress:

    def __init__(self, city: str, country: str, id: str, latitude: str, longitude: str, state: str, street: str, org_aries_common_StreetAddress: "ZipCode" = None):
        self.city = city
        self.country = country
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.state = state
        self.street = street
        self.org_aries_common_StreetAddress = org_aries_common_StreetAddress
        
    @property
    def longitude(self) -> str:
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude: str):
        self.__longitude = longitude

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def latitude(self) -> str:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: str):
        self.__latitude = latitude

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def org_aries_common_StreetAddress(self):
        return self.__org_aries_common_StreetAddress

    @org_aries_common_StreetAddress.setter
    def org_aries_common_StreetAddress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_StreetAddress__org_aries_common_StreetAddress", None)
        self.__org_aries_common_StreetAddress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ZipCode96"):
                opp_val = getattr(old_value, "ZipCode96", None)
                if opp_val == self:
                    setattr(old_value, "ZipCode96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ZipCode96"):
                opp_val = getattr(value, "ZipCode96", None)
                setattr(value, "ZipCode96", self)

class org_aries_common_Properties:

    pass
class org_aries_common_Property:

    def __init__(self, mixed: str, id: str, name: str, value: str):
        self.mixed = mixed
        self.id = id
        self.name = name
        self.value = value
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

class org_aries_common_PhoneNumber:

    def __init__(self, country: str, extension: str, number: str, id: str, type: str, area: str, value: str):
        self.country = country
        self.extension = extension
        self.number = number
        self.id = id
        self.type = type
        self.area = area
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

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
    def area(self) -> str:
        return self.__area

    @area.setter
    def area(self, area: str):
        self.__area = area

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class org_aries_common_PersonName:

    def __init__(self, lastName: str, firstName: str, middleInitial: str):
        self.lastName = lastName
        self.firstName = firstName
        self.middleInitial = middleInitial
        
    @property
    def middleInitial(self) -> str:
        return self.__middleInitial

    @middleInitial.setter
    def middleInitial(self, middleInitial: str):
        self.__middleInitial = middleInitial

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

class org_aries_common_Note:

    def __init__(self, id: str, creationDate: str, text: str, lastUpdate: str, org_aries_common_Note: "User" = None):
        self.id = id
        self.creationDate = creationDate
        self.text = text
        self.lastUpdate = lastUpdate
        self.org_aries_common_Note = org_aries_common_Note
        
    @property
    def creationDate(self) -> str:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: str):
        self.__creationDate = creationDate

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def org_aries_common_Note(self):
        return self.__org_aries_common_Note

    @org_aries_common_Note.setter
    def org_aries_common_Note(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_Note__org_aries_common_Note", None)
        self.__org_aries_common_Note = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User81"):
                opp_val = getattr(old_value, "User81", None)
                if opp_val == self:
                    setattr(old_value, "User81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User81"):
                opp_val = getattr(value, "User81", None)
                setattr(value, "User81", self)

class org_aries_common_Person:

    def __init__(self, id: str, userId: str, org_aries_common_Person: "PersonName" = None, org_aries_common_Person85: "PhoneNumber" = None, org_aries_common_Person88: "EmailAddress" = None, org_aries_common_Person91: "StreetAddress" = None):
        self.id = id
        self.userId = userId
        self.org_aries_common_Person = org_aries_common_Person
        self.org_aries_common_Person85 = org_aries_common_Person85
        self.org_aries_common_Person88 = org_aries_common_Person88
        self.org_aries_common_Person91 = org_aries_common_Person91
        
    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def org_aries_common_Person91(self):
        return self.__org_aries_common_Person91

    @org_aries_common_Person91.setter
    def org_aries_common_Person91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_Person__org_aries_common_Person91", None)
        self.__org_aries_common_Person91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StreetAddress92"):
                opp_val = getattr(old_value, "StreetAddress92", None)
                if opp_val == self:
                    setattr(old_value, "StreetAddress92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StreetAddress92"):
                opp_val = getattr(value, "StreetAddress92", None)
                setattr(value, "StreetAddress92", self)

    @property
    def org_aries_common_Person85(self):
        return self.__org_aries_common_Person85

    @org_aries_common_Person85.setter
    def org_aries_common_Person85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_Person__org_aries_common_Person85", None)
        self.__org_aries_common_Person85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhoneNumber86"):
                opp_val = getattr(old_value, "PhoneNumber86", None)
                if opp_val == self:
                    setattr(old_value, "PhoneNumber86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhoneNumber86"):
                opp_val = getattr(value, "PhoneNumber86", None)
                setattr(value, "PhoneNumber86", self)

    @property
    def org_aries_common_Person88(self):
        return self.__org_aries_common_Person88

    @org_aries_common_Person88.setter
    def org_aries_common_Person88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_Person__org_aries_common_Person88", None)
        self.__org_aries_common_Person88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmailAddress89"):
                opp_val = getattr(old_value, "EmailAddress89", None)
                if opp_val == self:
                    setattr(old_value, "EmailAddress89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmailAddress89"):
                opp_val = getattr(value, "EmailAddress89", None)
                setattr(value, "EmailAddress89", self)

    @property
    def org_aries_common_Person(self):
        return self.__org_aries_common_Person

    @org_aries_common_Person.setter
    def org_aries_common_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_Person__org_aries_common_Person", None)
        self.__org_aries_common_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PersonName83"):
                opp_val = getattr(old_value, "PersonName83", None)
                if opp_val == self:
                    setattr(old_value, "PersonName83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PersonName83"):
                opp_val = getattr(value, "PersonName83", None)
                setattr(value, "PersonName83", self)

class org_aries_common_MapEntry:

    pass
class org_aries_common_EObject:

    pass
class org_aries_common_Map:

    pass
class org_aries_common_Event:

    def __init__(self, id: str, org_aries_common_Event: "User" = None):
        self.id = id
        self.org_aries_common_Event = org_aries_common_Event
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def org_aries_common_Event(self):
        return self.__org_aries_common_Event

    @org_aries_common_Event.setter
    def org_aries_common_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_Event__org_aries_common_Event", None)
        self.__org_aries_common_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User73"):
                opp_val = getattr(old_value, "User73", None)
                if opp_val == self:
                    setattr(old_value, "User73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User73"):
                opp_val = getattr(value, "User73", None)
                setattr(value, "User73", self)

class org_aries_common_EmailMessage:

    def __init__(self, id: str, content: str, subject: str, timestamp: str, smtpPort: str, sourceId: str, smtpHost: str, sendAsHtml: str, org_aries_common_EmailMessage: "EmailAddress" = None, org_aries_common_EmailMessage55: set["EmailAddressList"] = None, org_aries_common_EmailMessage58: set["EmailAddressList"] = None, org_aries_common_EmailMessage61: set["EmailAddressList"] = None, org_aries_common_EmailMessage67: set["EmailAddressList"] = None, org_aries_common_EmailMessage70: set["Attachment"] = None, org_aries_common_EmailMessage64: set["EmailAddressList"] = None):
        self.id = id
        self.content = content
        self.subject = subject
        self.timestamp = timestamp
        self.smtpPort = smtpPort
        self.sourceId = sourceId
        self.smtpHost = smtpHost
        self.sendAsHtml = sendAsHtml
        self.org_aries_common_EmailMessage = org_aries_common_EmailMessage
        self.org_aries_common_EmailMessage55 = org_aries_common_EmailMessage55 if org_aries_common_EmailMessage55 is not None else set()
        self.org_aries_common_EmailMessage58 = org_aries_common_EmailMessage58 if org_aries_common_EmailMessage58 is not None else set()
        self.org_aries_common_EmailMessage61 = org_aries_common_EmailMessage61 if org_aries_common_EmailMessage61 is not None else set()
        self.org_aries_common_EmailMessage67 = org_aries_common_EmailMessage67 if org_aries_common_EmailMessage67 is not None else set()
        self.org_aries_common_EmailMessage70 = org_aries_common_EmailMessage70 if org_aries_common_EmailMessage70 is not None else set()
        self.org_aries_common_EmailMessage64 = org_aries_common_EmailMessage64 if org_aries_common_EmailMessage64 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def sendAsHtml(self) -> str:
        return self.__sendAsHtml

    @sendAsHtml.setter
    def sendAsHtml(self, sendAsHtml: str):
        self.__sendAsHtml = sendAsHtml

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def smtpPort(self) -> str:
        return self.__smtpPort

    @smtpPort.setter
    def smtpPort(self, smtpPort: str):
        self.__smtpPort = smtpPort

    @property
    def sourceId(self) -> str:
        return self.__sourceId

    @sourceId.setter
    def sourceId(self, sourceId: str):
        self.__sourceId = sourceId

    @property
    def smtpHost(self) -> str:
        return self.__smtpHost

    @smtpHost.setter
    def smtpHost(self, smtpHost: str):
        self.__smtpHost = smtpHost

    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

    @property
    def org_aries_common_EmailMessage58(self):
        return self.__org_aries_common_EmailMessage58

    @org_aries_common_EmailMessage58.setter
    def org_aries_common_EmailMessage58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_EmailMessage__org_aries_common_EmailMessage58", None)
        self.__org_aries_common_EmailMessage58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailAddressList59"):
                    opp_val = getattr(item, "EmailAddressList59", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailAddressList59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailAddressList59"):
                    opp_val = getattr(item, "EmailAddressList59", None)
                    
                    setattr(item, "EmailAddressList59", self)
                    

    @property
    def org_aries_common_EmailMessage55(self):
        return self.__org_aries_common_EmailMessage55

    @org_aries_common_EmailMessage55.setter
    def org_aries_common_EmailMessage55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_EmailMessage__org_aries_common_EmailMessage55", None)
        self.__org_aries_common_EmailMessage55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailAddressList56"):
                    opp_val = getattr(item, "EmailAddressList56", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailAddressList56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailAddressList56"):
                    opp_val = getattr(item, "EmailAddressList56", None)
                    
                    setattr(item, "EmailAddressList56", self)
                    

    @property
    def org_aries_common_EmailMessage61(self):
        return self.__org_aries_common_EmailMessage61

    @org_aries_common_EmailMessage61.setter
    def org_aries_common_EmailMessage61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_EmailMessage__org_aries_common_EmailMessage61", None)
        self.__org_aries_common_EmailMessage61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailAddressList62"):
                    opp_val = getattr(item, "EmailAddressList62", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailAddressList62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailAddressList62"):
                    opp_val = getattr(item, "EmailAddressList62", None)
                    
                    setattr(item, "EmailAddressList62", self)
                    

    @property
    def org_aries_common_EmailMessage64(self):
        return self.__org_aries_common_EmailMessage64

    @org_aries_common_EmailMessage64.setter
    def org_aries_common_EmailMessage64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_EmailMessage__org_aries_common_EmailMessage64", None)
        self.__org_aries_common_EmailMessage64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailAddressList65"):
                    opp_val = getattr(item, "EmailAddressList65", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailAddressList65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailAddressList65"):
                    opp_val = getattr(item, "EmailAddressList65", None)
                    
                    setattr(item, "EmailAddressList65", self)
                    

    @property
    def org_aries_common_EmailMessage70(self):
        return self.__org_aries_common_EmailMessage70

    @org_aries_common_EmailMessage70.setter
    def org_aries_common_EmailMessage70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_EmailMessage__org_aries_common_EmailMessage70", None)
        self.__org_aries_common_EmailMessage70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attachment71"):
                    opp_val = getattr(item, "Attachment71", None)
                    
                    if opp_val == self:
                        setattr(item, "Attachment71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attachment71"):
                    opp_val = getattr(item, "Attachment71", None)
                    
                    setattr(item, "Attachment71", self)
                    

    @property
    def org_aries_common_EmailMessage67(self):
        return self.__org_aries_common_EmailMessage67

    @org_aries_common_EmailMessage67.setter
    def org_aries_common_EmailMessage67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_EmailMessage__org_aries_common_EmailMessage67", None)
        self.__org_aries_common_EmailMessage67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailAddressList68"):
                    opp_val = getattr(item, "EmailAddressList68", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailAddressList68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailAddressList68"):
                    opp_val = getattr(item, "EmailAddressList68", None)
                    
                    setattr(item, "EmailAddressList68", self)
                    

    @property
    def org_aries_common_EmailMessage(self):
        return self.__org_aries_common_EmailMessage

    @org_aries_common_EmailMessage.setter
    def org_aries_common_EmailMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_EmailMessage__org_aries_common_EmailMessage", None)
        self.__org_aries_common_EmailMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmailAddress53"):
                opp_val = getattr(old_value, "EmailAddress53", None)
                if opp_val == self:
                    setattr(old_value, "EmailAddress53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmailAddress53"):
                opp_val = getattr(value, "EmailAddress53", None)
                setattr(value, "EmailAddress53", self)

class org_aries_common_EmailBox:

    def __init__(self, id: str, type: str, name: str, lastUpdate: str, creationDate: str, org_aries_common_EmailBox: "EmailAccount" = None, org_aries_common_EmailBox47: "EmailBox" = None, org_aries_common_EmailBox50: set["EmailMessage"] = None):
        self.id = id
        self.type = type
        self.name = name
        self.lastUpdate = lastUpdate
        self.creationDate = creationDate
        self.org_aries_common_EmailBox = org_aries_common_EmailBox
        self.org_aries_common_EmailBox47 = org_aries_common_EmailBox47
        self.org_aries_common_EmailBox50 = org_aries_common_EmailBox50 if org_aries_common_EmailBox50 is not None else set()
        
    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def creationDate(self) -> str:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: str):
        self.__creationDate = creationDate

    @property
    def org_aries_common_EmailBox(self):
        return self.__org_aries_common_EmailBox

    @org_aries_common_EmailBox.setter
    def org_aries_common_EmailBox(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_EmailBox__org_aries_common_EmailBox", None)
        self.__org_aries_common_EmailBox = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmailAccount45"):
                opp_val = getattr(old_value, "EmailAccount45", None)
                if opp_val == self:
                    setattr(old_value, "EmailAccount45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmailAccount45"):
                opp_val = getattr(value, "EmailAccount45", None)
                setattr(value, "EmailAccount45", self)

    @property
    def org_aries_common_EmailBox47(self):
        return self.__org_aries_common_EmailBox47

    @org_aries_common_EmailBox47.setter
    def org_aries_common_EmailBox47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_EmailBox__org_aries_common_EmailBox47", None)
        self.__org_aries_common_EmailBox47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmailBox48"):
                opp_val = getattr(old_value, "EmailBox48", None)
                if opp_val == self:
                    setattr(old_value, "EmailBox48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmailBox48"):
                opp_val = getattr(value, "EmailBox48", None)
                setattr(value, "EmailBox48", self)

    @property
    def org_aries_common_EmailBox50(self):
        return self.__org_aries_common_EmailBox50

    @org_aries_common_EmailBox50.setter
    def org_aries_common_EmailBox50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_EmailBox__org_aries_common_EmailBox50", None)
        self.__org_aries_common_EmailBox50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailMessage51"):
                    opp_val = getattr(item, "EmailMessage51", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailMessage51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailMessage51"):
                    opp_val = getattr(item, "EmailMessage51", None)
                    
                    setattr(item, "EmailMessage51", self)
                    

class org_aries_common_EmailAddressList:

    def __init__(self, name: str, emailAddress: str):
        self.name = name
        self.emailAddress = emailAddress
        
    @property
    def emailAddress(self) -> str:
        return self.__emailAddress

    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class org_aries_common_EmailAddress:

    def __init__(self, id: str, url: str, userId: str, firstName: str, lastName: str, organization: str, creationDate: str, lastUpdate: str, enabled: str, org_aries_common_EmailAddress: "PhoneNumber" = None):
        self.id = id
        self.url = url
        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.organization = organization
        self.creationDate = creationDate
        self.lastUpdate = lastUpdate
        self.enabled = enabled
        self.org_aries_common_EmailAddress = org_aries_common_EmailAddress
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def lastUpdate(self) -> str:
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, lastUpdate: str):
        self.__lastUpdate = lastUpdate

    @property
    def enabled(self) -> str:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: str):
        self.__enabled = enabled

    @property
    def creationDate(self) -> str:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: str):
        self.__creationDate = creationDate

    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def org_aries_common_EmailAddress(self):
        return self.__org_aries_common_EmailAddress

    @org_aries_common_EmailAddress.setter
    def org_aries_common_EmailAddress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_EmailAddress__org_aries_common_EmailAddress", None)
        self.__org_aries_common_EmailAddress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhoneNumber43"):
                opp_val = getattr(old_value, "PhoneNumber43", None)
                if opp_val == self:
                    setattr(old_value, "PhoneNumber43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhoneNumber43"):
                opp_val = getattr(value, "PhoneNumber43", None)
                setattr(value, "PhoneNumber43", self)

class ZipCode:

    pass
class org_aries_common_EmailAccount:

    def __init__(self, id: str, userId: str, password: str, firstName: str, lastName: str, enabled: str, org_aries_common_EmailAccount: set["EmailBox"] = None):
        self.id = id
        self.userId = userId
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.enabled = enabled
        self.org_aries_common_EmailAccount = org_aries_common_EmailAccount if org_aries_common_EmailAccount is not None else set()
        
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def enabled(self) -> str:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: str):
        self.__enabled = enabled

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def org_aries_common_EmailAccount(self):
        return self.__org_aries_common_EmailAccount

    @org_aries_common_EmailAccount.setter
    def org_aries_common_EmailAccount(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_EmailAccount__org_aries_common_EmailAccount", None)
        self.__org_aries_common_EmailAccount = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailBox41"):
                    opp_val = getattr(item, "EmailBox41", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailBox41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailBox41"):
                    opp_val = getattr(item, "EmailBox41", None)
                    
                    setattr(item, "EmailBox41", self)
                    

class PhoneNumber:

    pass
class User:

    pass
class StreetAddress:

    pass
class Property:

    pass
class Properties:

    pass
class MapEntry:

    pass
class PersonName:

    pass
class Person:

    pass
class Note:

    pass
class EmailAddressList:

    pass
class Map:

    pass
class Event:

    pass
class EmailMessage:

    pass
class EmailBox:

    pass
class org_aries_common_EStringToStringMapEntry:

    pass
class EmailAddress:

    pass
class EmailAccount:

    pass
class Attachment:

    pass
class org_aries_common_DocumentRoot:

    def __init__(self, mixed: str, org_aries_common_DocumentRoot: set["org_aries_common_EStringToStringMapEntry"] = None, org_aries_common_DocumentRoot2: set["org_aries_common_EStringToStringMapEntry"] = None, org_aries_common_DocumentRoot5: set["Attachment"] = None, org_aries_common_DocumentRoot7: set["EmailAccount"] = None, org_aries_common_DocumentRoot9: set["EmailAddress"] = None, org_aries_common_DocumentRoot13: set["EmailBox"] = None, org_aries_common_DocumentRoot15: set["EmailMessage"] = None, org_aries_common_DocumentRoot17: set["Event"] = None, org_aries_common_DocumentRoot19: set["Map"] = None, org_aries_common_DocumentRoot11: set["EmailAddressList"] = None, org_aries_common_DocumentRoot23: set["Note"] = None, org_aries_common_DocumentRoot25: set["Person"] = None, org_aries_common_DocumentRoot27: set["PersonName"] = None, org_aries_common_DocumentRoot21: set["MapEntry"] = None, org_aries_common_DocumentRoot31: set["Properties"] = None, org_aries_common_DocumentRoot33: set["Property"] = None, org_aries_common_DocumentRoot35: set["StreetAddress"] = None, org_aries_common_DocumentRoot37: set["User"] = None, org_aries_common_DocumentRoot29: set["PhoneNumber"] = None, org_aries_common_DocumentRoot39: set["ZipCode"] = None):
        self.mixed = mixed
        self.org_aries_common_DocumentRoot = org_aries_common_DocumentRoot if org_aries_common_DocumentRoot is not None else set()
        self.org_aries_common_DocumentRoot2 = org_aries_common_DocumentRoot2 if org_aries_common_DocumentRoot2 is not None else set()
        self.org_aries_common_DocumentRoot5 = org_aries_common_DocumentRoot5 if org_aries_common_DocumentRoot5 is not None else set()
        self.org_aries_common_DocumentRoot7 = org_aries_common_DocumentRoot7 if org_aries_common_DocumentRoot7 is not None else set()
        self.org_aries_common_DocumentRoot9 = org_aries_common_DocumentRoot9 if org_aries_common_DocumentRoot9 is not None else set()
        self.org_aries_common_DocumentRoot13 = org_aries_common_DocumentRoot13 if org_aries_common_DocumentRoot13 is not None else set()
        self.org_aries_common_DocumentRoot15 = org_aries_common_DocumentRoot15 if org_aries_common_DocumentRoot15 is not None else set()
        self.org_aries_common_DocumentRoot17 = org_aries_common_DocumentRoot17 if org_aries_common_DocumentRoot17 is not None else set()
        self.org_aries_common_DocumentRoot19 = org_aries_common_DocumentRoot19 if org_aries_common_DocumentRoot19 is not None else set()
        self.org_aries_common_DocumentRoot11 = org_aries_common_DocumentRoot11 if org_aries_common_DocumentRoot11 is not None else set()
        self.org_aries_common_DocumentRoot23 = org_aries_common_DocumentRoot23 if org_aries_common_DocumentRoot23 is not None else set()
        self.org_aries_common_DocumentRoot25 = org_aries_common_DocumentRoot25 if org_aries_common_DocumentRoot25 is not None else set()
        self.org_aries_common_DocumentRoot27 = org_aries_common_DocumentRoot27 if org_aries_common_DocumentRoot27 is not None else set()
        self.org_aries_common_DocumentRoot21 = org_aries_common_DocumentRoot21 if org_aries_common_DocumentRoot21 is not None else set()
        self.org_aries_common_DocumentRoot31 = org_aries_common_DocumentRoot31 if org_aries_common_DocumentRoot31 is not None else set()
        self.org_aries_common_DocumentRoot33 = org_aries_common_DocumentRoot33 if org_aries_common_DocumentRoot33 is not None else set()
        self.org_aries_common_DocumentRoot35 = org_aries_common_DocumentRoot35 if org_aries_common_DocumentRoot35 is not None else set()
        self.org_aries_common_DocumentRoot37 = org_aries_common_DocumentRoot37 if org_aries_common_DocumentRoot37 is not None else set()
        self.org_aries_common_DocumentRoot29 = org_aries_common_DocumentRoot29 if org_aries_common_DocumentRoot29 is not None else set()
        self.org_aries_common_DocumentRoot39 = org_aries_common_DocumentRoot39 if org_aries_common_DocumentRoot39 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def org_aries_common_DocumentRoot17(self):
        return self.__org_aries_common_DocumentRoot17

    @org_aries_common_DocumentRoot17.setter
    def org_aries_common_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot17", None)
        self.__org_aries_common_DocumentRoot17 = value if value is not None else set()
        
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
    def org_aries_common_DocumentRoot9(self):
        return self.__org_aries_common_DocumentRoot9

    @org_aries_common_DocumentRoot9.setter
    def org_aries_common_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot9", None)
        self.__org_aries_common_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailAddress"):
                    opp_val = getattr(item, "EmailAddress", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailAddress", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailAddress"):
                    opp_val = getattr(item, "EmailAddress", None)
                    
                    setattr(item, "EmailAddress", self)
                    

    @property
    def org_aries_common_DocumentRoot37(self):
        return self.__org_aries_common_DocumentRoot37

    @org_aries_common_DocumentRoot37.setter
    def org_aries_common_DocumentRoot37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot37", None)
        self.__org_aries_common_DocumentRoot37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User"):
                    opp_val = getattr(item, "User", None)
                    
                    if opp_val == self:
                        setattr(item, "User", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User"):
                    opp_val = getattr(item, "User", None)
                    
                    setattr(item, "User", self)
                    

    @property
    def org_aries_common_DocumentRoot7(self):
        return self.__org_aries_common_DocumentRoot7

    @org_aries_common_DocumentRoot7.setter
    def org_aries_common_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot7", None)
        self.__org_aries_common_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailAccount"):
                    opp_val = getattr(item, "EmailAccount", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailAccount", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailAccount"):
                    opp_val = getattr(item, "EmailAccount", None)
                    
                    setattr(item, "EmailAccount", self)
                    

    @property
    def org_aries_common_DocumentRoot33(self):
        return self.__org_aries_common_DocumentRoot33

    @org_aries_common_DocumentRoot33.setter
    def org_aries_common_DocumentRoot33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot33", None)
        self.__org_aries_common_DocumentRoot33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

    @property
    def org_aries_common_DocumentRoot35(self):
        return self.__org_aries_common_DocumentRoot35

    @org_aries_common_DocumentRoot35.setter
    def org_aries_common_DocumentRoot35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot35", None)
        self.__org_aries_common_DocumentRoot35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StreetAddress"):
                    opp_val = getattr(item, "StreetAddress", None)
                    
                    if opp_val == self:
                        setattr(item, "StreetAddress", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StreetAddress"):
                    opp_val = getattr(item, "StreetAddress", None)
                    
                    setattr(item, "StreetAddress", self)
                    

    @property
    def org_aries_common_DocumentRoot29(self):
        return self.__org_aries_common_DocumentRoot29

    @org_aries_common_DocumentRoot29.setter
    def org_aries_common_DocumentRoot29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot29", None)
        self.__org_aries_common_DocumentRoot29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhoneNumber"):
                    opp_val = getattr(item, "PhoneNumber", None)
                    
                    if opp_val == self:
                        setattr(item, "PhoneNumber", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhoneNumber"):
                    opp_val = getattr(item, "PhoneNumber", None)
                    
                    setattr(item, "PhoneNumber", self)
                    

    @property
    def org_aries_common_DocumentRoot39(self):
        return self.__org_aries_common_DocumentRoot39

    @org_aries_common_DocumentRoot39.setter
    def org_aries_common_DocumentRoot39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot39", None)
        self.__org_aries_common_DocumentRoot39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ZipCode"):
                    opp_val = getattr(item, "ZipCode", None)
                    
                    if opp_val == self:
                        setattr(item, "ZipCode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ZipCode"):
                    opp_val = getattr(item, "ZipCode", None)
                    
                    setattr(item, "ZipCode", self)
                    

    @property
    def org_aries_common_DocumentRoot13(self):
        return self.__org_aries_common_DocumentRoot13

    @org_aries_common_DocumentRoot13.setter
    def org_aries_common_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot13", None)
        self.__org_aries_common_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailBox"):
                    opp_val = getattr(item, "EmailBox", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailBox", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailBox"):
                    opp_val = getattr(item, "EmailBox", None)
                    
                    setattr(item, "EmailBox", self)
                    

    @property
    def org_aries_common_DocumentRoot31(self):
        return self.__org_aries_common_DocumentRoot31

    @org_aries_common_DocumentRoot31.setter
    def org_aries_common_DocumentRoot31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot31", None)
        self.__org_aries_common_DocumentRoot31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Properties"):
                    opp_val = getattr(item, "Properties", None)
                    
                    if opp_val == self:
                        setattr(item, "Properties", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Properties"):
                    opp_val = getattr(item, "Properties", None)
                    
                    setattr(item, "Properties", self)
                    

    @property
    def org_aries_common_DocumentRoot15(self):
        return self.__org_aries_common_DocumentRoot15

    @org_aries_common_DocumentRoot15.setter
    def org_aries_common_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot15", None)
        self.__org_aries_common_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailMessage"):
                    opp_val = getattr(item, "EmailMessage", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailMessage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailMessage"):
                    opp_val = getattr(item, "EmailMessage", None)
                    
                    setattr(item, "EmailMessage", self)
                    

    @property
    def org_aries_common_DocumentRoot25(self):
        return self.__org_aries_common_DocumentRoot25

    @org_aries_common_DocumentRoot25.setter
    def org_aries_common_DocumentRoot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot25", None)
        self.__org_aries_common_DocumentRoot25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def org_aries_common_DocumentRoot23(self):
        return self.__org_aries_common_DocumentRoot23

    @org_aries_common_DocumentRoot23.setter
    def org_aries_common_DocumentRoot23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot23", None)
        self.__org_aries_common_DocumentRoot23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Note"):
                    opp_val = getattr(item, "Note", None)
                    
                    if opp_val == self:
                        setattr(item, "Note", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Note"):
                    opp_val = getattr(item, "Note", None)
                    
                    setattr(item, "Note", self)
                    

    @property
    def org_aries_common_DocumentRoot27(self):
        return self.__org_aries_common_DocumentRoot27

    @org_aries_common_DocumentRoot27.setter
    def org_aries_common_DocumentRoot27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot27", None)
        self.__org_aries_common_DocumentRoot27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PersonName"):
                    opp_val = getattr(item, "PersonName", None)
                    
                    if opp_val == self:
                        setattr(item, "PersonName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PersonName"):
                    opp_val = getattr(item, "PersonName", None)
                    
                    setattr(item, "PersonName", self)
                    

    @property
    def org_aries_common_DocumentRoot(self):
        return self.__org_aries_common_DocumentRoot

    @org_aries_common_DocumentRoot.setter
    def org_aries_common_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot", None)
        self.__org_aries_common_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "org_aries_common_EStringToStringMapEntry"):
                    opp_val = getattr(item, "org_aries_common_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "org_aries_common_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "org_aries_common_EStringToStringMapEntry"):
                    opp_val = getattr(item, "org_aries_common_EStringToStringMapEntry", None)
                    
                    setattr(item, "org_aries_common_EStringToStringMapEntry", self)
                    

    @property
    def org_aries_common_DocumentRoot2(self):
        return self.__org_aries_common_DocumentRoot2

    @org_aries_common_DocumentRoot2.setter
    def org_aries_common_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot2", None)
        self.__org_aries_common_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "org_aries_common_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "org_aries_common_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "org_aries_common_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "org_aries_common_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "org_aries_common_EStringToStringMapEntry3", None)
                    
                    setattr(item, "org_aries_common_EStringToStringMapEntry3", self)
                    

    @property
    def org_aries_common_DocumentRoot5(self):
        return self.__org_aries_common_DocumentRoot5

    @org_aries_common_DocumentRoot5.setter
    def org_aries_common_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot5", None)
        self.__org_aries_common_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attachment"):
                    opp_val = getattr(item, "Attachment", None)
                    
                    if opp_val == self:
                        setattr(item, "Attachment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attachment"):
                    opp_val = getattr(item, "Attachment", None)
                    
                    setattr(item, "Attachment", self)
                    

    @property
    def org_aries_common_DocumentRoot11(self):
        return self.__org_aries_common_DocumentRoot11

    @org_aries_common_DocumentRoot11.setter
    def org_aries_common_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot11", None)
        self.__org_aries_common_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmailAddressList"):
                    opp_val = getattr(item, "EmailAddressList", None)
                    
                    if opp_val == self:
                        setattr(item, "EmailAddressList", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmailAddressList"):
                    opp_val = getattr(item, "EmailAddressList", None)
                    
                    setattr(item, "EmailAddressList", self)
                    

    @property
    def org_aries_common_DocumentRoot19(self):
        return self.__org_aries_common_DocumentRoot19

    @org_aries_common_DocumentRoot19.setter
    def org_aries_common_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot19", None)
        self.__org_aries_common_DocumentRoot19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Map"):
                    opp_val = getattr(item, "Map", None)
                    
                    if opp_val == self:
                        setattr(item, "Map", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Map"):
                    opp_val = getattr(item, "Map", None)
                    
                    setattr(item, "Map", self)
                    

    @property
    def org_aries_common_DocumentRoot21(self):
        return self.__org_aries_common_DocumentRoot21

    @org_aries_common_DocumentRoot21.setter
    def org_aries_common_DocumentRoot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_aries_common_DocumentRoot__org_aries_common_DocumentRoot21", None)
        self.__org_aries_common_DocumentRoot21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MapEntry"):
                    opp_val = getattr(item, "MapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "MapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MapEntry"):
                    opp_val = getattr(item, "MapEntry", None)
                    
                    setattr(item, "MapEntry", self)
                    

class org_aries_common_Attachment:

    def __init__(self, id: str, name: str, size: str, fileName: str, fileData: str, contentType: str):
        self.id = id
        self.name = name
        self.size = size
        self.fileName = fileName
        self.fileData = fileData
        self.contentType = contentType
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fileData(self) -> str:
        return self.__fileData

    @fileData.setter
    def fileData(self, fileData: str):
        self.__fileData = fileData

    @property
    def contentType(self) -> str:
        return self.__contentType

    @contentType.setter
    def contentType(self, contentType: str):
        self.__contentType = contentType

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName
