from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Multiplier(Enum):
    K = "K"
    M = "M"
    G = "G"
    T = "T"
    P = "P"
class NumericTypes(Enum):
    NUMERIC = "NUMERIC"
    DECIMAL = "DECIMAL"
    SMALLINT = "SMALLINT"
    INTEGER = "INTEGER"
    BIGINT = "BIGINT"
    FLOAT = "FLOAT"
    REAL = "REAL"
    DOUBLEPRECISION = "DOUBLEPRECISION"
class StringFeatures(Enum):
    length = "length"
    unit = "unit"
    multiplier = "multiplier"
class TriggerLevel(Enum):
    ROW_LEVEL = "ROW_LEVEL"
    STATEMENT_LEVEL = "STATEMENT_LEVEL"
class TriggerEvent(Enum):
    INSERT = "INSERT"
    DELETE = "DELETE"
    UPDATE = "UPDATE"
class NumericFeatures(Enum):
    precision = "precision"
    scale = "scale"
    radix = "radix"
class IntervalFeatures(Enum):
    start_leading_precision = "start_leading_precision"
    end_leading_precision = "end_leading_precision"
    leading_precision = "leading_precision"
    second_precision = "second_precision"
class DatetimeTypes(Enum):
    DATE = "DATE"
    TIMEWITHTIMEZONE = "TIMEWITHTIMEZONE"
    TIMEWITHOUTTIMEZONE = "TIMEWITHOUTTIMEZONE"
    TIMESTAMPWITHOUTTIMEZONE = "TIMESTAMPWITHOUTTIMEZONE"
    TIMESTAMPWITHTIMEZONE = "TIMESTAMPWITHTIMEZONE"
