from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Charset(Enum):
    CP1257 = "CP1257"
    DEC8 = "DEC8"
    BINARY = "BINARY"
    CP850 = "CP850"
    LATIN2 = "LATIN2"
    ARMSCII8 = "ARMSCII8"
    ASCII = "ASCII"
    BIG5 = "BIG5"
    CP852 = "CP852"
    CP866 = "CP866"
    CP932 = "CP932"
    CP1250 = "CP1250"
    CP1251 = "CP1251"
    CP1256 = "CP1256"
    SWE7 = "SWE7"
    TIS620 = "TIS620"
    UCS2 = "UCS2"
    UJIS = "UJIS"
    EUCJMPS = "EUCJMPS"
    EUCKR = "EUCKR"
    GB2312 = "GB2312"
    GBK = "GBK"
    GEOSTD8 = "GEOSTD8"
    GREEK = "GREEK"
    HEBREW = "HEBREW"
    HP8 = "HP8"
    KEYBCS2 = "KEYBCS2"
    KOI8R = "KOI8R"
    KOI8U = "KOI8U"
    LATIN1 = "LATIN1"
    LATIN5 = "LATIN5"
    LATIN7 = "LATIN7"
    MACCE = "MACCE"
    MACROMAN = "MACROMAN"
    SJIS = "SJIS"
    UTF8 = "UTF8"
class FormMethod(Enum):
    GET = "GET"
    POST = "POST"
class Behavior(Enum):
    CASCADE = "CASCADE"
    RESTRICT = "RESTRICT"
class InputType(Enum):
    TEXT = "TEXT"
    BUTTON = "BUTTON"
class ColumnType(Enum):
    FLOAT = "FLOAT"
    BIT = "BIT"
    TINYBLOB = "TINYBLOB"
    BLOB = "BLOB"
    MEDIUMBLOB = "MEDIUMBLOB"
    BIGINT = "BIGINT"
    TINYINT = "TINYINT"
    MEDIUMINT = "MEDIUMINT"
    SMALLINT = "SMALLINT"
    INTEGER = "INTEGER"
    NUMERIC = "NUMERIC"
    REAL = "REAL"
    DOUBLE = "DOUBLE"
    DECIMAL = "DECIMAL"
    LONGBLOB = "LONGBLOB"
    CHAR = "CHAR"
    VARCHAR = "VARCHAR"
    BINARY = "BINARY"
    VARBINARY = "VARBINARY"
    TEXT = "TEXT"
    TINYTEXT = "TINYTEXT"
    MEDIUMTEXT = "MEDIUMTEXT"
    LONGTEXT = "LONGTEXT"
    DATE = "DATE"
    DATETIME = "DATETIME"
    TIME = "TIME"
    TIMESTAMP = "TIMESTAMP"
    YEAR = "YEAR"


############################################
# Definition of Classes
############################################

