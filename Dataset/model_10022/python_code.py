from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EnforcementMode(Enum):
    Creation = "Creation"
    Deletion = "Deletion"


############################################
# Definition of Classes
############################################

class qvtcorebase_Property:

    pass
class Variable:

    pass
class Domain:

    pass
class Assignment:

    pass
class qvtcorebase_VariableAssignment(Assignment):

    pass
class qvtcorebase_PropertyAssignment(Assignment):

    pass
class qvtcorebase_OperationCallExp:

    pass
class qvtcorebase_Variable:

    pass
class Pattern:

    pass
class qvtcorebase_CorePattern(Pattern):

    def __init__(self, qvtcorebase_CorePattern: set["qvtcorebase_Variable"] = None):
        self.qvtcorebase_CorePattern = qvtcorebase_CorePattern if qvtcorebase_CorePattern is not None else set()
        
        pass
    @property
    def qvtcorebase_CorePattern(self):
        return self.__qvtcorebase_CorePattern

    @qvtcorebase_CorePattern.setter
    def qvtcorebase_CorePattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcorebase_CorePattern__qvtcorebase_CorePattern", None)
        self.__qvtcorebase_CorePattern = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qvtcorebase_Variable"):
                    opp_val = getattr(item, "qvtcorebase_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "qvtcorebase_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qvtcorebase_Variable"):
                    opp_val = getattr(item, "qvtcorebase_Variable", None)
                    
                    setattr(item, "qvtcorebase_Variable", self)
                    

    def getAllVariables(self) :
        # TODO: Implement getAllVariables method
        pass

    def getArea(self) :
        # TODO: Implement getArea method
        pass

class qvtcorebase_RealizedVariable(Variable):

    pass
class CorePattern:

    pass
class qvtcorebase_BottomPattern(CorePattern):

    pass
class qvtcorebase_OCLExpression:

    pass
class qvtcorebase_GuardPattern(CorePattern):

    pass
class Element:

    pass
class qvtcorebase_EnforcementOperation(Element):

    def __init__(self, enforcementMode: str, EnforcementOperation: "qvtcorebase_BottomPattern" = None, enforcementOperation: "qvtcorebase_BottomPattern" = None, qvtcorebase_EnforcementOperation: "qvtcorebase_OperationCallExp" = None):
        self.enforcementMode = enforcementMode
        self.EnforcementOperation = EnforcementOperation
        self.enforcementOperation = enforcementOperation
        self.qvtcorebase_EnforcementOperation = qvtcorebase_EnforcementOperation
        
        pass
    @property
    def enforcementMode(self):
        return self.__enforcementMode

    @enforcementMode.setter
    def enforcementMode(self, enforcementMode: str):
        self.__enforcementMode = enforcementMode


    @property
    def EnforcementOperation(self):
        return self.__EnforcementOperation

    @EnforcementOperation.setter
    def EnforcementOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcorebase_EnforcementOperation__EnforcementOperation", None)
        self.__EnforcementOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bottomPattern10"):
                opp_val = getattr(old_value, "bottomPattern10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottomPattern10"):
                opp_val = getattr(value, "bottomPattern10", None)
                if opp_val is None:
                    setattr(value, "bottomPattern10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def enforcementOperation(self):
        return self.__enforcementOperation

    @enforcementOperation.setter
    def enforcementOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcorebase_EnforcementOperation__enforcementOperation", None)
        self.__enforcementOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottomPattern14"):
                opp_val = getattr(old_value, "BottomPattern14", None)
                if opp_val == self:
                    setattr(old_value, "BottomPattern14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottomPattern14"):
                opp_val = getattr(value, "BottomPattern14", None)
                setattr(value, "BottomPattern14", self)

    @property
    def qvtcorebase_EnforcementOperation(self):
        return self.__qvtcorebase_EnforcementOperation

    @qvtcorebase_EnforcementOperation.setter
    def qvtcorebase_EnforcementOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcorebase_EnforcementOperation__qvtcorebase_EnforcementOperation", None)
        self.__qvtcorebase_EnforcementOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtcorebase_OperationCallExp"):
                opp_val = getattr(old_value, "qvtcorebase_OperationCallExp", None)
                if opp_val == self:
                    setattr(old_value, "qvtcorebase_OperationCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtcorebase_OperationCallExp"):
                opp_val = getattr(value, "qvtcorebase_OperationCallExp", None)
                setattr(value, "qvtcorebase_OperationCallExp", self)

class qvtcorebase_Assignment(Element):

    def __init__(self, isDefault: str, assignment: "qvtcorebase_BottomPattern" = None, qvtcorebase_Assignment: "qvtcorebase_OCLExpression" = None, Assignment: "qvtcorebase_BottomPattern" = None):
        self.isDefault = isDefault
        self.assignment = assignment
        self.qvtcorebase_Assignment = qvtcorebase_Assignment
        self.Assignment = Assignment
        
        pass
    @property
    def isDefault(self):
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: str):
        self.__isDefault = isDefault


    @property
    def Assignment(self):
        return self.__Assignment

    @Assignment.setter
    def Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcorebase_Assignment__Assignment", None)
        self.__Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bottomPattern8"):
                opp_val = getattr(old_value, "bottomPattern8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottomPattern8"):
                opp_val = getattr(value, "bottomPattern8", None)
                if opp_val is None:
                    setattr(value, "bottomPattern8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qvtcorebase_Assignment(self):
        return self.__qvtcorebase_Assignment

    @qvtcorebase_Assignment.setter
    def qvtcorebase_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcorebase_Assignment__qvtcorebase_Assignment", None)
        self.__qvtcorebase_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtcorebase_OCLExpression"):
                opp_val = getattr(old_value, "qvtcorebase_OCLExpression", None)
                if opp_val == self:
                    setattr(old_value, "qvtcorebase_OCLExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtcorebase_OCLExpression"):
                opp_val = getattr(value, "qvtcorebase_OCLExpression", None)
                setattr(value, "qvtcorebase_OCLExpression", self)

    @property
    def assignment(self):
        return self.__assignment

    @assignment.setter
    def assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcorebase_Assignment__assignment", None)
        self.__assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottomPattern4"):
                opp_val = getattr(old_value, "BottomPattern4", None)
                if opp_val == self:
                    setattr(old_value, "BottomPattern4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottomPattern4"):
                opp_val = getattr(value, "BottomPattern4", None)
                setattr(value, "BottomPattern4", self)

class qvtcorebase_Area(Element):

    def __init__(self, area: "qvtcorebase_GuardPattern" = None, area2: "qvtcorebase_BottomPattern" = None, Area: "qvtcorebase_BottomPattern" = None, Area17: "qvtcorebase_GuardPattern" = None):
        self.area = area
        self.area2 = area2
        self.Area = Area
        self.Area17 = Area17
        
        pass
    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcorebase_Area__area", None)
        self.__area = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GuardPattern"):
                opp_val = getattr(old_value, "GuardPattern", None)
                if opp_val == self:
                    setattr(old_value, "GuardPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GuardPattern"):
                opp_val = getattr(value, "GuardPattern", None)
                setattr(value, "GuardPattern", self)

    @property
    def area2(self):
        return self.__area2

    @area2.setter
    def area2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcorebase_Area__area2", None)
        self.__area2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottomPattern"):
                opp_val = getattr(old_value, "BottomPattern", None)
                if opp_val == self:
                    setattr(old_value, "BottomPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottomPattern"):
                opp_val = getattr(value, "BottomPattern", None)
                setattr(value, "BottomPattern", self)

    @property
    def Area17(self):
        return self.__Area17

    @Area17.setter
    def Area17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcorebase_Area__Area17", None)
        self.__Area17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guardPattern"):
                opp_val = getattr(old_value, "guardPattern", None)
                if opp_val == self:
                    setattr(old_value, "guardPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guardPattern"):
                opp_val = getattr(value, "guardPattern", None)
                setattr(value, "guardPattern", self)

    @property
    def Area(self):
        return self.__Area

    @Area.setter
    def Area(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcorebase_Area__Area", None)
        self.__Area = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bottomPattern"):
                opp_val = getattr(old_value, "bottomPattern", None)
                if opp_val == self:
                    setattr(old_value, "bottomPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bottomPattern"):
                opp_val = getattr(value, "bottomPattern", None)
                setattr(value, "bottomPattern", self)

    def getAllVariables(self) :
        # TODO: Implement getAllVariables method
        pass

class Area:

    pass
class qvtcorebase_CoreDomain(Domain, Area):

    pass
class Rule:

    pass
class qvtcorebase_AbstractMapping(Rule, Area):

    def __init__(self):
        
        pass
    def getRefinement(self) :
        # TODO: Implement getRefinement method
        pass

    def getContext(self) :
        # TODO: Implement getContext method
        pass