class TriggerActionTime(Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"
class XMLTypes(Enum):
    XMLTYPE = "XMLTYPE"
class DatetimeFeatures(Enum):
    precision = "precision"
class ParameterMode(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class Unit(Enum):
    OCTETS = "OCTETS"
    CHARACTERS = "CHARACTERS"
class CharacterStringTypes(Enum):
    CHARACTER = "CHARACTER"
    CHARACTERVARYING = "CHARACTERVARYING"
    CHARACTERLARGEOBJECT = "CHARACTERLARGEOBJECT"
class MatchTypes(Enum):
    SIMPLE = "SIMPLE"
    PARTIAL = "PARTIAL"
    TOTAL = "TOTAL"
class BinaryStringTypes(Enum):
    BINARYLARGEOBJECT = "BINARYLARGEOBJECT"
    BINARY = "BINARY"
    BINARYVARYING = "BINARYVARYING"
class BooleanTypes(Enum):
    BOOLEAN = "BOOLEAN"
class NumericRadix(Enum):
    BINARY = "BINARY"
    DECIMAL = "DECIMAL"
class IntervalTypes(Enum):
    HOUR_MINUTE = "HOUR_MINUTE"
    HOUR_SECOND = "HOUR_SECOND"
    MINUTE_SECOND = "MINUTE_SECOND"
    YEAR = "YEAR"
    YEAR_MONTH = "YEAR_MONTH"
    DAY_HOUR = "DAY_HOUR"
    DAY_MINUTE = "DAY_MINUTE"
    DAY_SECOND = "DAY_SECOND"
    MONTH = "MONTH"
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"
    SECOND = "SECOND"
class ReferentialAction(Enum):
    CASCADE = "CASCADE"
    SET_NULL = "SET_NULL"
    RESTRICT = "RESTRICT"
    NO_ACTION = "NO_ACTION"
    SET_DEFAULT = "SET_DEFAULT"


############################################
# Definition of Classes
############################################

class DerivedTable:

    pass
class BaseTable:

    pass
class SQL2003_V2_TriggerDescriptor:

    def __init__(self, event: str, actionTime: str, triggeredAction: str, level: str, TriggerDescriptor: "SQL2003_V2_Trigger" = None, description: "SQL2003_V2_Trigger" = None):
        self.event = event
        self.actionTime = actionTime
        self.triggeredAction = triggeredAction
        self.level = level
        self.TriggerDescriptor = TriggerDescriptor
        self.description = description
        
    @property
    def triggeredAction(self) -> str:
        return self.__triggeredAction

    @triggeredAction.setter
    def triggeredAction(self, triggeredAction: str):
        self.__triggeredAction = triggeredAction

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
        old_value = getattr(self, f"_SQL2003_V2_TriggerDescriptor__TriggerDescriptor", None)
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
        old_value = getattr(self, f"_SQL2003_V2_TriggerDescriptor__description", None)
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

class SQL2003_V2_TypedTable(BaseTable):

    pass
class SQL2003_V2_Domain:

    def __init__(self, name: str, expression: str, default: str, Domain: "SQL2003_V2_Schema" = None, Domain59: "SQL2003_V2_StructuralComponent" = None, domains: "SQL2003_V2_Schema" = None, has_domain: set["SQL2003_V2_StructuralComponent"] = None):
        self.name = name
        self.expression = expression
        self.default = default
        self.Domain = Domain
        self.Domain59 = Domain59
        self.domains = domains
        self.has_domain = has_domain if has_domain is not None else set()
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Domain59(self):
        return self.__Domain59

    @Domain59.setter
    def Domain59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Domain__Domain59", None)
        self.__Domain59 = value
        
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

    @property
    def domains(self):
        return self.__domains

    @domains.setter
    def domains(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Domain__domains", None)
        self.__domains = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema96"):
                opp_val = getattr(old_value, "Schema96", None)
                if opp_val == self:
                    setattr(old_value, "Schema96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema96"):
                opp_val = getattr(value, "Schema96", None)
                setattr(value, "Schema96", self)

    @property
    def has_domain(self):
        return self.__has_domain

    @has_domain.setter
    def has_domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Domain__has_domain", None)
        self.__has_domain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StructuralComponent98"):
                    opp_val = getattr(item, "StructuralComponent98", None)
                    
                    if opp_val == self:
                        setattr(item, "StructuralComponent98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StructuralComponent98"):
                    opp_val = getattr(item, "StructuralComponent98", None)
                    
                    setattr(item, "StructuralComponent98", self)
                    

    @property
    def Domain(self):
        return self.__Domain

    @Domain.setter
    def Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Domain__Domain", None)
        self.__Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema49"):
                opp_val = getattr(old_value, "schema49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema49"):
                opp_val = getattr(value, "schema49", None)
                if opp_val is None:
                    setattr(value, "schema49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SQL2003_V2_View(DerivedTable):

    pass
class SQL2003_V2_StructuralComponent(ABC):

    def __init__(self, name: str, StructuralComponent: "SQL2003_V2_Restriction" = None, components: set["SQL2003_V2_View"] = None, SQL2003_V2_StructuralComponent: "SQL2003_V2_DataType" = None, columns54: set["SQL2003_V2_Restriction"] = None, SQL2003_V2_StructuralComponent56: set["SQL2003_V2_Feature"] = None, defines: "SQL2003_V2_Domain" = None, SQL2003_V2_StructuralComponent80: "SQL2003_V2_Trigger" = None, StructuralComponent94: "SQL2003_V2_View" = None, StructuralComponent98: "SQL2003_V2_Domain" = None):
        self.name = name
        self.StructuralComponent = StructuralComponent
        self.components = components if components is not None else set()
        self.SQL2003_V2_StructuralComponent = SQL2003_V2_StructuralComponent
        self.columns54 = columns54 if columns54 is not None else set()
        self.SQL2003_V2_StructuralComponent56 = SQL2003_V2_StructuralComponent56 if SQL2003_V2_StructuralComponent56 is not None else set()
        self.defines = defines
        self.SQL2003_V2_StructuralComponent80 = SQL2003_V2_StructuralComponent80
        self.StructuralComponent94 = StructuralComponent94
        self.StructuralComponent98 = StructuralComponent98
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SQL2003_V2_StructuralComponent(self):
        return self.__SQL2003_V2_StructuralComponent

    @SQL2003_V2_StructuralComponent.setter
    def SQL2003_V2_StructuralComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuralComponent__SQL2003_V2_StructuralComponent", None)
        self.__SQL2003_V2_StructuralComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V2_DataType51"):
                opp_val = getattr(old_value, "SQL2003_V2_DataType51", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V2_DataType51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V2_DataType51"):
                opp_val = getattr(value, "SQL2003_V2_DataType51", None)
                setattr(value, "SQL2003_V2_DataType51", self)

    @property
    def StructuralComponent(self):
        return self.__StructuralComponent

    @StructuralComponent.setter
    def StructuralComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuralComponent__StructuralComponent", None)
        self.__StructuralComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restrictions40"):
                opp_val = getattr(old_value, "restrictions40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restrictions40"):
                opp_val = getattr(value, "restrictions40", None)
                if opp_val is None:
                    setattr(value, "restrictions40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SQL2003_V2_StructuralComponent80(self):
        return self.__SQL2003_V2_StructuralComponent80

    @SQL2003_V2_StructuralComponent80.setter
    def SQL2003_V2_StructuralComponent80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuralComponent__SQL2003_V2_StructuralComponent80", None)
        self.__SQL2003_V2_StructuralComponent80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V2_Trigger"):
                opp_val = getattr(old_value, "SQL2003_V2_Trigger", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V2_Trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V2_Trigger"):
                opp_val = getattr(value, "SQL2003_V2_Trigger", None)
                setattr(value, "SQL2003_V2_Trigger", self)

    @property
    def StructuralComponent98(self):
        return self.__StructuralComponent98

    @StructuralComponent98.setter
    def StructuralComponent98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuralComponent__StructuralComponent98", None)
        self.__StructuralComponent98 = value
        
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
    def columns54(self):
        return self.__columns54

    @columns54.setter
    def columns54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuralComponent__columns54", None)
        self.__columns54 = value if value is not None else set()
        
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
    def defines(self):
        return self.__defines

    @defines.setter
    def defines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuralComponent__defines", None)
        self.__defines = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Domain59"):
                opp_val = getattr(old_value, "Domain59", None)
                if opp_val == self:
                    setattr(old_value, "Domain59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Domain59"):
                opp_val = getattr(value, "Domain59", None)
                setattr(value, "Domain59", self)

    @property
    def SQL2003_V2_StructuralComponent56(self):
        return self.__SQL2003_V2_StructuralComponent56

    @SQL2003_V2_StructuralComponent56.setter
    def SQL2003_V2_StructuralComponent56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuralComponent__SQL2003_V2_StructuralComponent56", None)
        self.__SQL2003_V2_StructuralComponent56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SQL2003_V2_Feature57"):
                    opp_val = getattr(item, "SQL2003_V2_Feature57", None)
                    
                    if opp_val == self:
                        setattr(item, "SQL2003_V2_Feature57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SQL2003_V2_Feature57"):
                    opp_val = getattr(item, "SQL2003_V2_Feature57", None)
                    
                    setattr(item, "SQL2003_V2_Feature57", self)
                    

    @property
    def components(self):
        return self.__components

    @components.setter
    def components(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuralComponent__components", None)
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
    def StructuralComponent94(self):
        return self.__StructuralComponent94

    @StructuralComponent94.setter
    def StructuralComponent94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuralComponent__StructuralComponent94", None)
        self.__StructuralComponent94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "views93"):
                opp_val = getattr(old_value, "views93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "views93"):
                opp_val = getattr(value, "views93", None)
                if opp_val is None:
                    setattr(value, "views93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SQL2003_V2_Restriction(ABC):

    pass
class TableConstraint:

    pass
class SQL2003_V2_TableCheckConstraint(TableConstraint):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class SQL2003_V2_UniqueConstraint(TableConstraint):

    pass
class SQL2003_V2_ReferentialConstraint(TableConstraint):

    def __init__(self, update_action: str, delete_action: str, match: str, SQL2003_V2_ReferentialConstraint: "SQL2003_V2_UniqueConstraint" = None):
        self.update_action = update_action
        self.delete_action = delete_action
        self.match = match
        self.SQL2003_V2_ReferentialConstraint = SQL2003_V2_ReferentialConstraint
        
    @property
    def match(self) -> str:
        return self.__match

    @match.setter
    def match(self, match: str):
        self.__match = match

    @property
    def update_action(self) -> str:
        return self.__update_action

    @update_action.setter
    def update_action(self, update_action: str):
        self.__update_action = update_action

    @property
    def delete_action(self) -> str:
        return self.__delete_action

    @delete_action.setter
    def delete_action(self, delete_action: str):
        self.__delete_action = delete_action

    @property
    def SQL2003_V2_ReferentialConstraint(self):
        return self.__SQL2003_V2_ReferentialConstraint

    @SQL2003_V2_ReferentialConstraint.setter
    def SQL2003_V2_ReferentialConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_ReferentialConstraint__SQL2003_V2_ReferentialConstraint", None)
        self.__SQL2003_V2_ReferentialConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V2_UniqueConstraint"):
                opp_val = getattr(old_value, "SQL2003_V2_UniqueConstraint", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V2_UniqueConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V2_UniqueConstraint"):
                opp_val = getattr(value, "SQL2003_V2_UniqueConstraint", None)
                setattr(value, "SQL2003_V2_UniqueConstraint", self)

class UniqueConstraint:

    pass
class SQL2003_V2_PrimaryKey(UniqueConstraint):

    pass
class SQL2003_V2_Parameter(ABC):

    def __init__(self, name: str, SQL2003_V2_Parameter: "SQL2003_V2_DataType" = None):
        self.name = name
        self.SQL2003_V2_Parameter = SQL2003_V2_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SQL2003_V2_Parameter(self):
        return self.__SQL2003_V2_Parameter

    @SQL2003_V2_Parameter.setter
    def SQL2003_V2_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Parameter__SQL2003_V2_Parameter", None)
        self.__SQL2003_V2_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V2_DataType25"):
                opp_val = getattr(old_value, "SQL2003_V2_DataType25", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V2_DataType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V2_DataType25"):
                opp_val = getattr(value, "SQL2003_V2_DataType25", None)
                setattr(value, "SQL2003_V2_DataType25", self)

class ColumnConstraint:

    pass
class SQL2003_V2_NotNull(ColumnConstraint):

    pass
class Parameter:

    pass
class SQL2003_V2_MethodParameter(Parameter):

    pass
class SQL2003_V2_Method:

    def __init__(self, name: str, body: str, SQL2003_V2_Method: "SQL2003_V2_Method" = None, SQL2003_V2_Method15: "SQL2003_V2_Method" = None, methods: "SQL2003_V2_StructuredType" = None, SQL2003_V2_Method20: "SQL2003_V2_DataType" = None, method: set["SQL2003_V2_MethodParameter"] = None, Method: "SQL2003_V2_MethodParameter" = None, Method66: "SQL2003_V2_StructuredType" = None):
        self.name = name
        self.body = body
        self.SQL2003_V2_Method = SQL2003_V2_Method
        self.SQL2003_V2_Method15 = SQL2003_V2_Method15
        self.methods = methods
        self.SQL2003_V2_Method20 = SQL2003_V2_Method20
        self.method = method if method is not None else set()
        self.Method = Method
        self.Method66 = Method66
        
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
    def SQL2003_V2_Method15(self):
        return self.__SQL2003_V2_Method15

    @SQL2003_V2_Method15.setter
    def SQL2003_V2_Method15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Method__SQL2003_V2_Method15", None)
        self.__SQL2003_V2_Method15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V2_Method"):
                opp_val = getattr(old_value, "SQL2003_V2_Method", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V2_Method", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V2_Method"):
                opp_val = getattr(value, "SQL2003_V2_Method", None)
                setattr(value, "SQL2003_V2_Method", self)

    @property
    def SQL2003_V2_Method(self):
        return self.__SQL2003_V2_Method

    @SQL2003_V2_Method.setter
    def SQL2003_V2_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Method__SQL2003_V2_Method", None)
        self.__SQL2003_V2_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V2_Method15"):
                opp_val = getattr(old_value, "SQL2003_V2_Method15", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V2_Method15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V2_Method15"):
                opp_val = getattr(value, "SQL2003_V2_Method15", None)
                setattr(value, "SQL2003_V2_Method15", self)

    @property
    def SQL2003_V2_Method20(self):
        return self.__SQL2003_V2_Method20

    @SQL2003_V2_Method20.setter
    def SQL2003_V2_Method20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Method__SQL2003_V2_Method20", None)
        self.__SQL2003_V2_Method20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V2_DataType21"):
                opp_val = getattr(old_value, "SQL2003_V2_DataType21", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V2_DataType21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V2_DataType21"):
                opp_val = getattr(value, "SQL2003_V2_DataType21", None)
                setattr(value, "SQL2003_V2_DataType21", self)

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Method__Method", None)
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
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Method__method", None)
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
                    

    @property
    def Method66(self):
        return self.__Method66

    @Method66.setter
    def Method66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Method__Method66", None)
        self.__Method66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structured65"):
                opp_val = getattr(old_value, "structured65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structured65"):
                opp_val = getattr(value, "structured65", None)
                if opp_val is None:
                    setattr(value, "structured65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Method__methods", None)
        self.__methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StructuredType18"):
                opp_val = getattr(old_value, "StructuredType18", None)
                if opp_val == self:
                    setattr(old_value, "StructuredType18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StructuredType18"):
                opp_val = getattr(value, "StructuredType18", None)
                setattr(value, "StructuredType18", self)

class BehaviouralComponent:

    pass
class SQL2003_V2_Procedure(BehaviouralComponent):

    pass
class SQL2003_V2_Function(BehaviouralComponent):

    pass
class SQL2003_V2_Feature(ABC):

    pass
class UserDefinedType:

    pass
class SQL2003_V2_DistinctType(UserDefinedType):

    pass
class Feature:

    pass
class SQL2003_V2_StringFeature(Feature):

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

class SQL2003_V2_IntervalFeature(Feature):

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

class SQL2003_V2_NumericFeature(Feature):

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

class SQL2003_V2_DatetimeFeature(Feature):

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
class SQL2003_V2_PredefinedType(DataType):

    pass
class SQL2003_V2_UserDefinedType(DataType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SQL2003_V2_ConstructedType(DataType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Restriction:

    pass
class SQL2003_V2_Trigger(Restriction):

    def __init__(self, name: str, trigger: "SQL2003_V2_TriggerDescriptor" = None, SQL2003_V2_Trigger: "SQL2003_V2_StructuralComponent" = None, Trigger: "SQL2003_V2_TriggerDescriptor" = None):
        self.name = name
        self.trigger = trigger
        self.SQL2003_V2_Trigger = SQL2003_V2_Trigger
        self.Trigger = Trigger
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SQL2003_V2_Trigger(self):
        return self.__SQL2003_V2_Trigger

    @SQL2003_V2_Trigger.setter
    def SQL2003_V2_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Trigger__SQL2003_V2_Trigger", None)
        self.__SQL2003_V2_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V2_StructuralComponent80"):
                opp_val = getattr(old_value, "SQL2003_V2_StructuralComponent80", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V2_StructuralComponent80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V2_StructuralComponent80"):
                opp_val = getattr(value, "SQL2003_V2_StructuralComponent80", None)
                setattr(value, "SQL2003_V2_StructuralComponent80", self)

    @property
    def Trigger(self):
        return self.__Trigger

    @Trigger.setter
    def Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Trigger__Trigger", None)
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

    @property
    def trigger(self):
        return self.__trigger

    @trigger.setter
    def trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Trigger__trigger", None)
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

class SQL2003_V2_TableConstraint(Restriction):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SQL2003_V2_ColumnConstraint(Restriction):

    pass
class SQL2003_V2_Table(ABC):

    def __init__(self, name: str, Table: "SQL2003_V2_Column" = None, Table47: "SQL2003_V2_Schema" = None, Table38: "SQL2003_V2_Restriction" = None, tables: "SQL2003_V2_Schema" = None, table: set["SQL2003_V2_Column"] = None, tables73: set["SQL2003_V2_View"] = None, table76: set["SQL2003_V2_Restriction"] = None, Table91: "SQL2003_V2_View" = None):
        self.name = name
        self.Table = Table
        self.Table47 = Table47
        self.Table38 = Table38
        self.tables = tables
        self.table = table if table is not None else set()
        self.tables73 = tables73 if tables73 is not None else set()
        self.table76 = table76 if table76 is not None else set()
        self.Table91 = Table91
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Table91(self):
        return self.__Table91

    @Table91.setter
    def Table91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Table__Table91", None)
        self.__Table91 = value
        
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
    def tables73(self):
        return self.__tables73

    @tables73.setter
    def tables73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Table__tables73", None)
        self.__tables73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "View74"):
                    opp_val = getattr(item, "View74", None)
                    
                    if opp_val == self:
                        setattr(item, "View74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "View74"):
                    opp_val = getattr(item, "View74", None)
                    
                    setattr(item, "View74", self)
                    

    @property
    def tables(self):
        return self.__tables

    @tables.setter
    def tables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Table__tables", None)
        self.__tables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema70"):
                opp_val = getattr(old_value, "Schema70", None)
                if opp_val == self:
                    setattr(old_value, "Schema70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema70"):
                opp_val = getattr(value, "Schema70", None)
                setattr(value, "Schema70", self)

    @property
    def Table47(self):
        return self.__Table47

    @Table47.setter
    def Table47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Table__Table47", None)
        self.__Table47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema46"):
                opp_val = getattr(old_value, "schema46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema46"):
                opp_val = getattr(value, "schema46", None)
                if opp_val is None:
                    setattr(value, "schema46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Table__Table", None)
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
    def Table38(self):
        return self.__Table38

    @Table38.setter
    def Table38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Table__Table38", None)
        self.__Table38 = value
        
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

    @property
    def table76(self):
        return self.__table76

    @table76.setter
    def table76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Table__table76", None)
        self.__table76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Restriction77"):
                    opp_val = getattr(item, "Restriction77", None)
                    
                    if opp_val == self:
                        setattr(item, "Restriction77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Restriction77"):
                    opp_val = getattr(item, "Restriction77", None)
                    
                    setattr(item, "Restriction77", self)
                    

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Table__table", None)
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
                    

class SQL2003_V2_DataType(ABC):

    pass
class ConstructedType:

    pass
class SQL2003_V2_ROW(ConstructedType):

    pass
class SQL2003_V2_ReferenceType(ConstructedType):

    pass
class SQL2003_V2_CollectionType(ConstructedType):

    pass
class SQL2003_V2_ParameterWithMode(Parameter):

    def __init__(self, mode: str, ParameterWithMode: "SQL2003_V2_BehaviouralComponent" = None, parametersWithMode: "SQL2003_V2_BehaviouralComponent" = None):
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
        old_value = getattr(self, f"_SQL2003_V2_ParameterWithMode__parametersWithMode", None)
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
        old_value = getattr(self, f"_SQL2003_V2_ParameterWithMode__ParameterWithMode", None)
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

class SQL2003_V2_Schema:

    def __init__(self, name: str, Schema: "SQL2003_V2_BehaviouralComponent" = None, Schema9: "SQL2003_V2_DataType" = None, schema46: set["SQL2003_V2_Table"] = None, schema: set["SQL2003_V2_BehaviouralComponent"] = None, schema44: set["SQL2003_V2_DataType"] = None, schema49: set["SQL2003_V2_Domain"] = None, Schema70: "SQL2003_V2_Table" = None, Schema96: "SQL2003_V2_Domain" = None):
        self.name = name
        self.Schema = Schema
        self.Schema9 = Schema9
        self.schema46 = schema46 if schema46 is not None else set()
        self.schema = schema if schema is not None else set()
        self.schema44 = schema44 if schema44 is not None else set()
        self.schema49 = schema49 if schema49 is not None else set()
        self.Schema70 = Schema70
        self.Schema96 = Schema96
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Schema__schema", None)
        self.__schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BehaviouralComponent42"):
                    opp_val = getattr(item, "BehaviouralComponent42", None)
                    
                    if opp_val == self:
                        setattr(item, "BehaviouralComponent42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BehaviouralComponent42"):
                    opp_val = getattr(item, "BehaviouralComponent42", None)
                    
                    setattr(item, "BehaviouralComponent42", self)
                    

    @property
    def Schema9(self):
        return self.__Schema9

    @Schema9.setter
    def Schema9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Schema__Schema9", None)
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
    def schema44(self):
        return self.__schema44

    @schema44.setter
    def schema44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Schema__schema44", None)
        self.__schema44 = value if value is not None else set()
        
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
    def Schema(self):
        return self.__Schema

    @Schema.setter
    def Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Schema__Schema", None)
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
    def schema49(self):
        return self.__schema49

    @schema49.setter
    def schema49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Schema__schema49", None)
        self.__schema49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Domain"):
                    opp_val = getattr(item, "Domain", None)
                    
                    if opp_val == self:
                        setattr(item, "Domain", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Domain"):
                    opp_val = getattr(item, "Domain", None)
                    
                    setattr(item, "Domain", self)
                    

    @property
    def Schema70(self):
        return self.__Schema70

    @Schema70.setter
    def Schema70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Schema__Schema70", None)
        self.__Schema70 = value
        
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
    def Schema96(self):
        return self.__Schema96

    @Schema96.setter
    def Schema96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Schema__Schema96", None)
        self.__Schema96 = value
        
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

    @property
    def schema46(self):
        return self.__schema46

    @schema46.setter
    def schema46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Schema__schema46", None)
        self.__schema46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table47"):
                    opp_val = getattr(item, "Table47", None)
                    
                    if opp_val == self:
                        setattr(item, "Table47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table47"):
                    opp_val = getattr(item, "Table47", None)
                    
                    setattr(item, "Table47", self)
                    

class SQL2003_V2_BehaviouralComponent(ABC):

    def __init__(self, name: str, body: str, behaviouralComponents: "SQL2003_V2_Schema" = None, behaviouralComponent: set["SQL2003_V2_ParameterWithMode"] = None, BehaviouralComponent: "SQL2003_V2_ParameterWithMode" = None, BehaviouralComponent42: "SQL2003_V2_Schema" = None):
        self.name = name
        self.body = body
        self.behaviouralComponents = behaviouralComponents
        self.behaviouralComponent = behaviouralComponent if behaviouralComponent is not None else set()
        self.BehaviouralComponent = BehaviouralComponent
        self.BehaviouralComponent42 = BehaviouralComponent42
        
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
    def behaviouralComponents(self):
        return self.__behaviouralComponents

    @behaviouralComponents.setter
    def behaviouralComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_BehaviouralComponent__behaviouralComponents", None)
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
    def BehaviouralComponent42(self):
        return self.__BehaviouralComponent42

    @BehaviouralComponent42.setter
    def BehaviouralComponent42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_BehaviouralComponent__BehaviouralComponent42", None)
        self.__BehaviouralComponent42 = value
        
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
    def behaviouralComponent(self):
        return self.__behaviouralComponent

    @behaviouralComponent.setter
    def behaviouralComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_BehaviouralComponent__behaviouralComponent", None)
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
                    

    @property
    def BehaviouralComponent(self):
        return self.__BehaviouralComponent

    @BehaviouralComponent.setter
    def BehaviouralComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_BehaviouralComponent__BehaviouralComponent", None)
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

class Table:

    pass
class SQL2003_V2_DerivedTable(Table):

    def __init__(self, query_expression: str):
        self.query_expression = query_expression
        
    @property
    def query_expression(self) -> str:
        return self.__query_expression

    @query_expression.setter
    def query_expression(self, query_expression: str):
        self.__query_expression = query_expression

class SQL2003_V2_BaseTable(Table):

    pass
class SQL2003_V2_StructuredType(UserDefinedType):

    def __init__(self, is_final: bool, is_instantiable: bool, StructuredType: "SQL2003_V2_Attribute" = None, StructuredType18: "SQL2003_V2_Method" = None, SQL2003_V2_StructuredType: "SQL2003_V2_ReferenceType" = None, SQL2003_V2_StructuredType62: "SQL2003_V2_StructuredType" = None, SQL2003_V2_StructuredType60: "SQL2003_V2_StructuredType" = None, structured: set["SQL2003_V2_Attribute"] = None, structured65: set["SQL2003_V2_Method"] = None, structured68: set["SQL2003_V2_TypedTable"] = None, StructuredType83: "SQL2003_V2_TypedTable" = None):
        self.is_final = is_final
        self.is_instantiable = is_instantiable
        self.StructuredType = StructuredType
        self.StructuredType18 = StructuredType18
        self.SQL2003_V2_StructuredType = SQL2003_V2_StructuredType
        self.SQL2003_V2_StructuredType62 = SQL2003_V2_StructuredType62
        self.SQL2003_V2_StructuredType60 = SQL2003_V2_StructuredType60
        self.structured = structured if structured is not None else set()
        self.structured65 = structured65 if structured65 is not None else set()
        self.structured68 = structured68 if structured68 is not None else set()
        self.StructuredType83 = StructuredType83
        
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
    def StructuredType(self):
        return self.__StructuredType

    @StructuredType.setter
    def StructuredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuredType__StructuredType", None)
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
    def SQL2003_V2_StructuredType62(self):
        return self.__SQL2003_V2_StructuredType62

    @SQL2003_V2_StructuredType62.setter
    def SQL2003_V2_StructuredType62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuredType__SQL2003_V2_StructuredType62", None)
        self.__SQL2003_V2_StructuredType62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V2_StructuredType60"):
                opp_val = getattr(old_value, "SQL2003_V2_StructuredType60", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V2_StructuredType60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V2_StructuredType60"):
                opp_val = getattr(value, "SQL2003_V2_StructuredType60", None)
                setattr(value, "SQL2003_V2_StructuredType60", self)

    @property
    def StructuredType83(self):
        return self.__StructuredType83

    @StructuredType83.setter
    def StructuredType83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuredType__StructuredType83", None)
        self.__StructuredType83 = value
        
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

    @property
    def structured(self):
        return self.__structured

    @structured.setter
    def structured(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuredType__structured", None)
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
    def structured65(self):
        return self.__structured65

    @structured65.setter
    def structured65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuredType__structured65", None)
        self.__structured65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method66"):
                    opp_val = getattr(item, "Method66", None)
                    
                    if opp_val == self:
                        setattr(item, "Method66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method66"):
                    opp_val = getattr(item, "Method66", None)
                    
                    setattr(item, "Method66", self)
                    

    @property
    def SQL2003_V2_StructuredType(self):
        return self.__SQL2003_V2_StructuredType

    @SQL2003_V2_StructuredType.setter
    def SQL2003_V2_StructuredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuredType__SQL2003_V2_StructuredType", None)
        self.__SQL2003_V2_StructuredType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V2_ReferenceType"):
                opp_val = getattr(old_value, "SQL2003_V2_ReferenceType", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V2_ReferenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V2_ReferenceType"):
                opp_val = getattr(value, "SQL2003_V2_ReferenceType", None)
                setattr(value, "SQL2003_V2_ReferenceType", self)

    @property
    def structured68(self):
        return self.__structured68

    @structured68.setter
    def structured68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuredType__structured68", None)
        self.__structured68 = value if value is not None else set()
        
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
    def StructuredType18(self):
        return self.__StructuredType18

    @StructuredType18.setter
    def StructuredType18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuredType__StructuredType18", None)
        self.__StructuredType18 = value
        
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
    def SQL2003_V2_StructuredType60(self):
        return self.__SQL2003_V2_StructuredType60

    @SQL2003_V2_StructuredType60.setter
    def SQL2003_V2_StructuredType60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_StructuredType__SQL2003_V2_StructuredType60", None)
        self.__SQL2003_V2_StructuredType60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_V2_StructuredType62"):
                opp_val = getattr(old_value, "SQL2003_V2_StructuredType62", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_V2_StructuredType62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_V2_StructuredType62"):
                opp_val = getattr(value, "SQL2003_V2_StructuredType62", None)
                setattr(value, "SQL2003_V2_StructuredType62", self)

class StructuralComponent:

    pass
class SQL2003_V2_Column(StructuralComponent):

    def __init__(self, default: str, columns: "SQL2003_V2_Table" = None, Column: "SQL2003_V2_Table" = None):
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
        old_value = getattr(self, f"_SQL2003_V2_Column__Column", None)
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
        old_value = getattr(self, f"_SQL2003_V2_Column__columns", None)
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

class SQL2003_V2_Field(StructuralComponent):

    pass
class SQL2003_V2_Attribute(StructuralComponent):

    def __init__(self, default: str, attributes: "SQL2003_V2_StructuredType" = None, Attribute: "SQL2003_V2_StructuredType" = None):
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
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Attribute__Attribute", None)
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

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_V2_Attribute__attributes", None)
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

class CollectionType:

    pass
class SQL2003_V2_MULTISET(CollectionType):

    pass
class SQL2003_V2_ARRAY(CollectionType):

    def __init__(self, num_elements: str):
        self.num_elements = num_elements
        
    @property
    def num_elements(self) -> str:
        return self.__num_elements

    @num_elements.setter
    def num_elements(self, num_elements: str):
        self.__num_elements = num_elements

class PredefinedType:

    pass
class SQL2003_V2_IntervalType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_V2_XMLType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_V2_CharacterStringType(PredefinedType):

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

class SQL2003_V2_BooleanType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_V2_NumericType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_V2_DatetimeType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_V2_BinaryStringType(PredefinedType):

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
