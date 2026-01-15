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

class research19_Action:

    def __init__(self, actionLabel: str, actionStatement: str, research19_Action84: "research19_Action" = None, research19_Action82: "research19_Action" = None, research19_Action: "research19_Transition" = None, research19_Action81: "research19_State" = None):
        self.actionLabel = actionLabel
        self.actionStatement = actionStatement
        self.research19_Action84 = research19_Action84
        self.research19_Action82 = research19_Action82
        self.research19_Action = research19_Action
        self.research19_Action81 = research19_Action81
        
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
    def research19_Action81(self):
        return self.__research19_Action81

    @research19_Action81.setter
    def research19_Action81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Action__research19_Action81", None)
        self.__research19_Action81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_State80"):
                opp_val = getattr(old_value, "research19_State80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_State80"):
                opp_val = getattr(value, "research19_State80", None)
                if opp_val is None:
                    setattr(value, "research19_State80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research19_Action(self):
        return self.__research19_Action

    @research19_Action.setter
    def research19_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Action__research19_Action", None)
        self.__research19_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Transition"):
                opp_val = getattr(old_value, "research19_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Transition"):
                opp_val = getattr(value, "research19_Transition", None)
                if opp_val is None:
                    setattr(value, "research19_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research19_Action84(self):
        return self.__research19_Action84

    @research19_Action84.setter
    def research19_Action84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Action__research19_Action84", None)
        self.__research19_Action84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Action82"):
                opp_val = getattr(old_value, "research19_Action82", None)
                if opp_val == self:
                    setattr(old_value, "research19_Action82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Action82"):
                opp_val = getattr(value, "research19_Action82", None)
                setattr(value, "research19_Action82", self)

    @property
    def research19_Action82(self):
        return self.__research19_Action82

    @research19_Action82.setter
    def research19_Action82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Action__research19_Action82", None)
        self.__research19_Action82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Action84"):
                opp_val = getattr(old_value, "research19_Action84", None)
                if opp_val == self:
                    setattr(old_value, "research19_Action84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Action84"):
                opp_val = getattr(value, "research19_Action84", None)
                setattr(value, "research19_Action84", self)

class StateMachineObject:

    pass
class research19_Transition(StateMachineObject):

    def __init__(self, guardLabel: str, guardExpression: str, research19_Transition: set["research19_Action"] = None, research19_Transition71: "research19_State" = None, research19_Transition74: "research19_State" = None, research19_Transition78: "research19_State" = None):
        self.guardLabel = guardLabel
        self.guardExpression = guardExpression
        self.research19_Transition = research19_Transition if research19_Transition is not None else set()
        self.research19_Transition71 = research19_Transition71
        self.research19_Transition74 = research19_Transition74
        self.research19_Transition78 = research19_Transition78
        
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
    def research19_Transition78(self):
        return self.__research19_Transition78

    @research19_Transition78.setter
    def research19_Transition78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Transition__research19_Transition78", None)
        self.__research19_Transition78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_State77"):
                opp_val = getattr(old_value, "research19_State77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_State77"):
                opp_val = getattr(value, "research19_State77", None)
                if opp_val is None:
                    setattr(value, "research19_State77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research19_Transition71(self):
        return self.__research19_Transition71

    @research19_Transition71.setter
    def research19_Transition71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Transition__research19_Transition71", None)
        self.__research19_Transition71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_State72"):
                opp_val = getattr(old_value, "research19_State72", None)
                if opp_val == self:
                    setattr(old_value, "research19_State72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_State72"):
                opp_val = getattr(value, "research19_State72", None)
                setattr(value, "research19_State72", self)

    @property
    def research19_Transition(self):
        return self.__research19_Transition

    @research19_Transition.setter
    def research19_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Transition__research19_Transition", None)
        self.__research19_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research19_Action"):
                    opp_val = getattr(item, "research19_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "research19_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research19_Action"):
                    opp_val = getattr(item, "research19_Action", None)
                    
                    setattr(item, "research19_Action", self)
                    

    @property
    def research19_Transition74(self):
        return self.__research19_Transition74

    @research19_Transition74.setter
    def research19_Transition74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Transition__research19_Transition74", None)
        self.__research19_Transition74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_State75"):
                opp_val = getattr(old_value, "research19_State75", None)
                if opp_val == self:
                    setattr(old_value, "research19_State75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_State75"):
                opp_val = getattr(value, "research19_State75", None)
                setattr(value, "research19_State75", self)

class research19_StateMachineObject(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class research19_StateMachineVariable:

    pass
class research19_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class research19_PublicationStatus:

    def __init__(self, label: str, research19_PublicationStatus: "research19_PublicationSystem" = None, research19_PublicationStatus65: set["research19_StateMachineVariable"] = None, research19_PublicationStatus67: set["research19_State"] = None):
        self.label = label
        self.research19_PublicationStatus = research19_PublicationStatus
        self.research19_PublicationStatus65 = research19_PublicationStatus65 if research19_PublicationStatus65 is not None else set()
        self.research19_PublicationStatus67 = research19_PublicationStatus67 if research19_PublicationStatus67 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def research19_PublicationStatus65(self):
        return self.__research19_PublicationStatus65

    @research19_PublicationStatus65.setter
    def research19_PublicationStatus65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_PublicationStatus__research19_PublicationStatus65", None)
        self.__research19_PublicationStatus65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research19_StateMachineVariable"):
                    opp_val = getattr(item, "research19_StateMachineVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "research19_StateMachineVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research19_StateMachineVariable"):
                    opp_val = getattr(item, "research19_StateMachineVariable", None)
                    
                    setattr(item, "research19_StateMachineVariable", self)
                    

    @property
    def research19_PublicationStatus67(self):
        return self.__research19_PublicationStatus67

    @research19_PublicationStatus67.setter
    def research19_PublicationStatus67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_PublicationStatus__research19_PublicationStatus67", None)
        self.__research19_PublicationStatus67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research19_State68"):
                    opp_val = getattr(item, "research19_State68", None)
                    
                    if opp_val == self:
                        setattr(item, "research19_State68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research19_State68"):
                    opp_val = getattr(item, "research19_State68", None)
                    
                    setattr(item, "research19_State68", self)
                    

    @property
    def research19_PublicationStatus(self):
        return self.__research19_PublicationStatus

    @research19_PublicationStatus.setter
    def research19_PublicationStatus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_PublicationStatus__research19_PublicationStatus", None)
        self.__research19_PublicationStatus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_PublicationSystem49"):
                opp_val = getattr(old_value, "research19_PublicationSystem49", None)
                if opp_val == self:
                    setattr(old_value, "research19_PublicationSystem49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_PublicationSystem49"):
                opp_val = getattr(value, "research19_PublicationSystem49", None)
                setattr(value, "research19_PublicationSystem49", self)

class research19_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class research19_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class Labelled:

    pass
class Counted:

    pass
class research19_Collaboration:

    def __init__(self, ratio: int, research19_Collaboration: "research19_Researcher" = None, research19_Collaboration62: "research19_Paper" = None):
        self.ratio = ratio
        self.research19_Collaboration = research19_Collaboration
        self.research19_Collaboration62 = research19_Collaboration62
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def research19_Collaboration62(self):
        return self.__research19_Collaboration62

    @research19_Collaboration62.setter
    def research19_Collaboration62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Collaboration__research19_Collaboration62", None)
        self.__research19_Collaboration62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Paper63"):
                opp_val = getattr(old_value, "research19_Paper63", None)
                if opp_val == self:
                    setattr(old_value, "research19_Paper63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Paper63"):
                opp_val = getattr(value, "research19_Paper63", None)
                setattr(value, "research19_Paper63", self)

    @property
    def research19_Collaboration(self):
        return self.__research19_Collaboration

    @research19_Collaboration.setter
    def research19_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Collaboration__research19_Collaboration", None)
        self.__research19_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Researcher10"):
                opp_val = getattr(old_value, "research19_Researcher10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Researcher10"):
                opp_val = getattr(value, "research19_Researcher10", None)
                if opp_val is None:
                    setattr(value, "research19_Researcher10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research19_Skill:

    def __init__(self, description: str, research19_Skill: "research19_Researcher" = None):
        self.description = description
        self.research19_Skill = research19_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research19_Skill(self):
        return self.__research19_Skill

    @research19_Skill.setter
    def research19_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Skill__research19_Skill", None)
        self.__research19_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Researcher6"):
                opp_val = getattr(old_value, "research19_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Researcher6"):
                opp_val = getattr(value, "research19_Researcher6", None)
                if opp_val is None:
                    setattr(value, "research19_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research19_Review(Labelled):

    def __init__(self, date: date, research19_Review: "research19_Researcher" = None, research19_Review31: "research19_ReviewNote" = None):
        self.date = date
        self.research19_Review = research19_Review
        self.research19_Review31 = research19_Review31
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def research19_Review(self):
        return self.__research19_Review

    @research19_Review.setter
    def research19_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Review__research19_Review", None)
        self.__research19_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Researcher3"):
                opp_val = getattr(old_value, "research19_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Researcher3"):
                opp_val = getattr(value, "research19_Researcher3", None)
                if opp_val is None:
                    setattr(value, "research19_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research19_Review31(self):
        return self.__research19_Review31

    @research19_Review31.setter
    def research19_Review31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Review__research19_Review31", None)
        self.__research19_Review31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_ReviewNote32"):
                opp_val = getattr(old_value, "research19_ReviewNote32", None)
                if opp_val == self:
                    setattr(old_value, "research19_ReviewNote32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_ReviewNote32"):
                opp_val = getattr(value, "research19_ReviewNote32", None)
                setattr(value, "research19_ReviewNote32", self)

class research19_Write(Labelled):

    def __init__(self, timeSpent: int, research19_Write: "research19_Researcher" = None, research19_Write28: "research19_Paragraph" = None):
        self.timeSpent = timeSpent
        self.research19_Write = research19_Write
        self.research19_Write28 = research19_Write28
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def research19_Write28(self):
        return self.__research19_Write28

    @research19_Write28.setter
    def research19_Write28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Write__research19_Write28", None)
        self.__research19_Write28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Paragraph29"):
                opp_val = getattr(old_value, "research19_Paragraph29", None)
                if opp_val == self:
                    setattr(old_value, "research19_Paragraph29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Paragraph29"):
                opp_val = getattr(value, "research19_Paragraph29", None)
                setattr(value, "research19_Paragraph29", self)

    @property
    def research19_Write(self):
        return self.__research19_Write

    @research19_Write.setter
    def research19_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Write__research19_Write", None)
        self.__research19_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Researcher"):
                opp_val = getattr(old_value, "research19_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Researcher"):
                opp_val = getattr(value, "research19_Researcher", None)
                if opp_val is None:
                    setattr(value, "research19_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research19_State(StateMachineObject):

    def __init__(self, id: int, kind: str, name: str, research19_State: "research19_Paper" = None, research19_State68: "research19_PublicationStatus" = None, research19_State72: "research19_Transition" = None, research19_State75: "research19_Transition" = None, research19_State77: set["research19_Transition"] = None, research19_State80: set["research19_Action"] = None):
        self.id = id
        self.kind = kind
        self.name = name
        self.research19_State = research19_State
        self.research19_State68 = research19_State68
        self.research19_State72 = research19_State72
        self.research19_State75 = research19_State75
        self.research19_State77 = research19_State77 if research19_State77 is not None else set()
        self.research19_State80 = research19_State80 if research19_State80 is not None else set()
        
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
    def research19_State77(self):
        return self.__research19_State77

    @research19_State77.setter
    def research19_State77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_State__research19_State77", None)
        self.__research19_State77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research19_Transition78"):
                    opp_val = getattr(item, "research19_Transition78", None)
                    
                    if opp_val == self:
                        setattr(item, "research19_Transition78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research19_Transition78"):
                    opp_val = getattr(item, "research19_Transition78", None)
                    
                    setattr(item, "research19_Transition78", self)
                    

    @property
    def research19_State(self):
        return self.__research19_State

    @research19_State.setter
    def research19_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_State__research19_State", None)
        self.__research19_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Paper20"):
                opp_val = getattr(old_value, "research19_Paper20", None)
                if opp_val == self:
                    setattr(old_value, "research19_Paper20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Paper20"):
                opp_val = getattr(value, "research19_Paper20", None)
                setattr(value, "research19_Paper20", self)

    @property
    def research19_State75(self):
        return self.__research19_State75

    @research19_State75.setter
    def research19_State75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_State__research19_State75", None)
        self.__research19_State75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Transition74"):
                opp_val = getattr(old_value, "research19_Transition74", None)
                if opp_val == self:
                    setattr(old_value, "research19_Transition74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Transition74"):
                opp_val = getattr(value, "research19_Transition74", None)
                setattr(value, "research19_Transition74", self)

    @property
    def research19_State72(self):
        return self.__research19_State72

    @research19_State72.setter
    def research19_State72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_State__research19_State72", None)
        self.__research19_State72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Transition71"):
                opp_val = getattr(old_value, "research19_Transition71", None)
                if opp_val == self:
                    setattr(old_value, "research19_Transition71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Transition71"):
                opp_val = getattr(value, "research19_Transition71", None)
                setattr(value, "research19_Transition71", self)

    @property
    def research19_State80(self):
        return self.__research19_State80

    @research19_State80.setter
    def research19_State80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_State__research19_State80", None)
        self.__research19_State80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research19_Action81"):
                    opp_val = getattr(item, "research19_Action81", None)
                    
                    if opp_val == self:
                        setattr(item, "research19_Action81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research19_Action81"):
                    opp_val = getattr(item, "research19_Action81", None)
                    
                    setattr(item, "research19_Action81", self)
                    

    @property
    def research19_State68(self):
        return self.__research19_State68

    @research19_State68.setter
    def research19_State68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_State__research19_State68", None)
        self.__research19_State68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_PublicationStatus67"):
                opp_val = getattr(old_value, "research19_PublicationStatus67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_PublicationStatus67"):
                opp_val = getattr(value, "research19_PublicationStatus67", None)
                if opp_val is None:
                    setattr(value, "research19_PublicationStatus67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research19_PaperKeyword:

    def __init__(self, weight: int, research19_PaperKeyword: "research19_Paper" = None, research19_PaperKeyword59: "research19_Keyword" = None):
        self.weight = weight
        self.research19_PaperKeyword = research19_PaperKeyword
        self.research19_PaperKeyword59 = research19_PaperKeyword59
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def research19_PaperKeyword(self):
        return self.__research19_PaperKeyword

    @research19_PaperKeyword.setter
    def research19_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_PaperKeyword__research19_PaperKeyword", None)
        self.__research19_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Paper15"):
                opp_val = getattr(old_value, "research19_Paper15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Paper15"):
                opp_val = getattr(value, "research19_Paper15", None)
                if opp_val is None:
                    setattr(value, "research19_Paper15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research19_PaperKeyword59(self):
        return self.__research19_PaperKeyword59

    @research19_PaperKeyword59.setter
    def research19_PaperKeyword59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_PaperKeyword__research19_PaperKeyword59", None)
        self.__research19_PaperKeyword59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Keyword60"):
                opp_val = getattr(old_value, "research19_Keyword60", None)
                if opp_val == self:
                    setattr(old_value, "research19_Keyword60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Keyword60"):
                opp_val = getattr(value, "research19_Keyword60", None)
                setattr(value, "research19_Keyword60", self)

class research19_Progress(Labelled):

    def __init__(self, percent: int, Progress: "research19_Paper" = None, research19_Progress: "research19_PublicationProcess" = None, progress: "research19_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.research19_Progress = research19_Progress
        self.progress = progress
        
    @property
    def percent(self) -> int:
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Progress__progress", None)
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
    def Progress(self):
        return self.__Progress

    @Progress.setter
    def Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Progress__Progress", None)
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
    def research19_Progress(self):
        return self.__research19_Progress

    @research19_Progress.setter
    def research19_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Progress__research19_Progress", None)
        self.__research19_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_PublicationProcess24"):
                opp_val = getattr(old_value, "research19_PublicationProcess24", None)
                if opp_val == self:
                    setattr(old_value, "research19_PublicationProcess24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_PublicationProcess24"):
                opp_val = getattr(value, "research19_PublicationProcess24", None)
                setattr(value, "research19_PublicationProcess24", self)

class research19_Researcher:

    def __init__(self, name: str, forName: str, Researcher: "research19_Paper" = None, research19_Researcher: set["research19_Write"] = None, research19_Researcher3: set["research19_Review"] = None, authors: set["research19_Paper"] = None, research19_Researcher6: set["research19_Skill"] = None, research19_Researcher8: "research19_Position" = None, research19_Researcher10: set["research19_Collaboration"] = None, research19_Researcher34: "research19_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.Researcher = Researcher
        self.research19_Researcher = research19_Researcher if research19_Researcher is not None else set()
        self.research19_Researcher3 = research19_Researcher3 if research19_Researcher3 is not None else set()
        self.authors = authors if authors is not None else set()
        self.research19_Researcher6 = research19_Researcher6 if research19_Researcher6 is not None else set()
        self.research19_Researcher8 = research19_Researcher8
        self.research19_Researcher10 = research19_Researcher10 if research19_Researcher10 is not None else set()
        self.research19_Researcher34 = research19_Researcher34
        
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
    def research19_Researcher(self):
        return self.__research19_Researcher

    @research19_Researcher.setter
    def research19_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Researcher__research19_Researcher", None)
        self.__research19_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research19_Write"):
                    opp_val = getattr(item, "research19_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "research19_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research19_Write"):
                    opp_val = getattr(item, "research19_Write", None)
                    
                    setattr(item, "research19_Write", self)
                    

    @property
    def research19_Researcher3(self):
        return self.__research19_Researcher3

    @research19_Researcher3.setter
    def research19_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Researcher__research19_Researcher3", None)
        self.__research19_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research19_Review"):
                    opp_val = getattr(item, "research19_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "research19_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research19_Review"):
                    opp_val = getattr(item, "research19_Review", None)
                    
                    setattr(item, "research19_Review", self)
                    

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Researcher__Researcher", None)
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
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Researcher__authors", None)
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
    def research19_Researcher8(self):
        return self.__research19_Researcher8

    @research19_Researcher8.setter
    def research19_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Researcher__research19_Researcher8", None)
        self.__research19_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Position"):
                opp_val = getattr(old_value, "research19_Position", None)
                if opp_val == self:
                    setattr(old_value, "research19_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Position"):
                opp_val = getattr(value, "research19_Position", None)
                setattr(value, "research19_Position", self)

    @property
    def research19_Researcher34(self):
        return self.__research19_Researcher34

    @research19_Researcher34.setter
    def research19_Researcher34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Researcher__research19_Researcher34", None)
        self.__research19_Researcher34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_PublicationStructure"):
                opp_val = getattr(old_value, "research19_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_PublicationStructure"):
                opp_val = getattr(value, "research19_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "research19_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research19_Researcher6(self):
        return self.__research19_Researcher6

    @research19_Researcher6.setter
    def research19_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Researcher__research19_Researcher6", None)
        self.__research19_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research19_Skill"):
                    opp_val = getattr(item, "research19_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "research19_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research19_Skill"):
                    opp_val = getattr(item, "research19_Skill", None)
                    
                    setattr(item, "research19_Skill", self)
                    

    @property
    def research19_Researcher10(self):
        return self.__research19_Researcher10

    @research19_Researcher10.setter
    def research19_Researcher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Researcher__research19_Researcher10", None)
        self.__research19_Researcher10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research19_Collaboration"):
                    opp_val = getattr(item, "research19_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "research19_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research19_Collaboration"):
                    opp_val = getattr(item, "research19_Collaboration", None)
                    
                    setattr(item, "research19_Collaboration", self)
                    

class research19_Phase:

    def __init__(self, name: str, research19_Phase: "research19_PublicationProcess" = None):
        self.name = name
        self.research19_Phase = research19_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research19_Phase(self):
        return self.__research19_Phase

    @research19_Phase.setter
    def research19_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Phase__research19_Phase", None)
        self.__research19_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_PublicationProcess"):
                opp_val = getattr(old_value, "research19_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_PublicationProcess"):
                opp_val = getattr(value, "research19_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "research19_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class research19_Keyword(Named):

    def __init__(self, word: str, research19_Keyword: set["research19_Paper"] = None, research19_Keyword57: "research19_KnowledgeManager" = None, research19_Keyword60: "research19_PaperKeyword" = None):
        self.word = word
        self.research19_Keyword = research19_Keyword if research19_Keyword is not None else set()
        self.research19_Keyword57 = research19_Keyword57
        self.research19_Keyword60 = research19_Keyword60
        
    @property
    def word(self) -> str:
        return self.__word

    @word.setter
    def word(self, word: str):
        self.__word = word

    @property
    def research19_Keyword57(self):
        return self.__research19_Keyword57

    @research19_Keyword57.setter
    def research19_Keyword57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Keyword__research19_Keyword57", None)
        self.__research19_Keyword57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_KnowledgeManager56"):
                opp_val = getattr(old_value, "research19_KnowledgeManager56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_KnowledgeManager56"):
                opp_val = getattr(value, "research19_KnowledgeManager56", None)
                if opp_val is None:
                    setattr(value, "research19_KnowledgeManager56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research19_Keyword(self):
        return self.__research19_Keyword

    @research19_Keyword.setter
    def research19_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Keyword__research19_Keyword", None)
        self.__research19_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research19_Paper54"):
                    opp_val = getattr(item, "research19_Paper54", None)
                    
                    if opp_val == self:
                        setattr(item, "research19_Paper54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research19_Paper54"):
                    opp_val = getattr(item, "research19_Paper54", None)
                    
                    setattr(item, "research19_Paper54", self)
                    

    @property
    def research19_Keyword60(self):
        return self.__research19_Keyword60

    @research19_Keyword60.setter
    def research19_Keyword60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Keyword__research19_Keyword60", None)
        self.__research19_Keyword60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_PaperKeyword59"):
                opp_val = getattr(old_value, "research19_PaperKeyword59", None)
                if opp_val == self:
                    setattr(old_value, "research19_PaperKeyword59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_PaperKeyword59"):
                opp_val = getattr(value, "research19_PaperKeyword59", None)
                setattr(value, "research19_PaperKeyword59", self)

class research19_KnowledgeManager(Named):

    pass
class research19_PublicationStructure(Named):

    pass
class research19_Paragraph(Counted, Named):

    def __init__(self, content: str, research19_Paragraph: "research19_Paper" = None, research19_Paragraph29: "research19_Write" = None, research19_Paragraph22: set["research19_ReviewNote"] = None):
        self.content = content
        self.research19_Paragraph = research19_Paragraph
        self.research19_Paragraph29 = research19_Paragraph29
        self.research19_Paragraph22 = research19_Paragraph22 if research19_Paragraph22 is not None else set()
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research19_Paragraph22(self):
        return self.__research19_Paragraph22

    @research19_Paragraph22.setter
    def research19_Paragraph22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Paragraph__research19_Paragraph22", None)
        self.__research19_Paragraph22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research19_ReviewNote"):
                    opp_val = getattr(item, "research19_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "research19_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research19_ReviewNote"):
                    opp_val = getattr(item, "research19_ReviewNote", None)
                    
                    setattr(item, "research19_ReviewNote", self)
                    

    @property
    def research19_Paragraph(self):
        return self.__research19_Paragraph

    @research19_Paragraph.setter
    def research19_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Paragraph__research19_Paragraph", None)
        self.__research19_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Paper"):
                opp_val = getattr(old_value, "research19_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Paper"):
                opp_val = getattr(value, "research19_Paper", None)
                if opp_val is None:
                    setattr(value, "research19_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research19_Paragraph29(self):
        return self.__research19_Paragraph29

    @research19_Paragraph29.setter
    def research19_Paragraph29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Paragraph__research19_Paragraph29", None)
        self.__research19_Paragraph29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Write28"):
                opp_val = getattr(old_value, "research19_Write28", None)
                if opp_val == self:
                    setattr(old_value, "research19_Write28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Write28"):
                opp_val = getattr(value, "research19_Write28", None)
                setattr(value, "research19_Write28", self)

class research19_Position(Named):

    def __init__(self, description: str, research19_Position: "research19_Researcher" = None, research19_Position52: "research19_Position" = None, research19_Position50: "research19_Position" = None, research19_Position47: "research19_PublicationSystem" = None):
        self.description = description
        self.research19_Position = research19_Position
        self.research19_Position52 = research19_Position52
        self.research19_Position50 = research19_Position50
        self.research19_Position47 = research19_Position47
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research19_Position47(self):
        return self.__research19_Position47

    @research19_Position47.setter
    def research19_Position47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Position__research19_Position47", None)
        self.__research19_Position47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_PublicationSystem46"):
                opp_val = getattr(old_value, "research19_PublicationSystem46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_PublicationSystem46"):
                opp_val = getattr(value, "research19_PublicationSystem46", None)
                if opp_val is None:
                    setattr(value, "research19_PublicationSystem46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research19_Position52(self):
        return self.__research19_Position52

    @research19_Position52.setter
    def research19_Position52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Position__research19_Position52", None)
        self.__research19_Position52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Position50"):
                opp_val = getattr(old_value, "research19_Position50", None)
                if opp_val == self:
                    setattr(old_value, "research19_Position50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Position50"):
                opp_val = getattr(value, "research19_Position50", None)
                setattr(value, "research19_Position50", self)

    @property
    def research19_Position(self):
        return self.__research19_Position

    @research19_Position.setter
    def research19_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Position__research19_Position", None)
        self.__research19_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Researcher8"):
                opp_val = getattr(old_value, "research19_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "research19_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Researcher8"):
                opp_val = getattr(value, "research19_Researcher8", None)
                setattr(value, "research19_Researcher8", self)

    @property
    def research19_Position50(self):
        return self.__research19_Position50

    @research19_Position50.setter
    def research19_Position50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_Position__research19_Position50", None)
        self.__research19_Position50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Position52"):
                opp_val = getattr(old_value, "research19_Position52", None)
                if opp_val == self:
                    setattr(old_value, "research19_Position52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Position52"):
                opp_val = getattr(value, "research19_Position52", None)
                setattr(value, "research19_Position52", self)

class research19_Paper(Named):

    pass
class research19_PublicationSystem(Named):

    pass
class research19_ReviewNote(Named):

    def __init__(self, content: str, research19_ReviewNote32: "research19_Review" = None, research19_ReviewNote: "research19_Paragraph" = None):
        self.content = content
        self.research19_ReviewNote32 = research19_ReviewNote32
        self.research19_ReviewNote = research19_ReviewNote
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research19_ReviewNote(self):
        return self.__research19_ReviewNote

    @research19_ReviewNote.setter
    def research19_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_ReviewNote__research19_ReviewNote", None)
        self.__research19_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Paragraph22"):
                opp_val = getattr(old_value, "research19_Paragraph22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Paragraph22"):
                opp_val = getattr(value, "research19_Paragraph22", None)
                if opp_val is None:
                    setattr(value, "research19_Paragraph22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research19_ReviewNote32(self):
        return self.__research19_ReviewNote32

    @research19_ReviewNote32.setter
    def research19_ReviewNote32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_ReviewNote__research19_ReviewNote32", None)
        self.__research19_ReviewNote32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Review31"):
                opp_val = getattr(old_value, "research19_Review31", None)
                if opp_val == self:
                    setattr(old_value, "research19_Review31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Review31"):
                opp_val = getattr(value, "research19_Review31", None)
                setattr(value, "research19_Review31", self)

class research19_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, research19_PublicationProcess: set["research19_Phase"] = None, research19_PublicationProcess24: "research19_Progress" = None, research19_PublicationProcess41: "research19_PublicationSystem" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.research19_PublicationProcess = research19_PublicationProcess if research19_PublicationProcess is not None else set()
        self.research19_PublicationProcess24 = research19_PublicationProcess24
        self.research19_PublicationProcess41 = research19_PublicationProcess41
        
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
    def research19_PublicationProcess41(self):
        return self.__research19_PublicationProcess41

    @research19_PublicationProcess41.setter
    def research19_PublicationProcess41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_PublicationProcess__research19_PublicationProcess41", None)
        self.__research19_PublicationProcess41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_PublicationSystem"):
                opp_val = getattr(old_value, "research19_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "research19_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_PublicationSystem"):
                opp_val = getattr(value, "research19_PublicationSystem", None)
                setattr(value, "research19_PublicationSystem", self)

    @property
    def research19_PublicationProcess(self):
        return self.__research19_PublicationProcess

    @research19_PublicationProcess.setter
    def research19_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_PublicationProcess__research19_PublicationProcess", None)
        self.__research19_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research19_Phase"):
                    opp_val = getattr(item, "research19_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "research19_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research19_Phase"):
                    opp_val = getattr(item, "research19_Phase", None)
                    
                    setattr(item, "research19_Phase", self)
                    

    @property
    def research19_PublicationProcess24(self):
        return self.__research19_PublicationProcess24

    @research19_PublicationProcess24.setter
    def research19_PublicationProcess24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research19_PublicationProcess__research19_PublicationProcess24", None)
        self.__research19_PublicationProcess24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research19_Progress"):
                opp_val = getattr(old_value, "research19_Progress", None)
                if opp_val == self:
                    setattr(old_value, "research19_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research19_Progress"):
                opp_val = getattr(value, "research19_Progress", None)
                setattr(value, "research19_Progress", self)
