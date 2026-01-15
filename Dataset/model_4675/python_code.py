from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ImportationMode(Enum):
    protecting = "protecting"
    including = "including"
    extending = "extending"


############################################
# Definition of Classes
############################################

class RenMapping:

    pass
class Maude_SortMapping(RenMapping):

    def __init__(self, to: str, Maude_SortMapping: "Maude_Sort" = None):
        self.to = to
        self.Maude_SortMapping = Maude_SortMapping
        
    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def Maude_SortMapping(self):
        return self.__Maude_SortMapping

    @Maude_SortMapping.setter
    def Maude_SortMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_SortMapping__Maude_SortMapping", None)
        self.__Maude_SortMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_Sort85"):
                opp_val = getattr(old_value, "Maude_Sort85", None)
                if opp_val == self:
                    setattr(old_value, "Maude_Sort85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_Sort85"):
                opp_val = getattr(value, "Maude_Sort85", None)
                setattr(value, "Maude_Sort85", self)

class ViewMapping:

    pass
class Maude_TermMapping(ViewMapping):

    pass
class Maude_ViewMapping(ABC):

    pass
class Maude_LabelMapping(RenMapping):

    def __init__(self, from: str, to: str):
        self.from = from
        self.to = to
        
    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def from(self) -> str:
        return self.__from

    @from.setter
    def from(self, from: str):
        self.__from = from

class Maude_OpMapping(RenMapping):

    def __init__(self, to: str, Maude_OpMapping: "Maude_Operation" = None):
        self.to = to
        self.Maude_OpMapping = Maude_OpMapping
        
    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def Maude_OpMapping(self):
        return self.__Maude_OpMapping

    @Maude_OpMapping.setter
    def Maude_OpMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_OpMapping__Maude_OpMapping", None)
        self.__Maude_OpMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_Operation89"):
                opp_val = getattr(old_value, "Maude_Operation89", None)
                if opp_val == self:
                    setattr(old_value, "Maude_Operation89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_Operation89"):
                opp_val = getattr(value, "Maude_Operation89", None)
                setattr(value, "Maude_Operation89", self)

class Maude_OpTypedMapping(RenMapping):

    def __init__(self, to: str, atts: str, Maude_OpTypedMapping: "Maude_Operation" = None):
        self.to = to
        self.atts = atts
        self.Maude_OpTypedMapping = Maude_OpTypedMapping
        
    @property
    def atts(self) -> str:
        return self.__atts

    @atts.setter
    def atts(self, atts: str):
        self.__atts = atts

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def Maude_OpTypedMapping(self):
        return self.__Maude_OpTypedMapping

    @Maude_OpTypedMapping.setter
    def Maude_OpTypedMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_OpTypedMapping__Maude_OpTypedMapping", None)
        self.__Maude_OpTypedMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_Operation87"):
                opp_val = getattr(old_value, "Maude_Operation87", None)
                if opp_val == self:
                    setattr(old_value, "Maude_Operation87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_Operation87"):
                opp_val = getattr(value, "Maude_Operation87", None)
                setattr(value, "Maude_Operation87", self)

class EquationalCond:

    pass
class Maude_BooleanCond(EquationalCond):

    pass
class Maude_MembershipCond(EquationalCond):

    pass
class Condition:

    pass
class Maude_RewriteCond(Condition):

    pass
class Maude_EquationalCond(Condition):

    pass
class Term:

    pass
class Maude_Variable(Term):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Maude_RecTerm(Term):

    def __init__(self, op: str, Maude_RecTerm: set["Maude_Term"] = None):
        self.op = op
        self.Maude_RecTerm = Maude_RecTerm if Maude_RecTerm is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def Maude_RecTerm(self):
        return self.__Maude_RecTerm

    @Maude_RecTerm.setter
    def Maude_RecTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_RecTerm__Maude_RecTerm", None)
        self.__Maude_RecTerm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Maude_Term70"):
                    opp_val = getattr(item, "Maude_Term70", None)
                    
                    if opp_val == self:
                        setattr(item, "Maude_Term70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Maude_Term70"):
                    opp_val = getattr(item, "Maude_Term70", None)
                    
                    setattr(item, "Maude_Term70", self)
                    

class Maude_Constant(Term):

    def __init__(self, op: str):
        self.op = op
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class Maude_EqualCond(EquationalCond):

    pass
class Maude_MatchingCond(EquationalCond):

    pass
class Maude_Term(ABC):

    pass
class Statement:

    pass
class Maude_Equation(Statement):

    pass
class Maude_Rule(Statement):

    pass
class Maude_Membership(Statement):

    pass
class Maude_Condition(ABC):

    pass
class Theory:

    pass
class Maude_STheory(Theory):

    pass
class Maude_FTheory(Theory):

    pass
class Maude_ModElement(ABC):

    pass
class MaudeTopEl:

    pass
class Type:

    pass
class Maude_Kind(Type):

    pass
