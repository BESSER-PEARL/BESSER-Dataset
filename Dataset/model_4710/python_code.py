from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SetMembership:

    pass
class SOS_set_ForAllIn(SetMembership):

    pass
class SOS_set_ExistsIn(SetMembership):

    pass
class VariableRef:

    pass
class SetOperator:

    pass
class SOS_set_Excluding(SetOperator):

    pass
class SOS_set_Union(SetOperator):

    pass
class set_SOS_AlgebraicConditionList:

    pass
class SetTerm:

    pass
class SOS_set_ModelSet(SetTerm):

    pass
class SOS_set_SetConstructor(SetTerm):

    pass
class SOS_set_SetOperator(SetTerm):

    pass
class SOS_set_SetMembership(SetTerm):

    pass
class SOS_adtmm_AbstractOperation(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SOS_adtmm_SortDeclaration:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SOS_set_Intersection(SetOperator):

    pass
class SOS_adtmm_AbstractEquation(ABC):

    pass
class SOS_adtmm_Term(ABC):

    pass
class Equation:

    pass
class SOS_adtmm_CondEquation:

    pass
class SOS_adtmm_Variable:

    def __init__(self, name: str, SOS_adtmm_Variable: "Sort" = None):
        self.name = name
        self.SOS_adtmm_Variable = SOS_adtmm_Variable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SOS_adtmm_Variable(self):
        return self.__SOS_adtmm_Variable

    @SOS_adtmm_Variable.setter
    def SOS_adtmm_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOS_adtmm_Variable__SOS_adtmm_Variable", None)
        self.__SOS_adtmm_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sort57"):
                opp_val = getattr(old_value, "Sort57", None)
                if opp_val == self:
                    setattr(old_value, "Sort57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sort57"):
                opp_val = getattr(value, "Sort57", None)
                setattr(value, "Sort57", self)

class Sort:

    pass
class SOS_set_Set(Sort):

    pass
class SOS_set_ModelSort(Sort):

    def __init__(self, className: str, packageName: str, Sort55: "SOS_adtmm_Operation", Sort57: "SOS_adtmm_Variable", Sort100: "SOS_set_Set", Sort: "SOS_adtmm_Operation"):
        self.className = className
        self.packageName = packageName
        
    @property
    def packageName(self) -> str:
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName

    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

class AbstractOperation:

    pass
class SOS_adtmm_AbstractGenericOp(AbstractOperation):

    pass
class SOS_adtmm_Operation(AbstractOperation):

    pass
class SOS_adtmm_Sort(ABC):

    pass
class SOS_adtmm_AtomicSort(Sort):

    pass
class SOS_adtmm_AbstractSort(ABC):

    pass
class Operation:

    pass
class SortDeclaration:

    pass
class SOS_adtmm_ADT:

    def __init__(self, name: str, SOS_adtmm_ADT51: set["CondEquation"] = None, SOS_adtmm_ADT: set["SortDeclaration"] = None, SOS_adtmm_ADT43: set["Operation"] = None, SOS_adtmm_ADT45: set["Operation"] = None, SOS_adtmm_ADT48: set["Variable"] = None):
        self.name = name
        self.SOS_adtmm_ADT51 = SOS_adtmm_ADT51 if SOS_adtmm_ADT51 is not None else set()
        self.SOS_adtmm_ADT = SOS_adtmm_ADT if SOS_adtmm_ADT is not None else set()
        self.SOS_adtmm_ADT43 = SOS_adtmm_ADT43 if SOS_adtmm_ADT43 is not None else set()
        self.SOS_adtmm_ADT45 = SOS_adtmm_ADT45 if SOS_adtmm_ADT45 is not None else set()
        self.SOS_adtmm_ADT48 = SOS_adtmm_ADT48 if SOS_adtmm_ADT48 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SOS_adtmm_ADT51(self):
        return self.__SOS_adtmm_ADT51

    @SOS_adtmm_ADT51.setter
    def SOS_adtmm_ADT51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOS_adtmm_ADT__SOS_adtmm_ADT51", None)
        self.__SOS_adtmm_ADT51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CondEquation"):
                    opp_val = getattr(item, "CondEquation", None)
                    
                    if opp_val == self:
                        setattr(item, "CondEquation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CondEquation"):
                    opp_val = getattr(item, "CondEquation", None)
                    
                    setattr(item, "CondEquation", self)
                    

    @property
    def SOS_adtmm_ADT43(self):
        return self.__SOS_adtmm_ADT43

    @SOS_adtmm_ADT43.setter
    def SOS_adtmm_ADT43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOS_adtmm_ADT__SOS_adtmm_ADT43", None)
        self.__SOS_adtmm_ADT43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def SOS_adtmm_ADT45(self):
        return self.__SOS_adtmm_ADT45

    @SOS_adtmm_ADT45.setter
    def SOS_adtmm_ADT45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOS_adtmm_ADT__SOS_adtmm_ADT45", None)
        self.__SOS_adtmm_ADT45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation46"):
                    opp_val = getattr(item, "Operation46", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation46"):
                    opp_val = getattr(item, "Operation46", None)
                    
                    setattr(item, "Operation46", self)
                    

    @property
    def SOS_adtmm_ADT48(self):
        return self.__SOS_adtmm_ADT48

    @SOS_adtmm_ADT48.setter
    def SOS_adtmm_ADT48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOS_adtmm_ADT__SOS_adtmm_ADT48", None)
        self.__SOS_adtmm_ADT48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable49"):
                    opp_val = getattr(item, "Variable49", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable49"):
                    opp_val = getattr(item, "Variable49", None)
                    
                    setattr(item, "Variable49", self)
                    

    @property
    def SOS_adtmm_ADT(self):
        return self.__SOS_adtmm_ADT

    @SOS_adtmm_ADT.setter
    def SOS_adtmm_ADT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOS_adtmm_ADT__SOS_adtmm_ADT", None)
        self.__SOS_adtmm_ADT = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SortDeclaration"):
                    opp_val = getattr(item, "SortDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "SortDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SortDeclaration"):
                    opp_val = getattr(item, "SortDeclaration", None)
                    
                    setattr(item, "SortDeclaration", self)
                    

class SOS_AlgebraicConditionList:

    pass
class AbstractEquation:

    pass
class SOS_adtmm_Equation(AbstractEquation):

    pass
class SOS_adtmm_Inequation(AbstractEquation):

    pass
class Term:

    pass
class SOS_set_ModelRelation(Term):

    def __init__(self, referenceName: str, SOS_set_ModelRelation: "VariableRef" = None, SOS_set_ModelRelation95: "VariableRef" = None, Term34: "SOS_TypeJudment", Term28: "SOS_TypeJudment", Term71: "SOS_adtmm_CTerm", Term80: "SOS_set_SetMembership", Term65: "SOS_adtmm_CTerm", Term20: "SOS_Transition", Term85: "SOS_set_SetOperator", Term: "SOS_Transition", Term83: "SOS_set_SetMembership", Term73: "SOS_adtmm_AbstractEquation", Term76: "SOS_adtmm_AbstractEquation", Term26: "SOS_Transition", Term88: "SOS_set_SetOperator", Term31: "SOS_TypeJudment", Term23: "SOS_Transition", Term92: "SOS_set_SetConstructor"):
        self.referenceName = referenceName
        self.SOS_set_ModelRelation = SOS_set_ModelRelation
        self.SOS_set_ModelRelation95 = SOS_set_ModelRelation95
        
    @property
    def referenceName(self) -> str:
        return self.__referenceName

    @referenceName.setter
    def referenceName(self, referenceName: str):
        self.__referenceName = referenceName

    @property
    def SOS_set_ModelRelation(self):
        return self.__SOS_set_ModelRelation

    @SOS_set_ModelRelation.setter
    def SOS_set_ModelRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOS_set_ModelRelation__SOS_set_ModelRelation", None)
        self.__SOS_set_ModelRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableRef"):
                opp_val = getattr(old_value, "VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableRef"):
                opp_val = getattr(value, "VariableRef", None)
                setattr(value, "VariableRef", self)

    @property
    def SOS_set_ModelRelation95(self):
        return self.__SOS_set_ModelRelation95

    @SOS_set_ModelRelation95.setter
    def SOS_set_ModelRelation95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOS_set_ModelRelation__SOS_set_ModelRelation95", None)
        self.__SOS_set_ModelRelation95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableRef96"):
                opp_val = getattr(old_value, "VariableRef96", None)
                if opp_val == self:
                    setattr(old_value, "VariableRef96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableRef96"):
                opp_val = getattr(value, "VariableRef96", None)
                setattr(value, "VariableRef96", self)

class SOS_adtmm_CTerm(Term):

    def __init__(self, iter: int, SOS_adtmm_CTerm: set["Term"] = None, SOS_adtmm_CTerm67: "Operation" = None, SOS_adtmm_CTerm70: "Term" = None, Term34: "SOS_TypeJudment", Term28: "SOS_TypeJudment", Term71: "SOS_adtmm_CTerm", Term80: "SOS_set_SetMembership", Term65: "SOS_adtmm_CTerm", Term20: "SOS_Transition", Term85: "SOS_set_SetOperator", Term: "SOS_Transition", Term83: "SOS_set_SetMembership", Term73: "SOS_adtmm_AbstractEquation", Term76: "SOS_adtmm_AbstractEquation", Term26: "SOS_Transition", Term88: "SOS_set_SetOperator", Term31: "SOS_TypeJudment", Term23: "SOS_Transition", Term92: "SOS_set_SetConstructor"):
        self.iter = iter
        self.SOS_adtmm_CTerm = SOS_adtmm_CTerm if SOS_adtmm_CTerm is not None else set()
        self.SOS_adtmm_CTerm67 = SOS_adtmm_CTerm67
        self.SOS_adtmm_CTerm70 = SOS_adtmm_CTerm70
        
    @property
    def iter(self) -> int:
        return self.__iter

    @iter.setter
    def iter(self, iter: int):
        self.__iter = iter

    @property
    def SOS_adtmm_CTerm(self):
        return self.__SOS_adtmm_CTerm

    @SOS_adtmm_CTerm.setter
    def SOS_adtmm_CTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOS_adtmm_CTerm__SOS_adtmm_CTerm", None)
        self.__SOS_adtmm_CTerm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Term65"):
                    opp_val = getattr(item, "Term65", None)
                    
                    if opp_val == self:
                        setattr(item, "Term65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Term65"):
                    opp_val = getattr(item, "Term65", None)
                    
                    setattr(item, "Term65", self)
                    

    @property
    def SOS_adtmm_CTerm70(self):
        return self.__SOS_adtmm_CTerm70

    @SOS_adtmm_CTerm70.setter
    def SOS_adtmm_CTerm70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOS_adtmm_CTerm__SOS_adtmm_CTerm70", None)
        self.__SOS_adtmm_CTerm70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Term71"):
                opp_val = getattr(old_value, "Term71", None)
                if opp_val == self:
                    setattr(old_value, "Term71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Term71"):
                opp_val = getattr(value, "Term71", None)
                setattr(value, "Term71", self)

    @property
    def SOS_adtmm_CTerm67(self):
        return self.__SOS_adtmm_CTerm67

    @SOS_adtmm_CTerm67.setter
    def SOS_adtmm_CTerm67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOS_adtmm_CTerm__SOS_adtmm_CTerm67", None)
        self.__SOS_adtmm_CTerm67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation68"):
                opp_val = getattr(old_value, "Operation68", None)
                if opp_val == self:
                    setattr(old_value, "Operation68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation68"):
                opp_val = getattr(value, "Operation68", None)
                setattr(value, "Operation68", self)

class SOS_set_SetTerm(Term):

    pass
class SOS_set_ModelClassAttribute(Term):

    def __init__(self, attributeName: str, SOS_set_ModelClassAttribute: "VariableRef" = None, Term34: "SOS_TypeJudment", Term28: "SOS_TypeJudment", Term71: "SOS_adtmm_CTerm", Term80: "SOS_set_SetMembership", Term65: "SOS_adtmm_CTerm", Term20: "SOS_Transition", Term85: "SOS_set_SetOperator", Term: "SOS_Transition", Term83: "SOS_set_SetMembership", Term73: "SOS_adtmm_AbstractEquation", Term76: "SOS_adtmm_AbstractEquation", Term26: "SOS_Transition", Term88: "SOS_set_SetOperator", Term31: "SOS_TypeJudment", Term23: "SOS_Transition", Term92: "SOS_set_SetConstructor"):
        self.attributeName = attributeName
        self.SOS_set_ModelClassAttribute = SOS_set_ModelClassAttribute
        
    @property
    def attributeName(self) -> str:
        return self.__attributeName

    @attributeName.setter
    def attributeName(self, attributeName: str):
        self.__attributeName = attributeName

    @property
    def SOS_set_ModelClassAttribute(self):
        return self.__SOS_set_ModelClassAttribute

    @SOS_set_ModelClassAttribute.setter
    def SOS_set_ModelClassAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SOS_set_ModelClassAttribute__SOS_set_ModelClassAttribute", None)
        self.__SOS_set_ModelClassAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableRef98"):
                opp_val = getattr(old_value, "VariableRef98", None)
                if opp_val == self:
                    setattr(old_value, "VariableRef98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableRef98"):
                opp_val = getattr(value, "VariableRef98", None)
                setattr(value, "VariableRef98", self)

class SOS_adtmm_VariableRef(Term):

    pass
class Condition:

    pass
class SOS_TypeJudment(Condition):

    pass
class SOS_AlgebraicCondition(Condition):

    pass
class CondEquation:

    pass
class SOS_Condition(ABC):

    pass
class Variable:

    pass
class SOS_Conclusion:

    pass
class SOS_PremisseList:

    pass
class ADT:

    pass
class SOS_Rule:

    pass
class SOS_Semantics:

    pass
class SOS_Transition(Condition):

    pass