from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class database_DatabaseElement(ABC):

    def __init__(self, ID: str, comments: str):
        self.ID = ID
        self.comments = comments
        
    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class AbstractTable:

    pass
class database_Table(AbstractTable):

    pass
class database_View(AbstractTable):

    def __init__(self, query: str):
        self.query = query
        
    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

class database_Type:

    pass
class NamedElement:

    pass
class database_Constraint(NamedElement):

    def __init__(self, expression: str, Constraint: "database_Table" = None, constraints: "database_Table" = None):
        self.expression = expression
        self.Constraint = Constraint
        self.constraints = constraints
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def Constraint(self):
        return self.__Constraint

    @Constraint.setter
    def Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Constraint__Constraint", None)
        self.__Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner26"):
                opp_val = getattr(old_value, "owner26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner26"):
                opp_val = getattr(value, "owner26", None)
                if opp_val is None:
                    setattr(value, "owner26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Constraint__constraints", None)
        self.__constraints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table48"):
                opp_val = getattr(old_value, "Table48", None)
                if opp_val == self:
                    setattr(old_value, "Table48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table48"):
                opp_val = getattr(value, "Table48", None)
                setattr(value, "Table48", self)

class database_Index(NamedElement):

    def __init__(self, qualifier: str, unique: bool, cardinality: int, indexType: str, database_Index: "database_Column" = None, database_Index18: set["database_IndexElement"] = None, indexes: "database_Table" = None, Index: "database_Table" = None):
        self.qualifier = qualifier
        self.unique = unique
        self.cardinality = cardinality
        self.indexType = indexType
        self.database_Index = database_Index
        self.database_Index18 = database_Index18 if database_Index18 is not None else set()
        self.indexes = indexes
        self.Index = Index
        
    @property
    def indexType(self) -> str:
        return self.__indexType

    @indexType.setter
    def indexType(self, indexType: str):
        self.__indexType = indexType

    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def cardinality(self) -> int:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: int):
        self.__cardinality = cardinality

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def Index(self):
        return self.__Index

    @Index.setter
    def Index(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Index__Index", None)
        self.__Index = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner28"):
                opp_val = getattr(old_value, "owner28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner28"):
                opp_val = getattr(value, "owner28", None)
                if opp_val is None:
                    setattr(value, "owner28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def indexes(self):
        return self.__indexes

    @indexes.setter
    def indexes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Index__indexes", None)
        self.__indexes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table"):
                opp_val = getattr(old_value, "Table", None)
                if opp_val == self:
                    setattr(old_value, "Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table"):
                opp_val = getattr(value, "Table", None)
                setattr(value, "Table", self)

    @property
    def database_Index18(self):
        return self.__database_Index18

    @database_Index18.setter
    def database_Index18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Index__database_Index18", None)
        self.__database_Index18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_IndexElement"):
                    opp_val = getattr(item, "database_IndexElement", None)
                    
                    if opp_val == self:
                        setattr(item, "database_IndexElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_IndexElement"):
                    opp_val = getattr(item, "database_IndexElement", None)
                    
                    setattr(item, "database_IndexElement", self)
                    

    @property
    def database_Index(self):
        return self.__database_Index

    @database_Index.setter
    def database_Index(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Index__database_Index", None)
        self.__database_Index = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Column"):
                opp_val = getattr(old_value, "database_Column", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Column"):
                opp_val = getattr(value, "database_Column", None)
                if opp_val is None:
                    setattr(value, "database_Column", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class database_Sequence(NamedElement):

    def __init__(self, start: int, increment: int, minValue: int, maxValue: int, database_Sequence: "database_Column" = None, database_Sequence53: "database_TableContainer" = None):
        self.start = start
        self.increment = increment
        self.minValue = minValue
        self.maxValue = maxValue
        self.database_Sequence = database_Sequence
        self.database_Sequence53 = database_Sequence53
        
    @property
    def increment(self) -> int:
        return self.__increment

    @increment.setter
    def increment(self, increment: int):
        self.__increment = increment

    @property
    def minValue(self) -> int:
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: int):
        self.__minValue = minValue

    @property
    def maxValue(self) -> int:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: int):
        self.__maxValue = maxValue

    @property
    def start(self) -> int:
        return self.__start

    @start.setter
    def start(self, start: int):
        self.__start = start

    @property
    def database_Sequence(self):
        return self.__database_Sequence

    @database_Sequence.setter
    def database_Sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Sequence__database_Sequence", None)
        self.__database_Sequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Column14"):
                opp_val = getattr(old_value, "database_Column14", None)
                if opp_val == self:
                    setattr(old_value, "database_Column14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Column14"):
                opp_val = getattr(value, "database_Column14", None)
                setattr(value, "database_Column14", self)

    @property
    def database_Sequence53(self):
        return self.__database_Sequence53

    @database_Sequence53.setter
    def database_Sequence53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Sequence__database_Sequence53", None)
        self.__database_Sequence53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_TableContainer"):
                opp_val = getattr(old_value, "database_TableContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_TableContainer"):
                opp_val = getattr(value, "database_TableContainer", None)
                if opp_val is None:
                    setattr(value, "database_TableContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class database_ForeignKey(NamedElement):

    def __init__(self, database_ForeignKey: "database_Column" = None, database_ForeignKey35: set["database_ForeignKeyElement"] = None, foreignKeys: "database_Table" = None, database_ForeignKey39: "database_Table" = None, ForeignKey: "database_Table" = None):
        self.database_ForeignKey = database_ForeignKey
        self.database_ForeignKey35 = database_ForeignKey35 if database_ForeignKey35 is not None else set()
        self.foreignKeys = foreignKeys
        self.database_ForeignKey39 = database_ForeignKey39
        self.ForeignKey = ForeignKey
        
    @property
    def ForeignKey(self):
        return self.__ForeignKey

    @ForeignKey.setter
    def ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__ForeignKey", None)
        self.__ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner24"):
                opp_val = getattr(old_value, "owner24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner24"):
                opp_val = getattr(value, "owner24", None)
                if opp_val is None:
                    setattr(value, "owner24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_ForeignKey(self):
        return self.__database_ForeignKey

    @database_ForeignKey.setter
    def database_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__database_ForeignKey", None)
        self.__database_ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Column9"):
                opp_val = getattr(old_value, "database_Column9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Column9"):
                opp_val = getattr(value, "database_Column9", None)
                if opp_val is None:
                    setattr(value, "database_Column9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_ForeignKey35(self):
        return self.__database_ForeignKey35

    @database_ForeignKey35.setter
    def database_ForeignKey35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__database_ForeignKey35", None)
        self.__database_ForeignKey35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_ForeignKeyElement"):
                    opp_val = getattr(item, "database_ForeignKeyElement", None)
                    
                    if opp_val == self:
                        setattr(item, "database_ForeignKeyElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_ForeignKeyElement"):
                    opp_val = getattr(item, "database_ForeignKeyElement", None)
                    
                    setattr(item, "database_ForeignKeyElement", self)
                    

    @property
    def database_ForeignKey39(self):
        return self.__database_ForeignKey39

    @database_ForeignKey39.setter
    def database_ForeignKey39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__database_ForeignKey39", None)
        self.__database_ForeignKey39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Table"):
                opp_val = getattr(old_value, "database_Table", None)
                if opp_val == self:
                    setattr(old_value, "database_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Table"):
                opp_val = getattr(value, "database_Table", None)
                setattr(value, "database_Table", self)

    @property
    def foreignKeys(self):
        return self.__foreignKeys

    @foreignKeys.setter
    def foreignKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__foreignKeys", None)
        self.__foreignKeys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table37"):
                opp_val = getattr(old_value, "Table37", None)
                if opp_val == self:
                    setattr(old_value, "Table37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table37"):
                opp_val = getattr(value, "Table37", None)
                setattr(value, "Table37", self)

    def getSourceTable(self) -> str:
        # TODO: Implement getSourceTable method
        pass

    def getTargetTable(self) -> str:
        # TODO: Implement getTargetTable method
        pass

class database_PrimaryKey(NamedElement):

    pass
class database_AbstractTable(NamedElement):

    pass
class database_UserDefinedTypesLibrary:

    pass
class TypesLibraryUser:

    pass
class TableContainer:

    pass
class database_Schema(TableContainer):

    pass
class database_DataBase(TableContainer, TypesLibraryUser):

    def __init__(self, url: str, database_DataBase: set["database_Schema"] = None, database_DataBase2: set["database_UserDefinedTypesLibrary"] = None):
        self.url = url
        self.database_DataBase = database_DataBase if database_DataBase is not None else set()
        self.database_DataBase2 = database_DataBase2 if database_DataBase2 is not None else set()
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def database_DataBase2(self):
        return self.__database_DataBase2

    @database_DataBase2.setter
    def database_DataBase2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_DataBase__database_DataBase2", None)
        self.__database_DataBase2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_UserDefinedTypesLibrary"):
                    opp_val = getattr(item, "database_UserDefinedTypesLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "database_UserDefinedTypesLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_UserDefinedTypesLibrary"):
                    opp_val = getattr(item, "database_UserDefinedTypesLibrary", None)
                    
                    setattr(item, "database_UserDefinedTypesLibrary", self)
                    

    @property
    def database_DataBase(self):
        return self.__database_DataBase

    @database_DataBase.setter
    def database_DataBase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_DataBase__database_DataBase", None)
        self.__database_DataBase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_Schema"):
                    opp_val = getattr(item, "database_Schema", None)
                    
                    if opp_val == self:
                        setattr(item, "database_Schema", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_Schema"):
                    opp_val = getattr(item, "database_Schema", None)
                    
                    setattr(item, "database_Schema", self)
                    

class DatabaseElement:

    pass
class database_IndexElement(DatabaseElement):

    def __init__(self, asc: bool, IndexElement: "database_Column" = None, database_IndexElement: "database_Index" = None, indexElements: "database_Column" = None):
        self.asc = asc
        self.IndexElement = IndexElement
        self.database_IndexElement = database_IndexElement
        self.indexElements = indexElements
        
    @property
    def asc(self) -> bool:
        return self.__asc

    @asc.setter
    def asc(self, asc: bool):
        self.__asc = asc

    @property
    def indexElements(self):
        return self.__indexElements

    @indexElements.setter
    def indexElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_IndexElement__indexElements", None)
        self.__indexElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Column46"):
                opp_val = getattr(old_value, "Column46", None)
                if opp_val == self:
                    setattr(old_value, "Column46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Column46"):
                opp_val = getattr(value, "Column46", None)
                setattr(value, "Column46", self)

    @property
    def IndexElement(self):
        return self.__IndexElement

    @IndexElement.setter
    def IndexElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_IndexElement__IndexElement", None)
        self.__IndexElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "column"):
                opp_val = getattr(old_value, "column", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "column"):
                opp_val = getattr(value, "column", None)
                if opp_val is None:
                    setattr(value, "column", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_IndexElement(self):
        return self.__database_IndexElement

    @database_IndexElement.setter
    def database_IndexElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_IndexElement__database_IndexElement", None)
        self.__database_IndexElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Index18"):
                opp_val = getattr(old_value, "database_Index18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Index18"):
                opp_val = getattr(value, "database_Index18", None)
                if opp_val is None:
                    setattr(value, "database_Index18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class database_ForeignKeyElement(DatabaseElement):

    pass
class database_NamedElement(DatabaseElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class database_TableContainer(NamedElement):

    pass
class database_Column(NamedElement):

    def __init__(self, nullable: bool, defaultValue: str, autoincrement: bool, inPrimaryKey: bool, inForeignKey: bool, unique: bool, Column: "database_AbstractTable" = None, database_Column12: "database_Type" = None, database_Column14: "database_Sequence" = None, database_Column: set["database_Index"] = None, column: set["database_IndexElement"] = None, columns: "database_PrimaryKey" = None, database_Column9: set["database_ForeignKey"] = None, fkColumn: set["database_ForeignKeyElement"] = None, columns16: "database_AbstractTable" = None, Column30: "database_PrimaryKey" = None, Column41: "database_ForeignKeyElement" = None, database_Column44: "database_ForeignKeyElement" = None, Column46: "database_IndexElement" = None):
        self.nullable = nullable
        self.defaultValue = defaultValue
        self.autoincrement = autoincrement
        self.inPrimaryKey = inPrimaryKey
        self.inForeignKey = inForeignKey
        self.unique = unique
        self.Column = Column
        self.database_Column12 = database_Column12
        self.database_Column14 = database_Column14
        self.database_Column = database_Column if database_Column is not None else set()
        self.column = column if column is not None else set()
        self.columns = columns
        self.database_Column9 = database_Column9 if database_Column9 is not None else set()
        self.fkColumn = fkColumn if fkColumn is not None else set()
        self.columns16 = columns16
        self.Column30 = Column30
        self.Column41 = Column41
        self.database_Column44 = database_Column44
        self.Column46 = Column46
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def autoincrement(self) -> bool:
        return self.__autoincrement

    @autoincrement.setter
    def autoincrement(self, autoincrement: bool):
        self.__autoincrement = autoincrement

    @property
    def inForeignKey(self) -> bool:
        return self.__inForeignKey

    @inForeignKey.setter
    def inForeignKey(self, inForeignKey: bool):
        self.__inForeignKey = inForeignKey

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def inPrimaryKey(self) -> bool:
        return self.__inPrimaryKey

    @inPrimaryKey.setter
    def inPrimaryKey(self, inPrimaryKey: bool):
        self.__inPrimaryKey = inPrimaryKey

    @property
    def Column46(self):
        return self.__Column46

    @Column46.setter
    def Column46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__Column46", None)
        self.__Column46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "indexElements"):
                opp_val = getattr(old_value, "indexElements", None)
                if opp_val == self:
                    setattr(old_value, "indexElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "indexElements"):
                opp_val = getattr(value, "indexElements", None)
                setattr(value, "indexElements", self)

    @property
    def Column30(self):
        return self.__Column30

    @Column30.setter
    def Column30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__Column30", None)
        self.__Column30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "primaryKey"):
                opp_val = getattr(old_value, "primaryKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "primaryKey"):
                opp_val = getattr(value, "primaryKey", None)
                if opp_val is None:
                    setattr(value, "primaryKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_Column14(self):
        return self.__database_Column14

    @database_Column14.setter
    def database_Column14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column14", None)
        self.__database_Column14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Sequence"):
                opp_val = getattr(old_value, "database_Sequence", None)
                if opp_val == self:
                    setattr(old_value, "database_Sequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Sequence"):
                opp_val = getattr(value, "database_Sequence", None)
                setattr(value, "database_Sequence", self)

    @property
    def database_Column9(self):
        return self.__database_Column9

    @database_Column9.setter
    def database_Column9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column9", None)
        self.__database_Column9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_ForeignKey"):
                    opp_val = getattr(item, "database_ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "database_ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_ForeignKey"):
                    opp_val = getattr(item, "database_ForeignKey", None)
                    
                    setattr(item, "database_ForeignKey", self)
                    

    @property
    def columns16(self):
        return self.__columns16

    @columns16.setter
    def columns16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__columns16", None)
        self.__columns16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractTable"):
                opp_val = getattr(old_value, "AbstractTable", None)
                if opp_val == self:
                    setattr(old_value, "AbstractTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractTable"):
                opp_val = getattr(value, "AbstractTable", None)
                setattr(value, "AbstractTable", self)

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__columns", None)
        self.__columns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimaryKey"):
                opp_val = getattr(old_value, "PrimaryKey", None)
                if opp_val == self:
                    setattr(old_value, "PrimaryKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimaryKey"):
                opp_val = getattr(value, "PrimaryKey", None)
                setattr(value, "PrimaryKey", self)

    @property
    def database_Column(self):
        return self.__database_Column

    @database_Column.setter
    def database_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column", None)
        self.__database_Column = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_Index"):
                    opp_val = getattr(item, "database_Index", None)
                    
                    if opp_val == self:
                        setattr(item, "database_Index", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_Index"):
                    opp_val = getattr(item, "database_Index", None)
                    
                    setattr(item, "database_Index", self)
                    

    @property
    def fkColumn(self):
        return self.__fkColumn

    @fkColumn.setter
    def fkColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__fkColumn", None)
        self.__fkColumn = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKeyElement"):
                    opp_val = getattr(item, "ForeignKeyElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKeyElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKeyElement"):
                    opp_val = getattr(item, "ForeignKeyElement", None)
                    
                    setattr(item, "ForeignKeyElement", self)
                    

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__column", None)
        self.__column = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IndexElement"):
                    opp_val = getattr(item, "IndexElement", None)
                    
                    if opp_val == self:
                        setattr(item, "IndexElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IndexElement"):
                    opp_val = getattr(item, "IndexElement", None)
                    
                    setattr(item, "IndexElement", self)
                    

    @property
    def database_Column44(self):
        return self.__database_Column44

    @database_Column44.setter
    def database_Column44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column44", None)
        self.__database_Column44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_ForeignKeyElement43"):
                opp_val = getattr(old_value, "database_ForeignKeyElement43", None)
                if opp_val == self:
                    setattr(old_value, "database_ForeignKeyElement43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_ForeignKeyElement43"):
                opp_val = getattr(value, "database_ForeignKeyElement43", None)
                setattr(value, "database_ForeignKeyElement43", self)

    @property
    def database_Column12(self):
        return self.__database_Column12

    @database_Column12.setter
    def database_Column12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column12", None)
        self.__database_Column12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Type"):
                opp_val = getattr(old_value, "database_Type", None)
                if opp_val == self:
                    setattr(old_value, "database_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Type"):
                opp_val = getattr(value, "database_Type", None)
                setattr(value, "database_Type", self)

    @property
    def Column41(self):
        return self.__Column41

    @Column41.setter
    def Column41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__Column41", None)
        self.__Column41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foreignKeyElements"):
                opp_val = getattr(old_value, "foreignKeyElements", None)
                if opp_val == self:
                    setattr(old_value, "foreignKeyElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foreignKeyElements"):
                opp_val = getattr(value, "foreignKeyElements", None)
                setattr(value, "foreignKeyElements", self)

    def addToUniqueIndex(self):
        # TODO: Implement addToUniqueIndex method
        pass

    def removeFromUniqueIndex(self):
        # TODO: Implement removeFromUniqueIndex method
        pass

    def addToPrimaryKey(self):
        # TODO: Implement addToPrimaryKey method
        pass

    def removeFromPrimaryKey(self):
        # TODO: Implement removeFromPrimaryKey method
        pass
