from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class DDL_DDLDefinition:

    pass
class DDL_CreateFk:

    def __init__(self, columnReference: str, nameFk: str, columnName: str, DDL_CreateFk: "DDL_CreateTable" = None, DDL_CreateFk7: "DDL_CreateTable" = None):
        self.columnReference = columnReference
        self.nameFk = nameFk
        self.columnName = columnName
        self.DDL_CreateFk = DDL_CreateFk
        self.DDL_CreateFk7 = DDL_CreateFk7
        
    @property
    def columnReference(self) -> str:
        return self.__columnReference

    @columnReference.setter
    def columnReference(self, columnReference: str):
        self.__columnReference = columnReference

    @property
    def nameFk(self) -> str:
        return self.__nameFk

    @nameFk.setter
    def nameFk(self, nameFk: str):
        self.__nameFk = nameFk

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def DDL_CreateFk7(self):
        return self.__DDL_CreateFk7

    @DDL_CreateFk7.setter
    def DDL_CreateFk7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_CreateFk__DDL_CreateFk7", None)
        self.__DDL_CreateFk7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_CreateTable6"):
                opp_val = getattr(old_value, "DDL_CreateTable6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_CreateTable6"):
                opp_val = getattr(value, "DDL_CreateTable6", None)
                if opp_val is None:
                    setattr(value, "DDL_CreateTable6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DDL_CreateFk(self):
        return self.__DDL_CreateFk

    @DDL_CreateFk.setter
    def DDL_CreateFk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_CreateFk__DDL_CreateFk", None)
        self.__DDL_CreateFk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_CreateTable"):
                opp_val = getattr(old_value, "DDL_CreateTable", None)
                if opp_val == self:
                    setattr(old_value, "DDL_CreateTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_CreateTable"):
                opp_val = getattr(value, "DDL_CreateTable", None)
                setattr(value, "DDL_CreateTable", self)

class DataDefinition:

    pass
class DDL_CreateCommentColumn(DataDefinition):

    def __init__(self, tableName: str, columnName: str, columnComment: str):
        self.tableName = tableName
        self.columnName = columnName
        self.columnComment = columnComment
        
    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def columnComment(self) -> str:
        return self.__columnComment

    @columnComment.setter
    def columnComment(self, columnComment: str):
        self.__columnComment = columnComment

    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

class DDL_CreateCommentTable(DataDefinition):

    def __init__(self, tableName: str, tableComment: str):
        self.tableName = tableName
        self.tableComment = tableComment
        
    @property
    def tableComment(self) -> str:
        return self.__tableComment

    @tableComment.setter
    def tableComment(self, tableComment: str):
        self.__tableComment = tableComment

    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

class DDL_CreateTable(DataDefinition):

    def __init__(self, tableName: str, commentTable: str, DDL_CreateTable: "DDL_CreateFk" = None, DDL_CreateTable9: set["DDL_CreateCk"] = None, DDL_CreateTable2: set["DDL_CreateColumn"] = None, DDL_CreateTable4: "DDL_CreatePk" = None, DDL_CreateTable6: set["DDL_CreateFk"] = None):
        self.tableName = tableName
        self.commentTable = commentTable
        self.DDL_CreateTable = DDL_CreateTable
        self.DDL_CreateTable9 = DDL_CreateTable9 if DDL_CreateTable9 is not None else set()
        self.DDL_CreateTable2 = DDL_CreateTable2 if DDL_CreateTable2 is not None else set()
        self.DDL_CreateTable4 = DDL_CreateTable4
        self.DDL_CreateTable6 = DDL_CreateTable6 if DDL_CreateTable6 is not None else set()
        
    @property
    def commentTable(self) -> str:
        return self.__commentTable

    @commentTable.setter
    def commentTable(self, commentTable: str):
        self.__commentTable = commentTable

    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def DDL_CreateTable4(self):
        return self.__DDL_CreateTable4

    @DDL_CreateTable4.setter
    def DDL_CreateTable4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_CreateTable__DDL_CreateTable4", None)
        self.__DDL_CreateTable4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_CreatePk"):
                opp_val = getattr(old_value, "DDL_CreatePk", None)
                if opp_val == self:
                    setattr(old_value, "DDL_CreatePk", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_CreatePk"):
                opp_val = getattr(value, "DDL_CreatePk", None)
                setattr(value, "DDL_CreatePk", self)

    @property
    def DDL_CreateTable9(self):
        return self.__DDL_CreateTable9

    @DDL_CreateTable9.setter
    def DDL_CreateTable9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_CreateTable__DDL_CreateTable9", None)
        self.__DDL_CreateTable9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDL_CreateCk"):
                    opp_val = getattr(item, "DDL_CreateCk", None)
                    
                    if opp_val == self:
                        setattr(item, "DDL_CreateCk", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDL_CreateCk"):
                    opp_val = getattr(item, "DDL_CreateCk", None)
                    
                    setattr(item, "DDL_CreateCk", self)
                    

    @property
    def DDL_CreateTable2(self):
        return self.__DDL_CreateTable2

    @DDL_CreateTable2.setter
    def DDL_CreateTable2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_CreateTable__DDL_CreateTable2", None)
        self.__DDL_CreateTable2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDL_CreateColumn"):
                    opp_val = getattr(item, "DDL_CreateColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "DDL_CreateColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDL_CreateColumn"):
                    opp_val = getattr(item, "DDL_CreateColumn", None)
                    
                    setattr(item, "DDL_CreateColumn", self)
                    

    @property
    def DDL_CreateTable(self):
        return self.__DDL_CreateTable

    @DDL_CreateTable.setter
    def DDL_CreateTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_CreateTable__DDL_CreateTable", None)
        self.__DDL_CreateTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_CreateFk"):
                opp_val = getattr(old_value, "DDL_CreateFk", None)
                if opp_val == self:
                    setattr(old_value, "DDL_CreateFk", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_CreateFk"):
                opp_val = getattr(value, "DDL_CreateFk", None)
                setattr(value, "DDL_CreateFk", self)

    @property
    def DDL_CreateTable6(self):
        return self.__DDL_CreateTable6

    @DDL_CreateTable6.setter
    def DDL_CreateTable6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_CreateTable__DDL_CreateTable6", None)
        self.__DDL_CreateTable6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDL_CreateFk7"):
                    opp_val = getattr(item, "DDL_CreateFk7", None)
                    
                    if opp_val == self:
                        setattr(item, "DDL_CreateFk7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDL_CreateFk7"):
                    opp_val = getattr(item, "DDL_CreateFk7", None)
                    
                    setattr(item, "DDL_CreateFk7", self)
                    

class DDL_CreateDatabase(DataDefinition):

    def __init__(self, databaseName: str):
        self.databaseName = databaseName
        
    @property
    def databaseName(self) -> str:
        return self.__databaseName

    @databaseName.setter
    def databaseName(self, databaseName: str):
        self.__databaseName = databaseName

class DDL_CreateColumn:

    def __init__(self, columnName: str, commentColumn: str, columnType: str, columnNull: bool, DDL_CreateColumn: "DDL_CreateTable" = None):
        self.columnName = columnName
        self.commentColumn = commentColumn
        self.columnType = columnType
        self.columnNull = columnNull
        self.DDL_CreateColumn = DDL_CreateColumn
        
    @property
    def columnType(self) -> str:
        return self.__columnType

    @columnType.setter
    def columnType(self, columnType: str):
        self.__columnType = columnType

    @property
    def columnNull(self) -> bool:
        return self.__columnNull

    @columnNull.setter
    def columnNull(self, columnNull: bool):
        self.__columnNull = columnNull

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def commentColumn(self) -> str:
        return self.__commentColumn

    @commentColumn.setter
    def commentColumn(self, commentColumn: str):
        self.__commentColumn = commentColumn

    @property
    def DDL_CreateColumn(self):
        return self.__DDL_CreateColumn

    @DDL_CreateColumn.setter
    def DDL_CreateColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_CreateColumn__DDL_CreateColumn", None)
        self.__DDL_CreateColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_CreateTable2"):
                opp_val = getattr(old_value, "DDL_CreateTable2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_CreateTable2"):
                opp_val = getattr(value, "DDL_CreateTable2", None)
                if opp_val is None:
                    setattr(value, "DDL_CreateTable2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DDL_CreateCk:

    def __init__(self, nameCk: str, valuesCk: str, columnName: str, DDL_CreateCk: "DDL_CreateTable" = None):
        self.nameCk = nameCk
        self.valuesCk = valuesCk
        self.columnName = columnName
        self.DDL_CreateCk = DDL_CreateCk
        
    @property
    def nameCk(self) -> str:
        return self.__nameCk

    @nameCk.setter
    def nameCk(self, nameCk: str):
        self.__nameCk = nameCk

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def valuesCk(self) -> str:
        return self.__valuesCk

    @valuesCk.setter
    def valuesCk(self, valuesCk: str):
        self.__valuesCk = valuesCk

    @property
    def DDL_CreateCk(self):
        return self.__DDL_CreateCk

    @DDL_CreateCk.setter
    def DDL_CreateCk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_CreateCk__DDL_CreateCk", None)
        self.__DDL_CreateCk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_CreateTable9"):
                opp_val = getattr(old_value, "DDL_CreateTable9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_CreateTable9"):
                opp_val = getattr(value, "DDL_CreateTable9", None)
                if opp_val is None:
                    setattr(value, "DDL_CreateTable9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DDL_CreatePk:

    def __init__(self, namePk: str, columnName: str, DDL_CreatePk: "DDL_CreateTable" = None):
        self.namePk = namePk
        self.columnName = columnName
        self.DDL_CreatePk = DDL_CreatePk
        
    @property
    def namePk(self) -> str:
        return self.__namePk

    @namePk.setter
    def namePk(self, namePk: str):
        self.__namePk = namePk

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def DDL_CreatePk(self):
        return self.__DDL_CreatePk

    @DDL_CreatePk.setter
    def DDL_CreatePk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_CreatePk__DDL_CreatePk", None)
        self.__DDL_CreatePk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_CreateTable4"):
                opp_val = getattr(old_value, "DDL_CreateTable4", None)
                if opp_val == self:
                    setattr(old_value, "DDL_CreateTable4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_CreateTable4"):
                opp_val = getattr(value, "DDL_CreateTable4", None)
                setattr(value, "DDL_CreateTable4", self)

class Statement:

    pass
class DDL_DataDefinition(Statement):

    pass
class DDL_Statement:

    pass