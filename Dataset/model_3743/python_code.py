from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SuppliedMediaTypes(Enum):
    SI_FEATURELIST = "SI_FEATURELIST"
    SI_COLOR = "SI_COLOR"
    ORDAudio = "ORDAudio"
    ORDImage = "ORDImage"
    ORDVideo = "ORDVideo"
    ORDDoc = "ORDDoc"
    ORDImageSignature = "ORDImageSignature"
    SI_STILLIMAGE = "SI_STILLIMAGE"
    SI_AVERAGECOLOR = "SI_AVERAGECOLOR"
    SI_POSITIONALCOLOR = "SI_POSITIONALCOLOR"
    SI_COLORHISTOGRAM = "SI_COLORHISTOGRAM"
    SI_TEXTURE = "SI_TEXTURE"
class RawFeatures(Enum):
    size = "size"
class ParameterMode(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class BuiltInLongAndRawTypes(Enum):
    LONG = "LONG"
    LONGRAW = "LONGRAW"
    RAW = "RAW"
class BuiltNumberTypes(Enum):
    NUMBER = "NUMBER"
    BINARY_FLOAT = "BINARY_FLOAT"
    BINARY_DOUBLE = "BINARY_DOUBLE"
class SuppliedSpacialTypes(Enum):
    SDO_GEOMETRY = "SDO_GEOMETRY"
    SDO_TOPO_GEOMETRY = "SDO_TOPO_GEOMETRY"
    SDO_RASTER = "SDO_RASTER"
class RowFeatures(Enum):
    size = "size"
class BuiltInCharacterSemantics(Enum):
    BYTE = "BYTE"
    CHAR = "CHAR"
class ANSINumberTypes(Enum):
    NUMERIC = "NUMERIC"
    DECIMAL = "DECIMAL"
    DEC = "DEC"
    INTEGER = "INTEGER"
    INT = "INT"
    SMALLINT = "SMALLINT"
    FLOAT = "FLOAT"
    DOUBLEPRECISION = "DOUBLEPRECISION"
    REAL = "REAL"
class BuiltInDatetimeTypes(Enum):
    DATE = "DATE"
    TIMESTAMP = "TIMESTAMP"
    TIMESTAMPWITHTIMEZONE = "TIMESTAMPWITHTIMEZONE"
    TIMESTAMPWITHLOCALTIMEZONE = "TIMESTAMPWITHLOCALTIMEZONE"
    INTERVALYEARTOMONTH = "INTERVALYEARTOMONTH"
    INTERVALDAYTOSECOND = "INTERVALDAYTOSECOND"
class SuppliedAnyTypes(Enum):
    SYSANYDATA = "SYSANYDATA"
    SYSANYTYPE = "SYSANYTYPE"
    SYSANYDATASET = "SYSANYDATASET"
class SuppliedXMLTypes(Enum):
    XMLTYPE = "XMLTYPE"
    URITYPE = "URITYPE"
class IntervalFeatures(Enum):
    day_precision = "day_precision"
    second_precision = "second_precision"
    year_precision = "year_precision"
class ONDELETEActions(Enum):
    CASCADE = "CASCADE"
    SETNULL = "SETNULL"
class DatetimeFeatures(Enum):
    precision = "precision"
class BuiltInROWIDType(Enum):
    ROWID = "ROWID"
    UROWID = "UROWID"
class BuiltInLOBType(Enum):
    BFILE = "BFILE"
    BLOB = "BLOB"
    CLOB = "CLOB"
    NLOB = "NLOB"
class TriggerActionTime(Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    INSTEADOF = "INSTEADOF"
class NumberFeatures(Enum):
    size = "size"
    precision = "precision"
    scale = "scale"
class TriggerEvent(Enum):
    DELETE = "DELETE"
    INSERT = "INSERT"
    UPDATE = "UPDATE"
class ANSICharacterTypes(Enum):
    CHARACTER = "CHARACTER"
    CHARACTERVARYING = "CHARACTERVARYING"
    CHARVARYING = "CHARVARYING"
    NCHARVARYING = "NCHARVARYING"
    VARCHAR = "VARCHAR"
    NATIONALCHARACTER = "NATIONALCHARACTER"
    NATIONALCHAR = "NATIONALCHAR"
    NATIONALCHARACTERVARYING = "NATIONALCHARACTERVARYING"
    NATIONALCHARVARYING = "NATIONALCHARVARYING"
class CharacterFeatures(Enum):
    size = "size"
    semantic = "semantic"
class BuiltInCharacterTypes(Enum):
    CHAR = "CHAR"
    VARCHAR2 = "VARCHAR2"
    NCHAR = "NCHAR"
    NVARCHAR2 = "NVARCHAR2"


############################################
# Definition of Classes
############################################

class DerivedTable:

    pass
class ORDB4ORA_View(DerivedTable):

    pass
class ORDB4ORA_Trigger:

    def __init__(self, Name: str, Body: str, Event: str, Action: str, Trigger: "ORDB4ORA_Table" = None, ORDB4ORA_Trigger: set["ORDB4ORA_StructuralComponent"] = None, triggers: "ORDB4ORA_Table" = None):
        self.Name = Name
        self.Body = Body
        self.Event = Event
        self.Action = Action
        self.Trigger = Trigger
        self.ORDB4ORA_Trigger = ORDB4ORA_Trigger if ORDB4ORA_Trigger is not None else set()
        self.triggers = triggers
        
    @property
    def Event(self) -> str:
        return self.__Event

    @Event.setter
    def Event(self, Event: str):
        self.__Event = Event

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Action(self) -> str:
        return self.__Action

    @Action.setter
    def Action(self, Action: str):
        self.__Action = Action

    @property
    def Body(self) -> str:
        return self.__Body

    @Body.setter
    def Body(self, Body: str):
        self.__Body = Body

    @property
    def ORDB4ORA_Trigger(self):
        return self.__ORDB4ORA_Trigger

    @ORDB4ORA_Trigger.setter
    def ORDB4ORA_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Trigger__ORDB4ORA_Trigger", None)
        self.__ORDB4ORA_Trigger = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ORDB4ORA_StructuralComponent72"):
                    opp_val = getattr(item, "ORDB4ORA_StructuralComponent72", None)
                    
                    if opp_val == self:
                        setattr(item, "ORDB4ORA_StructuralComponent72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ORDB4ORA_StructuralComponent72"):
                    opp_val = getattr(item, "ORDB4ORA_StructuralComponent72", None)
                    
                    setattr(item, "ORDB4ORA_StructuralComponent72", self)
                    

    @property
    def Trigger(self):
        return self.__Trigger

    @Trigger.setter
    def Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Trigger__Trigger", None)
        self.__Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table69"):
                opp_val = getattr(old_value, "table69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table69"):
                opp_val = getattr(value, "table69", None)
                if opp_val is None:
                    setattr(value, "table69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def triggers(self):
        return self.__triggers

    @triggers.setter
    def triggers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Trigger__triggers", None)
        self.__triggers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table74"):
                opp_val = getattr(old_value, "Table74", None)
                if opp_val == self:
                    setattr(old_value, "Table74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table74"):
                opp_val = getattr(value, "Table74", None)
                setattr(value, "Table74", self)

class Table:

    pass
class ORDB4ORA_DerivedTable(Table):

    def __init__(self, query_expression: str):
        self.query_expression = query_expression
        
    @property
    def query_expression(self) -> str:
        return self.__query_expression

    @query_expression.setter
    def query_expression(self, query_expression: str):
        self.__query_expression = query_expression

class ORDB4ORA_StoredNestedTable:

    def __init__(self, Name: str, storedNested: "ORDB4ORA_TypedTable" = None, ORDB4ORA_StoredNestedTable: "ORDB4ORA_Attribute" = None, StoredNestedTable: "ORDB4ORA_TypedTable" = None):
        self.Name = Name
        self.storedNested = storedNested
        self.ORDB4ORA_StoredNestedTable = ORDB4ORA_StoredNestedTable
        self.StoredNestedTable = StoredNestedTable
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def storedNested(self):
        return self.__storedNested

    @storedNested.setter
    def storedNested(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StoredNestedTable__storedNested", None)
        self.__storedNested = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypedTable"):
                opp_val = getattr(old_value, "TypedTable", None)
                if opp_val == self:
                    setattr(old_value, "TypedTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypedTable"):
                opp_val = getattr(value, "TypedTable", None)
                setattr(value, "TypedTable", self)

    @property
    def ORDB4ORA_StoredNestedTable(self):
        return self.__ORDB4ORA_StoredNestedTable

    @ORDB4ORA_StoredNestedTable.setter
    def ORDB4ORA_StoredNestedTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StoredNestedTable__ORDB4ORA_StoredNestedTable", None)
        self.__ORDB4ORA_StoredNestedTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_Attribute"):
                opp_val = getattr(old_value, "ORDB4ORA_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_Attribute"):
                opp_val = getattr(value, "ORDB4ORA_Attribute", None)
                setattr(value, "ORDB4ORA_Attribute", self)

    @property
    def StoredNestedTable(self):
        return self.__StoredNestedTable

    @StoredNestedTable.setter
    def StoredNestedTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StoredNestedTable__StoredNestedTable", None)
        self.__StoredNestedTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typed"):
                opp_val = getattr(old_value, "typed", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typed"):
                opp_val = getattr(value, "typed", None)
                if opp_val is None:
                    setattr(value, "typed", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ORDB4ORA_TypedTable(Table):

    pass
class ORDB4ORA_Parameter:

    def __init__(self, Name: str, ORDB4ORA_Parameter: "ORDB4ORA_Datatype" = None):
        self.Name = Name
        self.ORDB4ORA_Parameter = ORDB4ORA_Parameter
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ORDB4ORA_Parameter(self):
        return self.__ORDB4ORA_Parameter

    @ORDB4ORA_Parameter.setter
    def ORDB4ORA_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Parameter__ORDB4ORA_Parameter", None)
        self.__ORDB4ORA_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_Datatype39"):
                opp_val = getattr(old_value, "ORDB4ORA_Datatype39", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_Datatype39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_Datatype39"):
                opp_val = getattr(value, "ORDB4ORA_Datatype39", None)
                setattr(value, "ORDB4ORA_Datatype39", self)

class ORDB4ORA_StructuralComponent:

    def __init__(self, Name: str, StructuralComponent: "ORDB4ORA_Restriction" = None, ORDB4ORA_StructuralComponent: "ORDB4ORA_Datatype" = None, ORDB4ORA_StructuralComponent49: set["ORDB4ORA_Feature"] = None, attributes: set["ORDB4ORA_Restriction"] = None, ORDB4ORA_StructuralComponent72: "ORDB4ORA_Trigger" = None, ORDB4ORA_StructuralComponent84: "ORDB4ORA_View" = None):
        self.Name = Name
        self.StructuralComponent = StructuralComponent
        self.ORDB4ORA_StructuralComponent = ORDB4ORA_StructuralComponent
        self.ORDB4ORA_StructuralComponent49 = ORDB4ORA_StructuralComponent49 if ORDB4ORA_StructuralComponent49 is not None else set()
        self.attributes = attributes if attributes is not None else set()
        self.ORDB4ORA_StructuralComponent72 = ORDB4ORA_StructuralComponent72
        self.ORDB4ORA_StructuralComponent84 = ORDB4ORA_StructuralComponent84
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def StructuralComponent(self):
        return self.__StructuralComponent

    @StructuralComponent.setter
    def StructuralComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuralComponent__StructuralComponent", None)
        self.__StructuralComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restrictions"):
                opp_val = getattr(old_value, "restrictions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restrictions"):
                opp_val = getattr(value, "restrictions", None)
                if opp_val is None:
                    setattr(value, "restrictions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuralComponent__attributes", None)
        self.__attributes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Restriction"):
                    opp_val = getattr(item, "Restriction", None)
                    
                    if opp_val == self:
                        setattr(item, "Restriction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Restriction"):
                    opp_val = getattr(item, "Restriction", None)
                    
                    setattr(item, "Restriction", self)
                    

    @property
    def ORDB4ORA_StructuralComponent49(self):
        return self.__ORDB4ORA_StructuralComponent49

    @ORDB4ORA_StructuralComponent49.setter
    def ORDB4ORA_StructuralComponent49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuralComponent__ORDB4ORA_StructuralComponent49", None)
        self.__ORDB4ORA_StructuralComponent49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ORDB4ORA_Feature"):
                    opp_val = getattr(item, "ORDB4ORA_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "ORDB4ORA_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ORDB4ORA_Feature"):
                    opp_val = getattr(item, "ORDB4ORA_Feature", None)
                    
                    setattr(item, "ORDB4ORA_Feature", self)
                    

    @property
    def ORDB4ORA_StructuralComponent84(self):
        return self.__ORDB4ORA_StructuralComponent84

    @ORDB4ORA_StructuralComponent84.setter
    def ORDB4ORA_StructuralComponent84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuralComponent__ORDB4ORA_StructuralComponent84", None)
        self.__ORDB4ORA_StructuralComponent84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_View"):
                opp_val = getattr(old_value, "ORDB4ORA_View", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_View"):
                opp_val = getattr(value, "ORDB4ORA_View", None)
                if opp_val is None:
                    setattr(value, "ORDB4ORA_View", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ORDB4ORA_StructuralComponent72(self):
        return self.__ORDB4ORA_StructuralComponent72

    @ORDB4ORA_StructuralComponent72.setter
    def ORDB4ORA_StructuralComponent72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuralComponent__ORDB4ORA_StructuralComponent72", None)
        self.__ORDB4ORA_StructuralComponent72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_Trigger"):
                opp_val = getattr(old_value, "ORDB4ORA_Trigger", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_Trigger"):
                opp_val = getattr(value, "ORDB4ORA_Trigger", None)
                if opp_val is None:
                    setattr(value, "ORDB4ORA_Trigger", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ORDB4ORA_StructuralComponent(self):
        return self.__ORDB4ORA_StructuralComponent

    @ORDB4ORA_StructuralComponent.setter
    def ORDB4ORA_StructuralComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuralComponent__ORDB4ORA_StructuralComponent", None)
        self.__ORDB4ORA_StructuralComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_Datatype47"):
                opp_val = getattr(old_value, "ORDB4ORA_Datatype47", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_Datatype47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_Datatype47"):
                opp_val = getattr(value, "ORDB4ORA_Datatype47", None)
                setattr(value, "ORDB4ORA_Datatype47", self)

class ORDB4ORA_Restriction(ABC):

    def __init__(self, Name: str, NameColumns: str, restrictions: set["ORDB4ORA_StructuralComponent"] = None, restriction: "ORDB4ORA_Table" = None, Restriction: "ORDB4ORA_StructuralComponent" = None, Restriction62: "ORDB4ORA_Table" = None):
        self.Name = Name
        self.NameColumns = NameColumns
        self.restrictions = restrictions if restrictions is not None else set()
        self.restriction = restriction
        self.Restriction = Restriction
        self.Restriction62 = Restriction62
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def NameColumns(self) -> str:
        return self.__NameColumns

    @NameColumns.setter
    def NameColumns(self, NameColumns: str):
        self.__NameColumns = NameColumns

    @property
    def Restriction62(self):
        return self.__Restriction62

    @Restriction62.setter
    def Restriction62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Restriction__Restriction62", None)
        self.__Restriction62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table"):
                opp_val = getattr(old_value, "table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table"):
                opp_val = getattr(value, "table", None)
                if opp_val is None:
                    setattr(value, "table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Restriction(self):
        return self.__Restriction

    @Restriction.setter
    def Restriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Restriction__Restriction", None)
        self.__Restriction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes"):
                opp_val = getattr(old_value, "attributes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes"):
                opp_val = getattr(value, "attributes", None)
                if opp_val is None:
                    setattr(value, "attributes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def restrictions(self):
        return self.__restrictions

    @restrictions.setter
    def restrictions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Restriction__restrictions", None)
        self.__restrictions = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StructuralComponent"):
                    opp_val = getattr(item, "StructuralComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "StructuralComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StructuralComponent"):
                    opp_val = getattr(item, "StructuralComponent", None)
                    
                    setattr(item, "StructuralComponent", self)
                    

    @property
    def restriction(self):
        return self.__restriction

    @restriction.setter
    def restriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Restriction__restriction", None)
        self.__restriction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table43"):
                opp_val = getattr(old_value, "Table43", None)
                if opp_val == self:
                    setattr(old_value, "Table43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table43"):
                opp_val = getattr(value, "Table43", None)
                setattr(value, "Table43", self)

class ORDB4ORA_Method:

    def __init__(self, Name: str, Body: str, ORDB4ORA_Method: "ORDB4ORA_Method" = None, ORDB4ORA_Method13: "ORDB4ORA_Method" = None, method: "ORDB4ORA_StructuredType" = None, method18: set["ORDB4ORA_MethodParameter"] = None, ORDB4ORA_Method20: "ORDB4ORA_Datatype" = None, Method: "ORDB4ORA_MethodParameter" = None, Method54: "ORDB4ORA_StructuredType" = None):
        self.Name = Name
        self.Body = Body
        self.ORDB4ORA_Method = ORDB4ORA_Method
        self.ORDB4ORA_Method13 = ORDB4ORA_Method13
        self.method = method
        self.method18 = method18 if method18 is not None else set()
        self.ORDB4ORA_Method20 = ORDB4ORA_Method20
        self.Method = Method
        self.Method54 = Method54
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Body(self) -> str:
        return self.__Body

    @Body.setter
    def Body(self, Body: str):
        self.__Body = Body

    @property
    def ORDB4ORA_Method13(self):
        return self.__ORDB4ORA_Method13

    @ORDB4ORA_Method13.setter
    def ORDB4ORA_Method13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Method__ORDB4ORA_Method13", None)
        self.__ORDB4ORA_Method13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_Method"):
                opp_val = getattr(old_value, "ORDB4ORA_Method", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_Method", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_Method"):
                opp_val = getattr(value, "ORDB4ORA_Method", None)
                setattr(value, "ORDB4ORA_Method", self)

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Method__method", None)
        self.__method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StructuredType16"):
                opp_val = getattr(old_value, "StructuredType16", None)
                if opp_val == self:
                    setattr(old_value, "StructuredType16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StructuredType16"):
                opp_val = getattr(value, "StructuredType16", None)
                setattr(value, "StructuredType16", self)

    @property
    def ORDB4ORA_Method(self):
        return self.__ORDB4ORA_Method

    @ORDB4ORA_Method.setter
    def ORDB4ORA_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Method__ORDB4ORA_Method", None)
        self.__ORDB4ORA_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_Method13"):
                opp_val = getattr(old_value, "ORDB4ORA_Method13", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_Method13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_Method13"):
                opp_val = getattr(value, "ORDB4ORA_Method13", None)
                setattr(value, "ORDB4ORA_Method13", self)

    @property
    def Method54(self):
        return self.__Method54

    @Method54.setter
    def Method54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Method__Method54", None)
        self.__Method54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structured53"):
                opp_val = getattr(old_value, "structured53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structured53"):
                opp_val = getattr(value, "structured53", None)
                if opp_val is None:
                    setattr(value, "structured53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def method18(self):
        return self.__method18

    @method18.setter
    def method18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Method__method18", None)
        self.__method18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MethodParameter"):
                    opp_val = getattr(item, "MethodParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "MethodParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MethodParameter"):
                    opp_val = getattr(item, "MethodParameter", None)
                    
                    setattr(item, "MethodParameter", self)
                    

    @property
    def ORDB4ORA_Method20(self):
        return self.__ORDB4ORA_Method20

    @ORDB4ORA_Method20.setter
    def ORDB4ORA_Method20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Method__ORDB4ORA_Method20", None)
        self.__ORDB4ORA_Method20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_Datatype21"):
                opp_val = getattr(old_value, "ORDB4ORA_Datatype21", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_Datatype21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_Datatype21"):
                opp_val = getattr(value, "ORDB4ORA_Datatype21", None)
                setattr(value, "ORDB4ORA_Datatype21", self)

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Method__Method", None)
        self.__Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters"):
                opp_val = getattr(old_value, "parameters", None)
                if opp_val == self:
                    setattr(old_value, "parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters"):
                opp_val = getattr(value, "parameters", None)
                setattr(value, "parameters", self)

class Operation:

    pass
class ORDB4ORA_Procedure(Operation):

    pass
class ORDB4ORA_Function(Operation):

    pass
class Parameter:

    pass
class ORDB4ORA_OperationParameter(Parameter):

    def __init__(self, Mode: str, operationParameters: "ORDB4ORA_Operation" = None, OperationParameter: "ORDB4ORA_Operation" = None):
        self.Mode = Mode
        self.operationParameters = operationParameters
        self.OperationParameter = OperationParameter
        
    @property
    def Mode(self) -> str:
        return self.__Mode

    @Mode.setter
    def Mode(self, Mode: str):
        self.__Mode = Mode

    @property
    def OperationParameter(self):
        return self.__OperationParameter

    @OperationParameter.setter
    def OperationParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_OperationParameter__OperationParameter", None)
        self.__OperationParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation"):
                opp_val = getattr(old_value, "operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation"):
                opp_val = getattr(value, "operation", None)
                if opp_val is None:
                    setattr(value, "operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operationParameters(self):
        return self.__operationParameters

    @operationParameters.setter
    def operationParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_OperationParameter__operationParameters", None)
        self.__operationParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation32"):
                opp_val = getattr(old_value, "Operation32", None)
                if opp_val == self:
                    setattr(old_value, "Operation32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation32"):
                opp_val = getattr(value, "Operation32", None)
                setattr(value, "Operation32", self)

class ORDB4ORA_MethodParameter(Parameter):

    pass
class Restriction:

    pass
class ORDB4ORA_PrimaryKey(Restriction):

    pass
class ORDB4ORA_Unique(Restriction):

    pass
class ORDB4ORA_NotNull(Restriction):

    pass
class ORDB4ORA_Check(Restriction):

    def __init__(self, Condition: str):
        self.Condition = Condition
        
    @property
    def Condition(self) -> str:
        return self.__Condition

    @Condition.setter
    def Condition(self, Condition: str):
        self.__Condition = Condition

class Feature:

    pass
class ORDB4ORA_RawFeature(Feature):

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ORDB4ORA_DatetimeFeature(Feature):

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class ORDB4ORA_RowFeature(Feature):

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class ORDB4ORA_NumberFeature(Feature):

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ORDB4ORA_IntervalFeature(Feature):

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class ORDB4ORA_CharacterFeature(Feature):

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ORDB4ORA_ForeignKey(Restriction):

    def __init__(self, OnDelete: str, ORDB4ORA_ForeignKey: "ORDB4ORA_Table" = None):
        self.OnDelete = OnDelete
        self.ORDB4ORA_ForeignKey = ORDB4ORA_ForeignKey
        
    @property
    def OnDelete(self) -> str:
        return self.__OnDelete

    @OnDelete.setter
    def OnDelete(self, OnDelete: str):
        self.__OnDelete = OnDelete

    @property
    def ORDB4ORA_ForeignKey(self):
        return self.__ORDB4ORA_ForeignKey

    @ORDB4ORA_ForeignKey.setter
    def ORDB4ORA_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_ForeignKey__ORDB4ORA_ForeignKey", None)
        self.__ORDB4ORA_ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_Table"):
                opp_val = getattr(old_value, "ORDB4ORA_Table", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_Table"):
                opp_val = getattr(value, "ORDB4ORA_Table", None)
                setattr(value, "ORDB4ORA_Table", self)

class ORDB4ORA_Feature(ABC):

    pass
class BuiltInType:

    pass
class ORDB4ORA_LOBType(BuiltInType):

    def __init__(self, Descriptor: str):
        self.Descriptor = Descriptor
        
    @property
    def Descriptor(self) -> str:
        return self.__Descriptor

    @Descriptor.setter
    def Descriptor(self, Descriptor: str):
        self.__Descriptor = Descriptor

class ORDB4ORA_LongAndRawType(BuiltInType):

    def __init__(self, Descriptor: str, Size_Min: int, Size_Max: int):
        self.Descriptor = Descriptor
        self.Size_Min = Size_Min
        self.Size_Max = Size_Max
        
    @property
    def Size_Max(self) -> int:
        return self.__Size_Max

    @Size_Max.setter
    def Size_Max(self, Size_Max: int):
        self.__Size_Max = Size_Max

    @property
    def Size_Min(self) -> int:
        return self.__Size_Min

    @Size_Min.setter
    def Size_Min(self, Size_Min: int):
        self.__Size_Min = Size_Min

    @property
    def Descriptor(self) -> str:
        return self.__Descriptor

    @Descriptor.setter
    def Descriptor(self, Descriptor: str):
        self.__Descriptor = Descriptor

class ORDB4ORA_DatetimeType(BuiltInType):

    def __init__(self, Descriptor: str, SecondPrecision_Min: int, SecondPrecision_Max: int, SecondPrecision_Def: int, DayPrecision_Min: int, DayPrecision_Max: int, DayPrecision_Def: int, YearPrecision_Min: int, YearPrecision_Max: int, YearPrecision_Def: int):
        self.Descriptor = Descriptor
        self.SecondPrecision_Min = SecondPrecision_Min
        self.SecondPrecision_Max = SecondPrecision_Max
        self.SecondPrecision_Def = SecondPrecision_Def
        self.DayPrecision_Min = DayPrecision_Min
        self.DayPrecision_Max = DayPrecision_Max
        self.DayPrecision_Def = DayPrecision_Def
        self.YearPrecision_Min = YearPrecision_Min
        self.YearPrecision_Max = YearPrecision_Max
        self.YearPrecision_Def = YearPrecision_Def
        
    @property
    def Descriptor(self) -> str:
        return self.__Descriptor

    @Descriptor.setter
    def Descriptor(self, Descriptor: str):
        self.__Descriptor = Descriptor

    @property
    def YearPrecision_Min(self) -> int:
        return self.__YearPrecision_Min

    @YearPrecision_Min.setter
    def YearPrecision_Min(self, YearPrecision_Min: int):
        self.__YearPrecision_Min = YearPrecision_Min

    @property
    def YearPrecision_Def(self) -> int:
        return self.__YearPrecision_Def

    @YearPrecision_Def.setter
    def YearPrecision_Def(self, YearPrecision_Def: int):
        self.__YearPrecision_Def = YearPrecision_Def

    @property
    def SecondPrecision_Def(self) -> int:
        return self.__SecondPrecision_Def

    @SecondPrecision_Def.setter
    def SecondPrecision_Def(self, SecondPrecision_Def: int):
        self.__SecondPrecision_Def = SecondPrecision_Def

    @property
    def DayPrecision_Def(self) -> int:
        return self.__DayPrecision_Def

    @DayPrecision_Def.setter
    def DayPrecision_Def(self, DayPrecision_Def: int):
        self.__DayPrecision_Def = DayPrecision_Def

    @property
    def YearPrecision_Max(self) -> int:
        return self.__YearPrecision_Max

    @YearPrecision_Max.setter
    def YearPrecision_Max(self, YearPrecision_Max: int):
        self.__YearPrecision_Max = YearPrecision_Max

    @property
    def DayPrecision_Max(self) -> int:
        return self.__DayPrecision_Max

    @DayPrecision_Max.setter
    def DayPrecision_Max(self, DayPrecision_Max: int):
        self.__DayPrecision_Max = DayPrecision_Max

    @property
    def SecondPrecision_Min(self) -> int:
        return self.__SecondPrecision_Min

    @SecondPrecision_Min.setter
    def SecondPrecision_Min(self, SecondPrecision_Min: int):
        self.__SecondPrecision_Min = SecondPrecision_Min

    @property
    def SecondPrecision_Max(self) -> int:
        return self.__SecondPrecision_Max

    @SecondPrecision_Max.setter
    def SecondPrecision_Max(self, SecondPrecision_Max: int):
        self.__SecondPrecision_Max = SecondPrecision_Max

    @property
    def DayPrecision_Min(self) -> int:
        return self.__DayPrecision_Min

    @DayPrecision_Min.setter
    def DayPrecision_Min(self, DayPrecision_Min: int):
        self.__DayPrecision_Min = DayPrecision_Min

class ORDB4ORA_ROWIDType(BuiltInType):

    def __init__(self, Descriptor: str, Size_Min: int, Size_Max: int):
        self.Descriptor = Descriptor
        self.Size_Min = Size_Min
        self.Size_Max = Size_Max
        
    @property
    def Descriptor(self) -> str:
        return self.__Descriptor

    @Descriptor.setter
    def Descriptor(self, Descriptor: str):
        self.__Descriptor = Descriptor

    @property
    def Size_Max(self) -> int:
        return self.__Size_Max

    @Size_Max.setter
    def Size_Max(self, Size_Max: int):
        self.__Size_Max = Size_Max

    @property
    def Size_Min(self) -> int:
        return self.__Size_Min

    @Size_Min.setter
    def Size_Min(self, Size_Min: int):
        self.__Size_Min = Size_Min

class ORDB4ORA_BuiltInCharacterType(BuiltInType):

    def __init__(self, Descriptor: str, Semantic: str, Size_Min: int, Size_Max: int, Size_Def: int):
        self.Descriptor = Descriptor
        self.Semantic = Semantic
        self.Size_Min = Size_Min
        self.Size_Max = Size_Max
        self.Size_Def = Size_Def
        
    @property
    def Size_Min(self) -> int:
        return self.__Size_Min

    @Size_Min.setter
    def Size_Min(self, Size_Min: int):
        self.__Size_Min = Size_Min

    @property
    def Size_Def(self) -> int:
        return self.__Size_Def

    @Size_Def.setter
    def Size_Def(self, Size_Def: int):
        self.__Size_Def = Size_Def

    @property
    def Size_Max(self) -> int:
        return self.__Size_Max

    @Size_Max.setter
    def Size_Max(self, Size_Max: int):
        self.__Size_Max = Size_Max

    @property
    def Descriptor(self) -> str:
        return self.__Descriptor

    @Descriptor.setter
    def Descriptor(self, Descriptor: str):
        self.__Descriptor = Descriptor

    @property
    def Semantic(self) -> str:
        return self.__Semantic

    @Semantic.setter
    def Semantic(self, Semantic: str):
        self.__Semantic = Semantic

class Datatype:

    pass
class ORDB4ORA_ReferenceType(Datatype):

    def __init__(self, Name: str, ORDB4ORA_ReferenceType: "ORDB4ORA_StructuredType" = None):
        self.Name = Name
        self.ORDB4ORA_ReferenceType = ORDB4ORA_ReferenceType
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ORDB4ORA_ReferenceType(self):
        return self.__ORDB4ORA_ReferenceType

    @ORDB4ORA_ReferenceType.setter
    def ORDB4ORA_ReferenceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_ReferenceType__ORDB4ORA_ReferenceType", None)
        self.__ORDB4ORA_ReferenceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_StructuredType"):
                opp_val = getattr(old_value, "ORDB4ORA_StructuredType", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_StructuredType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_StructuredType"):
                opp_val = getattr(value, "ORDB4ORA_StructuredType", None)
                setattr(value, "ORDB4ORA_StructuredType", self)

class ORDB4ORA_Varray(Datatype):

    def __init__(self, Name: str, NumElements: int, ORDB4ORA_Varray: "ORDB4ORA_Datatype" = None):
        self.Name = Name
        self.NumElements = NumElements
        self.ORDB4ORA_Varray = ORDB4ORA_Varray
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def NumElements(self) -> int:
        return self.__NumElements

    @NumElements.setter
    def NumElements(self, NumElements: int):
        self.__NumElements = NumElements

    @property
    def ORDB4ORA_Varray(self):
        return self.__ORDB4ORA_Varray

    @ORDB4ORA_Varray.setter
    def ORDB4ORA_Varray(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Varray__ORDB4ORA_Varray", None)
        self.__ORDB4ORA_Varray = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_Datatype80"):
                opp_val = getattr(old_value, "ORDB4ORA_Datatype80", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_Datatype80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_Datatype80"):
                opp_val = getattr(value, "ORDB4ORA_Datatype80", None)
                setattr(value, "ORDB4ORA_Datatype80", self)

class ORDB4ORA_NestedTableType(Datatype):

    def __init__(self, Name: str, ORDB4ORA_NestedTableType: "ORDB4ORA_Datatype" = None):
        self.Name = Name
        self.ORDB4ORA_NestedTableType = ORDB4ORA_NestedTableType
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ORDB4ORA_NestedTableType(self):
        return self.__ORDB4ORA_NestedTableType

    @ORDB4ORA_NestedTableType.setter
    def ORDB4ORA_NestedTableType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_NestedTableType__ORDB4ORA_NestedTableType", None)
        self.__ORDB4ORA_NestedTableType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_Datatype24"):
                opp_val = getattr(old_value, "ORDB4ORA_Datatype24", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_Datatype24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_Datatype24"):
                opp_val = getattr(value, "ORDB4ORA_Datatype24", None)
                setattr(value, "ORDB4ORA_Datatype24", self)

class ORDB4ORA_BasicDataType(Datatype):

    pass
class ORDB4ORA_StructuredType(Datatype):

    def __init__(self, Name: str, is_instantiable: bool, is_final: bool, StructuredType: "ORDB4ORA_Attribute" = None, StructuredType16: "ORDB4ORA_Method" = None, ORDB4ORA_StructuredType: "ORDB4ORA_ReferenceType" = None, structured: set["ORDB4ORA_Attribute"] = None, structured53: set["ORDB4ORA_Method"] = None, ORDB4ORA_StructuredType57: "ORDB4ORA_StructuredType" = None, ORDB4ORA_StructuredType55: "ORDB4ORA_StructuredType" = None, structured59: set["ORDB4ORA_TypedTable"] = None, StructuredType78: "ORDB4ORA_TypedTable" = None):
        self.Name = Name
        self.is_instantiable = is_instantiable
        self.is_final = is_final
        self.StructuredType = StructuredType
        self.StructuredType16 = StructuredType16
        self.ORDB4ORA_StructuredType = ORDB4ORA_StructuredType
        self.structured = structured if structured is not None else set()
        self.structured53 = structured53 if structured53 is not None else set()
        self.ORDB4ORA_StructuredType57 = ORDB4ORA_StructuredType57
        self.ORDB4ORA_StructuredType55 = ORDB4ORA_StructuredType55
        self.structured59 = structured59 if structured59 is not None else set()
        self.StructuredType78 = StructuredType78
        
    @property
    def is_final(self) -> bool:
        return self.__is_final

    @is_final.setter
    def is_final(self, is_final: bool):
        self.__is_final = is_final

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def is_instantiable(self) -> bool:
        return self.__is_instantiable

    @is_instantiable.setter
    def is_instantiable(self, is_instantiable: bool):
        self.__is_instantiable = is_instantiable

    @property
    def structured53(self):
        return self.__structured53

    @structured53.setter
    def structured53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuredType__structured53", None)
        self.__structured53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method54"):
                    opp_val = getattr(item, "Method54", None)
                    
                    if opp_val == self:
                        setattr(item, "Method54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method54"):
                    opp_val = getattr(item, "Method54", None)
                    
                    setattr(item, "Method54", self)
                    

    @property
    def StructuredType(self):
        return self.__StructuredType

    @StructuredType.setter
    def StructuredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuredType__StructuredType", None)
        self.__StructuredType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attribute"):
                opp_val = getattr(old_value, "attribute", None)
                if opp_val == self:
                    setattr(old_value, "attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attribute"):
                opp_val = getattr(value, "attribute", None)
                setattr(value, "attribute", self)

    @property
    def ORDB4ORA_StructuredType55(self):
        return self.__ORDB4ORA_StructuredType55

    @ORDB4ORA_StructuredType55.setter
    def ORDB4ORA_StructuredType55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuredType__ORDB4ORA_StructuredType55", None)
        self.__ORDB4ORA_StructuredType55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_StructuredType57"):
                opp_val = getattr(old_value, "ORDB4ORA_StructuredType57", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_StructuredType57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_StructuredType57"):
                opp_val = getattr(value, "ORDB4ORA_StructuredType57", None)
                setattr(value, "ORDB4ORA_StructuredType57", self)

    @property
    def ORDB4ORA_StructuredType(self):
        return self.__ORDB4ORA_StructuredType

    @ORDB4ORA_StructuredType.setter
    def ORDB4ORA_StructuredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuredType__ORDB4ORA_StructuredType", None)
        self.__ORDB4ORA_StructuredType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_ReferenceType"):
                opp_val = getattr(old_value, "ORDB4ORA_ReferenceType", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_ReferenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_ReferenceType"):
                opp_val = getattr(value, "ORDB4ORA_ReferenceType", None)
                setattr(value, "ORDB4ORA_ReferenceType", self)

    @property
    def ORDB4ORA_StructuredType57(self):
        return self.__ORDB4ORA_StructuredType57

    @ORDB4ORA_StructuredType57.setter
    def ORDB4ORA_StructuredType57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuredType__ORDB4ORA_StructuredType57", None)
        self.__ORDB4ORA_StructuredType57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_StructuredType55"):
                opp_val = getattr(old_value, "ORDB4ORA_StructuredType55", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_StructuredType55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_StructuredType55"):
                opp_val = getattr(value, "ORDB4ORA_StructuredType55", None)
                setattr(value, "ORDB4ORA_StructuredType55", self)

    @property
    def StructuredType16(self):
        return self.__StructuredType16

    @StructuredType16.setter
    def StructuredType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuredType__StructuredType16", None)
        self.__StructuredType16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "method"):
                opp_val = getattr(old_value, "method", None)
                if opp_val == self:
                    setattr(old_value, "method", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "method"):
                opp_val = getattr(value, "method", None)
                setattr(value, "method", self)

    @property
    def structured(self):
        return self.__structured

    @structured.setter
    def structured(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuredType__structured", None)
        self.__structured = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

    @property
    def structured59(self):
        return self.__structured59

    @structured59.setter
    def structured59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuredType__structured59", None)
        self.__structured59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypedTable60"):
                    opp_val = getattr(item, "TypedTable60", None)
                    
                    if opp_val == self:
                        setattr(item, "TypedTable60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypedTable60"):
                    opp_val = getattr(item, "TypedTable60", None)
                    
                    setattr(item, "TypedTable60", self)
                    

    @property
    def StructuredType78(self):
        return self.__StructuredType78

    @StructuredType78.setter
    def StructuredType78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_StructuredType__StructuredType78", None)
        self.__StructuredType78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typed77"):
                opp_val = getattr(old_value, "typed77", None)
                if opp_val == self:
                    setattr(old_value, "typed77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typed77"):
                opp_val = getattr(value, "typed77", None)
                setattr(value, "typed77", self)

class StructuralComponent:

    pass
class ORDB4ORA_Column(StructuralComponent):

    pass
class ORDB4ORA_Attribute(StructuralComponent):

    pass
class ORDB4ORA_BuiltInNumberType(BuiltInType):

    def __init__(self, Descriptor: str, Precision_Mn: int, Precision_Max: int, Scale_Min: int, Scale_Max: int):
        self.Descriptor = Descriptor
        self.Precision_Mn = Precision_Mn
        self.Precision_Max = Precision_Max
        self.Scale_Min = Scale_Min
        self.Scale_Max = Scale_Max
        
    @property
    def Precision_Mn(self) -> int:
        return self.__Precision_Mn

    @Precision_Mn.setter
    def Precision_Mn(self, Precision_Mn: int):
        self.__Precision_Mn = Precision_Mn

    @property
    def Scale_Max(self) -> int:
        return self.__Scale_Max

    @Scale_Max.setter
    def Scale_Max(self, Scale_Max: int):
        self.__Scale_Max = Scale_Max

    @property
    def Descriptor(self) -> str:
        return self.__Descriptor

    @Descriptor.setter
    def Descriptor(self, Descriptor: str):
        self.__Descriptor = Descriptor

    @property
    def Scale_Min(self) -> int:
        return self.__Scale_Min

    @Scale_Min.setter
    def Scale_Min(self, Scale_Min: int):
        self.__Scale_Min = Scale_Min

    @property
    def Precision_Max(self) -> int:
        return self.__Precision_Max

    @Precision_Max.setter
    def Precision_Max(self, Precision_Max: int):
        self.__Precision_Max = Precision_Max

class ANSIType:

    pass
class ORDB4ORA_ANSINumberType(ANSIType):

    def __init__(self, Descriptor: str):
        self.Descriptor = Descriptor
        
    @property
    def Descriptor(self) -> str:
        return self.__Descriptor

    @Descriptor.setter
    def Descriptor(self, Descriptor: str):
        self.__Descriptor = Descriptor

class ORDB4ORA_ANSICharacterType(ANSIType):

    def __init__(self, Descriptor: str):
        self.Descriptor = Descriptor
        
    @property
    def Descriptor(self) -> str:
        return self.__Descriptor

    @Descriptor.setter
    def Descriptor(self, Descriptor: str):
        self.__Descriptor = Descriptor

class ORDB4ORA_Package:

    def __init__(self, Name: str, Package: "ORDB4ORA_Model" = None, Package30: "ORDB4ORA_Operation" = None, package: set["ORDB4ORA_Operation"] = None, package36: "ORDB4ORA_Model" = None):
        self.Name = Name
        self.Package = Package
        self.Package30 = Package30
        self.package = package if package is not None else set()
        self.package36 = package36
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Package30(self):
        return self.__Package30

    @Package30.setter
    def Package30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Package__Package30", None)
        self.__Package30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operations"):
                opp_val = getattr(old_value, "operations", None)
                if opp_val == self:
                    setattr(old_value, "operations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operations"):
                opp_val = getattr(value, "operations", None)
                setattr(value, "operations", self)

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Package__Package", None)
        self.__Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model6"):
                opp_val = getattr(old_value, "model6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model6"):
                opp_val = getattr(value, "model6", None)
                if opp_val is None:
                    setattr(value, "model6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def package36(self):
        return self.__package36

    @package36.setter
    def package36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Package__package36", None)
        self.__package36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model37"):
                opp_val = getattr(old_value, "Model37", None)
                if opp_val == self:
                    setattr(old_value, "Model37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model37"):
                opp_val = getattr(value, "Model37", None)
                setattr(value, "Model37", self)

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Package__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation34"):
                    opp_val = getattr(item, "Operation34", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation34"):
                    opp_val = getattr(item, "Operation34", None)
                    
                    setattr(item, "Operation34", self)
                    

class ORDB4ORA_Operation(ABC):

    def __init__(self, Name: str, Body: str, Operation: "ORDB4ORA_Model" = None, operations: "ORDB4ORA_Package" = None, Operation32: "ORDB4ORA_OperationParameter" = None, Operation34: "ORDB4ORA_Package" = None, operation: set["ORDB4ORA_OperationParameter"] = None, operation27: "ORDB4ORA_Model" = None):
        self.Name = Name
        self.Body = Body
        self.Operation = Operation
        self.operations = operations
        self.Operation32 = Operation32
        self.Operation34 = Operation34
        self.operation = operation if operation is not None else set()
        self.operation27 = operation27
        
    @property
    def Body(self) -> str:
        return self.__Body

    @Body.setter
    def Body(self, Body: str):
        self.__Body = Body

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def operation27(self):
        return self.__operation27

    @operation27.setter
    def operation27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Operation__operation27", None)
        self.__operation27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model28"):
                opp_val = getattr(old_value, "Model28", None)
                if opp_val == self:
                    setattr(old_value, "Model28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model28"):
                opp_val = getattr(value, "Model28", None)
                setattr(value, "Model28", self)

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Operation__operation", None)
        self.__operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OperationParameter"):
                    opp_val = getattr(item, "OperationParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "OperationParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OperationParameter"):
                    opp_val = getattr(item, "OperationParameter", None)
                    
                    setattr(item, "OperationParameter", self)
                    

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model4"):
                opp_val = getattr(old_value, "model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model4"):
                opp_val = getattr(value, "model4", None)
                if opp_val is None:
                    setattr(value, "model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operations(self):
        return self.__operations

    @operations.setter
    def operations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Operation__operations", None)
        self.__operations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package30"):
                opp_val = getattr(old_value, "Package30", None)
                if opp_val == self:
                    setattr(old_value, "Package30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package30"):
                opp_val = getattr(value, "Package30", None)
                setattr(value, "Package30", self)

    @property
    def Operation32(self):
        return self.__Operation32

    @Operation32.setter
    def Operation32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Operation__Operation32", None)
        self.__Operation32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operationParameters"):
                opp_val = getattr(old_value, "operationParameters", None)
                if opp_val == self:
                    setattr(old_value, "operationParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operationParameters"):
                opp_val = getattr(value, "operationParameters", None)
                setattr(value, "operationParameters", self)

    @property
    def Operation34(self):
        return self.__Operation34

    @Operation34.setter
    def Operation34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Operation__Operation34", None)
        self.__Operation34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package"):
                opp_val = getattr(old_value, "package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package"):
                opp_val = getattr(value, "package", None)
                if opp_val is None:
                    setattr(value, "package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ORDB4ORA_Table:

    def __init__(self, Name: str, Table: "ORDB4ORA_Model" = None, Table9: "ORDB4ORA_Column" = None, ORDB4ORA_Table: "ORDB4ORA_ForeignKey" = None, Table43: "ORDB4ORA_Restriction" = None, table: set["ORDB4ORA_Restriction"] = None, table64: set["ORDB4ORA_Column"] = None, table66: "ORDB4ORA_Model" = None, table69: set["ORDB4ORA_Trigger"] = None, tables: set["ORDB4ORA_View"] = None, Table74: "ORDB4ORA_Trigger" = None, Table82: "ORDB4ORA_View" = None):
        self.Name = Name
        self.Table = Table
        self.Table9 = Table9
        self.ORDB4ORA_Table = ORDB4ORA_Table
        self.Table43 = Table43
        self.table = table if table is not None else set()
        self.table64 = table64 if table64 is not None else set()
        self.table66 = table66
        self.table69 = table69 if table69 is not None else set()
        self.tables = tables if tables is not None else set()
        self.Table74 = Table74
        self.Table82 = Table82
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def table64(self):
        return self.__table64

    @table64.setter
    def table64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Table__table64", None)
        self.__table64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    if opp_val == self:
                        setattr(item, "Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    setattr(item, "Column", self)
                    

    @property
    def tables(self):
        return self.__tables

    @tables.setter
    def tables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Table__tables", None)
        self.__tables = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "View"):
                    opp_val = getattr(item, "View", None)
                    
                    if opp_val == self:
                        setattr(item, "View", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "View"):
                    opp_val = getattr(item, "View", None)
                    
                    setattr(item, "View", self)
                    

    @property
    def table66(self):
        return self.__table66

    @table66.setter
    def table66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Table__table66", None)
        self.__table66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model67"):
                opp_val = getattr(old_value, "Model67", None)
                if opp_val == self:
                    setattr(old_value, "Model67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model67"):
                opp_val = getattr(value, "Model67", None)
                setattr(value, "Model67", self)

    @property
    def ORDB4ORA_Table(self):
        return self.__ORDB4ORA_Table

    @ORDB4ORA_Table.setter
    def ORDB4ORA_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Table__ORDB4ORA_Table", None)
        self.__ORDB4ORA_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ORDB4ORA_ForeignKey"):
                opp_val = getattr(old_value, "ORDB4ORA_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "ORDB4ORA_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ORDB4ORA_ForeignKey"):
                opp_val = getattr(value, "ORDB4ORA_ForeignKey", None)
                setattr(value, "ORDB4ORA_ForeignKey", self)

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Table__table", None)
        self.__table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Restriction62"):
                    opp_val = getattr(item, "Restriction62", None)
                    
                    if opp_val == self:
                        setattr(item, "Restriction62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Restriction62"):
                    opp_val = getattr(item, "Restriction62", None)
                    
                    setattr(item, "Restriction62", self)
                    

    @property
    def Table74(self):
        return self.__Table74

    @Table74.setter
    def Table74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Table__Table74", None)
        self.__Table74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "triggers"):
                opp_val = getattr(old_value, "triggers", None)
                if opp_val == self:
                    setattr(old_value, "triggers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "triggers"):
                opp_val = getattr(value, "triggers", None)
                setattr(value, "triggers", self)

    @property
    def Table82(self):
        return self.__Table82

    @Table82.setter
    def Table82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Table__Table82", None)
        self.__Table82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "views"):
                opp_val = getattr(old_value, "views", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "views"):
                opp_val = getattr(value, "views", None)
                if opp_val is None:
                    setattr(value, "views", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Table43(self):
        return self.__Table43

    @Table43.setter
    def Table43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Table__Table43", None)
        self.__Table43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restriction"):
                opp_val = getattr(old_value, "restriction", None)
                if opp_val == self:
                    setattr(old_value, "restriction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restriction"):
                opp_val = getattr(value, "restriction", None)
                setattr(value, "restriction", self)

    @property
    def table69(self):
        return self.__table69

    @table69.setter
    def table69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Table__table69", None)
        self.__table69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trigger"):
                    opp_val = getattr(item, "Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trigger"):
                    opp_val = getattr(item, "Trigger", None)
                    
                    setattr(item, "Trigger", self)
                    

    @property
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Table__Table", None)
        self.__Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model2"):
                opp_val = getattr(old_value, "model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model2"):
                opp_val = getattr(value, "model2", None)
                if opp_val is None:
                    setattr(value, "model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Table9(self):
        return self.__Table9

    @Table9.setter
    def Table9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Table__Table9", None)
        self.__Table9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columns"):
                opp_val = getattr(old_value, "columns", None)
                if opp_val == self:
                    setattr(old_value, "columns", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columns"):
                opp_val = getattr(value, "columns", None)
                setattr(value, "columns", self)

class ORDB4ORA_Datatype(ABC):

    pass
class SuppliedType:

    pass
class ORDB4ORA_MediaType(SuppliedType):

    def __init__(self, Descriptor: str):
        self.Descriptor = Descriptor
        
    @property
    def Descriptor(self) -> str:
        return self.__Descriptor

    @Descriptor.setter
    def Descriptor(self, Descriptor: str):
        self.__Descriptor = Descriptor

class ORDB4ORA_XMLType(SuppliedType):

    def __init__(self, Descriptor: str):
        self.Descriptor = Descriptor
        
    @property
    def Descriptor(self) -> str:
        return self.__Descriptor

    @Descriptor.setter
    def Descriptor(self, Descriptor: str):
        self.__Descriptor = Descriptor

class ORDB4ORA_SpacialType(SuppliedType):

    def __init__(self, Descriptor: str):
        self.Descriptor = Descriptor
        
    @property
    def Descriptor(self) -> str:
        return self.__Descriptor

    @Descriptor.setter
    def Descriptor(self, Descriptor: str):
        self.__Descriptor = Descriptor

class ORDB4ORA_AnyType(SuppliedType):

    def __init__(self, Descriptor: str):
        self.Descriptor = Descriptor
        
    @property
    def Descriptor(self) -> str:
        return self.__Descriptor

    @Descriptor.setter
    def Descriptor(self, Descriptor: str):
        self.__Descriptor = Descriptor

class BasicDataType:

    pass
class ORDB4ORA_SuppliedType(BasicDataType):

    pass
class ORDB4ORA_BuiltInType(BasicDataType):

    pass
class ORDB4ORA_ANSIType(BasicDataType):

    pass
class ORDB4ORA_Model:

    def __init__(self, Name: str, model: set["ORDB4ORA_Datatype"] = None, model2: set["ORDB4ORA_Table"] = None, model4: set["ORDB4ORA_Operation"] = None, model6: set["ORDB4ORA_Package"] = None, Model: "ORDB4ORA_Datatype" = None, Model28: "ORDB4ORA_Operation" = None, Model37: "ORDB4ORA_Package" = None, Model67: "ORDB4ORA_Table" = None):
        self.Name = Name
        self.model = model if model is not None else set()
        self.model2 = model2 if model2 is not None else set()
        self.model4 = model4 if model4 is not None else set()
        self.model6 = model6 if model6 is not None else set()
        self.Model = Model
        self.Model28 = Model28
        self.Model37 = Model37
        self.Model67 = Model67
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Model67(self):
        return self.__Model67

    @Model67.setter
    def Model67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Model__Model67", None)
        self.__Model67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table66"):
                opp_val = getattr(old_value, "table66", None)
                if opp_val == self:
                    setattr(old_value, "table66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table66"):
                opp_val = getattr(value, "table66", None)
                setattr(value, "table66", self)

    @property
    def Model28(self):
        return self.__Model28

    @Model28.setter
    def Model28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Model__Model28", None)
        self.__Model28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation27"):
                opp_val = getattr(old_value, "operation27", None)
                if opp_val == self:
                    setattr(old_value, "operation27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation27"):
                opp_val = getattr(value, "operation27", None)
                setattr(value, "operation27", self)

    @property
    def Model37(self):
        return self.__Model37

    @Model37.setter
    def Model37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Model__Model37", None)
        self.__Model37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package36"):
                opp_val = getattr(old_value, "package36", None)
                if opp_val == self:
                    setattr(old_value, "package36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package36"):
                opp_val = getattr(value, "package36", None)
                setattr(value, "package36", self)

    @property
    def model4(self):
        return self.__model4

    @model4.setter
    def model4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Model__model4", None)
        self.__model4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def model6(self):
        return self.__model6

    @model6.setter
    def model6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Model__model6", None)
        self.__model6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Model__model", None)
        self.__model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Datatype"):
                    opp_val = getattr(item, "Datatype", None)
                    
                    if opp_val == self:
                        setattr(item, "Datatype", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Datatype"):
                    opp_val = getattr(item, "Datatype", None)
                    
                    setattr(item, "Datatype", self)
                    

    @property
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Model__Model", None)
        self.__Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatype"):
                opp_val = getattr(old_value, "datatype", None)
                if opp_val == self:
                    setattr(old_value, "datatype", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatype"):
                opp_val = getattr(value, "datatype", None)
                setattr(value, "datatype", self)

    @property
    def model2(self):
        return self.__model2

    @model2.setter
    def model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ORDB4ORA_Model__model2", None)
        self.__model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table"):
                    opp_val = getattr(item, "Table", None)
                    
                    if opp_val == self:
                        setattr(item, "Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table"):
                    opp_val = getattr(item, "Table", None)
                    
                    setattr(item, "Table", self)
                    
