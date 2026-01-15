from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class brmodel_EObject:

    pass
class brmodel_Trace:

    pass
class Variable:

    pass
class brmodel_RelatedVariable(Variable):

    pass
class brmodel_RulePart:

    def __init__(self, granularity: str, brmodel_RulePart8: set["brmodel_Statement"] = None, brmodel_RulePart10: "brmodel_Statement" = None, brmodel_RulePart13: set["brmodel_ReachableMethod"] = None, brmodel_RulePart15: set["brmodel_ReachableVariable"] = None, brmodel_RulePart: "brmodel_Rule" = None, brmodel_RulePart6: "brmodel_RelatedMethod" = None):
        self.granularity = granularity
        self.brmodel_RulePart8 = brmodel_RulePart8 if brmodel_RulePart8 is not None else set()
        self.brmodel_RulePart10 = brmodel_RulePart10
        self.brmodel_RulePart13 = brmodel_RulePart13 if brmodel_RulePart13 is not None else set()
        self.brmodel_RulePart15 = brmodel_RulePart15 if brmodel_RulePart15 is not None else set()
        self.brmodel_RulePart = brmodel_RulePart
        self.brmodel_RulePart6 = brmodel_RulePart6
        
    @property
    def granularity(self) -> str:
        return self.__granularity

    @granularity.setter
    def granularity(self, granularity: str):
        self.__granularity = granularity

    @property
    def brmodel_RulePart10(self):
        return self.__brmodel_RulePart10

    @brmodel_RulePart10.setter
    def brmodel_RulePart10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_brmodel_RulePart__brmodel_RulePart10", None)
        self.__brmodel_RulePart10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "brmodel_Statement11"):
                opp_val = getattr(old_value, "brmodel_Statement11", None)
                if opp_val == self:
                    setattr(old_value, "brmodel_Statement11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "brmodel_Statement11"):
                opp_val = getattr(value, "brmodel_Statement11", None)
                setattr(value, "brmodel_Statement11", self)

    @property
    def brmodel_RulePart13(self):
        return self.__brmodel_RulePart13

    @brmodel_RulePart13.setter
    def brmodel_RulePart13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_brmodel_RulePart__brmodel_RulePart13", None)
        self.__brmodel_RulePart13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "brmodel_ReachableMethod"):
                    opp_val = getattr(item, "brmodel_ReachableMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "brmodel_ReachableMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "brmodel_ReachableMethod"):
                    opp_val = getattr(item, "brmodel_ReachableMethod", None)
                    
                    setattr(item, "brmodel_ReachableMethod", self)
                    

    @property
    def brmodel_RulePart(self):
        return self.__brmodel_RulePart

    @brmodel_RulePart.setter
    def brmodel_RulePart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_brmodel_RulePart__brmodel_RulePart", None)
        self.__brmodel_RulePart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "brmodel_Rule4"):
                opp_val = getattr(old_value, "brmodel_Rule4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "brmodel_Rule4"):
                opp_val = getattr(value, "brmodel_Rule4", None)
                if opp_val is None:
                    setattr(value, "brmodel_Rule4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def brmodel_RulePart15(self):
        return self.__brmodel_RulePart15

    @brmodel_RulePart15.setter
    def brmodel_RulePart15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_brmodel_RulePart__brmodel_RulePart15", None)
        self.__brmodel_RulePart15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "brmodel_ReachableVariable"):
                    opp_val = getattr(item, "brmodel_ReachableVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "brmodel_ReachableVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "brmodel_ReachableVariable"):
                    opp_val = getattr(item, "brmodel_ReachableVariable", None)
                    
                    setattr(item, "brmodel_ReachableVariable", self)
                    

    @property
    def brmodel_RulePart8(self):
        return self.__brmodel_RulePart8

    @brmodel_RulePart8.setter
    def brmodel_RulePart8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_brmodel_RulePart__brmodel_RulePart8", None)
        self.__brmodel_RulePart8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "brmodel_Statement"):
                    opp_val = getattr(item, "brmodel_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "brmodel_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "brmodel_Statement"):
                    opp_val = getattr(item, "brmodel_Statement", None)
                    
                    setattr(item, "brmodel_Statement", self)
                    

    @property
    def brmodel_RulePart6(self):
        return self.__brmodel_RulePart6

    @brmodel_RulePart6.setter
    def brmodel_RulePart6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_brmodel_RulePart__brmodel_RulePart6", None)
        self.__brmodel_RulePart6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "brmodel_RelatedMethod"):
                opp_val = getattr(old_value, "brmodel_RelatedMethod", None)
                if opp_val == self:
                    setattr(old_value, "brmodel_RelatedMethod", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "brmodel_RelatedMethod"):
                opp_val = getattr(value, "brmodel_RelatedMethod", None)
                setattr(value, "brmodel_RelatedMethod", self)

class brmodel_SlicedVariable(Variable):

    pass
