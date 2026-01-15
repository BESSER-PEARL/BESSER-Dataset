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

class research20_Action:

    def __init__(self, actionLabel: str, actionStatement: str, research20_Action: "research20_Transition" = None, research20_Action81: "research20_State" = None, research20_Action84: "research20_Action" = None, research20_Action82: "research20_Action" = None):
        self.actionLabel = actionLabel
        self.actionStatement = actionStatement
        self.research20_Action = research20_Action
        self.research20_Action81 = research20_Action81
        self.research20_Action84 = research20_Action84
        self.research20_Action82 = research20_Action82
        
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
    def research20_Action84(self):
        return self.__research20_Action84

    @research20_Action84.setter
    def research20_Action84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Action__research20_Action84", None)
        self.__research20_Action84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Action82"):
                opp_val = getattr(old_value, "research20_Action82", None)
                if opp_val == self:
                    setattr(old_value, "research20_Action82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Action82"):
                opp_val = getattr(value, "research20_Action82", None)
                setattr(value, "research20_Action82", self)

    @property
    def research20_Action82(self):
        return self.__research20_Action82

    @research20_Action82.setter
    def research20_Action82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Action__research20_Action82", None)
        self.__research20_Action82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Action84"):
                opp_val = getattr(old_value, "research20_Action84", None)
                if opp_val == self:
                    setattr(old_value, "research20_Action84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Action84"):
                opp_val = getattr(value, "research20_Action84", None)
                setattr(value, "research20_Action84", self)

    @property
    def research20_Action(self):
        return self.__research20_Action

    @research20_Action.setter
    def research20_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Action__research20_Action", None)
        self.__research20_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Transition"):
                opp_val = getattr(old_value, "research20_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Transition"):
                opp_val = getattr(value, "research20_Transition", None)
                if opp_val is None:
                    setattr(value, "research20_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research20_Action81(self):
        return self.__research20_Action81

    @research20_Action81.setter
    def research20_Action81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Action__research20_Action81", None)
        self.__research20_Action81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_State80"):
                opp_val = getattr(old_value, "research20_State80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_State80"):
                opp_val = getattr(value, "research20_State80", None)
                if opp_val is None:
                    setattr(value, "research20_State80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StateMachineObject:

    pass
class research20_Transition(StateMachineObject):

    def __init__(self, guardLabel: str, guardExpression: str, research20_Transition71: "research20_State" = None, research20_Transition74: "research20_State" = None, research20_Transition78: "research20_State" = None, research20_Transition: set["research20_Action"] = None):
        self.guardLabel = guardLabel
        self.guardExpression = guardExpression
        self.research20_Transition71 = research20_Transition71
        self.research20_Transition74 = research20_Transition74
        self.research20_Transition78 = research20_Transition78
        self.research20_Transition = research20_Transition if research20_Transition is not None else set()
        
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
    def research20_Transition74(self):
        return self.__research20_Transition74

    @research20_Transition74.setter
    def research20_Transition74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Transition__research20_Transition74", None)
        self.__research20_Transition74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_State75"):
                opp_val = getattr(old_value, "research20_State75", None)
                if opp_val == self:
                    setattr(old_value, "research20_State75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_State75"):
                opp_val = getattr(value, "research20_State75", None)
                setattr(value, "research20_State75", self)

    @property
    def research20_Transition(self):
        return self.__research20_Transition

    @research20_Transition.setter
    def research20_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Transition__research20_Transition", None)
        self.__research20_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research20_Action"):
                    opp_val = getattr(item, "research20_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "research20_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research20_Action"):
                    opp_val = getattr(item, "research20_Action", None)
                    
                    setattr(item, "research20_Action", self)
                    

    @property
    def research20_Transition78(self):
        return self.__research20_Transition78

    @research20_Transition78.setter
    def research20_Transition78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Transition__research20_Transition78", None)
        self.__research20_Transition78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_State77"):
                opp_val = getattr(old_value, "research20_State77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_State77"):
                opp_val = getattr(value, "research20_State77", None)
                if opp_val is None:
                    setattr(value, "research20_State77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research20_Transition71(self):
        return self.__research20_Transition71

    @research20_Transition71.setter
    def research20_Transition71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Transition__research20_Transition71", None)
        self.__research20_Transition71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_State72"):
                opp_val = getattr(old_value, "research20_State72", None)
                if opp_val == self:
                    setattr(old_value, "research20_State72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_State72"):
                opp_val = getattr(value, "research20_State72", None)
                setattr(value, "research20_State72", self)

class research20_StateMachineObject(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class research20_StateMachineVariable:

    pass
class research20_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class research20_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class research20_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class research20_PublicationStatus:

    def __init__(self, label: str, research20_PublicationStatus: "research20_PublicationStructure" = None, research20_PublicationStatus65: set["research20_StateMachineVariable"] = None, research20_PublicationStatus67: set["research20_State"] = None):
        self.label = label
        self.research20_PublicationStatus = research20_PublicationStatus
        self.research20_PublicationStatus65 = research20_PublicationStatus65 if research20_PublicationStatus65 is not None else set()
        self.research20_PublicationStatus67 = research20_PublicationStatus67 if research20_PublicationStatus67 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def research20_PublicationStatus(self):
        return self.__research20_PublicationStatus

    @research20_PublicationStatus.setter
    def research20_PublicationStatus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_PublicationStatus__research20_PublicationStatus", None)
        self.__research20_PublicationStatus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_PublicationStructure41"):
                opp_val = getattr(old_value, "research20_PublicationStructure41", None)
                if opp_val == self:
                    setattr(old_value, "research20_PublicationStructure41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_PublicationStructure41"):
                opp_val = getattr(value, "research20_PublicationStructure41", None)
                setattr(value, "research20_PublicationStructure41", self)

    @property
    def research20_PublicationStatus67(self):
        return self.__research20_PublicationStatus67

    @research20_PublicationStatus67.setter
    def research20_PublicationStatus67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_PublicationStatus__research20_PublicationStatus67", None)
        self.__research20_PublicationStatus67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research20_State68"):
                    opp_val = getattr(item, "research20_State68", None)
                    
                    if opp_val == self:
                        setattr(item, "research20_State68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research20_State68"):
                    opp_val = getattr(item, "research20_State68", None)
                    
                    setattr(item, "research20_State68", self)
                    

    @property
    def research20_PublicationStatus65(self):
        return self.__research20_PublicationStatus65

    @research20_PublicationStatus65.setter
    def research20_PublicationStatus65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_PublicationStatus__research20_PublicationStatus65", None)
        self.__research20_PublicationStatus65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research20_StateMachineVariable"):
                    opp_val = getattr(item, "research20_StateMachineVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "research20_StateMachineVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research20_StateMachineVariable"):
                    opp_val = getattr(item, "research20_StateMachineVariable", None)
                    
                    setattr(item, "research20_StateMachineVariable", self)
                    

class Labelled:

    pass
class research20_Collaboration:

    def __init__(self, ratio: int, research20_Collaboration: "research20_Researcher" = None, research20_Collaboration62: "research20_Paper" = None):
        self.ratio = ratio
        self.research20_Collaboration = research20_Collaboration
        self.research20_Collaboration62 = research20_Collaboration62
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def research20_Collaboration62(self):
        return self.__research20_Collaboration62

    @research20_Collaboration62.setter
    def research20_Collaboration62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Collaboration__research20_Collaboration62", None)
        self.__research20_Collaboration62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Paper63"):
                opp_val = getattr(old_value, "research20_Paper63", None)
                if opp_val == self:
                    setattr(old_value, "research20_Paper63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Paper63"):
                opp_val = getattr(value, "research20_Paper63", None)
                setattr(value, "research20_Paper63", self)

    @property
    def research20_Collaboration(self):
        return self.__research20_Collaboration

    @research20_Collaboration.setter
    def research20_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Collaboration__research20_Collaboration", None)
        self.__research20_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Researcher10"):
                opp_val = getattr(old_value, "research20_Researcher10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Researcher10"):
                opp_val = getattr(value, "research20_Researcher10", None)
                if opp_val is None:
                    setattr(value, "research20_Researcher10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research20_Skill:

    def __init__(self, description: str, research20_Skill: "research20_Researcher" = None):
        self.description = description
        self.research20_Skill = research20_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research20_Skill(self):
        return self.__research20_Skill

    @research20_Skill.setter
    def research20_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Skill__research20_Skill", None)
        self.__research20_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Researcher6"):
                opp_val = getattr(old_value, "research20_Researcher6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Researcher6"):
                opp_val = getattr(value, "research20_Researcher6", None)
                if opp_val is None:
                    setattr(value, "research20_Researcher6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research20_Review(Labelled):

    def __init__(self, date: date, research20_Review: "research20_Researcher" = None, research20_Review31: "research20_ReviewNote" = None):
        self.date = date
        self.research20_Review = research20_Review
        self.research20_Review31 = research20_Review31
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def research20_Review(self):
        return self.__research20_Review

    @research20_Review.setter
    def research20_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Review__research20_Review", None)
        self.__research20_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Researcher3"):
                opp_val = getattr(old_value, "research20_Researcher3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Researcher3"):
                opp_val = getattr(value, "research20_Researcher3", None)
                if opp_val is None:
                    setattr(value, "research20_Researcher3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research20_Review31(self):
        return self.__research20_Review31

    @research20_Review31.setter
    def research20_Review31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Review__research20_Review31", None)
        self.__research20_Review31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_ReviewNote32"):
                opp_val = getattr(old_value, "research20_ReviewNote32", None)
                if opp_val == self:
                    setattr(old_value, "research20_ReviewNote32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_ReviewNote32"):
                opp_val = getattr(value, "research20_ReviewNote32", None)
                setattr(value, "research20_ReviewNote32", self)

class research20_Write(Labelled):

    def __init__(self, timeSpent: int, research20_Write: "research20_Researcher" = None, research20_Write28: "research20_Paragraph" = None):
        self.timeSpent = timeSpent
        self.research20_Write = research20_Write
        self.research20_Write28 = research20_Write28
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def research20_Write(self):
        return self.__research20_Write

    @research20_Write.setter
    def research20_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Write__research20_Write", None)
        self.__research20_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Researcher"):
                opp_val = getattr(old_value, "research20_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Researcher"):
                opp_val = getattr(value, "research20_Researcher", None)
                if opp_val is None:
                    setattr(value, "research20_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research20_Write28(self):
        return self.__research20_Write28

    @research20_Write28.setter
    def research20_Write28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Write__research20_Write28", None)
        self.__research20_Write28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Paragraph29"):
                opp_val = getattr(old_value, "research20_Paragraph29", None)
                if opp_val == self:
                    setattr(old_value, "research20_Paragraph29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Paragraph29"):
                opp_val = getattr(value, "research20_Paragraph29", None)
                setattr(value, "research20_Paragraph29", self)

class Counted:

    pass
class research20_State(StateMachineObject):

    def __init__(self, id: int, kind: str, name: str, research20_State: "research20_Paper" = None, research20_State68: "research20_PublicationStatus" = None, research20_State72: "research20_Transition" = None, research20_State75: "research20_Transition" = None, research20_State77: set["research20_Transition"] = None, research20_State80: set["research20_Action"] = None):
        self.id = id
        self.kind = kind
        self.name = name
        self.research20_State = research20_State
        self.research20_State68 = research20_State68
        self.research20_State72 = research20_State72
        self.research20_State75 = research20_State75
        self.research20_State77 = research20_State77 if research20_State77 is not None else set()
        self.research20_State80 = research20_State80 if research20_State80 is not None else set()
        
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
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def research20_State75(self):
        return self.__research20_State75

    @research20_State75.setter
    def research20_State75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_State__research20_State75", None)
        self.__research20_State75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Transition74"):
                opp_val = getattr(old_value, "research20_Transition74", None)
                if opp_val == self:
                    setattr(old_value, "research20_Transition74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Transition74"):
                opp_val = getattr(value, "research20_Transition74", None)
                setattr(value, "research20_Transition74", self)

    @property
    def research20_State72(self):
        return self.__research20_State72

    @research20_State72.setter
    def research20_State72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_State__research20_State72", None)
        self.__research20_State72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Transition71"):
                opp_val = getattr(old_value, "research20_Transition71", None)
                if opp_val == self:
                    setattr(old_value, "research20_Transition71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Transition71"):
                opp_val = getattr(value, "research20_Transition71", None)
                setattr(value, "research20_Transition71", self)

    @property
    def research20_State80(self):
        return self.__research20_State80

    @research20_State80.setter
    def research20_State80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_State__research20_State80", None)
        self.__research20_State80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research20_Action81"):
                    opp_val = getattr(item, "research20_Action81", None)
                    
                    if opp_val == self:
                        setattr(item, "research20_Action81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research20_Action81"):
                    opp_val = getattr(item, "research20_Action81", None)
                    
                    setattr(item, "research20_Action81", self)
                    

    @property
    def research20_State68(self):
        return self.__research20_State68

    @research20_State68.setter
    def research20_State68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_State__research20_State68", None)
        self.__research20_State68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_PublicationStatus67"):
                opp_val = getattr(old_value, "research20_PublicationStatus67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_PublicationStatus67"):
                opp_val = getattr(value, "research20_PublicationStatus67", None)
                if opp_val is None:
                    setattr(value, "research20_PublicationStatus67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research20_State(self):
        return self.__research20_State

    @research20_State.setter
    def research20_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_State__research20_State", None)
        self.__research20_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Paper20"):
                opp_val = getattr(old_value, "research20_Paper20", None)
                if opp_val == self:
                    setattr(old_value, "research20_Paper20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Paper20"):
                opp_val = getattr(value, "research20_Paper20", None)
                setattr(value, "research20_Paper20", self)

    @property
    def research20_State77(self):
        return self.__research20_State77

    @research20_State77.setter
    def research20_State77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_State__research20_State77", None)
        self.__research20_State77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research20_Transition78"):
                    opp_val = getattr(item, "research20_Transition78", None)
                    
                    if opp_val == self:
                        setattr(item, "research20_Transition78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research20_Transition78"):
                    opp_val = getattr(item, "research20_Transition78", None)
                    
                    setattr(item, "research20_Transition78", self)
                    

class research20_PaperKeyword:

    def __init__(self, weight: int, research20_PaperKeyword: "research20_Paper" = None, research20_PaperKeyword59: "research20_Keyword" = None):
        self.weight = weight
        self.research20_PaperKeyword = research20_PaperKeyword
        self.research20_PaperKeyword59 = research20_PaperKeyword59
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def research20_PaperKeyword59(self):
        return self.__research20_PaperKeyword59

    @research20_PaperKeyword59.setter
    def research20_PaperKeyword59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_PaperKeyword__research20_PaperKeyword59", None)
        self.__research20_PaperKeyword59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Keyword60"):
                opp_val = getattr(old_value, "research20_Keyword60", None)
                if opp_val == self:
                    setattr(old_value, "research20_Keyword60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Keyword60"):
                opp_val = getattr(value, "research20_Keyword60", None)
                setattr(value, "research20_Keyword60", self)

    @property
    def research20_PaperKeyword(self):
        return self.__research20_PaperKeyword

    @research20_PaperKeyword.setter
    def research20_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_PaperKeyword__research20_PaperKeyword", None)
        self.__research20_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Paper15"):
                opp_val = getattr(old_value, "research20_Paper15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Paper15"):
                opp_val = getattr(value, "research20_Paper15", None)
                if opp_val is None:
                    setattr(value, "research20_Paper15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research20_Progress(Labelled):

    def __init__(self, percent: int, Progress: "research20_Paper" = None, research20_Progress: "research20_PublicationProcess" = None, progress: "research20_Paper" = None):
        self.percent = percent
        self.Progress = Progress
        self.research20_Progress = research20_Progress
        self.progress = progress
        
    @property
    def percent(self) -> int:
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent

    @property
    def research20_Progress(self):
        return self.__research20_Progress

    @research20_Progress.setter
    def research20_Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Progress__research20_Progress", None)
        self.__research20_Progress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_PublicationProcess24"):
                opp_val = getattr(old_value, "research20_PublicationProcess24", None)
                if opp_val == self:
                    setattr(old_value, "research20_PublicationProcess24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_PublicationProcess24"):
                opp_val = getattr(value, "research20_PublicationProcess24", None)
                setattr(value, "research20_PublicationProcess24", self)

    @property
    def Progress(self):
        return self.__Progress

    @Progress.setter
    def Progress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Progress__Progress", None)
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
        old_value = getattr(self, f"_research20_Progress__progress", None)
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

class Named:

    pass
class research20_Position(Named):

    def __init__(self, description: str, research20_Position: "research20_Researcher" = None, research20_Position49: "research20_PublicationSystem" = None, research20_Position52: "research20_Position" = None, research20_Position50: "research20_Position" = None):
        self.description = description
        self.research20_Position = research20_Position
        self.research20_Position49 = research20_Position49
        self.research20_Position52 = research20_Position52
        self.research20_Position50 = research20_Position50
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def research20_Position(self):
        return self.__research20_Position

    @research20_Position.setter
    def research20_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Position__research20_Position", None)
        self.__research20_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Researcher8"):
                opp_val = getattr(old_value, "research20_Researcher8", None)
                if opp_val == self:
                    setattr(old_value, "research20_Researcher8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Researcher8"):
                opp_val = getattr(value, "research20_Researcher8", None)
                setattr(value, "research20_Researcher8", self)

    @property
    def research20_Position50(self):
        return self.__research20_Position50

    @research20_Position50.setter
    def research20_Position50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Position__research20_Position50", None)
        self.__research20_Position50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Position52"):
                opp_val = getattr(old_value, "research20_Position52", None)
                if opp_val == self:
                    setattr(old_value, "research20_Position52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Position52"):
                opp_val = getattr(value, "research20_Position52", None)
                setattr(value, "research20_Position52", self)

    @property
    def research20_Position49(self):
        return self.__research20_Position49

    @research20_Position49.setter
    def research20_Position49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Position__research20_Position49", None)
        self.__research20_Position49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_PublicationSystem48"):
                opp_val = getattr(old_value, "research20_PublicationSystem48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_PublicationSystem48"):
                opp_val = getattr(value, "research20_PublicationSystem48", None)
                if opp_val is None:
                    setattr(value, "research20_PublicationSystem48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research20_Position52(self):
        return self.__research20_Position52

    @research20_Position52.setter
    def research20_Position52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Position__research20_Position52", None)
        self.__research20_Position52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Position50"):
                opp_val = getattr(old_value, "research20_Position50", None)
                if opp_val == self:
                    setattr(old_value, "research20_Position50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Position50"):
                opp_val = getattr(value, "research20_Position50", None)
                setattr(value, "research20_Position50", self)

class research20_PublicationStructure(Named):

    pass
class research20_Keyword(Named):

    def __init__(self, word: str, research20_Keyword57: "research20_KnowledgeManager" = None, research20_Keyword: set["research20_Paper"] = None, research20_Keyword60: "research20_PaperKeyword" = None):
        self.word = word
        self.research20_Keyword57 = research20_Keyword57
        self.research20_Keyword = research20_Keyword if research20_Keyword is not None else set()
        self.research20_Keyword60 = research20_Keyword60
        
    @property
    def word(self) -> str:
        return self.__word

    @word.setter
    def word(self, word: str):
        self.__word = word

    @property
    def research20_Keyword(self):
        return self.__research20_Keyword

    @research20_Keyword.setter
    def research20_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Keyword__research20_Keyword", None)
        self.__research20_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research20_Paper54"):
                    opp_val = getattr(item, "research20_Paper54", None)
                    
                    if opp_val == self:
                        setattr(item, "research20_Paper54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research20_Paper54"):
                    opp_val = getattr(item, "research20_Paper54", None)
                    
                    setattr(item, "research20_Paper54", self)
                    

    @property
    def research20_Keyword57(self):
        return self.__research20_Keyword57

    @research20_Keyword57.setter
    def research20_Keyword57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Keyword__research20_Keyword57", None)
        self.__research20_Keyword57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_KnowledgeManager56"):
                opp_val = getattr(old_value, "research20_KnowledgeManager56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_KnowledgeManager56"):
                opp_val = getattr(value, "research20_KnowledgeManager56", None)
                if opp_val is None:
                    setattr(value, "research20_KnowledgeManager56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research20_Keyword60(self):
        return self.__research20_Keyword60

    @research20_Keyword60.setter
    def research20_Keyword60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Keyword__research20_Keyword60", None)
        self.__research20_Keyword60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_PaperKeyword59"):
                opp_val = getattr(old_value, "research20_PaperKeyword59", None)
                if opp_val == self:
                    setattr(old_value, "research20_PaperKeyword59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_PaperKeyword59"):
                opp_val = getattr(value, "research20_PaperKeyword59", None)
                setattr(value, "research20_PaperKeyword59", self)

class research20_ReviewNote(Named):

    def __init__(self, content: str, research20_ReviewNote32: "research20_Review" = None, research20_ReviewNote: "research20_Paragraph" = None):
        self.content = content
        self.research20_ReviewNote32 = research20_ReviewNote32
        self.research20_ReviewNote = research20_ReviewNote
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research20_ReviewNote32(self):
        return self.__research20_ReviewNote32

    @research20_ReviewNote32.setter
    def research20_ReviewNote32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_ReviewNote__research20_ReviewNote32", None)
        self.__research20_ReviewNote32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Review31"):
                opp_val = getattr(old_value, "research20_Review31", None)
                if opp_val == self:
                    setattr(old_value, "research20_Review31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Review31"):
                opp_val = getattr(value, "research20_Review31", None)
                setattr(value, "research20_Review31", self)

    @property
    def research20_ReviewNote(self):
        return self.__research20_ReviewNote

    @research20_ReviewNote.setter
    def research20_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_ReviewNote__research20_ReviewNote", None)
        self.__research20_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Paragraph22"):
                opp_val = getattr(old_value, "research20_Paragraph22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Paragraph22"):
                opp_val = getattr(value, "research20_Paragraph22", None)
                if opp_val is None:
                    setattr(value, "research20_Paragraph22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research20_Paper(Named):

    pass
class research20_PublicationSystem(Named):

    pass
class research20_Paragraph(Counted, Named):

    def __init__(self, content: str, research20_Paragraph: "research20_Paper" = None, research20_Paragraph29: "research20_Write" = None, research20_Paragraph22: set["research20_ReviewNote"] = None):
        self.content = content
        self.research20_Paragraph = research20_Paragraph
        self.research20_Paragraph29 = research20_Paragraph29
        self.research20_Paragraph22 = research20_Paragraph22 if research20_Paragraph22 is not None else set()
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def research20_Paragraph(self):
        return self.__research20_Paragraph

    @research20_Paragraph.setter
    def research20_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Paragraph__research20_Paragraph", None)
        self.__research20_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Paper"):
                opp_val = getattr(old_value, "research20_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Paper"):
                opp_val = getattr(value, "research20_Paper", None)
                if opp_val is None:
                    setattr(value, "research20_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research20_Paragraph29(self):
        return self.__research20_Paragraph29

    @research20_Paragraph29.setter
    def research20_Paragraph29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Paragraph__research20_Paragraph29", None)
        self.__research20_Paragraph29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Write28"):
                opp_val = getattr(old_value, "research20_Write28", None)
                if opp_val == self:
                    setattr(old_value, "research20_Write28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Write28"):
                opp_val = getattr(value, "research20_Write28", None)
                setattr(value, "research20_Write28", self)

    @property
    def research20_Paragraph22(self):
        return self.__research20_Paragraph22

    @research20_Paragraph22.setter
    def research20_Paragraph22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Paragraph__research20_Paragraph22", None)
        self.__research20_Paragraph22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research20_ReviewNote"):
                    opp_val = getattr(item, "research20_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "research20_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research20_ReviewNote"):
                    opp_val = getattr(item, "research20_ReviewNote", None)
                    
                    setattr(item, "research20_ReviewNote", self)
                    

class research20_KnowledgeManager(Named):

    pass
class research20_PublicationProcess(Named):

    def __init__(self, minTime: int, maxTime: int, research20_PublicationProcess: set["research20_Phase"] = None, research20_PublicationProcess24: "research20_Progress" = None, research20_PublicationProcess43: "research20_PublicationSystem" = None):
        self.minTime = minTime
        self.maxTime = maxTime
        self.research20_PublicationProcess = research20_PublicationProcess if research20_PublicationProcess is not None else set()
        self.research20_PublicationProcess24 = research20_PublicationProcess24
        self.research20_PublicationProcess43 = research20_PublicationProcess43
        
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
    def research20_PublicationProcess(self):
        return self.__research20_PublicationProcess

    @research20_PublicationProcess.setter
    def research20_PublicationProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_PublicationProcess__research20_PublicationProcess", None)
        self.__research20_PublicationProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research20_Phase"):
                    opp_val = getattr(item, "research20_Phase", None)
                    
                    if opp_val == self:
                        setattr(item, "research20_Phase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research20_Phase"):
                    opp_val = getattr(item, "research20_Phase", None)
                    
                    setattr(item, "research20_Phase", self)
                    

    @property
    def research20_PublicationProcess43(self):
        return self.__research20_PublicationProcess43

    @research20_PublicationProcess43.setter
    def research20_PublicationProcess43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_PublicationProcess__research20_PublicationProcess43", None)
        self.__research20_PublicationProcess43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_PublicationSystem"):
                opp_val = getattr(old_value, "research20_PublicationSystem", None)
                if opp_val == self:
                    setattr(old_value, "research20_PublicationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_PublicationSystem"):
                opp_val = getattr(value, "research20_PublicationSystem", None)
                setattr(value, "research20_PublicationSystem", self)

    @property
    def research20_PublicationProcess24(self):
        return self.__research20_PublicationProcess24

    @research20_PublicationProcess24.setter
    def research20_PublicationProcess24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_PublicationProcess__research20_PublicationProcess24", None)
        self.__research20_PublicationProcess24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Progress"):
                opp_val = getattr(old_value, "research20_Progress", None)
                if opp_val == self:
                    setattr(old_value, "research20_Progress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Progress"):
                opp_val = getattr(value, "research20_Progress", None)
                setattr(value, "research20_Progress", self)

class research20_Researcher:

    def __init__(self, name: str, forName: str, Researcher: "research20_Paper" = None, research20_Researcher: set["research20_Write"] = None, research20_Researcher3: set["research20_Review"] = None, authors: set["research20_Paper"] = None, research20_Researcher6: set["research20_Skill"] = None, research20_Researcher8: "research20_Position" = None, research20_Researcher10: set["research20_Collaboration"] = None, research20_Researcher34: "research20_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.Researcher = Researcher
        self.research20_Researcher = research20_Researcher if research20_Researcher is not None else set()
        self.research20_Researcher3 = research20_Researcher3 if research20_Researcher3 is not None else set()
        self.authors = authors if authors is not None else set()
        self.research20_Researcher6 = research20_Researcher6 if research20_Researcher6 is not None else set()
        self.research20_Researcher8 = research20_Researcher8
        self.research20_Researcher10 = research20_Researcher10 if research20_Researcher10 is not None else set()
        self.research20_Researcher34 = research20_Researcher34
        
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
    def research20_Researcher34(self):
        return self.__research20_Researcher34

    @research20_Researcher34.setter
    def research20_Researcher34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Researcher__research20_Researcher34", None)
        self.__research20_Researcher34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_PublicationStructure"):
                opp_val = getattr(old_value, "research20_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_PublicationStructure"):
                opp_val = getattr(value, "research20_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "research20_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Researcher__authors", None)
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
    def research20_Researcher3(self):
        return self.__research20_Researcher3

    @research20_Researcher3.setter
    def research20_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Researcher__research20_Researcher3", None)
        self.__research20_Researcher3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research20_Review"):
                    opp_val = getattr(item, "research20_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "research20_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research20_Review"):
                    opp_val = getattr(item, "research20_Review", None)
                    
                    setattr(item, "research20_Review", self)
                    

    @property
    def research20_Researcher10(self):
        return self.__research20_Researcher10

    @research20_Researcher10.setter
    def research20_Researcher10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Researcher__research20_Researcher10", None)
        self.__research20_Researcher10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research20_Collaboration"):
                    opp_val = getattr(item, "research20_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "research20_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research20_Collaboration"):
                    opp_val = getattr(item, "research20_Collaboration", None)
                    
                    setattr(item, "research20_Collaboration", self)
                    

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Researcher__Researcher", None)
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
    def research20_Researcher(self):
        return self.__research20_Researcher

    @research20_Researcher.setter
    def research20_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Researcher__research20_Researcher", None)
        self.__research20_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research20_Write"):
                    opp_val = getattr(item, "research20_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "research20_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research20_Write"):
                    opp_val = getattr(item, "research20_Write", None)
                    
                    setattr(item, "research20_Write", self)
                    

    @property
    def research20_Researcher6(self):
        return self.__research20_Researcher6

    @research20_Researcher6.setter
    def research20_Researcher6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Researcher__research20_Researcher6", None)
        self.__research20_Researcher6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research20_Skill"):
                    opp_val = getattr(item, "research20_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "research20_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research20_Skill"):
                    opp_val = getattr(item, "research20_Skill", None)
                    
                    setattr(item, "research20_Skill", self)
                    

    @property
    def research20_Researcher8(self):
        return self.__research20_Researcher8

    @research20_Researcher8.setter
    def research20_Researcher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Researcher__research20_Researcher8", None)
        self.__research20_Researcher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_Position"):
                opp_val = getattr(old_value, "research20_Position", None)
                if opp_val == self:
                    setattr(old_value, "research20_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_Position"):
                opp_val = getattr(value, "research20_Position", None)
                setattr(value, "research20_Position", self)

class research20_Phase:

    def __init__(self, name: str, research20_Phase: "research20_PublicationProcess" = None):
        self.name = name
        self.research20_Phase = research20_Phase
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def research20_Phase(self):
        return self.__research20_Phase

    @research20_Phase.setter
    def research20_Phase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research20_Phase__research20_Phase", None)
        self.__research20_Phase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research20_PublicationProcess"):
                opp_val = getattr(old_value, "research20_PublicationProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research20_PublicationProcess"):
                opp_val = getattr(value, "research20_PublicationProcess", None)
                if opp_val is None:
                    setattr(value, "research20_PublicationProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
