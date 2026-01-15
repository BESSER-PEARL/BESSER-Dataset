from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Error:

    pass
class errors_ForeignError(Error):

    def __init__(self, porcent: int, errors_ForeignError: "errors_Table" = None, errors_ForeignError3: "errors_Table" = None, errors_ForeignError6: set["errors_Column"] = None, errors_ForeignError8: "errors_Fk" = None):
        self.porcent = porcent
        self.errors_ForeignError = errors_ForeignError
        self.errors_ForeignError3 = errors_ForeignError3
        self.errors_ForeignError6 = errors_ForeignError6 if errors_ForeignError6 is not None else set()
        self.errors_ForeignError8 = errors_ForeignError8
        
    @property
    def porcent(self) -> int:
        return self.__porcent

    @porcent.setter
    def porcent(self, porcent: int):
        self.__porcent = porcent

    @property
    def errors_ForeignError6(self):
        return self.__errors_ForeignError6

    @errors_ForeignError6.setter
    def errors_ForeignError6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_ForeignError__errors_ForeignError6", None)
        self.__errors_ForeignError6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "errors_Column"):
                    opp_val = getattr(item, "errors_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "errors_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "errors_Column"):
                    opp_val = getattr(item, "errors_Column", None)
                    
                    setattr(item, "errors_Column", self)
                    

    @property
    def errors_ForeignError(self):
        return self.__errors_ForeignError

    @errors_ForeignError.setter
    def errors_ForeignError(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_ForeignError__errors_ForeignError", None)
        self.__errors_ForeignError = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errors_Table"):
                opp_val = getattr(old_value, "errors_Table", None)
                if opp_val == self:
                    setattr(old_value, "errors_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errors_Table"):
                opp_val = getattr(value, "errors_Table", None)
                setattr(value, "errors_Table", self)

    @property
    def errors_ForeignError3(self):
        return self.__errors_ForeignError3

    @errors_ForeignError3.setter
    def errors_ForeignError3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_ForeignError__errors_ForeignError3", None)
        self.__errors_ForeignError3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errors_Table4"):
                opp_val = getattr(old_value, "errors_Table4", None)
                if opp_val == self:
                    setattr(old_value, "errors_Table4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errors_Table4"):
                opp_val = getattr(value, "errors_Table4", None)
                setattr(value, "errors_Table4", self)

    @property
    def errors_ForeignError8(self):
        return self.__errors_ForeignError8

    @errors_ForeignError8.setter
    def errors_ForeignError8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_ForeignError__errors_ForeignError8", None)
        self.__errors_ForeignError8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errors_Fk"):
                opp_val = getattr(old_value, "errors_Fk", None)
                if opp_val == self:
                    setattr(old_value, "errors_Fk", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errors_Fk"):
                opp_val = getattr(value, "errors_Fk", None)
                setattr(value, "errors_Fk", self)

class errors_Error(ABC):

    def __init__(self, id: int, apply: bool, errors_Error: "errors_Errores" = None):
        self.id = id
        self.apply = apply
        self.errors_Error = errors_Error
        
    @property
    def apply(self) -> bool:
        return self.__apply

    @apply.setter
    def apply(self, apply: bool):
        self.__apply = apply

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def errors_Error(self):
        return self.__errors_Error

    @errors_Error.setter
    def errors_Error(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_Error__errors_Error", None)
        self.__errors_Error = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errors_Errores"):
                opp_val = getattr(old_value, "errors_Errores", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errors_Errores"):
                opp_val = getattr(value, "errors_Errores", None)
                if opp_val is None:
                    setattr(value, "errors_Errores", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class errors_Errores:

    pass
class errors_Fk:

    pass
class errors_Column:

    pass
class errors_Table:

    pass