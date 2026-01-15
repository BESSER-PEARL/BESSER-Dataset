from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class R4EReviewType(Enum):
    R4E_REVIEW_TYPE_BASIC = "R4E_REVIEW_TYPE_BASIC"
    R4E_REVIEW_TYPE_INFORMAL = "R4E_REVIEW_TYPE_INFORMAL"
    R4E_REVIEW_TYPE_FORMAL = "R4E_REVIEW_TYPE_FORMAL"
class R4EReviewPhase(Enum):
    R4E_REVIEW_PHASE_REWORK = "R4E_REVIEW_PHASE_REWORK"
    R4E_REVIEW_PHASE_COMPLETED = "R4E_REVIEW_PHASE_COMPLETED"
    R4E_REVIEW_PHASE_STARTED = "R4E_REVIEW_PHASE_STARTED"
    R4E_REVIEW_PHASE_PREPARATION = "R4E_REVIEW_PHASE_PREPARATION"
    R4E_REVIEW_PHASE_DECISION = "R4E_REVIEW_PHASE_DECISION"
class R4EContextType(Enum):
    R4E_UNDEFINED = "R4E_UNDEFINED"
    R4E_ADDED = "R4E_ADDED"
    R4E_DELETED = "R4E_DELETED"
    R4E_MODIFIED = "R4E_MODIFIED"
    R4E_REPLACED = "R4E_REPLACED"
class R4EUserRole(Enum):
    R4E_ROLE_REVIEWER = "R4E_ROLE_REVIEWER"
    R4E_ROLE_LEAD = "R4E_ROLE_LEAD"
    R4E_ROLE_AUTHOR = "R4E_ROLE_AUTHOR"
    R4E_ROLE_ORGANIZER = "R4E_ROLE_ORGANIZER"
class R4EAnomalyState(Enum):
    R4E_ANOMALY_STATE_CREATED = "R4E_ANOMALY_STATE_CREATED"
    R4E_ANOMALY_STATE_ASSIGNED = "R4E_ANOMALY_STATE_ASSIGNED"
    R4E_ANOMALY_STATE_ACCEPTED = "R4E_ANOMALY_STATE_ACCEPTED"
    R4E_ANOMALY_STATE_FIXED = "R4E_ANOMALY_STATE_FIXED"
    R4E_ANOMALY_STATE_DUPLICATED = "R4E_ANOMALY_STATE_DUPLICATED"
    R4E_ANOMALY_STATE_REJECTED = "R4E_ANOMALY_STATE_REJECTED"
    R4E_ANOMALY_STATE_DEFERRED = "R4E_ANOMALY_STATE_DEFERRED"
    R4E_ANOMALY_STATE_VERIFIED = "R4E_ANOMALY_STATE_VERIFIED"
class R4EDecision(Enum):
    R4E_REVIEW_DECISION_NONE = "R4E_REVIEW_DECISION_NONE"
    R4E_REVIEW_DECISION_ACCEPTED = "R4E_REVIEW_DECISION_ACCEPTED"
    R4E_REVIEW_DECISION_ACCEPTED_FOLLOWUP = "R4E_REVIEW_DECISION_ACCEPTED_FOLLOWUP"
    R4E_REVIEW_DECISION_REJECTED = "R4E_REVIEW_DECISION_REJECTED"


############################################
# Definition of Classes
############################################

