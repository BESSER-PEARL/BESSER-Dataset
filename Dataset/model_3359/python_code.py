from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConstraintType(Enum):
    FOREIGN_KEY = "FOREIGN_KEY"
    UNIQUE = "UNIQUE"
    COMPOSITE_PRIMARY_KEY = "COMPOSITE_PRIMARY_KEY"
    PRIMARY_KEY = "PRIMARY_KEY"
class Datatype(Enum):
    STRING = "STRING"
    DATE = "DATE"
    FLOAT = "FLOAT"
    TIMESTAMP = "TIMESTAMP"
    TEXT = "TEXT"
    DECIMAL = "DECIMAL"
    INT = "INT"
    DOUBLE = "DOUBLE"
    BOOLEAN = "BOOLEAN"
    DATETIME = "DATETIME"
    VARCHAR = "VARCHAR"
    CHAR = "CHAR"
    TINYTEXT = "TINYTEXT"
    BLOB = "BLOB"
    LONGTEXT = "LONGTEXT"
    SMALLINT = "SMALLINT"
    BIGINT = "BIGINT"


############################################
# Definition of Classes
############################################

class metamodel_Cell:

    def __init__(self, value: str, metamodel_Cell: "metamodel_Row" = None, metamodel_Cell18: "metamodel_Column" = None):
        self.value = value
        self.metamodel_Cell = metamodel_Cell
        self.metamodel_Cell18 = metamodel_Cell18
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def metamodel_Cell18(self):
        return self.__metamodel_Cell18

    @metamodel_Cell18.setter
    def metamodel_Cell18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Cell__metamodel_Cell18", None)
        self.__metamodel_Cell18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Column19"):
                opp_val = getattr(old_value, "metamodel_Column19", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Column19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Column19"):
                opp_val = getattr(value, "metamodel_Column19", None)
                setattr(value, "metamodel_Column19", self)

    @property
    def metamodel_Cell(self):
        return self.__metamodel_Cell

    @metamodel_Cell.setter
    def metamodel_Cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Cell__metamodel_Cell", None)
        self.__metamodel_Cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Row16"):
                opp_val = getattr(old_value, "metamodel_Row16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Row16"):
                opp_val = getattr(value, "metamodel_Row16", None)
                if opp_val is None:
                    setattr(value, "metamodel_Row16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_Row:

    pass
class metamodel_Column:

    def __init__(self, name: str, type: str, nullable: bool, size: str, metamodel_Column: "metamodel_Table" = None, metamodel_Column11: "metamodel_Constraint" = None, metamodel_Column13: set["metamodel_Constraint"] = None, metamodel_Column19: "metamodel_Cell" = None):
        self.name = name
        self.type = type
        self.nullable = nullable
        self.size = size
        self.metamodel_Column = metamodel_Column
        self.metamodel_Column11 = metamodel_Column11
        self.metamodel_Column13 = metamodel_Column13 if metamodel_Column13 is not None else set()
        self.metamodel_Column19 = metamodel_Column19
        
    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def metamodel_Column11(self):
        return self.__metamodel_Column11

    @metamodel_Column11.setter
    def metamodel_Column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Column__metamodel_Column11", None)
        self.__metamodel_Column11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Constraint10"):
                opp_val = getattr(old_value, "metamodel_Constraint10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Constraint10"):
                opp_val = getattr(value, "metamodel_Constraint10", None)
                if opp_val is None:
                    setattr(value, "metamodel_Constraint10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_Column13(self):
        return self.__metamodel_Column13

    @metamodel_Column13.setter
    def metamodel_Column13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Column__metamodel_Column13", None)
        self.__metamodel_Column13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Constraint14"):
                    opp_val = getattr(item, "metamodel_Constraint14", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Constraint14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Constraint14"):
                    opp_val = getattr(item, "metamodel_Constraint14", None)
                    
                    setattr(item, "metamodel_Constraint14", self)
                    

    @property
    def metamodel_Column19(self):
        return self.__metamodel_Column19

    @metamodel_Column19.setter
    def metamodel_Column19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Column__metamodel_Column19", None)
        self.__metamodel_Column19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Cell18"):
                opp_val = getattr(old_value, "metamodel_Cell18", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Cell18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Cell18"):
                opp_val = getattr(value, "metamodel_Cell18", None)
                setattr(value, "metamodel_Cell18", self)

    @property
    def metamodel_Column(self):
        return self.__metamodel_Column

    @metamodel_Column.setter
    def metamodel_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Column__metamodel_Column", None)
        self.__metamodel_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Table6"):
                opp_val = getattr(old_value, "metamodel_Table6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Table6"):
                opp_val = getattr(value, "metamodel_Table6", None)
                if opp_val is None:
                    setattr(value, "metamodel_Table6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_Sequence:

    def __init__(self, name: str, minValue: int, maxValue: str, incrementby: int, startwith: str, currentValue: str, cycle: bool, metamodel_Sequence: "metamodel_Database" = None):
        self.name = name
        self.minValue = minValue
        self.maxValue = maxValue
        self.incrementby = incrementby
        self.startwith = startwith
        self.currentValue = currentValue
        self.cycle = cycle
        self.metamodel_Sequence = metamodel_Sequence
        
    @property
    def maxValue(self) -> str:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: str):
        self.__maxValue = maxValue

    @property
    def startwith(self) -> str:
        return self.__startwith

    @startwith.setter
    def startwith(self, startwith: str):
        self.__startwith = startwith

    @property
    def incrementby(self) -> int:
        return self.__incrementby

    @incrementby.setter
    def incrementby(self, incrementby: int):
        self.__incrementby = incrementby

    @property
    def cycle(self) -> bool:
        return self.__cycle

    @cycle.setter
    def cycle(self, cycle: bool):
        self.__cycle = cycle

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minValue(self) -> int:
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: int):
        self.__minValue = minValue

    @property
    def currentValue(self) -> str:
        return self.__currentValue

    @currentValue.setter
    def currentValue(self, currentValue: str):
        self.__currentValue = currentValue

    @property
    def metamodel_Sequence(self):
        return self.__metamodel_Sequence

    @metamodel_Sequence.setter
    def metamodel_Sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Sequence__metamodel_Sequence", None)
        self.__metamodel_Sequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Database2"):
                opp_val = getattr(old_value, "metamodel_Database2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Database2"):
                opp_val = getattr(value, "metamodel_Database2", None)
                if opp_val is None:
                    setattr(value, "metamodel_Database2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_Table:

    def __init__(self, name: str, metamodel_Table4: set["metamodel_Constraint"] = None, metamodel_Table: "metamodel_Database" = None, metamodel_Table6: set["metamodel_Column"] = None, metamodel_Table8: set["metamodel_Row"] = None):
        self.name = name
        self.metamodel_Table4 = metamodel_Table4 if metamodel_Table4 is not None else set()
        self.metamodel_Table = metamodel_Table
        self.metamodel_Table6 = metamodel_Table6 if metamodel_Table6 is not None else set()
        self.metamodel_Table8 = metamodel_Table8 if metamodel_Table8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Table8(self):
        return self.__metamodel_Table8

    @metamodel_Table8.setter
    def metamodel_Table8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Table__metamodel_Table8", None)
        self.__metamodel_Table8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Row"):
                    opp_val = getattr(item, "metamodel_Row", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Row", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Row"):
                    opp_val = getattr(item, "metamodel_Row", None)
                    
                    setattr(item, "metamodel_Row", self)
                    

    @property
    def metamodel_Table6(self):
        return self.__metamodel_Table6

    @metamodel_Table6.setter
    def metamodel_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Table__metamodel_Table6", None)
        self.__metamodel_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Column"):
                    opp_val = getattr(item, "metamodel_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Column"):
                    opp_val = getattr(item, "metamodel_Column", None)
                    
                    setattr(item, "metamodel_Column", self)
                    

    @property
    def metamodel_Table4(self):
        return self.__metamodel_Table4

    @metamodel_Table4.setter
    def metamodel_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Table__metamodel_Table4", None)
        self.__metamodel_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Constraint"):
                    opp_val = getattr(item, "metamodel_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Constraint"):
                    opp_val = getattr(item, "metamodel_Constraint", None)
                    
                    setattr(item, "metamodel_Constraint", self)
                    

    @property
    def metamodel_Table(self):
        return self.__metamodel_Table

    @metamodel_Table.setter
    def metamodel_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Table__metamodel_Table", None)
        self.__metamodel_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Database"):
                opp_val = getattr(old_value, "metamodel_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Database"):
                opp_val = getattr(value, "metamodel_Database", None)
                if opp_val is None:
                    setattr(value, "metamodel_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_Database:

    def __init__(self, name: str, metamodel_Database: set["metamodel_Table"] = None, metamodel_Database2: set["metamodel_Sequence"] = None):
        self.name = name
        self.metamodel_Database = metamodel_Database if metamodel_Database is not None else set()
        self.metamodel_Database2 = metamodel_Database2 if metamodel_Database2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Database2(self):
        return self.__metamodel_Database2

    @metamodel_Database2.setter
    def metamodel_Database2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Database__metamodel_Database2", None)
        self.__metamodel_Database2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Sequence"):
                    opp_val = getattr(item, "metamodel_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Sequence"):
                    opp_val = getattr(item, "metamodel_Sequence", None)
                    
                    setattr(item, "metamodel_Sequence", self)
                    

    @property
    def metamodel_Database(self):
        return self.__metamodel_Database

    @metamodel_Database.setter
    def metamodel_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Database__metamodel_Database", None)
        self.__metamodel_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Table"):
                    opp_val = getattr(item, "metamodel_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Table"):
                    opp_val = getattr(item, "metamodel_Table", None)
                    
                    setattr(item, "metamodel_Table", self)
                    

class metamodel_Constraint:

    def __init__(self, name: str, type: str, reference: str, metamodel_Constraint: "metamodel_Table" = None, metamodel_Constraint10: set["metamodel_Column"] = None, metamodel_Constraint14: "metamodel_Column" = None):
        self.name = name
        self.type = type
        self.reference = reference
        self.metamodel_Constraint = metamodel_Constraint
        self.metamodel_Constraint10 = metamodel_Constraint10 if metamodel_Constraint10 is not None else set()
        self.metamodel_Constraint14 = metamodel_Constraint14
        
    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def metamodel_Constraint14(self):
        return self.__metamodel_Constraint14

    @metamodel_Constraint14.setter
    def metamodel_Constraint14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Constraint__metamodel_Constraint14", None)
        self.__metamodel_Constraint14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Column13"):
                opp_val = getattr(old_value, "metamodel_Column13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Column13"):
                opp_val = getattr(value, "metamodel_Column13", None)
                if opp_val is None:
                    setattr(value, "metamodel_Column13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_Constraint10(self):
        return self.__metamodel_Constraint10

    @metamodel_Constraint10.setter
    def metamodel_Constraint10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Constraint__metamodel_Constraint10", None)
        self.__metamodel_Constraint10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Column11"):
                    opp_val = getattr(item, "metamodel_Column11", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Column11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Column11"):
                    opp_val = getattr(item, "metamodel_Column11", None)
                    
                    setattr(item, "metamodel_Column11", self)
                    

    @property
    def metamodel_Constraint(self):
        return self.__metamodel_Constraint

    @metamodel_Constraint.setter
    def metamodel_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Constraint__metamodel_Constraint", None)
        self.__metamodel_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Table4"):
                opp_val = getattr(old_value, "metamodel_Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Table4"):
                opp_val = getattr(value, "metamodel_Table4", None)
                if opp_val is None:
                    setattr(value, "metamodel_Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