class webapp_Field:

    def __init__(self, name: str, type: str, defaultValue: str, webapp_Field: "webapp_Input" = None, webapp_Field106: "webapp_BusinessObject" = None, webapp_Field117: "webapp_BusinessObject" = None):
        self.name = name
        self.type = type
        self.defaultValue = defaultValue
        self.webapp_Field = webapp_Field
        self.webapp_Field106 = webapp_Field106
        self.webapp_Field117 = webapp_Field117
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def webapp_Field117(self):
        return self.__webapp_Field117

    @webapp_Field117.setter
    def webapp_Field117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Field__webapp_Field117", None)
        self.__webapp_Field117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_BusinessObject118"):
                opp_val = getattr(old_value, "webapp_BusinessObject118", None)
                if opp_val == self:
                    setattr(old_value, "webapp_BusinessObject118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_BusinessObject118"):
                opp_val = getattr(value, "webapp_BusinessObject118", None)
                setattr(value, "webapp_BusinessObject118", self)

    @property
    def webapp_Field(self):
        return self.__webapp_Field

    @webapp_Field.setter
    def webapp_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Field__webapp_Field", None)
        self.__webapp_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Input92"):
                opp_val = getattr(old_value, "webapp_Input92", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Input92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Input92"):
                opp_val = getattr(value, "webapp_Input92", None)
                setattr(value, "webapp_Input92", self)

    @property
    def webapp_Field106(self):
        return self.__webapp_Field106

    @webapp_Field106.setter
    def webapp_Field106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Field__webapp_Field106", None)
        self.__webapp_Field106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_BusinessObject105"):
                opp_val = getattr(old_value, "webapp_BusinessObject105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_BusinessObject105"):
                opp_val = getattr(value, "webapp_BusinessObject105", None)
                if opp_val is None:
                    setattr(value, "webapp_BusinessObject105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_Attribute:

    def __init__(self, name: str, value: str, webapp_Attribute: "webapp_Tag" = None):
        self.name = name
        self.value = value
        self.webapp_Attribute = webapp_Attribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def webapp_Attribute(self):
        return self.__webapp_Attribute

    @webapp_Attribute.setter
    def webapp_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Attribute__webapp_Attribute", None)
        self.__webapp_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Tag82"):
                opp_val = getattr(old_value, "webapp_Tag82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Tag82"):
                opp_val = getattr(value, "webapp_Tag82", None)
                if opp_val is None:
                    setattr(value, "webapp_Tag82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Tag:

    pass
class webapp_Input(Tag):

    def __init__(self, type: str, webapp_Input: "webapp_Action" = None, webapp_Input86: "webapp_Mapping" = None, webapp_Input89: "webapp_Mapping" = None, webapp_Input92: "webapp_Field" = None, webapp_Input94: "webapp_Validator" = None):
        self.type = type
        self.webapp_Input = webapp_Input
        self.webapp_Input86 = webapp_Input86
        self.webapp_Input89 = webapp_Input89
        self.webapp_Input92 = webapp_Input92
        self.webapp_Input94 = webapp_Input94
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def webapp_Input86(self):
        return self.__webapp_Input86

    @webapp_Input86.setter
    def webapp_Input86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Input__webapp_Input86", None)
        self.__webapp_Input86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Mapping87"):
                opp_val = getattr(old_value, "webapp_Mapping87", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Mapping87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Mapping87"):
                opp_val = getattr(value, "webapp_Mapping87", None)
                setattr(value, "webapp_Mapping87", self)

    @property
    def webapp_Input94(self):
        return self.__webapp_Input94

    @webapp_Input94.setter
    def webapp_Input94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Input__webapp_Input94", None)
        self.__webapp_Input94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Validator95"):
                opp_val = getattr(old_value, "webapp_Validator95", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Validator95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Validator95"):
                opp_val = getattr(value, "webapp_Validator95", None)
                setattr(value, "webapp_Validator95", self)

    @property
    def webapp_Input92(self):
        return self.__webapp_Input92

    @webapp_Input92.setter
    def webapp_Input92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Input__webapp_Input92", None)
        self.__webapp_Input92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Field"):
                opp_val = getattr(old_value, "webapp_Field", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Field", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Field"):
                opp_val = getattr(value, "webapp_Field", None)
                setattr(value, "webapp_Field", self)

    @property
    def webapp_Input(self):
        return self.__webapp_Input

    @webapp_Input.setter
    def webapp_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Input__webapp_Input", None)
        self.__webapp_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Action84"):
                opp_val = getattr(old_value, "webapp_Action84", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Action84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Action84"):
                opp_val = getattr(value, "webapp_Action84", None)
                setattr(value, "webapp_Action84", self)

    @property
    def webapp_Input89(self):
        return self.__webapp_Input89

    @webapp_Input89.setter
    def webapp_Input89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Input__webapp_Input89", None)
        self.__webapp_Input89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Mapping90"):
                opp_val = getattr(old_value, "webapp_Mapping90", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Mapping90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Mapping90"):
                opp_val = getattr(value, "webapp_Mapping90", None)
                setattr(value, "webapp_Mapping90", self)

class webapp_Th(Tag):

    pass
class webapp_Td(Tag):

    pass
class webapp_Messages(Tag):

    pass
class webapp_TableHTML(Tag):

    pass
class webapp_Tr(Tag):

    pass
class webapp_Form(Tag):

    def __init__(self, method: str, webapp_Form: set["webapp_Tag"] = None):
        self.method = method
        self.webapp_Form = webapp_Form if webapp_Form is not None else set()
        
    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def webapp_Form(self):
        return self.__webapp_Form

    @webapp_Form.setter
    def webapp_Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Form__webapp_Form", None)
        self.__webapp_Form = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Tag"):
                    opp_val = getattr(item, "webapp_Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Tag"):
                    opp_val = getattr(item, "webapp_Tag", None)
                    
                    setattr(item, "webapp_Tag", self)
                    

class webapp_Instruction:

    pass
class Instruction:

    pass
class webapp_Tag(Instruction):

    def __init__(self, property: str, webapp_Tag: "webapp_Form" = None, webapp_Tag82: set["webapp_Attribute"] = None, webapp_Tag103: "webapp_Td" = None):
        self.property = property
        self.webapp_Tag = webapp_Tag
        self.webapp_Tag82 = webapp_Tag82 if webapp_Tag82 is not None else set()
        self.webapp_Tag103 = webapp_Tag103
        
    @property
    def property(self) -> str:
        return self.__property

    @property.setter
    def property(self, property: str):
        self.__property = property

    @property
    def webapp_Tag(self):
        return self.__webapp_Tag

    @webapp_Tag.setter
    def webapp_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Tag__webapp_Tag", None)
        self.__webapp_Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Form"):
                opp_val = getattr(old_value, "webapp_Form", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Form"):
                opp_val = getattr(value, "webapp_Form", None)
                if opp_val is None:
                    setattr(value, "webapp_Form", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Tag82(self):
        return self.__webapp_Tag82

    @webapp_Tag82.setter
    def webapp_Tag82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Tag__webapp_Tag82", None)
        self.__webapp_Tag82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Attribute"):
                    opp_val = getattr(item, "webapp_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Attribute"):
                    opp_val = getattr(item, "webapp_Attribute", None)
                    
                    setattr(item, "webapp_Attribute", self)
                    

    @property
    def webapp_Tag103(self):
        return self.__webapp_Tag103

    @webapp_Tag103.setter
    def webapp_Tag103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Tag__webapp_Tag103", None)
        self.__webapp_Tag103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Td102"):
                opp_val = getattr(old_value, "webapp_Td102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Td102"):
                opp_val = getattr(value, "webapp_Td102", None)
                if opp_val is None:
                    setattr(value, "webapp_Td102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_Text(Instruction):

    def __init__(self, content: str):
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class webapp_OnUpdate:

    def __init__(self, behavior: str, webapp_OnUpdate: "webapp_ForeignKey" = None):
        self.behavior = behavior
        self.webapp_OnUpdate = webapp_OnUpdate
        
    @property
    def behavior(self) -> str:
        return self.__behavior

    @behavior.setter
    def behavior(self, behavior: str):
        self.__behavior = behavior

    @property
    def webapp_OnUpdate(self):
        return self.__webapp_OnUpdate

    @webapp_OnUpdate.setter
    def webapp_OnUpdate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_OnUpdate__webapp_OnUpdate", None)
        self.__webapp_OnUpdate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_ForeignKey56"):
                opp_val = getattr(old_value, "webapp_ForeignKey56", None)
                if opp_val == self:
                    setattr(old_value, "webapp_ForeignKey56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_ForeignKey56"):
                opp_val = getattr(value, "webapp_ForeignKey56", None)
                setattr(value, "webapp_ForeignKey56", self)

class webapp_OnDelete:

    def __init__(self, behavior: str, webapp_OnDelete: "webapp_ForeignKey" = None):
        self.behavior = behavior
        self.webapp_OnDelete = webapp_OnDelete
        
    @property
    def behavior(self) -> str:
        return self.__behavior

    @behavior.setter
    def behavior(self, behavior: str):
        self.__behavior = behavior

    @property
    def webapp_OnDelete(self):
        return self.__webapp_OnDelete

    @webapp_OnDelete.setter
    def webapp_OnDelete(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_OnDelete__webapp_OnDelete", None)
        self.__webapp_OnDelete = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_ForeignKey54"):
                opp_val = getattr(old_value, "webapp_ForeignKey54", None)
                if opp_val == self:
                    setattr(old_value, "webapp_ForeignKey54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_ForeignKey54"):
                opp_val = getattr(value, "webapp_ForeignKey54", None)
                setattr(value, "webapp_ForeignKey54", self)

class webapp_ForeignKey:

    pass
class webapp_Check:

    def __init__(self, expr: str, webapp_Check: "webapp_Constraint" = None):
        self.expr = expr
        self.webapp_Check = webapp_Check
        
    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def webapp_Check(self):
        return self.__webapp_Check

    @webapp_Check.setter
    def webapp_Check(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Check__webapp_Check", None)
        self.__webapp_Check = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Constraint44"):
                opp_val = getattr(old_value, "webapp_Constraint44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Constraint44"):
                opp_val = getattr(value, "webapp_Constraint44", None)
                if opp_val is None:
                    setattr(value, "webapp_Constraint44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_Unique:

    pass
class webapp_PrimaryKey:

    pass
class webapp_Detail:

    def __init__(self, precision: int, scale: int, webapp_Detail: "webapp_Column" = None):
        self.precision = precision
        self.scale = scale
        self.webapp_Detail = webapp_Detail
        
    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def webapp_Detail(self):
        return self.__webapp_Detail

    @webapp_Detail.setter
    def webapp_Detail(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Detail__webapp_Detail", None)
        self.__webapp_Detail = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Column38"):
                opp_val = getattr(old_value, "webapp_Column38", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Column38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Column38"):
                opp_val = getattr(value, "webapp_Column38", None)
                setattr(value, "webapp_Column38", self)

class webapp_Column:

    def __init__(self, type: str, defaultValue: str, name: str, isNotNull: bool, size: int, useZeroFill: bool, webapp_Column: "webapp_Table" = None, webapp_Column38: "webapp_Detail" = None, webapp_Column49: "webapp_PrimaryKey" = None, webapp_Column52: "webapp_ForeignKey" = None, webapp_Column62: "webapp_ForeignKey" = None, webapp_Column65: "webapp_Unique" = None):
        self.type = type
        self.defaultValue = defaultValue
        self.name = name
        self.isNotNull = isNotNull
        self.size = size
        self.useZeroFill = useZeroFill
        self.webapp_Column = webapp_Column
        self.webapp_Column38 = webapp_Column38
        self.webapp_Column49 = webapp_Column49
        self.webapp_Column52 = webapp_Column52
        self.webapp_Column62 = webapp_Column62
        self.webapp_Column65 = webapp_Column65
        
    @property
    def isNotNull(self) -> bool:
        return self.__isNotNull

    @isNotNull.setter
    def isNotNull(self, isNotNull: bool):
        self.__isNotNull = isNotNull

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def useZeroFill(self) -> bool:
        return self.__useZeroFill

    @useZeroFill.setter
    def useZeroFill(self, useZeroFill: bool):
        self.__useZeroFill = useZeroFill

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def webapp_Column65(self):
        return self.__webapp_Column65

    @webapp_Column65.setter
    def webapp_Column65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Column__webapp_Column65", None)
        self.__webapp_Column65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Unique64"):
                opp_val = getattr(old_value, "webapp_Unique64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Unique64"):
                opp_val = getattr(value, "webapp_Unique64", None)
                if opp_val is None:
                    setattr(value, "webapp_Unique64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Column52(self):
        return self.__webapp_Column52

    @webapp_Column52.setter
    def webapp_Column52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Column__webapp_Column52", None)
        self.__webapp_Column52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_ForeignKey51"):
                opp_val = getattr(old_value, "webapp_ForeignKey51", None)
                if opp_val == self:
                    setattr(old_value, "webapp_ForeignKey51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_ForeignKey51"):
                opp_val = getattr(value, "webapp_ForeignKey51", None)
                setattr(value, "webapp_ForeignKey51", self)

    @property
    def webapp_Column49(self):
        return self.__webapp_Column49

    @webapp_Column49.setter
    def webapp_Column49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Column__webapp_Column49", None)
        self.__webapp_Column49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_PrimaryKey48"):
                opp_val = getattr(old_value, "webapp_PrimaryKey48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_PrimaryKey48"):
                opp_val = getattr(value, "webapp_PrimaryKey48", None)
                if opp_val is None:
                    setattr(value, "webapp_PrimaryKey48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Column(self):
        return self.__webapp_Column

    @webapp_Column.setter
    def webapp_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Column__webapp_Column", None)
        self.__webapp_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Table34"):
                opp_val = getattr(old_value, "webapp_Table34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Table34"):
                opp_val = getattr(value, "webapp_Table34", None)
                if opp_val is None:
                    setattr(value, "webapp_Table34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Column38(self):
        return self.__webapp_Column38

    @webapp_Column38.setter
    def webapp_Column38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Column__webapp_Column38", None)
        self.__webapp_Column38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Detail"):
                opp_val = getattr(old_value, "webapp_Detail", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Detail", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Detail"):
                opp_val = getattr(value, "webapp_Detail", None)
                setattr(value, "webapp_Detail", self)

    @property
    def webapp_Column62(self):
        return self.__webapp_Column62

    @webapp_Column62.setter
    def webapp_Column62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Column__webapp_Column62", None)
        self.__webapp_Column62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_ForeignKey61"):
                opp_val = getattr(old_value, "webapp_ForeignKey61", None)
                if opp_val == self:
                    setattr(old_value, "webapp_ForeignKey61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_ForeignKey61"):
                opp_val = getattr(value, "webapp_ForeignKey61", None)
                setattr(value, "webapp_ForeignKey61", self)

class webapp_Mapping:

    def __init__(self, left: str, right: str, webapp_Mapping: "webapp_Properties" = None, webapp_Mapping74: "webapp_Page" = None, webapp_Mapping87: "webapp_Input" = None, webapp_Mapping90: "webapp_Input" = None):
        self.left = left
        self.right = right
        self.webapp_Mapping = webapp_Mapping
        self.webapp_Mapping74 = webapp_Mapping74
        self.webapp_Mapping87 = webapp_Mapping87
        self.webapp_Mapping90 = webapp_Mapping90
        
    @property
    def right(self) -> str:
        return self.__right

    @right.setter
    def right(self, right: str):
        self.__right = right

    @property
    def left(self) -> str:
        return self.__left

    @left.setter
    def left(self, left: str):
        self.__left = left

    @property
    def webapp_Mapping87(self):
        return self.__webapp_Mapping87

    @webapp_Mapping87.setter
    def webapp_Mapping87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Mapping__webapp_Mapping87", None)
        self.__webapp_Mapping87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Input86"):
                opp_val = getattr(old_value, "webapp_Input86", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Input86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Input86"):
                opp_val = getattr(value, "webapp_Input86", None)
                setattr(value, "webapp_Input86", self)

    @property
    def webapp_Mapping74(self):
        return self.__webapp_Mapping74

    @webapp_Mapping74.setter
    def webapp_Mapping74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Mapping__webapp_Mapping74", None)
        self.__webapp_Mapping74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Page73"):
                opp_val = getattr(old_value, "webapp_Page73", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Page73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Page73"):
                opp_val = getattr(value, "webapp_Page73", None)
                setattr(value, "webapp_Page73", self)

    @property
    def webapp_Mapping90(self):
        return self.__webapp_Mapping90

    @webapp_Mapping90.setter
    def webapp_Mapping90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Mapping__webapp_Mapping90", None)
        self.__webapp_Mapping90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Input89"):
                opp_val = getattr(old_value, "webapp_Input89", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Input89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Input89"):
                opp_val = getattr(value, "webapp_Input89", None)
                setattr(value, "webapp_Input89", self)

    @property
    def webapp_Mapping(self):
        return self.__webapp_Mapping

    @webapp_Mapping.setter
    def webapp_Mapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Mapping__webapp_Mapping", None)
        self.__webapp_Mapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Properties32"):
                opp_val = getattr(old_value, "webapp_Properties32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Properties32"):
                opp_val = getattr(value, "webapp_Properties32", None)
                if opp_val is None:
                    setattr(value, "webapp_Properties32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_Properties:

    def __init__(self, name: str, package: str, webapp_Properties: "webapp_Resource" = None, webapp_Properties32: set["webapp_Mapping"] = None, webapp_Properties71: "webapp_Page" = None):
        self.name = name
        self.package = package
        self.webapp_Properties = webapp_Properties
        self.webapp_Properties32 = webapp_Properties32 if webapp_Properties32 is not None else set()
        self.webapp_Properties71 = webapp_Properties71
        
    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def webapp_Properties(self):
        return self.__webapp_Properties

    @webapp_Properties.setter
    def webapp_Properties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Properties__webapp_Properties", None)
        self.__webapp_Properties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Resource30"):
                opp_val = getattr(old_value, "webapp_Resource30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Resource30"):
                opp_val = getattr(value, "webapp_Resource30", None)
                if opp_val is None:
                    setattr(value, "webapp_Resource30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Properties32(self):
        return self.__webapp_Properties32

    @webapp_Properties32.setter
    def webapp_Properties32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Properties__webapp_Properties32", None)
        self.__webapp_Properties32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Mapping"):
                    opp_val = getattr(item, "webapp_Mapping", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Mapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Mapping"):
                    opp_val = getattr(item, "webapp_Mapping", None)
                    
                    setattr(item, "webapp_Mapping", self)
                    

    @property
    def webapp_Properties71(self):
        return self.__webapp_Properties71

    @webapp_Properties71.setter
    def webapp_Properties71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Properties__webapp_Properties71", None)
        self.__webapp_Properties71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Page70"):
                opp_val = getattr(old_value, "webapp_Page70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Page70"):
                opp_val = getattr(value, "webapp_Page70", None)
                if opp_val is None:
                    setattr(value, "webapp_Page70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_Constraint:

    pass
class webapp_Action:

    def __init__(self, name: str, returnType: str, webapp_Action: "webapp_Controller" = None, webapp_Action79: "webapp_BusinessObject" = None, webapp_Action84: "webapp_Input" = None, webapp_Action109: "webapp_BusinessObject" = None):
        self.name = name
        self.returnType = returnType
        self.webapp_Action = webapp_Action
        self.webapp_Action79 = webapp_Action79
        self.webapp_Action84 = webapp_Action84
        self.webapp_Action109 = webapp_Action109
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def webapp_Action79(self):
        return self.__webapp_Action79

    @webapp_Action79.setter
    def webapp_Action79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Action__webapp_Action79", None)
        self.__webapp_Action79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_BusinessObject80"):
                opp_val = getattr(old_value, "webapp_BusinessObject80", None)
                if opp_val == self:
                    setattr(old_value, "webapp_BusinessObject80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_BusinessObject80"):
                opp_val = getattr(value, "webapp_BusinessObject80", None)
                setattr(value, "webapp_BusinessObject80", self)

    @property
    def webapp_Action109(self):
        return self.__webapp_Action109

    @webapp_Action109.setter
    def webapp_Action109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Action__webapp_Action109", None)
        self.__webapp_Action109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_BusinessObject108"):
                opp_val = getattr(old_value, "webapp_BusinessObject108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_BusinessObject108"):
                opp_val = getattr(value, "webapp_BusinessObject108", None)
                if opp_val is None:
                    setattr(value, "webapp_BusinessObject108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Action(self):
        return self.__webapp_Action

    @webapp_Action.setter
    def webapp_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Action__webapp_Action", None)
        self.__webapp_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Controller24"):
                opp_val = getattr(old_value, "webapp_Controller24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Controller24"):
                opp_val = getattr(value, "webapp_Controller24", None)
                if opp_val is None:
                    setattr(value, "webapp_Controller24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Action84(self):
        return self.__webapp_Action84

    @webapp_Action84.setter
    def webapp_Action84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Action__webapp_Action84", None)
        self.__webapp_Action84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Input"):
                opp_val = getattr(old_value, "webapp_Input", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Input", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Input"):
                opp_val = getattr(value, "webapp_Input", None)
                setattr(value, "webapp_Input", self)

class webapp_Validator:

    def __init__(self, package: str, name: str, webapp_Validator: "webapp_Controller" = None, webapp_Validator67: "webapp_Page" = None, webapp_Validator95: "webapp_Input" = None):
        self.package = package
        self.name = name
        self.webapp_Validator = webapp_Validator
        self.webapp_Validator67 = webapp_Validator67
        self.webapp_Validator95 = webapp_Validator95
        
    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def webapp_Validator95(self):
        return self.__webapp_Validator95

    @webapp_Validator95.setter
    def webapp_Validator95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Validator__webapp_Validator95", None)
        self.__webapp_Validator95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Input94"):
                opp_val = getattr(old_value, "webapp_Input94", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Input94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Input94"):
                opp_val = getattr(value, "webapp_Input94", None)
                setattr(value, "webapp_Input94", self)

    @property
    def webapp_Validator(self):
        return self.__webapp_Validator

    @webapp_Validator.setter
    def webapp_Validator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Validator__webapp_Validator", None)
        self.__webapp_Validator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Controller22"):
                opp_val = getattr(old_value, "webapp_Controller22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Controller22"):
                opp_val = getattr(value, "webapp_Controller22", None)
                if opp_val is None:
                    setattr(value, "webapp_Controller22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Validator67(self):
        return self.__webapp_Validator67

    @webapp_Validator67.setter
    def webapp_Validator67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Validator__webapp_Validator67", None)
        self.__webapp_Validator67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Page68"):
                opp_val = getattr(old_value, "webapp_Page68", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Page68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Page68"):
                opp_val = getattr(value, "webapp_Page68", None)
                setattr(value, "webapp_Page68", self)

class webapp_BusinessObject:

    def __init__(self, name: str, package: str, webapp_BusinessObject: "webapp_Model" = None, webapp_BusinessObject80: "webapp_Action" = None, webapp_BusinessObject105: set["webapp_Field"] = None, webapp_BusinessObject108: set["webapp_Action"] = None, webapp_BusinessObject112: "webapp_BusinessObject" = None, webapp_BusinessObject110: set["webapp_BusinessObject"] = None, webapp_BusinessObject114: "webapp_Model" = None, webapp_BusinessObject118: "webapp_Field" = None):
        self.name = name
        self.package = package
        self.webapp_BusinessObject = webapp_BusinessObject
        self.webapp_BusinessObject80 = webapp_BusinessObject80
        self.webapp_BusinessObject105 = webapp_BusinessObject105 if webapp_BusinessObject105 is not None else set()
        self.webapp_BusinessObject108 = webapp_BusinessObject108 if webapp_BusinessObject108 is not None else set()
        self.webapp_BusinessObject112 = webapp_BusinessObject112
        self.webapp_BusinessObject110 = webapp_BusinessObject110 if webapp_BusinessObject110 is not None else set()
        self.webapp_BusinessObject114 = webapp_BusinessObject114
        self.webapp_BusinessObject118 = webapp_BusinessObject118
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def webapp_BusinessObject(self):
        return self.__webapp_BusinessObject

    @webapp_BusinessObject.setter
    def webapp_BusinessObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_BusinessObject__webapp_BusinessObject", None)
        self.__webapp_BusinessObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Model20"):
                opp_val = getattr(old_value, "webapp_Model20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Model20"):
                opp_val = getattr(value, "webapp_Model20", None)
                if opp_val is None:
                    setattr(value, "webapp_Model20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_BusinessObject114(self):
        return self.__webapp_BusinessObject114

    @webapp_BusinessObject114.setter
    def webapp_BusinessObject114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_BusinessObject__webapp_BusinessObject114", None)
        self.__webapp_BusinessObject114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Model115"):
                opp_val = getattr(old_value, "webapp_Model115", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Model115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Model115"):
                opp_val = getattr(value, "webapp_Model115", None)
                setattr(value, "webapp_Model115", self)

    @property
    def webapp_BusinessObject110(self):
        return self.__webapp_BusinessObject110

    @webapp_BusinessObject110.setter
    def webapp_BusinessObject110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_BusinessObject__webapp_BusinessObject110", None)
        self.__webapp_BusinessObject110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_BusinessObject112"):
                    opp_val = getattr(item, "webapp_BusinessObject112", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_BusinessObject112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_BusinessObject112"):
                    opp_val = getattr(item, "webapp_BusinessObject112", None)
                    
                    setattr(item, "webapp_BusinessObject112", self)
                    

    @property
    def webapp_BusinessObject118(self):
        return self.__webapp_BusinessObject118

    @webapp_BusinessObject118.setter
    def webapp_BusinessObject118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_BusinessObject__webapp_BusinessObject118", None)
        self.__webapp_BusinessObject118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Field117"):
                opp_val = getattr(old_value, "webapp_Field117", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Field117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Field117"):
                opp_val = getattr(value, "webapp_Field117", None)
                setattr(value, "webapp_Field117", self)

    @property
    def webapp_BusinessObject80(self):
        return self.__webapp_BusinessObject80

    @webapp_BusinessObject80.setter
    def webapp_BusinessObject80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_BusinessObject__webapp_BusinessObject80", None)
        self.__webapp_BusinessObject80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Action79"):
                opp_val = getattr(old_value, "webapp_Action79", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Action79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Action79"):
                opp_val = getattr(value, "webapp_Action79", None)
                setattr(value, "webapp_Action79", self)

    @property
    def webapp_BusinessObject112(self):
        return self.__webapp_BusinessObject112

    @webapp_BusinessObject112.setter
    def webapp_BusinessObject112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_BusinessObject__webapp_BusinessObject112", None)
        self.__webapp_BusinessObject112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_BusinessObject110"):
                opp_val = getattr(old_value, "webapp_BusinessObject110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_BusinessObject110"):
                opp_val = getattr(value, "webapp_BusinessObject110", None)
                if opp_val is None:
                    setattr(value, "webapp_BusinessObject110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_BusinessObject105(self):
        return self.__webapp_BusinessObject105

    @webapp_BusinessObject105.setter
    def webapp_BusinessObject105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_BusinessObject__webapp_BusinessObject105", None)
        self.__webapp_BusinessObject105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Field106"):
                    opp_val = getattr(item, "webapp_Field106", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Field106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Field106"):
                    opp_val = getattr(item, "webapp_Field106", None)
                    
                    setattr(item, "webapp_Field106", self)
                    

    @property
    def webapp_BusinessObject108(self):
        return self.__webapp_BusinessObject108

    @webapp_BusinessObject108.setter
    def webapp_BusinessObject108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_BusinessObject__webapp_BusinessObject108", None)
        self.__webapp_BusinessObject108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Action109"):
                    opp_val = getattr(item, "webapp_Action109", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Action109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Action109"):
                    opp_val = getattr(item, "webapp_Action109", None)
                    
                    setattr(item, "webapp_Action109", self)
                    

class webapp_File:

    pass
class webapp_Image:

    pass
class webapp_Table:

    def __init__(self, name: str, charset: str, webapp_Table: "webapp_Model" = None, webapp_Table36: "webapp_Constraint" = None, webapp_Table34: set["webapp_Column"] = None, webapp_Table59: "webapp_ForeignKey" = None):
        self.name = name
        self.charset = charset
        self.webapp_Table = webapp_Table
        self.webapp_Table36 = webapp_Table36
        self.webapp_Table34 = webapp_Table34 if webapp_Table34 is not None else set()
        self.webapp_Table59 = webapp_Table59
        
    @property
    def charset(self) -> str:
        return self.__charset

    @charset.setter
    def charset(self, charset: str):
        self.__charset = charset

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def webapp_Table59(self):
        return self.__webapp_Table59

    @webapp_Table59.setter
    def webapp_Table59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Table__webapp_Table59", None)
        self.__webapp_Table59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_ForeignKey58"):
                opp_val = getattr(old_value, "webapp_ForeignKey58", None)
                if opp_val == self:
                    setattr(old_value, "webapp_ForeignKey58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_ForeignKey58"):
                opp_val = getattr(value, "webapp_ForeignKey58", None)
                setattr(value, "webapp_ForeignKey58", self)

    @property
    def webapp_Table34(self):
        return self.__webapp_Table34

    @webapp_Table34.setter
    def webapp_Table34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Table__webapp_Table34", None)
        self.__webapp_Table34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Column"):
                    opp_val = getattr(item, "webapp_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Column"):
                    opp_val = getattr(item, "webapp_Column", None)
                    
                    setattr(item, "webapp_Column", self)
                    

    @property
    def webapp_Table36(self):
        return self.__webapp_Table36

    @webapp_Table36.setter
    def webapp_Table36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Table__webapp_Table36", None)
        self.__webapp_Table36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Constraint"):
                opp_val = getattr(old_value, "webapp_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Constraint"):
                opp_val = getattr(value, "webapp_Constraint", None)
                setattr(value, "webapp_Constraint", self)

    @property
    def webapp_Table(self):
        return self.__webapp_Table

    @webapp_Table.setter
    def webapp_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Table__webapp_Table", None)
        self.__webapp_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Model18"):
                opp_val = getattr(old_value, "webapp_Model18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Model18"):
                opp_val = getattr(value, "webapp_Model18", None)
                if opp_val is None:
                    setattr(value, "webapp_Model18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_Navigation:

    def __init__(self, message: str, webapp_Navigation: "webapp_View" = None, webapp_Navigation123: "webapp_Page" = None, webapp_Navigation120: "webapp_Page" = None):
        self.message = message
        self.webapp_Navigation = webapp_Navigation
        self.webapp_Navigation123 = webapp_Navigation123
        self.webapp_Navigation120 = webapp_Navigation120
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def webapp_Navigation(self):
        return self.__webapp_Navigation

    @webapp_Navigation.setter
    def webapp_Navigation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Navigation__webapp_Navigation", None)
        self.__webapp_Navigation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_View16"):
                opp_val = getattr(old_value, "webapp_View16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_View16"):
                opp_val = getattr(value, "webapp_View16", None)
                if opp_val is None:
                    setattr(value, "webapp_View16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Navigation120(self):
        return self.__webapp_Navigation120

    @webapp_Navigation120.setter
    def webapp_Navigation120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Navigation__webapp_Navigation120", None)
        self.__webapp_Navigation120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Page121"):
                opp_val = getattr(old_value, "webapp_Page121", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Page121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Page121"):
                opp_val = getattr(value, "webapp_Page121", None)
                setattr(value, "webapp_Page121", self)

    @property
    def webapp_Navigation123(self):
        return self.__webapp_Navigation123

    @webapp_Navigation123.setter
    def webapp_Navigation123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Navigation__webapp_Navigation123", None)
        self.__webapp_Navigation123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Page124"):
                opp_val = getattr(old_value, "webapp_Page124", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Page124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Page124"):
                opp_val = getattr(value, "webapp_Page124", None)
                setattr(value, "webapp_Page124", self)

class webapp_Page:

    def __init__(self, name: str, isMain: bool, webapp_Page: "webapp_View" = None, webapp_Page68: "webapp_Validator" = None, webapp_Page70: set["webapp_Properties"] = None, webapp_Page73: "webapp_Mapping" = None, webapp_Page76: set["webapp_Instruction"] = None, webapp_Page124: "webapp_Navigation" = None, webapp_Page121: "webapp_Navigation" = None):
        self.name = name
        self.isMain = isMain
        self.webapp_Page = webapp_Page
        self.webapp_Page68 = webapp_Page68
        self.webapp_Page70 = webapp_Page70 if webapp_Page70 is not None else set()
        self.webapp_Page73 = webapp_Page73
        self.webapp_Page76 = webapp_Page76 if webapp_Page76 is not None else set()
        self.webapp_Page124 = webapp_Page124
        self.webapp_Page121 = webapp_Page121
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isMain(self) -> bool:
        return self.__isMain

    @isMain.setter
    def isMain(self, isMain: bool):
        self.__isMain = isMain

    @property
    def webapp_Page121(self):
        return self.__webapp_Page121

    @webapp_Page121.setter
    def webapp_Page121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Page__webapp_Page121", None)
        self.__webapp_Page121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Navigation120"):
                opp_val = getattr(old_value, "webapp_Navigation120", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Navigation120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Navigation120"):
                opp_val = getattr(value, "webapp_Navigation120", None)
                setattr(value, "webapp_Navigation120", self)

    @property
    def webapp_Page68(self):
        return self.__webapp_Page68

    @webapp_Page68.setter
    def webapp_Page68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Page__webapp_Page68", None)
        self.__webapp_Page68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Validator67"):
                opp_val = getattr(old_value, "webapp_Validator67", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Validator67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Validator67"):
                opp_val = getattr(value, "webapp_Validator67", None)
                setattr(value, "webapp_Validator67", self)

    @property
    def webapp_Page76(self):
        return self.__webapp_Page76

    @webapp_Page76.setter
    def webapp_Page76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Page__webapp_Page76", None)
        self.__webapp_Page76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Instruction"):
                    opp_val = getattr(item, "webapp_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Instruction"):
                    opp_val = getattr(item, "webapp_Instruction", None)
                    
                    setattr(item, "webapp_Instruction", self)
                    

    @property
    def webapp_Page73(self):
        return self.__webapp_Page73

    @webapp_Page73.setter
    def webapp_Page73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Page__webapp_Page73", None)
        self.__webapp_Page73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Mapping74"):
                opp_val = getattr(old_value, "webapp_Mapping74", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Mapping74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Mapping74"):
                opp_val = getattr(value, "webapp_Mapping74", None)
                setattr(value, "webapp_Mapping74", self)

    @property
    def webapp_Page(self):
        return self.__webapp_Page

    @webapp_Page.setter
    def webapp_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Page__webapp_Page", None)
        self.__webapp_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_View14"):
                opp_val = getattr(old_value, "webapp_View14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_View14"):
                opp_val = getattr(value, "webapp_View14", None)
                if opp_val is None:
                    setattr(value, "webapp_View14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_Page70(self):
        return self.__webapp_Page70

    @webapp_Page70.setter
    def webapp_Page70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Page__webapp_Page70", None)
        self.__webapp_Page70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Properties71"):
                    opp_val = getattr(item, "webapp_Properties71", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Properties71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Properties71"):
                    opp_val = getattr(item, "webapp_Properties71", None)
                    
                    setattr(item, "webapp_Properties71", self)
                    

    @property
    def webapp_Page124(self):
        return self.__webapp_Page124

    @webapp_Page124.setter
    def webapp_Page124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Page__webapp_Page124", None)
        self.__webapp_Page124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Navigation123"):
                opp_val = getattr(old_value, "webapp_Navigation123", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Navigation123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Navigation123"):
                opp_val = getattr(value, "webapp_Navigation123", None)
                setattr(value, "webapp_Navigation123", self)

class webapp_Model:

    def __init__(self, databaseName: str, url: str, userName: str, password: str, webapp_Model: "webapp_WebApp" = None, webapp_Model18: set["webapp_Table"] = None, webapp_Model20: set["webapp_BusinessObject"] = None, webapp_Model115: "webapp_BusinessObject" = None):
        self.databaseName = databaseName
        self.url = url
        self.userName = userName
        self.password = password
        self.webapp_Model = webapp_Model
        self.webapp_Model18 = webapp_Model18 if webapp_Model18 is not None else set()
        self.webapp_Model20 = webapp_Model20 if webapp_Model20 is not None else set()
        self.webapp_Model115 = webapp_Model115
        
    @property
    def databaseName(self) -> str:
        return self.__databaseName

    @databaseName.setter
    def databaseName(self, databaseName: str):
        self.__databaseName = databaseName

    @property
    def userName(self) -> str:
        return self.__userName

    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def webapp_Model18(self):
        return self.__webapp_Model18

    @webapp_Model18.setter
    def webapp_Model18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Model__webapp_Model18", None)
        self.__webapp_Model18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Table"):
                    opp_val = getattr(item, "webapp_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Table"):
                    opp_val = getattr(item, "webapp_Table", None)
                    
                    setattr(item, "webapp_Table", self)
                    

    @property
    def webapp_Model(self):
        return self.__webapp_Model

    @webapp_Model.setter
    def webapp_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Model__webapp_Model", None)
        self.__webapp_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_WebApp8"):
                opp_val = getattr(old_value, "webapp_WebApp8", None)
                if opp_val == self:
                    setattr(old_value, "webapp_WebApp8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_WebApp8"):
                opp_val = getattr(value, "webapp_WebApp8", None)
                setattr(value, "webapp_WebApp8", self)

    @property
    def webapp_Model115(self):
        return self.__webapp_Model115

    @webapp_Model115.setter
    def webapp_Model115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Model__webapp_Model115", None)
        self.__webapp_Model115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_BusinessObject114"):
                opp_val = getattr(old_value, "webapp_BusinessObject114", None)
                if opp_val == self:
                    setattr(old_value, "webapp_BusinessObject114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_BusinessObject114"):
                opp_val = getattr(value, "webapp_BusinessObject114", None)
                setattr(value, "webapp_BusinessObject114", self)

    @property
    def webapp_Model20(self):
        return self.__webapp_Model20

    @webapp_Model20.setter
    def webapp_Model20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Model__webapp_Model20", None)
        self.__webapp_Model20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_BusinessObject"):
                    opp_val = getattr(item, "webapp_BusinessObject", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_BusinessObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_BusinessObject"):
                    opp_val = getattr(item, "webapp_BusinessObject", None)
                    
                    setattr(item, "webapp_BusinessObject", self)
                    

class webapp_View:

    pass
class webapp_Library:

    pass
class webapp_WebConfig:

    def __init__(self, displayName: str, webapp_WebConfig: "webapp_WebApp" = None):
        self.displayName = displayName
        self.webapp_WebConfig = webapp_WebConfig
        
    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def webapp_WebConfig(self):
        return self.__webapp_WebConfig

    @webapp_WebConfig.setter
    def webapp_WebConfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_WebConfig__webapp_WebConfig", None)
        self.__webapp_WebConfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_WebApp2"):
                opp_val = getattr(old_value, "webapp_WebApp2", None)
                if opp_val == self:
                    setattr(old_value, "webapp_WebApp2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_WebApp2"):
                opp_val = getattr(value, "webapp_WebApp2", None)
                setattr(value, "webapp_WebApp2", self)

class webapp_AppConfig:

    pass
class webapp_Resource:

    pass
class webapp_Controller:

    pass
class webapp_WebApp:

    def __init__(self, name: str, framework: str, webapp_WebApp10: "webapp_Controller" = None, webapp_WebApp12: "webapp_Resource" = None, webapp_WebApp: "webapp_AppConfig" = None, webapp_WebApp2: "webapp_WebConfig" = None, webapp_WebApp4: set["webapp_Library"] = None, webapp_WebApp6: "webapp_View" = None, webapp_WebApp8: "webapp_Model" = None):
        self.name = name
        self.framework = framework
        self.webapp_WebApp10 = webapp_WebApp10
        self.webapp_WebApp12 = webapp_WebApp12
        self.webapp_WebApp = webapp_WebApp
        self.webapp_WebApp2 = webapp_WebApp2
        self.webapp_WebApp4 = webapp_WebApp4 if webapp_WebApp4 is not None else set()
        self.webapp_WebApp6 = webapp_WebApp6
        self.webapp_WebApp8 = webapp_WebApp8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def framework(self) -> str:
        return self.__framework

    @framework.setter
    def framework(self, framework: str):
        self.__framework = framework

    @property
    def webapp_WebApp6(self):
        return self.__webapp_WebApp6

    @webapp_WebApp6.setter
    def webapp_WebApp6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_WebApp__webapp_WebApp6", None)
        self.__webapp_WebApp6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_View"):
                opp_val = getattr(old_value, "webapp_View", None)
                if opp_val == self:
                    setattr(old_value, "webapp_View", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_View"):
                opp_val = getattr(value, "webapp_View", None)
                setattr(value, "webapp_View", self)

    @property
    def webapp_WebApp4(self):
        return self.__webapp_WebApp4

    @webapp_WebApp4.setter
    def webapp_WebApp4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_WebApp__webapp_WebApp4", None)
        self.__webapp_WebApp4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Library"):
                    opp_val = getattr(item, "webapp_Library", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Library", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Library"):
                    opp_val = getattr(item, "webapp_Library", None)
                    
                    setattr(item, "webapp_Library", self)
                    

    @property
    def webapp_WebApp(self):
        return self.__webapp_WebApp

    @webapp_WebApp.setter
    def webapp_WebApp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_WebApp__webapp_WebApp", None)
        self.__webapp_WebApp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_AppConfig"):
                opp_val = getattr(old_value, "webapp_AppConfig", None)
                if opp_val == self:
                    setattr(old_value, "webapp_AppConfig", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_AppConfig"):
                opp_val = getattr(value, "webapp_AppConfig", None)
                setattr(value, "webapp_AppConfig", self)

    @property
    def webapp_WebApp12(self):
        return self.__webapp_WebApp12

    @webapp_WebApp12.setter
    def webapp_WebApp12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_WebApp__webapp_WebApp12", None)
        self.__webapp_WebApp12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Resource"):
                opp_val = getattr(old_value, "webapp_Resource", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Resource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Resource"):
                opp_val = getattr(value, "webapp_Resource", None)
                setattr(value, "webapp_Resource", self)

    @property
    def webapp_WebApp10(self):
        return self.__webapp_WebApp10

    @webapp_WebApp10.setter
    def webapp_WebApp10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_WebApp__webapp_WebApp10", None)
        self.__webapp_WebApp10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Controller"):
                opp_val = getattr(old_value, "webapp_Controller", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Controller", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Controller"):
                opp_val = getattr(value, "webapp_Controller", None)
                setattr(value, "webapp_Controller", self)

    @property
    def webapp_WebApp2(self):
        return self.__webapp_WebApp2

    @webapp_WebApp2.setter
    def webapp_WebApp2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_WebApp__webapp_WebApp2", None)
        self.__webapp_WebApp2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_WebConfig"):
                opp_val = getattr(old_value, "webapp_WebConfig", None)
                if opp_val == self:
                    setattr(old_value, "webapp_WebConfig", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_WebConfig"):
                opp_val = getattr(value, "webapp_WebConfig", None)
                setattr(value, "webapp_WebConfig", self)

    @property
    def webapp_WebApp8(self):
        return self.__webapp_WebApp8

    @webapp_WebApp8.setter
    def webapp_WebApp8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_WebApp__webapp_WebApp8", None)
        self.__webapp_WebApp8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Model"):
                opp_val = getattr(old_value, "webapp_Model", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Model"):
                opp_val = getattr(value, "webapp_Model", None)
                setattr(value, "webapp_Model", self)
