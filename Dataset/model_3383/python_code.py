from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class errors_ValueCk:

    def __init__(self, value: str, errors_ValueCk: "errors_ColumnCk" = None):
        self.value = value
        self.errors_ValueCk = errors_ValueCk
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def errors_ValueCk(self):
        return self.__errors_ValueCk

    @errors_ValueCk.setter
    def errors_ValueCk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_ValueCk__errors_ValueCk", None)
        self.__errors_ValueCk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errors_ColumnCk9"):
                opp_val = getattr(old_value, "errors_ColumnCk9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errors_ColumnCk9"):
                opp_val = getattr(value, "errors_ColumnCk9", None)
                if opp_val is None:
                    setattr(value, "errors_ColumnCk9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class errors_ColumnCk:

    def __init__(self, columnName: str, errors_ColumnCk: "errors_CheckError" = None, errors_ColumnCk9: set["errors_ValueCk"] = None):
        self.columnName = columnName
        self.errors_ColumnCk = errors_ColumnCk
        self.errors_ColumnCk9 = errors_ColumnCk9 if errors_ColumnCk9 is not None else set()
        
    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def errors_ColumnCk9(self):
        return self.__errors_ColumnCk9

    @errors_ColumnCk9.setter
    def errors_ColumnCk9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_ColumnCk__errors_ColumnCk9", None)
        self.__errors_ColumnCk9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "errors_ValueCk"):
                    opp_val = getattr(item, "errors_ValueCk", None)
                    
                    if opp_val == self:
                        setattr(item, "errors_ValueCk", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "errors_ValueCk"):
                    opp_val = getattr(item, "errors_ValueCk", None)
                    
                    setattr(item, "errors_ValueCk", self)
                    

    @property
    def errors_ColumnCk(self):
        return self.__errors_ColumnCk

    @errors_ColumnCk.setter
    def errors_ColumnCk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_ColumnCk__errors_ColumnCk", None)
        self.__errors_ColumnCk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errors_CheckError"):
                opp_val = getattr(old_value, "errors_CheckError", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errors_CheckError"):
                opp_val = getattr(value, "errors_CheckError", None)
                if opp_val is None:
                    setattr(value, "errors_CheckError", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class errors_ColumnFk:

    def __init__(self, nameColumn: str, errors_ColumnFk: "errors_Table" = None):
        self.nameColumn = nameColumn
        self.errors_ColumnFk = errors_ColumnFk
        
    @property
    def nameColumn(self) -> str:
        return self.__nameColumn

    @nameColumn.setter
    def nameColumn(self, nameColumn: str):
        self.__nameColumn = nameColumn

    @property
    def errors_ColumnFk(self):
        return self.__errors_ColumnFk

    @errors_ColumnFk.setter
    def errors_ColumnFk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_ColumnFk__errors_ColumnFk", None)
        self.__errors_ColumnFk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errors_Table6"):
                opp_val = getattr(old_value, "errors_Table6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errors_Table6"):
                opp_val = getattr(value, "errors_Table6", None)
                if opp_val is None:
                    setattr(value, "errors_Table6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Error:

    pass
class errors_CheckError(Error):

    def __init__(self, nameTable: str, nameCk: str, porcent: str, errors_CheckError: set["errors_ColumnCk"] = None):
        self.nameTable = nameTable
        self.nameCk = nameCk
        self.porcent = porcent
        self.errors_CheckError = errors_CheckError if errors_CheckError is not None else set()
        
    @property
    def nameCk(self) -> str:
        return self.__nameCk

    @nameCk.setter
    def nameCk(self, nameCk: str):
        self.__nameCk = nameCk

    @property
    def nameTable(self) -> str:
        return self.__nameTable

    @nameTable.setter
    def nameTable(self, nameTable: str):
        self.__nameTable = nameTable

    @property
    def porcent(self) -> str:
        return self.__porcent

    @porcent.setter
    def porcent(self, porcent: str):
        self.__porcent = porcent

    @property
    def errors_CheckError(self):
        return self.__errors_CheckError

    @errors_CheckError.setter
    def errors_CheckError(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_CheckError__errors_CheckError", None)
        self.__errors_CheckError = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "errors_ColumnCk"):
                    opp_val = getattr(item, "errors_ColumnCk", None)
                    
                    if opp_val == self:
                        setattr(item, "errors_ColumnCk", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "errors_ColumnCk"):
                    opp_val = getattr(item, "errors_ColumnCk", None)
                    
                    setattr(item, "errors_ColumnCk", self)
                    

class errors_ForeignError(Error):

    def __init__(self, nameFk: str, porcent: str, errors_ForeignError: "errors_Table" = None, errors_ForeignError3: "errors_Table" = None):
        self.nameFk = nameFk
        self.porcent = porcent
        self.errors_ForeignError = errors_ForeignError
        self.errors_ForeignError3 = errors_ForeignError3
        
    @property
    def porcent(self) -> str:
        return self.__porcent

    @porcent.setter
    def porcent(self, porcent: str):
        self.__porcent = porcent

    @property
    def nameFk(self) -> str:
        return self.__nameFk

    @nameFk.setter
    def nameFk(self, nameFk: str):
        self.__nameFk = nameFk

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

class errors_Error:

    pass
class errors_Errores:

    pass
class errors_Table:

    def __init__(self, nameTable: str, errors_Table: "errors_ForeignError" = None, errors_Table4: "errors_ForeignError" = None, errors_Table6: set["errors_ColumnFk"] = None):
        self.nameTable = nameTable
        self.errors_Table = errors_Table
        self.errors_Table4 = errors_Table4
        self.errors_Table6 = errors_Table6 if errors_Table6 is not None else set()
        
    @property
    def nameTable(self) -> str:
        return self.__nameTable

    @nameTable.setter
    def nameTable(self, nameTable: str):
        self.__nameTable = nameTable

    @property
    def errors_Table4(self):
        return self.__errors_Table4

    @errors_Table4.setter
    def errors_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_Table__errors_Table4", None)
        self.__errors_Table4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errors_ForeignError3"):
                opp_val = getattr(old_value, "errors_ForeignError3", None)
                if opp_val == self:
                    setattr(old_value, "errors_ForeignError3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errors_ForeignError3"):
                opp_val = getattr(value, "errors_ForeignError3", None)
                setattr(value, "errors_ForeignError3", self)

    @property
    def errors_Table(self):
        return self.__errors_Table

    @errors_Table.setter
    def errors_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_Table__errors_Table", None)
        self.__errors_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "errors_ForeignError"):
                opp_val = getattr(old_value, "errors_ForeignError", None)
                if opp_val == self:
                    setattr(old_value, "errors_ForeignError", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "errors_ForeignError"):
                opp_val = getattr(value, "errors_ForeignError", None)
                setattr(value, "errors_ForeignError", self)

    @property
    def errors_Table6(self):
        return self.__errors_Table6

    @errors_Table6.setter
    def errors_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_errors_Table__errors_Table6", None)
        self.__errors_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "errors_ColumnFk"):
                    opp_val = getattr(item, "errors_ColumnFk", None)
                    
                    if opp_val == self:
                        setattr(item, "errors_ColumnFk", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "errors_ColumnFk"):
                    opp_val = getattr(item, "errors_ColumnFk", None)
                    
                    setattr(item, "errors_ColumnFk", self)
                    
