from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OrgType(Enum):
    department = "department"
    school = "school"
    major = "major"
    Misc = "Misc"
    Discipline = "Discipline"
    Specjalization = "Specjalization"
class Role(Enum):
    student = "student"
    teacher = "teacher"


############################################
# Definition of Classes
############################################

class Org:

    pass
class dXP_OrgUnit(Org):

    pass
class dXP_UserId:

    def __init__(self, type: str, identifier: str, dXP_UserId: "dXP_User" = None):
        self.type = type
        self.identifier = identifier
        self.dXP_UserId = dXP_UserId
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dXP_UserId(self):
        return self.__dXP_UserId

    @dXP_UserId.setter
    def dXP_UserId(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_UserId__dXP_UserId", None)
        self.__dXP_UserId = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_User13"):
                opp_val = getattr(old_value, "dXP_User13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_User13"):
                opp_val = getattr(value, "dXP_User13", None)
                if opp_val is None:
                    setattr(value, "dXP_User13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dXP_Metadata:

    def __init__(self, key: str, value: str, dXP_Metadata: "dXP_Base" = None):
        self.key = key
        self.value = value
        self.dXP_Metadata = dXP_Metadata
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def dXP_Metadata(self):
        return self.__dXP_Metadata

    @dXP_Metadata.setter
    def dXP_Metadata(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_Metadata__dXP_Metadata", None)
        self.__dXP_Metadata = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_Base"):
                opp_val = getattr(old_value, "dXP_Base", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_Base"):
                opp_val = getattr(value, "dXP_Base", None)
                if opp_val is None:
                    setattr(value, "dXP_Base", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dXP_Base(ABC):

    def __init__(self, sourceId: str, status: str, dateLastModified: str, dXP_Base: set["dXP_Metadata"] = None):
        self.sourceId = sourceId
        self.status = status
        self.dateLastModified = dateLastModified
        self.dXP_Base = dXP_Base if dXP_Base is not None else set()
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def dateLastModified(self) -> str:
        return self.__dateLastModified

    @dateLastModified.setter
    def dateLastModified(self, dateLastModified: str):
        self.__dateLastModified = dateLastModified

    @property
    def sourceId(self) -> str:
        return self.__sourceId

    @sourceId.setter
    def sourceId(self, sourceId: str):
        self.__sourceId = sourceId

    @property
    def dXP_Base(self):
        return self.__dXP_Base

    @dXP_Base.setter
    def dXP_Base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_Base__dXP_Base", None)
        self.__dXP_Base = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dXP_Metadata"):
                    opp_val = getattr(item, "dXP_Metadata", None)
                    
                    if opp_val == self:
                        setattr(item, "dXP_Metadata", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dXP_Metadata"):
                    opp_val = getattr(item, "dXP_Metadata", None)
                    
                    setattr(item, "dXP_Metadata", self)
                    

class Base:

    pass
class dXP_Class(Base):

    def __init__(self, title: str, classCode: str, classType: str, location: str, dXP_Class: "dXP_Course" = None, dXP_Class21: "dXP_Enrolment" = None):
        self.title = title
        self.classCode = classCode
        self.classType = classType
        self.location = location
        self.dXP_Class = dXP_Class
        self.dXP_Class21 = dXP_Class21
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def classType(self) -> str:
        return self.__classType

    @classType.setter
    def classType(self, classType: str):
        self.__classType = classType

    @property
    def classCode(self) -> str:
        return self.__classCode

    @classCode.setter
    def classCode(self, classCode: str):
        self.__classCode = classCode

    @property
    def dXP_Class21(self):
        return self.__dXP_Class21

    @dXP_Class21.setter
    def dXP_Class21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_Class__dXP_Class21", None)
        self.__dXP_Class21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_Enrolment20"):
                opp_val = getattr(old_value, "dXP_Enrolment20", None)
                if opp_val == self:
                    setattr(old_value, "dXP_Enrolment20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_Enrolment20"):
                opp_val = getattr(value, "dXP_Enrolment20", None)
                setattr(value, "dXP_Enrolment20", self)

    @property
    def dXP_Class(self):
        return self.__dXP_Class

    @dXP_Class.setter
    def dXP_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_Class__dXP_Class", None)
        self.__dXP_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_Course"):
                opp_val = getattr(old_value, "dXP_Course", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_Course"):
                opp_val = getattr(value, "dXP_Course", None)
                if opp_val is None:
                    setattr(value, "dXP_Course", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dXP_User(Base):

    def __init__(self, userName: str, enabledUser: str, role: str, identifier: str, dXP_User: "dXP_AcademicSession" = None, dXP_User13: set["dXP_UserId"] = None, dXP_User18: "dXP_Enrolment" = None):
        self.userName = userName
        self.enabledUser = enabledUser
        self.role = role
        self.identifier = identifier
        self.dXP_User = dXP_User
        self.dXP_User13 = dXP_User13 if dXP_User13 is not None else set()
        self.dXP_User18 = dXP_User18
        
    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def userName(self) -> str:
        return self.__userName

    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def enabledUser(self) -> str:
        return self.__enabledUser

    @enabledUser.setter
    def enabledUser(self, enabledUser: str):
        self.__enabledUser = enabledUser

    @property
    def dXP_User13(self):
        return self.__dXP_User13

    @dXP_User13.setter
    def dXP_User13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_User__dXP_User13", None)
        self.__dXP_User13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dXP_UserId"):
                    opp_val = getattr(item, "dXP_UserId", None)
                    
                    if opp_val == self:
                        setattr(item, "dXP_UserId", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dXP_UserId"):
                    opp_val = getattr(item, "dXP_UserId", None)
                    
                    setattr(item, "dXP_UserId", self)
                    

    @property
    def dXP_User(self):
        return self.__dXP_User

    @dXP_User.setter
    def dXP_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_User__dXP_User", None)
        self.__dXP_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_AcademicSession11"):
                opp_val = getattr(old_value, "dXP_AcademicSession11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_AcademicSession11"):
                opp_val = getattr(value, "dXP_AcademicSession11", None)
                if opp_val is None:
                    setattr(value, "dXP_AcademicSession11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dXP_User18(self):
        return self.__dXP_User18

    @dXP_User18.setter
    def dXP_User18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_User__dXP_User18", None)
        self.__dXP_User18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_Enrolment17"):
                opp_val = getattr(old_value, "dXP_Enrolment17", None)
                if opp_val == self:
                    setattr(old_value, "dXP_Enrolment17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_Enrolment17"):
                opp_val = getattr(value, "dXP_Enrolment17", None)
                setattr(value, "dXP_Enrolment17", self)

class dXP_Course(Base):

    def __init__(self, title: str, courseCode: str, dXP_Course: set["dXP_Class"] = None, dXP_Course9: "dXP_AcademicSession" = None):
        self.title = title
        self.courseCode = courseCode
        self.dXP_Course = dXP_Course if dXP_Course is not None else set()
        self.dXP_Course9 = dXP_Course9
        
    @property
    def courseCode(self) -> str:
        return self.__courseCode

    @courseCode.setter
    def courseCode(self, courseCode: str):
        self.__courseCode = courseCode

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def dXP_Course9(self):
        return self.__dXP_Course9

    @dXP_Course9.setter
    def dXP_Course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_Course__dXP_Course9", None)
        self.__dXP_Course9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_AcademicSession8"):
                opp_val = getattr(old_value, "dXP_AcademicSession8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_AcademicSession8"):
                opp_val = getattr(value, "dXP_AcademicSession8", None)
                if opp_val is None:
                    setattr(value, "dXP_AcademicSession8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dXP_Course(self):
        return self.__dXP_Course

    @dXP_Course.setter
    def dXP_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_Course__dXP_Course", None)
        self.__dXP_Course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dXP_Class"):
                    opp_val = getattr(item, "dXP_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "dXP_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dXP_Class"):
                    opp_val = getattr(item, "dXP_Class", None)
                    
                    setattr(item, "dXP_Class", self)
                    

class dXP_Enrolment(Base):

    def __init__(self, role: str, primary: str, dXP_Enrolment: "dXP_OneRoster" = None, dXP_Enrolment17: "dXP_User" = None, dXP_Enrolment20: "dXP_Class" = None, dXP_Enrolment23: "dXP_OrgUnit" = None):
        self.role = role
        self.primary = primary
        self.dXP_Enrolment = dXP_Enrolment
        self.dXP_Enrolment17 = dXP_Enrolment17
        self.dXP_Enrolment20 = dXP_Enrolment20
        self.dXP_Enrolment23 = dXP_Enrolment23
        
    @property
    def primary(self) -> str:
        return self.__primary

    @primary.setter
    def primary(self, primary: str):
        self.__primary = primary

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def dXP_Enrolment(self):
        return self.__dXP_Enrolment

    @dXP_Enrolment.setter
    def dXP_Enrolment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_Enrolment__dXP_Enrolment", None)
        self.__dXP_Enrolment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_OneRoster4"):
                opp_val = getattr(old_value, "dXP_OneRoster4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_OneRoster4"):
                opp_val = getattr(value, "dXP_OneRoster4", None)
                if opp_val is None:
                    setattr(value, "dXP_OneRoster4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dXP_Enrolment17(self):
        return self.__dXP_Enrolment17

    @dXP_Enrolment17.setter
    def dXP_Enrolment17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_Enrolment__dXP_Enrolment17", None)
        self.__dXP_Enrolment17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_User18"):
                opp_val = getattr(old_value, "dXP_User18", None)
                if opp_val == self:
                    setattr(old_value, "dXP_User18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_User18"):
                opp_val = getattr(value, "dXP_User18", None)
                setattr(value, "dXP_User18", self)

    @property
    def dXP_Enrolment23(self):
        return self.__dXP_Enrolment23

    @dXP_Enrolment23.setter
    def dXP_Enrolment23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_Enrolment__dXP_Enrolment23", None)
        self.__dXP_Enrolment23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_OrgUnit24"):
                opp_val = getattr(old_value, "dXP_OrgUnit24", None)
                if opp_val == self:
                    setattr(old_value, "dXP_OrgUnit24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_OrgUnit24"):
                opp_val = getattr(value, "dXP_OrgUnit24", None)
                setattr(value, "dXP_OrgUnit24", self)

    @property
    def dXP_Enrolment20(self):
        return self.__dXP_Enrolment20

    @dXP_Enrolment20.setter
    def dXP_Enrolment20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_Enrolment__dXP_Enrolment20", None)
        self.__dXP_Enrolment20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_Class21"):
                opp_val = getattr(old_value, "dXP_Class21", None)
                if opp_val == self:
                    setattr(old_value, "dXP_Class21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_Class21"):
                opp_val = getattr(value, "dXP_Class21", None)
                setattr(value, "dXP_Class21", self)

class dXP_Org(Base):

    def __init__(self, name: str, type: str, dXP_Org: "dXP_OneRoster" = None, dXP_Org15: set["dXP_OrgUnit"] = None):
        self.name = name
        self.type = type
        self.dXP_Org = dXP_Org
        self.dXP_Org15 = dXP_Org15 if dXP_Org15 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dXP_Org15(self):
        return self.__dXP_Org15

    @dXP_Org15.setter
    def dXP_Org15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_Org__dXP_Org15", None)
        self.__dXP_Org15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dXP_OrgUnit"):
                    opp_val = getattr(item, "dXP_OrgUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "dXP_OrgUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dXP_OrgUnit"):
                    opp_val = getattr(item, "dXP_OrgUnit", None)
                    
                    setattr(item, "dXP_OrgUnit", self)
                    

    @property
    def dXP_Org(self):
        return self.__dXP_Org

    @dXP_Org.setter
    def dXP_Org(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_Org__dXP_Org", None)
        self.__dXP_Org = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_OneRoster2"):
                opp_val = getattr(old_value, "dXP_OneRoster2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_OneRoster2"):
                opp_val = getattr(value, "dXP_OneRoster2", None)
                if opp_val is None:
                    setattr(value, "dXP_OneRoster2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dXP_AcademicSession(Base):

    def __init__(self, title: str, startDate: str, endDate: str, schoolYear: str, type: str, dXP_AcademicSession: "dXP_OneRoster" = None, dXP_AcademicSession11: set["dXP_User"] = None, dXP_AcademicSession8: set["dXP_Course"] = None):
        self.title = title
        self.startDate = startDate
        self.endDate = endDate
        self.schoolYear = schoolYear
        self.type = type
        self.dXP_AcademicSession = dXP_AcademicSession
        self.dXP_AcademicSession11 = dXP_AcademicSession11 if dXP_AcademicSession11 is not None else set()
        self.dXP_AcademicSession8 = dXP_AcademicSession8 if dXP_AcademicSession8 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def schoolYear(self) -> str:
        return self.__schoolYear

    @schoolYear.setter
    def schoolYear(self, schoolYear: str):
        self.__schoolYear = schoolYear

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def startDate(self) -> str:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate

    @property
    def endDate(self) -> str:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate

    @property
    def dXP_AcademicSession8(self):
        return self.__dXP_AcademicSession8

    @dXP_AcademicSession8.setter
    def dXP_AcademicSession8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_AcademicSession__dXP_AcademicSession8", None)
        self.__dXP_AcademicSession8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dXP_Course9"):
                    opp_val = getattr(item, "dXP_Course9", None)
                    
                    if opp_val == self:
                        setattr(item, "dXP_Course9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dXP_Course9"):
                    opp_val = getattr(item, "dXP_Course9", None)
                    
                    setattr(item, "dXP_Course9", self)
                    

    @property
    def dXP_AcademicSession(self):
        return self.__dXP_AcademicSession

    @dXP_AcademicSession.setter
    def dXP_AcademicSession(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_AcademicSession__dXP_AcademicSession", None)
        self.__dXP_AcademicSession = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dXP_OneRoster"):
                opp_val = getattr(old_value, "dXP_OneRoster", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dXP_OneRoster"):
                opp_val = getattr(value, "dXP_OneRoster", None)
                if opp_val is None:
                    setattr(value, "dXP_OneRoster", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dXP_AcademicSession11(self):
        return self.__dXP_AcademicSession11

    @dXP_AcademicSession11.setter
    def dXP_AcademicSession11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dXP_AcademicSession__dXP_AcademicSession11", None)
        self.__dXP_AcademicSession11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dXP_User"):
                    opp_val = getattr(item, "dXP_User", None)
                    
                    if opp_val == self:
                        setattr(item, "dXP_User", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dXP_User"):
                    opp_val = getattr(item, "dXP_User", None)
                    
                    setattr(item, "dXP_User", self)
                    

class dXP_OneRoster:

    pass