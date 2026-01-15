from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    ascii = "ascii"
    blob = "blob"
    boolean = "boolean"
    counter = "counter"
    decimal = "decimal"
    double = "double"
    float = "float"
    int = "int"
    text = "text"
    timestamp = "timestamp"
    uuid = "uuid"
    timeuuid = "timeuuid"
    varchar = "varchar"
    varint = "varint"
    bigint = "bigint"


############################################
# Definition of Classes
############################################

class nosql_Cell:

    def __init__(self, value: str, nosql_Cell: "nosql_Row" = None, nosql_Cell38: "nosql_Column" = None):
        self.value = value
        self.nosql_Cell = nosql_Cell
        self.nosql_Cell38 = nosql_Cell38
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def nosql_Cell38(self):
        return self.__nosql_Cell38

    @nosql_Cell38.setter
    def nosql_Cell38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Cell__nosql_Cell38", None)
        self.__nosql_Cell38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_Column39"):
                opp_val = getattr(old_value, "nosql_Column39", None)
                if opp_val == self:
                    setattr(old_value, "nosql_Column39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_Column39"):
                opp_val = getattr(value, "nosql_Column39", None)
                setattr(value, "nosql_Column39", self)

    @property
    def nosql_Cell(self):
        return self.__nosql_Cell

    @nosql_Cell.setter
    def nosql_Cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Cell__nosql_Cell", None)
        self.__nosql_Cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_Row33"):
                opp_val = getattr(old_value, "nosql_Row33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_Row33"):
                opp_val = getattr(value, "nosql_Row33", None)
                if opp_val is None:
                    setattr(value, "nosql_Row33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ColumnFamily:

    pass
class nosql_Column:

    def __init__(self, name: str, datatype: str, size: str, nosql_Column14: "nosql_ColumnFamily" = None, nosql_Column: "nosql_Index" = None, nosql_Column31: "nosql_PK" = None, nosql_Column27: "nosql_ColumnFamily" = None, nosql_Column39: "nosql_Cell" = None, nosql_Column36: "nosql_Row" = None):
        self.name = name
        self.datatype = datatype
        self.size = size
        self.nosql_Column14 = nosql_Column14
        self.nosql_Column = nosql_Column
        self.nosql_Column31 = nosql_Column31
        self.nosql_Column27 = nosql_Column27
        self.nosql_Column39 = nosql_Column39
        self.nosql_Column36 = nosql_Column36
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def datatype(self) -> str:
        return self.__datatype

    @datatype.setter
    def datatype(self, datatype: str):
        self.__datatype = datatype

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def nosql_Column39(self):
        return self.__nosql_Column39

    @nosql_Column39.setter
    def nosql_Column39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Column__nosql_Column39", None)
        self.__nosql_Column39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_Cell38"):
                opp_val = getattr(old_value, "nosql_Cell38", None)
                if opp_val == self:
                    setattr(old_value, "nosql_Cell38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_Cell38"):
                opp_val = getattr(value, "nosql_Cell38", None)
                setattr(value, "nosql_Cell38", self)

    @property
    def nosql_Column36(self):
        return self.__nosql_Column36

    @nosql_Column36.setter
    def nosql_Column36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Column__nosql_Column36", None)
        self.__nosql_Column36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_Row35"):
                opp_val = getattr(old_value, "nosql_Row35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_Row35"):
                opp_val = getattr(value, "nosql_Row35", None)
                if opp_val is None:
                    setattr(value, "nosql_Row35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nosql_Column14(self):
        return self.__nosql_Column14

    @nosql_Column14.setter
    def nosql_Column14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Column__nosql_Column14", None)
        self.__nosql_Column14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_ColumnFamily13"):
                opp_val = getattr(old_value, "nosql_ColumnFamily13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_ColumnFamily13"):
                opp_val = getattr(value, "nosql_ColumnFamily13", None)
                if opp_val is None:
                    setattr(value, "nosql_ColumnFamily13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nosql_Column31(self):
        return self.__nosql_Column31

    @nosql_Column31.setter
    def nosql_Column31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Column__nosql_Column31", None)
        self.__nosql_Column31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_PK30"):
                opp_val = getattr(old_value, "nosql_PK30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_PK30"):
                opp_val = getattr(value, "nosql_PK30", None)
                if opp_val is None:
                    setattr(value, "nosql_PK30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nosql_Column(self):
        return self.__nosql_Column

    @nosql_Column.setter
    def nosql_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Column__nosql_Column", None)
        self.__nosql_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_Index11"):
                opp_val = getattr(old_value, "nosql_Index11", None)
                if opp_val == self:
                    setattr(old_value, "nosql_Index11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_Index11"):
                opp_val = getattr(value, "nosql_Index11", None)
                setattr(value, "nosql_Index11", self)

    @property
    def nosql_Column27(self):
        return self.__nosql_Column27

    @nosql_Column27.setter
    def nosql_Column27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Column__nosql_Column27", None)
        self.__nosql_Column27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_ColumnFamily28"):
                opp_val = getattr(old_value, "nosql_ColumnFamily28", None)
                if opp_val == self:
                    setattr(old_value, "nosql_ColumnFamily28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_ColumnFamily28"):
                opp_val = getattr(value, "nosql_ColumnFamily28", None)
                setattr(value, "nosql_ColumnFamily28", self)

class nosql_Row(ColumnFamily):

    pass
class nosql_PK:

    pass
class nosql_Options:

    def __init__(self, name: str, value: str, nosql_Options: "nosql_KeySpace" = None, nosql_Options7: "nosql_KeySpace" = None, nosql_Options17: "nosql_ColumnFamily" = None):
        self.name = name
        self.value = value
        self.nosql_Options = nosql_Options
        self.nosql_Options7 = nosql_Options7
        self.nosql_Options17 = nosql_Options17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def nosql_Options17(self):
        return self.__nosql_Options17

    @nosql_Options17.setter
    def nosql_Options17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Options__nosql_Options17", None)
        self.__nosql_Options17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_ColumnFamily16"):
                opp_val = getattr(old_value, "nosql_ColumnFamily16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_ColumnFamily16"):
                opp_val = getattr(value, "nosql_ColumnFamily16", None)
                if opp_val is None:
                    setattr(value, "nosql_ColumnFamily16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nosql_Options7(self):
        return self.__nosql_Options7

    @nosql_Options7.setter
    def nosql_Options7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Options__nosql_Options7", None)
        self.__nosql_Options7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_KeySpace6"):
                opp_val = getattr(old_value, "nosql_KeySpace6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_KeySpace6"):
                opp_val = getattr(value, "nosql_KeySpace6", None)
                if opp_val is None:
                    setattr(value, "nosql_KeySpace6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nosql_Options(self):
        return self.__nosql_Options

    @nosql_Options.setter
    def nosql_Options(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Options__nosql_Options", None)
        self.__nosql_Options = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_KeySpace4"):
                opp_val = getattr(old_value, "nosql_KeySpace4", None)
                if opp_val == self:
                    setattr(old_value, "nosql_KeySpace4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_KeySpace4"):
                opp_val = getattr(value, "nosql_KeySpace4", None)
                setattr(value, "nosql_KeySpace4", self)

class nosql_ColumnFamily:

    def __init__(self, name: str, comment: str, nosql_ColumnFamily: "nosql_KeySpace" = None, nosql_ColumnFamily13: set["nosql_Column"] = None, nosql_ColumnFamily16: set["nosql_Options"] = None, nosql_ColumnFamily19: "nosql_PK" = None, nosql_ColumnFamily22: set["nosql_Row"] = None, nosql_ColumnFamily24: "nosql_KeySpace" = None, nosql_ColumnFamily28: "nosql_Column" = None):
        self.name = name
        self.comment = comment
        self.nosql_ColumnFamily = nosql_ColumnFamily
        self.nosql_ColumnFamily13 = nosql_ColumnFamily13 if nosql_ColumnFamily13 is not None else set()
        self.nosql_ColumnFamily16 = nosql_ColumnFamily16 if nosql_ColumnFamily16 is not None else set()
        self.nosql_ColumnFamily19 = nosql_ColumnFamily19
        self.nosql_ColumnFamily22 = nosql_ColumnFamily22 if nosql_ColumnFamily22 is not None else set()
        self.nosql_ColumnFamily24 = nosql_ColumnFamily24
        self.nosql_ColumnFamily28 = nosql_ColumnFamily28
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nosql_ColumnFamily16(self):
        return self.__nosql_ColumnFamily16

    @nosql_ColumnFamily16.setter
    def nosql_ColumnFamily16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_ColumnFamily__nosql_ColumnFamily16", None)
        self.__nosql_ColumnFamily16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nosql_Options17"):
                    opp_val = getattr(item, "nosql_Options17", None)
                    
                    if opp_val == self:
                        setattr(item, "nosql_Options17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nosql_Options17"):
                    opp_val = getattr(item, "nosql_Options17", None)
                    
                    setattr(item, "nosql_Options17", self)
                    

    @property
    def nosql_ColumnFamily24(self):
        return self.__nosql_ColumnFamily24

    @nosql_ColumnFamily24.setter
    def nosql_ColumnFamily24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_ColumnFamily__nosql_ColumnFamily24", None)
        self.__nosql_ColumnFamily24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_KeySpace25"):
                opp_val = getattr(old_value, "nosql_KeySpace25", None)
                if opp_val == self:
                    setattr(old_value, "nosql_KeySpace25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_KeySpace25"):
                opp_val = getattr(value, "nosql_KeySpace25", None)
                setattr(value, "nosql_KeySpace25", self)

    @property
    def nosql_ColumnFamily22(self):
        return self.__nosql_ColumnFamily22

    @nosql_ColumnFamily22.setter
    def nosql_ColumnFamily22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_ColumnFamily__nosql_ColumnFamily22", None)
        self.__nosql_ColumnFamily22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nosql_Row"):
                    opp_val = getattr(item, "nosql_Row", None)
                    
                    if opp_val == self:
                        setattr(item, "nosql_Row", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nosql_Row"):
                    opp_val = getattr(item, "nosql_Row", None)
                    
                    setattr(item, "nosql_Row", self)
                    

    @property
    def nosql_ColumnFamily(self):
        return self.__nosql_ColumnFamily

    @nosql_ColumnFamily.setter
    def nosql_ColumnFamily(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_ColumnFamily__nosql_ColumnFamily", None)
        self.__nosql_ColumnFamily = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_KeySpace2"):
                opp_val = getattr(old_value, "nosql_KeySpace2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_KeySpace2"):
                opp_val = getattr(value, "nosql_KeySpace2", None)
                if opp_val is None:
                    setattr(value, "nosql_KeySpace2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nosql_ColumnFamily28(self):
        return self.__nosql_ColumnFamily28

    @nosql_ColumnFamily28.setter
    def nosql_ColumnFamily28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_ColumnFamily__nosql_ColumnFamily28", None)
        self.__nosql_ColumnFamily28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_Column27"):
                opp_val = getattr(old_value, "nosql_Column27", None)
                if opp_val == self:
                    setattr(old_value, "nosql_Column27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_Column27"):
                opp_val = getattr(value, "nosql_Column27", None)
                setattr(value, "nosql_Column27", self)

    @property
    def nosql_ColumnFamily13(self):
        return self.__nosql_ColumnFamily13

    @nosql_ColumnFamily13.setter
    def nosql_ColumnFamily13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_ColumnFamily__nosql_ColumnFamily13", None)
        self.__nosql_ColumnFamily13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nosql_Column14"):
                    opp_val = getattr(item, "nosql_Column14", None)
                    
                    if opp_val == self:
                        setattr(item, "nosql_Column14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nosql_Column14"):
                    opp_val = getattr(item, "nosql_Column14", None)
                    
                    setattr(item, "nosql_Column14", self)
                    

    @property
    def nosql_ColumnFamily19(self):
        return self.__nosql_ColumnFamily19

    @nosql_ColumnFamily19.setter
    def nosql_ColumnFamily19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_ColumnFamily__nosql_ColumnFamily19", None)
        self.__nosql_ColumnFamily19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_PK20"):
                opp_val = getattr(old_value, "nosql_PK20", None)
                if opp_val == self:
                    setattr(old_value, "nosql_PK20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_PK20"):
                opp_val = getattr(value, "nosql_PK20", None)
                setattr(value, "nosql_PK20", self)

class nosql_Index:

    def __init__(self, name: str, reference: str, nosql_Index: "nosql_KeySpace" = None, nosql_Index11: "nosql_Column" = None):
        self.name = name
        self.reference = reference
        self.nosql_Index = nosql_Index
        self.nosql_Index11 = nosql_Index11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def nosql_Index11(self):
        return self.__nosql_Index11

    @nosql_Index11.setter
    def nosql_Index11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Index__nosql_Index11", None)
        self.__nosql_Index11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_Column"):
                opp_val = getattr(old_value, "nosql_Column", None)
                if opp_val == self:
                    setattr(old_value, "nosql_Column", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_Column"):
                opp_val = getattr(value, "nosql_Column", None)
                setattr(value, "nosql_Column", self)

    @property
    def nosql_Index(self):
        return self.__nosql_Index

    @nosql_Index.setter
    def nosql_Index(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Index__nosql_Index", None)
        self.__nosql_Index = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_KeySpace"):
                opp_val = getattr(old_value, "nosql_KeySpace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_KeySpace"):
                opp_val = getattr(value, "nosql_KeySpace", None)
                if opp_val is None:
                    setattr(value, "nosql_KeySpace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class nosql_KeySpace:

    def __init__(self, name: str, nosql_KeySpace: set["nosql_Index"] = None, nosql_KeySpace2: set["nosql_ColumnFamily"] = None, nosql_KeySpace4: "nosql_Options" = None, nosql_KeySpace6: set["nosql_Options"] = None, nosql_KeySpace9: set["nosql_PK"] = None, nosql_KeySpace25: "nosql_ColumnFamily" = None):
        self.name = name
        self.nosql_KeySpace = nosql_KeySpace if nosql_KeySpace is not None else set()
        self.nosql_KeySpace2 = nosql_KeySpace2 if nosql_KeySpace2 is not None else set()
        self.nosql_KeySpace4 = nosql_KeySpace4
        self.nosql_KeySpace6 = nosql_KeySpace6 if nosql_KeySpace6 is not None else set()
        self.nosql_KeySpace9 = nosql_KeySpace9 if nosql_KeySpace9 is not None else set()
        self.nosql_KeySpace25 = nosql_KeySpace25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nosql_KeySpace(self):
        return self.__nosql_KeySpace

    @nosql_KeySpace.setter
    def nosql_KeySpace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_KeySpace__nosql_KeySpace", None)
        self.__nosql_KeySpace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nosql_Index"):
                    opp_val = getattr(item, "nosql_Index", None)
                    
                    if opp_val == self:
                        setattr(item, "nosql_Index", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nosql_Index"):
                    opp_val = getattr(item, "nosql_Index", None)
                    
                    setattr(item, "nosql_Index", self)
                    

    @property
    def nosql_KeySpace25(self):
        return self.__nosql_KeySpace25

    @nosql_KeySpace25.setter
    def nosql_KeySpace25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_KeySpace__nosql_KeySpace25", None)
        self.__nosql_KeySpace25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_ColumnFamily24"):
                opp_val = getattr(old_value, "nosql_ColumnFamily24", None)
                if opp_val == self:
                    setattr(old_value, "nosql_ColumnFamily24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_ColumnFamily24"):
                opp_val = getattr(value, "nosql_ColumnFamily24", None)
                setattr(value, "nosql_ColumnFamily24", self)

    @property
    def nosql_KeySpace9(self):
        return self.__nosql_KeySpace9

    @nosql_KeySpace9.setter
    def nosql_KeySpace9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_KeySpace__nosql_KeySpace9", None)
        self.__nosql_KeySpace9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nosql_PK"):
                    opp_val = getattr(item, "nosql_PK", None)
                    
                    if opp_val == self:
                        setattr(item, "nosql_PK", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nosql_PK"):
                    opp_val = getattr(item, "nosql_PK", None)
                    
                    setattr(item, "nosql_PK", self)
                    

    @property
    def nosql_KeySpace6(self):
        return self.__nosql_KeySpace6

    @nosql_KeySpace6.setter
    def nosql_KeySpace6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_KeySpace__nosql_KeySpace6", None)
        self.__nosql_KeySpace6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nosql_Options7"):
                    opp_val = getattr(item, "nosql_Options7", None)
                    
                    if opp_val == self:
                        setattr(item, "nosql_Options7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nosql_Options7"):
                    opp_val = getattr(item, "nosql_Options7", None)
                    
                    setattr(item, "nosql_Options7", self)
                    

    @property
    def nosql_KeySpace2(self):
        return self.__nosql_KeySpace2

    @nosql_KeySpace2.setter
    def nosql_KeySpace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_KeySpace__nosql_KeySpace2", None)
        self.__nosql_KeySpace2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nosql_ColumnFamily"):
                    opp_val = getattr(item, "nosql_ColumnFamily", None)
                    
                    if opp_val == self:
                        setattr(item, "nosql_ColumnFamily", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nosql_ColumnFamily"):
                    opp_val = getattr(item, "nosql_ColumnFamily", None)
                    
                    setattr(item, "nosql_ColumnFamily", self)
                    

    @property
    def nosql_KeySpace4(self):
        return self.__nosql_KeySpace4

    @nosql_KeySpace4.setter
    def nosql_KeySpace4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_KeySpace__nosql_KeySpace4", None)
        self.__nosql_KeySpace4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_Options"):
                opp_val = getattr(old_value, "nosql_Options", None)
                if opp_val == self:
                    setattr(old_value, "nosql_Options", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_Options"):
                opp_val = getattr(value, "nosql_Options", None)
                setattr(value, "nosql_Options", self)
