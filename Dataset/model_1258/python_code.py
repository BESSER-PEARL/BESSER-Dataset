from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
class ImportKind(Enum):
    extension = "extension"
    access = "access"


############################################
# Definition of Classes
############################################

class CallExp:

    pass
class qvtoperational_Element:

    pass
class Parameter:

    pass
class Variable:

    pass
class qvtoperational_VarParameter(Parameter, Variable):

    def __init__(self, kind: str, qvtoperational_VarParameter: "ImperativeOperation" = None, qvtoperational_VarParameter94: "ImperativeOperation" = None):
        self.kind = kind
        self.qvtoperational_VarParameter = qvtoperational_VarParameter
        self.qvtoperational_VarParameter94 = qvtoperational_VarParameter94
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def qvtoperational_VarParameter(self):
        return self.__qvtoperational_VarParameter

    @qvtoperational_VarParameter.setter
    def qvtoperational_VarParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_VarParameter__qvtoperational_VarParameter", None)
        self.__qvtoperational_VarParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation92"):
                opp_val = getattr(old_value, "ImperativeOperation92", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation92"):
                opp_val = getattr(value, "ImperativeOperation92", None)
                setattr(value, "ImperativeOperation92", self)

    @property
    def qvtoperational_VarParameter94(self):
        return self.__qvtoperational_VarParameter94

    @qvtoperational_VarParameter94.setter
    def qvtoperational_VarParameter94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_VarParameter__qvtoperational_VarParameter94", None)
        self.__qvtoperational_VarParameter94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation95"):
                opp_val = getattr(old_value, "ImperativeOperation95", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation95"):
                opp_val = getattr(value, "ImperativeOperation95", None)
                setattr(value, "ImperativeOperation95", self)

class ResolveExp:

    pass
class qvtoperational_ResolveInExp(ResolveExp):

    pass
class ConstructorBody:

    pass
class InstantiationExp:

    pass
class Dummy2:

    pass
class qvtoperational_Package:

    pass
class qvtoperational_ObjectExp(InstantiationExp):

    pass
class ModelType:

    pass
class qvtoperational_Variable:

    pass
class qvtoperational_TemplateableElement:

    pass
class ModuleImport:

    pass
class EntryOperation:

    pass
class MappingOperation:

    pass
class ImperativeCallExp:

    pass
class qvtoperational_MappingCallExp(ImperativeCallExp):

    def __init__(self, isStrict: str):
        self.isStrict = isStrict
        
    @property
    def isStrict(self) -> str:
        return self.__isStrict

    @isStrict.setter
    def isStrict(self, isStrict: str):
        self.__isStrict = isStrict

class Class:

    pass
class qvtoperational_Module(Class):

    def __init__(self, isBlackbox: str, qvtoperational_Module43: "EntryOperation" = None, qvtoperational_Module45: set["ModuleImport"] = None, qvtoperational_Module47: set["qvtoperational_TemplateableElement"] = None, qvtoperational_Module49: set["qvtoperational_Variable"] = None, qvtoperational_Module51: set["ModelType"] = None, qvtoperational_Module: set["qvtoperational_Property"] = None):
        self.isBlackbox = isBlackbox
        self.qvtoperational_Module43 = qvtoperational_Module43
        self.qvtoperational_Module45 = qvtoperational_Module45 if qvtoperational_Module45 is not None else set()
        self.qvtoperational_Module47 = qvtoperational_Module47 if qvtoperational_Module47 is not None else set()
        self.qvtoperational_Module49 = qvtoperational_Module49 if qvtoperational_Module49 is not None else set()
        self.qvtoperational_Module51 = qvtoperational_Module51 if qvtoperational_Module51 is not None else set()
        self.qvtoperational_Module = qvtoperational_Module if qvtoperational_Module is not None else set()
        
    @property
    def isBlackbox(self) -> str:
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox

    @property
    def qvtoperational_Module51(self):
        return self.__qvtoperational_Module51

    @qvtoperational_Module51.setter
    def qvtoperational_Module51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__qvtoperational_Module51", None)
        self.__qvtoperational_Module51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelType"):
                    opp_val = getattr(item, "ModelType", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelType"):
                    opp_val = getattr(item, "ModelType", None)
                    
                    setattr(item, "ModelType", self)
                    

    @property
    def qvtoperational_Module49(self):
        return self.__qvtoperational_Module49

    @qvtoperational_Module49.setter
    def qvtoperational_Module49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__qvtoperational_Module49", None)
        self.__qvtoperational_Module49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qvtoperational_Variable"):
                    opp_val = getattr(item, "qvtoperational_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "qvtoperational_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qvtoperational_Variable"):
                    opp_val = getattr(item, "qvtoperational_Variable", None)
                    
                    setattr(item, "qvtoperational_Variable", self)
                    

    @property
    def qvtoperational_Module45(self):
        return self.__qvtoperational_Module45

    @qvtoperational_Module45.setter
    def qvtoperational_Module45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__qvtoperational_Module45", None)
        self.__qvtoperational_Module45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModuleImport"):
                    opp_val = getattr(item, "ModuleImport", None)
                    
                    if opp_val == self:
                        setattr(item, "ModuleImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModuleImport"):
                    opp_val = getattr(item, "ModuleImport", None)
                    
                    setattr(item, "ModuleImport", self)
                    

    @property
    def qvtoperational_Module43(self):
        return self.__qvtoperational_Module43

    @qvtoperational_Module43.setter
    def qvtoperational_Module43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__qvtoperational_Module43", None)
        self.__qvtoperational_Module43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntryOperation"):
                opp_val = getattr(old_value, "EntryOperation", None)
                if opp_val == self:
                    setattr(old_value, "EntryOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntryOperation"):
                opp_val = getattr(value, "EntryOperation", None)
                setattr(value, "EntryOperation", self)

    @property
    def qvtoperational_Module47(self):
        return self.__qvtoperational_Module47

    @qvtoperational_Module47.setter
    def qvtoperational_Module47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__qvtoperational_Module47", None)
        self.__qvtoperational_Module47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qvtoperational_TemplateableElement"):
                    opp_val = getattr(item, "qvtoperational_TemplateableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "qvtoperational_TemplateableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qvtoperational_TemplateableElement"):
                    opp_val = getattr(item, "qvtoperational_TemplateableElement", None)
                    
                    setattr(item, "qvtoperational_TemplateableElement", self)
                    

    @property
    def qvtoperational_Module(self):
        return self.__qvtoperational_Module

    @qvtoperational_Module.setter
    def qvtoperational_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__qvtoperational_Module", None)
        self.__qvtoperational_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qvtoperational_Property41"):
                    opp_val = getattr(item, "qvtoperational_Property41", None)
                    
                    if opp_val == self:
                        setattr(item, "qvtoperational_Property41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qvtoperational_Property41"):
                    opp_val = getattr(item, "qvtoperational_Property41", None)
                    
                    setattr(item, "qvtoperational_Property41", self)
                    

class qvtoperational_ModelType(Class):

    def __init__(self, conformanceKind: str, qvtoperational_ModelType: set["qvtoperational_OCLExpression"] = None, qvtoperational_ModelType39: set["qvtoperational_Package"] = None):
        self.conformanceKind = conformanceKind
        self.qvtoperational_ModelType = qvtoperational_ModelType if qvtoperational_ModelType is not None else set()
        self.qvtoperational_ModelType39 = qvtoperational_ModelType39 if qvtoperational_ModelType39 is not None else set()
        
    @property
    def conformanceKind(self) -> str:
        return self.__conformanceKind

    @conformanceKind.setter
    def conformanceKind(self, conformanceKind: str):
        self.__conformanceKind = conformanceKind

    @property
    def qvtoperational_ModelType(self):
        return self.__qvtoperational_ModelType

    @qvtoperational_ModelType.setter
    def qvtoperational_ModelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModelType__qvtoperational_ModelType", None)
        self.__qvtoperational_ModelType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qvtoperational_OCLExpression37"):
                    opp_val = getattr(item, "qvtoperational_OCLExpression37", None)
                    
                    if opp_val == self:
                        setattr(item, "qvtoperational_OCLExpression37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qvtoperational_OCLExpression37"):
                    opp_val = getattr(item, "qvtoperational_OCLExpression37", None)
                    
                    setattr(item, "qvtoperational_OCLExpression37", self)
                    

    @property
    def qvtoperational_ModelType39(self):
        return self.__qvtoperational_ModelType39

    @qvtoperational_ModelType39.setter
    def qvtoperational_ModelType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModelType__qvtoperational_ModelType39", None)
        self.__qvtoperational_ModelType39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qvtoperational_Package"):
                    opp_val = getattr(item, "qvtoperational_Package", None)
                    
                    if opp_val == self:
                        setattr(item, "qvtoperational_Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qvtoperational_Package"):
                    opp_val = getattr(item, "qvtoperational_Package", None)
                    
                    setattr(item, "qvtoperational_Package", self)
                    

class DummyRelationDomain:

    pass
class ModelParameter:

    pass
class DummyRelation:

    pass
class Operation:

    pass
class qvtoperational_ImperativeOperation(Operation):

    def __init__(self, isBlackbox: str, qvtoperational_ImperativeOperation: "OperationBody" = None, qvtoperational_ImperativeOperation7: "VarParameter" = None, qvtoperational_ImperativeOperation9: "ImperativeOperation" = None, qvtoperational_ImperativeOperation11: set["VarParameter"] = None):
        self.isBlackbox = isBlackbox
        self.qvtoperational_ImperativeOperation = qvtoperational_ImperativeOperation
        self.qvtoperational_ImperativeOperation7 = qvtoperational_ImperativeOperation7
        self.qvtoperational_ImperativeOperation9 = qvtoperational_ImperativeOperation9
        self.qvtoperational_ImperativeOperation11 = qvtoperational_ImperativeOperation11 if qvtoperational_ImperativeOperation11 is not None else set()
        
    @property
    def isBlackbox(self) -> str:
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox

    @property
    def qvtoperational_ImperativeOperation7(self):
        return self.__qvtoperational_ImperativeOperation7

    @qvtoperational_ImperativeOperation7.setter
    def qvtoperational_ImperativeOperation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ImperativeOperation__qvtoperational_ImperativeOperation7", None)
        self.__qvtoperational_ImperativeOperation7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VarParameter"):
                opp_val = getattr(old_value, "VarParameter", None)
                if opp_val == self:
                    setattr(old_value, "VarParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VarParameter"):
                opp_val = getattr(value, "VarParameter", None)
                setattr(value, "VarParameter", self)

    @property
    def qvtoperational_ImperativeOperation(self):
        return self.__qvtoperational_ImperativeOperation

    @qvtoperational_ImperativeOperation.setter
    def qvtoperational_ImperativeOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ImperativeOperation__qvtoperational_ImperativeOperation", None)
        self.__qvtoperational_ImperativeOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationBody"):
                opp_val = getattr(old_value, "OperationBody", None)
                if opp_val == self:
                    setattr(old_value, "OperationBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationBody"):
                opp_val = getattr(value, "OperationBody", None)
                setattr(value, "OperationBody", self)

    @property
    def qvtoperational_ImperativeOperation11(self):
        return self.__qvtoperational_ImperativeOperation11

    @qvtoperational_ImperativeOperation11.setter
    def qvtoperational_ImperativeOperation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ImperativeOperation__qvtoperational_ImperativeOperation11", None)
        self.__qvtoperational_ImperativeOperation11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VarParameter12"):
                    opp_val = getattr(item, "VarParameter12", None)
                    
                    if opp_val == self:
                        setattr(item, "VarParameter12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VarParameter12"):
                    opp_val = getattr(item, "VarParameter12", None)
                    
                    setattr(item, "VarParameter12", self)
                    

    @property
    def qvtoperational_ImperativeOperation9(self):
        return self.__qvtoperational_ImperativeOperation9

    @qvtoperational_ImperativeOperation9.setter
    def qvtoperational_ImperativeOperation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ImperativeOperation__qvtoperational_ImperativeOperation9", None)
        self.__qvtoperational_ImperativeOperation9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation"):
                opp_val = getattr(old_value, "ImperativeOperation", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation"):
                opp_val = getattr(value, "ImperativeOperation", None)
                setattr(value, "ImperativeOperation", self)

class ImperativeExpression:

    pass
class qvtoperational_ResolveExp(CallExp, ImperativeExpression):

    def __init__(self, isDeferred: str, isInverse: str, one: str, qvtoperational_ResolveExp87: "qvtoperational_Variable" = None, qvtoperational_ResolveExp: "qvtoperational_OCLExpression" = None):
        self.isDeferred = isDeferred
        self.isInverse = isInverse
        self.one = one
        self.qvtoperational_ResolveExp87 = qvtoperational_ResolveExp87
        self.qvtoperational_ResolveExp = qvtoperational_ResolveExp
        
    @property
    def isDeferred(self) -> str:
        return self.__isDeferred

    @isDeferred.setter
    def isDeferred(self, isDeferred: str):
        self.__isDeferred = isDeferred

    @property
    def isInverse(self) -> str:
        return self.__isInverse

    @isInverse.setter
    def isInverse(self, isInverse: str):
        self.__isInverse = isInverse

    @property
    def one(self) -> str:
        return self.__one

    @one.setter
    def one(self, one: str):
        self.__one = one

    @property
    def qvtoperational_ResolveExp(self):
        return self.__qvtoperational_ResolveExp

    @qvtoperational_ResolveExp.setter
    def qvtoperational_ResolveExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ResolveExp__qvtoperational_ResolveExp", None)
        self.__qvtoperational_ResolveExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtoperational_OCLExpression85"):
                opp_val = getattr(old_value, "qvtoperational_OCLExpression85", None)
                if opp_val == self:
                    setattr(old_value, "qvtoperational_OCLExpression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtoperational_OCLExpression85"):
                opp_val = getattr(value, "qvtoperational_OCLExpression85", None)
                setattr(value, "qvtoperational_OCLExpression85", self)

    @property
    def qvtoperational_ResolveExp87(self):
        return self.__qvtoperational_ResolveExp87

    @qvtoperational_ResolveExp87.setter
    def qvtoperational_ResolveExp87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ResolveExp__qvtoperational_ResolveExp87", None)
        self.__qvtoperational_ResolveExp87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtoperational_Variable88"):
                opp_val = getattr(old_value, "qvtoperational_Variable88", None)
                if opp_val == self:
                    setattr(old_value, "qvtoperational_Variable88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtoperational_Variable88"):
                opp_val = getattr(value, "qvtoperational_Variable88", None)
                setattr(value, "qvtoperational_Variable88", self)

class OperationCallExp:

    pass
class qvtoperational_ImperativeCallExp(OperationCallExp, ImperativeExpression):

    def __init__(self, isVirtual: str):
        self.isVirtual = isVirtual
        
    @property
    def isVirtual(self) -> str:
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: str):
        self.__isVirtual = isVirtual

class Module:

    pass
class qvtoperational_OperationalTransformation(Module):

    pass
class qvtoperational_Library(Module):

    pass
class VarParameter:

    pass
class qvtoperational_MappingParameter(VarParameter):

    pass
class qvtoperational_ModelParameter(VarParameter):

    pass
class Element:

    pass
class qvtoperational_DummyRelationDomain(Element):

    pass
class qvtoperational_DummyRelationalTransformation(Element):

    pass
class qvtoperational_OperationBody(Element):

    pass
class qvtoperational_Tag(Element):

    def __init__(self, name: str, value: str, qvtoperational_Tag: set["qvtoperational_Element"] = None):
        self.name = name
        self.value = value
        self.qvtoperational_Tag = qvtoperational_Tag if qvtoperational_Tag is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def qvtoperational_Tag(self):
        return self.__qvtoperational_Tag

    @qvtoperational_Tag.setter
    def qvtoperational_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Tag__qvtoperational_Tag", None)
        self.__qvtoperational_Tag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qvtoperational_Element"):
                    opp_val = getattr(item, "qvtoperational_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "qvtoperational_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qvtoperational_Element"):
                    opp_val = getattr(item, "qvtoperational_Element", None)
                    
                    setattr(item, "qvtoperational_Element", self)
                    

class qvtoperational_ModuleImport(Element):

    def __init__(self, kind: str, qvtoperational_ModuleImport: set["ModelType"] = None, qvtoperational_ModuleImport55: "Module" = None, qvtoperational_ModuleImport57: "Module" = None):
        self.kind = kind
        self.qvtoperational_ModuleImport = qvtoperational_ModuleImport if qvtoperational_ModuleImport is not None else set()
        self.qvtoperational_ModuleImport55 = qvtoperational_ModuleImport55
        self.qvtoperational_ModuleImport57 = qvtoperational_ModuleImport57
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def qvtoperational_ModuleImport57(self):
        return self.__qvtoperational_ModuleImport57

    @qvtoperational_ModuleImport57.setter
    def qvtoperational_ModuleImport57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModuleImport__qvtoperational_ModuleImport57", None)
        self.__qvtoperational_ModuleImport57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module58"):
                opp_val = getattr(old_value, "Module58", None)
                if opp_val == self:
                    setattr(old_value, "Module58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module58"):
                opp_val = getattr(value, "Module58", None)
                setattr(value, "Module58", self)

    @property
    def qvtoperational_ModuleImport55(self):
        return self.__qvtoperational_ModuleImport55

    @qvtoperational_ModuleImport55.setter
    def qvtoperational_ModuleImport55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModuleImport__qvtoperational_ModuleImport55", None)
        self.__qvtoperational_ModuleImport55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module"):
                opp_val = getattr(old_value, "Module", None)
                if opp_val == self:
                    setattr(old_value, "Module", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module"):
                opp_val = getattr(value, "Module", None)
                setattr(value, "Module", self)

    @property
    def qvtoperational_ModuleImport(self):
        return self.__qvtoperational_ModuleImport

    @qvtoperational_ModuleImport.setter
    def qvtoperational_ModuleImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModuleImport__qvtoperational_ModuleImport", None)
        self.__qvtoperational_ModuleImport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelType53"):
                    opp_val = getattr(item, "ModelType53", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelType53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelType53"):
                    opp_val = getattr(item, "ModelType53", None)
                    
                    setattr(item, "ModelType53", self)
                    

class qvtoperational_DummyRelation(Element):

    pass
class qvtoperational_Property:

    pass
class qvtoperational_OCLExpression:

    pass
class qvtoperational_Class:

    pass
class Property:

    pass
class qvtoperational_ContextualProperty(Property):

    pass
class OperationBody:

    pass
class qvtoperational_MappingBody(OperationBody):

    pass
class qvtoperational_ConstructorBody(OperationBody):

    pass
class ImperativeOperation:

    pass
class qvtoperational_Helper(ImperativeOperation):

    def __init__(self, isQuery: str, ImperativeOperation95: "qvtoperational_VarParameter", ImperativeOperation92: "qvtoperational_VarParameter", ImperativeOperation: "qvtoperational_ImperativeOperation", ImperativeOperation67: "qvtoperational_OperationBody"):
        self.isQuery = isQuery
        
    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

class qvtoperational_MappingOperation(ImperativeOperation):

    pass
class qvtoperational_EntryOperation(ImperativeOperation):

    pass
class qvtoperational_Constructor(ImperativeOperation):

    pass