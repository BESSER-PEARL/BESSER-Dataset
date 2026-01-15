from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BinaryStringTypes(Enum):
    BINARYLARGEOBJECT = "BINARYLARGEOBJECT"
    BINARY = "BINARY"
    BINARYVARYING = "BINARYVARYING"
class DatetimeFeatures(Enum):
    precision = "precision"
class DatetimeTypes(Enum):
    DATE = "DATE"
    TIMEWITHTIMEZONE = "TIMEWITHTIMEZONE"
    TIMEWITHOUTTIMEZONE = "TIMEWITHOUTTIMEZONE"
    TIMESTAMPWITHOUTTIMEZONE = "TIMESTAMPWITHOUTTIMEZONE"
    TIMESTAMPWITHTIMEZONE = "TIMESTAMPWITHTIMEZONE"
class MatchTypes(Enum):
    SIMPLE = "SIMPLE"
    PARTIAL = "PARTIAL"
    TOTAL = "TOTAL"
class ParameterMode(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class NumericTypes(Enum):
    DECIMAL = "DECIMAL"
    SMALLINT = "SMALLINT"
    INTEGER = "INTEGER"
    BIGINT = "BIGINT"
    FLOAT = "FLOAT"
    REAL = "REAL"
    DOUBLEPRECISION = "DOUBLEPRECISION"
    NUMERIC = "NUMERIC"
class StringFeatures(Enum):
    length = "length"
    unit = "unit"
    multiplier = "multiplier"
class TriggerLevel(Enum):
    ROW_LEVEL = "ROW_LEVEL"
    STATEMENT_LEVEL = "STATEMENT_LEVEL"
class TriggerActionTime(Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"
class TriggerEvent(Enum):
    INSERT = "INSERT"
    DELETE = "DELETE"
    UPDATE = "UPDATE"
class IntervalTypes(Enum):
    MONTH = "MONTH"
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"
    SECOND = "SECOND"
    YEAR_MONTH = "YEAR_MONTH"
    DAY_HOUR = "DAY_HOUR"
    DAY_MINUTE = "DAY_MINUTE"
    DAY_SECOND = "DAY_SECOND"
    HOUR_MINUTE = "HOUR_MINUTE"
    HOUR_SECOND = "HOUR_SECOND"
    MINUTE_SECOND = "MINUTE_SECOND"
    YEAR = "YEAR"
class NumericFeatures(Enum):
    precision = "precision"
    scale = "scale"
    radix = "radix"
class IntervalFeatures(Enum):
    start_leading_precision = "start_leading_precision"
    end_leading_precision = "end_leading_precision"
    leading_precision = "leading_precision"
    second_precision = "second_precision"
class ReferentialAction(Enum):
    CASCADE = "CASCADE"
    SET_NULL = "SET_NULL"
    RESTRICT = "RESTRICT"
    NO_ACTION = "NO_ACTION"
    SET_DEFAULT = "SET_DEFAULT"
class NumericRadix(Enum):
    DECIMAL = "DECIMAL"
    BINARY = "BINARY"
class CharacterStringTypes(Enum):
    CHARACTER = "CHARACTER"
    CHARACTERVARYING = "CHARACTERVARYING"
    CHARACTERLARGEOBJECT = "CHARACTERLARGEOBJECT"
class Unit(Enum):
    CHARACTERS = "CHARACTERS"
    OCTETS = "OCTETS"
class XMLTypes(Enum):
    XMLTYPE = "XMLTYPE"
class Multiplier(Enum):
    K = "K"
    M = "M"
    G = "G"
    T = "T"
    P = "P"
class BooleanTypes(Enum):
    BOOLEAN = "BOOLEAN"


############################################
# Definition of Classes
############################################

class DerivedTable:

    pass
class BaseTable:

    pass
class SQL2003_V3_TriggerDescriptor:

    def __init__(self, event: str, actionTime: str, triggeredAction: str, level: str, TriggerDescriptor: "SQL2003_V3_Trigger" = None, description: "SQL2003_V3_Trigger" = None):
        self.event = event
        self.actionTime = actionTime
        self.triggeredAction = triggeredAction
        self.level = level
        self.TriggerDescriptor = TriggerDescriptor
        self.description = description
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def triggeredAction(self) -> str:
        return self.__triggeredAction

    @triggeredAction.setter
    def triggeredAction(self, triggeredAction: str):
        self.__triggeredAction = triggeredAction

    @property
    def actionTime(self) -> str:
        return self.__actionTime

    @actionTime.setter
    def actionTime(self, actionTime: str):
        self.__actionTime = actionTime

    @property
    def TriggerDescriptor(self):
        return self.__TriggerDescriptor

    @TriggerDescriptor.setter
    def TriggerDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_TriggerDescriptor__TriggerDescriptor", None)
        self.__TriggerDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trigger"):
                opp_val = getattr(old_value, "trigger", None)
                if opp_val == self:
                    setattr(old_value, "trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trigger"):
                opp_val = getattr(value, "trigger", None)
                setattr(value, "trigger", self)

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_TriggerDescriptor__description", None)
        self.__description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Trigger"):
                opp_val = getattr(old_value, "Trigger", None)
                if opp_val == self:
                    setattr(old_value, "Trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Trigger"):
                opp_val = getattr(value, "Trigger", None)
                setattr(value, "Trigger", self)

class SQL2003_V3_TypedTable(BaseTable):

    pass
class SQL2003_V3_View(DerivedTable):

    pass
class SQL2003_V3_Restriction(ABC):

    pass
class UniqueConstraint:

    pass
class SQL2003_V3_PrimaryKey(UniqueConstraint):

    pass
class SQL2003_V3_Parameter(ABC):

    def __init__(self, name: str, SQL2003_V3_Parameter: "SQL2003_V3_DataType" = None):
        self.name = name
        self.SQL2003_V3_Parameter = SQL2003_V3_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SQL2003_V3_Parameter(self):
        return self.__SQL2003_V3_Parameter

    @SQL2003_V3_Parameter.setter
    def SQL2003_V3_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Parameter__SQL2003_V3_Parameter", None)
        self.__SQL2003_V3_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V3_DataType30"):
                opp_val = getattr(old_value, "SQL2003_V3_DataType30", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V3_DataType30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V3_DataType30"):
                opp_val = getattr(value, "SQL2003_V3_DataType30", None)
                setattr(value, "SQL2003_V3_DataType30", self)

class Parameter:

    pass
class SQL2003_V3_MethodParameter(Parameter):

    pass
class ColumnConstraint:

    pass
class SQL2003_V3_NotNull(ColumnConstraint):

    pass
class SQL2003_V3_Method:

    def __init__(self, name: str, body: str, SQL2003_V3_Method: "SQL2003_V3_Method" = None, SQL2003_V3_Method20: "SQL2003_V3_Method" = None, Method: "SQL2003_V3_MethodParameter" = None, methods: "SQL2003_V3_StructuredType" = None, SQL2003_V3_Method25: "SQL2003_V3_DataType" = None, method: set["SQL2003_V3_MethodParameter"] = None, Method73: "SQL2003_V3_StructuredType" = None):
        self.name = name
        self.body = body
        self.SQL2003_V3_Method = SQL2003_V3_Method
        self.SQL2003_V3_Method20 = SQL2003_V3_Method20
        self.Method = Method
        self.methods = methods
        self.SQL2003_V3_Method25 = SQL2003_V3_Method25
        self.method = method if method is not None else set()
        self.Method73 = Method73
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def SQL2003_V3_Method25(self):
        return self.__SQL2003_V3_Method25

    @SQL2003_V3_Method25.setter
    def SQL2003_V3_Method25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Method__SQL2003_V3_Method25", None)
        self.__SQL2003_V3_Method25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V3_DataType26"):
                opp_val = getattr(old_value, "SQL2003_V3_DataType26", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V3_DataType26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V3_DataType26"):
                opp_val = getattr(value, "SQL2003_V3_DataType26", None)
                setattr(value, "SQL2003_V3_DataType26", self)

    @property
    def Method73(self):
        return self.__Method73

    @Method73.setter
    def Method73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Method__Method73", None)
        self.__Method73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structured72"):
                opp_val = getattr(old_value, "structured72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structured72"):
                opp_val = getattr(value, "structured72", None)
                if opp_val is None:
                    setattr(value, "structured72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Method__methods", None)
        self.__methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StructuredType23"):
                opp_val = getattr(old_value, "StructuredType23", None)
                if opp_val == self:
                    setattr(old_value, "StructuredType23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StructuredType23"):
                opp_val = getattr(value, "StructuredType23", None)
                setattr(value, "StructuredType23", self)

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Method__Method", None)
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

    @property
    def SQL2003_V3_Method20(self):
        return self.__SQL2003_V3_Method20

    @SQL2003_V3_Method20.setter
    def SQL2003_V3_Method20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Method__SQL2003_V3_Method20", None)
        self.__SQL2003_V3_Method20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V3_Method"):
                opp_val = getattr(old_value, "SQL2003_V3_Method", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V3_Method", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V3_Method"):
                opp_val = getattr(value, "SQL2003_V3_Method", None)
                setattr(value, "SQL2003_V3_Method", self)

    @property
    def SQL2003_V3_Method(self):
        return self.__SQL2003_V3_Method

    @SQL2003_V3_Method.setter
    def SQL2003_V3_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Method__SQL2003_V3_Method", None)
        self.__SQL2003_V3_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V3_Method20"):
                opp_val = getattr(old_value, "SQL2003_V3_Method20", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V3_Method20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V3_Method20"):
                opp_val = getattr(value, "SQL2003_V3_Method20", None)
                setattr(value, "SQL2003_V3_Method20", self)

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Method__method", None)
        self.__method = value if value is not None else set()
        
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
                    

class TableConstraint:

    pass
class SQL2003_V3_TableCheckConstraint(TableConstraint):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class SQL2003_V3_ReferentialConstraint(TableConstraint):

    def __init__(self, delete_action: str, update_action: str, match: str, SQL2003_V3_ReferentialConstraint: "SQL2003_V3_UniqueConstraint" = None):
        self.delete_action = delete_action
        self.update_action = update_action
        self.match = match
        self.SQL2003_V3_ReferentialConstraint = SQL2003_V3_ReferentialConstraint
        
    @property
    def match(self) -> str:
        return self.__match

    @match.setter
    def match(self, match: str):
        self.__match = match

    @property
    def delete_action(self) -> str:
        return self.__delete_action

    @delete_action.setter
    def delete_action(self, delete_action: str):
        self.__delete_action = delete_action

    @property
    def update_action(self) -> str:
        return self.__update_action

    @update_action.setter
    def update_action(self, update_action: str):
        self.__update_action = update_action

    @property
    def SQL2003_V3_ReferentialConstraint(self):
        return self.__SQL2003_V3_ReferentialConstraint

    @SQL2003_V3_ReferentialConstraint.setter
    def SQL2003_V3_ReferentialConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_ReferentialConstraint__SQL2003_V3_ReferentialConstraint", None)
        self.__SQL2003_V3_ReferentialConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V3_UniqueConstraint"):
                opp_val = getattr(old_value, "SQL2003_V3_UniqueConstraint", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V3_UniqueConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V3_UniqueConstraint"):
                opp_val = getattr(value, "SQL2003_V3_UniqueConstraint", None)
                setattr(value, "SQL2003_V3_UniqueConstraint", self)

class SQL2003_V3_UniqueConstraint(TableConstraint):

    pass
class BehaviouralComponent:

    pass
class SQL2003_V3_Procedure(BehaviouralComponent):

    pass
class SQL2003_V3_Function(BehaviouralComponent):

    pass
class UserDefinedType:

    pass
class SQL2003_V3_DistinctType(UserDefinedType):

    pass
class SQL2003_V3_DomainConstraint(TableConstraint):

    pass
class SQL2003_V3_StructuralComponent(ABC):

    def __init__(self, name: str, StructuralComponent: "SQL2003_V3_Domain" = None, StructuralComponent46: "SQL2003_V3_Restriction" = None, SQL2003_V3_StructuralComponent: "SQL2003_V3_DataType" = None, components: set["SQL2003_V3_View"] = None, columns61: set["SQL2003_V3_Restriction"] = None, SQL2003_V3_StructuralComponent63: set["SQL2003_V3_Feature"] = None, defines: "SQL2003_V3_Domain" = None, SQL2003_V3_StructuralComponent87: "SQL2003_V3_Trigger" = None, StructuralComponent101: "SQL2003_V3_View" = None):
        self.name = name
        self.StructuralComponent = StructuralComponent
        self.StructuralComponent46 = StructuralComponent46
        self.SQL2003_V3_StructuralComponent = SQL2003_V3_StructuralComponent
        self.components = components if components is not None else set()
        self.columns61 = columns61 if columns61 is not None else set()
        self.SQL2003_V3_StructuralComponent63 = SQL2003_V3_StructuralComponent63 if SQL2003_V3_StructuralComponent63 is not None else set()
        self.defines = defines
        self.SQL2003_V3_StructuralComponent87 = SQL2003_V3_StructuralComponent87
        self.StructuralComponent101 = StructuralComponent101
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def components(self):
        return self.__components

    @components.setter
    def components(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuralComponent__components", None)
        self.__components = value if value is not None else set()
        
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
    def SQL2003_V3_StructuralComponent(self):
        return self.__SQL2003_V3_StructuralComponent

    @SQL2003_V3_StructuralComponent.setter
    def SQL2003_V3_StructuralComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuralComponent__SQL2003_V3_StructuralComponent", None)
        self.__SQL2003_V3_StructuralComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V3_DataType58"):
                opp_val = getattr(old_value, "SQL2003_V3_DataType58", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V3_DataType58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V3_DataType58"):
                opp_val = getattr(value, "SQL2003_V3_DataType58", None)
                setattr(value, "SQL2003_V3_DataType58", self)

    @property
    def defines(self):
        return self.__defines

    @defines.setter
    def defines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuralComponent__defines", None)
        self.__defines = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Domain66"):
                opp_val = getattr(old_value, "Domain66", None)
                if opp_val == self:
                    setattr(old_value, "Domain66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Domain66"):
                opp_val = getattr(value, "Domain66", None)
                setattr(value, "Domain66", self)

    @property
    def SQL2003_V3_StructuralComponent87(self):
        return self.__SQL2003_V3_StructuralComponent87

    @SQL2003_V3_StructuralComponent87.setter
    def SQL2003_V3_StructuralComponent87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuralComponent__SQL2003_V3_StructuralComponent87", None)
        self.__SQL2003_V3_StructuralComponent87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V3_Trigger"):
                opp_val = getattr(old_value, "SQL2003_V3_Trigger", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V3_Trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V3_Trigger"):
                opp_val = getattr(value, "SQL2003_V3_Trigger", None)
                setattr(value, "SQL2003_V3_Trigger", self)

    @property
    def StructuralComponent101(self):
        return self.__StructuralComponent101

    @StructuralComponent101.setter
    def StructuralComponent101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuralComponent__StructuralComponent101", None)
        self.__StructuralComponent101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "views100"):
                opp_val = getattr(old_value, "views100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "views100"):
                opp_val = getattr(value, "views100", None)
                if opp_val is None:
                    setattr(value, "views100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SQL2003_V3_StructuralComponent63(self):
        return self.__SQL2003_V3_StructuralComponent63

    @SQL2003_V3_StructuralComponent63.setter
    def SQL2003_V3_StructuralComponent63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuralComponent__SQL2003_V3_StructuralComponent63", None)
        self.__SQL2003_V3_StructuralComponent63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SQL2003_V3_Feature64"):
                    opp_val = getattr(item, "SQL2003_V3_Feature64", None)
                    
                    if opp_val == self:
                        setattr(item, "SQL2003_V3_Feature64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SQL2003_V3_Feature64"):
                    opp_val = getattr(item, "SQL2003_V3_Feature64", None)
                    
                    setattr(item, "SQL2003_V3_Feature64", self)
                    

    @property
    def StructuralComponent46(self):
        return self.__StructuralComponent46

    @StructuralComponent46.setter
    def StructuralComponent46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuralComponent__StructuralComponent46", None)
        self.__StructuralComponent46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restrictions45"):
                opp_val = getattr(old_value, "restrictions45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restrictions45"):
                opp_val = getattr(value, "restrictions45", None)
                if opp_val is None:
                    setattr(value, "restrictions45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StructuralComponent(self):
        return self.__StructuralComponent

    @StructuralComponent.setter
    def StructuralComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuralComponent__StructuralComponent", None)
        self.__StructuralComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has_domain"):
                opp_val = getattr(old_value, "has_domain", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has_domain"):
                opp_val = getattr(value, "has_domain", None)
                if opp_val is None:
                    setattr(value, "has_domain", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def columns61(self):
        return self.__columns61

    @columns61.setter
    def columns61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuralComponent__columns61", None)
        self.__columns61 = value if value is not None else set()
        
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
                    

class SQL2003_V3_Domain:

    def __init__(self, name: str, expression: str, default: str, domains: "SQL2003_V3_Schema" = None, has_domain: set["SQL2003_V3_StructuralComponent"] = None, domain: set["SQL2003_V3_DomainConstraint"] = None, Domain: "SQL2003_V3_DomainConstraint" = None, Domain66: "SQL2003_V3_StructuralComponent" = None, Domain56: "SQL2003_V3_Schema" = None):
        self.name = name
        self.expression = expression
        self.default = default
        self.domains = domains
        self.has_domain = has_domain if has_domain is not None else set()
        self.domain = domain if domain is not None else set()
        self.Domain = Domain
        self.Domain66 = Domain66
        self.Domain56 = Domain56
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def domains(self):
        return self.__domains

    @domains.setter
    def domains(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Domain__domains", None)
        self.__domains = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema13"):
                opp_val = getattr(old_value, "Schema13", None)
                if opp_val == self:
                    setattr(old_value, "Schema13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema13"):
                opp_val = getattr(value, "Schema13", None)
                setattr(value, "Schema13", self)

    @property
    def Domain(self):
        return self.__Domain

    @Domain.setter
    def Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Domain__Domain", None)
        self.__Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "constraint"):
                opp_val = getattr(old_value, "constraint", None)
                if opp_val == self:
                    setattr(old_value, "constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "constraint"):
                opp_val = getattr(value, "constraint", None)
                setattr(value, "constraint", self)

    @property
    def has_domain(self):
        return self.__has_domain

    @has_domain.setter
    def has_domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Domain__has_domain", None)
        self.__has_domain = value if value is not None else set()
        
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
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Domain__domain", None)
        self.__domain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DomainConstraint"):
                    opp_val = getattr(item, "DomainConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "DomainConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DomainConstraint"):
                    opp_val = getattr(item, "DomainConstraint", None)
                    
                    setattr(item, "DomainConstraint", self)
                    

    @property
    def Domain56(self):
        return self.__Domain56

    @Domain56.setter
    def Domain56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Domain__Domain56", None)
        self.__Domain56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema55"):
                opp_val = getattr(old_value, "schema55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema55"):
                opp_val = getattr(value, "schema55", None)
                if opp_val is None:
                    setattr(value, "schema55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Domain66(self):
        return self.__Domain66

    @Domain66.setter
    def Domain66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Domain__Domain66", None)
        self.__Domain66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "defines"):
                opp_val = getattr(old_value, "defines", None)
                if opp_val == self:
                    setattr(old_value, "defines", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "defines"):
                opp_val = getattr(value, "defines", None)
                setattr(value, "defines", self)

class SQL2003_V3_Feature(ABC):

    pass
class Restriction:

    pass
class SQL2003_V3_TableConstraint(Restriction):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SQL2003_V3_Trigger(Restriction):

    def __init__(self, name: str, trigger: "SQL2003_V3_TriggerDescriptor" = None, SQL2003_V3_Trigger: "SQL2003_V3_StructuralComponent" = None, Trigger: "SQL2003_V3_TriggerDescriptor" = None):
        self.name = name
        self.trigger = trigger
        self.SQL2003_V3_Trigger = SQL2003_V3_Trigger
        self.Trigger = Trigger
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SQL2003_V3_Trigger(self):
        return self.__SQL2003_V3_Trigger

    @SQL2003_V3_Trigger.setter
    def SQL2003_V3_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Trigger__SQL2003_V3_Trigger", None)
        self.__SQL2003_V3_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V3_StructuralComponent87"):
                opp_val = getattr(old_value, "SQL2003_V3_StructuralComponent87", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V3_StructuralComponent87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V3_StructuralComponent87"):
                opp_val = getattr(value, "SQL2003_V3_StructuralComponent87", None)
                setattr(value, "SQL2003_V3_StructuralComponent87", self)

    @property
    def trigger(self):
        return self.__trigger

    @trigger.setter
    def trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Trigger__trigger", None)
        self.__trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TriggerDescriptor"):
                opp_val = getattr(old_value, "TriggerDescriptor", None)
                if opp_val == self:
                    setattr(old_value, "TriggerDescriptor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TriggerDescriptor"):
                opp_val = getattr(value, "TriggerDescriptor", None)
                setattr(value, "TriggerDescriptor", self)

    @property
    def Trigger(self):
        return self.__Trigger

    @Trigger.setter
    def Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Trigger__Trigger", None)
        self.__Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description"):
                opp_val = getattr(old_value, "description", None)
                if opp_val == self:
                    setattr(old_value, "description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description"):
                opp_val = getattr(value, "description", None)
                setattr(value, "description", self)

class SQL2003_V3_ColumnConstraint(Restriction):

    pass
class SQL2003_V3_Table(ABC):

    def __init__(self, name: str, Table: "SQL2003_V3_Column" = None, Table43: "SQL2003_V3_Restriction" = None, Table53: "SQL2003_V3_Schema" = None, tables: "SQL2003_V3_Schema" = None, table: set["SQL2003_V3_Column"] = None, tables80: set["SQL2003_V3_View"] = None, table83: set["SQL2003_V3_Restriction"] = None, Table98: "SQL2003_V3_View" = None):
        self.name = name
        self.Table = Table
        self.Table43 = Table43
        self.Table53 = Table53
        self.tables = tables
        self.table = table if table is not None else set()
        self.tables80 = tables80 if tables80 is not None else set()
        self.table83 = table83 if table83 is not None else set()
        self.Table98 = Table98
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def table83(self):
        return self.__table83

    @table83.setter
    def table83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Table__table83", None)
        self.__table83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Restriction84"):
                    opp_val = getattr(item, "Restriction84", None)
                    
                    if opp_val == self:
                        setattr(item, "Restriction84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Restriction84"):
                    opp_val = getattr(item, "Restriction84", None)
                    
                    setattr(item, "Restriction84", self)
                    

    @property
    def Table98(self):
        return self.__Table98

    @Table98.setter
    def Table98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Table__Table98", None)
        self.__Table98 = value
        
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
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Table__Table", None)
        self.__Table = value
        
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

    @property
    def Table53(self):
        return self.__Table53

    @Table53.setter
    def Table53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Table__Table53", None)
        self.__Table53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema52"):
                opp_val = getattr(old_value, "schema52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema52"):
                opp_val = getattr(value, "schema52", None)
                if opp_val is None:
                    setattr(value, "schema52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Table__table", None)
        self.__table = value if value is not None else set()
        
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
        old_value = getattr(self, f"_SQL2003_V3_Table__tables", None)
        self.__tables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema77"):
                opp_val = getattr(old_value, "Schema77", None)
                if opp_val == self:
                    setattr(old_value, "Schema77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema77"):
                opp_val = getattr(value, "Schema77", None)
                setattr(value, "Schema77", self)

    @property
    def tables80(self):
        return self.__tables80

    @tables80.setter
    def tables80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Table__tables80", None)
        self.__tables80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "View81"):
                    opp_val = getattr(item, "View81", None)
                    
                    if opp_val == self:
                        setattr(item, "View81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "View81"):
                    opp_val = getattr(item, "View81", None)
                    
                    setattr(item, "View81", self)
                    

    @property
    def Table43(self):
        return self.__Table43

    @Table43.setter
    def Table43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Table__Table43", None)
        self.__Table43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restrictions"):
                opp_val = getattr(old_value, "restrictions", None)
                if opp_val == self:
                    setattr(old_value, "restrictions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restrictions"):
                opp_val = getattr(value, "restrictions", None)
                setattr(value, "restrictions", self)

class Feature:

    pass
class SQL2003_V3_NumericFeature(Feature):

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

class SQL2003_V3_StringFeature(Feature):

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

class SQL2003_V3_IntervalFeature(Feature):

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

class SQL2003_V3_DatetimeFeature(Feature):

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

class DataType:

    pass
class SQL2003_V3_UserDefinedType(DataType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SQL2003_V3_PredefinedType(DataType):

    pass
class SQL2003_V3_ConstructedType(DataType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class PredefinedType:

    pass
class SQL2003_V3_IntervalType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_V3_XMLType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_V3_NumericType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_V3_DatetimeType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_V3_BinaryStringType(PredefinedType):

    def __init__(self, descriptor: str, length_def: str):
        self.descriptor = descriptor
        self.length_def = length_def
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

    @property
    def length_def(self) -> str:
        return self.__length_def

    @length_def.setter
    def length_def(self, length_def: str):
        self.__length_def = length_def

class SQL2003_V3_DataType(ABC):

    pass
class ConstructedType:

    pass
class SQL2003_V3_ReferenceType(ConstructedType):

    pass
class SQL2003_V3_ROW(ConstructedType):

    pass
class SQL2003_V3_CollectionType(ConstructedType):

    pass
class SQL2003_V3_CharacterStringType(PredefinedType):

    def __init__(self, descriptor: str, length_def: str):
        self.descriptor = descriptor
        self.length_def = length_def
        
    @property
    def length_def(self) -> str:
        return self.__length_def

    @length_def.setter
    def length_def(self, length_def: str):
        self.__length_def = length_def

    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_V3_BooleanType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class CollectionType:

    pass
class SQL2003_V3_MULTISET(CollectionType):

    pass
class SQL2003_V3_ARRAY(CollectionType):

    def __init__(self, num_elements: str):
        self.num_elements = num_elements
        
    @property
    def num_elements(self) -> str:
        return self.__num_elements

    @num_elements.setter
    def num_elements(self, num_elements: str):
        self.__num_elements = num_elements

class SQL2003_V3_ParameterWithMode(Parameter):

    def __init__(self, mode: str, ParameterWithMode: "SQL2003_V3_BehaviouralComponent" = None, parametersWithMode: "SQL2003_V3_BehaviouralComponent" = None):
        self.mode = mode
        self.ParameterWithMode = ParameterWithMode
        self.parametersWithMode = parametersWithMode
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def parametersWithMode(self):
        return self.__parametersWithMode

    @parametersWithMode.setter
    def parametersWithMode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_ParameterWithMode__parametersWithMode", None)
        self.__parametersWithMode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BehaviouralComponent"):
                opp_val = getattr(old_value, "BehaviouralComponent", None)
                if opp_val == self:
                    setattr(old_value, "BehaviouralComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BehaviouralComponent"):
                opp_val = getattr(value, "BehaviouralComponent", None)
                setattr(value, "BehaviouralComponent", self)

    @property
    def ParameterWithMode(self):
        return self.__ParameterWithMode

    @ParameterWithMode.setter
    def ParameterWithMode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_ParameterWithMode__ParameterWithMode", None)
        self.__ParameterWithMode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviouralComponent"):
                opp_val = getattr(old_value, "behaviouralComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviouralComponent"):
                opp_val = getattr(value, "behaviouralComponent", None)
                if opp_val is None:
                    setattr(value, "behaviouralComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SQL2003_V3_Schema:

    def __init__(self, name: str, Schema: "SQL2003_V3_BehaviouralComponent" = None, Schema9: "SQL2003_V3_DataType" = None, Schema13: "SQL2003_V3_Domain" = None, schema: set["SQL2003_V3_BehaviouralComponent"] = None, schema50: set["SQL2003_V3_DataType"] = None, schema52: set["SQL2003_V3_Table"] = None, schema55: set["SQL2003_V3_Domain"] = None, Schema77: "SQL2003_V3_Table" = None):
        self.name = name
        self.Schema = Schema
        self.Schema9 = Schema9
        self.Schema13 = Schema13
        self.schema = schema if schema is not None else set()
        self.schema50 = schema50 if schema50 is not None else set()
        self.schema52 = schema52 if schema52 is not None else set()
        self.schema55 = schema55 if schema55 is not None else set()
        self.Schema77 = Schema77
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def schema55(self):
        return self.__schema55

    @schema55.setter
    def schema55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Schema__schema55", None)
        self.__schema55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Domain56"):
                    opp_val = getattr(item, "Domain56", None)
                    
                    if opp_val == self:
                        setattr(item, "Domain56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Domain56"):
                    opp_val = getattr(item, "Domain56", None)
                    
                    setattr(item, "Domain56", self)
                    

    @property
    def schema52(self):
        return self.__schema52

    @schema52.setter
    def schema52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Schema__schema52", None)
        self.__schema52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table53"):
                    opp_val = getattr(item, "Table53", None)
                    
                    if opp_val == self:
                        setattr(item, "Table53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table53"):
                    opp_val = getattr(item, "Table53", None)
                    
                    setattr(item, "Table53", self)
                    

    @property
    def Schema77(self):
        return self.__Schema77

    @Schema77.setter
    def Schema77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Schema__Schema77", None)
        self.__Schema77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables"):
                opp_val = getattr(old_value, "tables", None)
                if opp_val == self:
                    setattr(old_value, "tables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables"):
                opp_val = getattr(value, "tables", None)
                setattr(value, "tables", self)

    @property
    def Schema9(self):
        return self.__Schema9

    @Schema9.setter
    def Schema9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Schema__Schema9", None)
        self.__Schema9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatypes"):
                opp_val = getattr(old_value, "datatypes", None)
                if opp_val == self:
                    setattr(old_value, "datatypes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatypes"):
                opp_val = getattr(value, "datatypes", None)
                setattr(value, "datatypes", self)

    @property
    def Schema(self):
        return self.__Schema

    @Schema.setter
    def Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Schema__Schema", None)
        self.__Schema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviouralComponents"):
                opp_val = getattr(old_value, "behaviouralComponents", None)
                if opp_val == self:
                    setattr(old_value, "behaviouralComponents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviouralComponents"):
                opp_val = getattr(value, "behaviouralComponents", None)
                setattr(value, "behaviouralComponents", self)

    @property
    def schema50(self):
        return self.__schema50

    @schema50.setter
    def schema50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Schema__schema50", None)
        self.__schema50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataType"):
                    opp_val = getattr(item, "DataType", None)
                    
                    if opp_val == self:
                        setattr(item, "DataType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataType"):
                    opp_val = getattr(item, "DataType", None)
                    
                    setattr(item, "DataType", self)
                    

    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Schema__schema", None)
        self.__schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BehaviouralComponent48"):
                    opp_val = getattr(item, "BehaviouralComponent48", None)
                    
                    if opp_val == self:
                        setattr(item, "BehaviouralComponent48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BehaviouralComponent48"):
                    opp_val = getattr(item, "BehaviouralComponent48", None)
                    
                    setattr(item, "BehaviouralComponent48", self)
                    

    @property
    def Schema13(self):
        return self.__Schema13

    @Schema13.setter
    def Schema13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Schema__Schema13", None)
        self.__Schema13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domains"):
                opp_val = getattr(old_value, "domains", None)
                if opp_val == self:
                    setattr(old_value, "domains", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domains"):
                opp_val = getattr(value, "domains", None)
                setattr(value, "domains", self)

class SQL2003_V3_BehaviouralComponent(ABC):

    def __init__(self, name: str, body: str, behaviouralComponents: "SQL2003_V3_Schema" = None, behaviouralComponent: set["SQL2003_V3_ParameterWithMode"] = None, BehaviouralComponent: "SQL2003_V3_ParameterWithMode" = None, BehaviouralComponent48: "SQL2003_V3_Schema" = None):
        self.name = name
        self.body = body
        self.behaviouralComponents = behaviouralComponents
        self.behaviouralComponent = behaviouralComponent if behaviouralComponent is not None else set()
        self.BehaviouralComponent = BehaviouralComponent
        self.BehaviouralComponent48 = BehaviouralComponent48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def BehaviouralComponent(self):
        return self.__BehaviouralComponent

    @BehaviouralComponent.setter
    def BehaviouralComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_BehaviouralComponent__BehaviouralComponent", None)
        self.__BehaviouralComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parametersWithMode"):
                opp_val = getattr(old_value, "parametersWithMode", None)
                if opp_val == self:
                    setattr(old_value, "parametersWithMode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parametersWithMode"):
                opp_val = getattr(value, "parametersWithMode", None)
                setattr(value, "parametersWithMode", self)

    @property
    def BehaviouralComponent48(self):
        return self.__BehaviouralComponent48

    @BehaviouralComponent48.setter
    def BehaviouralComponent48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_BehaviouralComponent__BehaviouralComponent48", None)
        self.__BehaviouralComponent48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema"):
                opp_val = getattr(old_value, "schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema"):
                opp_val = getattr(value, "schema", None)
                if opp_val is None:
                    setattr(value, "schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviouralComponents(self):
        return self.__behaviouralComponents

    @behaviouralComponents.setter
    def behaviouralComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_BehaviouralComponent__behaviouralComponents", None)
        self.__behaviouralComponents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema"):
                opp_val = getattr(old_value, "Schema", None)
                if opp_val == self:
                    setattr(old_value, "Schema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema"):
                opp_val = getattr(value, "Schema", None)
                setattr(value, "Schema", self)

    @property
    def behaviouralComponent(self):
        return self.__behaviouralComponent

    @behaviouralComponent.setter
    def behaviouralComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_BehaviouralComponent__behaviouralComponent", None)
        self.__behaviouralComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParameterWithMode"):
                    opp_val = getattr(item, "ParameterWithMode", None)
                    
                    if opp_val == self:
                        setattr(item, "ParameterWithMode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParameterWithMode"):
                    opp_val = getattr(item, "ParameterWithMode", None)
                    
                    setattr(item, "ParameterWithMode", self)
                    

class Table:

    pass
class SQL2003_V3_DerivedTable(Table):

    def __init__(self, query_expression: str):
        self.query_expression = query_expression
        
    @property
    def query_expression(self) -> str:
        return self.__query_expression

    @query_expression.setter
    def query_expression(self, query_expression: str):
        self.__query_expression = query_expression

class SQL2003_V3_BaseTable(Table):

    pass
class SQL2003_V3_StructuredType(UserDefinedType):

    def __init__(self, is_final: bool, is_instantiable: bool, StructuredType: "SQL2003_V3_Attribute" = None, StructuredType23: "SQL2003_V3_Method" = None, SQL2003_V3_StructuredType: "SQL2003_V3_ReferenceType" = None, structured72: set["SQL2003_V3_Method"] = None, structured75: set["SQL2003_V3_TypedTable"] = None, SQL2003_V3_StructuredType69: "SQL2003_V3_StructuredType" = None, SQL2003_V3_StructuredType67: "SQL2003_V3_StructuredType" = None, structured: set["SQL2003_V3_Attribute"] = None, StructuredType90: "SQL2003_V3_TypedTable" = None):
        self.is_final = is_final
        self.is_instantiable = is_instantiable
        self.StructuredType = StructuredType
        self.StructuredType23 = StructuredType23
        self.SQL2003_V3_StructuredType = SQL2003_V3_StructuredType
        self.structured72 = structured72 if structured72 is not None else set()
        self.structured75 = structured75 if structured75 is not None else set()
        self.SQL2003_V3_StructuredType69 = SQL2003_V3_StructuredType69
        self.SQL2003_V3_StructuredType67 = SQL2003_V3_StructuredType67
        self.structured = structured if structured is not None else set()
        self.StructuredType90 = StructuredType90
        
    @property
    def is_instantiable(self) -> bool:
        return self.__is_instantiable

    @is_instantiable.setter
    def is_instantiable(self, is_instantiable: bool):
        self.__is_instantiable = is_instantiable

    @property
    def is_final(self) -> bool:
        return self.__is_final

    @is_final.setter
    def is_final(self, is_final: bool):
        self.__is_final = is_final

    @property
    def SQL2003_V3_StructuredType69(self):
        return self.__SQL2003_V3_StructuredType69

    @SQL2003_V3_StructuredType69.setter
    def SQL2003_V3_StructuredType69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuredType__SQL2003_V3_StructuredType69", None)
        self.__SQL2003_V3_StructuredType69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V3_StructuredType67"):
                opp_val = getattr(old_value, "SQL2003_V3_StructuredType67", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V3_StructuredType67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V3_StructuredType67"):
                opp_val = getattr(value, "SQL2003_V3_StructuredType67", None)
                setattr(value, "SQL2003_V3_StructuredType67", self)

    @property
    def StructuredType(self):
        return self.__StructuredType

    @StructuredType.setter
    def StructuredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuredType__StructuredType", None)
        self.__StructuredType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes"):
                opp_val = getattr(old_value, "attributes", None)
                if opp_val == self:
                    setattr(old_value, "attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes"):
                opp_val = getattr(value, "attributes", None)
                setattr(value, "attributes", self)

    @property
    def StructuredType23(self):
        return self.__StructuredType23

    @StructuredType23.setter
    def StructuredType23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuredType__StructuredType23", None)
        self.__StructuredType23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methods"):
                opp_val = getattr(old_value, "methods", None)
                if opp_val == self:
                    setattr(old_value, "methods", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methods"):
                opp_val = getattr(value, "methods", None)
                setattr(value, "methods", self)

    @property
    def structured72(self):
        return self.__structured72

    @structured72.setter
    def structured72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuredType__structured72", None)
        self.__structured72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method73"):
                    opp_val = getattr(item, "Method73", None)
                    
                    if opp_val == self:
                        setattr(item, "Method73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method73"):
                    opp_val = getattr(item, "Method73", None)
                    
                    setattr(item, "Method73", self)
                    

    @property
    def structured(self):
        return self.__structured

    @structured.setter
    def structured(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuredType__structured", None)
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
    def structured75(self):
        return self.__structured75

    @structured75.setter
    def structured75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuredType__structured75", None)
        self.__structured75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypedTable"):
                    opp_val = getattr(item, "TypedTable", None)
                    
                    if opp_val == self:
                        setattr(item, "TypedTable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypedTable"):
                    opp_val = getattr(item, "TypedTable", None)
                    
                    setattr(item, "TypedTable", self)
                    

    @property
    def SQL2003_V3_StructuredType67(self):
        return self.__SQL2003_V3_StructuredType67

    @SQL2003_V3_StructuredType67.setter
    def SQL2003_V3_StructuredType67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuredType__SQL2003_V3_StructuredType67", None)
        self.__SQL2003_V3_StructuredType67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V3_StructuredType69"):
                opp_val = getattr(old_value, "SQL2003_V3_StructuredType69", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V3_StructuredType69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V3_StructuredType69"):
                opp_val = getattr(value, "SQL2003_V3_StructuredType69", None)
                setattr(value, "SQL2003_V3_StructuredType69", self)

    @property
    def SQL2003_V3_StructuredType(self):
        return self.__SQL2003_V3_StructuredType

    @SQL2003_V3_StructuredType.setter
    def SQL2003_V3_StructuredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuredType__SQL2003_V3_StructuredType", None)
        self.__SQL2003_V3_StructuredType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V3_ReferenceType"):
                opp_val = getattr(old_value, "SQL2003_V3_ReferenceType", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V3_ReferenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V3_ReferenceType"):
                opp_val = getattr(value, "SQL2003_V3_ReferenceType", None)
                setattr(value, "SQL2003_V3_ReferenceType", self)

    @property
    def StructuredType90(self):
        return self.__StructuredType90

    @StructuredType90.setter
    def StructuredType90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_StructuredType__StructuredType90", None)
        self.__StructuredType90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typed"):
                opp_val = getattr(old_value, "typed", None)
                if opp_val == self:
                    setattr(old_value, "typed", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typed"):
                opp_val = getattr(value, "typed", None)
                setattr(value, "typed", self)

class StructuralComponent:

    pass
class SQL2003_V3_Field(StructuralComponent):

    pass
class SQL2003_V3_Column(StructuralComponent):

    def __init__(self, default: str, columns: "SQL2003_V3_Table" = None, Column: "SQL2003_V3_Table" = None):
        self.default = default
        self.columns = columns
        self.Column = Column
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Column__Column", None)
        self.__Column = value
        
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
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Column__columns", None)
        self.__columns = value
        
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

class SQL2003_V3_Attribute(StructuralComponent):

    def __init__(self, default: str, attributes: "SQL2003_V3_StructuredType" = None, Attribute: "SQL2003_V3_StructuredType" = None):
        self.default = default
        self.attributes = attributes
        self.Attribute = Attribute
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Attribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StructuredType"):
                opp_val = getattr(old_value, "StructuredType", None)
                if opp_val == self:
                    setattr(old_value, "StructuredType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StructuredType"):
                opp_val = getattr(value, "StructuredType", None)
                setattr(value, "StructuredType", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V3_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structured"):
                opp_val = getattr(old_value, "structured", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structured"):
                opp_val = getattr(value, "structured", None)
                if opp_val is None:
                    setattr(value, "structured", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