class Trace:

    pass
class brmodel_Variable(Trace):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class brmodel_Method(Trace):

    def __init__(self, class: str, name: str):
        self.class = class
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

class Method:

    pass
class brmodel_RelatedMethod(Method):

    pass
class brmodel_ReachableVariable(Variable):

    pass
class brmodel_ReachableMethod(Method):

    def __init__(self, distance: str, brmodel_ReachableMethod: "brmodel_RulePart" = None):
        self.distance = distance
        self.brmodel_ReachableMethod = brmodel_ReachableMethod
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

    @property
    def brmodel_ReachableMethod(self):
        return self.__brmodel_ReachableMethod

    @brmodel_ReachableMethod.setter
    def brmodel_ReachableMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_brmodel_ReachableMethod__brmodel_ReachableMethod", None)
        self.__brmodel_ReachableMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "brmodel_RulePart13"):
                opp_val = getattr(old_value, "brmodel_RulePart13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "brmodel_RulePart13"):
                opp_val = getattr(value, "brmodel_RulePart13", None)
                if opp_val is None:
                    setattr(value, "brmodel_RulePart13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class brmodel_Statement(Trace):

    def __init__(self, textContent: str, brmodel_Statement: "brmodel_RulePart" = None, brmodel_Statement11: "brmodel_RulePart" = None):
        self.textContent = textContent
        self.brmodel_Statement = brmodel_Statement
        self.brmodel_Statement11 = brmodel_Statement11
        
    @property
    def textContent(self) -> str:
        return self.__textContent

    @textContent.setter
    def textContent(self, textContent: str):
        self.__textContent = textContent

    @property
    def brmodel_Statement(self):
        return self.__brmodel_Statement

    @brmodel_Statement.setter
    def brmodel_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_brmodel_Statement__brmodel_Statement", None)
        self.__brmodel_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "brmodel_RulePart8"):
                opp_val = getattr(old_value, "brmodel_RulePart8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "brmodel_RulePart8"):
                opp_val = getattr(value, "brmodel_RulePart8", None)
                if opp_val is None:
                    setattr(value, "brmodel_RulePart8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def brmodel_Statement11(self):
        return self.__brmodel_Statement11

    @brmodel_Statement11.setter
    def brmodel_Statement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_brmodel_Statement__brmodel_Statement11", None)
        self.__brmodel_Statement11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "brmodel_RulePart10"):
                opp_val = getattr(old_value, "brmodel_RulePart10", None)
                if opp_val == self:
                    setattr(old_value, "brmodel_RulePart10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "brmodel_RulePart10"):
                opp_val = getattr(value, "brmodel_RulePart10", None)
                setattr(value, "brmodel_RulePart10", self)

class brmodel_Rule:

    def __init__(self, id: str, brmodel_Rule: "brmodel_Model" = None, brmodel_Rule2: "brmodel_SlicedVariable" = None, brmodel_Rule4: set["brmodel_RulePart"] = None):
        self.id = id
        self.brmodel_Rule = brmodel_Rule
        self.brmodel_Rule2 = brmodel_Rule2
        self.brmodel_Rule4 = brmodel_Rule4 if brmodel_Rule4 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def brmodel_Rule(self):
        return self.__brmodel_Rule

    @brmodel_Rule.setter
    def brmodel_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_brmodel_Rule__brmodel_Rule", None)
        self.__brmodel_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "brmodel_Model"):
                opp_val = getattr(old_value, "brmodel_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "brmodel_Model"):
                opp_val = getattr(value, "brmodel_Model", None)
                if opp_val is None:
                    setattr(value, "brmodel_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def brmodel_Rule2(self):
        return self.__brmodel_Rule2

    @brmodel_Rule2.setter
    def brmodel_Rule2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_brmodel_Rule__brmodel_Rule2", None)
        self.__brmodel_Rule2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "brmodel_SlicedVariable"):
                opp_val = getattr(old_value, "brmodel_SlicedVariable", None)
                if opp_val == self:
                    setattr(old_value, "brmodel_SlicedVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "brmodel_SlicedVariable"):
                opp_val = getattr(value, "brmodel_SlicedVariable", None)
                setattr(value, "brmodel_SlicedVariable", self)

    @property
    def brmodel_Rule4(self):
        return self.__brmodel_Rule4

    @brmodel_Rule4.setter
    def brmodel_Rule4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_brmodel_Rule__brmodel_Rule4", None)
        self.__brmodel_Rule4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "brmodel_RulePart"):
                    opp_val = getattr(item, "brmodel_RulePart", None)
                    
                    if opp_val == self:
                        setattr(item, "brmodel_RulePart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "brmodel_RulePart"):
                    opp_val = getattr(item, "brmodel_RulePart", None)
                    
                    setattr(item, "brmodel_RulePart", self)
                    

class brmodel_Model:

    pass