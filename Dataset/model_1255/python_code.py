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

class ResolveExp:

    pass
class QVTOperational_ResolveInExp(ResolveExp):

    pass
class QVTOperational_ResolveExp:

    def __init__(self, isDeferred: str, isInverse: str, one: str):
        self.isDeferred = isDeferred
        self.isInverse = isInverse
        self.one = one
        
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
    def isDeferred(self) -> str:
        return self.__isDeferred

    @isDeferred.setter
    def isDeferred(self, isDeferred: str):
        self.__isDeferred = isDeferred

class QVTOperational_VarParameter:

    def __init__(self, kind: str, QVTOperational_VarParameter: "ImperativeOperation" = None, QVTOperational_VarParameter38: "ImperativeOperation" = None):
        self.kind = kind
        self.QVTOperational_VarParameter = QVTOperational_VarParameter
        self.QVTOperational_VarParameter38 = QVTOperational_VarParameter38
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def QVTOperational_VarParameter38(self):
        return self.__QVTOperational_VarParameter38

    @QVTOperational_VarParameter38.setter
    def QVTOperational_VarParameter38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_VarParameter__QVTOperational_VarParameter38", None)
        self.__QVTOperational_VarParameter38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation39"):
                opp_val = getattr(old_value, "ImperativeOperation39", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation39"):
                opp_val = getattr(value, "ImperativeOperation39", None)
                setattr(value, "ImperativeOperation39", self)

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
            if hasattr(old_value, "ImperativeOperation36"):
                opp_val = getattr(old_value, "ImperativeOperation36", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation36"):
                opp_val = getattr(value, "ImperativeOperation36", None)
                setattr(value, "ImperativeOperation36", self)

class QVTOperational_OperationBody:

    pass
class ConstructorBody:

    pass
class QVTOperational_ObjectExp:

    pass
class QVTOperational_ModuleImport:

    def __init__(self, kind: str, QVTOperational_ModuleImport: set["ModelType"] = None, QVTOperational_ModuleImport24: "Module" = None, QVTOperational_ModuleImport26: "Module" = None):
        self.kind = kind
        self.QVTOperational_ModuleImport = QVTOperational_ModuleImport if QVTOperational_ModuleImport is not None else set()
        self.QVTOperational_ModuleImport24 = QVTOperational_ModuleImport24
        self.QVTOperational_ModuleImport26 = QVTOperational_ModuleImport26
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def QVTOperational_ModuleImport24(self):
        return self.__QVTOperational_ModuleImport24

    @QVTOperational_ModuleImport24.setter
    def QVTOperational_ModuleImport24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModuleImport__QVTOperational_ModuleImport24", None)
        self.__QVTOperational_ModuleImport24 = value
        
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
                if hasattr(item, "ModelType22"):
                    opp_val = getattr(item, "ModelType22", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelType22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelType22"):
                    opp_val = getattr(item, "ModelType22", None)
                    
                    setattr(item, "ModelType22", self)
                    

    @property
    def QVTOperational_ModuleImport26(self):
        return self.__QVTOperational_ModuleImport26

    @QVTOperational_ModuleImport26.setter
    def QVTOperational_ModuleImport26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModuleImport__QVTOperational_ModuleImport26", None)
        self.__QVTOperational_ModuleImport26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module27"):
                opp_val = getattr(old_value, "Module27", None)
                if opp_val == self:
                    setattr(old_value, "Module27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module27"):
                opp_val = getattr(value, "Module27", None)
                setattr(value, "Module27", self)

class ModelType:

    pass
class ModuleImport:

    pass
class EntryOperation:

    pass
class QVTOperational_Module:

    def __init__(self, isBlackbox: str, QVTOperational_Module: "EntryOperation" = None, QVTOperational_Module18: set["ModuleImport"] = None, QVTOperational_Module20: set["ModelType"] = None):
        self.isBlackbox = isBlackbox
        self.QVTOperational_Module = QVTOperational_Module
        self.QVTOperational_Module18 = QVTOperational_Module18 if QVTOperational_Module18 is not None else set()
        self.QVTOperational_Module20 = QVTOperational_Module20 if QVTOperational_Module20 is not None else set()
        
    @property
    def isBlackbox(self) -> str:
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox

    @property
    def QVTOperational_Module18(self):
        return self.__QVTOperational_Module18

    @QVTOperational_Module18.setter
    def QVTOperational_Module18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module18", None)
        self.__QVTOperational_Module18 = value if value is not None else set()
        
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
    def QVTOperational_Module20(self):
        return self.__QVTOperational_Module20

    @QVTOperational_Module20.setter
    def QVTOperational_Module20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module20", None)
        self.__QVTOperational_Module20 = value if value is not None else set()
        
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
    def QVTOperational_Module(self):
        return self.__QVTOperational_Module

    @QVTOperational_Module.setter
    def QVTOperational_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module", None)
        self.__QVTOperational_Module = value
        
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

class QVTOperational_ModelType:

    def __init__(self, conformanceKind: str):
        self.conformanceKind = conformanceKind
        
    @property
    def conformanceKind(self) -> str:
        return self.__conformanceKind

    @conformanceKind.setter
    def conformanceKind(self, conformanceKind: str):
        self.__conformanceKind = conformanceKind

class ModelParameter:

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

class Module:

    pass
class QVTOperational_OperationalTransformation(Module):

    pass
class QVTOperational_Library(Module):

    pass
class VarParameter:

    pass
class QVTOperational_MappingParameter(VarParameter):

    pass
class QVTOperational_ModelParameter(VarParameter):

    pass
class QVTOperational_ImperativeOperation:

    def __init__(self, isBlackbox: str, QVTOperational_ImperativeOperation4: "ImperativeOperation" = None, QVTOperational_ImperativeOperation: "OperationBody" = None, QVTOperational_ImperativeOperation2: "VarParameter" = None, QVTOperational_ImperativeOperation6: set["VarParameter"] = None):
        self.isBlackbox = isBlackbox
        self.QVTOperational_ImperativeOperation4 = QVTOperational_ImperativeOperation4
        self.QVTOperational_ImperativeOperation = QVTOperational_ImperativeOperation
        self.QVTOperational_ImperativeOperation2 = QVTOperational_ImperativeOperation2
        self.QVTOperational_ImperativeOperation6 = QVTOperational_ImperativeOperation6 if QVTOperational_ImperativeOperation6 is not None else set()
        
    @property
    def isBlackbox(self) -> str:
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox

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

    @property
    def QVTOperational_ImperativeOperation6(self):
        return self.__QVTOperational_ImperativeOperation6

    @QVTOperational_ImperativeOperation6.setter
    def QVTOperational_ImperativeOperation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__QVTOperational_ImperativeOperation6", None)
        self.__QVTOperational_ImperativeOperation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VarParameter7"):
                    opp_val = getattr(item, "VarParameter7", None)
                    
                    if opp_val == self:
                        setattr(item, "VarParameter7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VarParameter7"):
                    opp_val = getattr(item, "VarParameter7", None)
                    
                    setattr(item, "VarParameter7", self)
                    

    @property
    def QVTOperational_ImperativeOperation2(self):
        return self.__QVTOperational_ImperativeOperation2

    @QVTOperational_ImperativeOperation2.setter
    def QVTOperational_ImperativeOperation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__QVTOperational_ImperativeOperation2", None)
        self.__QVTOperational_ImperativeOperation2 = value
        
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
    def QVTOperational_ImperativeOperation4(self):
        return self.__QVTOperational_ImperativeOperation4

    @QVTOperational_ImperativeOperation4.setter
    def QVTOperational_ImperativeOperation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__QVTOperational_ImperativeOperation4", None)
        self.__QVTOperational_ImperativeOperation4 = value
        
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

class QVTOperational_ImperativeCallExp:

    def __init__(self, isVirtual: str):
        self.isVirtual = isVirtual
        
    @property
    def isVirtual(self) -> str:
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: str):
        self.__isVirtual = isVirtual

class QVTOperational_ContextualProperty:

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
class QVTOperational_MappingOperation(ImperativeOperation):

    pass
class QVTOperational_Helper(ImperativeOperation):

    def __init__(self, isQuery: str, ImperativeOperation: "QVTOperational_ImperativeOperation", ImperativeOperation39: "QVTOperational_VarParameter", ImperativeOperation30: "QVTOperational_OperationBody", ImperativeOperation36: "QVTOperational_VarParameter"):
        self.isQuery = isQuery
        
    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

class QVTOperational_Constructor(ImperativeOperation):

    pass