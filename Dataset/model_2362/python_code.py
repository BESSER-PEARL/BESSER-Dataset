from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class database_DatabaseElement(ABC):

    def __init__(self, ID: str, comments: str, techID: str):
        self.ID = ID
        self.comments = comments
        self.techID = techID
        
    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def techID(self) -> str:
        return self.__techID

    @techID.setter
    def techID(self, techID: str):
        self.__techID = techID

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class database_ViewElement:

    def __init__(self, name: str, alias: str, database_ViewElement: "database_View" = None, database_ViewElement23: "database_View" = None):
        self.name = name
        self.alias = alias
        self.database_ViewElement = database_ViewElement
        self.database_ViewElement23 = database_ViewElement23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def database_ViewElement23(self):
        return self.__database_ViewElement23

    @database_ViewElement23.setter
    def database_ViewElement23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ViewElement__database_ViewElement23", None)
        self.__database_ViewElement23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_View22"):
                opp_val = getattr(old_value, "database_View22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_View22"):
                opp_val = getattr(value, "database_View22", None)
                if opp_val is None:
                    setattr(value, "database_View22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_ViewElement(self):
        return self.__database_ViewElement

    @database_ViewElement.setter
    def database_ViewElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ViewElement__database_ViewElement", None)
        self.__database_ViewElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_View"):
                opp_val = getattr(old_value, "database_View", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_View"):
                opp_val = getattr(value, "database_View", None)
                if opp_val is None:
                    setattr(value, "database_View", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractTable:

    pass
class database_View(AbstractTable):

    def __init__(self, query: str, database_View: set["database_ViewElement"] = None, database_View22: set["database_ViewElement"] = None):
        self.query = query
        self.database_View = database_View if database_View is not None else set()
        self.database_View22 = database_View22 if database_View22 is not None else set()
        
    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

    @property
    def database_View22(self):
        return self.__database_View22

    @database_View22.setter
    def database_View22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_View__database_View22", None)
        self.__database_View22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_ViewElement23"):
                    opp_val = getattr(item, "database_ViewElement23", None)
                    
                    if opp_val == self:
                        setattr(item, "database_ViewElement23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_ViewElement23"):
                    opp_val = getattr(item, "database_ViewElement23", None)
                    
                    setattr(item, "database_ViewElement23", self)
                    

    @property
    def database_View(self):
        return self.__database_View

    @database_View.setter
    def database_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_View__database_View", None)
        self.__database_View = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_ViewElement"):
                    opp_val = getattr(item, "database_ViewElement", None)
                    
                    if opp_val == self:
                        setattr(item, "database_ViewElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_ViewElement"):
                    opp_val = getattr(item, "database_ViewElement", None)
                    
                    setattr(item, "database_ViewElement", self)
                    

class database_Table(AbstractTable):

    pass
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
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Constraint__constraints", None)
        self.__constraints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table53"):
                opp_val = getattr(old_value, "Table53", None)
                if opp_val == self:
                    setattr(old_value, "Table53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table53"):
                opp_val = getattr(value, "Table53", None)
                setattr(value, "Table53", self)

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
            if hasattr(old_value, "owner29"):
                opp_val = getattr(old_value, "owner29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner29"):
                opp_val = getattr(value, "owner29", None)
                if opp_val is None:
                    setattr(value, "owner29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class database_Index(NamedElement):

    def __init__(self, qualifier: str, unique: bool, cardinality: int, indexType: str, database_Index: "database_Column" = None, database_Index17: set["database_IndexElement"] = None, Index: "database_Table" = None, indexes: "database_Table" = None):
        self.qualifier = qualifier
        self.unique = unique
        self.cardinality = cardinality
        self.indexType = indexType
        self.database_Index = database_Index
        self.database_Index17 = database_Index17 if database_Index17 is not None else set()
        self.Index = Index
        self.indexes = indexes
        
    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def indexType(self) -> str:
        return self.__indexType

    @indexType.setter
    def indexType(self, indexType: str):
        self.__indexType = indexType

    @property
    def cardinality(self) -> int:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: int):
        self.__cardinality = cardinality

    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def database_Index17(self):
        return self.__database_Index17

    @database_Index17.setter
    def database_Index17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Index__database_Index17", None)
        self.__database_Index17 = value if value is not None else set()
        
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
    def indexes(self):
        return self.__indexes

    @indexes.setter
    def indexes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Index__indexes", None)
        self.__indexes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table19"):
                opp_val = getattr(old_value, "Table19", None)
                if opp_val == self:
                    setattr(old_value, "Table19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table19"):
                opp_val = getattr(value, "Table19", None)
                setattr(value, "Table19", self)

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
            if hasattr(old_value, "owner31"):
                opp_val = getattr(old_value, "owner31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner31"):
                opp_val = getattr(value, "owner31", None)
                if opp_val is None:
                    setattr(value, "owner31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class database_Column(NamedElement):

    def __init__(self, nullable: bool, defaultValue: str, autoincrement: bool, inPrimaryKey: bool, inForeignKey: bool, unique: bool, column: set["database_IndexElement"] = None, columns: "database_PrimaryKey" = None, database_Column: set["database_Index"] = None, database_Column8: set["database_ForeignKey"] = None, fkColumn: set["database_ForeignKeyElement"] = None, database_Column11: "database_Type" = None, columns13: "database_Sequence" = None, columns15: "database_Table" = None, Column: "database_Table" = None, Column46: "database_ForeignKeyElement" = None, database_Column49: "database_ForeignKeyElement" = None, Column35: "database_PrimaryKey" = None, Column55: "database_Sequence" = None, Column51: "database_IndexElement" = None):
        self.nullable = nullable
        self.defaultValue = defaultValue
        self.autoincrement = autoincrement
        self.inPrimaryKey = inPrimaryKey
        self.inForeignKey = inForeignKey
        self.unique = unique
        self.column = column if column is not None else set()
        self.columns = columns
        self.database_Column = database_Column if database_Column is not None else set()
        self.database_Column8 = database_Column8 if database_Column8 is not None else set()
        self.fkColumn = fkColumn if fkColumn is not None else set()
        self.database_Column11 = database_Column11
        self.columns13 = columns13
        self.columns15 = columns15
        self.Column = Column
        self.Column46 = Column46
        self.database_Column49 = database_Column49
        self.Column35 = Column35
        self.Column55 = Column55
        self.Column51 = Column51
        
    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def autoincrement(self) -> bool:
        return self.__autoincrement

    @autoincrement.setter
    def autoincrement(self, autoincrement: bool):
        self.__autoincrement = autoincrement

    @property
    def inPrimaryKey(self) -> bool:
        return self.__inPrimaryKey

    @inPrimaryKey.setter
    def inPrimaryKey(self, inPrimaryKey: bool):
        self.__inPrimaryKey = inPrimaryKey

    @property
    def inForeignKey(self) -> bool:
        return self.__inForeignKey

    @inForeignKey.setter
    def inForeignKey(self, inForeignKey: bool):
        self.__inForeignKey = inForeignKey

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def database_Column11(self):
        return self.__database_Column11

    @database_Column11.setter
    def database_Column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column11", None)
        self.__database_Column11 = value
        
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
    def columns15(self):
        return self.__columns15

    @columns15.setter
    def columns15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__columns15", None)
        self.__columns15 = value
        
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
    def Column46(self):
        return self.__Column46

    @Column46.setter
    def Column46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__Column46", None)
        self.__Column46 = value
        
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
            if hasattr(old_value, "owner33"):
                opp_val = getattr(old_value, "owner33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner33"):
                opp_val = getattr(value, "owner33", None)
                if opp_val is None:
                    setattr(value, "owner33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def Column55(self):
        return self.__Column55

    @Column55.setter
    def Column55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__Column55", None)
        self.__Column55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sequence"):
                opp_val = getattr(old_value, "sequence", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sequence"):
                opp_val = getattr(value, "sequence", None)
                if opp_val is None:
                    setattr(value, "sequence", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column35(self):
        return self.__Column35

    @Column35.setter
    def Column35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__Column35", None)
        self.__Column35 = value
        
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
    def database_Column8(self):
        return self.__database_Column8

    @database_Column8.setter
    def database_Column8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column8", None)
        self.__database_Column8 = value if value is not None else set()
        
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
    def columns13(self):
        return self.__columns13

    @columns13.setter
    def columns13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__columns13", None)
        self.__columns13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sequence"):
                opp_val = getattr(old_value, "Sequence", None)
                if opp_val == self:
                    setattr(old_value, "Sequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sequence"):
                opp_val = getattr(value, "Sequence", None)
                setattr(value, "Sequence", self)

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
    def Column51(self):
        return self.__Column51

    @Column51.setter
    def Column51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__Column51", None)
        self.__Column51 = value
        
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
    def database_Column49(self):
        return self.__database_Column49

    @database_Column49.setter
    def database_Column49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column49", None)
        self.__database_Column49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_ForeignKeyElement48"):
                opp_val = getattr(old_value, "database_ForeignKeyElement48", None)
                if opp_val == self:
                    setattr(old_value, "database_ForeignKeyElement48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_ForeignKeyElement48"):
                opp_val = getattr(value, "database_ForeignKeyElement48", None)
                setattr(value, "database_ForeignKeyElement48", self)

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
                    

    def addToPrimaryKey(self):
        # TODO: Implement addToPrimaryKey method
        pass

    def removeFromPrimaryKey(self):
        # TODO: Implement removeFromPrimaryKey method
        pass

    def removeFromUniqueIndex(self):
        # TODO: Implement removeFromUniqueIndex method
        pass

    def addToUniqueIndex(self):
        # TODO: Implement addToUniqueIndex method
        pass

class database_Sequence(NamedElement):

    def __init__(self, minValue: str, maxValue: str, cacheSize: str, cycle: bool, start: str, increment: str, Sequence: "database_Column" = None, sequence: set["database_Column"] = None, database_Sequence: "database_TableContainer" = None):
        self.minValue = minValue
        self.maxValue = maxValue
        self.cacheSize = cacheSize
        self.cycle = cycle
        self.start = start
        self.increment = increment
        self.Sequence = Sequence
        self.sequence = sequence if sequence is not None else set()
        self.database_Sequence = database_Sequence
        
    @property
    def cacheSize(self) -> str:
        return self.__cacheSize

    @cacheSize.setter
    def cacheSize(self, cacheSize: str):
        self.__cacheSize = cacheSize

    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def maxValue(self) -> str:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: str):
        self.__maxValue = maxValue

    @property
    def minValue(self) -> str:
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: str):
        self.__minValue = minValue

    @property
    def cycle(self) -> bool:
        return self.__cycle

    @cycle.setter
    def cycle(self, cycle: bool):
        self.__cycle = cycle

    @property
    def increment(self) -> str:
        return self.__increment

    @increment.setter
    def increment(self, increment: str):
        self.__increment = increment

    @property
    def Sequence(self):
        return self.__Sequence

    @Sequence.setter
    def Sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Sequence__Sequence", None)
        self.__Sequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columns13"):
                opp_val = getattr(old_value, "columns13", None)
                if opp_val == self:
                    setattr(old_value, "columns13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columns13"):
                opp_val = getattr(value, "columns13", None)
                setattr(value, "columns13", self)

    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Sequence__sequence", None)
        self.__sequence = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column55"):
                    opp_val = getattr(item, "Column55", None)
                    
                    if opp_val == self:
                        setattr(item, "Column55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column55"):
                    opp_val = getattr(item, "Column55", None)
                    
                    setattr(item, "Column55", self)
                    

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

class database_TableContainer(NamedElement):

    pass
class database_AbstractTable(NamedElement):

    pass
class database_UserDefinedTypesLibrary:

    pass
class database_ForeignKey(NamedElement):

    def __init__(self, database_ForeignKey: "database_Column" = None, ForeignKey: "database_Table" = None, database_ForeignKey40: set["database_ForeignKeyElement"] = None, foreignKeys: "database_Table" = None, database_ForeignKey44: "database_Table" = None):
        self.database_ForeignKey = database_ForeignKey
        self.ForeignKey = ForeignKey
        self.database_ForeignKey40 = database_ForeignKey40 if database_ForeignKey40 is not None else set()
        self.foreignKeys = foreignKeys
        self.database_ForeignKey44 = database_ForeignKey44
        
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
            if hasattr(old_value, "database_Column8"):
                opp_val = getattr(old_value, "database_Column8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Column8"):
                opp_val = getattr(value, "database_Column8", None)
                if opp_val is None:
                    setattr(value, "database_Column8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "owner27"):
                opp_val = getattr(old_value, "owner27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner27"):
                opp_val = getattr(value, "owner27", None)
                if opp_val is None:
                    setattr(value, "owner27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Table42"):
                opp_val = getattr(old_value, "Table42", None)
                if opp_val == self:
                    setattr(old_value, "Table42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table42"):
                opp_val = getattr(value, "Table42", None)
                setattr(value, "Table42", self)

    @property
    def database_ForeignKey44(self):
        return self.__database_ForeignKey44

    @database_ForeignKey44.setter
    def database_ForeignKey44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__database_ForeignKey44", None)
        self.__database_ForeignKey44 = value
        
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
    def database_ForeignKey40(self):
        return self.__database_ForeignKey40

    @database_ForeignKey40.setter
    def database_ForeignKey40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__database_ForeignKey40", None)
        self.__database_ForeignKey40 = value if value is not None else set()
        
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
                    

    def getSourceTable(self) -> str:
        # TODO: Implement getSourceTable method
        pass

    def getTargetTable(self) -> str:
        # TODO: Implement getTargetTable method
        pass

class database_PrimaryKey(NamedElement):

    pass
class TableContainer:

    pass
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
    def database_IndexElement(self):
        return self.__database_IndexElement

    @database_IndexElement.setter
    def database_IndexElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_IndexElement__database_IndexElement", None)
        self.__database_IndexElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Index17"):
                opp_val = getattr(old_value, "database_Index17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Index17"):
                opp_val = getattr(value, "database_Index17", None)
                if opp_val is None:
                    setattr(value, "database_Index17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def indexElements(self):
        return self.__indexElements

    @indexElements.setter
    def indexElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_IndexElement__indexElements", None)
        self.__indexElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Column51"):
                opp_val = getattr(old_value, "Column51", None)
                if opp_val == self:
                    setattr(old_value, "Column51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Column51"):
                opp_val = getattr(value, "Column51", None)
                setattr(value, "Column51", self)

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

class database_Schema(TableContainer):

    pass
class TypesLibraryUser:

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
                    
