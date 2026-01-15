from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StateType(Enum):
    initial = "initial"
    ongoing = "ongoing"
    final = "final"


############################################
# Definition of Classes
############################################

class research18_StateMachineVariable:

    pass
class research18_Action:

    def __init__(self, actionLabel: str, actionStatement: str, research18_Action: "research18_Transition" = None, research18_Action82: "research18_Action" = None, research18_Action81: "research18_State" = None, research18_Action84: "research18_Action" = None):
        self.actionLabel = actionLabel
        self.actionStatement = actionStatement
        self.research18_Action = research18_Action
        self.research18_Action82 = research18_Action82
        self.research18_Action81 = research18_Action81
        self.research18_Action84 = research18_Action84
        
    @property
    def actionLabel(self) -> str:
        return self.__actionLabel

    @actionLabel.setter
    def actionLabel(self, actionLabel: str):
        self.__actionLabel = actionLabel

    @property
    def actionStatement(self) -> str:
        return self.__actionStatement

    @actionStatement.setter
    def actionStatement(self, actionStatement: str):
        self.__actionStatement = actionStatement

    @property
    def research18_Action82(self):
        return self.__research18_Action82

    @research18_Action82.setter
    def research18_Action82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Action__research18_Action82", None)
        self.__research18_Action82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Action84"):
                opp_val = getattr(old_value, "research18_Action84", None)
                if opp_val == self:
                    setattr(old_value, "research18_Action84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Action84"):
                opp_val = getattr(value, "research18_Action84", None)
                setattr(value, "research18_Action84", self)

    @property
    def research18_Action81(self):
        return self.__research18_Action81

    @research18_Action81.setter
    def research18_Action81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Action__research18_Action81", None)
        self.__research18_Action81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_State80"):
                opp_val = getattr(old_value, "research18_State80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_State80"):
                opp_val = getattr(value, "research18_State80", None)
                if opp_val is None:
                    setattr(value, "research18_State80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research18_Action(self):
        return self.__research18_Action

    @research18_Action.setter
    def research18_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Action__research18_Action", None)
        self.__research18_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Transition"):
                opp_val = getattr(old_value, "research18_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Transition"):
                opp_val = getattr(value, "research18_Transition", None)
                if opp_val is None:
                    setattr(value, "research18_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research18_Action84(self):
        return self.__research18_Action84

    @research18_Action84.setter
    def research18_Action84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Action__research18_Action84", None)
        self.__research18_Action84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Action82"):
                opp_val = getattr(old_value, "research18_Action82", None)
                if opp_val == self:
                    setattr(old_value, "research18_Action82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Action82"):
                opp_val = getattr(value, "research18_Action82", None)
                setattr(value, "research18_Action82", self)

class StateMachineObject:

    pass
class research18_Transition(StateMachineObject):

    def __init__(self, guardLabel: str, guardExpression: str, research18_Transition: set["research18_Action"] = None, research18_Transition71: "research18_State" = None, research18_Transition74: "research18_State" = None, research18_Transition78: "research18_State" = None):
        self.guardLabel = guardLabel
        self.guardExpression = guardExpression
        self.research18_Transition = research18_Transition if research18_Transition is not None else set()
        self.research18_Transition71 = research18_Transition71
        self.research18_Transition74 = research18_Transition74
        self.research18_Transition78 = research18_Transition78
        
    @property
    def guardExpression(self) -> str:
        return self.__guardExpression

    @guardExpression.setter
    def guardExpression(self, guardExpression: str):
        self.__guardExpression = guardExpression

    @property
    def guardLabel(self) -> str:
        return self.__guardLabel

    @guardLabel.setter
    def guardLabel(self, guardLabel: str):
        self.__guardLabel = guardLabel

    @property
    def research18_Transition74(self):
        return self.__research18_Transition74

    @research18_Transition74.setter
    def research18_Transition74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Transition__research18_Transition74", None)
        self.__research18_Transition74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_State75"):
                opp_val = getattr(old_value, "research18_State75", None)
                if opp_val == self:
                    setattr(old_value, "research18_State75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_State75"):
                opp_val = getattr(value, "research18_State75", None)
                setattr(value, "research18_State75", self)

    @property
    def research18_Transition78(self):
        return self.__research18_Transition78

    @research18_Transition78.setter
    def research18_Transition78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Transition__research18_Transition78", None)
        self.__research18_Transition78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_State77"):
                opp_val = getattr(old_value, "research18_State77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_State77"):
                opp_val = getattr(value, "research18_State77", None)
                if opp_val is None:
                    setattr(value, "research18_State77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research18_Transition(self):
        return self.__research18_Transition

    @research18_Transition.setter
    def research18_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Transition__research18_Transition", None)
        self.__research18_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research18_Action"):
                    opp_val = getattr(item, "research18_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "research18_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research18_Action"):
                    opp_val = getattr(item, "research18_Action", None)
                    
                    setattr(item, "research18_Action", self)
                    

    @property
    def research18_Transition71(self):
        return self.__research18_Transition71

    @research18_Transition71.setter
    def research18_Transition71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Transition__research18_Transition71", None)
        self.__research18_Transition71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_State72"):
                opp_val = getattr(old_value, "research18_State72", None)
                if opp_val == self:
                    setattr(old_value, "research18_State72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_State72"):
                opp_val = getattr(value, "research18_State72", None)
                setattr(value, "research18_State72", self)

class research18_StateMachineObject(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class research18_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class research18_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class research18_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class research18_PublicationStatus:

    def __init__(self, label: str, research18_PublicationStatus: "research18_PublicationSystem" = None, research18_PublicationStatus67: set["research18_State"] = None, research18_PublicationStatus65: set["research18_StateMachineVariable"] = None):
        self.label = label
        self.research18_PublicationStatus = research18_PublicationStatus
        self.research18_PublicationStatus67 = research18_PublicationStatus67 if research18_PublicationStatus67 is not None else set()
        self.research18_PublicationStatus65 = research18_PublicationStatus65 if research18_PublicationStatus65 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def research18_PublicationStatus65(self):
        return self.__research18_PublicationStatus65

    @research18_PublicationStatus65.setter
    def research18_PublicationStatus65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_PublicationStatus__research18_PublicationStatus65", None)
        self.__research18_PublicationStatus65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research18_StateMachineVariable"):
                    opp_val = getattr(item, "research18_StateMachineVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "research18_StateMachineVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research18_StateMachineVariable"):
                    opp_val = getattr(item, "research18_StateMachineVariable", None)
                    
                    setattr(item, "research18_StateMachineVariable", self)
                    

    @property
    def research18_PublicationStatus67(self):
        return self.__research18_PublicationStatus67

    @research18_PublicationStatus67.setter
    def research18_PublicationStatus67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_PublicationStatus__research18_PublicationStatus67", None)
        self.__research18_PublicationStatus67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research18_State68"):
                    opp_val = getattr(item, "research18_State68", None)
                    
                    if opp_val == self:
                        setattr(item, "research18_State68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research18_State68"):
                    opp_val = getattr(item, "research18_State68", None)
                    
                    setattr(item, "research18_State68", self)
                    

    @property
    def research18_PublicationStatus(self):
        return self.__research18_PublicationStatus

    @research18_PublicationStatus.setter
    def research18_PublicationStatus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_PublicationStatus__research18_PublicationStatus", None)
        self.__research18_PublicationStatus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_PublicationSystem49"):
                opp_val = getattr(old_value, "research18_PublicationSystem49", None)
                if opp_val == self:
                    setattr(old_value, "research18_PublicationSystem49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_PublicationSystem49"):
                opp_val = getattr(value, "research18_PublicationSystem49", None)
                setattr(value, "research18_PublicationSystem49", self)

class Counted:

    pass
class research18_State(StateMachineObject):

    def __init__(self, id: int, kind: str, name: str, research18_State: "research18_Paper" = None, research18_State68: "research18_PublicationStatus" = None, research18_State72: "research18_Transition" = None, research18_State75: "research18_Transition" = None, research18_State77: set["research18_Transition"] = None, research18_State80: set["research18_Action"] = None):
        self.id = id
        self.kind = kind
        self.name = name
        self.research18_State = research18_State
        self.research18_State68 = research18_State68
        self.research18_State72 = research18_State72
        self.research18_State75 = research18_State75
        self.research18_State77 = research18_State77 if research18_State77 is not None else set()
        self.research18_State80 = research18_State80 if research18_State80 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research18_State68(self):
        return self.__research18_State68

    @research18_State68.setter
    def research18_State68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_State__research18_State68", None)
        self.__research18_State68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_PublicationStatus67"):
                opp_val = getattr(old_value, "research18_PublicationStatus67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_PublicationStatus67"):
                opp_val = getattr(value, "research18_PublicationStatus67", None)
                if opp_val is None:
                    setattr(value, "research18_PublicationStatus67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research18_State72(self):
        return self.__research18_State72

    @research18_State72.setter
    def research18_State72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_State__research18_State72", None)
        self.__research18_State72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Transition71"):
                opp_val = getattr(old_value, "research18_Transition71", None)
                if opp_val == self:
                    setattr(old_value, "research18_Transition71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Transition71"):
                opp_val = getattr(value, "research18_Transition71", None)
                setattr(value, "research18_Transition71", self)

    @property
    def research18_State77(self):
        return self.__research18_State77

    @research18_State77.setter
    def research18_State77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_State__research18_State77", None)
        self.__research18_State77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research18_Transition78"):
                    opp_val = getattr(item, "research18_Transition78", None)
                    
                    if opp_val == self:
                        setattr(item, "research18_Transition78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research18_Transition78"):
                    opp_val = getattr(item, "research18_Transition78", None)
                    
                    setattr(item, "research18_Transition78", self)
                    

    @property
    def research18_State(self):
        return self.__research18_State

    @research18_State.setter
    def research18_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_State__research18_State", None)
        self.__research18_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Paper20"):
                opp_val = getattr(old_value, "research18_Paper20", None)
                if opp_val == self:
                    setattr(old_value, "research18_Paper20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Paper20"):
                opp_val = getattr(value, "research18_Paper20", None)
                setattr(value, "research18_Paper20", self)

    @property
    def research18_State80(self):
        return self.__research18_State80

    @research18_State80.setter
    def research18_State80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_State__research18_State80", None)
        self.__research18_State80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research18_Action81"):
                    opp_val = getattr(item, "research18_Action81", None)
                    
                    if opp_val == self:
                        setattr(item, "research18_Action81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research18_Action81"):
                    opp_val = getattr(item, "research18_Action81", None)
                    
                    setattr(item, "research18_Action81", self)
                    

    @property
    def research18_State75(self):
        return self.__research18_State75

    @research18_State75.setter
    def research18_State75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_State__research18_State75", None)
        self.__research18_State75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Transition74"):
                opp_val = getattr(old_value, "research18_Transition74", None)
                if opp_val == self:
                    setattr(old_value, "research18_Transition74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Transition74"):
                opp_val = getattr(value, "research18_Transition74", None)
                setattr(value, "research18_Transition74", self)

class research18_PaperKeyword:

    def __init__(self, weight: int, research18_PaperKeyword: "research18_Paper" = None, research18_PaperKeyword59: "research18_Keyword" = None):
        self.weight = weight
        self.research18_PaperKeyword = research18_PaperKeyword
        self.research18_PaperKeyword59 = research18_PaperKeyword59
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def research18_PaperKeyword(self):
        return self.__research18_PaperKeyword

    @research18_PaperKeyword.setter
    def research18_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_PaperKeyword__research18_PaperKeyword", None)
        self.__research18_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Paper15"):
                opp_val = getattr(old_value, "research18_Paper15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Paper15"):
                opp_val = getattr(value, "research18_Paper15", None)
                if opp_val is None:
                    setattr(value, "research18_Paper15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research18_PaperKeyword59(self):
        return self.__research18_PaperKeyword59

    @research18_PaperKeyword59.setter
    def research18_PaperKeyword59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_PaperKeyword__research18_PaperKeyword59", None)
        self.__research18_PaperKeyword59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Keyword60"):
                opp_val = getattr(old_value, "research18_Keyword60", None)
                if opp_val == self:
                    setattr(old_value, "research18_Keyword60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Keyword60"):
                opp_val = getattr(value, "research18_Keyword60", None)
                setattr(value, "research18_Keyword60", self)

class Labelled:

    pass
class research18_Write(Labelled):

    def __init__(self, timeSpent: int, research18_Write: "research18_Researcher" = None, research18_Write28: "research18_Paragraph" = None):
        self.timeSpent = timeSpent
        self.research18_Write = research18_Write
        self.research18_Write28 = research18_Write28
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def research18_Write(self):
        return self.__research18_Write

    @research18_Write.setter
    def research18_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Write__research18_Write", None)
        self.__research18_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Researcher"):
                opp_val = getattr(old_value, "research18_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Researcher"):
                opp_val = getattr(value, "research18_Researcher", None)
                if opp_val is None:
                    setattr(value, "research18_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research18_Write28(self):
        return self.__research18_Write28

    @research18_Write28.setter
    def research18_Write28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Write__research18_Write28", None)
        self.__research18_Write28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Paragraph29"):
                opp_val = getattr(old_value, "research18_Paragraph29", None)
                if opp_val == self:
                    setattr(old_value, "research18_Paragraph29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Paragraph29"):
                opp_val = getattr(value, "research18_Paragraph29", None)
                setattr(value, "research18_Paragraph29", self)

class research18_Progress(Labelled):

    def __init__(self, percent: int, Progress: "research18_Paper" = None, research18_Progress: "research18_PublicationProcess" = None, progress: "research18_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.research18_Progress = research18_Progress
        self.progress = progress
        
    @property
    def percent(self) -> int:
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent

    @property
    def Progress(self):
        return self.__Progress

    @Progress.setter
    def Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Progress__Progress", None)
        self.__Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paper"):
                opp_val = getattr(old_value, "paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paper"):
                opp_val = getattr(value, "paper", None)
                if opp_val is None:
                    setattr(value, "paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research18_Progress(self):
        return self.__research18_Progress

    @research18_Progress.setter
    def research18_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Progress__research18_Progress", None)
        self.__research18_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_PublicationProcess24"):
                opp_val = getattr(old_value, "research18_PublicationProcess24", None)
                if opp_val == self:
                    setattr(old_value, "research18_PublicationProcess24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_PublicationProcess24"):
                opp_val = getattr(value, "research18_PublicationProcess24", None)
                setattr(value, "research18_PublicationProcess24", self)

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Progress__progress", None)
        self.__progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Paper26"):
                opp_val = getattr(old_value, "Paper26", None)
                if opp_val == self:
                    setattr(old_value, "Paper26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Paper26"):
                opp_val = getattr(value, "Paper26", None)
                setattr(value, "Paper26", self)

class research18_Collaboration:

    def __init__(self, ratio: int, research18_Collaboration: "research18_Researcher" = None, research18_Collaboration62: "research18_Paper" = None):
        self.ratio = ratio
        self.research18_Collaboration = research18_Collaboration
        self.research18_Collaboration62 = research18_Collaboration62
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def research18_Collaboration(self):
        return self.__research18_Collaboration

    @research18_Collaboration.setter
    def research18_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Collaboration__research18_Collaboration", None)
        self.__research18_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Researcher10"):
                opp_val = getattr(old_value, "research18_Researcher10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Researcher10"):
                opp_val = getattr(value, "research18_Researcher10", None)
                if opp_val is None:
                    setattr(value, "research18_Researcher10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research18_Collaboration62(self):
        return self.__research18_Collaboration62

    @research18_Collaboration62.setter
    def research18_Collaboration62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Collaboration__research18_Collaboration62", None)
        self.__research18_Collaboration62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Paper63"):
                opp_val = getattr(old_value, "research18_Paper63", None)
                if opp_val == self:
                    setattr(old_value, "research18_Paper63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Paper63"):
                opp_val = getattr(value, "research18_Paper63", None)
                setattr(value, "research18_Paper63", self)

class research18_Skill:

    def __init__(self, description: str, research18_Skill: "research18_Researcher" = None):
        self.description = description
        self.research18_Skill = research18_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research18_Skill(self):
        return self.__research18_Skill

    @research18_Skill.setter
    def research18_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Skill__research18_Skill", None)
        self.__research18_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Researcher6"):
                opp_val = getattr(old_value, "research18_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Researcher6"):
                opp_val = getattr(value, "research18_Researcher6", None)
                if opp_val is None:
                    setattr(value, "research18_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research18_Review(Labelled):

    def __init__(self, date: date, research18_Review: "research18_Researcher" = None, research18_Review31: "research18_ReviewNote" = None):
        self.date = date
        self.research18_Review = research18_Review
        self.research18_Review31 = research18_Review31
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def research18_Review(self):
        return self.__research18_Review

    @research18_Review.setter
    def research18_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Review__research18_Review", None)
        self.__research18_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Researcher3"):
                opp_val = getattr(old_value, "research18_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Researcher3"):
                opp_val = getattr(value, "research18_Researcher3", None)
                if opp_val is None:
                    setattr(value, "research18_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research18_Review31(self):
        return self.__research18_Review31

    @research18_Review31.setter
    def research18_Review31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Review__research18_Review31", None)
        self.__research18_Review31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_ReviewNote32"):
                opp_val = getattr(old_value, "research18_ReviewNote32", None)
                if opp_val == self:
                    setattr(old_value, "research18_ReviewNote32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_ReviewNote32"):
                opp_val = getattr(value, "research18_ReviewNote32", None)
                setattr(value, "research18_ReviewNote32", self)

class research18_Researcher:

    def __init__(self, name: str, forName: str, research18_Researcher3: set["research18_Review"] = None, authors: set["research18_Paper"] = None, research18_Researcher6: set["research18_Skill"] = None, research18_Researcher8: "research18_Position" = None, research18_Researcher10: set["research18_Collaboration"] = None, Researcher: "research18_Paper" = None, research18_Researcher: set["research18_Write"] = None, research18_Researcher34: "research18_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.research18_Researcher3 = research18_Researcher3 if research18_Researcher3 is not None else set()
        self.authors = authors if authors is not None else set()
        self.research18_Researcher6 = research18_Researcher6 if research18_Researcher6 is not None else set()
        self.research18_Researcher8 = research18_Researcher8
        self.research18_Researcher10 = research18_Researcher10 if research18_Researcher10 is not None else set()
        self.Researcher = Researcher
        self.research18_Researcher = research18_Researcher if research18_Researcher is not None else set()
        self.research18_Researcher34 = research18_Researcher34
        
    @property
    def forName(self) -> str:
        return self.__forName

    @forName.setter
    def forName(self, forName: str):
        self.__forName = forName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research18_Researcher3(self):
        return self.__research18_Researcher3

    @research18_Researcher3.setter
    def research18_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Researcher__research18_Researcher3", None)
        self.__research18_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research18_Review"):
                    opp_val = getattr(item, "research18_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "research18_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research18_Review"):
                    opp_val = getattr(item, "research18_Review", None)
                    
                    setattr(item, "research18_Review", self)
                    

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Researcher__authors", None)
        self.__authors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Paper"):
                    opp_val = getattr(item, "Paper", None)
                    
                    if opp_val == self:
                        setattr(item, "Paper", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Paper"):
                    opp_val = getattr(item, "Paper", None)
                    
                    setattr(item, "Paper", self)
                    

    @property
    def research18_Researcher8(self):
        return self.__research18_Researcher8

    @research18_Researcher8.setter
    def research18_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Researcher__research18_Researcher8", None)
        self.__research18_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Position"):
                opp_val = getattr(old_value, "research18_Position", None)
                if opp_val == self:
                    setattr(old_value, "research18_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Position"):
                opp_val = getattr(value, "research18_Position", None)
                setattr(value, "research18_Position", self)

    @property
    def research18_Researcher(self):
        return self.__research18_Researcher

    @research18_Researcher.setter
    def research18_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Researcher__research18_Researcher", None)
        self.__research18_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research18_Write"):
                    opp_val = getattr(item, "research18_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "research18_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research18_Write"):
                    opp_val = getattr(item, "research18_Write", None)
                    
                    setattr(item, "research18_Write", self)
                    

    @property
    def research18_Researcher34(self):
        return self.__research18_Researcher34

    @research18_Researcher34.setter
    def research18_Researcher34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Researcher__research18_Researcher34", None)
        self.__research18_Researcher34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_PublicationStructure"):
                opp_val = getattr(old_value, "research18_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_PublicationStructure"):
                opp_val = getattr(value, "research18_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "research18_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research18_Researcher6(self):
        return self.__research18_Researcher6

    @research18_Researcher6.setter
    def research18_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Researcher__research18_Researcher6", None)
        self.__research18_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research18_Skill"):
                    opp_val = getattr(item, "research18_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "research18_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research18_Skill"):
                    opp_val = getattr(item, "research18_Skill", None)
                    
                    setattr(item, "research18_Skill", self)
                    

    @property
    def research18_Researcher10(self):
        return self.__research18_Researcher10

    @research18_Researcher10.setter
    def research18_Researcher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Researcher__research18_Researcher10", None)
        self.__research18_Researcher10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research18_Collaboration"):
                    opp_val = getattr(item, "research18_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "research18_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research18_Collaboration"):
                    opp_val = getattr(item, "research18_Collaboration", None)
                    
                    setattr(item, "research18_Collaboration", self)
                    

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Researcher__Researcher", None)
        self.__Researcher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "res_papers"):
                opp_val = getattr(old_value, "res_papers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "res_papers"):
                opp_val = getattr(value, "res_papers", None)
                if opp_val is None:
                    setattr(value, "res_papers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research18_Phase:

    def __init__(self, name: str, research18_Phase: "research18_PublicationProcess" = None):
        self.name = name
        self.research18_Phase = research18_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research18_Phase(self):
        return self.__research18_Phase

    @research18_Phase.setter
    def research18_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Phase__research18_Phase", None)
        self.__research18_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_PublicationProcess"):
                opp_val = getattr(old_value, "research18_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_PublicationProcess"):
                opp_val = getattr(value, "research18_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "research18_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class research18_Keyword(Named):

    def __init__(self, word: str, research18_Keyword: set["research18_Paper"] = None, research18_Keyword57: "research18_KnowledgeManager" = None, research18_Keyword60: "research18_PaperKeyword" = None):
        self.word = word
        self.research18_Keyword = research18_Keyword if research18_Keyword is not None else set()
        self.research18_Keyword57 = research18_Keyword57
        self.research18_Keyword60 = research18_Keyword60
        
    @property
    def word(self) -> str:
        return self.__word

    @word.setter
    def word(self, word: str):
        self.__word = word

    @property
    def research18_Keyword57(self):
        return self.__research18_Keyword57

    @research18_Keyword57.setter
    def research18_Keyword57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Keyword__research18_Keyword57", None)
        self.__research18_Keyword57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_KnowledgeManager56"):
                opp_val = getattr(old_value, "research18_KnowledgeManager56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_KnowledgeManager56"):
                opp_val = getattr(value, "research18_KnowledgeManager56", None)
                if opp_val is None:
                    setattr(value, "research18_KnowledgeManager56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research18_Keyword(self):
        return self.__research18_Keyword

    @research18_Keyword.setter
    def research18_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Keyword__research18_Keyword", None)
        self.__research18_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research18_Paper54"):
                    opp_val = getattr(item, "research18_Paper54", None)
                    
                    if opp_val == self:
                        setattr(item, "research18_Paper54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research18_Paper54"):
                    opp_val = getattr(item, "research18_Paper54", None)
                    
                    setattr(item, "research18_Paper54", self)
                    

    @property
    def research18_Keyword60(self):
        return self.__research18_Keyword60

    @research18_Keyword60.setter
    def research18_Keyword60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Keyword__research18_Keyword60", None)
        self.__research18_Keyword60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_PaperKeyword59"):
                opp_val = getattr(old_value, "research18_PaperKeyword59", None)
                if opp_val == self:
                    setattr(old_value, "research18_PaperKeyword59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_PaperKeyword59"):
                opp_val = getattr(value, "research18_PaperKeyword59", None)
                setattr(value, "research18_PaperKeyword59", self)

class research18_PublicationStructure(Named):

    pass
class research18_Paragraph(Counted, Named):

    def __init__(self, content: str, research18_Paragraph: "research18_Paper" = None, research18_Paragraph22: set["research18_ReviewNote"] = None, research18_Paragraph29: "research18_Write" = None):
        self.content = content
        self.research18_Paragraph = research18_Paragraph
        self.research18_Paragraph22 = research18_Paragraph22 if research18_Paragraph22 is not None else set()
        self.research18_Paragraph29 = research18_Paragraph29
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research18_Paragraph(self):
        return self.__research18_Paragraph

    @research18_Paragraph.setter
    def research18_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Paragraph__research18_Paragraph", None)
        self.__research18_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Paper"):
                opp_val = getattr(old_value, "research18_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Paper"):
                opp_val = getattr(value, "research18_Paper", None)
                if opp_val is None:
                    setattr(value, "research18_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research18_Paragraph22(self):
        return self.__research18_Paragraph22

    @research18_Paragraph22.setter
    def research18_Paragraph22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Paragraph__research18_Paragraph22", None)
        self.__research18_Paragraph22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research18_ReviewNote"):
                    opp_val = getattr(item, "research18_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "research18_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research18_ReviewNote"):
                    opp_val = getattr(item, "research18_ReviewNote", None)
                    
                    setattr(item, "research18_ReviewNote", self)
                    

    @property
    def research18_Paragraph29(self):
        return self.__research18_Paragraph29

    @research18_Paragraph29.setter
    def research18_Paragraph29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Paragraph__research18_Paragraph29", None)
        self.__research18_Paragraph29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Write28"):
                opp_val = getattr(old_value, "research18_Write28", None)
                if opp_val == self:
                    setattr(old_value, "research18_Write28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Write28"):
                opp_val = getattr(value, "research18_Write28", None)
                setattr(value, "research18_Write28", self)

class research18_ReviewNote(Named):

    def __init__(self, content: str, research18_ReviewNote: "research18_Paragraph" = None, research18_ReviewNote32: "research18_Review" = None):
        self.content = content
        self.research18_ReviewNote = research18_ReviewNote
        self.research18_ReviewNote32 = research18_ReviewNote32
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research18_ReviewNote32(self):
        return self.__research18_ReviewNote32

    @research18_ReviewNote32.setter
    def research18_ReviewNote32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_ReviewNote__research18_ReviewNote32", None)
        self.__research18_ReviewNote32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Review31"):
                opp_val = getattr(old_value, "research18_Review31", None)
                if opp_val == self:
                    setattr(old_value, "research18_Review31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Review31"):
                opp_val = getattr(value, "research18_Review31", None)
                setattr(value, "research18_Review31", self)

    @property
    def research18_ReviewNote(self):
        return self.__research18_ReviewNote

    @research18_ReviewNote.setter
    def research18_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_ReviewNote__research18_ReviewNote", None)
        self.__research18_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Paragraph22"):
                opp_val = getattr(old_value, "research18_Paragraph22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Paragraph22"):
                opp_val = getattr(value, "research18_Paragraph22", None)
                if opp_val is None:
                    setattr(value, "research18_Paragraph22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research18_KnowledgeManager(Named):

    pass
class research18_PublicationSystem(Named):

    pass
class research18_Paper(Named):

    pass
class research18_Position(Named):

    def __init__(self, description: str, research18_Position: "research18_Researcher" = None, research18_Position47: "research18_PublicationSystem" = None, research18_Position52: "research18_Position" = None, research18_Position50: "research18_Position" = None):
        self.description = description
        self.research18_Position = research18_Position
        self.research18_Position47 = research18_Position47
        self.research18_Position52 = research18_Position52
        self.research18_Position50 = research18_Position50
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research18_Position(self):
        return self.__research18_Position

    @research18_Position.setter
    def research18_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Position__research18_Position", None)
        self.__research18_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Researcher8"):
                opp_val = getattr(old_value, "research18_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "research18_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Researcher8"):
                opp_val = getattr(value, "research18_Researcher8", None)
                setattr(value, "research18_Researcher8", self)

    @property
    def research18_Position52(self):
        return self.__research18_Position52

    @research18_Position52.setter
    def research18_Position52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Position__research18_Position52", None)
        self.__research18_Position52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Position50"):
                opp_val = getattr(old_value, "research18_Position50", None)
                if opp_val == self:
                    setattr(old_value, "research18_Position50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Position50"):
                opp_val = getattr(value, "research18_Position50", None)
                setattr(value, "research18_Position50", self)

    @property
    def research18_Position50(self):
        return self.__research18_Position50

    @research18_Position50.setter
    def research18_Position50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Position__research18_Position50", None)
        self.__research18_Position50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Position52"):
                opp_val = getattr(old_value, "research18_Position52", None)
                if opp_val == self:
                    setattr(old_value, "research18_Position52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Position52"):
                opp_val = getattr(value, "research18_Position52", None)
                setattr(value, "research18_Position52", self)

    @property
    def research18_Position47(self):
        return self.__research18_Position47

    @research18_Position47.setter
    def research18_Position47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_Position__research18_Position47", None)
        self.__research18_Position47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_PublicationSystem46"):
                opp_val = getattr(old_value, "research18_PublicationSystem46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_PublicationSystem46"):
                opp_val = getattr(value, "research18_PublicationSystem46", None)
                if opp_val is None:
                    setattr(value, "research18_PublicationSystem46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research18_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, research18_PublicationProcess: set["research18_Phase"] = None, research18_PublicationProcess24: "research18_Progress" = None, research18_PublicationProcess41: "research18_PublicationSystem" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.research18_PublicationProcess = research18_PublicationProcess if research18_PublicationProcess is not None else set()
        self.research18_PublicationProcess24 = research18_PublicationProcess24
        self.research18_PublicationProcess41 = research18_PublicationProcess41
        
    @property
    def maxTime(self) -> int:
        return self.__maxTime

    @maxTime.setter
    def maxTime(self, maxTime: int):
        self.__maxTime = maxTime

    @property
    def minTime(self) -> int:
        return self.__minTime

    @minTime.setter
    def minTime(self, minTime: int):
        self.__minTime = minTime

    @property
    def research18_PublicationProcess41(self):
        return self.__research18_PublicationProcess41

    @research18_PublicationProcess41.setter
    def research18_PublicationProcess41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_PublicationProcess__research18_PublicationProcess41", None)
        self.__research18_PublicationProcess41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_PublicationSystem"):
                opp_val = getattr(old_value, "research18_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "research18_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_PublicationSystem"):
                opp_val = getattr(value, "research18_PublicationSystem", None)
                setattr(value, "research18_PublicationSystem", self)

    @property
    def research18_PublicationProcess24(self):
        return self.__research18_PublicationProcess24

    @research18_PublicationProcess24.setter
    def research18_PublicationProcess24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_PublicationProcess__research18_PublicationProcess24", None)
        self.__research18_PublicationProcess24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research18_Progress"):
                opp_val = getattr(old_value, "research18_Progress", None)
                if opp_val == self:
                    setattr(old_value, "research18_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research18_Progress"):
                opp_val = getattr(value, "research18_Progress", None)
                setattr(value, "research18_Progress", self)

    @property
    def research18_PublicationProcess(self):
        return self.__research18_PublicationProcess

    @research18_PublicationProcess.setter
    def research18_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research18_PublicationProcess__research18_PublicationProcess", None)
        self.__research18_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research18_Phase"):
                    opp_val = getattr(item, "research18_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "research18_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research18_Phase"):
                    opp_val = getattr(item, "research18_Phase", None)
                    
                    setattr(item, "research18_Phase", self)
                    