class model_R4EUserReviews:

    def __init__(self, name: str, createdReviews: str, model_R4EUserReviews94: "model_MapUserIDToUserReviews" = None, model_R4EUserReviews: set["model_MapNameToReview"] = None, model_R4EUserReviews82: "model_R4EReviewGroup" = None):
        self.name = name
        self.createdReviews = createdReviews
        self.model_R4EUserReviews94 = model_R4EUserReviews94
        self.model_R4EUserReviews = model_R4EUserReviews if model_R4EUserReviews is not None else set()
        self.model_R4EUserReviews82 = model_R4EUserReviews82
        
    @property
    def createdReviews(self) -> str:
        return self.__createdReviews

    @createdReviews.setter
    def createdReviews(self, createdReviews: str):
        self.__createdReviews = createdReviews

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_R4EUserReviews94(self):
        return self.__model_R4EUserReviews94

    @model_R4EUserReviews94.setter
    def model_R4EUserReviews94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EUserReviews__model_R4EUserReviews94", None)
        self.__model_R4EUserReviews94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MapUserIDToUserReviews93"):
                opp_val = getattr(old_value, "model_MapUserIDToUserReviews93", None)
                if opp_val == self:
                    setattr(old_value, "model_MapUserIDToUserReviews93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MapUserIDToUserReviews93"):
                opp_val = getattr(value, "model_MapUserIDToUserReviews93", None)
                setattr(value, "model_MapUserIDToUserReviews93", self)

    @property
    def model_R4EUserReviews82(self):
        return self.__model_R4EUserReviews82

    @model_R4EUserReviews82.setter
    def model_R4EUserReviews82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EUserReviews__model_R4EUserReviews82", None)
        self.__model_R4EUserReviews82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReviewGroup83"):
                opp_val = getattr(old_value, "model_R4EReviewGroup83", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EReviewGroup83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReviewGroup83"):
                opp_val = getattr(value, "model_R4EReviewGroup83", None)
                setattr(value, "model_R4EReviewGroup83", self)

    @property
    def model_R4EUserReviews(self):
        return self.__model_R4EUserReviews

    @model_R4EUserReviews.setter
    def model_R4EUserReviews(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EUserReviews__model_R4EUserReviews", None)
        self.__model_R4EUserReviews = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MapNameToReview80"):
                    opp_val = getattr(item, "model_MapNameToReview80", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MapNameToReview80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MapNameToReview80"):
                    opp_val = getattr(item, "model_MapNameToReview80", None)
                    
                    setattr(item, "model_MapNameToReview80", self)
                    

class R4ETextPosition:

    pass
class model_R4EAnomalyTextPosition(R4ETextPosition):

    pass
class model_R4EPosition:

    pass
class Location:

    pass
class model_R4EContent(Location):

    def __init__(self, info: str, model_R4EContent69: "model_R4EPosition" = None, model_R4EContent: "model_R4EDelta" = None, model_R4EContent64: "model_R4EDelta" = None):
        self.info = info
        self.model_R4EContent69 = model_R4EContent69
        self.model_R4EContent = model_R4EContent
        self.model_R4EContent64 = model_R4EContent64
        
    @property
    def info(self) -> str:
        return self.__info

    @info.setter
    def info(self, info: str):
        self.__info = info

    @property
    def model_R4EContent(self):
        return self.__model_R4EContent

    @model_R4EContent.setter
    def model_R4EContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EContent__model_R4EContent", None)
        self.__model_R4EContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EDelta61"):
                opp_val = getattr(old_value, "model_R4EDelta61", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EDelta61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EDelta61"):
                opp_val = getattr(value, "model_R4EDelta61", None)
                setattr(value, "model_R4EDelta61", self)

    @property
    def model_R4EContent69(self):
        return self.__model_R4EContent69

    @model_R4EContent69.setter
    def model_R4EContent69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EContent__model_R4EContent69", None)
        self.__model_R4EContent69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EPosition"):
                opp_val = getattr(old_value, "model_R4EPosition", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EPosition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EPosition"):
                opp_val = getattr(value, "model_R4EPosition", None)
                setattr(value, "model_R4EPosition", self)

    @property
    def model_R4EContent64(self):
        return self.__model_R4EContent64

    @model_R4EContent64.setter
    def model_R4EContent64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EContent__model_R4EContent64", None)
        self.__model_R4EContent64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EDelta63"):
                opp_val = getattr(old_value, "model_R4EDelta63", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EDelta63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EDelta63"):
                opp_val = getattr(value, "model_R4EDelta63", None)
                setattr(value, "model_R4EDelta63", self)

class ReviewComponent:

    pass
class model_R4EReviewComponent(ReviewComponent):

    def __init__(self, assignedTo: str):
        self.assignedTo = assignedTo
        
    @property
    def assignedTo(self) -> str:
        return self.__assignedTo

    @assignedTo.setter
    def assignedTo(self, assignedTo: str):
        self.__assignedTo = assignedTo

class Comment:

    pass
class ReviewState:

    pass
class model_R4EReviewState(ReviewState):

    def __init__(self, state: str):
        self.state = state
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

class TaskReference:

    pass
class R4EContent:

    pass
class model_R4ETextContent(R4EContent):

    def __init__(self, content: str):
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class model_MapKeyToInfoAttributes:

    def __init__(self, key: str, value: str, model_MapKeyToInfoAttributes: "model_R4EItem" = None, model_MapKeyToInfoAttributes48: "model_R4EComment" = None, model_MapKeyToInfoAttributes59: "model_R4EFileContext" = None, model_MapKeyToInfoAttributes72: "model_R4EFileVersion" = None):
        self.key = key
        self.value = value
        self.model_MapKeyToInfoAttributes = model_MapKeyToInfoAttributes
        self.model_MapKeyToInfoAttributes48 = model_MapKeyToInfoAttributes48
        self.model_MapKeyToInfoAttributes59 = model_MapKeyToInfoAttributes59
        self.model_MapKeyToInfoAttributes72 = model_MapKeyToInfoAttributes72
        
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
    def model_MapKeyToInfoAttributes48(self):
        return self.__model_MapKeyToInfoAttributes48

    @model_MapKeyToInfoAttributes48.setter
    def model_MapKeyToInfoAttributes48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapKeyToInfoAttributes__model_MapKeyToInfoAttributes48", None)
        self.__model_MapKeyToInfoAttributes48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EComment47"):
                opp_val = getattr(old_value, "model_R4EComment47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EComment47"):
                opp_val = getattr(value, "model_R4EComment47", None)
                if opp_val is None:
                    setattr(value, "model_R4EComment47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MapKeyToInfoAttributes59(self):
        return self.__model_MapKeyToInfoAttributes59

    @model_MapKeyToInfoAttributes59.setter
    def model_MapKeyToInfoAttributes59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapKeyToInfoAttributes__model_MapKeyToInfoAttributes59", None)
        self.__model_MapKeyToInfoAttributes59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EFileContext58"):
                opp_val = getattr(old_value, "model_R4EFileContext58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EFileContext58"):
                opp_val = getattr(value, "model_R4EFileContext58", None)
                if opp_val is None:
                    setattr(value, "model_R4EFileContext58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MapKeyToInfoAttributes72(self):
        return self.__model_MapKeyToInfoAttributes72

    @model_MapKeyToInfoAttributes72.setter
    def model_MapKeyToInfoAttributes72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapKeyToInfoAttributes__model_MapKeyToInfoAttributes72", None)
        self.__model_MapKeyToInfoAttributes72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EFileVersion71"):
                opp_val = getattr(old_value, "model_R4EFileVersion71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EFileVersion71"):
                opp_val = getattr(value, "model_R4EFileVersion71", None)
                if opp_val is None:
                    setattr(value, "model_R4EFileVersion71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MapKeyToInfoAttributes(self):
        return self.__model_MapKeyToInfoAttributes

    @model_MapKeyToInfoAttributes.setter
    def model_MapKeyToInfoAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapKeyToInfoAttributes__model_MapKeyToInfoAttributes", None)
        self.__model_MapKeyToInfoAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EItem42"):
                opp_val = getattr(old_value, "model_R4EItem42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EItem42"):
                opp_val = getattr(value, "model_R4EItem42", None)
                if opp_val is None:
                    setattr(value, "model_R4EItem42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CommentType:

    pass
class model_R4ECommentType(CommentType):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class R4EUser:

    pass
class Item:

    pass
class R4EIDComponent:

    pass
class model_R4EFileContext(R4EIDComponent):

    def __init__(self, type: str, model_R4EFileContext: "model_R4EItem" = None, model_R4EFileContext50: set["model_R4EDelta"] = None, model_R4EFileContext52: "model_R4EFileVersion" = None, model_R4EFileContext55: "model_R4EFileVersion" = None, model_R4EFileContext58: set["model_MapKeyToInfoAttributes"] = None):
        self.type = type
        self.model_R4EFileContext = model_R4EFileContext
        self.model_R4EFileContext50 = model_R4EFileContext50 if model_R4EFileContext50 is not None else set()
        self.model_R4EFileContext52 = model_R4EFileContext52
        self.model_R4EFileContext55 = model_R4EFileContext55
        self.model_R4EFileContext58 = model_R4EFileContext58 if model_R4EFileContext58 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def model_R4EFileContext(self):
        return self.__model_R4EFileContext

    @model_R4EFileContext.setter
    def model_R4EFileContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EFileContext__model_R4EFileContext", None)
        self.__model_R4EFileContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EItem40"):
                opp_val = getattr(old_value, "model_R4EItem40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EItem40"):
                opp_val = getattr(value, "model_R4EItem40", None)
                if opp_val is None:
                    setattr(value, "model_R4EItem40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_R4EFileContext58(self):
        return self.__model_R4EFileContext58

    @model_R4EFileContext58.setter
    def model_R4EFileContext58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EFileContext__model_R4EFileContext58", None)
        self.__model_R4EFileContext58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MapKeyToInfoAttributes59"):
                    opp_val = getattr(item, "model_MapKeyToInfoAttributes59", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MapKeyToInfoAttributes59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MapKeyToInfoAttributes59"):
                    opp_val = getattr(item, "model_MapKeyToInfoAttributes59", None)
                    
                    setattr(item, "model_MapKeyToInfoAttributes59", self)
                    

    @property
    def model_R4EFileContext50(self):
        return self.__model_R4EFileContext50

    @model_R4EFileContext50.setter
    def model_R4EFileContext50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EFileContext__model_R4EFileContext50", None)
        self.__model_R4EFileContext50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_R4EDelta"):
                    opp_val = getattr(item, "model_R4EDelta", None)
                    
                    if opp_val == self:
                        setattr(item, "model_R4EDelta", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_R4EDelta"):
                    opp_val = getattr(item, "model_R4EDelta", None)
                    
                    setattr(item, "model_R4EDelta", self)
                    

    @property
    def model_R4EFileContext55(self):
        return self.__model_R4EFileContext55

    @model_R4EFileContext55.setter
    def model_R4EFileContext55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EFileContext__model_R4EFileContext55", None)
        self.__model_R4EFileContext55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EFileVersion56"):
                opp_val = getattr(old_value, "model_R4EFileVersion56", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EFileVersion56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EFileVersion56"):
                opp_val = getattr(value, "model_R4EFileVersion56", None)
                setattr(value, "model_R4EFileVersion56", self)

    @property
    def model_R4EFileContext52(self):
        return self.__model_R4EFileContext52

    @model_R4EFileContext52.setter
    def model_R4EFileContext52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EFileContext__model_R4EFileContext52", None)
        self.__model_R4EFileContext52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EFileVersion53"):
                opp_val = getattr(old_value, "model_R4EFileVersion53", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EFileVersion53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EFileVersion53"):
                opp_val = getattr(value, "model_R4EFileVersion53", None)
                setattr(value, "model_R4EFileVersion53", self)

class model_R4EDelta(R4EIDComponent):

    pass
class model_MapDateToDuration:

    def __init__(self, key: date, value: str, model_MapDateToDuration: "model_R4EParticipant" = None):
        self.key = key
        self.value = value
        self.model_MapDateToDuration = model_MapDateToDuration
        
    @property
    def key(self) -> date:
        return self.__key

    @key.setter
    def key(self, key: date):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def model_MapDateToDuration(self):
        return self.__model_MapDateToDuration

    @model_MapDateToDuration.setter
    def model_MapDateToDuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapDateToDuration__model_MapDateToDuration", None)
        self.__model_MapDateToDuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EParticipant38"):
                opp_val = getattr(old_value, "model_R4EParticipant38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EParticipant38"):
                opp_val = getattr(value, "model_R4EParticipant38", None)
                if opp_val is None:
                    setattr(value, "model_R4EParticipant38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_R4EID:

    def __init__(self, sequenceID: int, userID: str, model_R4EID: "model_R4EParticipant" = None, model_R4EID85: "model_R4EIDComponent" = None, model_R4EID88: "model_MapIDToComponent" = None):
        self.sequenceID = sequenceID
        self.userID = userID
        self.model_R4EID = model_R4EID
        self.model_R4EID85 = model_R4EID85
        self.model_R4EID88 = model_R4EID88
        
    @property
    def userID(self) -> str:
        return self.__userID

    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID

    @property
    def sequenceID(self) -> int:
        return self.__sequenceID

    @sequenceID.setter
    def sequenceID(self, sequenceID: int):
        self.__sequenceID = sequenceID

    @property
    def model_R4EID(self):
        return self.__model_R4EID

    @model_R4EID.setter
    def model_R4EID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EID__model_R4EID", None)
        self.__model_R4EID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EParticipant36"):
                opp_val = getattr(old_value, "model_R4EParticipant36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EParticipant36"):
                opp_val = getattr(value, "model_R4EParticipant36", None)
                if opp_val is None:
                    setattr(value, "model_R4EParticipant36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_R4EID88(self):
        return self.__model_R4EID88

    @model_R4EID88.setter
    def model_R4EID88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EID__model_R4EID88", None)
        self.__model_R4EID88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MapIDToComponent87"):
                opp_val = getattr(old_value, "model_MapIDToComponent87", None)
                if opp_val == self:
                    setattr(old_value, "model_MapIDToComponent87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MapIDToComponent87"):
                opp_val = getattr(value, "model_MapIDToComponent87", None)
                setattr(value, "model_MapIDToComponent87", self)

    @property
    def model_R4EID85(self):
        return self.__model_R4EID85

    @model_R4EID85.setter
    def model_R4EID85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EID__model_R4EID85", None)
        self.__model_R4EID85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EIDComponent"):
                opp_val = getattr(old_value, "model_R4EIDComponent", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EIDComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EIDComponent"):
                opp_val = getattr(value, "model_R4EIDComponent", None)
                setattr(value, "model_R4EIDComponent", self)

class User:

    pass
class model_R4EItem(R4EIDComponent, Item):

    def __init__(self, description: str, addedById: str, repositoryRef: str, ProjectURIs: str, authorRep: str, submitted: date, model_R4EItem: "model_R4EUser" = None, model_R4EItem40: set["model_R4EFileContext"] = None, model_R4EItem42: set["model_MapKeyToInfoAttributes"] = None):
        self.description = description
        self.addedById = addedById
        self.repositoryRef = repositoryRef
        self.ProjectURIs = ProjectURIs
        self.authorRep = authorRep
        self.submitted = submitted
        self.model_R4EItem = model_R4EItem
        self.model_R4EItem40 = model_R4EItem40 if model_R4EItem40 is not None else set()
        self.model_R4EItem42 = model_R4EItem42 if model_R4EItem42 is not None else set()
        
    @property
    def submitted(self) -> date:
        return self.__submitted

    @submitted.setter
    def submitted(self, submitted: date):
        self.__submitted = submitted

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def repositoryRef(self) -> str:
        return self.__repositoryRef

    @repositoryRef.setter
    def repositoryRef(self, repositoryRef: str):
        self.__repositoryRef = repositoryRef

    @property
    def authorRep(self) -> str:
        return self.__authorRep

    @authorRep.setter
    def authorRep(self, authorRep: str):
        self.__authorRep = authorRep

    @property
    def ProjectURIs(self) -> str:
        return self.__ProjectURIs

    @ProjectURIs.setter
    def ProjectURIs(self, ProjectURIs: str):
        self.__ProjectURIs = ProjectURIs

    @property
    def addedById(self) -> str:
        return self.__addedById

    @addedById.setter
    def addedById(self, addedById: str):
        self.__addedById = addedById

    @property
    def model_R4EItem40(self):
        return self.__model_R4EItem40

    @model_R4EItem40.setter
    def model_R4EItem40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EItem__model_R4EItem40", None)
        self.__model_R4EItem40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_R4EFileContext"):
                    opp_val = getattr(item, "model_R4EFileContext", None)
                    
                    if opp_val == self:
                        setattr(item, "model_R4EFileContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_R4EFileContext"):
                    opp_val = getattr(item, "model_R4EFileContext", None)
                    
                    setattr(item, "model_R4EFileContext", self)
                    

    @property
    def model_R4EItem42(self):
        return self.__model_R4EItem42

    @model_R4EItem42.setter
    def model_R4EItem42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EItem__model_R4EItem42", None)
        self.__model_R4EItem42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MapKeyToInfoAttributes"):
                    opp_val = getattr(item, "model_MapKeyToInfoAttributes", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MapKeyToInfoAttributes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MapKeyToInfoAttributes"):
                    opp_val = getattr(item, "model_MapKeyToInfoAttributes", None)
                    
                    setattr(item, "model_MapKeyToInfoAttributes", self)
                    

    @property
    def model_R4EItem(self):
        return self.__model_R4EItem

    @model_R4EItem.setter
    def model_R4EItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EItem__model_R4EItem", None)
        self.__model_R4EItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EUser31"):
                opp_val = getattr(old_value, "model_R4EUser31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EUser31"):
                opp_val = getattr(value, "model_R4EUser31", None)
                if opp_val is None:
                    setattr(value, "model_R4EUser31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_R4EReviewPhaseInfo:

    def __init__(self, startDate: date, endDate: date, type: str, phaseOwnerID: str, model_R4EReviewPhaseInfo: "model_R4EFormalReview" = None, model_R4EReviewPhaseInfo27: "model_R4EFormalReview" = None):
        self.startDate = startDate
        self.endDate = endDate
        self.type = type
        self.phaseOwnerID = phaseOwnerID
        self.model_R4EReviewPhaseInfo = model_R4EReviewPhaseInfo
        self.model_R4EReviewPhaseInfo27 = model_R4EReviewPhaseInfo27
        
    @property
    def phaseOwnerID(self) -> str:
        return self.__phaseOwnerID

    @phaseOwnerID.setter
    def phaseOwnerID(self, phaseOwnerID: str):
        self.__phaseOwnerID = phaseOwnerID

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def model_R4EReviewPhaseInfo27(self):
        return self.__model_R4EReviewPhaseInfo27

    @model_R4EReviewPhaseInfo27.setter
    def model_R4EReviewPhaseInfo27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReviewPhaseInfo__model_R4EReviewPhaseInfo27", None)
        self.__model_R4EReviewPhaseInfo27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EFormalReview26"):
                opp_val = getattr(old_value, "model_R4EFormalReview26", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EFormalReview26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EFormalReview26"):
                opp_val = getattr(value, "model_R4EFormalReview26", None)
                setattr(value, "model_R4EFormalReview26", self)

    @property
    def model_R4EReviewPhaseInfo(self):
        return self.__model_R4EReviewPhaseInfo

    @model_R4EReviewPhaseInfo.setter
    def model_R4EReviewPhaseInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReviewPhaseInfo__model_R4EReviewPhaseInfo", None)
        self.__model_R4EReviewPhaseInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EFormalReview24"):
                opp_val = getattr(old_value, "model_R4EFormalReview24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EFormalReview24"):
                opp_val = getattr(value, "model_R4EFormalReview24", None)
                if opp_val is None:
                    setattr(value, "model_R4EFormalReview24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class R4EPosition:

    pass
class model_R4ETextPosition(R4EPosition):

    def __init__(self, startPosition: int, length: int, startLine: int, endLine: int):
        self.startPosition = startPosition
        self.length = length
        self.startLine = startLine
        self.endLine = endLine
        
    @property
    def startPosition(self) -> int:
        return self.__startPosition

    @startPosition.setter
    def startPosition(self, startPosition: int):
        self.__startPosition = startPosition

    @property
    def endLine(self) -> int:
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: int):
        self.__endLine = endLine

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def startLine(self) -> int:
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: int):
        self.__startLine = startLine

class model_R4EParticipant(R4EUser):

    def __init__(self, isPartOfDecision: bool, roles: str, focusArea: str, model_R4EParticipant: "model_R4EFormalReview" = None, model_R4EParticipant36: set["model_R4EID"] = None, model_R4EParticipant38: set["model_MapDateToDuration"] = None):
        self.isPartOfDecision = isPartOfDecision
        self.roles = roles
        self.focusArea = focusArea
        self.model_R4EParticipant = model_R4EParticipant
        self.model_R4EParticipant36 = model_R4EParticipant36 if model_R4EParticipant36 is not None else set()
        self.model_R4EParticipant38 = model_R4EParticipant38 if model_R4EParticipant38 is not None else set()
        
    @property
    def isPartOfDecision(self) -> bool:
        return self.__isPartOfDecision

    @isPartOfDecision.setter
    def isPartOfDecision(self, isPartOfDecision: bool):
        self.__isPartOfDecision = isPartOfDecision

    @property
    def focusArea(self) -> str:
        return self.__focusArea

    @focusArea.setter
    def focusArea(self, focusArea: str):
        self.__focusArea = focusArea

    @property
    def roles(self) -> str:
        return self.__roles

    @roles.setter
    def roles(self, roles: str):
        self.__roles = roles

    @property
    def model_R4EParticipant(self):
        return self.__model_R4EParticipant

    @model_R4EParticipant.setter
    def model_R4EParticipant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EParticipant__model_R4EParticipant", None)
        self.__model_R4EParticipant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EFormalReview"):
                opp_val = getattr(old_value, "model_R4EFormalReview", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EFormalReview", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EFormalReview"):
                opp_val = getattr(value, "model_R4EFormalReview", None)
                setattr(value, "model_R4EFormalReview", self)

    @property
    def model_R4EParticipant38(self):
        return self.__model_R4EParticipant38

    @model_R4EParticipant38.setter
    def model_R4EParticipant38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EParticipant__model_R4EParticipant38", None)
        self.__model_R4EParticipant38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MapDateToDuration"):
                    opp_val = getattr(item, "model_MapDateToDuration", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MapDateToDuration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MapDateToDuration"):
                    opp_val = getattr(item, "model_MapDateToDuration", None)
                    
                    setattr(item, "model_MapDateToDuration", self)
                    

    @property
    def model_R4EParticipant36(self):
        return self.__model_R4EParticipant36

    @model_R4EParticipant36.setter
    def model_R4EParticipant36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EParticipant__model_R4EParticipant36", None)
        self.__model_R4EParticipant36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_R4EID"):
                    opp_val = getattr(item, "model_R4EID", None)
                    
                    if opp_val == self:
                        setattr(item, "model_R4EID", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_R4EID"):
                    opp_val = getattr(item, "model_R4EID", None)
                    
                    setattr(item, "model_R4EID", self)
                    

class R4EReview:

    pass
class model_R4EFormalReview(R4EReview):

    pass
class model_R4EFileVersion:

    def __init__(self, platformURI: str, versionID: str, repositoryPath: str, name: str, resource: str, localVersionID: str, fileRevision: str, model_R4EFileVersion: "model_R4EAnomaly" = None, model_R4EFileVersion53: "model_R4EFileContext" = None, model_R4EFileVersion56: "model_R4EFileContext" = None, model_R4EFileVersion71: set["model_MapKeyToInfoAttributes"] = None, model_R4EFileVersion96: "model_R4EAnomalyTextPosition" = None):
        self.platformURI = platformURI
        self.versionID = versionID
        self.repositoryPath = repositoryPath
        self.name = name
        self.resource = resource
        self.localVersionID = localVersionID
        self.fileRevision = fileRevision
        self.model_R4EFileVersion = model_R4EFileVersion
        self.model_R4EFileVersion53 = model_R4EFileVersion53
        self.model_R4EFileVersion56 = model_R4EFileVersion56
        self.model_R4EFileVersion71 = model_R4EFileVersion71 if model_R4EFileVersion71 is not None else set()
        self.model_R4EFileVersion96 = model_R4EFileVersion96
        
    @property
    def repositoryPath(self) -> str:
        return self.__repositoryPath

    @repositoryPath.setter
    def repositoryPath(self, repositoryPath: str):
        self.__repositoryPath = repositoryPath

    @property
    def platformURI(self) -> str:
        return self.__platformURI

    @platformURI.setter
    def platformURI(self, platformURI: str):
        self.__platformURI = platformURI

    @property
    def localVersionID(self) -> str:
        return self.__localVersionID

    @localVersionID.setter
    def localVersionID(self, localVersionID: str):
        self.__localVersionID = localVersionID

    @property
    def resource(self) -> str:
        return self.__resource

    @resource.setter
    def resource(self, resource: str):
        self.__resource = resource

    @property
    def fileRevision(self) -> str:
        return self.__fileRevision

    @fileRevision.setter
    def fileRevision(self, fileRevision: str):
        self.__fileRevision = fileRevision

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def versionID(self) -> str:
        return self.__versionID

    @versionID.setter
    def versionID(self, versionID: str):
        self.__versionID = versionID

    @property
    def model_R4EFileVersion56(self):
        return self.__model_R4EFileVersion56

    @model_R4EFileVersion56.setter
    def model_R4EFileVersion56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EFileVersion__model_R4EFileVersion56", None)
        self.__model_R4EFileVersion56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EFileContext55"):
                opp_val = getattr(old_value, "model_R4EFileContext55", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EFileContext55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EFileContext55"):
                opp_val = getattr(value, "model_R4EFileContext55", None)
                setattr(value, "model_R4EFileContext55", self)

    @property
    def model_R4EFileVersion53(self):
        return self.__model_R4EFileVersion53

    @model_R4EFileVersion53.setter
    def model_R4EFileVersion53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EFileVersion__model_R4EFileVersion53", None)
        self.__model_R4EFileVersion53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EFileContext52"):
                opp_val = getattr(old_value, "model_R4EFileContext52", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EFileContext52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EFileContext52"):
                opp_val = getattr(value, "model_R4EFileContext52", None)
                setattr(value, "model_R4EFileContext52", self)

    @property
    def model_R4EFileVersion71(self):
        return self.__model_R4EFileVersion71

    @model_R4EFileVersion71.setter
    def model_R4EFileVersion71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EFileVersion__model_R4EFileVersion71", None)
        self.__model_R4EFileVersion71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MapKeyToInfoAttributes72"):
                    opp_val = getattr(item, "model_MapKeyToInfoAttributes72", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MapKeyToInfoAttributes72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MapKeyToInfoAttributes72"):
                    opp_val = getattr(item, "model_MapKeyToInfoAttributes72", None)
                    
                    setattr(item, "model_MapKeyToInfoAttributes72", self)
                    

    @property
    def model_R4EFileVersion(self):
        return self.__model_R4EFileVersion

    @model_R4EFileVersion.setter
    def model_R4EFileVersion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EFileVersion__model_R4EFileVersion", None)
        self.__model_R4EFileVersion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EAnomaly21"):
                opp_val = getattr(old_value, "model_R4EAnomaly21", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EAnomaly21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EAnomaly21"):
                opp_val = getattr(value, "model_R4EAnomaly21", None)
                setattr(value, "model_R4EAnomaly21", self)

    @property
    def model_R4EFileVersion96(self):
        return self.__model_R4EFileVersion96

    @model_R4EFileVersion96.setter
    def model_R4EFileVersion96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EFileVersion__model_R4EFileVersion96", None)
        self.__model_R4EFileVersion96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EAnomalyTextPosition"):
                opp_val = getattr(old_value, "model_R4EAnomalyTextPosition", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EAnomalyTextPosition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EAnomalyTextPosition"):
                opp_val = getattr(value, "model_R4EAnomalyTextPosition", None)
                setattr(value, "model_R4EAnomalyTextPosition", self)

class model_R4EDesignRule:

    pass
class Topic:

    pass
class model_R4EMeetingData:

    def __init__(self, id: str, subject: str, location: str, startTime: str, duration: int, sentCount: int, sender: str, receivers: str, body: str, model_R4EMeetingData: "model_R4EReview" = None):
        self.id = id
        self.subject = subject
        self.location = location
        self.startTime = startTime
        self.duration = duration
        self.sentCount = sentCount
        self.sender = sender
        self.receivers = receivers
        self.body = body
        self.model_R4EMeetingData = model_R4EMeetingData
        
    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def receivers(self) -> str:
        return self.__receivers

    @receivers.setter
    def receivers(self, receivers: str):
        self.__receivers = receivers

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def startTime(self) -> str:
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime: str):
        self.__startTime = startTime

    @property
    def sender(self) -> str:
        return self.__sender

    @sender.setter
    def sender(self, sender: str):
        self.__sender = sender

    @property
    def sentCount(self) -> int:
        return self.__sentCount

    @sentCount.setter
    def sentCount(self, sentCount: int):
        self.__sentCount = sentCount

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def model_R4EMeetingData(self):
        return self.__model_R4EMeetingData

    @model_R4EMeetingData.setter
    def model_R4EMeetingData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EMeetingData__model_R4EMeetingData", None)
        self.__model_R4EMeetingData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReview17"):
                opp_val = getattr(old_value, "model_R4EReview17", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EReview17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReview17"):
                opp_val = getattr(value, "model_R4EReview17", None)
                setattr(value, "model_R4EReview17", self)

class model_MapIDToComponent:

    pass
class R4EComment:

    pass
class model_MapToUsers:

    def __init__(self, key: str, model_MapToUsers: "model_R4EReview" = None, model_MapToUsers77: "model_R4EUser" = None):
        self.key = key
        self.model_MapToUsers = model_MapToUsers
        self.model_MapToUsers77 = model_MapToUsers77
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_MapToUsers77(self):
        return self.__model_MapToUsers77

    @model_MapToUsers77.setter
    def model_MapToUsers77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapToUsers__model_MapToUsers77", None)
        self.__model_MapToUsers77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EUser78"):
                opp_val = getattr(old_value, "model_R4EUser78", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EUser78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EUser78"):
                opp_val = getattr(value, "model_R4EUser78", None)
                setattr(value, "model_R4EUser78", self)

    @property
    def model_MapToUsers(self):
        return self.__model_MapToUsers

    @model_MapToUsers.setter
    def model_MapToUsers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapToUsers__model_MapToUsers", None)
        self.__model_MapToUsers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReview11"):
                opp_val = getattr(old_value, "model_R4EReview11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReview11"):
                opp_val = getattr(value, "model_R4EReview11", None)
                if opp_val is None:
                    setattr(value, "model_R4EReview11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Review:

    pass
class model_MapUserIDToUserReviews:

    def __init__(self, key: str, model_MapUserIDToUserReviews: "model_R4EReviewGroup" = None, model_MapUserIDToUserReviews93: "model_R4EUserReviews" = None):
        self.key = key
        self.model_MapUserIDToUserReviews = model_MapUserIDToUserReviews
        self.model_MapUserIDToUserReviews93 = model_MapUserIDToUserReviews93
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_MapUserIDToUserReviews(self):
        return self.__model_MapUserIDToUserReviews

    @model_MapUserIDToUserReviews.setter
    def model_MapUserIDToUserReviews(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapUserIDToUserReviews__model_MapUserIDToUserReviews", None)
        self.__model_MapUserIDToUserReviews = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReviewGroup6"):
                opp_val = getattr(old_value, "model_R4EReviewGroup6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReviewGroup6"):
                opp_val = getattr(value, "model_R4EReviewGroup6", None)
                if opp_val is None:
                    setattr(value, "model_R4EReviewGroup6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MapUserIDToUserReviews93(self):
        return self.__model_MapUserIDToUserReviews93

    @model_MapUserIDToUserReviews93.setter
    def model_MapUserIDToUserReviews93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapUserIDToUserReviews__model_MapUserIDToUserReviews93", None)
        self.__model_MapUserIDToUserReviews93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EUserReviews94"):
                opp_val = getattr(old_value, "model_R4EUserReviews94", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EUserReviews94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EUserReviews94"):
                opp_val = getattr(value, "model_R4EUserReviews94", None)
                setattr(value, "model_R4EUserReviews94", self)

class model_MapNameToReview:

    def __init__(self, key: str, model_MapNameToReview: "model_R4EReviewGroup" = None, model_MapNameToReview74: "model_R4EReview" = None, model_MapNameToReview80: "model_R4EUserReviews" = None):
        self.key = key
        self.model_MapNameToReview = model_MapNameToReview
        self.model_MapNameToReview74 = model_MapNameToReview74
        self.model_MapNameToReview80 = model_MapNameToReview80
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_MapNameToReview80(self):
        return self.__model_MapNameToReview80

    @model_MapNameToReview80.setter
    def model_MapNameToReview80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapNameToReview__model_MapNameToReview80", None)
        self.__model_MapNameToReview80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EUserReviews"):
                opp_val = getattr(old_value, "model_R4EUserReviews", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EUserReviews"):
                opp_val = getattr(value, "model_R4EUserReviews", None)
                if opp_val is None:
                    setattr(value, "model_R4EUserReviews", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MapNameToReview(self):
        return self.__model_MapNameToReview

    @model_MapNameToReview.setter
    def model_MapNameToReview(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapNameToReview__model_MapNameToReview", None)
        self.__model_MapNameToReview = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReviewGroup4"):
                opp_val = getattr(old_value, "model_R4EReviewGroup4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReviewGroup4"):
                opp_val = getattr(value, "model_R4EReviewGroup4", None)
                if opp_val is None:
                    setattr(value, "model_R4EReviewGroup4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MapNameToReview74(self):
        return self.__model_MapNameToReview74

    @model_MapNameToReview74.setter
    def model_MapNameToReview74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapNameToReview__model_MapNameToReview74", None)
        self.__model_MapNameToReview74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReview75"):
                opp_val = getattr(old_value, "model_R4EReview75", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EReview75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReview75"):
                opp_val = getattr(value, "model_R4EReview75", None)
                setattr(value, "model_R4EReview75", self)

class model_R4EReviewDecision:

    def __init__(self, spentTime: int, value: str, model_R4EReviewDecision: "model_R4EReview" = None):
        self.spentTime = spentTime
        self.value = value
        self.model_R4EReviewDecision = model_R4EReviewDecision
        
    @property
    def spentTime(self) -> int:
        return self.__spentTime

    @spentTime.setter
    def spentTime(self, spentTime: int):
        self.__spentTime = spentTime

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def model_R4EReviewDecision(self):
        return self.__model_R4EReviewDecision

    @model_R4EReviewDecision.setter
    def model_R4EReviewDecision(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReviewDecision__model_R4EReviewDecision", None)
        self.__model_R4EReviewDecision = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReview"):
                opp_val = getattr(old_value, "model_R4EReview", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EReview", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReview"):
                opp_val = getattr(value, "model_R4EReview", None)
                setattr(value, "model_R4EReview", self)

class R4EReviewComponent:

    pass
class model_R4EComment(R4EIDComponent, R4EReviewComponent, Comment):

    def __init__(self, createdOn: date, model_R4EComment: "model_R4EUser" = None, model_R4EComment44: "model_R4EAnomaly" = None, model_R4EComment47: set["model_MapKeyToInfoAttributes"] = None):
        self.createdOn = createdOn
        self.model_R4EComment = model_R4EComment
        self.model_R4EComment44 = model_R4EComment44
        self.model_R4EComment47 = model_R4EComment47 if model_R4EComment47 is not None else set()
        
    @property
    def createdOn(self) -> date:
        return self.__createdOn

    @createdOn.setter
    def createdOn(self, createdOn: date):
        self.__createdOn = createdOn

    @property
    def model_R4EComment44(self):
        return self.__model_R4EComment44

    @model_R4EComment44.setter
    def model_R4EComment44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EComment__model_R4EComment44", None)
        self.__model_R4EComment44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EAnomaly45"):
                opp_val = getattr(old_value, "model_R4EAnomaly45", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EAnomaly45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EAnomaly45"):
                opp_val = getattr(value, "model_R4EAnomaly45", None)
                setattr(value, "model_R4EAnomaly45", self)

    @property
    def model_R4EComment(self):
        return self.__model_R4EComment

    @model_R4EComment.setter
    def model_R4EComment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EComment__model_R4EComment", None)
        self.__model_R4EComment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EUser29"):
                opp_val = getattr(old_value, "model_R4EUser29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EUser29"):
                opp_val = getattr(value, "model_R4EUser29", None)
                if opp_val is None:
                    setattr(value, "model_R4EUser29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_R4EComment47(self):
        return self.__model_R4EComment47

    @model_R4EComment47.setter
    def model_R4EComment47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EComment__model_R4EComment47", None)
        self.__model_R4EComment47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MapKeyToInfoAttributes48"):
                    opp_val = getattr(item, "model_MapKeyToInfoAttributes48", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MapKeyToInfoAttributes48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MapKeyToInfoAttributes48"):
                    opp_val = getattr(item, "model_MapKeyToInfoAttributes48", None)
                    
                    setattr(item, "model_MapKeyToInfoAttributes48", self)
                    

class model_R4EUser(User, R4EReviewComponent):

    def __init__(self, groupPaths: str, sequenceIDCounter: int, reviewCreatedByMe: bool, reviewCompleted: bool, reviewCompletedCode: int, model_R4EUser: "model_R4EReview" = None, model_R4EUser29: set["model_R4EComment"] = None, model_R4EUser31: set["model_R4EItem"] = None, model_R4EUser33: "model_R4EReview" = None, model_R4EUser78: "model_MapToUsers" = None):
        self.groupPaths = groupPaths
        self.sequenceIDCounter = sequenceIDCounter
        self.reviewCreatedByMe = reviewCreatedByMe
        self.reviewCompleted = reviewCompleted
        self.reviewCompletedCode = reviewCompletedCode
        self.model_R4EUser = model_R4EUser
        self.model_R4EUser29 = model_R4EUser29 if model_R4EUser29 is not None else set()
        self.model_R4EUser31 = model_R4EUser31 if model_R4EUser31 is not None else set()
        self.model_R4EUser33 = model_R4EUser33
        self.model_R4EUser78 = model_R4EUser78
        
    @property
    def reviewCompleted(self) -> bool:
        return self.__reviewCompleted

    @reviewCompleted.setter
    def reviewCompleted(self, reviewCompleted: bool):
        self.__reviewCompleted = reviewCompleted

    @property
    def reviewCreatedByMe(self) -> bool:
        return self.__reviewCreatedByMe

    @reviewCreatedByMe.setter
    def reviewCreatedByMe(self, reviewCreatedByMe: bool):
        self.__reviewCreatedByMe = reviewCreatedByMe

    @property
    def groupPaths(self) -> str:
        return self.__groupPaths

    @groupPaths.setter
    def groupPaths(self, groupPaths: str):
        self.__groupPaths = groupPaths

    @property
    def reviewCompletedCode(self) -> int:
        return self.__reviewCompletedCode

    @reviewCompletedCode.setter
    def reviewCompletedCode(self, reviewCompletedCode: int):
        self.__reviewCompletedCode = reviewCompletedCode

    @property
    def sequenceIDCounter(self) -> int:
        return self.__sequenceIDCounter

    @sequenceIDCounter.setter
    def sequenceIDCounter(self, sequenceIDCounter: int):
        self.__sequenceIDCounter = sequenceIDCounter

    @property
    def model_R4EUser29(self):
        return self.__model_R4EUser29

    @model_R4EUser29.setter
    def model_R4EUser29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EUser__model_R4EUser29", None)
        self.__model_R4EUser29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_R4EComment"):
                    opp_val = getattr(item, "model_R4EComment", None)
                    
                    if opp_val == self:
                        setattr(item, "model_R4EComment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_R4EComment"):
                    opp_val = getattr(item, "model_R4EComment", None)
                    
                    setattr(item, "model_R4EComment", self)
                    

    @property
    def model_R4EUser31(self):
        return self.__model_R4EUser31

    @model_R4EUser31.setter
    def model_R4EUser31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EUser__model_R4EUser31", None)
        self.__model_R4EUser31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_R4EItem"):
                    opp_val = getattr(item, "model_R4EItem", None)
                    
                    if opp_val == self:
                        setattr(item, "model_R4EItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_R4EItem"):
                    opp_val = getattr(item, "model_R4EItem", None)
                    
                    setattr(item, "model_R4EItem", self)
                    

    @property
    def model_R4EUser78(self):
        return self.__model_R4EUser78

    @model_R4EUser78.setter
    def model_R4EUser78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EUser__model_R4EUser78", None)
        self.__model_R4EUser78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MapToUsers77"):
                opp_val = getattr(old_value, "model_MapToUsers77", None)
                if opp_val == self:
                    setattr(old_value, "model_MapToUsers77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MapToUsers77"):
                opp_val = getattr(value, "model_MapToUsers77", None)
                setattr(value, "model_MapToUsers77", self)

    @property
    def model_R4EUser(self):
        return self.__model_R4EUser

    @model_R4EUser.setter
    def model_R4EUser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EUser__model_R4EUser", None)
        self.__model_R4EUser = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReview13"):
                opp_val = getattr(old_value, "model_R4EReview13", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EReview13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReview13"):
                opp_val = getattr(value, "model_R4EReview13", None)
                setattr(value, "model_R4EReview13", self)

    @property
    def model_R4EUser33(self):
        return self.__model_R4EUser33

    @model_R4EUser33.setter
    def model_R4EUser33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EUser__model_R4EUser33", None)
        self.__model_R4EUser33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReview34"):
                opp_val = getattr(old_value, "model_R4EReview34", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EReview34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReview34"):
                opp_val = getattr(value, "model_R4EReview34", None)
                setattr(value, "model_R4EReview34", self)

class model_R4ETaskReference(TaskReference, R4EReviewComponent):

    pass
class model_R4EAnomaly(R4EReviewComponent, Topic, R4EComment):

    def __init__(self, state: str, dueDate: date, ruleID: str, decidedByID: str, fixedByID: str, followUpByID: str, rank: str, notAcceptedReason: str, isImported: bool, model_R4EAnomaly: "model_R4EReview" = None, model_R4EAnomaly19: "model_R4EDesignRule" = None, model_R4EAnomaly21: "model_R4EFileVersion" = None, model_R4EAnomaly45: "model_R4EComment" = None):
        self.state = state
        self.dueDate = dueDate
        self.ruleID = ruleID
        self.decidedByID = decidedByID
        self.fixedByID = fixedByID
        self.followUpByID = followUpByID
        self.rank = rank
        self.notAcceptedReason = notAcceptedReason
        self.isImported = isImported
        self.model_R4EAnomaly = model_R4EAnomaly
        self.model_R4EAnomaly19 = model_R4EAnomaly19
        self.model_R4EAnomaly21 = model_R4EAnomaly21
        self.model_R4EAnomaly45 = model_R4EAnomaly45
        
    @property
    def fixedByID(self) -> str:
        return self.__fixedByID

    @fixedByID.setter
    def fixedByID(self, fixedByID: str):
        self.__fixedByID = fixedByID

    @property
    def decidedByID(self) -> str:
        return self.__decidedByID

    @decidedByID.setter
    def decidedByID(self, decidedByID: str):
        self.__decidedByID = decidedByID

    @property
    def dueDate(self) -> date:
        return self.__dueDate

    @dueDate.setter
    def dueDate(self, dueDate: date):
        self.__dueDate = dueDate

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def followUpByID(self) -> str:
        return self.__followUpByID

    @followUpByID.setter
    def followUpByID(self, followUpByID: str):
        self.__followUpByID = followUpByID

    @property
    def isImported(self) -> bool:
        return self.__isImported

    @isImported.setter
    def isImported(self, isImported: bool):
        self.__isImported = isImported

    @property
    def rank(self) -> str:
        return self.__rank

    @rank.setter
    def rank(self, rank: str):
        self.__rank = rank

    @property
    def notAcceptedReason(self) -> str:
        return self.__notAcceptedReason

    @notAcceptedReason.setter
    def notAcceptedReason(self, notAcceptedReason: str):
        self.__notAcceptedReason = notAcceptedReason

    @property
    def ruleID(self) -> str:
        return self.__ruleID

    @ruleID.setter
    def ruleID(self, ruleID: str):
        self.__ruleID = ruleID

    @property
    def model_R4EAnomaly19(self):
        return self.__model_R4EAnomaly19

    @model_R4EAnomaly19.setter
    def model_R4EAnomaly19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EAnomaly__model_R4EAnomaly19", None)
        self.__model_R4EAnomaly19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EDesignRule"):
                opp_val = getattr(old_value, "model_R4EDesignRule", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EDesignRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EDesignRule"):
                opp_val = getattr(value, "model_R4EDesignRule", None)
                setattr(value, "model_R4EDesignRule", self)

    @property
    def model_R4EAnomaly45(self):
        return self.__model_R4EAnomaly45

    @model_R4EAnomaly45.setter
    def model_R4EAnomaly45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EAnomaly__model_R4EAnomaly45", None)
        self.__model_R4EAnomaly45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EComment44"):
                opp_val = getattr(old_value, "model_R4EComment44", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EComment44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EComment44"):
                opp_val = getattr(value, "model_R4EComment44", None)
                setattr(value, "model_R4EComment44", self)

    @property
    def model_R4EAnomaly(self):
        return self.__model_R4EAnomaly

    @model_R4EAnomaly.setter
    def model_R4EAnomaly(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EAnomaly__model_R4EAnomaly", None)
        self.__model_R4EAnomaly = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReview9"):
                opp_val = getattr(old_value, "model_R4EReview9", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EReview9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReview9"):
                opp_val = getattr(value, "model_R4EReview9", None)
                setattr(value, "model_R4EReview9", self)

    @property
    def model_R4EAnomaly21(self):
        return self.__model_R4EAnomaly21

    @model_R4EAnomaly21.setter
    def model_R4EAnomaly21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EAnomaly__model_R4EAnomaly21", None)
        self.__model_R4EAnomaly21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EFileVersion"):
                opp_val = getattr(old_value, "model_R4EFileVersion", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EFileVersion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EFileVersion"):
                opp_val = getattr(value, "model_R4EFileVersion", None)
                setattr(value, "model_R4EFileVersion", self)

class model_R4EIDComponent(R4EReviewComponent):

    pass
class model_R4EReview(R4EReviewComponent, Review):

    def __init__(self, referenceMaterial: str, startDate: date, name: str, project: str, components: str, entryCriteria: str, extraNotes: str, objectives: str, endDate: date, dueDate: date, type: str, modifiedDate: date, model_R4EReview: "model_R4EReviewDecision" = None, model_R4EReview13: "model_R4EUser" = None, model_R4EReview9: "model_R4EAnomaly" = None, model_R4EReview11: set["model_MapToUsers"] = None, model_R4EReview15: set["model_MapIDToComponent"] = None, model_R4EReview17: "model_R4EMeetingData" = None, model_R4EReview34: "model_R4EUser" = None, model_R4EReview75: "model_MapNameToReview" = None):
        self.referenceMaterial = referenceMaterial
        self.startDate = startDate
        self.name = name
        self.project = project
        self.components = components
        self.entryCriteria = entryCriteria
        self.extraNotes = extraNotes
        self.objectives = objectives
        self.endDate = endDate
        self.dueDate = dueDate
        self.type = type
        self.modifiedDate = modifiedDate
        self.model_R4EReview = model_R4EReview
        self.model_R4EReview13 = model_R4EReview13
        self.model_R4EReview9 = model_R4EReview9
        self.model_R4EReview11 = model_R4EReview11 if model_R4EReview11 is not None else set()
        self.model_R4EReview15 = model_R4EReview15 if model_R4EReview15 is not None else set()
        self.model_R4EReview17 = model_R4EReview17
        self.model_R4EReview34 = model_R4EReview34
        self.model_R4EReview75 = model_R4EReview75
        
    @property
    def modifiedDate(self) -> date:
        return self.__modifiedDate

    @modifiedDate.setter
    def modifiedDate(self, modifiedDate: date):
        self.__modifiedDate = modifiedDate

    @property
    def entryCriteria(self) -> str:
        return self.__entryCriteria

    @entryCriteria.setter
    def entryCriteria(self, entryCriteria: str):
        self.__entryCriteria = entryCriteria

    @property
    def project(self) -> str:
        return self.__project

    @project.setter
    def project(self, project: str):
        self.__project = project

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def objectives(self) -> str:
        return self.__objectives

    @objectives.setter
    def objectives(self, objectives: str):
        self.__objectives = objectives

    @property
    def components(self) -> str:
        return self.__components

    @components.setter
    def components(self, components: str):
        self.__components = components

    @property
    def referenceMaterial(self) -> str:
        return self.__referenceMaterial

    @referenceMaterial.setter
    def referenceMaterial(self, referenceMaterial: str):
        self.__referenceMaterial = referenceMaterial

    @property
    def extraNotes(self) -> str:
        return self.__extraNotes

    @extraNotes.setter
    def extraNotes(self, extraNotes: str):
        self.__extraNotes = extraNotes

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def dueDate(self) -> date:
        return self.__dueDate

    @dueDate.setter
    def dueDate(self, dueDate: date):
        self.__dueDate = dueDate

    @property
    def model_R4EReview34(self):
        return self.__model_R4EReview34

    @model_R4EReview34.setter
    def model_R4EReview34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReview__model_R4EReview34", None)
        self.__model_R4EReview34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EUser33"):
                opp_val = getattr(old_value, "model_R4EUser33", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EUser33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EUser33"):
                opp_val = getattr(value, "model_R4EUser33", None)
                setattr(value, "model_R4EUser33", self)

    @property
    def model_R4EReview75(self):
        return self.__model_R4EReview75

    @model_R4EReview75.setter
    def model_R4EReview75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReview__model_R4EReview75", None)
        self.__model_R4EReview75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MapNameToReview74"):
                opp_val = getattr(old_value, "model_MapNameToReview74", None)
                if opp_val == self:
                    setattr(old_value, "model_MapNameToReview74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MapNameToReview74"):
                opp_val = getattr(value, "model_MapNameToReview74", None)
                setattr(value, "model_MapNameToReview74", self)

    @property
    def model_R4EReview15(self):
        return self.__model_R4EReview15

    @model_R4EReview15.setter
    def model_R4EReview15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReview__model_R4EReview15", None)
        self.__model_R4EReview15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MapIDToComponent"):
                    opp_val = getattr(item, "model_MapIDToComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MapIDToComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MapIDToComponent"):
                    opp_val = getattr(item, "model_MapIDToComponent", None)
                    
                    setattr(item, "model_MapIDToComponent", self)
                    

    @property
    def model_R4EReview13(self):
        return self.__model_R4EReview13

    @model_R4EReview13.setter
    def model_R4EReview13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReview__model_R4EReview13", None)
        self.__model_R4EReview13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EUser"):
                opp_val = getattr(old_value, "model_R4EUser", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EUser", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EUser"):
                opp_val = getattr(value, "model_R4EUser", None)
                setattr(value, "model_R4EUser", self)

    @property
    def model_R4EReview11(self):
        return self.__model_R4EReview11

    @model_R4EReview11.setter
    def model_R4EReview11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReview__model_R4EReview11", None)
        self.__model_R4EReview11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MapToUsers"):
                    opp_val = getattr(item, "model_MapToUsers", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MapToUsers", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MapToUsers"):
                    opp_val = getattr(item, "model_MapToUsers", None)
                    
                    setattr(item, "model_MapToUsers", self)
                    

    @property
    def model_R4EReview9(self):
        return self.__model_R4EReview9

    @model_R4EReview9.setter
    def model_R4EReview9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReview__model_R4EReview9", None)
        self.__model_R4EReview9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EAnomaly"):
                opp_val = getattr(old_value, "model_R4EAnomaly", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EAnomaly", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EAnomaly"):
                opp_val = getattr(value, "model_R4EAnomaly", None)
                setattr(value, "model_R4EAnomaly", self)

    @property
    def model_R4EReview(self):
        return self.__model_R4EReview

    @model_R4EReview.setter
    def model_R4EReview(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReview__model_R4EReview", None)
        self.__model_R4EReview = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReviewDecision"):
                opp_val = getattr(old_value, "model_R4EReviewDecision", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EReviewDecision", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReviewDecision"):
                opp_val = getattr(value, "model_R4EReviewDecision", None)
                setattr(value, "model_R4EReviewDecision", self)

    @property
    def model_R4EReview17(self):
        return self.__model_R4EReview17

    @model_R4EReview17.setter
    def model_R4EReview17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReview__model_R4EReview17", None)
        self.__model_R4EReview17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EMeetingData"):
                opp_val = getattr(old_value, "model_R4EMeetingData", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EMeetingData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EMeetingData"):
                opp_val = getattr(value, "model_R4EMeetingData", None)
                setattr(value, "model_R4EMeetingData", self)

class ReviewGroup:

    pass
class model_R4EReviewGroup(ReviewGroup, R4EReviewComponent):

    def __init__(self, availableProjects: str, availableComponents: str, designRuleLocations: str, name: str, folder: str, defaultEntryCriteria: str, model_R4EReviewGroup: set["model_R4EAnomalyType"] = None, model_R4EReviewGroup2: set["model_MapToAnomalyType"] = None, model_R4EReviewGroup4: set["model_MapNameToReview"] = None, model_R4EReviewGroup6: set["model_MapUserIDToUserReviews"] = None, model_R4EReviewGroup83: "model_R4EUserReviews" = None):
        self.availableProjects = availableProjects
        self.availableComponents = availableComponents
        self.designRuleLocations = designRuleLocations
        self.name = name
        self.folder = folder
        self.defaultEntryCriteria = defaultEntryCriteria
        self.model_R4EReviewGroup = model_R4EReviewGroup if model_R4EReviewGroup is not None else set()
        self.model_R4EReviewGroup2 = model_R4EReviewGroup2 if model_R4EReviewGroup2 is not None else set()
        self.model_R4EReviewGroup4 = model_R4EReviewGroup4 if model_R4EReviewGroup4 is not None else set()
        self.model_R4EReviewGroup6 = model_R4EReviewGroup6 if model_R4EReviewGroup6 is not None else set()
        self.model_R4EReviewGroup83 = model_R4EReviewGroup83
        
    @property
    def designRuleLocations(self) -> str:
        return self.__designRuleLocations

    @designRuleLocations.setter
    def designRuleLocations(self, designRuleLocations: str):
        self.__designRuleLocations = designRuleLocations

    @property
    def folder(self) -> str:
        return self.__folder

    @folder.setter
    def folder(self, folder: str):
        self.__folder = folder

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def defaultEntryCriteria(self) -> str:
        return self.__defaultEntryCriteria

    @defaultEntryCriteria.setter
    def defaultEntryCriteria(self, defaultEntryCriteria: str):
        self.__defaultEntryCriteria = defaultEntryCriteria

    @property
    def availableProjects(self) -> str:
        return self.__availableProjects

    @availableProjects.setter
    def availableProjects(self, availableProjects: str):
        self.__availableProjects = availableProjects

    @property
    def availableComponents(self) -> str:
        return self.__availableComponents

    @availableComponents.setter
    def availableComponents(self, availableComponents: str):
        self.__availableComponents = availableComponents

    @property
    def model_R4EReviewGroup2(self):
        return self.__model_R4EReviewGroup2

    @model_R4EReviewGroup2.setter
    def model_R4EReviewGroup2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReviewGroup__model_R4EReviewGroup2", None)
        self.__model_R4EReviewGroup2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MapToAnomalyType"):
                    opp_val = getattr(item, "model_MapToAnomalyType", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MapToAnomalyType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MapToAnomalyType"):
                    opp_val = getattr(item, "model_MapToAnomalyType", None)
                    
                    setattr(item, "model_MapToAnomalyType", self)
                    

    @property
    def model_R4EReviewGroup4(self):
        return self.__model_R4EReviewGroup4

    @model_R4EReviewGroup4.setter
    def model_R4EReviewGroup4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReviewGroup__model_R4EReviewGroup4", None)
        self.__model_R4EReviewGroup4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MapNameToReview"):
                    opp_val = getattr(item, "model_MapNameToReview", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MapNameToReview", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MapNameToReview"):
                    opp_val = getattr(item, "model_MapNameToReview", None)
                    
                    setattr(item, "model_MapNameToReview", self)
                    

    @property
    def model_R4EReviewGroup6(self):
        return self.__model_R4EReviewGroup6

    @model_R4EReviewGroup6.setter
    def model_R4EReviewGroup6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReviewGroup__model_R4EReviewGroup6", None)
        self.__model_R4EReviewGroup6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_MapUserIDToUserReviews"):
                    opp_val = getattr(item, "model_MapUserIDToUserReviews", None)
                    
                    if opp_val == self:
                        setattr(item, "model_MapUserIDToUserReviews", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_MapUserIDToUserReviews"):
                    opp_val = getattr(item, "model_MapUserIDToUserReviews", None)
                    
                    setattr(item, "model_MapUserIDToUserReviews", self)
                    

    @property
    def model_R4EReviewGroup(self):
        return self.__model_R4EReviewGroup

    @model_R4EReviewGroup.setter
    def model_R4EReviewGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReviewGroup__model_R4EReviewGroup", None)
        self.__model_R4EReviewGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_R4EAnomalyType"):
                    opp_val = getattr(item, "model_R4EAnomalyType", None)
                    
                    if opp_val == self:
                        setattr(item, "model_R4EAnomalyType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_R4EAnomalyType"):
                    opp_val = getattr(item, "model_R4EAnomalyType", None)
                    
                    setattr(item, "model_R4EAnomalyType", self)
                    

    @property
    def model_R4EReviewGroup83(self):
        return self.__model_R4EReviewGroup83

    @model_R4EReviewGroup83.setter
    def model_R4EReviewGroup83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EReviewGroup__model_R4EReviewGroup83", None)
        self.__model_R4EReviewGroup83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EUserReviews82"):
                opp_val = getattr(old_value, "model_R4EUserReviews82", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EUserReviews82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EUserReviews82"):
                opp_val = getattr(value, "model_R4EUserReviews82", None)
                setattr(value, "model_R4EUserReviews82", self)

class model_MapToAnomalyType:

    def __init__(self, key: str, model_MapToAnomalyType: "model_R4EReviewGroup" = None, model_MapToAnomalyType66: "model_R4EAnomalyType" = None):
        self.key = key
        self.model_MapToAnomalyType = model_MapToAnomalyType
        self.model_MapToAnomalyType66 = model_MapToAnomalyType66
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_MapToAnomalyType66(self):
        return self.__model_MapToAnomalyType66

    @model_MapToAnomalyType66.setter
    def model_MapToAnomalyType66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapToAnomalyType__model_MapToAnomalyType66", None)
        self.__model_MapToAnomalyType66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EAnomalyType67"):
                opp_val = getattr(old_value, "model_R4EAnomalyType67", None)
                if opp_val == self:
                    setattr(old_value, "model_R4EAnomalyType67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EAnomalyType67"):
                opp_val = getattr(value, "model_R4EAnomalyType67", None)
                setattr(value, "model_R4EAnomalyType67", self)

    @property
    def model_MapToAnomalyType(self):
        return self.__model_MapToAnomalyType

    @model_MapToAnomalyType.setter
    def model_MapToAnomalyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MapToAnomalyType__model_MapToAnomalyType", None)
        self.__model_MapToAnomalyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReviewGroup2"):
                opp_val = getattr(old_value, "model_R4EReviewGroup2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReviewGroup2"):
                opp_val = getattr(value, "model_R4EReviewGroup2", None)
                if opp_val is None:
                    setattr(value, "model_R4EReviewGroup2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_R4EAnomalyType(CommentType):

    def __init__(self, type: str, model_R4EAnomalyType: "model_R4EReviewGroup" = None, model_R4EAnomalyType67: "model_MapToAnomalyType" = None):
        self.type = type
        self.model_R4EAnomalyType = model_R4EAnomalyType
        self.model_R4EAnomalyType67 = model_R4EAnomalyType67
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def model_R4EAnomalyType67(self):
        return self.__model_R4EAnomalyType67

    @model_R4EAnomalyType67.setter
    def model_R4EAnomalyType67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EAnomalyType__model_R4EAnomalyType67", None)
        self.__model_R4EAnomalyType67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MapToAnomalyType66"):
                opp_val = getattr(old_value, "model_MapToAnomalyType66", None)
                if opp_val == self:
                    setattr(old_value, "model_MapToAnomalyType66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MapToAnomalyType66"):
                opp_val = getattr(value, "model_MapToAnomalyType66", None)
                setattr(value, "model_MapToAnomalyType66", self)

    @property
    def model_R4EAnomalyType(self):
        return self.__model_R4EAnomalyType

    @model_R4EAnomalyType.setter
    def model_R4EAnomalyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_R4EAnomalyType__model_R4EAnomalyType", None)
        self.__model_R4EAnomalyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_R4EReviewGroup"):
                opp_val = getattr(old_value, "model_R4EReviewGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_R4EReviewGroup"):
                opp_val = getattr(value, "model_R4EReviewGroup", None)
                if opp_val is None:
                    setattr(value, "model_R4EReviewGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
