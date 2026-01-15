from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class IdElement:

    pass
class base_ModelTrace(IdElement):

    def __init__(self, name: str, base_ModelTrace: "base_ModelTypeTrace" = None, base_ModelTrace8: "base_ModelElementTrace" = None):
        self.name = name
        self.base_ModelTrace = base_ModelTrace
        self.base_ModelTrace8 = base_ModelTrace8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def base_ModelTrace8(self):
        return self.__base_ModelTrace8

    @base_ModelTrace8.setter
    def base_ModelTrace8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_ModelTrace__base_ModelTrace8", None)
        self.__base_ModelTrace8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_ModelElementTrace7"):
                opp_val = getattr(old_value, "base_ModelElementTrace7", None)
                if opp_val == self:
                    setattr(old_value, "base_ModelElementTrace7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_ModelElementTrace7"):
                opp_val = getattr(value, "base_ModelElementTrace7", None)
                setattr(value, "base_ModelElementTrace7", self)

    @property
    def base_ModelTrace(self):
        return self.__base_ModelTrace

    @base_ModelTrace.setter
    def base_ModelTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_ModelTrace__base_ModelTrace", None)
        self.__base_ModelTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_ModelTypeTrace5"):
                opp_val = getattr(old_value, "base_ModelTypeTrace5", None)
                if opp_val == self:
                    setattr(old_value, "base_ModelTypeTrace5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_ModelTypeTrace5"):
                opp_val = getattr(value, "base_ModelTypeTrace5", None)
                setattr(value, "base_ModelTypeTrace5", self)

class base_ModuleTrace(IdElement):

    def __init__(self, source: str):
        self.source = source
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

