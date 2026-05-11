from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EventType(Enum):
    PRE = "PRE"
    POST = "POST"
    TIME = "TIME"
class ActionType(Enum):
    WS = "WS"
    AOP = "AOP"


############################################
# Definition of Classes
############################################

class ActivityEdge:

    pass
class PiServiceComposition_ObjectFlow(ActivityEdge):

    pass
class PiServiceComposition_ControlFlow(ActivityEdge):

    pass
class NamedElement:

    pass
class PiServiceComposition_ActivityNode(NamedElement):

    pass
class PiServiceComposition_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class PiServiceComposition_Variable:

    def __init__(self, name: str, type: str, PiServiceComposition_Variable: "PiServiceComposition_CompositionServiceModel" = None, PiServiceComposition_Variable49: "PiServiceComposition_Policy" = None):
        self.name = name
        self.type = type
        self.PiServiceComposition_Variable = PiServiceComposition_Variable
        self.PiServiceComposition_Variable49 = PiServiceComposition_Variable49
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def PiServiceComposition_Variable(self):
        return self.__PiServiceComposition_Variable

    @PiServiceComposition_Variable.setter
    def PiServiceComposition_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Variable__PiServiceComposition_Variable", None)
        self.__PiServiceComposition_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PiServiceComposition_CompositionServiceModel8"):
                opp_val = getattr(old_value, "PiServiceComposition_CompositionServiceModel8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PiServiceComposition_CompositionServiceModel8"):
                opp_val = getattr(value, "PiServiceComposition_CompositionServiceModel8", None)
                if opp_val is None:
                    setattr(value, "PiServiceComposition_CompositionServiceModel8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PiServiceComposition_Variable49(self):
        return self.__PiServiceComposition_Variable49

    @PiServiceComposition_Variable49.setter
    def PiServiceComposition_Variable49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Variable__PiServiceComposition_Variable49", None)
        self.__PiServiceComposition_Variable49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PiServiceComposition_Policy48"):
                opp_val = getattr(old_value, "PiServiceComposition_Policy48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PiServiceComposition_Policy48"):
                opp_val = getattr(value, "PiServiceComposition_Policy48", None)
                if opp_val is None:
                    setattr(value, "PiServiceComposition_Policy48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PiServiceComposition_Policy:

    def __init__(self, name: str, PiServiceComposition_Policy: "PiServiceComposition_CompositionServiceModel" = None, Policy43: "PiServiceComposition_BussinessCollaborator" = None, Policy45: "PiServiceComposition_Rule" = None, policy: set["PiServiceComposition_Rule"] = None, PiServiceComposition_Policy48: set["PiServiceComposition_Variable"] = None, hasPolices: set["PiServiceComposition_BussinessCollaborator"] = None, definePolices: set["PiServiceComposition_Action"] = None, PiServiceComposition_Policy40: "PiServiceComposition_ServiceActivity" = None, Policy: "PiServiceComposition_Action" = None):
        self.name = name
        self.PiServiceComposition_Policy = PiServiceComposition_Policy
        self.Policy43 = Policy43
        self.Policy45 = Policy45
        self.policy = policy if policy is not None else set()
        self.PiServiceComposition_Policy48 = PiServiceComposition_Policy48 if PiServiceComposition_Policy48 is not None else set()
        self.hasPolices = hasPolices if hasPolices is not None else set()
        self.definePolices = definePolices if definePolices is not None else set()
        self.PiServiceComposition_Policy40 = PiServiceComposition_Policy40
        self.Policy = Policy
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Policy43(self):
        return self.__Policy43

    @Policy43.setter
    def Policy43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Policy__Policy43", None)
        self.__Policy43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeOperation"):
                opp_val = getattr(old_value, "typeOperation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeOperation"):
                opp_val = getattr(value, "typeOperation", None)
                if opp_val is None:
                    setattr(value, "typeOperation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PiServiceComposition_Policy(self):
        return self.__PiServiceComposition_Policy

    @PiServiceComposition_Policy.setter
    def PiServiceComposition_Policy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Policy__PiServiceComposition_Policy", None)
        self.__PiServiceComposition_Policy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PiServiceComposition_CompositionServiceModel6"):
                opp_val = getattr(old_value, "PiServiceComposition_CompositionServiceModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PiServiceComposition_CompositionServiceModel6"):
                opp_val = getattr(value, "PiServiceComposition_CompositionServiceModel6", None)
                if opp_val is None:
                    setattr(value, "PiServiceComposition_CompositionServiceModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PiServiceComposition_Policy40(self):
        return self.__PiServiceComposition_Policy40

    @PiServiceComposition_Policy40.setter
    def PiServiceComposition_Policy40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Policy__PiServiceComposition_Policy40", None)
        self.__PiServiceComposition_Policy40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PiServiceComposition_ServiceActivity39"):
                opp_val = getattr(old_value, "PiServiceComposition_ServiceActivity39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PiServiceComposition_ServiceActivity39"):
                opp_val = getattr(value, "PiServiceComposition_ServiceActivity39", None)
                if opp_val is None:
                    setattr(value, "PiServiceComposition_ServiceActivity39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def policy(self):
        return self.__policy

    @policy.setter
    def policy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Policy__policy", None)
        self.__policy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rule"):
                    opp_val = getattr(item, "Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rule"):
                    opp_val = getattr(item, "Rule", None)
                    
                    setattr(item, "Rule", self)
                    

    @property
    def Policy45(self):
        return self.__Policy45

    @Policy45.setter
    def Policy45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Policy__Policy45", None)
        self.__Policy45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contains"):
                opp_val = getattr(old_value, "contains", None)
                if opp_val == self:
                    setattr(old_value, "contains", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contains"):
                opp_val = getattr(value, "contains", None)
                setattr(value, "contains", self)

    @property
    def PiServiceComposition_Policy48(self):
        return self.__PiServiceComposition_Policy48

    @PiServiceComposition_Policy48.setter
    def PiServiceComposition_Policy48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Policy__PiServiceComposition_Policy48", None)
        self.__PiServiceComposition_Policy48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PiServiceComposition_Variable49"):
                    opp_val = getattr(item, "PiServiceComposition_Variable49", None)
                    
                    if opp_val == self:
                        setattr(item, "PiServiceComposition_Variable49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PiServiceComposition_Variable49"):
                    opp_val = getattr(item, "PiServiceComposition_Variable49", None)
                    
                    setattr(item, "PiServiceComposition_Variable49", self)
                    

    @property
    def definePolices(self):
        return self.__definePolices

    @definePolices.setter
    def definePolices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Policy__definePolices", None)
        self.__definePolices = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    if opp_val == self:
                        setattr(item, "Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    setattr(item, "Action", self)
                    

    @property
    def hasPolices(self):
        return self.__hasPolices

    @hasPolices.setter
    def hasPolices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Policy__hasPolices", None)
        self.__hasPolices = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BussinessCollaborator"):
                    opp_val = getattr(item, "BussinessCollaborator", None)
                    
                    if opp_val == self:
                        setattr(item, "BussinessCollaborator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BussinessCollaborator"):
                    opp_val = getattr(item, "BussinessCollaborator", None)
                    
                    setattr(item, "BussinessCollaborator", self)
                    

    @property
    def Policy(self):
        return self.__Policy

    @Policy.setter
    def Policy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Policy__Policy", None)
        self.__Policy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "action"):
                opp_val = getattr(old_value, "action", None)
                if opp_val == self:
                    setattr(old_value, "action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "action"):
                opp_val = getattr(value, "action", None)
                setattr(value, "action", self)

class PiServiceComposition_ActivityEdge(NamedElement):

    pass
class PiServiceComposition_Activity(NamedElement):

    pass
class PiServiceComposition_ActivityPartition(NamedElement):

    def __init__(self, isDimension: bool, isExternal: bool, PiServiceComposition_ActivityPartition: "PiServiceComposition_CompositionServiceModel" = None, ActivityPartition: "PiServiceComposition_ActivityEdge" = None, ActivityPartition36: "PiServiceComposition_ActivityNode" = None, PiServiceComposition_ActivityPartition13: "PiServiceComposition_ActivityPartition" = None, PiServiceComposition_ActivityPartition11: "PiServiceComposition_ActivityPartition" = None, partition: set["PiServiceComposition_ActivityEdge"] = None, partition16: set["PiServiceComposition_ActivityNode"] = None):
        self.isDimension = isDimension
        self.isExternal = isExternal
        self.PiServiceComposition_ActivityPartition = PiServiceComposition_ActivityPartition
        self.ActivityPartition = ActivityPartition
        self.ActivityPartition36 = ActivityPartition36
        self.PiServiceComposition_ActivityPartition13 = PiServiceComposition_ActivityPartition13
        self.PiServiceComposition_ActivityPartition11 = PiServiceComposition_ActivityPartition11
        self.partition = partition if partition is not None else set()
        self.partition16 = partition16 if partition16 is not None else set()
        
        pass
    @property
    def isDimension(self):
        return self.__isDimension

    @isDimension.setter
    def isDimension(self, isDimension: bool):
        self.__isDimension = isDimension


    @property
    def isExternal(self):
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: bool):
        self.__isExternal = isExternal


    @property
    def partition16(self):
        return self.__partition16

    @partition16.setter
    def partition16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_ActivityPartition__partition16", None)
        self.__partition16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode"):
                    opp_val = getattr(item, "ActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode"):
                    opp_val = getattr(item, "ActivityNode", None)
                    
                    setattr(item, "ActivityNode", self)
                    

    @property
    def PiServiceComposition_ActivityPartition13(self):
        return self.__PiServiceComposition_ActivityPartition13

    @PiServiceComposition_ActivityPartition13.setter
    def PiServiceComposition_ActivityPartition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_ActivityPartition__PiServiceComposition_ActivityPartition13", None)
        self.__PiServiceComposition_ActivityPartition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PiServiceComposition_ActivityPartition11"):
                opp_val = getattr(old_value, "PiServiceComposition_ActivityPartition11", None)
                if opp_val == self:
                    setattr(old_value, "PiServiceComposition_ActivityPartition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PiServiceComposition_ActivityPartition11"):
                opp_val = getattr(value, "PiServiceComposition_ActivityPartition11", None)
                setattr(value, "PiServiceComposition_ActivityPartition11", self)

    @property
    def PiServiceComposition_ActivityPartition11(self):
        return self.__PiServiceComposition_ActivityPartition11

    @PiServiceComposition_ActivityPartition11.setter
    def PiServiceComposition_ActivityPartition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_ActivityPartition__PiServiceComposition_ActivityPartition11", None)
        self.__PiServiceComposition_ActivityPartition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PiServiceComposition_ActivityPartition13"):
                opp_val = getattr(old_value, "PiServiceComposition_ActivityPartition13", None)
                if opp_val == self:
                    setattr(old_value, "PiServiceComposition_ActivityPartition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PiServiceComposition_ActivityPartition13"):
                opp_val = getattr(value, "PiServiceComposition_ActivityPartition13", None)
                setattr(value, "PiServiceComposition_ActivityPartition13", self)

    @property
    def partition(self):
        return self.__partition

    @partition.setter
    def partition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_ActivityPartition__partition", None)
        self.__partition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    setattr(item, "ActivityEdge", self)
                    

    @property
    def ActivityPartition(self):
        return self.__ActivityPartition

    @ActivityPartition.setter
    def ActivityPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_ActivityPartition__ActivityPartition", None)
        self.__ActivityPartition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edges"):
                opp_val = getattr(old_value, "edges", None)
                if opp_val == self:
                    setattr(old_value, "edges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edges"):
                opp_val = getattr(value, "edges", None)
                setattr(value, "edges", self)

    @property
    def PiServiceComposition_ActivityPartition(self):
        return self.__PiServiceComposition_ActivityPartition

    @PiServiceComposition_ActivityPartition.setter
    def PiServiceComposition_ActivityPartition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_ActivityPartition__PiServiceComposition_ActivityPartition", None)
        self.__PiServiceComposition_ActivityPartition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PiServiceComposition_CompositionServiceModel"):
                opp_val = getattr(old_value, "PiServiceComposition_CompositionServiceModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PiServiceComposition_CompositionServiceModel"):
                opp_val = getattr(value, "PiServiceComposition_CompositionServiceModel", None)
                if opp_val is None:
                    setattr(value, "PiServiceComposition_CompositionServiceModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ActivityPartition36(self):
        return self.__ActivityPartition36

    @ActivityPartition36.setter
    def ActivityPartition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_ActivityPartition__ActivityPartition36", None)
        self.__ActivityPartition36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

class PiServiceComposition_CompositionServiceModel:

    pass
class ExecutableNode:

    pass
class PiServiceComposition_Action(ExecutableNode):

    def __init__(self, type: str, Action: "PiServiceComposition_Policy" = None, PiServiceComposition_Action: "PiServiceComposition_ServiceActivity" = None, action: "PiServiceComposition_Policy" = None):
        self.type = type
        self.Action = Action
        self.PiServiceComposition_Action = PiServiceComposition_Action
        self.action = action
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Action__action", None)
        self.__action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Policy"):
                opp_val = getattr(old_value, "Policy", None)
                if opp_val == self:
                    setattr(old_value, "Policy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Policy"):
                opp_val = getattr(value, "Policy", None)
                setattr(value, "Policy", self)

    @property
    def Action(self):
        return self.__Action

    @Action.setter
    def Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Action__Action", None)
        self.__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "definePolices"):
                opp_val = getattr(old_value, "definePolices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "definePolices"):
                opp_val = getattr(value, "definePolices", None)
                if opp_val is None:
                    setattr(value, "definePolices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PiServiceComposition_Action(self):
        return self.__PiServiceComposition_Action

    @PiServiceComposition_Action.setter
    def PiServiceComposition_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Action__PiServiceComposition_Action", None)
        self.__PiServiceComposition_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PiServiceComposition_ServiceActivity"):
                opp_val = getattr(old_value, "PiServiceComposition_ServiceActivity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PiServiceComposition_ServiceActivity"):
                opp_val = getattr(value, "PiServiceComposition_ServiceActivity", None)
                if opp_val is None:
                    setattr(value, "PiServiceComposition_ServiceActivity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Activity:

    pass
class PiServiceComposition_ServiceActivity(Activity):

    pass
class FinalNode:

    pass
class PiServiceComposition_ActivityFinalNode(FinalNode):

    pass
class PiServiceComposition_Rule:

    def __init__(self, name: str, event: str, condition: str, action: str, contains: "PiServiceComposition_Policy" = None, Rule: "PiServiceComposition_Policy" = None):
        self.name = name
        self.event = event
        self.condition = condition
        self.action = action
        self.contains = contains
        self.Rule = Rule
        
        pass
    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event


    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def contains(self):
        return self.__contains

    @contains.setter
    def contains(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Rule__contains", None)
        self.__contains = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Policy45"):
                opp_val = getattr(old_value, "Policy45", None)
                if opp_val == self:
                    setattr(old_value, "Policy45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Policy45"):
                opp_val = getattr(value, "Policy45", None)
                setattr(value, "Policy45", self)

    @property
    def Rule(self):
        return self.__Rule

    @Rule.setter
    def Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PiServiceComposition_Rule__Rule", None)
        self.__Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "policy"):
                opp_val = getattr(old_value, "policy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "policy"):
                opp_val = getattr(value, "policy", None)
                if opp_val is None:
                    setattr(value, "policy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ActivityPartition:

    pass
class PiServiceComposition_BussinessCollaborator(ActivityPartition):

    pass
class ControlNode:

    pass
class PiServiceComposition_DecisionNode(ControlNode):

    pass
class PiServiceComposition_MergeNode(ControlNode):

    pass
class PiServiceComposition_ForkNode(ControlNode):

    pass
class PiServiceComposition_JoinNode(ControlNode):

    pass
class PiServiceComposition_FinalNode(ControlNode):

    pass
class PiServiceComposition_InitialNode(ControlNode):

    pass
class ActivityNode:

    pass
class PiServiceComposition_ObjectNode(ActivityNode):

    pass
class PiServiceComposition_ExecutableNode(ActivityNode):

    pass
class PiServiceComposition_ControlNode(ActivityNode):

    pass