from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StateType(Enum):
    ongoing = "ongoing"
    final = "final"
    initial = "initial"


############################################
# Definition of Classes
############################################

class research32_Action:

    def __init__(self, actionLabel: str, actionStatement: str, research32_Action: "research32_Transition" = None, research32_Action81: "research32_State" = None, research32_Action84: "research32_Action" = None, research32_Action82: "research32_Action" = None):
        self.actionLabel = actionLabel
        self.actionStatement = actionStatement
        self.research32_Action = research32_Action
        self.research32_Action81 = research32_Action81
        self.research32_Action84 = research32_Action84
        self.research32_Action82 = research32_Action82
        
    @property
    def actionStatement(self) -> str:
        return self.__actionStatement

    @actionStatement.setter
    def actionStatement(self, actionStatement: str):
        self.__actionStatement = actionStatement

    @property
    def actionLabel(self) -> str:
        return self.__actionLabel

    @actionLabel.setter
    def actionLabel(self, actionLabel: str):
        self.__actionLabel = actionLabel

    @property
    def research32_Action(self):
        return self.__research32_Action

    @research32_Action.setter
    def research32_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Action__research32_Action", None)
        self.__research32_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Transition"):
                opp_val = getattr(old_value, "research32_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Transition"):
                opp_val = getattr(value, "research32_Transition", None)
                if opp_val is None:
                    setattr(value, "research32_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research32_Action82(self):
        return self.__research32_Action82

    @research32_Action82.setter
    def research32_Action82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Action__research32_Action82", None)
        self.__research32_Action82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Action84"):
                opp_val = getattr(old_value, "research32_Action84", None)
                if opp_val == self:
                    setattr(old_value, "research32_Action84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Action84"):
                opp_val = getattr(value, "research32_Action84", None)
                setattr(value, "research32_Action84", self)

    @property
    def research32_Action84(self):
        return self.__research32_Action84

    @research32_Action84.setter
    def research32_Action84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Action__research32_Action84", None)
        self.__research32_Action84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Action82"):
                opp_val = getattr(old_value, "research32_Action82", None)
                if opp_val == self:
                    setattr(old_value, "research32_Action82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Action82"):
                opp_val = getattr(value, "research32_Action82", None)
                setattr(value, "research32_Action82", self)

    @property
    def research32_Action81(self):
        return self.__research32_Action81

    @research32_Action81.setter
    def research32_Action81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Action__research32_Action81", None)
        self.__research32_Action81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_State80"):
                opp_val = getattr(old_value, "research32_State80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_State80"):
                opp_val = getattr(value, "research32_State80", None)
                if opp_val is None:
                    setattr(value, "research32_State80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StateMachineObject:

    pass
class research32_Transition(StateMachineObject):

    def __init__(self, guardLabel: str, guardExpression: str, research32_Transition: set["research32_Action"] = None, research32_Transition71: "research32_State" = None, research32_Transition74: "research32_State" = None, research32_Transition78: "research32_State" = None):
        self.guardLabel = guardLabel
        self.guardExpression = guardExpression
        self.research32_Transition = research32_Transition if research32_Transition is not None else set()
        self.research32_Transition71 = research32_Transition71
        self.research32_Transition74 = research32_Transition74
        self.research32_Transition78 = research32_Transition78
        
    @property
    def guardLabel(self) -> str:
        return self.__guardLabel

    @guardLabel.setter
    def guardLabel(self, guardLabel: str):
        self.__guardLabel = guardLabel

    @property
    def guardExpression(self) -> str:
        return self.__guardExpression

    @guardExpression.setter
    def guardExpression(self, guardExpression: str):
        self.__guardExpression = guardExpression

    @property
    def research32_Transition71(self):
        return self.__research32_Transition71

    @research32_Transition71.setter
    def research32_Transition71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Transition__research32_Transition71", None)
        self.__research32_Transition71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_State72"):
                opp_val = getattr(old_value, "research32_State72", None)
                if opp_val == self:
                    setattr(old_value, "research32_State72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_State72"):
                opp_val = getattr(value, "research32_State72", None)
                setattr(value, "research32_State72", self)

    @property
    def research32_Transition(self):
        return self.__research32_Transition

    @research32_Transition.setter
    def research32_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Transition__research32_Transition", None)
        self.__research32_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research32_Action"):
                    opp_val = getattr(item, "research32_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "research32_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research32_Action"):
                    opp_val = getattr(item, "research32_Action", None)
                    
                    setattr(item, "research32_Action", self)
                    

    @property
    def research32_Transition74(self):
        return self.__research32_Transition74

    @research32_Transition74.setter
    def research32_Transition74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Transition__research32_Transition74", None)
        self.__research32_Transition74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_State75"):
                opp_val = getattr(old_value, "research32_State75", None)
                if opp_val == self:
                    setattr(old_value, "research32_State75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_State75"):
                opp_val = getattr(value, "research32_State75", None)
                setattr(value, "research32_State75", self)

    @property
    def research32_Transition78(self):
        return self.__research32_Transition78

    @research32_Transition78.setter
    def research32_Transition78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Transition__research32_Transition78", None)
        self.__research32_Transition78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_State77"):
                opp_val = getattr(old_value, "research32_State77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_State77"):
                opp_val = getattr(value, "research32_State77", None)
                if opp_val is None:
                    setattr(value, "research32_State77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research32_StateMachineObject(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class research32_StateMachineVariable:

    pass
class research32_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class research32_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class research32_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class research32_PublicationStatus:

    def __init__(self, label: str, research32_PublicationStatus: "research32_PublicationStructure" = None, research32_PublicationStatus67: set["research32_State"] = None, research32_PublicationStatus65: set["research32_StateMachineVariable"] = None):
        self.label = label
        self.research32_PublicationStatus = research32_PublicationStatus
        self.research32_PublicationStatus67 = research32_PublicationStatus67 if research32_PublicationStatus67 is not None else set()
        self.research32_PublicationStatus65 = research32_PublicationStatus65 if research32_PublicationStatus65 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def research32_PublicationStatus67(self):
        return self.__research32_PublicationStatus67

    @research32_PublicationStatus67.setter
    def research32_PublicationStatus67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_PublicationStatus__research32_PublicationStatus67", None)
        self.__research32_PublicationStatus67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research32_State68"):
                    opp_val = getattr(item, "research32_State68", None)
                    
                    if opp_val == self:
                        setattr(item, "research32_State68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research32_State68"):
                    opp_val = getattr(item, "research32_State68", None)
                    
                    setattr(item, "research32_State68", self)
                    

    @property
    def research32_PublicationStatus(self):
        return self.__research32_PublicationStatus

    @research32_PublicationStatus.setter
    def research32_PublicationStatus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_PublicationStatus__research32_PublicationStatus", None)
        self.__research32_PublicationStatus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_PublicationStructure41"):
                opp_val = getattr(old_value, "research32_PublicationStructure41", None)
                if opp_val == self:
                    setattr(old_value, "research32_PublicationStructure41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_PublicationStructure41"):
                opp_val = getattr(value, "research32_PublicationStructure41", None)
                setattr(value, "research32_PublicationStructure41", self)

    @property
    def research32_PublicationStatus65(self):
        return self.__research32_PublicationStatus65

    @research32_PublicationStatus65.setter
    def research32_PublicationStatus65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_PublicationStatus__research32_PublicationStatus65", None)
        self.__research32_PublicationStatus65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research32_StateMachineVariable"):
                    opp_val = getattr(item, "research32_StateMachineVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "research32_StateMachineVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research32_StateMachineVariable"):
                    opp_val = getattr(item, "research32_StateMachineVariable", None)
                    
                    setattr(item, "research32_StateMachineVariable", self)
                    

class Labelled:

    pass
class Counted:

    pass
class research32_State(StateMachineObject):

    def __init__(self, id: int, kind: str, name: str, research32_State: "research32_Paper" = None, research32_State68: "research32_PublicationStatus" = None, research32_State72: "research32_Transition" = None, research32_State75: "research32_Transition" = None, research32_State77: set["research32_Transition"] = None, research32_State80: set["research32_Action"] = None):
        self.id = id
        self.kind = kind
        self.name = name
        self.research32_State = research32_State
        self.research32_State68 = research32_State68
        self.research32_State72 = research32_State72
        self.research32_State75 = research32_State75
        self.research32_State77 = research32_State77 if research32_State77 is not None else set()
        self.research32_State80 = research32_State80 if research32_State80 is not None else set()
        
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
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def research32_State72(self):
        return self.__research32_State72

    @research32_State72.setter
    def research32_State72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_State__research32_State72", None)
        self.__research32_State72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Transition71"):
                opp_val = getattr(old_value, "research32_Transition71", None)
                if opp_val == self:
                    setattr(old_value, "research32_Transition71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Transition71"):
                opp_val = getattr(value, "research32_Transition71", None)
                setattr(value, "research32_Transition71", self)

    @property
    def research32_State(self):
        return self.__research32_State

    @research32_State.setter
    def research32_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_State__research32_State", None)
        self.__research32_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Paper20"):
                opp_val = getattr(old_value, "research32_Paper20", None)
                if opp_val == self:
                    setattr(old_value, "research32_Paper20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Paper20"):
                opp_val = getattr(value, "research32_Paper20", None)
                setattr(value, "research32_Paper20", self)

    @property
    def research32_State80(self):
        return self.__research32_State80

    @research32_State80.setter
    def research32_State80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_State__research32_State80", None)
        self.__research32_State80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research32_Action81"):
                    opp_val = getattr(item, "research32_Action81", None)
                    
                    if opp_val == self:
                        setattr(item, "research32_Action81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research32_Action81"):
                    opp_val = getattr(item, "research32_Action81", None)
                    
                    setattr(item, "research32_Action81", self)
                    

    @property
    def research32_State77(self):
        return self.__research32_State77

    @research32_State77.setter
    def research32_State77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_State__research32_State77", None)
        self.__research32_State77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research32_Transition78"):
                    opp_val = getattr(item, "research32_Transition78", None)
                    
                    if opp_val == self:
                        setattr(item, "research32_Transition78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research32_Transition78"):
                    opp_val = getattr(item, "research32_Transition78", None)
                    
                    setattr(item, "research32_Transition78", self)
                    

    @property
    def research32_State75(self):
        return self.__research32_State75

    @research32_State75.setter
    def research32_State75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_State__research32_State75", None)
        self.__research32_State75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Transition74"):
                opp_val = getattr(old_value, "research32_Transition74", None)
                if opp_val == self:
                    setattr(old_value, "research32_Transition74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Transition74"):
                opp_val = getattr(value, "research32_Transition74", None)
                setattr(value, "research32_Transition74", self)

    @property
    def research32_State68(self):
        return self.__research32_State68

    @research32_State68.setter
    def research32_State68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_State__research32_State68", None)
        self.__research32_State68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_PublicationStatus67"):
                opp_val = getattr(old_value, "research32_PublicationStatus67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_PublicationStatus67"):
                opp_val = getattr(value, "research32_PublicationStatus67", None)
                if opp_val is None:
                    setattr(value, "research32_PublicationStatus67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research32_PaperKeyword:

    def __init__(self, weight: int, research32_PaperKeyword: "research32_Paper" = None, research32_PaperKeyword59: "research32_Keyword" = None):
        self.weight = weight
        self.research32_PaperKeyword = research32_PaperKeyword
        self.research32_PaperKeyword59 = research32_PaperKeyword59
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def research32_PaperKeyword(self):
        return self.__research32_PaperKeyword

    @research32_PaperKeyword.setter
    def research32_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_PaperKeyword__research32_PaperKeyword", None)
        self.__research32_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Paper15"):
                opp_val = getattr(old_value, "research32_Paper15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Paper15"):
                opp_val = getattr(value, "research32_Paper15", None)
                if opp_val is None:
                    setattr(value, "research32_Paper15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research32_PaperKeyword59(self):
        return self.__research32_PaperKeyword59

    @research32_PaperKeyword59.setter
    def research32_PaperKeyword59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_PaperKeyword__research32_PaperKeyword59", None)
        self.__research32_PaperKeyword59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Keyword60"):
                opp_val = getattr(old_value, "research32_Keyword60", None)
                if opp_val == self:
                    setattr(old_value, "research32_Keyword60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Keyword60"):
                opp_val = getattr(value, "research32_Keyword60", None)
                setattr(value, "research32_Keyword60", self)

class research32_Progress(Labelled):

    def __init__(self, percent: int, Progress: "research32_Paper" = None, research32_Progress: "research32_PublicationProcess" = None, progress: "research32_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.research32_Progress = research32_Progress
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
        old_value = getattr(self, f"_research32_Progress__Progress", None)
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
    def research32_Progress(self):
        return self.__research32_Progress

    @research32_Progress.setter
    def research32_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Progress__research32_Progress", None)
        self.__research32_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_PublicationProcess24"):
                opp_val = getattr(old_value, "research32_PublicationProcess24", None)
                if opp_val == self:
                    setattr(old_value, "research32_PublicationProcess24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_PublicationProcess24"):
                opp_val = getattr(value, "research32_PublicationProcess24", None)
                setattr(value, "research32_PublicationProcess24", self)

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Progress__progress", None)
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

class research32_Collaboration:

    def __init__(self, ratio: int, research32_Collaboration: "research32_Researcher" = None, research32_Collaboration62: "research32_Paper" = None):
        self.ratio = ratio
        self.research32_Collaboration = research32_Collaboration
        self.research32_Collaboration62 = research32_Collaboration62
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def research32_Collaboration62(self):
        return self.__research32_Collaboration62

    @research32_Collaboration62.setter
    def research32_Collaboration62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Collaboration__research32_Collaboration62", None)
        self.__research32_Collaboration62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Paper63"):
                opp_val = getattr(old_value, "research32_Paper63", None)
                if opp_val == self:
                    setattr(old_value, "research32_Paper63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Paper63"):
                opp_val = getattr(value, "research32_Paper63", None)
                setattr(value, "research32_Paper63", self)

    @property
    def research32_Collaboration(self):
        return self.__research32_Collaboration

    @research32_Collaboration.setter
    def research32_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Collaboration__research32_Collaboration", None)
        self.__research32_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Researcher10"):
                opp_val = getattr(old_value, "research32_Researcher10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Researcher10"):
                opp_val = getattr(value, "research32_Researcher10", None)
                if opp_val is None:
                    setattr(value, "research32_Researcher10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research32_Skill:

    def __init__(self, description: str, research32_Skill: "research32_Researcher" = None):
        self.description = description
        self.research32_Skill = research32_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research32_Skill(self):
        return self.__research32_Skill

    @research32_Skill.setter
    def research32_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Skill__research32_Skill", None)
        self.__research32_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Researcher6"):
                opp_val = getattr(old_value, "research32_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Researcher6"):
                opp_val = getattr(value, "research32_Researcher6", None)
                if opp_val is None:
                    setattr(value, "research32_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research32_Review(Labelled):

    def __init__(self, date: date, research32_Review: "research32_Researcher" = None, research32_Review31: "research32_ReviewNote" = None):
        self.date = date
        self.research32_Review = research32_Review
        self.research32_Review31 = research32_Review31
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def research32_Review(self):
        return self.__research32_Review

    @research32_Review.setter
    def research32_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Review__research32_Review", None)
        self.__research32_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Researcher3"):
                opp_val = getattr(old_value, "research32_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Researcher3"):
                opp_val = getattr(value, "research32_Researcher3", None)
                if opp_val is None:
                    setattr(value, "research32_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research32_Review31(self):
        return self.__research32_Review31

    @research32_Review31.setter
    def research32_Review31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Review__research32_Review31", None)
        self.__research32_Review31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_ReviewNote32"):
                opp_val = getattr(old_value, "research32_ReviewNote32", None)
                if opp_val == self:
                    setattr(old_value, "research32_ReviewNote32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_ReviewNote32"):
                opp_val = getattr(value, "research32_ReviewNote32", None)
                setattr(value, "research32_ReviewNote32", self)

class research32_Write(Labelled):

    def __init__(self, timeSpent: int, research32_Write: "research32_Researcher" = None, research32_Write28: "research32_Paragraph" = None):
        self.timeSpent = timeSpent
        self.research32_Write = research32_Write
        self.research32_Write28 = research32_Write28
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def research32_Write(self):
        return self.__research32_Write

    @research32_Write.setter
    def research32_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Write__research32_Write", None)
        self.__research32_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Researcher"):
                opp_val = getattr(old_value, "research32_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Researcher"):
                opp_val = getattr(value, "research32_Researcher", None)
                if opp_val is None:
                    setattr(value, "research32_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research32_Write28(self):
        return self.__research32_Write28

    @research32_Write28.setter
    def research32_Write28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Write__research32_Write28", None)
        self.__research32_Write28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Paragraph29"):
                opp_val = getattr(old_value, "research32_Paragraph29", None)
                if opp_val == self:
                    setattr(old_value, "research32_Paragraph29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Paragraph29"):
                opp_val = getattr(value, "research32_Paragraph29", None)
                setattr(value, "research32_Paragraph29", self)

class research32_Researcher:

    def __init__(self, name: str, forName: str, research32_Researcher: set["research32_Write"] = None, research32_Researcher3: set["research32_Review"] = None, authors: set["research32_Paper"] = None, research32_Researcher6: set["research32_Skill"] = None, research32_Researcher8: "research32_Position" = None, research32_Researcher10: set["research32_Collaboration"] = None, Researcher: "research32_Paper" = None, research32_Researcher34: "research32_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.research32_Researcher = research32_Researcher if research32_Researcher is not None else set()
        self.research32_Researcher3 = research32_Researcher3 if research32_Researcher3 is not None else set()
        self.authors = authors if authors is not None else set()
        self.research32_Researcher6 = research32_Researcher6 if research32_Researcher6 is not None else set()
        self.research32_Researcher8 = research32_Researcher8
        self.research32_Researcher10 = research32_Researcher10 if research32_Researcher10 is not None else set()
        self.Researcher = Researcher
        self.research32_Researcher34 = research32_Researcher34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forName(self) -> str:
        return self.__forName

    @forName.setter
    def forName(self, forName: str):
        self.__forName = forName

    @property
    def research32_Researcher8(self):
        return self.__research32_Researcher8

    @research32_Researcher8.setter
    def research32_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Researcher__research32_Researcher8", None)
        self.__research32_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Position"):
                opp_val = getattr(old_value, "research32_Position", None)
                if opp_val == self:
                    setattr(old_value, "research32_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Position"):
                opp_val = getattr(value, "research32_Position", None)
                setattr(value, "research32_Position", self)

    @property
    def research32_Researcher3(self):
        return self.__research32_Researcher3

    @research32_Researcher3.setter
    def research32_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Researcher__research32_Researcher3", None)
        self.__research32_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research32_Review"):
                    opp_val = getattr(item, "research32_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "research32_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research32_Review"):
                    opp_val = getattr(item, "research32_Review", None)
                    
                    setattr(item, "research32_Review", self)
                    

    @property
    def research32_Researcher(self):
        return self.__research32_Researcher

    @research32_Researcher.setter
    def research32_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Researcher__research32_Researcher", None)
        self.__research32_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research32_Write"):
                    opp_val = getattr(item, "research32_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "research32_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research32_Write"):
                    opp_val = getattr(item, "research32_Write", None)
                    
                    setattr(item, "research32_Write", self)
                    

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Researcher__authors", None)
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
    def research32_Researcher34(self):
        return self.__research32_Researcher34

    @research32_Researcher34.setter
    def research32_Researcher34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Researcher__research32_Researcher34", None)
        self.__research32_Researcher34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_PublicationStructure"):
                opp_val = getattr(old_value, "research32_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_PublicationStructure"):
                opp_val = getattr(value, "research32_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "research32_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research32_Researcher10(self):
        return self.__research32_Researcher10

    @research32_Researcher10.setter
    def research32_Researcher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Researcher__research32_Researcher10", None)
        self.__research32_Researcher10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research32_Collaboration"):
                    opp_val = getattr(item, "research32_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "research32_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research32_Collaboration"):
                    opp_val = getattr(item, "research32_Collaboration", None)
                    
                    setattr(item, "research32_Collaboration", self)
                    

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Researcher__Researcher", None)
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

    @property
    def research32_Researcher6(self):
        return self.__research32_Researcher6

    @research32_Researcher6.setter
    def research32_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Researcher__research32_Researcher6", None)
        self.__research32_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research32_Skill"):
                    opp_val = getattr(item, "research32_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "research32_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research32_Skill"):
                    opp_val = getattr(item, "research32_Skill", None)
                    
                    setattr(item, "research32_Skill", self)
                    

class research32_Phase:

    def __init__(self, name: str, research32_Phase: "research32_PublicationProcess" = None):
        self.name = name
        self.research32_Phase = research32_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research32_Phase(self):
        return self.__research32_Phase

    @research32_Phase.setter
    def research32_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Phase__research32_Phase", None)
        self.__research32_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_PublicationProcess"):
                opp_val = getattr(old_value, "research32_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_PublicationProcess"):
                opp_val = getattr(value, "research32_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "research32_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class research32_Paragraph(Named, Counted):

    def __init__(self, content: str, research32_Paragraph: "research32_Paper" = None, research32_Paragraph22: set["research32_ReviewNote"] = None, research32_Paragraph29: "research32_Write" = None):
        self.content = content
        self.research32_Paragraph = research32_Paragraph
        self.research32_Paragraph22 = research32_Paragraph22 if research32_Paragraph22 is not None else set()
        self.research32_Paragraph29 = research32_Paragraph29
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research32_Paragraph22(self):
        return self.__research32_Paragraph22

    @research32_Paragraph22.setter
    def research32_Paragraph22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Paragraph__research32_Paragraph22", None)
        self.__research32_Paragraph22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research32_ReviewNote"):
                    opp_val = getattr(item, "research32_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "research32_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research32_ReviewNote"):
                    opp_val = getattr(item, "research32_ReviewNote", None)
                    
                    setattr(item, "research32_ReviewNote", self)
                    

    @property
    def research32_Paragraph29(self):
        return self.__research32_Paragraph29

    @research32_Paragraph29.setter
    def research32_Paragraph29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Paragraph__research32_Paragraph29", None)
        self.__research32_Paragraph29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Write28"):
                opp_val = getattr(old_value, "research32_Write28", None)
                if opp_val == self:
                    setattr(old_value, "research32_Write28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Write28"):
                opp_val = getattr(value, "research32_Write28", None)
                setattr(value, "research32_Write28", self)

    @property
    def research32_Paragraph(self):
        return self.__research32_Paragraph

    @research32_Paragraph.setter
    def research32_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Paragraph__research32_Paragraph", None)
        self.__research32_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Paper"):
                opp_val = getattr(old_value, "research32_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Paper"):
                opp_val = getattr(value, "research32_Paper", None)
                if opp_val is None:
                    setattr(value, "research32_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research32_Paper(Named):

    pass
class research32_Keyword(Named):

    def __init__(self, word: str, research32_Keyword: set["research32_Paper"] = None, research32_Keyword57: "research32_KnowledgeManager" = None, research32_Keyword60: "research32_PaperKeyword" = None):
        self.word = word
        self.research32_Keyword = research32_Keyword if research32_Keyword is not None else set()
        self.research32_Keyword57 = research32_Keyword57
        self.research32_Keyword60 = research32_Keyword60
        
    @property
    def word(self) -> str:
        return self.__word

    @word.setter
    def word(self, word: str):
        self.__word = word

    @property
    def research32_Keyword57(self):
        return self.__research32_Keyword57

    @research32_Keyword57.setter
    def research32_Keyword57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Keyword__research32_Keyword57", None)
        self.__research32_Keyword57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_KnowledgeManager56"):
                opp_val = getattr(old_value, "research32_KnowledgeManager56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_KnowledgeManager56"):
                opp_val = getattr(value, "research32_KnowledgeManager56", None)
                if opp_val is None:
                    setattr(value, "research32_KnowledgeManager56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research32_Keyword60(self):
        return self.__research32_Keyword60

    @research32_Keyword60.setter
    def research32_Keyword60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Keyword__research32_Keyword60", None)
        self.__research32_Keyword60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_PaperKeyword59"):
                opp_val = getattr(old_value, "research32_PaperKeyword59", None)
                if opp_val == self:
                    setattr(old_value, "research32_PaperKeyword59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_PaperKeyword59"):
                opp_val = getattr(value, "research32_PaperKeyword59", None)
                setattr(value, "research32_PaperKeyword59", self)

    @property
    def research32_Keyword(self):
        return self.__research32_Keyword

    @research32_Keyword.setter
    def research32_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Keyword__research32_Keyword", None)
        self.__research32_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research32_Paper54"):
                    opp_val = getattr(item, "research32_Paper54", None)
                    
                    if opp_val == self:
                        setattr(item, "research32_Paper54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research32_Paper54"):
                    opp_val = getattr(item, "research32_Paper54", None)
                    
                    setattr(item, "research32_Paper54", self)
                    

class research32_KnowledgeManager(Named):

    pass
class research32_PublicationSystem(Named):

    pass
class research32_Position(Named):

    def __init__(self, description: str, research32_Position: "research32_Researcher" = None, research32_Position49: "research32_PublicationSystem" = None, research32_Position52: "research32_Position" = None, research32_Position50: "research32_Position" = None):
        self.description = description
        self.research32_Position = research32_Position
        self.research32_Position49 = research32_Position49
        self.research32_Position52 = research32_Position52
        self.research32_Position50 = research32_Position50
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research32_Position(self):
        return self.__research32_Position

    @research32_Position.setter
    def research32_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Position__research32_Position", None)
        self.__research32_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Researcher8"):
                opp_val = getattr(old_value, "research32_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "research32_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Researcher8"):
                opp_val = getattr(value, "research32_Researcher8", None)
                setattr(value, "research32_Researcher8", self)

    @property
    def research32_Position49(self):
        return self.__research32_Position49

    @research32_Position49.setter
    def research32_Position49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Position__research32_Position49", None)
        self.__research32_Position49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_PublicationSystem48"):
                opp_val = getattr(old_value, "research32_PublicationSystem48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_PublicationSystem48"):
                opp_val = getattr(value, "research32_PublicationSystem48", None)
                if opp_val is None:
                    setattr(value, "research32_PublicationSystem48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research32_Position50(self):
        return self.__research32_Position50

    @research32_Position50.setter
    def research32_Position50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Position__research32_Position50", None)
        self.__research32_Position50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Position52"):
                opp_val = getattr(old_value, "research32_Position52", None)
                if opp_val == self:
                    setattr(old_value, "research32_Position52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Position52"):
                opp_val = getattr(value, "research32_Position52", None)
                setattr(value, "research32_Position52", self)

    @property
    def research32_Position52(self):
        return self.__research32_Position52

    @research32_Position52.setter
    def research32_Position52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_Position__research32_Position52", None)
        self.__research32_Position52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Position50"):
                opp_val = getattr(old_value, "research32_Position50", None)
                if opp_val == self:
                    setattr(old_value, "research32_Position50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Position50"):
                opp_val = getattr(value, "research32_Position50", None)
                setattr(value, "research32_Position50", self)

class research32_PublicationStructure(Named):

    pass
class research32_ReviewNote(Named):

    def __init__(self, content: str, research32_ReviewNote: "research32_Paragraph" = None, research32_ReviewNote32: "research32_Review" = None):
        self.content = content
        self.research32_ReviewNote = research32_ReviewNote
        self.research32_ReviewNote32 = research32_ReviewNote32
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research32_ReviewNote32(self):
        return self.__research32_ReviewNote32

    @research32_ReviewNote32.setter
    def research32_ReviewNote32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_ReviewNote__research32_ReviewNote32", None)
        self.__research32_ReviewNote32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Review31"):
                opp_val = getattr(old_value, "research32_Review31", None)
                if opp_val == self:
                    setattr(old_value, "research32_Review31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Review31"):
                opp_val = getattr(value, "research32_Review31", None)
                setattr(value, "research32_Review31", self)

    @property
    def research32_ReviewNote(self):
        return self.__research32_ReviewNote

    @research32_ReviewNote.setter
    def research32_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_ReviewNote__research32_ReviewNote", None)
        self.__research32_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Paragraph22"):
                opp_val = getattr(old_value, "research32_Paragraph22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Paragraph22"):
                opp_val = getattr(value, "research32_Paragraph22", None)
                if opp_val is None:
                    setattr(value, "research32_Paragraph22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research32_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, research32_PublicationProcess: set["research32_Phase"] = None, research32_PublicationProcess24: "research32_Progress" = None, research32_PublicationProcess43: "research32_PublicationSystem" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.research32_PublicationProcess = research32_PublicationProcess if research32_PublicationProcess is not None else set()
        self.research32_PublicationProcess24 = research32_PublicationProcess24
        self.research32_PublicationProcess43 = research32_PublicationProcess43
        
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
    def research32_PublicationProcess(self):
        return self.__research32_PublicationProcess

    @research32_PublicationProcess.setter
    def research32_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_PublicationProcess__research32_PublicationProcess", None)
        self.__research32_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research32_Phase"):
                    opp_val = getattr(item, "research32_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "research32_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research32_Phase"):
                    opp_val = getattr(item, "research32_Phase", None)
                    
                    setattr(item, "research32_Phase", self)
                    

    @property
    def research32_PublicationProcess43(self):
        return self.__research32_PublicationProcess43

    @research32_PublicationProcess43.setter
    def research32_PublicationProcess43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_PublicationProcess__research32_PublicationProcess43", None)
        self.__research32_PublicationProcess43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_PublicationSystem"):
                opp_val = getattr(old_value, "research32_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "research32_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_PublicationSystem"):
                opp_val = getattr(value, "research32_PublicationSystem", None)
                setattr(value, "research32_PublicationSystem", self)

    @property
    def research32_PublicationProcess24(self):
        return self.__research32_PublicationProcess24

    @research32_PublicationProcess24.setter
    def research32_PublicationProcess24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research32_PublicationProcess__research32_PublicationProcess24", None)
        self.__research32_PublicationProcess24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research32_Progress"):
                opp_val = getattr(old_value, "research32_Progress", None)
                if opp_val == self:
                    setattr(old_value, "research32_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research32_Progress"):
                opp_val = getattr(value, "research32_Progress", None)
                setattr(value, "research32_Progress", self)