class Maude_Type(ABC):

    def __init__(self, name: str, Maude_Type40: "Maude_Operation" = None, Maude_Type: "Maude_Operation" = None, Maude_Type68: "Maude_Term" = None):
        self.name = name
        self.Maude_Type40 = Maude_Type40
        self.Maude_Type = Maude_Type
        self.Maude_Type68 = Maude_Type68
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Maude_Type40(self):
        return self.__Maude_Type40

    @Maude_Type40.setter
    def Maude_Type40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_Type__Maude_Type40", None)
        self.__Maude_Type40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_Operation39"):
                opp_val = getattr(old_value, "Maude_Operation39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_Operation39"):
                opp_val = getattr(value, "Maude_Operation39", None)
                if opp_val is None:
                    setattr(value, "Maude_Operation39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Maude_Type(self):
        return self.__Maude_Type

    @Maude_Type.setter
    def Maude_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_Type__Maude_Type", None)
        self.__Maude_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_Operation"):
                opp_val = getattr(old_value, "Maude_Operation", None)
                if opp_val == self:
                    setattr(old_value, "Maude_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_Operation"):
                opp_val = getattr(value, "Maude_Operation", None)
                setattr(value, "Maude_Operation", self)

    @property
    def Maude_Type68(self):
        return self.__Maude_Type68

    @Maude_Type68.setter
    def Maude_Type68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_Type__Maude_Type68", None)
        self.__Maude_Type68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_Term67"):
                opp_val = getattr(old_value, "Maude_Term67", None)
                if opp_val == self:
                    setattr(old_value, "Maude_Term67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_Term67"):
                opp_val = getattr(value, "Maude_Term67", None)
                setattr(value, "Maude_Term67", self)

class ModElement:

    pass
class Maude_Sort(ModElement, Type):

    pass
class Maude_SubsortRel(ModElement):

    pass
class Maude_Statement(ModElement):

    def __init__(self, label: str, atts: str, Maude_Statement: set["Maude_Condition"] = None):
        self.label = label
        self.atts = atts
        self.Maude_Statement = Maude_Statement if Maude_Statement is not None else set()
        
    @property
    def atts(self) -> str:
        return self.__atts

    @atts.setter
    def atts(self, atts: str):
        self.__atts = atts

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def Maude_Statement(self):
        return self.__Maude_Statement

    @Maude_Statement.setter
    def Maude_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_Statement__Maude_Statement", None)
        self.__Maude_Statement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Maude_Condition"):
                    opp_val = getattr(item, "Maude_Condition", None)
                    
                    if opp_val == self:
                        setattr(item, "Maude_Condition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Maude_Condition"):
                    opp_val = getattr(item, "Maude_Condition", None)
                    
                    setattr(item, "Maude_Condition", self)
                    

class Maude_Operation(ModElement):

    def __init__(self, atts: str, name: str, Maude_Operation: "Maude_Type" = None, Maude_Operation39: set["Maude_Type"] = None, Maude_Operation87: "Maude_OpTypedMapping" = None, Maude_Operation89: "Maude_OpMapping" = None):
        self.atts = atts
        self.name = name
        self.Maude_Operation = Maude_Operation
        self.Maude_Operation39 = Maude_Operation39 if Maude_Operation39 is not None else set()
        self.Maude_Operation87 = Maude_Operation87
        self.Maude_Operation89 = Maude_Operation89
        
    @property
    def atts(self) -> str:
        return self.__atts

    @atts.setter
    def atts(self, atts: str):
        self.__atts = atts

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Maude_Operation87(self):
        return self.__Maude_Operation87

    @Maude_Operation87.setter
    def Maude_Operation87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_Operation__Maude_Operation87", None)
        self.__Maude_Operation87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_OpTypedMapping"):
                opp_val = getattr(old_value, "Maude_OpTypedMapping", None)
                if opp_val == self:
                    setattr(old_value, "Maude_OpTypedMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_OpTypedMapping"):
                opp_val = getattr(value, "Maude_OpTypedMapping", None)
                setattr(value, "Maude_OpTypedMapping", self)

    @property
    def Maude_Operation(self):
        return self.__Maude_Operation

    @Maude_Operation.setter
    def Maude_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_Operation__Maude_Operation", None)
        self.__Maude_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_Type"):
                opp_val = getattr(old_value, "Maude_Type", None)
                if opp_val == self:
                    setattr(old_value, "Maude_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_Type"):
                opp_val = getattr(value, "Maude_Type", None)
                setattr(value, "Maude_Type", self)

    @property
    def Maude_Operation89(self):
        return self.__Maude_Operation89

    @Maude_Operation89.setter
    def Maude_Operation89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_Operation__Maude_Operation89", None)
        self.__Maude_Operation89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_OpMapping"):
                opp_val = getattr(old_value, "Maude_OpMapping", None)
                if opp_val == self:
                    setattr(old_value, "Maude_OpMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_OpMapping"):
                opp_val = getattr(value, "Maude_OpMapping", None)
                setattr(value, "Maude_OpMapping", self)

    @property
    def Maude_Operation39(self):
        return self.__Maude_Operation39

    @Maude_Operation39.setter
    def Maude_Operation39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_Operation__Maude_Operation39", None)
        self.__Maude_Operation39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Maude_Type40"):
                    opp_val = getattr(item, "Maude_Type40", None)
                    
                    if opp_val == self:
                        setattr(item, "Maude_Type40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Maude_Type40"):
                    opp_val = getattr(item, "Maude_Type40", None)
                    
                    setattr(item, "Maude_Type40", self)
                    

class Maude_ModImportation(ModElement):

    def __init__(self, mode: str, Maude_ModImportation: "Maude_ModExpression" = None):
        self.mode = mode
        self.Maude_ModImportation = Maude_ModImportation
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def Maude_ModImportation(self):
        return self.__Maude_ModImportation

    @Maude_ModImportation.setter
    def Maude_ModImportation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_ModImportation__Maude_ModImportation", None)
        self.__Maude_ModImportation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_ModExpression27"):
                opp_val = getattr(old_value, "Maude_ModExpression27", None)
                if opp_val == self:
                    setattr(old_value, "Maude_ModExpression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_ModExpression27"):
                opp_val = getattr(value, "Maude_ModExpression27", None)
                setattr(value, "Maude_ModExpression27", self)

class Module:

    pass
class Maude_SModule(Module):

    pass
class Maude_FModule(Module):

    pass
class Maude_ModExpression(ABC):

    pass
class Maude_MaudeTopEl(ABC):

    def __init__(self, name: str, Maude_MaudeTopEl: "Maude_MaudeSpec" = None, Maude_MaudeTopEl3: "Maude_MaudeSpec" = None):
        self.name = name
        self.Maude_MaudeTopEl = Maude_MaudeTopEl
        self.Maude_MaudeTopEl3 = Maude_MaudeTopEl3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Maude_MaudeTopEl3(self):
        return self.__Maude_MaudeTopEl3

    @Maude_MaudeTopEl3.setter
    def Maude_MaudeTopEl3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_MaudeTopEl__Maude_MaudeTopEl3", None)
        self.__Maude_MaudeTopEl3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_MaudeSpec2"):
                opp_val = getattr(old_value, "Maude_MaudeSpec2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_MaudeSpec2"):
                opp_val = getattr(value, "Maude_MaudeSpec2", None)
                if opp_val is None:
                    setattr(value, "Maude_MaudeSpec2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Maude_MaudeTopEl(self):
        return self.__Maude_MaudeTopEl

    @Maude_MaudeTopEl.setter
    def Maude_MaudeTopEl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_MaudeTopEl__Maude_MaudeTopEl", None)
        self.__Maude_MaudeTopEl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_MaudeSpec"):
                opp_val = getattr(old_value, "Maude_MaudeSpec", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_MaudeSpec"):
                opp_val = getattr(value, "Maude_MaudeSpec", None)
                if opp_val is None:
                    setattr(value, "Maude_MaudeSpec", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Maude_MaudeSpec:

    pass
class Maude_Theory(MaudeTopEl):

    pass
class Maude_Module(MaudeTopEl):

    pass
class Maude_RenMapping(ViewMapping):

    pass
class Maude_View(MaudeTopEl):

    pass
class ModExpression:

    pass
class Maude_CompModExp(ModExpression):

    pass
class Maude_InstModExp(ModExpression):

    pass
class Maude_RenModExp(ModExpression):

    pass
class Maude_Parameter(ModExpression):

    def __init__(self, label: str, Maude_Parameter: "Maude_ModExpression" = None, Maude_Parameter22: "Maude_Module" = None):
        self.label = label
        self.Maude_Parameter = Maude_Parameter
        self.Maude_Parameter22 = Maude_Parameter22
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def Maude_Parameter22(self):
        return self.__Maude_Parameter22

    @Maude_Parameter22.setter
    def Maude_Parameter22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_Parameter__Maude_Parameter22", None)
        self.__Maude_Parameter22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_Module21"):
                opp_val = getattr(old_value, "Maude_Module21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_Module21"):
                opp_val = getattr(value, "Maude_Module21", None)
                if opp_val is None:
                    setattr(value, "Maude_Module21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Maude_Parameter(self):
        return self.__Maude_Parameter

    @Maude_Parameter.setter
    def Maude_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maude_Parameter__Maude_Parameter", None)
        self.__Maude_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maude_ModExpression16"):
                opp_val = getattr(old_value, "Maude_ModExpression16", None)
                if opp_val == self:
                    setattr(old_value, "Maude_ModExpression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maude_ModExpression16"):
                opp_val = getattr(value, "Maude_ModExpression16", None)
                setattr(value, "Maude_ModExpression16", self)

class Maude_ModuleIdModExp(ModExpression):

    pass
class Maude_TheoryIdModExp(ModExpression):

    pass