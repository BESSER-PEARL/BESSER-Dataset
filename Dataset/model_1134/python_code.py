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

class research23_StateMachineVariable:

    pass
class research23_Action:

    def __init__(self, actionLabel: str, actionStatement: str, research23_Action: "research23_Transition" = None, research23_Action81: "research23_State" = None, research23_Action84: "research23_Action" = None, research23_Action82: "research23_Action" = None):
        self.actionLabel = actionLabel
        self.actionStatement = actionStatement
        self.research23_Action = research23_Action
        self.research23_Action81 = research23_Action81
        self.research23_Action84 = research23_Action84
        self.research23_Action82 = research23_Action82
        
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
    def research23_Action81(self):
        return self.__research23_Action81

    @research23_Action81.setter
    def research23_Action81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Action__research23_Action81", None)
        self.__research23_Action81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_State80"):
                opp_val = getattr(old_value, "research23_State80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_State80"):
                opp_val = getattr(value, "research23_State80", None)
                if opp_val is None:
                    setattr(value, "research23_State80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research23_Action(self):
        return self.__research23_Action

    @research23_Action.setter
    def research23_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Action__research23_Action", None)
        self.__research23_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Transition"):
                opp_val = getattr(old_value, "research23_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Transition"):
                opp_val = getattr(value, "research23_Transition", None)
                if opp_val is None:
                    setattr(value, "research23_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research23_Action84(self):
        return self.__research23_Action84

    @research23_Action84.setter
    def research23_Action84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Action__research23_Action84", None)
        self.__research23_Action84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Action82"):
                opp_val = getattr(old_value, "research23_Action82", None)
                if opp_val == self:
                    setattr(old_value, "research23_Action82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Action82"):
                opp_val = getattr(value, "research23_Action82", None)
                setattr(value, "research23_Action82", self)

    @property
    def research23_Action82(self):
        return self.__research23_Action82

    @research23_Action82.setter
    def research23_Action82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Action__research23_Action82", None)
        self.__research23_Action82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Action84"):
                opp_val = getattr(old_value, "research23_Action84", None)
                if opp_val == self:
                    setattr(old_value, "research23_Action84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Action84"):
                opp_val = getattr(value, "research23_Action84", None)
                setattr(value, "research23_Action84", self)

class StateMachineObject:

    pass
class research23_Transition(StateMachineObject):

    def __init__(self, guardLabel: str, guardExpression: str, research23_Transition: set["research23_Action"] = None, research23_Transition71: "research23_State" = None, research23_Transition74: "research23_State" = None, research23_Transition78: "research23_State" = None):
        self.guardLabel = guardLabel
        self.guardExpression = guardExpression
        self.research23_Transition = research23_Transition if research23_Transition is not None else set()
        self.research23_Transition71 = research23_Transition71
        self.research23_Transition74 = research23_Transition74
        self.research23_Transition78 = research23_Transition78
        
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
    def research23_Transition(self):
        return self.__research23_Transition

    @research23_Transition.setter
    def research23_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Transition__research23_Transition", None)
        self.__research23_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research23_Action"):
                    opp_val = getattr(item, "research23_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "research23_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research23_Action"):
                    opp_val = getattr(item, "research23_Action", None)
                    
                    setattr(item, "research23_Action", self)
                    

    @property
    def research23_Transition74(self):
        return self.__research23_Transition74

    @research23_Transition74.setter
    def research23_Transition74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Transition__research23_Transition74", None)
        self.__research23_Transition74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_State75"):
                opp_val = getattr(old_value, "research23_State75", None)
                if opp_val == self:
                    setattr(old_value, "research23_State75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_State75"):
                opp_val = getattr(value, "research23_State75", None)
                setattr(value, "research23_State75", self)

    @property
    def research23_Transition71(self):
        return self.__research23_Transition71

    @research23_Transition71.setter
    def research23_Transition71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Transition__research23_Transition71", None)
        self.__research23_Transition71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_State72"):
                opp_val = getattr(old_value, "research23_State72", None)
                if opp_val == self:
                    setattr(old_value, "research23_State72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_State72"):
                opp_val = getattr(value, "research23_State72", None)
                setattr(value, "research23_State72", self)

    @property
    def research23_Transition78(self):
        return self.__research23_Transition78

    @research23_Transition78.setter
    def research23_Transition78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Transition__research23_Transition78", None)
        self.__research23_Transition78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_State77"):
                opp_val = getattr(old_value, "research23_State77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_State77"):
                opp_val = getattr(value, "research23_State77", None)
                if opp_val is None:
                    setattr(value, "research23_State77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research23_StateMachineObject(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class research23_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class research23_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class research23_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class research23_PublicationStatus:

    def __init__(self, label: str, research23_PublicationStatus: "research23_PublicationStructure" = None, research23_PublicationStatus67: set["research23_State"] = None, research23_PublicationStatus65: set["research23_StateMachineVariable"] = None):
        self.label = label
        self.research23_PublicationStatus = research23_PublicationStatus
        self.research23_PublicationStatus67 = research23_PublicationStatus67 if research23_PublicationStatus67 is not None else set()
        self.research23_PublicationStatus65 = research23_PublicationStatus65 if research23_PublicationStatus65 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def research23_PublicationStatus67(self):
        return self.__research23_PublicationStatus67

    @research23_PublicationStatus67.setter
    def research23_PublicationStatus67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_PublicationStatus__research23_PublicationStatus67", None)
        self.__research23_PublicationStatus67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research23_State68"):
                    opp_val = getattr(item, "research23_State68", None)
                    
                    if opp_val == self:
                        setattr(item, "research23_State68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research23_State68"):
                    opp_val = getattr(item, "research23_State68", None)
                    
                    setattr(item, "research23_State68", self)
                    

    @property
    def research23_PublicationStatus65(self):
        return self.__research23_PublicationStatus65

    @research23_PublicationStatus65.setter
    def research23_PublicationStatus65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_PublicationStatus__research23_PublicationStatus65", None)
        self.__research23_PublicationStatus65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research23_StateMachineVariable"):
                    opp_val = getattr(item, "research23_StateMachineVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "research23_StateMachineVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research23_StateMachineVariable"):
                    opp_val = getattr(item, "research23_StateMachineVariable", None)
                    
                    setattr(item, "research23_StateMachineVariable", self)
                    

    @property
    def research23_PublicationStatus(self):
        return self.__research23_PublicationStatus

    @research23_PublicationStatus.setter
    def research23_PublicationStatus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_PublicationStatus__research23_PublicationStatus", None)
        self.__research23_PublicationStatus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_PublicationStructure41"):
                opp_val = getattr(old_value, "research23_PublicationStructure41", None)
                if opp_val == self:
                    setattr(old_value, "research23_PublicationStructure41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_PublicationStructure41"):
                opp_val = getattr(value, "research23_PublicationStructure41", None)
                setattr(value, "research23_PublicationStructure41", self)

class research23_PaperKeyword:

    def __init__(self, weight: int, research23_PaperKeyword: "research23_Paper" = None, research23_PaperKeyword59: "research23_Keyword" = None):
        self.weight = weight
        self.research23_PaperKeyword = research23_PaperKeyword
        self.research23_PaperKeyword59 = research23_PaperKeyword59
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def research23_PaperKeyword(self):
        return self.__research23_PaperKeyword

    @research23_PaperKeyword.setter
    def research23_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_PaperKeyword__research23_PaperKeyword", None)
        self.__research23_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Paper15"):
                opp_val = getattr(old_value, "research23_Paper15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Paper15"):
                opp_val = getattr(value, "research23_Paper15", None)
                if opp_val is None:
                    setattr(value, "research23_Paper15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research23_PaperKeyword59(self):
        return self.__research23_PaperKeyword59

    @research23_PaperKeyword59.setter
    def research23_PaperKeyword59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_PaperKeyword__research23_PaperKeyword59", None)
        self.__research23_PaperKeyword59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Keyword60"):
                opp_val = getattr(old_value, "research23_Keyword60", None)
                if opp_val == self:
                    setattr(old_value, "research23_Keyword60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Keyword60"):
                opp_val = getattr(value, "research23_Keyword60", None)
                setattr(value, "research23_Keyword60", self)

class Labelled:

    pass
class Counted:

    pass
class research23_State(StateMachineObject):

    def __init__(self, id: int, kind: str, name: str, research23_State: "research23_Paper" = None, research23_State68: "research23_PublicationStatus" = None, research23_State72: "research23_Transition" = None, research23_State75: "research23_Transition" = None, research23_State77: set["research23_Transition"] = None, research23_State80: set["research23_Action"] = None):
        self.id = id
        self.kind = kind
        self.name = name
        self.research23_State = research23_State
        self.research23_State68 = research23_State68
        self.research23_State72 = research23_State72
        self.research23_State75 = research23_State75
        self.research23_State77 = research23_State77 if research23_State77 is not None else set()
        self.research23_State80 = research23_State80 if research23_State80 is not None else set()
        
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
    def research23_State68(self):
        return self.__research23_State68

    @research23_State68.setter
    def research23_State68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_State__research23_State68", None)
        self.__research23_State68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_PublicationStatus67"):
                opp_val = getattr(old_value, "research23_PublicationStatus67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_PublicationStatus67"):
                opp_val = getattr(value, "research23_PublicationStatus67", None)
                if opp_val is None:
                    setattr(value, "research23_PublicationStatus67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research23_State72(self):
        return self.__research23_State72

    @research23_State72.setter
    def research23_State72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_State__research23_State72", None)
        self.__research23_State72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Transition71"):
                opp_val = getattr(old_value, "research23_Transition71", None)
                if opp_val == self:
                    setattr(old_value, "research23_Transition71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Transition71"):
                opp_val = getattr(value, "research23_Transition71", None)
                setattr(value, "research23_Transition71", self)

    @property
    def research23_State80(self):
        return self.__research23_State80

    @research23_State80.setter
    def research23_State80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_State__research23_State80", None)
        self.__research23_State80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research23_Action81"):
                    opp_val = getattr(item, "research23_Action81", None)
                    
                    if opp_val == self:
                        setattr(item, "research23_Action81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research23_Action81"):
                    opp_val = getattr(item, "research23_Action81", None)
                    
                    setattr(item, "research23_Action81", self)
                    

    @property
    def research23_State75(self):
        return self.__research23_State75

    @research23_State75.setter
    def research23_State75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_State__research23_State75", None)
        self.__research23_State75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Transition74"):
                opp_val = getattr(old_value, "research23_Transition74", None)
                if opp_val == self:
                    setattr(old_value, "research23_Transition74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Transition74"):
                opp_val = getattr(value, "research23_Transition74", None)
                setattr(value, "research23_Transition74", self)

    @property
    def research23_State(self):
        return self.__research23_State

    @research23_State.setter
    def research23_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_State__research23_State", None)
        self.__research23_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Paper20"):
                opp_val = getattr(old_value, "research23_Paper20", None)
                if opp_val == self:
                    setattr(old_value, "research23_Paper20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Paper20"):
                opp_val = getattr(value, "research23_Paper20", None)
                setattr(value, "research23_Paper20", self)

    @property
    def research23_State77(self):
        return self.__research23_State77

    @research23_State77.setter
    def research23_State77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_State__research23_State77", None)
        self.__research23_State77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research23_Transition78"):
                    opp_val = getattr(item, "research23_Transition78", None)
                    
                    if opp_val == self:
                        setattr(item, "research23_Transition78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research23_Transition78"):
                    opp_val = getattr(item, "research23_Transition78", None)
                    
                    setattr(item, "research23_Transition78", self)
                    

class research23_Phase:

    def __init__(self, name: str, research23_Phase: "research23_PublicationProcess" = None):
        self.name = name
        self.research23_Phase = research23_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research23_Phase(self):
        return self.__research23_Phase

    @research23_Phase.setter
    def research23_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Phase__research23_Phase", None)
        self.__research23_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_PublicationProcess"):
                opp_val = getattr(old_value, "research23_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_PublicationProcess"):
                opp_val = getattr(value, "research23_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "research23_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research23_Progress(Labelled):

    def __init__(self, percent: int, Progress: "research23_Paper" = None, research23_Progress: "research23_PublicationProcess" = None, progress: "research23_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.research23_Progress = research23_Progress
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
        old_value = getattr(self, f"_research23_Progress__Progress", None)
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
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Progress__progress", None)
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

    @property
    def research23_Progress(self):
        return self.__research23_Progress

    @research23_Progress.setter
    def research23_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Progress__research23_Progress", None)
        self.__research23_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_PublicationProcess24"):
                opp_val = getattr(old_value, "research23_PublicationProcess24", None)
                if opp_val == self:
                    setattr(old_value, "research23_PublicationProcess24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_PublicationProcess24"):
                opp_val = getattr(value, "research23_PublicationProcess24", None)
                setattr(value, "research23_PublicationProcess24", self)

class research23_Collaboration:

    def __init__(self, ratio: int, research23_Collaboration: "research23_Researcher" = None, research23_Collaboration62: "research23_Paper" = None):
        self.ratio = ratio
        self.research23_Collaboration = research23_Collaboration
        self.research23_Collaboration62 = research23_Collaboration62
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def research23_Collaboration62(self):
        return self.__research23_Collaboration62

    @research23_Collaboration62.setter
    def research23_Collaboration62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Collaboration__research23_Collaboration62", None)
        self.__research23_Collaboration62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Paper63"):
                opp_val = getattr(old_value, "research23_Paper63", None)
                if opp_val == self:
                    setattr(old_value, "research23_Paper63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Paper63"):
                opp_val = getattr(value, "research23_Paper63", None)
                setattr(value, "research23_Paper63", self)

    @property
    def research23_Collaboration(self):
        return self.__research23_Collaboration

    @research23_Collaboration.setter
    def research23_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Collaboration__research23_Collaboration", None)
        self.__research23_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Researcher10"):
                opp_val = getattr(old_value, "research23_Researcher10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Researcher10"):
                opp_val = getattr(value, "research23_Researcher10", None)
                if opp_val is None:
                    setattr(value, "research23_Researcher10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research23_Skill:

    def __init__(self, description: str, research23_Skill: "research23_Researcher" = None):
        self.description = description
        self.research23_Skill = research23_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research23_Skill(self):
        return self.__research23_Skill

    @research23_Skill.setter
    def research23_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Skill__research23_Skill", None)
        self.__research23_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Researcher6"):
                opp_val = getattr(old_value, "research23_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Researcher6"):
                opp_val = getattr(value, "research23_Researcher6", None)
                if opp_val is None:
                    setattr(value, "research23_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research23_Review(Labelled):

    def __init__(self, date: date, research23_Review: "research23_Researcher" = None, research23_Review31: "research23_ReviewNote" = None):
        self.date = date
        self.research23_Review = research23_Review
        self.research23_Review31 = research23_Review31
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def research23_Review(self):
        return self.__research23_Review

    @research23_Review.setter
    def research23_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Review__research23_Review", None)
        self.__research23_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Researcher3"):
                opp_val = getattr(old_value, "research23_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Researcher3"):
                opp_val = getattr(value, "research23_Researcher3", None)
                if opp_val is None:
                    setattr(value, "research23_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research23_Review31(self):
        return self.__research23_Review31

    @research23_Review31.setter
    def research23_Review31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Review__research23_Review31", None)
        self.__research23_Review31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_ReviewNote32"):
                opp_val = getattr(old_value, "research23_ReviewNote32", None)
                if opp_val == self:
                    setattr(old_value, "research23_ReviewNote32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_ReviewNote32"):
                opp_val = getattr(value, "research23_ReviewNote32", None)
                setattr(value, "research23_ReviewNote32", self)

class research23_Write(Labelled):

    def __init__(self, timeSpent: int, research23_Write: "research23_Researcher" = None, research23_Write28: "research23_Paragraph" = None):
        self.timeSpent = timeSpent
        self.research23_Write = research23_Write
        self.research23_Write28 = research23_Write28
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def research23_Write(self):
        return self.__research23_Write

    @research23_Write.setter
    def research23_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Write__research23_Write", None)
        self.__research23_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Researcher"):
                opp_val = getattr(old_value, "research23_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Researcher"):
                opp_val = getattr(value, "research23_Researcher", None)
                if opp_val is None:
                    setattr(value, "research23_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research23_Write28(self):
        return self.__research23_Write28

    @research23_Write28.setter
    def research23_Write28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Write__research23_Write28", None)
        self.__research23_Write28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Paragraph29"):
                opp_val = getattr(old_value, "research23_Paragraph29", None)
                if opp_val == self:
                    setattr(old_value, "research23_Paragraph29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Paragraph29"):
                opp_val = getattr(value, "research23_Paragraph29", None)
                setattr(value, "research23_Paragraph29", self)

class research23_Researcher:

    def __init__(self, name: str, forName: str, research23_Researcher: set["research23_Write"] = None, research23_Researcher3: set["research23_Review"] = None, authors: set["research23_Paper"] = None, research23_Researcher6: set["research23_Skill"] = None, research23_Researcher8: "research23_Position" = None, research23_Researcher10: set["research23_Collaboration"] = None, Researcher: "research23_Paper" = None, research23_Researcher34: "research23_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.research23_Researcher = research23_Researcher if research23_Researcher is not None else set()
        self.research23_Researcher3 = research23_Researcher3 if research23_Researcher3 is not None else set()
        self.authors = authors if authors is not None else set()
        self.research23_Researcher6 = research23_Researcher6 if research23_Researcher6 is not None else set()
        self.research23_Researcher8 = research23_Researcher8
        self.research23_Researcher10 = research23_Researcher10 if research23_Researcher10 is not None else set()
        self.Researcher = Researcher
        self.research23_Researcher34 = research23_Researcher34
        
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
    def research23_Researcher34(self):
        return self.__research23_Researcher34

    @research23_Researcher34.setter
    def research23_Researcher34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Researcher__research23_Researcher34", None)
        self.__research23_Researcher34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_PublicationStructure"):
                opp_val = getattr(old_value, "research23_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_PublicationStructure"):
                opp_val = getattr(value, "research23_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "research23_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research23_Researcher(self):
        return self.__research23_Researcher

    @research23_Researcher.setter
    def research23_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Researcher__research23_Researcher", None)
        self.__research23_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research23_Write"):
                    opp_val = getattr(item, "research23_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "research23_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research23_Write"):
                    opp_val = getattr(item, "research23_Write", None)
                    
                    setattr(item, "research23_Write", self)
                    

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Researcher__Researcher", None)
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
    def research23_Researcher10(self):
        return self.__research23_Researcher10

    @research23_Researcher10.setter
    def research23_Researcher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Researcher__research23_Researcher10", None)
        self.__research23_Researcher10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research23_Collaboration"):
                    opp_val = getattr(item, "research23_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "research23_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research23_Collaboration"):
                    opp_val = getattr(item, "research23_Collaboration", None)
                    
                    setattr(item, "research23_Collaboration", self)
                    

    @property
    def research23_Researcher6(self):
        return self.__research23_Researcher6

    @research23_Researcher6.setter
    def research23_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Researcher__research23_Researcher6", None)
        self.__research23_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research23_Skill"):
                    opp_val = getattr(item, "research23_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "research23_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research23_Skill"):
                    opp_val = getattr(item, "research23_Skill", None)
                    
                    setattr(item, "research23_Skill", self)
                    

    @property
    def research23_Researcher3(self):
        return self.__research23_Researcher3

    @research23_Researcher3.setter
    def research23_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Researcher__research23_Researcher3", None)
        self.__research23_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research23_Review"):
                    opp_val = getattr(item, "research23_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "research23_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research23_Review"):
                    opp_val = getattr(item, "research23_Review", None)
                    
                    setattr(item, "research23_Review", self)
                    

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Researcher__authors", None)
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
    def research23_Researcher8(self):
        return self.__research23_Researcher8

    @research23_Researcher8.setter
    def research23_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Researcher__research23_Researcher8", None)
        self.__research23_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Position"):
                opp_val = getattr(old_value, "research23_Position", None)
                if opp_val == self:
                    setattr(old_value, "research23_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Position"):
                opp_val = getattr(value, "research23_Position", None)
                setattr(value, "research23_Position", self)

class Named:

    pass
class research23_KnowledgeManager(Named):

    pass
class research23_PublicationStructure(Named):

    pass
class research23_Position(Named):

    def __init__(self, description: str, research23_Position: "research23_Researcher" = None, research23_Position49: "research23_PublicationSystem" = None, research23_Position52: "research23_Position" = None, research23_Position50: "research23_Position" = None):
        self.description = description
        self.research23_Position = research23_Position
        self.research23_Position49 = research23_Position49
        self.research23_Position52 = research23_Position52
        self.research23_Position50 = research23_Position50
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research23_Position50(self):
        return self.__research23_Position50

    @research23_Position50.setter
    def research23_Position50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Position__research23_Position50", None)
        self.__research23_Position50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Position52"):
                opp_val = getattr(old_value, "research23_Position52", None)
                if opp_val == self:
                    setattr(old_value, "research23_Position52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Position52"):
                opp_val = getattr(value, "research23_Position52", None)
                setattr(value, "research23_Position52", self)

    @property
    def research23_Position52(self):
        return self.__research23_Position52

    @research23_Position52.setter
    def research23_Position52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Position__research23_Position52", None)
        self.__research23_Position52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Position50"):
                opp_val = getattr(old_value, "research23_Position50", None)
                if opp_val == self:
                    setattr(old_value, "research23_Position50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Position50"):
                opp_val = getattr(value, "research23_Position50", None)
                setattr(value, "research23_Position50", self)

    @property
    def research23_Position49(self):
        return self.__research23_Position49

    @research23_Position49.setter
    def research23_Position49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Position__research23_Position49", None)
        self.__research23_Position49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_PublicationSystem48"):
                opp_val = getattr(old_value, "research23_PublicationSystem48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_PublicationSystem48"):
                opp_val = getattr(value, "research23_PublicationSystem48", None)
                if opp_val is None:
                    setattr(value, "research23_PublicationSystem48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research23_Position(self):
        return self.__research23_Position

    @research23_Position.setter
    def research23_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Position__research23_Position", None)
        self.__research23_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Researcher8"):
                opp_val = getattr(old_value, "research23_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "research23_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Researcher8"):
                opp_val = getattr(value, "research23_Researcher8", None)
                setattr(value, "research23_Researcher8", self)

class research23_PublicationSystem(Named):

    pass
class research23_ReviewNote(Named):

    def __init__(self, content: str, research23_ReviewNote: "research23_Paragraph" = None, research23_ReviewNote32: "research23_Review" = None):
        self.content = content
        self.research23_ReviewNote = research23_ReviewNote
        self.research23_ReviewNote32 = research23_ReviewNote32
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research23_ReviewNote(self):
        return self.__research23_ReviewNote

    @research23_ReviewNote.setter
    def research23_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_ReviewNote__research23_ReviewNote", None)
        self.__research23_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Paragraph22"):
                opp_val = getattr(old_value, "research23_Paragraph22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Paragraph22"):
                opp_val = getattr(value, "research23_Paragraph22", None)
                if opp_val is None:
                    setattr(value, "research23_Paragraph22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research23_ReviewNote32(self):
        return self.__research23_ReviewNote32

    @research23_ReviewNote32.setter
    def research23_ReviewNote32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_ReviewNote__research23_ReviewNote32", None)
        self.__research23_ReviewNote32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Review31"):
                opp_val = getattr(old_value, "research23_Review31", None)
                if opp_val == self:
                    setattr(old_value, "research23_Review31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Review31"):
                opp_val = getattr(value, "research23_Review31", None)
                setattr(value, "research23_Review31", self)

class research23_Paragraph(Named, Counted):

    def __init__(self, content: str, research23_Paragraph: "research23_Paper" = None, research23_Paragraph22: set["research23_ReviewNote"] = None, research23_Paragraph29: "research23_Write" = None):
        self.content = content
        self.research23_Paragraph = research23_Paragraph
        self.research23_Paragraph22 = research23_Paragraph22 if research23_Paragraph22 is not None else set()
        self.research23_Paragraph29 = research23_Paragraph29
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research23_Paragraph(self):
        return self.__research23_Paragraph

    @research23_Paragraph.setter
    def research23_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Paragraph__research23_Paragraph", None)
        self.__research23_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Paper"):
                opp_val = getattr(old_value, "research23_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Paper"):
                opp_val = getattr(value, "research23_Paper", None)
                if opp_val is None:
                    setattr(value, "research23_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research23_Paragraph22(self):
        return self.__research23_Paragraph22

    @research23_Paragraph22.setter
    def research23_Paragraph22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Paragraph__research23_Paragraph22", None)
        self.__research23_Paragraph22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research23_ReviewNote"):
                    opp_val = getattr(item, "research23_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "research23_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research23_ReviewNote"):
                    opp_val = getattr(item, "research23_ReviewNote", None)
                    
                    setattr(item, "research23_ReviewNote", self)
                    

    @property
    def research23_Paragraph29(self):
        return self.__research23_Paragraph29

    @research23_Paragraph29.setter
    def research23_Paragraph29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Paragraph__research23_Paragraph29", None)
        self.__research23_Paragraph29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Write28"):
                opp_val = getattr(old_value, "research23_Write28", None)
                if opp_val == self:
                    setattr(old_value, "research23_Write28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Write28"):
                opp_val = getattr(value, "research23_Write28", None)
                setattr(value, "research23_Write28", self)

class research23_Paper(Named):

    pass
class research23_Keyword(Named):

    def __init__(self, word: str, research23_Keyword: set["research23_Paper"] = None, research23_Keyword57: "research23_KnowledgeManager" = None, research23_Keyword60: "research23_PaperKeyword" = None):
        self.word = word
        self.research23_Keyword = research23_Keyword if research23_Keyword is not None else set()
        self.research23_Keyword57 = research23_Keyword57
        self.research23_Keyword60 = research23_Keyword60
        
    @property
    def word(self) -> str:
        return self.__word

    @word.setter
    def word(self, word: str):
        self.__word = word

    @property
    def research23_Keyword60(self):
        return self.__research23_Keyword60

    @research23_Keyword60.setter
    def research23_Keyword60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Keyword__research23_Keyword60", None)
        self.__research23_Keyword60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_PaperKeyword59"):
                opp_val = getattr(old_value, "research23_PaperKeyword59", None)
                if opp_val == self:
                    setattr(old_value, "research23_PaperKeyword59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_PaperKeyword59"):
                opp_val = getattr(value, "research23_PaperKeyword59", None)
                setattr(value, "research23_PaperKeyword59", self)

    @property
    def research23_Keyword57(self):
        return self.__research23_Keyword57

    @research23_Keyword57.setter
    def research23_Keyword57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Keyword__research23_Keyword57", None)
        self.__research23_Keyword57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_KnowledgeManager56"):
                opp_val = getattr(old_value, "research23_KnowledgeManager56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_KnowledgeManager56"):
                opp_val = getattr(value, "research23_KnowledgeManager56", None)
                if opp_val is None:
                    setattr(value, "research23_KnowledgeManager56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research23_Keyword(self):
        return self.__research23_Keyword

    @research23_Keyword.setter
    def research23_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_Keyword__research23_Keyword", None)
        self.__research23_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research23_Paper54"):
                    opp_val = getattr(item, "research23_Paper54", None)
                    
                    if opp_val == self:
                        setattr(item, "research23_Paper54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research23_Paper54"):
                    opp_val = getattr(item, "research23_Paper54", None)
                    
                    setattr(item, "research23_Paper54", self)
                    

class research23_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, research23_PublicationProcess: set["research23_Phase"] = None, research23_PublicationProcess24: "research23_Progress" = None, research23_PublicationProcess43: "research23_PublicationSystem" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.research23_PublicationProcess = research23_PublicationProcess if research23_PublicationProcess is not None else set()
        self.research23_PublicationProcess24 = research23_PublicationProcess24
        self.research23_PublicationProcess43 = research23_PublicationProcess43
        
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
    def research23_PublicationProcess24(self):
        return self.__research23_PublicationProcess24

    @research23_PublicationProcess24.setter
    def research23_PublicationProcess24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_PublicationProcess__research23_PublicationProcess24", None)
        self.__research23_PublicationProcess24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_Progress"):
                opp_val = getattr(old_value, "research23_Progress", None)
                if opp_val == self:
                    setattr(old_value, "research23_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_Progress"):
                opp_val = getattr(value, "research23_Progress", None)
                setattr(value, "research23_Progress", self)

    @property
    def research23_PublicationProcess(self):
        return self.__research23_PublicationProcess

    @research23_PublicationProcess.setter
    def research23_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_PublicationProcess__research23_PublicationProcess", None)
        self.__research23_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research23_Phase"):
                    opp_val = getattr(item, "research23_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "research23_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research23_Phase"):
                    opp_val = getattr(item, "research23_Phase", None)
                    
                    setattr(item, "research23_Phase", self)
                    

    @property
    def research23_PublicationProcess43(self):
        return self.__research23_PublicationProcess43

    @research23_PublicationProcess43.setter
    def research23_PublicationProcess43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research23_PublicationProcess__research23_PublicationProcess43", None)
        self.__research23_PublicationProcess43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research23_PublicationSystem"):
                opp_val = getattr(old_value, "research23_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "research23_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research23_PublicationSystem"):
                opp_val = getattr(value, "research23_PublicationSystem", None)
                setattr(value, "research23_PublicationSystem", self)
