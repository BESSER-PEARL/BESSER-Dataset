from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class IssuePriority(Enum):
    HIGHER = "HIGHER"
    HIGH = "HIGH"
    NORMAL = "NORMAL"
    LOW = "LOW"
    LOWER = "LOWER"
class DependencyType(Enum):
    START_START = "START_START"
    START_END = "START_END"
    END_START = "END_START"
    END_END = "END_END"
class VersionStatus(Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    INPROGRESS = "INPROGRESS"
class IssueStatus(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    ASSIGNED = "ASSIGNED"
    RESOLVED = "RESOLVED"


############################################
# Definition of Classes
############################################

class itm_Issue:

    def __init__(self, status: str, priority: str, dueDate: date, completedDate: date, name: str, description: str, doneRatio: float, estimatedHours: float, elapsedHours: float, itm_Issue16: "itm_Tracker" = None, itm_Issue19: set["itm_IssueDependency"] = None, itm_Issue21: "itm_IssueCategory" = None, itm_Issue24: "itm_Member" = None, itm_Issue27: "itm_Member" = None, itm_Issue: "itm_Version" = None, itm_Issue31: "itm_IssueDependency" = None):
        self.status = status
        self.priority = priority
        self.dueDate = dueDate
        self.completedDate = completedDate
        self.name = name
        self.description = description
        self.doneRatio = doneRatio
        self.estimatedHours = estimatedHours
        self.elapsedHours = elapsedHours
        self.itm_Issue16 = itm_Issue16
        self.itm_Issue19 = itm_Issue19 if itm_Issue19 is not None else set()
        self.itm_Issue21 = itm_Issue21
        self.itm_Issue24 = itm_Issue24
        self.itm_Issue27 = itm_Issue27
        self.itm_Issue = itm_Issue
        self.itm_Issue31 = itm_Issue31
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def estimatedHours(self):
        return self.__estimatedHours

    @estimatedHours.setter
    def estimatedHours(self, estimatedHours: float):
        self.__estimatedHours = estimatedHours


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority


    @property
    def completedDate(self):
        return self.__completedDate

    @completedDate.setter
    def completedDate(self, completedDate: date):
        self.__completedDate = completedDate


    @property
    def dueDate(self):
        return self.__dueDate

    @dueDate.setter
    def dueDate(self, dueDate: date):
        self.__dueDate = dueDate


    @property
    def elapsedHours(self):
        return self.__elapsedHours

    @elapsedHours.setter
    def elapsedHours(self, elapsedHours: float):
        self.__elapsedHours = elapsedHours


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def doneRatio(self):
        return self.__doneRatio

    @doneRatio.setter
    def doneRatio(self, doneRatio: float):
        self.__doneRatio = doneRatio


    @property
    def itm_Issue(self):
        return self.__itm_Issue

    @itm_Issue.setter
    def itm_Issue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Issue__itm_Issue", None)
        self.__itm_Issue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_Version14"):
                opp_val = getattr(old_value, "itm_Version14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_Version14"):
                opp_val = getattr(value, "itm_Version14", None)
                if opp_val is None:
                    setattr(value, "itm_Version14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def itm_Issue21(self):
        return self.__itm_Issue21

    @itm_Issue21.setter
    def itm_Issue21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Issue__itm_Issue21", None)
        self.__itm_Issue21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_IssueCategory22"):
                opp_val = getattr(old_value, "itm_IssueCategory22", None)
                if opp_val == self:
                    setattr(old_value, "itm_IssueCategory22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_IssueCategory22"):
                opp_val = getattr(value, "itm_IssueCategory22", None)
                setattr(value, "itm_IssueCategory22", self)

    @property
    def itm_Issue24(self):
        return self.__itm_Issue24

    @itm_Issue24.setter
    def itm_Issue24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Issue__itm_Issue24", None)
        self.__itm_Issue24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_Member25"):
                opp_val = getattr(old_value, "itm_Member25", None)
                if opp_val == self:
                    setattr(old_value, "itm_Member25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_Member25"):
                opp_val = getattr(value, "itm_Member25", None)
                setattr(value, "itm_Member25", self)

    @property
    def itm_Issue19(self):
        return self.__itm_Issue19

    @itm_Issue19.setter
    def itm_Issue19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Issue__itm_Issue19", None)
        self.__itm_Issue19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "itm_IssueDependency"):
                    opp_val = getattr(item, "itm_IssueDependency", None)
                    
                    if opp_val == self:
                        setattr(item, "itm_IssueDependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "itm_IssueDependency"):
                    opp_val = getattr(item, "itm_IssueDependency", None)
                    
                    setattr(item, "itm_IssueDependency", self)
                    

    @property
    def itm_Issue16(self):
        return self.__itm_Issue16

    @itm_Issue16.setter
    def itm_Issue16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Issue__itm_Issue16", None)
        self.__itm_Issue16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_Tracker17"):
                opp_val = getattr(old_value, "itm_Tracker17", None)
                if opp_val == self:
                    setattr(old_value, "itm_Tracker17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_Tracker17"):
                opp_val = getattr(value, "itm_Tracker17", None)
                setattr(value, "itm_Tracker17", self)

    @property
    def itm_Issue31(self):
        return self.__itm_Issue31

    @itm_Issue31.setter
    def itm_Issue31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Issue__itm_Issue31", None)
        self.__itm_Issue31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_IssueDependency30"):
                opp_val = getattr(old_value, "itm_IssueDependency30", None)
                if opp_val == self:
                    setattr(old_value, "itm_IssueDependency30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_IssueDependency30"):
                opp_val = getattr(value, "itm_IssueDependency30", None)
                setattr(value, "itm_IssueDependency30", self)

    @property
    def itm_Issue27(self):
        return self.__itm_Issue27

    @itm_Issue27.setter
    def itm_Issue27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Issue__itm_Issue27", None)
        self.__itm_Issue27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_Member28"):
                opp_val = getattr(old_value, "itm_Member28", None)
                if opp_val == self:
                    setattr(old_value, "itm_Member28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_Member28"):
                opp_val = getattr(value, "itm_Member28", None)
                setattr(value, "itm_Member28", self)

class itm_IssueDependency:

    def __init__(self, type: str, itm_IssueDependency: "itm_Issue" = None, itm_IssueDependency30: "itm_Issue" = None):
        self.type = type
        self.itm_IssueDependency = itm_IssueDependency
        self.itm_IssueDependency30 = itm_IssueDependency30
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def itm_IssueDependency(self):
        return self.__itm_IssueDependency

    @itm_IssueDependency.setter
    def itm_IssueDependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_IssueDependency__itm_IssueDependency", None)
        self.__itm_IssueDependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_Issue19"):
                opp_val = getattr(old_value, "itm_Issue19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_Issue19"):
                opp_val = getattr(value, "itm_Issue19", None)
                if opp_val is None:
                    setattr(value, "itm_Issue19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def itm_IssueDependency30(self):
        return self.__itm_IssueDependency30

    @itm_IssueDependency30.setter
    def itm_IssueDependency30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_IssueDependency__itm_IssueDependency30", None)
        self.__itm_IssueDependency30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_Issue31"):
                opp_val = getattr(old_value, "itm_Issue31", None)
                if opp_val == self:
                    setattr(old_value, "itm_Issue31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_Issue31"):
                opp_val = getattr(value, "itm_Issue31", None)
                setattr(value, "itm_Issue31", self)

class itm_IssueTrackingDatabase:

    pass
class itm_Member:

    pass
class itm_IssueCategory:

    def __init__(self, name: str, itm_IssueCategory: "itm_Project" = None, itm_IssueCategory22: "itm_Issue" = None):
        self.name = name
        self.itm_IssueCategory = itm_IssueCategory
        self.itm_IssueCategory22 = itm_IssueCategory22
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def itm_IssueCategory22(self):
        return self.__itm_IssueCategory22

    @itm_IssueCategory22.setter
    def itm_IssueCategory22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_IssueCategory__itm_IssueCategory22", None)
        self.__itm_IssueCategory22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_Issue21"):
                opp_val = getattr(old_value, "itm_Issue21", None)
                if opp_val == self:
                    setattr(old_value, "itm_Issue21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_Issue21"):
                opp_val = getattr(value, "itm_Issue21", None)
                setattr(value, "itm_Issue21", self)

    @property
    def itm_IssueCategory(self):
        return self.__itm_IssueCategory

    @itm_IssueCategory.setter
    def itm_IssueCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_IssueCategory__itm_IssueCategory", None)
        self.__itm_IssueCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_Project10"):
                opp_val = getattr(old_value, "itm_Project10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_Project10"):
                opp_val = getattr(value, "itm_Project10", None)
                if opp_val is None:
                    setattr(value, "itm_Project10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class itm_Version:

    def __init__(self, description: str, name: str, status: str, completedDate: date, itm_Version: "itm_Project" = None, itm_Version14: set["itm_Issue"] = None):
        self.description = description
        self.name = name
        self.status = status
        self.completedDate = completedDate
        self.itm_Version = itm_Version
        self.itm_Version14 = itm_Version14 if itm_Version14 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def completedDate(self):
        return self.__completedDate

    @completedDate.setter
    def completedDate(self, completedDate: date):
        self.__completedDate = completedDate


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def itm_Version(self):
        return self.__itm_Version

    @itm_Version.setter
    def itm_Version(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Version__itm_Version", None)
        self.__itm_Version = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_Project8"):
                opp_val = getattr(old_value, "itm_Project8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_Project8"):
                opp_val = getattr(value, "itm_Project8", None)
                if opp_val is None:
                    setattr(value, "itm_Project8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def itm_Version14(self):
        return self.__itm_Version14

    @itm_Version14.setter
    def itm_Version14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Version__itm_Version14", None)
        self.__itm_Version14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "itm_Issue"):
                    opp_val = getattr(item, "itm_Issue", None)
                    
                    if opp_val == self:
                        setattr(item, "itm_Issue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "itm_Issue"):
                    opp_val = getattr(item, "itm_Issue", None)
                    
                    setattr(item, "itm_Issue", self)
                    

class itm_User:

    def __init__(self, login: str, language: str, itm_User: "itm_IssueTrackingDatabase" = None, itm_User34: "itm_Member" = None):
        self.login = login
        self.language = language
        self.itm_User = itm_User
        self.itm_User34 = itm_User34
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login


    @property
    def itm_User(self):
        return self.__itm_User

    @itm_User.setter
    def itm_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_User__itm_User", None)
        self.__itm_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_IssueTrackingDatabase6"):
                opp_val = getattr(old_value, "itm_IssueTrackingDatabase6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_IssueTrackingDatabase6"):
                opp_val = getattr(value, "itm_IssueTrackingDatabase6", None)
                if opp_val is None:
                    setattr(value, "itm_IssueTrackingDatabase6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def itm_User34(self):
        return self.__itm_User34

    @itm_User34.setter
    def itm_User34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_User__itm_User34", None)
        self.__itm_User34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_Member33"):
                opp_val = getattr(old_value, "itm_Member33", None)
                if opp_val == self:
                    setattr(old_value, "itm_Member33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_Member33"):
                opp_val = getattr(value, "itm_Member33", None)
                setattr(value, "itm_Member33", self)

class itm_Role:

    def __init__(self, name: str, permissions: str, itm_Role: "itm_IssueTrackingDatabase" = None, itm_Role37: "itm_Member" = None):
        self.name = name
        self.permissions = permissions
        self.itm_Role = itm_Role
        self.itm_Role37 = itm_Role37
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def permissions(self):
        return self.__permissions

    @permissions.setter
    def permissions(self, permissions: str):
        self.__permissions = permissions


    @property
    def itm_Role37(self):
        return self.__itm_Role37

    @itm_Role37.setter
    def itm_Role37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Role__itm_Role37", None)
        self.__itm_Role37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_Member36"):
                opp_val = getattr(old_value, "itm_Member36", None)
                if opp_val == self:
                    setattr(old_value, "itm_Member36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_Member36"):
                opp_val = getattr(value, "itm_Member36", None)
                setattr(value, "itm_Member36", self)

    @property
    def itm_Role(self):
        return self.__itm_Role

    @itm_Role.setter
    def itm_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Role__itm_Role", None)
        self.__itm_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_IssueTrackingDatabase4"):
                opp_val = getattr(old_value, "itm_IssueTrackingDatabase4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_IssueTrackingDatabase4"):
                opp_val = getattr(value, "itm_IssueTrackingDatabase4", None)
                if opp_val is None:
                    setattr(value, "itm_IssueTrackingDatabase4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class itm_Tracker:

    def __init__(self, name: str, itm_Tracker: "itm_IssueTrackingDatabase" = None, itm_Tracker17: "itm_Issue" = None):
        self.name = name
        self.itm_Tracker = itm_Tracker
        self.itm_Tracker17 = itm_Tracker17
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def itm_Tracker(self):
        return self.__itm_Tracker

    @itm_Tracker.setter
    def itm_Tracker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Tracker__itm_Tracker", None)
        self.__itm_Tracker = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_IssueTrackingDatabase2"):
                opp_val = getattr(old_value, "itm_IssueTrackingDatabase2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_IssueTrackingDatabase2"):
                opp_val = getattr(value, "itm_IssueTrackingDatabase2", None)
                if opp_val is None:
                    setattr(value, "itm_IssueTrackingDatabase2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def itm_Tracker17(self):
        return self.__itm_Tracker17

    @itm_Tracker17.setter
    def itm_Tracker17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Tracker__itm_Tracker17", None)
        self.__itm_Tracker17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_Issue16"):
                opp_val = getattr(old_value, "itm_Issue16", None)
                if opp_val == self:
                    setattr(old_value, "itm_Issue16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_Issue16"):
                opp_val = getattr(value, "itm_Issue16", None)
                setattr(value, "itm_Issue16", self)

class itm_Project:

    def __init__(self, name: str, description: str, itm_Project: "itm_IssueTrackingDatabase" = None, itm_Project8: set["itm_Version"] = None, itm_Project10: set["itm_IssueCategory"] = None, itm_Project12: set["itm_Member"] = None):
        self.name = name
        self.description = description
        self.itm_Project = itm_Project
        self.itm_Project8 = itm_Project8 if itm_Project8 is not None else set()
        self.itm_Project10 = itm_Project10 if itm_Project10 is not None else set()
        self.itm_Project12 = itm_Project12 if itm_Project12 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def itm_Project8(self):
        return self.__itm_Project8

    @itm_Project8.setter
    def itm_Project8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Project__itm_Project8", None)
        self.__itm_Project8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "itm_Version"):
                    opp_val = getattr(item, "itm_Version", None)
                    
                    if opp_val == self:
                        setattr(item, "itm_Version", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "itm_Version"):
                    opp_val = getattr(item, "itm_Version", None)
                    
                    setattr(item, "itm_Version", self)
                    

    @property
    def itm_Project12(self):
        return self.__itm_Project12

    @itm_Project12.setter
    def itm_Project12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Project__itm_Project12", None)
        self.__itm_Project12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "itm_Member"):
                    opp_val = getattr(item, "itm_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "itm_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "itm_Member"):
                    opp_val = getattr(item, "itm_Member", None)
                    
                    setattr(item, "itm_Member", self)
                    

    @property
    def itm_Project(self):
        return self.__itm_Project

    @itm_Project.setter
    def itm_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Project__itm_Project", None)
        self.__itm_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itm_IssueTrackingDatabase"):
                opp_val = getattr(old_value, "itm_IssueTrackingDatabase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itm_IssueTrackingDatabase"):
                opp_val = getattr(value, "itm_IssueTrackingDatabase", None)
                if opp_val is None:
                    setattr(value, "itm_IssueTrackingDatabase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def itm_Project10(self):
        return self.__itm_Project10

    @itm_Project10.setter
    def itm_Project10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itm_Project__itm_Project10", None)
        self.__itm_Project10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "itm_IssueCategory"):
                    opp_val = getattr(item, "itm_IssueCategory", None)
                    
                    if opp_val == self:
                        setattr(item, "itm_IssueCategory", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "itm_IssueCategory"):
                    opp_val = getattr(item, "itm_IssueCategory", None)
                    
                    setattr(item, "itm_IssueCategory", self)
                    