class base_IdElement(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class base_PropertyTrace(IdElement):

    def __init__(self, name: str, base_PropertyTrace: "base_PropertyAccess" = None, base_PropertyTrace10: "base_ModelElementTrace" = None):
        self.name = name
        self.base_PropertyTrace = base_PropertyTrace
        self.base_PropertyTrace10 = base_PropertyTrace10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def base_PropertyTrace(self):
        return self.__base_PropertyTrace

    @base_PropertyTrace.setter
    def base_PropertyTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_PropertyTrace__base_PropertyTrace", None)
        self.__base_PropertyTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_PropertyAccess"):
                opp_val = getattr(old_value, "base_PropertyAccess", None)
                if opp_val == self:
                    setattr(old_value, "base_PropertyAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_PropertyAccess"):
                opp_val = getattr(value, "base_PropertyAccess", None)
                setattr(value, "base_PropertyAccess", self)

    @property
    def base_PropertyTrace10(self):
        return self.__base_PropertyTrace10

    @base_PropertyTrace10.setter
    def base_PropertyTrace10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_PropertyTrace__base_PropertyTrace10", None)
        self.__base_PropertyTrace10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_ModelElementTrace11"):
                opp_val = getattr(old_value, "base_ModelElementTrace11", None)
                if opp_val == self:
                    setattr(old_value, "base_ModelElementTrace11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_ModelElementTrace11"):
                opp_val = getattr(value, "base_ModelElementTrace11", None)
                setattr(value, "base_ModelElementTrace11", self)

class base_ModelTypeTrace(IdElement):

    def __init__(self, name: str, base_ModelTypeTrace: "base_AllInstancesAccess" = None, base_ModelTypeTrace5: "base_ModelTrace" = None):
        self.name = name
        self.base_ModelTypeTrace = base_ModelTypeTrace
        self.base_ModelTypeTrace5 = base_ModelTypeTrace5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def base_ModelTypeTrace5(self):
        return self.__base_ModelTypeTrace5

    @base_ModelTypeTrace5.setter
    def base_ModelTypeTrace5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_ModelTypeTrace__base_ModelTypeTrace5", None)
        self.__base_ModelTypeTrace5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_ModelTrace"):
                opp_val = getattr(old_value, "base_ModelTrace", None)
                if opp_val == self:
                    setattr(old_value, "base_ModelTrace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_ModelTrace"):
                opp_val = getattr(value, "base_ModelTrace", None)
                setattr(value, "base_ModelTrace", self)

    @property
    def base_ModelTypeTrace(self):
        return self.__base_ModelTypeTrace

    @base_ModelTypeTrace.setter
    def base_ModelTypeTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_ModelTypeTrace__base_ModelTypeTrace", None)
        self.__base_ModelTypeTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_AllInstancesAccess"):
                opp_val = getattr(old_value, "base_AllInstancesAccess", None)
                if opp_val == self:
                    setattr(old_value, "base_AllInstancesAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_AllInstancesAccess"):
                opp_val = getattr(value, "base_AllInstancesAccess", None)
                setattr(value, "base_AllInstancesAccess", self)

class base_ModelElementTrace(IdElement):

    def __init__(self, uri: str, base_ModelElementTrace: "base_ElementAccess" = None, base_ModelElementTrace11: "base_PropertyTrace" = None, base_ModelElementTrace7: "base_ModelTrace" = None):
        self.uri = uri
        self.base_ModelElementTrace = base_ModelElementTrace
        self.base_ModelElementTrace11 = base_ModelElementTrace11
        self.base_ModelElementTrace7 = base_ModelElementTrace7
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def base_ModelElementTrace7(self):
        return self.__base_ModelElementTrace7

    @base_ModelElementTrace7.setter
    def base_ModelElementTrace7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_ModelElementTrace__base_ModelElementTrace7", None)
        self.__base_ModelElementTrace7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_ModelTrace8"):
                opp_val = getattr(old_value, "base_ModelTrace8", None)
                if opp_val == self:
                    setattr(old_value, "base_ModelTrace8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_ModelTrace8"):
                opp_val = getattr(value, "base_ModelTrace8", None)
                setattr(value, "base_ModelTrace8", self)

    @property
    def base_ModelElementTrace(self):
        return self.__base_ModelElementTrace

    @base_ModelElementTrace.setter
    def base_ModelElementTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_ModelElementTrace__base_ModelElementTrace", None)
        self.__base_ModelElementTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_ElementAccess"):
                opp_val = getattr(old_value, "base_ElementAccess", None)
                if opp_val == self:
                    setattr(old_value, "base_ElementAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_ElementAccess"):
                opp_val = getattr(value, "base_ElementAccess", None)
                setattr(value, "base_ElementAccess", self)

    @property
    def base_ModelElementTrace11(self):
        return self.__base_ModelElementTrace11

    @base_ModelElementTrace11.setter
    def base_ModelElementTrace11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_ModelElementTrace__base_ModelElementTrace11", None)
        self.__base_ModelElementTrace11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_PropertyTrace10"):
                opp_val = getattr(old_value, "base_PropertyTrace10", None)
                if opp_val == self:
                    setattr(old_value, "base_PropertyTrace10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_PropertyTrace10"):
                opp_val = getattr(value, "base_PropertyTrace10", None)
                setattr(value, "base_PropertyTrace10", self)

class Access:

    pass
class base_AllInstancesAccess(Access):

    def __init__(self, ofKind: bool, base_AllInstancesAccess: "base_ModelTypeTrace" = None):
        self.ofKind = ofKind
        self.base_AllInstancesAccess = base_AllInstancesAccess
        
    @property
    def ofKind(self) -> bool:
        return self.__ofKind

    @ofKind.setter
    def ofKind(self, ofKind: bool):
        self.__ofKind = ofKind

    @property
    def base_AllInstancesAccess(self):
        return self.__base_AllInstancesAccess

    @base_AllInstancesAccess.setter
    def base_AllInstancesAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_AllInstancesAccess__base_AllInstancesAccess", None)
        self.__base_AllInstancesAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_ModelTypeTrace"):
                opp_val = getattr(old_value, "base_ModelTypeTrace", None)
                if opp_val == self:
                    setattr(old_value, "base_ModelTypeTrace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_ModelTypeTrace"):
                opp_val = getattr(value, "base_ModelTypeTrace", None)
                setattr(value, "base_ModelTypeTrace", self)

class base_PropertyAccess(Access):

    def __init__(self, value: str, base_PropertyAccess: "base_PropertyTrace" = None):
        self.value = value
        self.base_PropertyAccess = base_PropertyAccess
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def base_PropertyAccess(self):
        return self.__base_PropertyAccess

    @base_PropertyAccess.setter
    def base_PropertyAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_base_PropertyAccess__base_PropertyAccess", None)
        self.__base_PropertyAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base_PropertyTrace"):
                opp_val = getattr(old_value, "base_PropertyTrace", None)
                if opp_val == self:
                    setattr(old_value, "base_PropertyTrace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base_PropertyTrace"):
                opp_val = getattr(value, "base_PropertyTrace", None)
                setattr(value, "base_PropertyTrace", self)

class base_ElementAccess(Access):

    pass
class base_Access(IdElement):

    pass
class base_ExecutionTrace(IdElement):

    pass