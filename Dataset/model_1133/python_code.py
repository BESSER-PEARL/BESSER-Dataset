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

class research31_Action:

    def __init__(self, actionLabel: str, actionStatement: str, research31_Action81: "research31_State" = None, research31_Action84: "research31_Action" = None, research31_Action82: "research31_Action" = None, research31_Action: "research31_Transition" = None):
        self.actionLabel = actionLabel
        self.actionStatement = actionStatement
        self.research31_Action81 = research31_Action81
        self.research31_Action84 = research31_Action84
        self.research31_Action82 = research31_Action82
        self.research31_Action = research31_Action
        
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
    def research31_Action(self):
        return self.__research31_Action

    @research31_Action.setter
    def research31_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Action__research31_Action", None)
        self.__research31_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Transition"):
                opp_val = getattr(old_value, "research31_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Transition"):
                opp_val = getattr(value, "research31_Transition", None)
                if opp_val is None:
                    setattr(value, "research31_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research31_Action81(self):
        return self.__research31_Action81

    @research31_Action81.setter
    def research31_Action81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Action__research31_Action81", None)
        self.__research31_Action81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_State80"):
                opp_val = getattr(old_value, "research31_State80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_State80"):
                opp_val = getattr(value, "research31_State80", None)
                if opp_val is None:
                    setattr(value, "research31_State80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research31_Action84(self):
        return self.__research31_Action84

    @research31_Action84.setter
    def research31_Action84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Action__research31_Action84", None)
        self.__research31_Action84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Action82"):
                opp_val = getattr(old_value, "research31_Action82", None)
                if opp_val == self:
                    setattr(old_value, "research31_Action82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Action82"):
                opp_val = getattr(value, "research31_Action82", None)
                setattr(value, "research31_Action82", self)

    @property
    def research31_Action82(self):
        return self.__research31_Action82

    @research31_Action82.setter
    def research31_Action82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Action__research31_Action82", None)
        self.__research31_Action82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Action84"):
                opp_val = getattr(old_value, "research31_Action84", None)
                if opp_val == self:
                    setattr(old_value, "research31_Action84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Action84"):
                opp_val = getattr(value, "research31_Action84", None)
                setattr(value, "research31_Action84", self)

class StateMachineObject:

    pass
class research31_Transition(StateMachineObject):

    def __init__(self, guardLabel: str, guardExpression: str, research31_Transition74: "research31_State" = None, research31_Transition78: "research31_State" = None, research31_Transition: set["research31_Action"] = None, research31_Transition71: "research31_State" = None):
        self.guardLabel = guardLabel
        self.guardExpression = guardExpression
        self.research31_Transition74 = research31_Transition74
        self.research31_Transition78 = research31_Transition78
        self.research31_Transition = research31_Transition if research31_Transition is not None else set()
        self.research31_Transition71 = research31_Transition71
        
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
    def research31_Transition74(self):
        return self.__research31_Transition74

    @research31_Transition74.setter
    def research31_Transition74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Transition__research31_Transition74", None)
        self.__research31_Transition74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_State75"):
                opp_val = getattr(old_value, "research31_State75", None)
                if opp_val == self:
                    setattr(old_value, "research31_State75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_State75"):
                opp_val = getattr(value, "research31_State75", None)
                setattr(value, "research31_State75", self)

    @property
    def research31_Transition(self):
        return self.__research31_Transition

    @research31_Transition.setter
    def research31_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Transition__research31_Transition", None)
        self.__research31_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research31_Action"):
                    opp_val = getattr(item, "research31_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "research31_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research31_Action"):
                    opp_val = getattr(item, "research31_Action", None)
                    
                    setattr(item, "research31_Action", self)
                    

    @property
    def research31_Transition78(self):
        return self.__research31_Transition78

    @research31_Transition78.setter
    def research31_Transition78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Transition__research31_Transition78", None)
        self.__research31_Transition78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_State77"):
                opp_val = getattr(old_value, "research31_State77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_State77"):
                opp_val = getattr(value, "research31_State77", None)
                if opp_val is None:
                    setattr(value, "research31_State77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research31_Transition71(self):
        return self.__research31_Transition71

    @research31_Transition71.setter
    def research31_Transition71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Transition__research31_Transition71", None)
        self.__research31_Transition71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_State72"):
                opp_val = getattr(old_value, "research31_State72", None)
                if opp_val == self:
                    setattr(old_value, "research31_State72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_State72"):
                opp_val = getattr(value, "research31_State72", None)
                setattr(value, "research31_State72", self)

class research31_StateMachineObject(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class research31_StateMachineVariable:

    pass
class research31_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class research31_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class research31_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class research31_PublicationStatus:

    def __init__(self, label: str, research31_PublicationStatus: "research31_PublicationStructure" = None, research31_PublicationStatus65: set["research31_StateMachineVariable"] = None, research31_PublicationStatus67: set["research31_State"] = None):
        self.label = label
        self.research31_PublicationStatus = research31_PublicationStatus
        self.research31_PublicationStatus65 = research31_PublicationStatus65 if research31_PublicationStatus65 is not None else set()
        self.research31_PublicationStatus67 = research31_PublicationStatus67 if research31_PublicationStatus67 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def research31_PublicationStatus65(self):
        return self.__research31_PublicationStatus65

    @research31_PublicationStatus65.setter
    def research31_PublicationStatus65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_PublicationStatus__research31_PublicationStatus65", None)
        self.__research31_PublicationStatus65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research31_StateMachineVariable"):
                    opp_val = getattr(item, "research31_StateMachineVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "research31_StateMachineVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research31_StateMachineVariable"):
                    opp_val = getattr(item, "research31_StateMachineVariable", None)
                    
                    setattr(item, "research31_StateMachineVariable", self)
                    

    @property
    def research31_PublicationStatus(self):
        return self.__research31_PublicationStatus

    @research31_PublicationStatus.setter
    def research31_PublicationStatus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_PublicationStatus__research31_PublicationStatus", None)
        self.__research31_PublicationStatus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_PublicationStructure41"):
                opp_val = getattr(old_value, "research31_PublicationStructure41", None)
                if opp_val == self:
                    setattr(old_value, "research31_PublicationStructure41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_PublicationStructure41"):
                opp_val = getattr(value, "research31_PublicationStructure41", None)
                setattr(value, "research31_PublicationStructure41", self)

    @property
    def research31_PublicationStatus67(self):
        return self.__research31_PublicationStatus67

    @research31_PublicationStatus67.setter
    def research31_PublicationStatus67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_PublicationStatus__research31_PublicationStatus67", None)
        self.__research31_PublicationStatus67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research31_State68"):
                    opp_val = getattr(item, "research31_State68", None)
                    
                    if opp_val == self:
                        setattr(item, "research31_State68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research31_State68"):
                    opp_val = getattr(item, "research31_State68", None)
                    
                    setattr(item, "research31_State68", self)
                    

class Labelled:

    pass
class Counted:

    pass
class research31_Collaboration:

    def __init__(self, ratio: int, research31_Collaboration: "research31_Researcher" = None, research31_Collaboration62: "research31_Paper" = None):
        self.ratio = ratio
        self.research31_Collaboration = research31_Collaboration
        self.research31_Collaboration62 = research31_Collaboration62
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def research31_Collaboration(self):
        return self.__research31_Collaboration

    @research31_Collaboration.setter
    def research31_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Collaboration__research31_Collaboration", None)
        self.__research31_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Researcher10"):
                opp_val = getattr(old_value, "research31_Researcher10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Researcher10"):
                opp_val = getattr(value, "research31_Researcher10", None)
                if opp_val is None:
                    setattr(value, "research31_Researcher10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research31_Collaboration62(self):
        return self.__research31_Collaboration62

    @research31_Collaboration62.setter
    def research31_Collaboration62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Collaboration__research31_Collaboration62", None)
        self.__research31_Collaboration62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Paper63"):
                opp_val = getattr(old_value, "research31_Paper63", None)
                if opp_val == self:
                    setattr(old_value, "research31_Paper63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Paper63"):
                opp_val = getattr(value, "research31_Paper63", None)
                setattr(value, "research31_Paper63", self)

class research31_Skill:

    def __init__(self, description: str, research31_Skill: "research31_Researcher" = None):
        self.description = description
        self.research31_Skill = research31_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research31_Skill(self):
        return self.__research31_Skill

    @research31_Skill.setter
    def research31_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Skill__research31_Skill", None)
        self.__research31_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Researcher6"):
                opp_val = getattr(old_value, "research31_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Researcher6"):
                opp_val = getattr(value, "research31_Researcher6", None)
                if opp_val is None:
                    setattr(value, "research31_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research31_Review(Labelled):

    def __init__(self, date: date, research31_Review: "research31_Researcher" = None, research31_Review31: "research31_ReviewNote" = None):
        self.date = date
        self.research31_Review = research31_Review
        self.research31_Review31 = research31_Review31
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def research31_Review(self):
        return self.__research31_Review

    @research31_Review.setter
    def research31_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Review__research31_Review", None)
        self.__research31_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Researcher3"):
                opp_val = getattr(old_value, "research31_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Researcher3"):
                opp_val = getattr(value, "research31_Researcher3", None)
                if opp_val is None:
                    setattr(value, "research31_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research31_Review31(self):
        return self.__research31_Review31

    @research31_Review31.setter
    def research31_Review31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Review__research31_Review31", None)
        self.__research31_Review31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_ReviewNote32"):
                opp_val = getattr(old_value, "research31_ReviewNote32", None)
                if opp_val == self:
                    setattr(old_value, "research31_ReviewNote32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_ReviewNote32"):
                opp_val = getattr(value, "research31_ReviewNote32", None)
                setattr(value, "research31_ReviewNote32", self)

class research31_Write(Labelled):

    def __init__(self, timeSpent: int, research31_Write: "research31_Researcher" = None, research31_Write28: "research31_Paragraph" = None):
        self.timeSpent = timeSpent
        self.research31_Write = research31_Write
        self.research31_Write28 = research31_Write28
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def research31_Write(self):
        return self.__research31_Write

    @research31_Write.setter
    def research31_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Write__research31_Write", None)
        self.__research31_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Researcher"):
                opp_val = getattr(old_value, "research31_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Researcher"):
                opp_val = getattr(value, "research31_Researcher", None)
                if opp_val is None:
                    setattr(value, "research31_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research31_Write28(self):
        return self.__research31_Write28

    @research31_Write28.setter
    def research31_Write28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Write__research31_Write28", None)
        self.__research31_Write28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Paragraph29"):
                opp_val = getattr(old_value, "research31_Paragraph29", None)
                if opp_val == self:
                    setattr(old_value, "research31_Paragraph29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Paragraph29"):
                opp_val = getattr(value, "research31_Paragraph29", None)
                setattr(value, "research31_Paragraph29", self)

class research31_State(StateMachineObject):

    def __init__(self, id: int, kind: str, name: str, research31_State: "research31_Paper" = None, research31_State68: "research31_PublicationStatus" = None, research31_State75: "research31_Transition" = None, research31_State77: set["research31_Transition"] = None, research31_State80: set["research31_Action"] = None, research31_State72: "research31_Transition" = None):
        self.id = id
        self.kind = kind
        self.name = name
        self.research31_State = research31_State
        self.research31_State68 = research31_State68
        self.research31_State75 = research31_State75
        self.research31_State77 = research31_State77 if research31_State77 is not None else set()
        self.research31_State80 = research31_State80 if research31_State80 is not None else set()
        self.research31_State72 = research31_State72
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def research31_State(self):
        return self.__research31_State

    @research31_State.setter
    def research31_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_State__research31_State", None)
        self.__research31_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Paper20"):
                opp_val = getattr(old_value, "research31_Paper20", None)
                if opp_val == self:
                    setattr(old_value, "research31_Paper20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Paper20"):
                opp_val = getattr(value, "research31_Paper20", None)
                setattr(value, "research31_Paper20", self)

    @property
    def research31_State77(self):
        return self.__research31_State77

    @research31_State77.setter
    def research31_State77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_State__research31_State77", None)
        self.__research31_State77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research31_Transition78"):
                    opp_val = getattr(item, "research31_Transition78", None)
                    
                    if opp_val == self:
                        setattr(item, "research31_Transition78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research31_Transition78"):
                    opp_val = getattr(item, "research31_Transition78", None)
                    
                    setattr(item, "research31_Transition78", self)
                    

    @property
    def research31_State75(self):
        return self.__research31_State75

    @research31_State75.setter
    def research31_State75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_State__research31_State75", None)
        self.__research31_State75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Transition74"):
                opp_val = getattr(old_value, "research31_Transition74", None)
                if opp_val == self:
                    setattr(old_value, "research31_Transition74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Transition74"):
                opp_val = getattr(value, "research31_Transition74", None)
                setattr(value, "research31_Transition74", self)

    @property
    def research31_State72(self):
        return self.__research31_State72

    @research31_State72.setter
    def research31_State72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_State__research31_State72", None)
        self.__research31_State72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Transition71"):
                opp_val = getattr(old_value, "research31_Transition71", None)
                if opp_val == self:
                    setattr(old_value, "research31_Transition71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Transition71"):
                opp_val = getattr(value, "research31_Transition71", None)
                setattr(value, "research31_Transition71", self)

    @property
    def research31_State68(self):
        return self.__research31_State68

    @research31_State68.setter
    def research31_State68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_State__research31_State68", None)
        self.__research31_State68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_PublicationStatus67"):
                opp_val = getattr(old_value, "research31_PublicationStatus67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_PublicationStatus67"):
                opp_val = getattr(value, "research31_PublicationStatus67", None)
                if opp_val is None:
                    setattr(value, "research31_PublicationStatus67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research31_State80(self):
        return self.__research31_State80

    @research31_State80.setter
    def research31_State80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_State__research31_State80", None)
        self.__research31_State80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research31_Action81"):
                    opp_val = getattr(item, "research31_Action81", None)
                    
                    if opp_val == self:
                        setattr(item, "research31_Action81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research31_Action81"):
                    opp_val = getattr(item, "research31_Action81", None)
                    
                    setattr(item, "research31_Action81", self)
                    

class research31_PaperKeyword:

    def __init__(self, weight: int, research31_PaperKeyword: "research31_Paper" = None, research31_PaperKeyword59: "research31_Keyword" = None):
        self.weight = weight
        self.research31_PaperKeyword = research31_PaperKeyword
        self.research31_PaperKeyword59 = research31_PaperKeyword59
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def research31_PaperKeyword59(self):
        return self.__research31_PaperKeyword59

    @research31_PaperKeyword59.setter
    def research31_PaperKeyword59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_PaperKeyword__research31_PaperKeyword59", None)
        self.__research31_PaperKeyword59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Keyword60"):
                opp_val = getattr(old_value, "research31_Keyword60", None)
                if opp_val == self:
                    setattr(old_value, "research31_Keyword60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Keyword60"):
                opp_val = getattr(value, "research31_Keyword60", None)
                setattr(value, "research31_Keyword60", self)

    @property
    def research31_PaperKeyword(self):
        return self.__research31_PaperKeyword

    @research31_PaperKeyword.setter
    def research31_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_PaperKeyword__research31_PaperKeyword", None)
        self.__research31_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Paper15"):
                opp_val = getattr(old_value, "research31_Paper15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Paper15"):
                opp_val = getattr(value, "research31_Paper15", None)
                if opp_val is None:
                    setattr(value, "research31_Paper15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research31_Progress(Labelled):

    def __init__(self, percent: int, Progress: "research31_Paper" = None, research31_Progress: "research31_PublicationProcess" = None, progress: "research31_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.research31_Progress = research31_Progress
        self.progress = progress
        
    @property
    def percent(self) -> int:
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent

    @property
    def research31_Progress(self):
        return self.__research31_Progress

    @research31_Progress.setter
    def research31_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Progress__research31_Progress", None)
        self.__research31_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_PublicationProcess24"):
                opp_val = getattr(old_value, "research31_PublicationProcess24", None)
                if opp_val == self:
                    setattr(old_value, "research31_PublicationProcess24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_PublicationProcess24"):
                opp_val = getattr(value, "research31_PublicationProcess24", None)
                setattr(value, "research31_PublicationProcess24", self)

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Progress__progress", None)
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
        old_value = getattr(self, f"_research31_Progress__Progress", None)
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

class Named:

    pass
class research31_Keyword(Named):

    def __init__(self, word: str, research31_Keyword: set["research31_Paper"] = None, research31_Keyword60: "research31_PaperKeyword" = None, research31_Keyword57: "research31_KnowledgeManager" = None):
        self.word = word
        self.research31_Keyword = research31_Keyword if research31_Keyword is not None else set()
        self.research31_Keyword60 = research31_Keyword60
        self.research31_Keyword57 = research31_Keyword57
        
    @property
    def word(self) -> str:
        return self.__word

    @word.setter
    def word(self, word: str):
        self.__word = word

    @property
    def research31_Keyword57(self):
        return self.__research31_Keyword57

    @research31_Keyword57.setter
    def research31_Keyword57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Keyword__research31_Keyword57", None)
        self.__research31_Keyword57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_KnowledgeManager56"):
                opp_val = getattr(old_value, "research31_KnowledgeManager56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_KnowledgeManager56"):
                opp_val = getattr(value, "research31_KnowledgeManager56", None)
                if opp_val is None:
                    setattr(value, "research31_KnowledgeManager56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research31_Keyword60(self):
        return self.__research31_Keyword60

    @research31_Keyword60.setter
    def research31_Keyword60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Keyword__research31_Keyword60", None)
        self.__research31_Keyword60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_PaperKeyword59"):
                opp_val = getattr(old_value, "research31_PaperKeyword59", None)
                if opp_val == self:
                    setattr(old_value, "research31_PaperKeyword59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_PaperKeyword59"):
                opp_val = getattr(value, "research31_PaperKeyword59", None)
                setattr(value, "research31_PaperKeyword59", self)

    @property
    def research31_Keyword(self):
        return self.__research31_Keyword

    @research31_Keyword.setter
    def research31_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Keyword__research31_Keyword", None)
        self.__research31_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research31_Paper54"):
                    opp_val = getattr(item, "research31_Paper54", None)
                    
                    if opp_val == self:
                        setattr(item, "research31_Paper54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research31_Paper54"):
                    opp_val = getattr(item, "research31_Paper54", None)
                    
                    setattr(item, "research31_Paper54", self)
                    

class research31_PublicationSystem(Named):

    pass
class research31_Paper(Named):

    pass
class research31_Position(Named):

    def __init__(self, description: str, research31_Position: "research31_Researcher" = None, research31_Position52: "research31_Position" = None, research31_Position50: "research31_Position" = None, research31_Position49: "research31_PublicationSystem" = None):
        self.description = description
        self.research31_Position = research31_Position
        self.research31_Position52 = research31_Position52
        self.research31_Position50 = research31_Position50
        self.research31_Position49 = research31_Position49
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research31_Position(self):
        return self.__research31_Position

    @research31_Position.setter
    def research31_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Position__research31_Position", None)
        self.__research31_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Researcher8"):
                opp_val = getattr(old_value, "research31_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "research31_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Researcher8"):
                opp_val = getattr(value, "research31_Researcher8", None)
                setattr(value, "research31_Researcher8", self)

    @property
    def research31_Position52(self):
        return self.__research31_Position52

    @research31_Position52.setter
    def research31_Position52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Position__research31_Position52", None)
        self.__research31_Position52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Position50"):
                opp_val = getattr(old_value, "research31_Position50", None)
                if opp_val == self:
                    setattr(old_value, "research31_Position50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Position50"):
                opp_val = getattr(value, "research31_Position50", None)
                setattr(value, "research31_Position50", self)

    @property
    def research31_Position50(self):
        return self.__research31_Position50

    @research31_Position50.setter
    def research31_Position50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Position__research31_Position50", None)
        self.__research31_Position50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Position52"):
                opp_val = getattr(old_value, "research31_Position52", None)
                if opp_val == self:
                    setattr(old_value, "research31_Position52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Position52"):
                opp_val = getattr(value, "research31_Position52", None)
                setattr(value, "research31_Position52", self)

    @property
    def research31_Position49(self):
        return self.__research31_Position49

    @research31_Position49.setter
    def research31_Position49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Position__research31_Position49", None)
        self.__research31_Position49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_PublicationSystem48"):
                opp_val = getattr(old_value, "research31_PublicationSystem48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_PublicationSystem48"):
                opp_val = getattr(value, "research31_PublicationSystem48", None)
                if opp_val is None:
                    setattr(value, "research31_PublicationSystem48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research31_Paragraph(Counted, Named):

    def __init__(self, content: str, research31_Paragraph: "research31_Paper" = None, research31_Paragraph29: "research31_Write" = None, research31_Paragraph22: set["research31_ReviewNote"] = None):
        self.content = content
        self.research31_Paragraph = research31_Paragraph
        self.research31_Paragraph29 = research31_Paragraph29
        self.research31_Paragraph22 = research31_Paragraph22 if research31_Paragraph22 is not None else set()
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research31_Paragraph29(self):
        return self.__research31_Paragraph29

    @research31_Paragraph29.setter
    def research31_Paragraph29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Paragraph__research31_Paragraph29", None)
        self.__research31_Paragraph29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Write28"):
                opp_val = getattr(old_value, "research31_Write28", None)
                if opp_val == self:
                    setattr(old_value, "research31_Write28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Write28"):
                opp_val = getattr(value, "research31_Write28", None)
                setattr(value, "research31_Write28", self)

    @property
    def research31_Paragraph(self):
        return self.__research31_Paragraph

    @research31_Paragraph.setter
    def research31_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Paragraph__research31_Paragraph", None)
        self.__research31_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Paper"):
                opp_val = getattr(old_value, "research31_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Paper"):
                opp_val = getattr(value, "research31_Paper", None)
                if opp_val is None:
                    setattr(value, "research31_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research31_Paragraph22(self):
        return self.__research31_Paragraph22

    @research31_Paragraph22.setter
    def research31_Paragraph22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Paragraph__research31_Paragraph22", None)
        self.__research31_Paragraph22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research31_ReviewNote"):
                    opp_val = getattr(item, "research31_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "research31_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research31_ReviewNote"):
                    opp_val = getattr(item, "research31_ReviewNote", None)
                    
                    setattr(item, "research31_ReviewNote", self)
                    

class research31_PublicationStructure(Named):

    pass
class research31_KnowledgeManager(Named):

    pass
class research31_ReviewNote(Named):

    def __init__(self, content: str, research31_ReviewNote: "research31_Paragraph" = None, research31_ReviewNote32: "research31_Review" = None):
        self.content = content
        self.research31_ReviewNote = research31_ReviewNote
        self.research31_ReviewNote32 = research31_ReviewNote32
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research31_ReviewNote32(self):
        return self.__research31_ReviewNote32

    @research31_ReviewNote32.setter
    def research31_ReviewNote32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_ReviewNote__research31_ReviewNote32", None)
        self.__research31_ReviewNote32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Review31"):
                opp_val = getattr(old_value, "research31_Review31", None)
                if opp_val == self:
                    setattr(old_value, "research31_Review31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Review31"):
                opp_val = getattr(value, "research31_Review31", None)
                setattr(value, "research31_Review31", self)

    @property
    def research31_ReviewNote(self):
        return self.__research31_ReviewNote

    @research31_ReviewNote.setter
    def research31_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_ReviewNote__research31_ReviewNote", None)
        self.__research31_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Paragraph22"):
                opp_val = getattr(old_value, "research31_Paragraph22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Paragraph22"):
                opp_val = getattr(value, "research31_Paragraph22", None)
                if opp_val is None:
                    setattr(value, "research31_Paragraph22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research31_PublicationProcess(Named):

    def __init__(self, maxTime: int, minTime: int, research31_PublicationProcess: set["research31_Phase"] = None, research31_PublicationProcess24: "research31_Progress" = None, research31_PublicationProcess43: "research31_PublicationSystem" = None):
        self.maxTime = maxTime
        self.minTime = minTime
        self.research31_PublicationProcess = research31_PublicationProcess if research31_PublicationProcess is not None else set()
        self.research31_PublicationProcess24 = research31_PublicationProcess24
        self.research31_PublicationProcess43 = research31_PublicationProcess43
        
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
    def research31_PublicationProcess(self):
        return self.__research31_PublicationProcess

    @research31_PublicationProcess.setter
    def research31_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_PublicationProcess__research31_PublicationProcess", None)
        self.__research31_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research31_Phase"):
                    opp_val = getattr(item, "research31_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "research31_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research31_Phase"):
                    opp_val = getattr(item, "research31_Phase", None)
                    
                    setattr(item, "research31_Phase", self)
                    

    @property
    def research31_PublicationProcess43(self):
        return self.__research31_PublicationProcess43

    @research31_PublicationProcess43.setter
    def research31_PublicationProcess43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_PublicationProcess__research31_PublicationProcess43", None)
        self.__research31_PublicationProcess43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_PublicationSystem"):
                opp_val = getattr(old_value, "research31_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "research31_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_PublicationSystem"):
                opp_val = getattr(value, "research31_PublicationSystem", None)
                setattr(value, "research31_PublicationSystem", self)

    @property
    def research31_PublicationProcess24(self):
        return self.__research31_PublicationProcess24

    @research31_PublicationProcess24.setter
    def research31_PublicationProcess24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_PublicationProcess__research31_PublicationProcess24", None)
        self.__research31_PublicationProcess24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Progress"):
                opp_val = getattr(old_value, "research31_Progress", None)
                if opp_val == self:
                    setattr(old_value, "research31_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Progress"):
                opp_val = getattr(value, "research31_Progress", None)
                setattr(value, "research31_Progress", self)

class research31_Researcher:

    def __init__(self, name: str, forName: str, Researcher: "research31_Paper" = None, research31_Researcher: set["research31_Write"] = None, research31_Researcher3: set["research31_Review"] = None, authors: set["research31_Paper"] = None, research31_Researcher6: set["research31_Skill"] = None, research31_Researcher8: "research31_Position" = None, research31_Researcher10: set["research31_Collaboration"] = None, research31_Researcher34: "research31_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.Researcher = Researcher
        self.research31_Researcher = research31_Researcher if research31_Researcher is not None else set()
        self.research31_Researcher3 = research31_Researcher3 if research31_Researcher3 is not None else set()
        self.authors = authors if authors is not None else set()
        self.research31_Researcher6 = research31_Researcher6 if research31_Researcher6 is not None else set()
        self.research31_Researcher8 = research31_Researcher8
        self.research31_Researcher10 = research31_Researcher10 if research31_Researcher10 is not None else set()
        self.research31_Researcher34 = research31_Researcher34
        
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
    def research31_Researcher10(self):
        return self.__research31_Researcher10

    @research31_Researcher10.setter
    def research31_Researcher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Researcher__research31_Researcher10", None)
        self.__research31_Researcher10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research31_Collaboration"):
                    opp_val = getattr(item, "research31_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "research31_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research31_Collaboration"):
                    opp_val = getattr(item, "research31_Collaboration", None)
                    
                    setattr(item, "research31_Collaboration", self)
                    

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Researcher__authors", None)
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
    def research31_Researcher8(self):
        return self.__research31_Researcher8

    @research31_Researcher8.setter
    def research31_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Researcher__research31_Researcher8", None)
        self.__research31_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_Position"):
                opp_val = getattr(old_value, "research31_Position", None)
                if opp_val == self:
                    setattr(old_value, "research31_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_Position"):
                opp_val = getattr(value, "research31_Position", None)
                setattr(value, "research31_Position", self)

    @property
    def research31_Researcher3(self):
        return self.__research31_Researcher3

    @research31_Researcher3.setter
    def research31_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Researcher__research31_Researcher3", None)
        self.__research31_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research31_Review"):
                    opp_val = getattr(item, "research31_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "research31_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research31_Review"):
                    opp_val = getattr(item, "research31_Review", None)
                    
                    setattr(item, "research31_Review", self)
                    

    @property
    def research31_Researcher(self):
        return self.__research31_Researcher

    @research31_Researcher.setter
    def research31_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Researcher__research31_Researcher", None)
        self.__research31_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research31_Write"):
                    opp_val = getattr(item, "research31_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "research31_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research31_Write"):
                    opp_val = getattr(item, "research31_Write", None)
                    
                    setattr(item, "research31_Write", self)
                    

    @property
    def research31_Researcher34(self):
        return self.__research31_Researcher34

    @research31_Researcher34.setter
    def research31_Researcher34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Researcher__research31_Researcher34", None)
        self.__research31_Researcher34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_PublicationStructure"):
                opp_val = getattr(old_value, "research31_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_PublicationStructure"):
                opp_val = getattr(value, "research31_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "research31_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research31_Researcher6(self):
        return self.__research31_Researcher6

    @research31_Researcher6.setter
    def research31_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Researcher__research31_Researcher6", None)
        self.__research31_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research31_Skill"):
                    opp_val = getattr(item, "research31_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "research31_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research31_Skill"):
                    opp_val = getattr(item, "research31_Skill", None)
                    
                    setattr(item, "research31_Skill", self)
                    

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Researcher__Researcher", None)
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

class research31_Phase:

    def __init__(self, name: str, research31_Phase: "research31_PublicationProcess" = None):
        self.name = name
        self.research31_Phase = research31_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research31_Phase(self):
        return self.__research31_Phase

    @research31_Phase.setter
    def research31_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research31_Phase__research31_Phase", None)
        self.__research31_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research31_PublicationProcess"):
                opp_val = getattr(old_value, "research31_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research31_PublicationProcess"):
                opp_val = getattr(value, "research31_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "research31_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
