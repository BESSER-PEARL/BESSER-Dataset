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

class StateMachineObject:

    pass
class research16_Transition(StateMachineObject):

    def __init__(self, guardLabel: str, guardExpression: str, research16_Transition: set["research16_Action"] = None, research16_Transition71: "research16_State" = None, research16_Transition74: "research16_State" = None, research16_Transition78: "research16_State" = None):
        self.guardLabel = guardLabel
        self.guardExpression = guardExpression
        self.research16_Transition = research16_Transition if research16_Transition is not None else set()
        self.research16_Transition71 = research16_Transition71
        self.research16_Transition74 = research16_Transition74
        self.research16_Transition78 = research16_Transition78
        
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
    def research16_Transition(self):
        return self.__research16_Transition

    @research16_Transition.setter
    def research16_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Transition__research16_Transition", None)
        self.__research16_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research16_Action"):
                    opp_val = getattr(item, "research16_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "research16_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research16_Action"):
                    opp_val = getattr(item, "research16_Action", None)
                    
                    setattr(item, "research16_Action", self)
                    

    @property
    def research16_Transition74(self):
        return self.__research16_Transition74

    @research16_Transition74.setter
    def research16_Transition74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Transition__research16_Transition74", None)
        self.__research16_Transition74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_State75"):
                opp_val = getattr(old_value, "research16_State75", None)
                if opp_val == self:
                    setattr(old_value, "research16_State75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_State75"):
                opp_val = getattr(value, "research16_State75", None)
                setattr(value, "research16_State75", self)

    @property
    def research16_Transition78(self):
        return self.__research16_Transition78

    @research16_Transition78.setter
    def research16_Transition78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Transition__research16_Transition78", None)
        self.__research16_Transition78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_State77"):
                opp_val = getattr(old_value, "research16_State77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_State77"):
                opp_val = getattr(value, "research16_State77", None)
                if opp_val is None:
                    setattr(value, "research16_State77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research16_Transition71(self):
        return self.__research16_Transition71

    @research16_Transition71.setter
    def research16_Transition71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Transition__research16_Transition71", None)
        self.__research16_Transition71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_State72"):
                opp_val = getattr(old_value, "research16_State72", None)
                if opp_val == self:
                    setattr(old_value, "research16_State72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_State72"):
                opp_val = getattr(value, "research16_State72", None)
                setattr(value, "research16_State72", self)

class research16_StateMachineObject(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class research16_StateMachineVariable:

    pass
class research16_Action:

    def __init__(self, actionLabel: str, actionStatement: str, research16_Action: "research16_Transition" = None, research16_Action81: "research16_State" = None, research16_Action84: "research16_Action" = None, research16_Action82: "research16_Action" = None):
        self.actionLabel = actionLabel
        self.actionStatement = actionStatement
        self.research16_Action = research16_Action
        self.research16_Action81 = research16_Action81
        self.research16_Action84 = research16_Action84
        self.research16_Action82 = research16_Action82
        
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
    def research16_Action82(self):
        return self.__research16_Action82

    @research16_Action82.setter
    def research16_Action82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Action__research16_Action82", None)
        self.__research16_Action82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Action84"):
                opp_val = getattr(old_value, "research16_Action84", None)
                if opp_val == self:
                    setattr(old_value, "research16_Action84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Action84"):
                opp_val = getattr(value, "research16_Action84", None)
                setattr(value, "research16_Action84", self)

    @property
    def research16_Action81(self):
        return self.__research16_Action81

    @research16_Action81.setter
    def research16_Action81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Action__research16_Action81", None)
        self.__research16_Action81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_State80"):
                opp_val = getattr(old_value, "research16_State80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_State80"):
                opp_val = getattr(value, "research16_State80", None)
                if opp_val is None:
                    setattr(value, "research16_State80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research16_Action(self):
        return self.__research16_Action

    @research16_Action.setter
    def research16_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Action__research16_Action", None)
        self.__research16_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Transition"):
                opp_val = getattr(old_value, "research16_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Transition"):
                opp_val = getattr(value, "research16_Transition", None)
                if opp_val is None:
                    setattr(value, "research16_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research16_Action84(self):
        return self.__research16_Action84

    @research16_Action84.setter
    def research16_Action84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Action__research16_Action84", None)
        self.__research16_Action84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Action82"):
                opp_val = getattr(old_value, "research16_Action82", None)
                if opp_val == self:
                    setattr(old_value, "research16_Action82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Action82"):
                opp_val = getattr(value, "research16_Action82", None)
                setattr(value, "research16_Action82", self)

class research16_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class research16_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class research16_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class research16_PublicationStatus:

    def __init__(self, label: str, research16_PublicationStatus: "research16_PublicationSystem" = None, research16_PublicationStatus65: set["research16_StateMachineVariable"] = None, research16_PublicationStatus67: set["research16_State"] = None):
        self.label = label
        self.research16_PublicationStatus = research16_PublicationStatus
        self.research16_PublicationStatus65 = research16_PublicationStatus65 if research16_PublicationStatus65 is not None else set()
        self.research16_PublicationStatus67 = research16_PublicationStatus67 if research16_PublicationStatus67 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def research16_PublicationStatus67(self):
        return self.__research16_PublicationStatus67

    @research16_PublicationStatus67.setter
    def research16_PublicationStatus67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_PublicationStatus__research16_PublicationStatus67", None)
        self.__research16_PublicationStatus67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research16_State68"):
                    opp_val = getattr(item, "research16_State68", None)
                    
                    if opp_val == self:
                        setattr(item, "research16_State68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research16_State68"):
                    opp_val = getattr(item, "research16_State68", None)
                    
                    setattr(item, "research16_State68", self)
                    

    @property
    def research16_PublicationStatus(self):
        return self.__research16_PublicationStatus

    @research16_PublicationStatus.setter
    def research16_PublicationStatus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_PublicationStatus__research16_PublicationStatus", None)
        self.__research16_PublicationStatus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_PublicationSystem49"):
                opp_val = getattr(old_value, "research16_PublicationSystem49", None)
                if opp_val == self:
                    setattr(old_value, "research16_PublicationSystem49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_PublicationSystem49"):
                opp_val = getattr(value, "research16_PublicationSystem49", None)
                setattr(value, "research16_PublicationSystem49", self)

    @property
    def research16_PublicationStatus65(self):
        return self.__research16_PublicationStatus65

    @research16_PublicationStatus65.setter
    def research16_PublicationStatus65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_PublicationStatus__research16_PublicationStatus65", None)
        self.__research16_PublicationStatus65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research16_StateMachineVariable"):
                    opp_val = getattr(item, "research16_StateMachineVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "research16_StateMachineVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research16_StateMachineVariable"):
                    opp_val = getattr(item, "research16_StateMachineVariable", None)
                    
                    setattr(item, "research16_StateMachineVariable", self)
                    

class Counted:

    pass
class research16_State(StateMachineObject):

    def __init__(self, id: int, kind: str, name: str, research16_State: "research16_Paper" = None, research16_State72: "research16_Transition" = None, research16_State75: "research16_Transition" = None, research16_State77: set["research16_Transition"] = None, research16_State80: set["research16_Action"] = None, research16_State68: "research16_PublicationStatus" = None):
        self.id = id
        self.kind = kind
        self.name = name
        self.research16_State = research16_State
        self.research16_State72 = research16_State72
        self.research16_State75 = research16_State75
        self.research16_State77 = research16_State77 if research16_State77 is not None else set()
        self.research16_State80 = research16_State80 if research16_State80 is not None else set()
        self.research16_State68 = research16_State68
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research16_State72(self):
        return self.__research16_State72

    @research16_State72.setter
    def research16_State72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_State__research16_State72", None)
        self.__research16_State72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Transition71"):
                opp_val = getattr(old_value, "research16_Transition71", None)
                if opp_val == self:
                    setattr(old_value, "research16_Transition71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Transition71"):
                opp_val = getattr(value, "research16_Transition71", None)
                setattr(value, "research16_Transition71", self)

    @property
    def research16_State80(self):
        return self.__research16_State80

    @research16_State80.setter
    def research16_State80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_State__research16_State80", None)
        self.__research16_State80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research16_Action81"):
                    opp_val = getattr(item, "research16_Action81", None)
                    
                    if opp_val == self:
                        setattr(item, "research16_Action81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research16_Action81"):
                    opp_val = getattr(item, "research16_Action81", None)
                    
                    setattr(item, "research16_Action81", self)
                    

    @property
    def research16_State68(self):
        return self.__research16_State68

    @research16_State68.setter
    def research16_State68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_State__research16_State68", None)
        self.__research16_State68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_PublicationStatus67"):
                opp_val = getattr(old_value, "research16_PublicationStatus67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_PublicationStatus67"):
                opp_val = getattr(value, "research16_PublicationStatus67", None)
                if opp_val is None:
                    setattr(value, "research16_PublicationStatus67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research16_State75(self):
        return self.__research16_State75

    @research16_State75.setter
    def research16_State75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_State__research16_State75", None)
        self.__research16_State75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Transition74"):
                opp_val = getattr(old_value, "research16_Transition74", None)
                if opp_val == self:
                    setattr(old_value, "research16_Transition74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Transition74"):
                opp_val = getattr(value, "research16_Transition74", None)
                setattr(value, "research16_Transition74", self)

    @property
    def research16_State77(self):
        return self.__research16_State77

    @research16_State77.setter
    def research16_State77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_State__research16_State77", None)
        self.__research16_State77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research16_Transition78"):
                    opp_val = getattr(item, "research16_Transition78", None)
                    
                    if opp_val == self:
                        setattr(item, "research16_Transition78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research16_Transition78"):
                    opp_val = getattr(item, "research16_Transition78", None)
                    
                    setattr(item, "research16_Transition78", self)
                    

    @property
    def research16_State(self):
        return self.__research16_State

    @research16_State.setter
    def research16_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_State__research16_State", None)
        self.__research16_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Paper20"):
                opp_val = getattr(old_value, "research16_Paper20", None)
                if opp_val == self:
                    setattr(old_value, "research16_Paper20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Paper20"):
                opp_val = getattr(value, "research16_Paper20", None)
                setattr(value, "research16_Paper20", self)

class Labelled:

    pass
class research16_Skill:

    def __init__(self, description: str, research16_Skill: "research16_Researcher" = None):
        self.description = description
        self.research16_Skill = research16_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research16_Skill(self):
        return self.__research16_Skill

    @research16_Skill.setter
    def research16_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Skill__research16_Skill", None)
        self.__research16_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Researcher6"):
                opp_val = getattr(old_value, "research16_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Researcher6"):
                opp_val = getattr(value, "research16_Researcher6", None)
                if opp_val is None:
                    setattr(value, "research16_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research16_Review(Labelled):

    def __init__(self, date: date, research16_Review: "research16_Researcher" = None, research16_Review31: "research16_ReviewNote" = None):
        self.date = date
        self.research16_Review = research16_Review
        self.research16_Review31 = research16_Review31
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def research16_Review31(self):
        return self.__research16_Review31

    @research16_Review31.setter
    def research16_Review31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Review__research16_Review31", None)
        self.__research16_Review31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_ReviewNote32"):
                opp_val = getattr(old_value, "research16_ReviewNote32", None)
                if opp_val == self:
                    setattr(old_value, "research16_ReviewNote32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_ReviewNote32"):
                opp_val = getattr(value, "research16_ReviewNote32", None)
                setattr(value, "research16_ReviewNote32", self)

    @property
    def research16_Review(self):
        return self.__research16_Review

    @research16_Review.setter
    def research16_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Review__research16_Review", None)
        self.__research16_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Researcher3"):
                opp_val = getattr(old_value, "research16_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Researcher3"):
                opp_val = getattr(value, "research16_Researcher3", None)
                if opp_val is None:
                    setattr(value, "research16_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research16_Write(Labelled):

    def __init__(self, timeSpent: int, research16_Write: "research16_Researcher" = None, research16_Write28: "research16_Paragraph" = None):
        self.timeSpent = timeSpent
        self.research16_Write = research16_Write
        self.research16_Write28 = research16_Write28
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def research16_Write28(self):
        return self.__research16_Write28

    @research16_Write28.setter
    def research16_Write28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Write__research16_Write28", None)
        self.__research16_Write28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Paragraph29"):
                opp_val = getattr(old_value, "research16_Paragraph29", None)
                if opp_val == self:
                    setattr(old_value, "research16_Paragraph29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Paragraph29"):
                opp_val = getattr(value, "research16_Paragraph29", None)
                setattr(value, "research16_Paragraph29", self)

    @property
    def research16_Write(self):
        return self.__research16_Write

    @research16_Write.setter
    def research16_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Write__research16_Write", None)
        self.__research16_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Researcher"):
                opp_val = getattr(old_value, "research16_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Researcher"):
                opp_val = getattr(value, "research16_Researcher", None)
                if opp_val is None:
                    setattr(value, "research16_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research16_Researcher:

    def __init__(self, name: str, forName: str, research16_Researcher10: set["research16_Collaboration"] = None, Researcher: "research16_Paper" = None, research16_Researcher: set["research16_Write"] = None, research16_Researcher3: set["research16_Review"] = None, authors: set["research16_Paper"] = None, research16_Researcher6: set["research16_Skill"] = None, research16_Researcher8: "research16_Position" = None, research16_Researcher34: "research16_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.research16_Researcher10 = research16_Researcher10 if research16_Researcher10 is not None else set()
        self.Researcher = Researcher
        self.research16_Researcher = research16_Researcher if research16_Researcher is not None else set()
        self.research16_Researcher3 = research16_Researcher3 if research16_Researcher3 is not None else set()
        self.authors = authors if authors is not None else set()
        self.research16_Researcher6 = research16_Researcher6 if research16_Researcher6 is not None else set()
        self.research16_Researcher8 = research16_Researcher8
        self.research16_Researcher34 = research16_Researcher34
        
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
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Researcher__authors", None)
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
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Researcher__Researcher", None)
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
    def research16_Researcher6(self):
        return self.__research16_Researcher6

    @research16_Researcher6.setter
    def research16_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Researcher__research16_Researcher6", None)
        self.__research16_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research16_Skill"):
                    opp_val = getattr(item, "research16_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "research16_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research16_Skill"):
                    opp_val = getattr(item, "research16_Skill", None)
                    
                    setattr(item, "research16_Skill", self)
                    

    @property
    def research16_Researcher8(self):
        return self.__research16_Researcher8

    @research16_Researcher8.setter
    def research16_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Researcher__research16_Researcher8", None)
        self.__research16_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Position"):
                opp_val = getattr(old_value, "research16_Position", None)
                if opp_val == self:
                    setattr(old_value, "research16_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Position"):
                opp_val = getattr(value, "research16_Position", None)
                setattr(value, "research16_Position", self)

    @property
    def research16_Researcher3(self):
        return self.__research16_Researcher3

    @research16_Researcher3.setter
    def research16_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Researcher__research16_Researcher3", None)
        self.__research16_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research16_Review"):
                    opp_val = getattr(item, "research16_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "research16_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research16_Review"):
                    opp_val = getattr(item, "research16_Review", None)
                    
                    setattr(item, "research16_Review", self)
                    

    @property
    def research16_Researcher34(self):
        return self.__research16_Researcher34

    @research16_Researcher34.setter
    def research16_Researcher34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Researcher__research16_Researcher34", None)
        self.__research16_Researcher34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_PublicationStructure"):
                opp_val = getattr(old_value, "research16_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_PublicationStructure"):
                opp_val = getattr(value, "research16_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "research16_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research16_Researcher(self):
        return self.__research16_Researcher

    @research16_Researcher.setter
    def research16_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Researcher__research16_Researcher", None)
        self.__research16_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research16_Write"):
                    opp_val = getattr(item, "research16_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "research16_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research16_Write"):
                    opp_val = getattr(item, "research16_Write", None)
                    
                    setattr(item, "research16_Write", self)
                    

    @property
    def research16_Researcher10(self):
        return self.__research16_Researcher10

    @research16_Researcher10.setter
    def research16_Researcher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Researcher__research16_Researcher10", None)
        self.__research16_Researcher10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research16_Collaboration"):
                    opp_val = getattr(item, "research16_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "research16_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research16_Collaboration"):
                    opp_val = getattr(item, "research16_Collaboration", None)
                    
                    setattr(item, "research16_Collaboration", self)
                    

class research16_PaperKeyword:

    def __init__(self, weight: int, research16_PaperKeyword: "research16_Paper" = None, research16_PaperKeyword59: "research16_Keyword" = None):
        self.weight = weight
        self.research16_PaperKeyword = research16_PaperKeyword
        self.research16_PaperKeyword59 = research16_PaperKeyword59
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def research16_PaperKeyword(self):
        return self.__research16_PaperKeyword

    @research16_PaperKeyword.setter
    def research16_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_PaperKeyword__research16_PaperKeyword", None)
        self.__research16_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Paper15"):
                opp_val = getattr(old_value, "research16_Paper15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Paper15"):
                opp_val = getattr(value, "research16_Paper15", None)
                if opp_val is None:
                    setattr(value, "research16_Paper15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research16_PaperKeyword59(self):
        return self.__research16_PaperKeyword59

    @research16_PaperKeyword59.setter
    def research16_PaperKeyword59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_PaperKeyword__research16_PaperKeyword59", None)
        self.__research16_PaperKeyword59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Keyword60"):
                opp_val = getattr(old_value, "research16_Keyword60", None)
                if opp_val == self:
                    setattr(old_value, "research16_Keyword60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Keyword60"):
                opp_val = getattr(value, "research16_Keyword60", None)
                setattr(value, "research16_Keyword60", self)

class research16_Progress(Labelled):

    def __init__(self, percent: int, Progress: "research16_Paper" = None, research16_Progress: "research16_PublicationProcess" = None, progress: "research16_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.research16_Progress = research16_Progress
        self.progress = progress
        
    @property
    def percent(self) -> int:
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent

    @property
    def research16_Progress(self):
        return self.__research16_Progress

    @research16_Progress.setter
    def research16_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Progress__research16_Progress", None)
        self.__research16_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_PublicationProcess24"):
                opp_val = getattr(old_value, "research16_PublicationProcess24", None)
                if opp_val == self:
                    setattr(old_value, "research16_PublicationProcess24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_PublicationProcess24"):
                opp_val = getattr(value, "research16_PublicationProcess24", None)
                setattr(value, "research16_PublicationProcess24", self)

    @property
    def Progress(self):
        return self.__Progress

    @Progress.setter
    def Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Progress__Progress", None)
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
        old_value = getattr(self, f"_research16_Progress__progress", None)
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

class research16_Collaboration:

    def __init__(self, ratio: int, research16_Collaboration: "research16_Researcher" = None, research16_Collaboration62: "research16_Paper" = None):
        self.ratio = ratio
        self.research16_Collaboration = research16_Collaboration
        self.research16_Collaboration62 = research16_Collaboration62
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def research16_Collaboration(self):
        return self.__research16_Collaboration

    @research16_Collaboration.setter
    def research16_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Collaboration__research16_Collaboration", None)
        self.__research16_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Researcher10"):
                opp_val = getattr(old_value, "research16_Researcher10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Researcher10"):
                opp_val = getattr(value, "research16_Researcher10", None)
                if opp_val is None:
                    setattr(value, "research16_Researcher10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research16_Collaboration62(self):
        return self.__research16_Collaboration62

    @research16_Collaboration62.setter
    def research16_Collaboration62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Collaboration__research16_Collaboration62", None)
        self.__research16_Collaboration62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Paper63"):
                opp_val = getattr(old_value, "research16_Paper63", None)
                if opp_val == self:
                    setattr(old_value, "research16_Paper63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Paper63"):
                opp_val = getattr(value, "research16_Paper63", None)
                setattr(value, "research16_Paper63", self)

class research16_Phase:

    def __init__(self, name: str, research16_Phase: "research16_PublicationProcess" = None):
        self.name = name
        self.research16_Phase = research16_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research16_Phase(self):
        return self.__research16_Phase

    @research16_Phase.setter
    def research16_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Phase__research16_Phase", None)
        self.__research16_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_PublicationProcess"):
                opp_val = getattr(old_value, "research16_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_PublicationProcess"):
                opp_val = getattr(value, "research16_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "research16_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class research16_Paragraph(Counted, Named):

    def __init__(self, content: str, research16_Paragraph: "research16_Paper" = None, research16_Paragraph29: "research16_Write" = None, research16_Paragraph22: set["research16_ReviewNote"] = None):
        self.content = content
        self.research16_Paragraph = research16_Paragraph
        self.research16_Paragraph29 = research16_Paragraph29
        self.research16_Paragraph22 = research16_Paragraph22 if research16_Paragraph22 is not None else set()
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research16_Paragraph29(self):
        return self.__research16_Paragraph29

    @research16_Paragraph29.setter
    def research16_Paragraph29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Paragraph__research16_Paragraph29", None)
        self.__research16_Paragraph29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Write28"):
                opp_val = getattr(old_value, "research16_Write28", None)
                if opp_val == self:
                    setattr(old_value, "research16_Write28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Write28"):
                opp_val = getattr(value, "research16_Write28", None)
                setattr(value, "research16_Write28", self)

    @property
    def research16_Paragraph(self):
        return self.__research16_Paragraph

    @research16_Paragraph.setter
    def research16_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Paragraph__research16_Paragraph", None)
        self.__research16_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Paper"):
                opp_val = getattr(old_value, "research16_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Paper"):
                opp_val = getattr(value, "research16_Paper", None)
                if opp_val is None:
                    setattr(value, "research16_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research16_Paragraph22(self):
        return self.__research16_Paragraph22

    @research16_Paragraph22.setter
    def research16_Paragraph22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Paragraph__research16_Paragraph22", None)
        self.__research16_Paragraph22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research16_ReviewNote"):
                    opp_val = getattr(item, "research16_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "research16_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research16_ReviewNote"):
                    opp_val = getattr(item, "research16_ReviewNote", None)
                    
                    setattr(item, "research16_ReviewNote", self)
                    

class research16_KnowledgeManager(Named):

    pass
class research16_ReviewNote(Named):

    def __init__(self, content: str, research16_ReviewNote32: "research16_Review" = None, research16_ReviewNote: "research16_Paragraph" = None):
        self.content = content
        self.research16_ReviewNote32 = research16_ReviewNote32
        self.research16_ReviewNote = research16_ReviewNote
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research16_ReviewNote32(self):
        return self.__research16_ReviewNote32

    @research16_ReviewNote32.setter
    def research16_ReviewNote32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_ReviewNote__research16_ReviewNote32", None)
        self.__research16_ReviewNote32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Review31"):
                opp_val = getattr(old_value, "research16_Review31", None)
                if opp_val == self:
                    setattr(old_value, "research16_Review31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Review31"):
                opp_val = getattr(value, "research16_Review31", None)
                setattr(value, "research16_Review31", self)

    @property
    def research16_ReviewNote(self):
        return self.__research16_ReviewNote

    @research16_ReviewNote.setter
    def research16_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_ReviewNote__research16_ReviewNote", None)
        self.__research16_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Paragraph22"):
                opp_val = getattr(old_value, "research16_Paragraph22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Paragraph22"):
                opp_val = getattr(value, "research16_Paragraph22", None)
                if opp_val is None:
                    setattr(value, "research16_Paragraph22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research16_PublicationStructure(Named):

    pass
class research16_Keyword(Named):

    def __init__(self, word: str, research16_Keyword: set["research16_Paper"] = None, research16_Keyword57: "research16_KnowledgeManager" = None, research16_Keyword60: "research16_PaperKeyword" = None):
        self.word = word
        self.research16_Keyword = research16_Keyword if research16_Keyword is not None else set()
        self.research16_Keyword57 = research16_Keyword57
        self.research16_Keyword60 = research16_Keyword60
        
    @property
    def word(self) -> str:
        return self.__word

    @word.setter
    def word(self, word: str):
        self.__word = word

    @property
    def research16_Keyword57(self):
        return self.__research16_Keyword57

    @research16_Keyword57.setter
    def research16_Keyword57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Keyword__research16_Keyword57", None)
        self.__research16_Keyword57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_KnowledgeManager56"):
                opp_val = getattr(old_value, "research16_KnowledgeManager56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_KnowledgeManager56"):
                opp_val = getattr(value, "research16_KnowledgeManager56", None)
                if opp_val is None:
                    setattr(value, "research16_KnowledgeManager56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research16_Keyword(self):
        return self.__research16_Keyword

    @research16_Keyword.setter
    def research16_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Keyword__research16_Keyword", None)
        self.__research16_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research16_Paper54"):
                    opp_val = getattr(item, "research16_Paper54", None)
                    
                    if opp_val == self:
                        setattr(item, "research16_Paper54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research16_Paper54"):
                    opp_val = getattr(item, "research16_Paper54", None)
                    
                    setattr(item, "research16_Paper54", self)
                    

    @property
    def research16_Keyword60(self):
        return self.__research16_Keyword60

    @research16_Keyword60.setter
    def research16_Keyword60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Keyword__research16_Keyword60", None)
        self.__research16_Keyword60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_PaperKeyword59"):
                opp_val = getattr(old_value, "research16_PaperKeyword59", None)
                if opp_val == self:
                    setattr(old_value, "research16_PaperKeyword59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_PaperKeyword59"):
                opp_val = getattr(value, "research16_PaperKeyword59", None)
                setattr(value, "research16_PaperKeyword59", self)

class research16_Paper(Named):

    pass
class research16_PublicationSystem(Named):

    pass
class research16_Position(Named):

    def __init__(self, description: str, research16_Position: "research16_Researcher" = None, research16_Position47: "research16_PublicationSystem" = None, research16_Position52: "research16_Position" = None, research16_Position50: "research16_Position" = None):
        self.description = description
        self.research16_Position = research16_Position
        self.research16_Position47 = research16_Position47
        self.research16_Position52 = research16_Position52
        self.research16_Position50 = research16_Position50
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research16_Position(self):
        return self.__research16_Position

    @research16_Position.setter
    def research16_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Position__research16_Position", None)
        self.__research16_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Researcher8"):
                opp_val = getattr(old_value, "research16_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "research16_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Researcher8"):
                opp_val = getattr(value, "research16_Researcher8", None)
                setattr(value, "research16_Researcher8", self)

    @property
    def research16_Position50(self):
        return self.__research16_Position50

    @research16_Position50.setter
    def research16_Position50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Position__research16_Position50", None)
        self.__research16_Position50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Position52"):
                opp_val = getattr(old_value, "research16_Position52", None)
                if opp_val == self:
                    setattr(old_value, "research16_Position52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Position52"):
                opp_val = getattr(value, "research16_Position52", None)
                setattr(value, "research16_Position52", self)

    @property
    def research16_Position52(self):
        return self.__research16_Position52

    @research16_Position52.setter
    def research16_Position52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Position__research16_Position52", None)
        self.__research16_Position52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Position50"):
                opp_val = getattr(old_value, "research16_Position50", None)
                if opp_val == self:
                    setattr(old_value, "research16_Position50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Position50"):
                opp_val = getattr(value, "research16_Position50", None)
                setattr(value, "research16_Position50", self)

    @property
    def research16_Position47(self):
        return self.__research16_Position47

    @research16_Position47.setter
    def research16_Position47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_Position__research16_Position47", None)
        self.__research16_Position47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_PublicationSystem46"):
                opp_val = getattr(old_value, "research16_PublicationSystem46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_PublicationSystem46"):
                opp_val = getattr(value, "research16_PublicationSystem46", None)
                if opp_val is None:
                    setattr(value, "research16_PublicationSystem46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research16_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, research16_PublicationProcess: set["research16_Phase"] = None, research16_PublicationProcess24: "research16_Progress" = None, research16_PublicationProcess41: "research16_PublicationSystem" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.research16_PublicationProcess = research16_PublicationProcess if research16_PublicationProcess is not None else set()
        self.research16_PublicationProcess24 = research16_PublicationProcess24
        self.research16_PublicationProcess41 = research16_PublicationProcess41
        
    @property
    def minTime(self) -> int:
        return self.__minTime

    @minTime.setter
    def minTime(self, minTime: int):
        self.__minTime = minTime

    @property
    def maxTime(self) -> int:
        return self.__maxTime

    @maxTime.setter
    def maxTime(self, maxTime: int):
        self.__maxTime = maxTime

    @property
    def research16_PublicationProcess24(self):
        return self.__research16_PublicationProcess24

    @research16_PublicationProcess24.setter
    def research16_PublicationProcess24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_PublicationProcess__research16_PublicationProcess24", None)
        self.__research16_PublicationProcess24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_Progress"):
                opp_val = getattr(old_value, "research16_Progress", None)
                if opp_val == self:
                    setattr(old_value, "research16_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_Progress"):
                opp_val = getattr(value, "research16_Progress", None)
                setattr(value, "research16_Progress", self)

    @property
    def research16_PublicationProcess41(self):
        return self.__research16_PublicationProcess41

    @research16_PublicationProcess41.setter
    def research16_PublicationProcess41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_PublicationProcess__research16_PublicationProcess41", None)
        self.__research16_PublicationProcess41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research16_PublicationSystem"):
                opp_val = getattr(old_value, "research16_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "research16_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research16_PublicationSystem"):
                opp_val = getattr(value, "research16_PublicationSystem", None)
                setattr(value, "research16_PublicationSystem", self)

    @property
    def research16_PublicationProcess(self):
        return self.__research16_PublicationProcess

    @research16_PublicationProcess.setter
    def research16_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research16_PublicationProcess__research16_PublicationProcess", None)
        self.__research16_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research16_Phase"):
                    opp_val = getattr(item, "research16_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "research16_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research16_Phase"):
                    opp_val = getattr(item, "research16_Phase", None)
                    
                    setattr(item, "research16_Phase", self)
                    
