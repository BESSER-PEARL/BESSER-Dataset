from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ImportKind(Enum):
    extension = "extension"
    access = "access"
class DirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"


############################################
# Definition of Classes
############################################

class CallExp:

    pass
class Parameter:

    pass
class ResolveExp:

    pass
class QVTOperational_ResolveInExp(ResolveExp):

    pass
class ConstructorBody:

    pass
class InstantiationExp:

    pass
class QVTOperational_ObjectExp(InstantiationExp):

    pass
class RelationalTransformation:

    pass
class EntryOperation:

    pass
class Package:

    pass
class Element:

    pass
class QVTOperational_OperationBody(Element):

    pass
class QVTOperational_ModuleImport(Element):

    def __init__(self, kind: str, QVTOperational_ModuleImport: set["ModelType"] = None, QVTOperational_ModuleImport56: "Module" = None, QVTOperational_ModuleImport58: "Module" = None):
        self.kind = kind
        self.QVTOperational_ModuleImport = QVTOperational_ModuleImport if QVTOperational_ModuleImport is not None else set()
        self.QVTOperational_ModuleImport56 = QVTOperational_ModuleImport56
        self.QVTOperational_ModuleImport58 = QVTOperational_ModuleImport58
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def QVTOperational_ModuleImport56(self):
        return self.__QVTOperational_ModuleImport56

    @QVTOperational_ModuleImport56.setter
    def QVTOperational_ModuleImport56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModuleImport__QVTOperational_ModuleImport56", None)
        self.__QVTOperational_ModuleImport56 = value
        
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
    def QVTOperational_ModuleImport(self):
        return self.__QVTOperational_ModuleImport

    @QVTOperational_ModuleImport.setter
    def QVTOperational_ModuleImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModuleImport__QVTOperational_ModuleImport", None)
        self.__QVTOperational_ModuleImport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelType54"):
                    opp_val = getattr(item, "ModelType54", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelType54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelType54"):
                    opp_val = getattr(item, "ModelType54", None)
                    
                    setattr(item, "ModelType54", self)
                    

    @property
    def QVTOperational_ModuleImport58(self):
        return self.__QVTOperational_ModuleImport58

    @QVTOperational_ModuleImport58.setter
    def QVTOperational_ModuleImport58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModuleImport__QVTOperational_ModuleImport58", None)
        self.__QVTOperational_ModuleImport58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module59"):
                opp_val = getattr(old_value, "Module59", None)
                if opp_val == self:
                    setattr(old_value, "Module59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module59"):
                opp_val = getattr(value, "Module59", None)
                setattr(value, "Module59", self)

class ModelType:

    pass
class Variable:

    pass
class QVTOperational_VarParameter(Parameter, Variable):

    def __init__(self, kind: str, QVTOperational_VarParameter: "ImperativeOperation" = None, QVTOperational_VarParameter94: "ImperativeOperation" = None, Variable88: "QVTOperational_ResolveExp", Variable: "QVTOperational_Module", Variable71: "QVTOperational_OperationBody", Variable63: "QVTOperational_ObjectExp"):
        self.kind = kind
        self.QVTOperational_VarParameter = QVTOperational_VarParameter
        self.QVTOperational_VarParameter94 = QVTOperational_VarParameter94
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def QVTOperational_VarParameter94(self):
        return self.__QVTOperational_VarParameter94

    @QVTOperational_VarParameter94.setter
    def QVTOperational_VarParameter94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_VarParameter__QVTOperational_VarParameter94", None)
        self.__QVTOperational_VarParameter94 = value
        
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

    @property
    def QVTOperational_VarParameter(self):
        return self.__QVTOperational_VarParameter

    @QVTOperational_VarParameter.setter
    def QVTOperational_VarParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_VarParameter__QVTOperational_VarParameter", None)
        self.__QVTOperational_VarParameter = value
        
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

class Tag:

    pass
class ModuleImport:

    pass
class MappingOperation:

    pass
class ImperativeCallExp:

    pass
class QVTOperational_MappingCallExp(ImperativeCallExp):

    def __init__(self, isStrict: str):
        self.isStrict = isStrict
        
    @property
    def isStrict(self) -> str:
        return self.__isStrict

    @isStrict.setter
    def isStrict(self, isStrict: str):
        self.__isStrict = isStrict

class OperationalTransformation:

    pass
class RelationDomain:

    pass
class ModelParameter:

    pass
class Relation:

    pass
class ImperativeExpression:

    pass
class QVTOperational_ResolveExp(ImperativeExpression, CallExp):

    def __init__(self, isDeferred: str, isInverse: str, one: str, QVTOperational_ResolveExp: "OclExpression" = None, QVTOperational_ResolveExp87: "Variable" = None):
        self.isDeferred = isDeferred
        self.isInverse = isInverse
        self.one = one
        self.QVTOperational_ResolveExp = QVTOperational_ResolveExp
        self.QVTOperational_ResolveExp87 = QVTOperational_ResolveExp87
        
    @property
    def isInverse(self) -> str:
        return self.__isInverse

    @isInverse.setter
    def isInverse(self, isInverse: str):
        self.__isInverse = isInverse

    @property
    def isDeferred(self) -> str:
        return self.__isDeferred

    @isDeferred.setter
    def isDeferred(self, isDeferred: str):
        self.__isDeferred = isDeferred

    @property
    def one(self) -> str:
        return self.__one

    @one.setter
    def one(self, one: str):
        self.__one = one

    @property
    def QVTOperational_ResolveExp(self):
        return self.__QVTOperational_ResolveExp

    @QVTOperational_ResolveExp.setter
    def QVTOperational_ResolveExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ResolveExp__QVTOperational_ResolveExp", None)
        self.__QVTOperational_ResolveExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression85"):
                opp_val = getattr(old_value, "OclExpression85", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression85"):
                opp_val = getattr(value, "OclExpression85", None)
                setattr(value, "OclExpression85", self)

    @property
    def QVTOperational_ResolveExp87(self):
        return self.__QVTOperational_ResolveExp87

    @QVTOperational_ResolveExp87.setter
    def QVTOperational_ResolveExp87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ResolveExp__QVTOperational_ResolveExp87", None)
        self.__QVTOperational_ResolveExp87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable88"):
                opp_val = getattr(old_value, "Variable88", None)
                if opp_val == self:
                    setattr(old_value, "Variable88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable88"):
                opp_val = getattr(value, "Variable88", None)
                setattr(value, "Variable88", self)

class OperationCallExp:

    pass
class QVTOperational_ImperativeCallExp(ImperativeExpression, OperationCallExp):

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
class QVTOperational_OperationalTransformation(Module):

    pass
class QVTOperational_Library(Module):

    pass
class VarParameter:

    pass
class QVTOperational_ModelParameter(VarParameter):

    pass
class QVTOperational_MappingParameter(VarParameter):

    pass
class Operation:

    pass
class QVTOperational_ImperativeOperation(Operation):

    def __init__(self, isBlackbox: str, QVTOperational_ImperativeOperation: "OperationBody" = None, QVTOperational_ImperativeOperation7: "VarParameter" = None, QVTOperational_ImperativeOperation9: "ImperativeOperation" = None, QVTOperational_ImperativeOperation11: set["VarParameter"] = None):
        self.isBlackbox = isBlackbox
        self.QVTOperational_ImperativeOperation = QVTOperational_ImperativeOperation
        self.QVTOperational_ImperativeOperation7 = QVTOperational_ImperativeOperation7
        self.QVTOperational_ImperativeOperation9 = QVTOperational_ImperativeOperation9
        self.QVTOperational_ImperativeOperation11 = QVTOperational_ImperativeOperation11 if QVTOperational_ImperativeOperation11 is not None else set()
        
    @property
    def isBlackbox(self) -> str:
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox

    @property
    def QVTOperational_ImperativeOperation7(self):
        return self.__QVTOperational_ImperativeOperation7

    @QVTOperational_ImperativeOperation7.setter
    def QVTOperational_ImperativeOperation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__QVTOperational_ImperativeOperation7", None)
        self.__QVTOperational_ImperativeOperation7 = value
        
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
    def QVTOperational_ImperativeOperation9(self):
        return self.__QVTOperational_ImperativeOperation9

    @QVTOperational_ImperativeOperation9.setter
    def QVTOperational_ImperativeOperation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__QVTOperational_ImperativeOperation9", None)
        self.__QVTOperational_ImperativeOperation9 = value
        
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

    @property
    def QVTOperational_ImperativeOperation11(self):
        return self.__QVTOperational_ImperativeOperation11

    @QVTOperational_ImperativeOperation11.setter
    def QVTOperational_ImperativeOperation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__QVTOperational_ImperativeOperation11", None)
        self.__QVTOperational_ImperativeOperation11 = value if value is not None else set()
        
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
    def QVTOperational_ImperativeOperation(self):
        return self.__QVTOperational_ImperativeOperation

    @QVTOperational_ImperativeOperation.setter
    def QVTOperational_ImperativeOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__QVTOperational_ImperativeOperation", None)
        self.__QVTOperational_ImperativeOperation = value
        
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

class OclExpression:

    pass
class Class:

    pass
class QVTOperational_ModelType(Class):

    def __init__(self, conformanceKind: str, QVTOperational_ModelType: set["OclExpression"] = None, QVTOperational_ModelType40: set["Package"] = None, Class73: "QVTOperational_OperationalTransformation", Class: "QVTOperational_ContextualProperty"):
        self.conformanceKind = conformanceKind
        self.QVTOperational_ModelType = QVTOperational_ModelType if QVTOperational_ModelType is not None else set()
        self.QVTOperational_ModelType40 = QVTOperational_ModelType40 if QVTOperational_ModelType40 is not None else set()
        
    @property
    def conformanceKind(self) -> str:
        return self.__conformanceKind

    @conformanceKind.setter
    def conformanceKind(self, conformanceKind: str):
        self.__conformanceKind = conformanceKind

    @property
    def QVTOperational_ModelType(self):
        return self.__QVTOperational_ModelType

    @QVTOperational_ModelType.setter
    def QVTOperational_ModelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModelType__QVTOperational_ModelType", None)
        self.__QVTOperational_ModelType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression38"):
                    opp_val = getattr(item, "OclExpression38", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression38"):
                    opp_val = getattr(item, "OclExpression38", None)
                    
                    setattr(item, "OclExpression38", self)
                    

    @property
    def QVTOperational_ModelType40(self):
        return self.__QVTOperational_ModelType40

    @QVTOperational_ModelType40.setter
    def QVTOperational_ModelType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModelType__QVTOperational_ModelType40", None)
        self.__QVTOperational_ModelType40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

class QVTOperational_Module(Class, Package):

    def __init__(self, isBlackbox: str, QVTOperational_Module46: set["ModuleImport"] = None, QVTOperational_Module48: set["Tag"] = None, QVTOperational_Module50: set["Variable"] = None, QVTOperational_Module52: set["ModelType"] = None, QVTOperational_Module: set["Property"] = None, QVTOperational_Module44: "EntryOperation" = None, Class73: "QVTOperational_OperationalTransformation", Class: "QVTOperational_ContextualProperty", Package: "QVTOperational_ModelType"):
        self.isBlackbox = isBlackbox
        self.QVTOperational_Module46 = QVTOperational_Module46 if QVTOperational_Module46 is not None else set()
        self.QVTOperational_Module48 = QVTOperational_Module48 if QVTOperational_Module48 is not None else set()
        self.QVTOperational_Module50 = QVTOperational_Module50 if QVTOperational_Module50 is not None else set()
        self.QVTOperational_Module52 = QVTOperational_Module52 if QVTOperational_Module52 is not None else set()
        self.QVTOperational_Module = QVTOperational_Module if QVTOperational_Module is not None else set()
        self.QVTOperational_Module44 = QVTOperational_Module44
        
    @property
    def isBlackbox(self) -> str:
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox

    @property
    def QVTOperational_Module(self):
        return self.__QVTOperational_Module

    @QVTOperational_Module.setter
    def QVTOperational_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module", None)
        self.__QVTOperational_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property42"):
                    opp_val = getattr(item, "Property42", None)
                    
                    if opp_val == self:
                        setattr(item, "Property42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property42"):
                    opp_val = getattr(item, "Property42", None)
                    
                    setattr(item, "Property42", self)
                    

    @property
    def QVTOperational_Module46(self):
        return self.__QVTOperational_Module46

    @QVTOperational_Module46.setter
    def QVTOperational_Module46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module46", None)
        self.__QVTOperational_Module46 = value if value is not None else set()
        
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
    def QVTOperational_Module44(self):
        return self.__QVTOperational_Module44

    @QVTOperational_Module44.setter
    def QVTOperational_Module44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module44", None)
        self.__QVTOperational_Module44 = value
        
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
    def QVTOperational_Module48(self):
        return self.__QVTOperational_Module48

    @QVTOperational_Module48.setter
    def QVTOperational_Module48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module48", None)
        self.__QVTOperational_Module48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tag"):
                    opp_val = getattr(item, "Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tag"):
                    opp_val = getattr(item, "Tag", None)
                    
                    setattr(item, "Tag", self)
                    

    @property
    def QVTOperational_Module50(self):
        return self.__QVTOperational_Module50

    @QVTOperational_Module50.setter
    def QVTOperational_Module50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module50", None)
        self.__QVTOperational_Module50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    setattr(item, "Variable", self)
                    

    @property
    def QVTOperational_Module52(self):
        return self.__QVTOperational_Module52

    @QVTOperational_Module52.setter
    def QVTOperational_Module52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module52", None)
        self.__QVTOperational_Module52 = value if value is not None else set()
        
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
                    

class Property:

    pass
class QVTOperational_ContextualProperty(Property):

    pass
class OperationBody:

    pass
class QVTOperational_MappingBody(OperationBody):

    pass
class QVTOperational_ConstructorBody(OperationBody):

    pass
class ImperativeOperation:

    pass
class QVTOperational_EntryOperation(ImperativeOperation):

    pass
class QVTOperational_Helper(ImperativeOperation):

    def __init__(self, isQuery: str, ImperativeOperation: "QVTOperational_ImperativeOperation", ImperativeOperation95: "QVTOperational_VarParameter", ImperativeOperation92: "QVTOperational_VarParameter", ImperativeOperation68: "QVTOperational_OperationBody"):
        self.isQuery = isQuery
        
    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

class QVTOperational_MappingOperation(ImperativeOperation):

    pass
class QVTOperational_Constructor(ImperativeOperation):

    pass