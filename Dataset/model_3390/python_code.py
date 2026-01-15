from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class DML_Value:

    def __init__(self, value: str, DML_Value: "DML_Registry" = None, DML_Value8: "DML_Column" = None):
        self.value = value
        self.DML_Value = DML_Value
        self.DML_Value8 = DML_Value8
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def DML_Value(self):
        return self.__DML_Value

    @DML_Value.setter
    def DML_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_Value__DML_Value", None)
        self.__DML_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_Registry6"):
                opp_val = getattr(old_value, "DML_Registry6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_Registry6"):
                opp_val = getattr(value, "DML_Registry6", None)
                if opp_val is None:
                    setattr(value, "DML_Registry6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DML_Value8(self):
        return self.__DML_Value8

    @DML_Value8.setter
    def DML_Value8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_Value__DML_Value8", None)
        self.__DML_Value8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_Column9"):
                opp_val = getattr(old_value, "DML_Column9", None)
                if opp_val == self:
                    setattr(old_value, "DML_Column9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_Column9"):
                opp_val = getattr(value, "DML_Column9", None)
                setattr(value, "DML_Column9", self)

class DML_Column:

    def __init__(self, columnName: str, DML_Column: "DML_InsertInto" = None, DML_Column9: "DML_Value" = None):
        self.columnName = columnName
        self.DML_Column = DML_Column
        self.DML_Column9 = DML_Column9
        
    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def DML_Column9(self):
        return self.__DML_Column9

    @DML_Column9.setter
    def DML_Column9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_Column__DML_Column9", None)
        self.__DML_Column9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_Value8"):
                opp_val = getattr(old_value, "DML_Value8", None)
                if opp_val == self:
                    setattr(old_value, "DML_Value8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_Value8"):
                opp_val = getattr(value, "DML_Value8", None)
                setattr(value, "DML_Value8", self)

    @property
    def DML_Column(self):
        return self.__DML_Column

    @DML_Column.setter
    def DML_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_Column__DML_Column", None)
        self.__DML_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_InsertInto4"):
                opp_val = getattr(old_value, "DML_InsertInto4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_InsertInto4"):
                opp_val = getattr(value, "DML_InsertInto4", None)
                if opp_val is None:
                    setattr(value, "DML_InsertInto4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DML_Registry:

    pass
class DML_InsertInto:

    def __init__(self, tableName: str, DML_InsertInto: "DML_InsertsStatements" = None, DML_InsertInto2: "DML_Registry" = None, DML_InsertInto4: set["DML_Column"] = None):
        self.tableName = tableName
        self.DML_InsertInto = DML_InsertInto
        self.DML_InsertInto2 = DML_InsertInto2
        self.DML_InsertInto4 = DML_InsertInto4 if DML_InsertInto4 is not None else set()
        
    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def DML_InsertInto2(self):
        return self.__DML_InsertInto2

    @DML_InsertInto2.setter
    def DML_InsertInto2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_InsertInto__DML_InsertInto2", None)
        self.__DML_InsertInto2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_Registry"):
                opp_val = getattr(old_value, "DML_Registry", None)
                if opp_val == self:
                    setattr(old_value, "DML_Registry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_Registry"):
                opp_val = getattr(value, "DML_Registry", None)
                setattr(value, "DML_Registry", self)

    @property
    def DML_InsertInto4(self):
        return self.__DML_InsertInto4

    @DML_InsertInto4.setter
    def DML_InsertInto4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_InsertInto__DML_InsertInto4", None)
        self.__DML_InsertInto4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DML_Column"):
                    opp_val = getattr(item, "DML_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "DML_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DML_Column"):
                    opp_val = getattr(item, "DML_Column", None)
                    
                    setattr(item, "DML_Column", self)
                    

    @property
    def DML_InsertInto(self):
        return self.__DML_InsertInto

    @DML_InsertInto.setter
    def DML_InsertInto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DML_InsertInto__DML_InsertInto", None)
        self.__DML_InsertInto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DML_InsertsStatements"):
                opp_val = getattr(old_value, "DML_InsertsStatements", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DML_InsertsStatements"):
                opp_val = getattr(value, "DML_InsertsStatements", None)
                if opp_val is None:
                    setattr(value, "DML_InsertsStatements", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DML_InsertsStatements:

    pass