from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class errors_Ck:

    pass
class errors_Registry:

    pass
class errors_Fk:

    pass
class errors_Column:

    pass
class errors_Table:

    pass
class Error:

    pass
class errors_CheckError(Error):

    def __init__(self, porcent: str, errors_CheckError: "errors_Ck" = None, errors_CheckError13: "errors_Table" = None, errors_CheckError16: set["errors_Registry"] = None):
        self.porcent = porcent
        self.errors_CheckError = errors_CheckError
        self.errors_CheckError13 = errors_CheckError13
        self.errors_CheckError16 = errors_CheckError16 if errors_CheckError16 is not None else set()
        
    @property
    def porcent(self) -> str:
        return self.__porcent

    @porcent.setter
    def porcent(self, porcent: str):
        self.__porcent = porcent

    @property
    def errors_CheckError16(self):
        return self.__errors_CheckError16

    @errors_CheckError16.setter
    def errors_CheckError16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_CheckError__errors_CheckError16", None)
        self.__errors_CheckError16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "errors_Registry17"):
                    opp_val = getattr(item, "errors_Registry17", None)
                    
                    if opp_val == self:
                        setattr(item, "errors_Registry17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "errors_Registry17"):
                    opp_val = getattr(item, "errors_Registry17", None)
                    
                    setattr(item, "errors_Registry17", self)
                    

    @property
    def errors_CheckError13(self):
        return self.__errors_CheckError13

    @errors_CheckError13.setter
    def errors_CheckError13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_CheckError__errors_CheckError13", None)
        self.__errors_CheckError13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errors_Table14"):
                opp_val = getattr(old_value, "errors_Table14", None)
                if opp_val == self:
                    setattr(old_value, "errors_Table14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errors_Table14"):
                opp_val = getattr(value, "errors_Table14", None)
                setattr(value, "errors_Table14", self)

    @property
    def errors_CheckError(self):
        return self.__errors_CheckError

    @errors_CheckError.setter
    def errors_CheckError(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_CheckError__errors_CheckError", None)
        self.__errors_CheckError = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errors_Ck"):
                opp_val = getattr(old_value, "errors_Ck", None)
                if opp_val == self:
                    setattr(old_value, "errors_Ck", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errors_Ck"):
                opp_val = getattr(value, "errors_Ck", None)
                setattr(value, "errors_Ck", self)

class errors_ForeignError(Error):

    def __init__(self, porcent: str, errors_ForeignError: "errors_Table" = None, errors_ForeignError3: "errors_Table" = None, errors_ForeignError6: set["errors_Column"] = None, errors_ForeignError8: "errors_Fk" = None, errors_ForeignError10: set["errors_Registry"] = None):
        self.porcent = porcent
        self.errors_ForeignError = errors_ForeignError
        self.errors_ForeignError3 = errors_ForeignError3
        self.errors_ForeignError6 = errors_ForeignError6 if errors_ForeignError6 is not None else set()
        self.errors_ForeignError8 = errors_ForeignError8
        self.errors_ForeignError10 = errors_ForeignError10 if errors_ForeignError10 is not None else set()
        
    @property
    def porcent(self) -> str:
        return self.__porcent

    @porcent.setter
    def porcent(self, porcent: str):
        self.__porcent = porcent

    @property
    def errors_ForeignError10(self):
        return self.__errors_ForeignError10

    @errors_ForeignError10.setter
    def errors_ForeignError10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_ForeignError__errors_ForeignError10", None)
        self.__errors_ForeignError10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "errors_Registry"):
                    opp_val = getattr(item, "errors_Registry", None)
                    
                    if opp_val == self:
                        setattr(item, "errors_Registry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "errors_Registry"):
                    opp_val = getattr(item, "errors_Registry", None)
                    
                    setattr(item, "errors_Registry", self)
                    

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

class errors_Error:

    def __init__(self, id: str, apply: str, errors_Error: "errors_Errores" = None):
        self.id = id
        self.apply = apply
        self.errors_Error = errors_Error
        
    @property
    def apply(self) -> str:
        return self.__apply

    @apply.setter
    def apply(self, apply: str):
        self.__apply = apply

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
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