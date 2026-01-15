from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ReviewStatus(Enum):
    New = "New"
    Submitted = "Submitted"
    Merged = "Merged"
    Abandoned = "Abandoned"
    Draft = "Draft"
class RequirementStatus(Enum):
    NotSatisfied = "NotSatisfied"
    Rejected = "Rejected"
    Error = "Error"
    Unknown = "Unknown"
    Satisfied = "Satisfied"
    Optional = "Optional"
    Closed = "Closed"


############################################
# Definition of Classes
############################################

class reviews_Dated(ABC):

    def __init__(self, creationDate: date, modificationDate: date):
        self.creationDate = creationDate
        self.modificationDate = modificationDate
        
    @property
    def modificationDate(self) -> date:
        return self.__modificationDate

    @modificationDate.setter
    def modificationDate(self, modificationDate: date):
        self.__modificationDate = modificationDate

    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

class reviews_Indexed(ABC):

    def __init__(self, index: str):
        self.index = index
        
    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

class reviews_RequirementEntry:

    def __init__(self, status: str, reviews_RequirementEntry78: "reviews_ReviewRequirementsMap" = None, reviews_RequirementEntry: "reviews_User" = None):
        self.status = status
        self.reviews_RequirementEntry78 = reviews_RequirementEntry78
        self.reviews_RequirementEntry = reviews_RequirementEntry
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def reviews_RequirementEntry(self):
        return self.__reviews_RequirementEntry

    @reviews_RequirementEntry.setter
    def reviews_RequirementEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_RequirementEntry__reviews_RequirementEntry", None)
        self.__reviews_RequirementEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_User72"):
                opp_val = getattr(old_value, "reviews_User72", None)
                if opp_val == self:
                    setattr(old_value, "reviews_User72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_User72"):
                opp_val = getattr(value, "reviews_User72", None)
                setattr(value, "reviews_User72", self)

    @property
    def reviews_RequirementEntry78(self):
        return self.__reviews_RequirementEntry78

    @reviews_RequirementEntry78.setter
    def reviews_RequirementEntry78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_RequirementEntry__reviews_RequirementEntry78", None)
        self.__reviews_RequirementEntry78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_ReviewRequirementsMap77"):
                opp_val = getattr(old_value, "reviews_ReviewRequirementsMap77", None)
                if opp_val == self:
                    setattr(old_value, "reviews_ReviewRequirementsMap77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_ReviewRequirementsMap77"):
                opp_val = getattr(value, "reviews_ReviewRequirementsMap77", None)
                setattr(value, "reviews_ReviewRequirementsMap77", self)

class reviews_ApprovalValueMap:

    def __init__(self, value: str, reviews_ApprovalValueMap: "reviews_ReviewerEntry" = None, reviews_ApprovalValueMap69: "reviews_ApprovalType" = None):
        self.value = value
        self.reviews_ApprovalValueMap = reviews_ApprovalValueMap
        self.reviews_ApprovalValueMap69 = reviews_ApprovalValueMap69
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def reviews_ApprovalValueMap69(self):
        return self.__reviews_ApprovalValueMap69

    @reviews_ApprovalValueMap69.setter
    def reviews_ApprovalValueMap69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_ApprovalValueMap__reviews_ApprovalValueMap69", None)
        self.__reviews_ApprovalValueMap69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_ApprovalType70"):
                opp_val = getattr(old_value, "reviews_ApprovalType70", None)
                if opp_val == self:
                    setattr(old_value, "reviews_ApprovalType70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_ApprovalType70"):
                opp_val = getattr(value, "reviews_ApprovalType70", None)
                setattr(value, "reviews_ApprovalType70", self)

    @property
    def reviews_ApprovalValueMap(self):
        return self.__reviews_ApprovalValueMap

    @reviews_ApprovalValueMap.setter
    def reviews_ApprovalValueMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_ApprovalValueMap__reviews_ApprovalValueMap", None)
        self.__reviews_ApprovalValueMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_ReviewerEntry67"):
                opp_val = getattr(old_value, "reviews_ReviewerEntry67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_ReviewerEntry67"):
                opp_val = getattr(value, "reviews_ReviewerEntry67", None)
                if opp_val is None:
                    setattr(value, "reviews_ReviewerEntry67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class reviews_ReviewerEntry:

    pass
class Location:

    pass
class reviews_LineLocation(Location):

    def __init__(self, rangeMin: int, rangeMax: int, reviews_LineLocation: set["reviews_LineRange"] = None):
        self.rangeMin = rangeMin
        self.rangeMax = rangeMax
        self.reviews_LineLocation = reviews_LineLocation if reviews_LineLocation is not None else set()
        
    @property
    def rangeMin(self) -> int:
        return self.__rangeMin

    @rangeMin.setter
    def rangeMin(self, rangeMin: int):
        self.__rangeMin = rangeMin

    @property
    def rangeMax(self) -> int:
        return self.__rangeMax

    @rangeMax.setter
    def rangeMax(self, rangeMax: int):
        self.__rangeMax = rangeMax

    @property
    def reviews_LineLocation(self):
        return self.__reviews_LineLocation

    @reviews_LineLocation.setter
    def reviews_LineLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_LineLocation__reviews_LineLocation", None)
        self.__reviews_LineLocation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reviews_LineRange"):
                    opp_val = getattr(item, "reviews_LineRange", None)
                    
                    if opp_val == self:
                        setattr(item, "reviews_LineRange", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reviews_LineRange"):
                    opp_val = getattr(item, "reviews_LineRange", None)
                    
                    setattr(item, "reviews_LineRange", self)
                    

class reviews_LineRange:

    def __init__(self, start: int, end: int, reviews_LineRange: "reviews_LineLocation" = None):
        self.start = start
        self.end = end
        self.reviews_LineRange = reviews_LineRange
        
    @property
    def start(self) -> int:
        return self.__start

    @start.setter
    def start(self, start: int):
        self.__start = start

    @property
    def end(self) -> int:
        return self.__end

    @end.setter
    def end(self, end: int):
        self.__end = end

    @property
    def reviews_LineRange(self):
        return self.__reviews_LineRange

    @reviews_LineRange.setter
    def reviews_LineRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_LineRange__reviews_LineRange", None)
        self.__reviews_LineRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_LineLocation"):
                opp_val = getattr(old_value, "reviews_LineLocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_LineLocation"):
                opp_val = getattr(value, "reviews_LineLocation", None)
                if opp_val is None:
                    setattr(value, "reviews_LineLocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ReviewItem:

    pass
class reviews_FileVersion(ReviewItem):

    def __init__(self, path: str, description: str, content: str, fileRevision: str, reviews_FileVersion: "reviews_FileItem" = None, reviews_FileVersion51: "reviews_FileItem" = None, reviews_FileVersion59: "reviews_FileItem" = None):
        self.path = path
        self.description = description
        self.content = content
        self.fileRevision = fileRevision
        self.reviews_FileVersion = reviews_FileVersion
        self.reviews_FileVersion51 = reviews_FileVersion51
        self.reviews_FileVersion59 = reviews_FileVersion59
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def fileRevision(self) -> str:
        return self.__fileRevision

    @fileRevision.setter
    def fileRevision(self, fileRevision: str):
        self.__fileRevision = fileRevision

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def reviews_FileVersion(self):
        return self.__reviews_FileVersion

    @reviews_FileVersion.setter
    def reviews_FileVersion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_FileVersion__reviews_FileVersion", None)
        self.__reviews_FileVersion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_FileItem"):
                opp_val = getattr(old_value, "reviews_FileItem", None)
                if opp_val == self:
                    setattr(old_value, "reviews_FileItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_FileItem"):
                opp_val = getattr(value, "reviews_FileItem", None)
                setattr(value, "reviews_FileItem", self)

    @property
    def reviews_FileVersion51(self):
        return self.__reviews_FileVersion51

    @reviews_FileVersion51.setter
    def reviews_FileVersion51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_FileVersion__reviews_FileVersion51", None)
        self.__reviews_FileVersion51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_FileItem50"):
                opp_val = getattr(old_value, "reviews_FileItem50", None)
                if opp_val == self:
                    setattr(old_value, "reviews_FileItem50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_FileItem50"):
                opp_val = getattr(value, "reviews_FileItem50", None)
                setattr(value, "reviews_FileItem50", self)

    @property
    def reviews_FileVersion59(self):
        return self.__reviews_FileVersion59

    @reviews_FileVersion59.setter
    def reviews_FileVersion59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_FileVersion__reviews_FileVersion59", None)
        self.__reviews_FileVersion59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_FileItem60"):
                opp_val = getattr(old_value, "reviews_FileItem60", None)
                if opp_val == self:
                    setattr(old_value, "reviews_FileItem60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_FileItem60"):
                opp_val = getattr(value, "reviews_FileItem60", None)
                setattr(value, "reviews_FileItem60", self)

class reviews_FileItem(ReviewItem):

    pass
class reviews_ApprovalType:

    def __init__(self, key: str, name: str, reviews_ApprovalType: "reviews_Repository" = None, reviews_ApprovalType70: "reviews_ApprovalValueMap" = None, reviews_ApprovalType75: "reviews_ReviewRequirementsMap" = None):
        self.key = key
        self.name = name
        self.reviews_ApprovalType = reviews_ApprovalType
        self.reviews_ApprovalType70 = reviews_ApprovalType70
        self.reviews_ApprovalType75 = reviews_ApprovalType75
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def reviews_ApprovalType70(self):
        return self.__reviews_ApprovalType70

    @reviews_ApprovalType70.setter
    def reviews_ApprovalType70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_ApprovalType__reviews_ApprovalType70", None)
        self.__reviews_ApprovalType70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_ApprovalValueMap69"):
                opp_val = getattr(old_value, "reviews_ApprovalValueMap69", None)
                if opp_val == self:
                    setattr(old_value, "reviews_ApprovalValueMap69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_ApprovalValueMap69"):
                opp_val = getattr(value, "reviews_ApprovalValueMap69", None)
                setattr(value, "reviews_ApprovalValueMap69", self)

    @property
    def reviews_ApprovalType75(self):
        return self.__reviews_ApprovalType75

    @reviews_ApprovalType75.setter
    def reviews_ApprovalType75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_ApprovalType__reviews_ApprovalType75", None)
        self.__reviews_ApprovalType75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_ReviewRequirementsMap74"):
                opp_val = getattr(old_value, "reviews_ReviewRequirementsMap74", None)
                if opp_val == self:
                    setattr(old_value, "reviews_ReviewRequirementsMap74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_ReviewRequirementsMap74"):
                opp_val = getattr(value, "reviews_ReviewRequirementsMap74", None)
                setattr(value, "reviews_ReviewRequirementsMap74", self)

    @property
    def reviews_ApprovalType(self):
        return self.__reviews_ApprovalType

    @reviews_ApprovalType.setter
    def reviews_ApprovalType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_ApprovalType__reviews_ApprovalType", None)
        self.__reviews_ApprovalType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_Repository"):
                opp_val = getattr(old_value, "reviews_Repository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_Repository"):
                opp_val = getattr(value, "reviews_Repository", None)
                if opp_val is None:
                    setattr(value, "reviews_Repository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Indexed:

    pass
class reviews_Location(Indexed):

    pass
class reviews_User:

    def __init__(self, id: str, email: str, displayName: str, reviews_User: "reviews_Change" = None, reviews_User22: "reviews_Comment" = None, reviews_User33: "reviews_ReviewItem" = None, reviews_User47: "reviews_Repository" = None, reviews_User36: "reviews_ReviewItem" = None, reviews_User43: "reviews_Repository" = None, reviews_User63: "reviews_UserApprovalsMap" = None, reviews_User72: "reviews_RequirementEntry" = None):
        self.id = id
        self.email = email
        self.displayName = displayName
        self.reviews_User = reviews_User
        self.reviews_User22 = reviews_User22
        self.reviews_User33 = reviews_User33
        self.reviews_User47 = reviews_User47
        self.reviews_User36 = reviews_User36
        self.reviews_User43 = reviews_User43
        self.reviews_User63 = reviews_User63
        self.reviews_User72 = reviews_User72
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def reviews_User63(self):
        return self.__reviews_User63

    @reviews_User63.setter
    def reviews_User63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_User__reviews_User63", None)
        self.__reviews_User63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_UserApprovalsMap62"):
                opp_val = getattr(old_value, "reviews_UserApprovalsMap62", None)
                if opp_val == self:
                    setattr(old_value, "reviews_UserApprovalsMap62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_UserApprovalsMap62"):
                opp_val = getattr(value, "reviews_UserApprovalsMap62", None)
                setattr(value, "reviews_UserApprovalsMap62", self)

    @property
    def reviews_User(self):
        return self.__reviews_User

    @reviews_User.setter
    def reviews_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_User__reviews_User", None)
        self.__reviews_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_Change"):
                opp_val = getattr(old_value, "reviews_Change", None)
                if opp_val == self:
                    setattr(old_value, "reviews_Change", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_Change"):
                opp_val = getattr(value, "reviews_Change", None)
                setattr(value, "reviews_Change", self)

    @property
    def reviews_User36(self):
        return self.__reviews_User36

    @reviews_User36.setter
    def reviews_User36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_User__reviews_User36", None)
        self.__reviews_User36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_ReviewItem35"):
                opp_val = getattr(old_value, "reviews_ReviewItem35", None)
                if opp_val == self:
                    setattr(old_value, "reviews_ReviewItem35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_ReviewItem35"):
                opp_val = getattr(value, "reviews_ReviewItem35", None)
                setattr(value, "reviews_ReviewItem35", self)

    @property
    def reviews_User47(self):
        return self.__reviews_User47

    @reviews_User47.setter
    def reviews_User47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_User__reviews_User47", None)
        self.__reviews_User47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_Repository46"):
                opp_val = getattr(old_value, "reviews_Repository46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_Repository46"):
                opp_val = getattr(value, "reviews_Repository46", None)
                if opp_val is None:
                    setattr(value, "reviews_Repository46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reviews_User33(self):
        return self.__reviews_User33

    @reviews_User33.setter
    def reviews_User33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_User__reviews_User33", None)
        self.__reviews_User33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_ReviewItem"):
                opp_val = getattr(old_value, "reviews_ReviewItem", None)
                if opp_val == self:
                    setattr(old_value, "reviews_ReviewItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_ReviewItem"):
                opp_val = getattr(value, "reviews_ReviewItem", None)
                setattr(value, "reviews_ReviewItem", self)

    @property
    def reviews_User43(self):
        return self.__reviews_User43

    @reviews_User43.setter
    def reviews_User43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_User__reviews_User43", None)
        self.__reviews_User43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_Repository42"):
                opp_val = getattr(old_value, "reviews_Repository42", None)
                if opp_val == self:
                    setattr(old_value, "reviews_Repository42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_Repository42"):
                opp_val = getattr(value, "reviews_Repository42", None)
                setattr(value, "reviews_Repository42", self)

    @property
    def reviews_User22(self):
        return self.__reviews_User22

    @reviews_User22.setter
    def reviews_User22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_User__reviews_User22", None)
        self.__reviews_User22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_Comment21"):
                opp_val = getattr(old_value, "reviews_Comment21", None)
                if opp_val == self:
                    setattr(old_value, "reviews_Comment21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_Comment21"):
                opp_val = getattr(value, "reviews_Comment21", None)
                setattr(value, "reviews_Comment21", self)

    @property
    def reviews_User72(self):
        return self.__reviews_User72

    @reviews_User72.setter
    def reviews_User72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_User__reviews_User72", None)
        self.__reviews_User72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_RequirementEntry"):
                opp_val = getattr(old_value, "reviews_RequirementEntry", None)
                if opp_val == self:
                    setattr(old_value, "reviews_RequirementEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_RequirementEntry"):
                opp_val = getattr(value, "reviews_RequirementEntry", None)
                setattr(value, "reviews_RequirementEntry", self)

class reviews_ReviewRequirementsMap:

    pass
class reviews_UserApprovalsMap:

    pass
class reviews_Repository:

    def __init__(self, taskRepositoryUrl: str, description: str, taskConnectorKind: str, taskRepository: str, Repository: "reviews_Review" = None, reviews_Repository: set["reviews_ApprovalType"] = None, reviews_Repository46: set["reviews_User"] = None, reviews_Repository42: "reviews_User" = None, repository: set["reviews_Review"] = None):
        self.taskRepositoryUrl = taskRepositoryUrl
        self.description = description
        self.taskConnectorKind = taskConnectorKind
        self.taskRepository = taskRepository
        self.Repository = Repository
        self.reviews_Repository = reviews_Repository if reviews_Repository is not None else set()
        self.reviews_Repository46 = reviews_Repository46 if reviews_Repository46 is not None else set()
        self.reviews_Repository42 = reviews_Repository42
        self.repository = repository if repository is not None else set()
        
    @property
    def taskRepositoryUrl(self) -> str:
        return self.__taskRepositoryUrl

    @taskRepositoryUrl.setter
    def taskRepositoryUrl(self, taskRepositoryUrl: str):
        self.__taskRepositoryUrl = taskRepositoryUrl

    @property
    def taskRepository(self) -> str:
        return self.__taskRepository

    @taskRepository.setter
    def taskRepository(self, taskRepository: str):
        self.__taskRepository = taskRepository

    @property
    def taskConnectorKind(self) -> str:
        return self.__taskConnectorKind

    @taskConnectorKind.setter
    def taskConnectorKind(self, taskConnectorKind: str):
        self.__taskConnectorKind = taskConnectorKind

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def reviews_Repository(self):
        return self.__reviews_Repository

    @reviews_Repository.setter
    def reviews_Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Repository__reviews_Repository", None)
        self.__reviews_Repository = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reviews_ApprovalType"):
                    opp_val = getattr(item, "reviews_ApprovalType", None)
                    
                    if opp_val == self:
                        setattr(item, "reviews_ApprovalType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reviews_ApprovalType"):
                    opp_val = getattr(item, "reviews_ApprovalType", None)
                    
                    setattr(item, "reviews_ApprovalType", self)
                    

    @property
    def Repository(self):
        return self.__Repository

    @Repository.setter
    def Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Repository__Repository", None)
        self.__Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews"):
                opp_val = getattr(old_value, "reviews", None)
                if opp_val == self:
                    setattr(old_value, "reviews", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews"):
                opp_val = getattr(value, "reviews", None)
                setattr(value, "reviews", self)

    @property
    def repository(self):
        return self.__repository

    @repository.setter
    def repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Repository__repository", None)
        self.__repository = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Review"):
                    opp_val = getattr(item, "Review", None)
                    
                    if opp_val == self:
                        setattr(item, "Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Review"):
                    opp_val = getattr(item, "Review", None)
                    
                    setattr(item, "Review", self)
                    

    @property
    def reviews_Repository46(self):
        return self.__reviews_Repository46

    @reviews_Repository46.setter
    def reviews_Repository46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Repository__reviews_Repository46", None)
        self.__reviews_Repository46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reviews_User47"):
                    opp_val = getattr(item, "reviews_User47", None)
                    
                    if opp_val == self:
                        setattr(item, "reviews_User47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reviews_User47"):
                    opp_val = getattr(item, "reviews_User47", None)
                    
                    setattr(item, "reviews_User47", self)
                    

    @property
    def reviews_Repository42(self):
        return self.__reviews_Repository42

    @reviews_Repository42.setter
    def reviews_Repository42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Repository__reviews_Repository42", None)
        self.__reviews_Repository42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_User43"):
                opp_val = getattr(old_value, "reviews_User43", None)
                if opp_val == self:
                    setattr(old_value, "reviews_User43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_User43"):
                opp_val = getattr(value, "reviews_User43", None)
                setattr(value, "reviews_User43", self)

class Change:

    pass
class CommentContainer:

    pass
class reviews_ReviewItem(CommentContainer):

    def __init__(self, name: str, id: str, reference: str, reviews_ReviewItem38: "reviews_Review" = None, reviews_ReviewItem: "reviews_User" = None, reviews_ReviewItem35: "reviews_User" = None):
        self.name = name
        self.id = id
        self.reference = reference
        self.reviews_ReviewItem38 = reviews_ReviewItem38
        self.reviews_ReviewItem = reviews_ReviewItem
        self.reviews_ReviewItem35 = reviews_ReviewItem35
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def reviews_ReviewItem(self):
        return self.__reviews_ReviewItem

    @reviews_ReviewItem.setter
    def reviews_ReviewItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_ReviewItem__reviews_ReviewItem", None)
        self.__reviews_ReviewItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_User33"):
                opp_val = getattr(old_value, "reviews_User33", None)
                if opp_val == self:
                    setattr(old_value, "reviews_User33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_User33"):
                opp_val = getattr(value, "reviews_User33", None)
                setattr(value, "reviews_User33", self)

    @property
    def reviews_ReviewItem38(self):
        return self.__reviews_ReviewItem38

    @reviews_ReviewItem38.setter
    def reviews_ReviewItem38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_ReviewItem__reviews_ReviewItem38", None)
        self.__reviews_ReviewItem38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_Review39"):
                opp_val = getattr(old_value, "reviews_Review39", None)
                if opp_val == self:
                    setattr(old_value, "reviews_Review39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_Review39"):
                opp_val = getattr(value, "reviews_Review39", None)
                setattr(value, "reviews_Review39", self)

    @property
    def reviews_ReviewItem35(self):
        return self.__reviews_ReviewItem35

    @reviews_ReviewItem35.setter
    def reviews_ReviewItem35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_ReviewItem__reviews_ReviewItem35", None)
        self.__reviews_ReviewItem35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_User36"):
                opp_val = getattr(old_value, "reviews_User36", None)
                if opp_val == self:
                    setattr(old_value, "reviews_User36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_User36"):
                opp_val = getattr(value, "reviews_User36", None)
                setattr(value, "reviews_User36", self)

class reviews_Review(Change, CommentContainer):

    pass
class reviews_CommentContainer(ABC):

    def __init__(self, reviews_CommentContainer: set["reviews_Comment"] = None, item: set["reviews_Comment"] = None, reviews_CommentContainer3: set["reviews_Comment"] = None, reviews_CommentContainer6: set["reviews_Comment"] = None, CommentContainer: "reviews_Comment" = None):
        self.reviews_CommentContainer = reviews_CommentContainer if reviews_CommentContainer is not None else set()
        self.item = item if item is not None else set()
        self.reviews_CommentContainer3 = reviews_CommentContainer3 if reviews_CommentContainer3 is not None else set()
        self.reviews_CommentContainer6 = reviews_CommentContainer6 if reviews_CommentContainer6 is not None else set()
        self.CommentContainer = CommentContainer
        
    @property
    def reviews_CommentContainer(self):
        return self.__reviews_CommentContainer

    @reviews_CommentContainer.setter
    def reviews_CommentContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_CommentContainer__reviews_CommentContainer", None)
        self.__reviews_CommentContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reviews_Comment"):
                    opp_val = getattr(item, "reviews_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "reviews_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reviews_Comment"):
                    opp_val = getattr(item, "reviews_Comment", None)
                    
                    setattr(item, "reviews_Comment", self)
                    

    @property
    def reviews_CommentContainer3(self):
        return self.__reviews_CommentContainer3

    @reviews_CommentContainer3.setter
    def reviews_CommentContainer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_CommentContainer__reviews_CommentContainer3", None)
        self.__reviews_CommentContainer3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reviews_Comment4"):
                    opp_val = getattr(item, "reviews_Comment4", None)
                    
                    if opp_val == self:
                        setattr(item, "reviews_Comment4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reviews_Comment4"):
                    opp_val = getattr(item, "reviews_Comment4", None)
                    
                    setattr(item, "reviews_Comment4", self)
                    

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_CommentContainer__item", None)
        self.__item = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    setattr(item, "Comment", self)
                    

    @property
    def CommentContainer(self):
        return self.__CommentContainer

    @CommentContainer.setter
    def CommentContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_CommentContainer__CommentContainer", None)
        self.__CommentContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comments"):
                opp_val = getattr(old_value, "comments", None)
                if opp_val == self:
                    setattr(old_value, "comments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comments"):
                opp_val = getattr(value, "comments", None)
                setattr(value, "comments", self)

    @property
    def reviews_CommentContainer6(self):
        return self.__reviews_CommentContainer6

    @reviews_CommentContainer6.setter
    def reviews_CommentContainer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_CommentContainer__reviews_CommentContainer6", None)
        self.__reviews_CommentContainer6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reviews_Comment7"):
                    opp_val = getattr(item, "reviews_Comment7", None)
                    
                    if opp_val == self:
                        setattr(item, "reviews_Comment7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reviews_Comment7"):
                    opp_val = getattr(item, "reviews_Comment7", None)
                    
                    setattr(item, "reviews_Comment7", self)
                    

    def createComment(self, initalLocation: str, commentText: str) -> str:
        # TODO: Implement createComment method
        pass

class Dated:

    pass
class reviews_ReviewItemSet(ReviewItem, Dated):

    def __init__(self, revision: str, ReviewItemSet: "reviews_Review" = None, ReviewItemSet53: "reviews_FileItem" = None, set: set["reviews_FileItem"] = None, sets: "reviews_Review" = None):
        self.revision = revision
        self.ReviewItemSet = ReviewItemSet
        self.ReviewItemSet53 = ReviewItemSet53
        self.set = set if set is not None else set()
        self.sets = sets
        
    @property
    def revision(self) -> str:
        return self.__revision

    @revision.setter
    def revision(self, revision: str):
        self.__revision = revision

    @property
    def ReviewItemSet53(self):
        return self.__ReviewItemSet53

    @ReviewItemSet53.setter
    def ReviewItemSet53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_ReviewItemSet__ReviewItemSet53", None)
        self.__ReviewItemSet53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items"):
                opp_val = getattr(old_value, "items", None)
                if opp_val == self:
                    setattr(old_value, "items", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items"):
                opp_val = getattr(value, "items", None)
                setattr(value, "items", self)

    @property
    def ReviewItemSet(self):
        return self.__ReviewItemSet

    @ReviewItemSet.setter
    def ReviewItemSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_ReviewItemSet__ReviewItemSet", None)
        self.__ReviewItemSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentReview"):
                opp_val = getattr(old_value, "parentReview", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentReview"):
                opp_val = getattr(value, "parentReview", None)
                if opp_val is None:
                    setattr(value, "parentReview", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def set(self):
        return self.__set

    @set.setter
    def set(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_ReviewItemSet__set", None)
        self.__set = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FileItem"):
                    opp_val = getattr(item, "FileItem", None)
                    
                    if opp_val == self:
                        setattr(item, "FileItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FileItem"):
                    opp_val = getattr(item, "FileItem", None)
                    
                    setattr(item, "FileItem", self)
                    

    @property
    def sets(self):
        return self.__sets

    @sets.setter
    def sets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_ReviewItemSet__sets", None)
        self.__sets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Review56"):
                opp_val = getattr(old_value, "Review56", None)
                if opp_val == self:
                    setattr(old_value, "Review56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Review56"):
                opp_val = getattr(value, "Review56", None)
                setattr(value, "Review56", self)

class reviews_Change(Dated):

    def __init__(self, state: str, id: str, key: str, subject: str, message: str, reviews_Change: "reviews_User" = None, reviews_Change12: "reviews_Review" = None, reviews_Change15: "reviews_Review" = None):
        self.state = state
        self.id = id
        self.key = key
        self.subject = subject
        self.message = message
        self.reviews_Change = reviews_Change
        self.reviews_Change12 = reviews_Change12
        self.reviews_Change15 = reviews_Change15
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def reviews_Change12(self):
        return self.__reviews_Change12

    @reviews_Change12.setter
    def reviews_Change12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Change__reviews_Change12", None)
        self.__reviews_Change12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_Review"):
                opp_val = getattr(old_value, "reviews_Review", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_Review"):
                opp_val = getattr(value, "reviews_Review", None)
                if opp_val is None:
                    setattr(value, "reviews_Review", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reviews_Change(self):
        return self.__reviews_Change

    @reviews_Change.setter
    def reviews_Change(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Change__reviews_Change", None)
        self.__reviews_Change = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_User"):
                opp_val = getattr(old_value, "reviews_User", None)
                if opp_val == self:
                    setattr(old_value, "reviews_User", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_User"):
                opp_val = getattr(value, "reviews_User", None)
                setattr(value, "reviews_User", self)

    @property
    def reviews_Change15(self):
        return self.__reviews_Change15

    @reviews_Change15.setter
    def reviews_Change15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Change__reviews_Change15", None)
        self.__reviews_Change15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_Review14"):
                opp_val = getattr(old_value, "reviews_Review14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_Review14"):
                opp_val = getattr(value, "reviews_Review14", None)
                if opp_val is None:
                    setattr(value, "reviews_Review14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class reviews_Comment(Dated, Indexed):

    def __init__(self, description: str, id: str, draft: bool, title: str, reviews_Comment: "reviews_CommentContainer" = None, Comment: "reviews_CommentContainer" = None, reviews_Comment4: "reviews_CommentContainer" = None, reviews_Comment7: "reviews_CommentContainer" = None, reviews_Comment21: "reviews_User" = None, reviews_Comment25: "reviews_Comment" = None, reviews_Comment23: set["reviews_Comment"] = None, reviews_Comment27: set["reviews_Location"] = None, reviews_Comment29: "reviews_Review" = None, comments: "reviews_CommentContainer" = None):
        self.description = description
        self.id = id
        self.draft = draft
        self.title = title
        self.reviews_Comment = reviews_Comment
        self.Comment = Comment
        self.reviews_Comment4 = reviews_Comment4
        self.reviews_Comment7 = reviews_Comment7
        self.reviews_Comment21 = reviews_Comment21
        self.reviews_Comment25 = reviews_Comment25
        self.reviews_Comment23 = reviews_Comment23 if reviews_Comment23 is not None else set()
        self.reviews_Comment27 = reviews_Comment27 if reviews_Comment27 is not None else set()
        self.reviews_Comment29 = reviews_Comment29
        self.comments = comments
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def draft(self) -> bool:
        return self.__draft

    @draft.setter
    def draft(self, draft: bool):
        self.__draft = draft

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def reviews_Comment29(self):
        return self.__reviews_Comment29

    @reviews_Comment29.setter
    def reviews_Comment29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Comment__reviews_Comment29", None)
        self.__reviews_Comment29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_Review30"):
                opp_val = getattr(old_value, "reviews_Review30", None)
                if opp_val == self:
                    setattr(old_value, "reviews_Review30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_Review30"):
                opp_val = getattr(value, "reviews_Review30", None)
                setattr(value, "reviews_Review30", self)

    @property
    def reviews_Comment23(self):
        return self.__reviews_Comment23

    @reviews_Comment23.setter
    def reviews_Comment23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Comment__reviews_Comment23", None)
        self.__reviews_Comment23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reviews_Comment25"):
                    opp_val = getattr(item, "reviews_Comment25", None)
                    
                    if opp_val == self:
                        setattr(item, "reviews_Comment25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reviews_Comment25"):
                    opp_val = getattr(item, "reviews_Comment25", None)
                    
                    setattr(item, "reviews_Comment25", self)
                    

    @property
    def reviews_Comment7(self):
        return self.__reviews_Comment7

    @reviews_Comment7.setter
    def reviews_Comment7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Comment__reviews_Comment7", None)
        self.__reviews_Comment7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_CommentContainer6"):
                opp_val = getattr(old_value, "reviews_CommentContainer6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_CommentContainer6"):
                opp_val = getattr(value, "reviews_CommentContainer6", None)
                if opp_val is None:
                    setattr(value, "reviews_CommentContainer6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reviews_Comment27(self):
        return self.__reviews_Comment27

    @reviews_Comment27.setter
    def reviews_Comment27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Comment__reviews_Comment27", None)
        self.__reviews_Comment27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reviews_Location"):
                    opp_val = getattr(item, "reviews_Location", None)
                    
                    if opp_val == self:
                        setattr(item, "reviews_Location", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reviews_Location"):
                    opp_val = getattr(item, "reviews_Location", None)
                    
                    setattr(item, "reviews_Location", self)
                    

    @property
    def reviews_Comment25(self):
        return self.__reviews_Comment25

    @reviews_Comment25.setter
    def reviews_Comment25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Comment__reviews_Comment25", None)
        self.__reviews_Comment25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_Comment23"):
                opp_val = getattr(old_value, "reviews_Comment23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_Comment23"):
                opp_val = getattr(value, "reviews_Comment23", None)
                if opp_val is None:
                    setattr(value, "reviews_Comment23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reviews_Comment(self):
        return self.__reviews_Comment

    @reviews_Comment.setter
    def reviews_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Comment__reviews_Comment", None)
        self.__reviews_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_CommentContainer"):
                opp_val = getattr(old_value, "reviews_CommentContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_CommentContainer"):
                opp_val = getattr(value, "reviews_CommentContainer", None)
                if opp_val is None:
                    setattr(value, "reviews_CommentContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Comment__comments", None)
        self.__comments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommentContainer"):
                opp_val = getattr(old_value, "CommentContainer", None)
                if opp_val == self:
                    setattr(old_value, "CommentContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommentContainer"):
                opp_val = getattr(value, "CommentContainer", None)
                setattr(value, "CommentContainer", self)

    @property
    def reviews_Comment21(self):
        return self.__reviews_Comment21

    @reviews_Comment21.setter
    def reviews_Comment21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Comment__reviews_Comment21", None)
        self.__reviews_Comment21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_User22"):
                opp_val = getattr(old_value, "reviews_User22", None)
                if opp_val == self:
                    setattr(old_value, "reviews_User22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_User22"):
                opp_val = getattr(value, "reviews_User22", None)
                setattr(value, "reviews_User22", self)

    @property
    def reviews_Comment4(self):
        return self.__reviews_Comment4

    @reviews_Comment4.setter
    def reviews_Comment4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Comment__reviews_Comment4", None)
        self.__reviews_Comment4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews_CommentContainer3"):
                opp_val = getattr(old_value, "reviews_CommentContainer3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews_CommentContainer3"):
                opp_val = getattr(value, "reviews_CommentContainer3", None)
                if opp_val is None:
                    setattr(value, "reviews_CommentContainer3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Comment(self):
        return self.__Comment

    @Comment.setter
    def Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reviews_Comment__Comment", None)
        self.__Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item"):
                opp_val = getattr(old_value, "item", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item"):
                opp_val = getattr(value, "item", None)
                if opp_val is None:
                    setattr(value, "item", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
