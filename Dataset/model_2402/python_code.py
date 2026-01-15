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
class StringFeatures(Enum):
    length = "length"
    unit = "unit"
    multiplier = "multiplier"
class ReferentialAction(Enum):
    CASCADE = "CASCADE"
    SET_NULL = "SET_NULL"
    RESTRICT = "RESTRICT"
    NO_ACTION = "NO_ACTION"
    SET_DEFAULT = "SET_DEFAULT"
class NumericTypes(Enum):
    BIGINT = "BIGINT"
    FLOAT = "FLOAT"
    REAL = "REAL"
    DOUBLEPRECISION = "DOUBLEPRECISION"
    NUMERIC = "NUMERIC"
    DECIMAL = "DECIMAL"
    SMALLINT = "SMALLINT"
    INTEGER = "INTEGER"
class XMLTypes(Enum):
    XMLTYPE = "XMLTYPE"
class NumericFeatures(Enum):
    precision = "precision"
    scale = "scale"
    radix = "radix"
class DatetimeFeatures(Enum):
    precision = "precision"
class DatetimeTypes(Enum):
    DATE = "DATE"
    TIMEWITHTIMEZONE = "TIMEWITHTIMEZONE"
    TIMEWITHOUTTIMEZONE = "TIMEWITHOUTTIMEZONE"
    TIMESTAMPWITHOUTTIMEZONE = "TIMESTAMPWITHOUTTIMEZONE"
    TIMESTAMPWITHTIMEZONE = "TIMESTAMPWITHTIMEZONE"
class NumericRadix(Enum):
    DECIMAL = "DECIMAL"
    BINARY = "BINARY"
class TriggerEvent(Enum):
    INSERT = "INSERT"
    DELETE = "DELETE"
    UPDATE = "UPDATE"
class IntervalFeatures(Enum):
    second_precision = "second_precision"
    start_leading_precision = "start_leading_precision"
    end_leading_precision = "end_leading_precision"
    leading_precision = "leading_precision"
class Unit(Enum):
    CHARACTERS = "CHARACTERS"
    OCTETS = "OCTETS"
class MatchTypes(Enum):
    SIMPLE = "SIMPLE"
    PARTIAL = "PARTIAL"
    TOTAL = "TOTAL"
class CharacterStringTypes(Enum):
    CHARACTER = "CHARACTER"
    CHARACTERVARYING = "CHARACTERVARYING"
    CHARACTERLARGEOBJECT = "CHARACTERLARGEOBJECT"
class BooleanTypes(Enum):
    BOOLEAN = "BOOLEAN"
class IntervalTypes(Enum):
    YEAR_MONTH = "YEAR_MONTH"
    DAY_HOUR = "DAY_HOUR"
    DAY_MINUTE = "DAY_MINUTE"
    DAY_SECOND = "DAY_SECOND"
    HOUR_MINUTE = "HOUR_MINUTE"
    HOUR_SECOND = "HOUR_SECOND"
    MINUTE_SECOND = "MINUTE_SECOND"
    YEAR = "YEAR"
    MONTH = "MONTH"
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"
    SECOND = "SECOND"
class BinaryStringTypes(Enum):
    BINARYLARGEOBJECT = "BINARYLARGEOBJECT"
    BINARY = "BINARY"
    BINARYVARYING = "BINARYVARYING"
class ParameterMode(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class TriggerActionTime(Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"


############################################
# Definition of Classes
############################################

class DerivedTable:

    pass
class BaseTable:

    pass
class SQL2003_Trigger:

    def __init__(self, name: str, event: str, actionTime: str, triggeredAction: str, triggers: "SQL2003_Table" = None, Trigger: "SQL2003_Table" = None, SQL2003_Trigger: set["SQL2003_StructuralComponent"] = None):
        self.name = name
        self.event = event
        self.actionTime = actionTime
        self.triggeredAction = triggeredAction
        self.triggers = triggers
        self.Trigger = Trigger
        self.SQL2003_Trigger = SQL2003_Trigger if SQL2003_Trigger is not None else set()
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def actionTime(self) -> str:
        return self.__actionTime

    @actionTime.setter
    def actionTime(self, actionTime: str):
        self.__actionTime = actionTime

    @property
    def SQL2003_Trigger(self):
        return self.__SQL2003_Trigger

    @SQL2003_Trigger.setter
    def SQL2003_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Trigger__SQL2003_Trigger", None)
        self.__SQL2003_Trigger = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SQL2003_StructuralComponent79"):
                    opp_val = getattr(item, "SQL2003_StructuralComponent79", None)
                    
                    if opp_val == self:
                        setattr(item, "SQL2003_StructuralComponent79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SQL2003_StructuralComponent79"):
                    opp_val = getattr(item, "SQL2003_StructuralComponent79", None)
                    
                    setattr(item, "SQL2003_StructuralComponent79", self)
                    

    @property
    def triggers(self):
        return self.__triggers

    @triggers.setter
    def triggers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Trigger__triggers", None)
        self.__triggers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table77"):
                opp_val = getattr(old_value, "Table77", None)
                if opp_val == self:
                    setattr(old_value, "Table77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table77"):
                opp_val = getattr(value, "Table77", None)
                setattr(value, "Table77", self)

    @property
    def Trigger(self):
        return self.__Trigger

    @Trigger.setter
    def Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Trigger__Trigger", None)
        self.__Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table72"):
                opp_val = getattr(old_value, "table72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table72"):
                opp_val = getattr(value, "table72", None)
                if opp_val is None:
                    setattr(value, "table72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SQL2003_TypedTable(BaseTable):

    pass
class SQL2003_View(DerivedTable):

    pass
class TableConstraint:

    pass
class SQL2003_TableCheckConstraint(TableConstraint):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class SQL2003_ReferentialConstraint(TableConstraint):

    def __init__(self, delete_action: str, update_action: str, match: str, SQL2003_ReferentialConstraint: "SQL2003_UniqueConstraint" = None):
        self.delete_action = delete_action
        self.update_action = update_action
        self.match = match
        self.SQL2003_ReferentialConstraint = SQL2003_ReferentialConstraint
        
    @property
    def update_action(self) -> str:
        return self.__update_action

    @update_action.setter
    def update_action(self, update_action: str):
        self.__update_action = update_action

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
    def SQL2003_ReferentialConstraint(self):
        return self.__SQL2003_ReferentialConstraint

    @SQL2003_ReferentialConstraint.setter
    def SQL2003_ReferentialConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_ReferentialConstraint__SQL2003_ReferentialConstraint", None)
        self.__SQL2003_ReferentialConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_UniqueConstraint"):
                opp_val = getattr(old_value, "SQL2003_UniqueConstraint", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_UniqueConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_UniqueConstraint"):
                opp_val = getattr(value, "SQL2003_UniqueConstraint", None)
                setattr(value, "SQL2003_UniqueConstraint", self)

class SQL2003_StructuralComponent(ABC):

    def __init__(self, name: str, StructuralComponent: "SQL2003_Restriction" = None, SQL2003_StructuralComponent: "SQL2003_DataType" = None, components: set["SQL2003_View"] = None, columns52: set["SQL2003_Restriction"] = None, SQL2003_StructuralComponent54: set["SQL2003_Feature"] = None, SQL2003_StructuralComponent79: "SQL2003_Trigger" = None, StructuralComponent92: "SQL2003_View" = None):
        self.name = name
        self.StructuralComponent = StructuralComponent
        self.SQL2003_StructuralComponent = SQL2003_StructuralComponent
        self.components = components if components is not None else set()
        self.columns52 = columns52 if columns52 is not None else set()
        self.SQL2003_StructuralComponent54 = SQL2003_StructuralComponent54 if SQL2003_StructuralComponent54 is not None else set()
        self.SQL2003_StructuralComponent79 = SQL2003_StructuralComponent79
        self.StructuralComponent92 = StructuralComponent92
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StructuralComponent(self):
        return self.__StructuralComponent

    @StructuralComponent.setter
    def StructuralComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuralComponent__StructuralComponent", None)
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
    def SQL2003_StructuralComponent(self):
        return self.__SQL2003_StructuralComponent

    @SQL2003_StructuralComponent.setter
    def SQL2003_StructuralComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuralComponent__SQL2003_StructuralComponent", None)
        self.__SQL2003_StructuralComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_DataType49"):
                opp_val = getattr(old_value, "SQL2003_DataType49", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_DataType49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_DataType49"):
                opp_val = getattr(value, "SQL2003_DataType49", None)
                setattr(value, "SQL2003_DataType49", self)

    @property
    def columns52(self):
        return self.__columns52

    @columns52.setter
    def columns52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuralComponent__columns52", None)
        self.__columns52 = value if value is not None else set()
        
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
    def SQL2003_StructuralComponent79(self):
        return self.__SQL2003_StructuralComponent79

    @SQL2003_StructuralComponent79.setter
    def SQL2003_StructuralComponent79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuralComponent__SQL2003_StructuralComponent79", None)
        self.__SQL2003_StructuralComponent79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_Trigger"):
                opp_val = getattr(old_value, "SQL2003_Trigger", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_Trigger"):
                opp_val = getattr(value, "SQL2003_Trigger", None)
                if opp_val is None:
                    setattr(value, "SQL2003_Trigger", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def components(self):
        return self.__components

    @components.setter
    def components(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuralComponent__components", None)
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
    def SQL2003_StructuralComponent54(self):
        return self.__SQL2003_StructuralComponent54

    @SQL2003_StructuralComponent54.setter
    def SQL2003_StructuralComponent54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuralComponent__SQL2003_StructuralComponent54", None)
        self.__SQL2003_StructuralComponent54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SQL2003_Feature55"):
                    opp_val = getattr(item, "SQL2003_Feature55", None)
                    
                    if opp_val == self:
                        setattr(item, "SQL2003_Feature55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SQL2003_Feature55"):
                    opp_val = getattr(item, "SQL2003_Feature55", None)
                    
                    setattr(item, "SQL2003_Feature55", self)
                    

    @property
    def StructuralComponent92(self):
        return self.__StructuralComponent92

    @StructuralComponent92.setter
    def StructuralComponent92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuralComponent__StructuralComponent92", None)
        self.__StructuralComponent92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "views91"):
                opp_val = getattr(old_value, "views91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "views91"):
                opp_val = getattr(value, "views91", None)
                if opp_val is None:
                    setattr(value, "views91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SQL2003_Restriction(ABC):

    pass
class SQL2003_UniqueConstraint(TableConstraint):

    pass
class UniqueConstraint:

    pass
class SQL2003_PrimaryKey(UniqueConstraint):

    pass
class SQL2003_Parameter(ABC):

    def __init__(self, name: str, SQL2003_Parameter: "SQL2003_DataType" = None):
        self.name = name
        self.SQL2003_Parameter = SQL2003_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SQL2003_Parameter(self):
        return self.__SQL2003_Parameter

    @SQL2003_Parameter.setter
    def SQL2003_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Parameter__SQL2003_Parameter", None)
        self.__SQL2003_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_DataType25"):
                opp_val = getattr(old_value, "SQL2003_DataType25", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_DataType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_DataType25"):
                opp_val = getattr(value, "SQL2003_DataType25", None)
                setattr(value, "SQL2003_DataType25", self)

class ColumnConstraint:

    pass
class SQL2003_NotNull(ColumnConstraint):

    pass
class Parameter:

    pass
class SQL2003_MethodParameter(Parameter):

    pass
class SQL2003_Method:

    def __init__(self, name: str, body: str, SQL2003_Method: "SQL2003_Method" = None, SQL2003_Method15: "SQL2003_Method" = None, methods: "SQL2003_StructuredType" = None, SQL2003_Method20: "SQL2003_DataType" = None, method: set["SQL2003_MethodParameter"] = None, Method: "SQL2003_MethodParameter" = None, Method62: "SQL2003_StructuredType" = None):
        self.name = name
        self.body = body
        self.SQL2003_Method = SQL2003_Method
        self.SQL2003_Method15 = SQL2003_Method15
        self.methods = methods
        self.SQL2003_Method20 = SQL2003_Method20
        self.method = method if method is not None else set()
        self.Method = Method
        self.Method62 = Method62
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SQL2003_Method(self):
        return self.__SQL2003_Method

    @SQL2003_Method.setter
    def SQL2003_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Method__SQL2003_Method", None)
        self.__SQL2003_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_Method15"):
                opp_val = getattr(old_value, "SQL2003_Method15", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_Method15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_Method15"):
                opp_val = getattr(value, "SQL2003_Method15", None)
                setattr(value, "SQL2003_Method15", self)

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Method__method", None)
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
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Method__methods", None)
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

    @property
    def Method62(self):
        return self.__Method62

    @Method62.setter
    def Method62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Method__Method62", None)
        self.__Method62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structured61"):
                opp_val = getattr(old_value, "structured61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structured61"):
                opp_val = getattr(value, "structured61", None)
                if opp_val is None:
                    setattr(value, "structured61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Method__Method", None)
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
    def SQL2003_Method15(self):
        return self.__SQL2003_Method15

    @SQL2003_Method15.setter
    def SQL2003_Method15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Method__SQL2003_Method15", None)
        self.__SQL2003_Method15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_Method"):
                opp_val = getattr(old_value, "SQL2003_Method", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_Method", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_Method"):
                opp_val = getattr(value, "SQL2003_Method", None)
                setattr(value, "SQL2003_Method", self)

    @property
    def SQL2003_Method20(self):
        return self.__SQL2003_Method20

    @SQL2003_Method20.setter
    def SQL2003_Method20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Method__SQL2003_Method20", None)
        self.__SQL2003_Method20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_DataType21"):
                opp_val = getattr(old_value, "SQL2003_DataType21", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_DataType21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_DataType21"):
                opp_val = getattr(value, "SQL2003_DataType21", None)
                setattr(value, "SQL2003_DataType21", self)

class UserDefinedType:

    pass
class SQL2003_DistinctType(UserDefinedType):

    pass
class BehaviouralComponent:

    pass
class SQL2003_Procedure(BehaviouralComponent):

    pass
class SQL2003_Function(BehaviouralComponent):

    pass
class SQL2003_Feature(ABC):

    pass
class DataType:

    pass
class SQL2003_UserDefinedType(DataType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SQL2003_PredefinedType(DataType):

    pass
class SQL2003_ConstructedType(DataType):

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
class SQL2003_TableConstraint(Restriction):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SQL2003_ColumnConstraint(Restriction):

    pass
class Feature:

    pass
class SQL2003_NumericFeature(Feature):

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

class SQL2003_IntervalFeature(Feature):

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

class SQL2003_StringFeature(Feature):

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

class SQL2003_DatetimeFeature(Feature):

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

class SQL2003_Table(ABC):

    def __init__(self, name: str, Table: "SQL2003_Column" = None, Table38: "SQL2003_Restriction" = None, Table47: "SQL2003_Schema" = None, tables: "SQL2003_Schema" = None, table: set["SQL2003_Column"] = None, table74: set["SQL2003_Restriction"] = None, Table77: "SQL2003_Trigger" = None, tables69: set["SQL2003_View"] = None, table72: set["SQL2003_Trigger"] = None, Table89: "SQL2003_View" = None):
        self.name = name
        self.Table = Table
        self.Table38 = Table38
        self.Table47 = Table47
        self.tables = tables
        self.table = table if table is not None else set()
        self.table74 = table74 if table74 is not None else set()
        self.Table77 = Table77
        self.tables69 = tables69 if tables69 is not None else set()
        self.table72 = table72 if table72 is not None else set()
        self.Table89 = Table89
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tables(self):
        return self.__tables

    @tables.setter
    def tables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Table__tables", None)
        self.__tables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema66"):
                opp_val = getattr(old_value, "Schema66", None)
                if opp_val == self:
                    setattr(old_value, "Schema66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema66"):
                opp_val = getattr(value, "Schema66", None)
                setattr(value, "Schema66", self)

    @property
    def tables69(self):
        return self.__tables69

    @tables69.setter
    def tables69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Table__tables69", None)
        self.__tables69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "View70"):
                    opp_val = getattr(item, "View70", None)
                    
                    if opp_val == self:
                        setattr(item, "View70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "View70"):
                    opp_val = getattr(item, "View70", None)
                    
                    setattr(item, "View70", self)
                    

    @property
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Table__Table", None)
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
    def Table47(self):
        return self.__Table47

    @Table47.setter
    def Table47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Table__Table47", None)
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
    def Table38(self):
        return self.__Table38

    @Table38.setter
    def Table38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Table__Table38", None)
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
    def table74(self):
        return self.__table74

    @table74.setter
    def table74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Table__table74", None)
        self.__table74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Restriction75"):
                    opp_val = getattr(item, "Restriction75", None)
                    
                    if opp_val == self:
                        setattr(item, "Restriction75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Restriction75"):
                    opp_val = getattr(item, "Restriction75", None)
                    
                    setattr(item, "Restriction75", self)
                    

    @property
    def table72(self):
        return self.__table72

    @table72.setter
    def table72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Table__table72", None)
        self.__table72 = value if value is not None else set()
        
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
    def Table77(self):
        return self.__Table77

    @Table77.setter
    def Table77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Table__Table77", None)
        self.__Table77 = value
        
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
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Table__table", None)
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
    def Table89(self):
        return self.__Table89

    @Table89.setter
    def Table89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Table__Table89", None)
        self.__Table89 = value
        
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

class SQL2003_DataType(ABC):

    pass
class ConstructedType:

    pass
class SQL2003_ROW(ConstructedType):

    pass
class SQL2003_ReferenceType(ConstructedType):

    pass
class SQL2003_CollectionType(ConstructedType):

    pass
class SQL2003_BehaviouralComponent(ABC):

    def __init__(self, name: str, body: str, behaviouralComponents: "SQL2003_Schema" = None, behaviouralComponent: set["SQL2003_ParameterWithMode"] = None, BehaviouralComponent: "SQL2003_ParameterWithMode" = None, BehaviouralComponent42: "SQL2003_Schema" = None):
        self.name = name
        self.body = body
        self.behaviouralComponents = behaviouralComponents
        self.behaviouralComponent = behaviouralComponent if behaviouralComponent is not None else set()
        self.BehaviouralComponent = BehaviouralComponent
        self.BehaviouralComponent42 = BehaviouralComponent42
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def behaviouralComponents(self):
        return self.__behaviouralComponents

    @behaviouralComponents.setter
    def behaviouralComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_BehaviouralComponent__behaviouralComponents", None)
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
        old_value = getattr(self, f"_SQL2003_BehaviouralComponent__behaviouralComponent", None)
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
        old_value = getattr(self, f"_SQL2003_BehaviouralComponent__BehaviouralComponent", None)
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
    def BehaviouralComponent42(self):
        return self.__BehaviouralComponent42

    @BehaviouralComponent42.setter
    def BehaviouralComponent42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_BehaviouralComponent__BehaviouralComponent42", None)
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

class Table:

    pass
class SQL2003_DerivedTable(Table):

    def __init__(self, query_expression: str):
        self.query_expression = query_expression
        
    @property
    def query_expression(self) -> str:
        return self.__query_expression

    @query_expression.setter
    def query_expression(self, query_expression: str):
        self.__query_expression = query_expression

class SQL2003_BaseTable(Table):

    pass
class PredefinedType:

    pass
class SQL2003_NumericType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_DatetimeType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_CharacterStringType(PredefinedType):

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

class SQL2003_BooleanType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_XMLType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_IntervalType(PredefinedType):

    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        
    @property
    def descriptor(self) -> str:
        return self.__descriptor

    @descriptor.setter
    def descriptor(self, descriptor: str):
        self.__descriptor = descriptor

class SQL2003_BinaryStringType(PredefinedType):

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

class SQL2003_ParameterWithMode(Parameter):

    def __init__(self, mode: str, ParameterWithMode: "SQL2003_BehaviouralComponent" = None, parametersWithMode: "SQL2003_BehaviouralComponent" = None):
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
        old_value = getattr(self, f"_SQL2003_ParameterWithMode__parametersWithMode", None)
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
        old_value = getattr(self, f"_SQL2003_ParameterWithMode__ParameterWithMode", None)
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

class SQL2003_Schema:

    def __init__(self, name: str, Schema: "SQL2003_BehaviouralComponent" = None, Schema9: "SQL2003_DataType" = None, schema: set["SQL2003_BehaviouralComponent"] = None, schema44: set["SQL2003_DataType"] = None, schema46: set["SQL2003_Table"] = None, Schema66: "SQL2003_Table" = None):
        self.name = name
        self.Schema = Schema
        self.Schema9 = Schema9
        self.schema = schema if schema is not None else set()
        self.schema44 = schema44 if schema44 is not None else set()
        self.schema46 = schema46 if schema46 is not None else set()
        self.Schema66 = Schema66
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def schema46(self):
        return self.__schema46

    @schema46.setter
    def schema46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Schema__schema46", None)
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
                    

    @property
    def schema44(self):
        return self.__schema44

    @schema44.setter
    def schema44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Schema__schema44", None)
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
    def Schema66(self):
        return self.__Schema66

    @Schema66.setter
    def Schema66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Schema__Schema66", None)
        self.__Schema66 = value
        
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
        old_value = getattr(self, f"_SQL2003_Schema__Schema9", None)
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
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Schema__schema", None)
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
    def Schema(self):
        return self.__Schema

    @Schema.setter
    def Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Schema__Schema", None)
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

class SQL2003_StructuredType(UserDefinedType):

    def __init__(self, is_instantiable: bool, is_final: bool, StructuredType: "SQL2003_Attribute" = None, StructuredType18: "SQL2003_Method" = None, SQL2003_StructuredType: "SQL2003_ReferenceType" = None, SQL2003_StructuredType58: "SQL2003_StructuredType" = None, SQL2003_StructuredType56: "SQL2003_StructuredType" = None, structured: set["SQL2003_Attribute"] = None, structured61: set["SQL2003_Method"] = None, structured64: set["SQL2003_TypedTable"] = None, StructuredType81: "SQL2003_TypedTable" = None):
        self.is_instantiable = is_instantiable
        self.is_final = is_final
        self.StructuredType = StructuredType
        self.StructuredType18 = StructuredType18
        self.SQL2003_StructuredType = SQL2003_StructuredType
        self.SQL2003_StructuredType58 = SQL2003_StructuredType58
        self.SQL2003_StructuredType56 = SQL2003_StructuredType56
        self.structured = structured if structured is not None else set()
        self.structured61 = structured61 if structured61 is not None else set()
        self.structured64 = structured64 if structured64 is not None else set()
        self.StructuredType81 = StructuredType81
        
    @property
    def is_final(self) -> bool:
        return self.__is_final

    @is_final.setter
    def is_final(self, is_final: bool):
        self.__is_final = is_final

    @property
    def is_instantiable(self) -> bool:
        return self.__is_instantiable

    @is_instantiable.setter
    def is_instantiable(self, is_instantiable: bool):
        self.__is_instantiable = is_instantiable

    @property
    def StructuredType81(self):
        return self.__StructuredType81

    @StructuredType81.setter
    def StructuredType81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuredType__StructuredType81", None)
        self.__StructuredType81 = value
        
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
    def structured61(self):
        return self.__structured61

    @structured61.setter
    def structured61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuredType__structured61", None)
        self.__structured61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method62"):
                    opp_val = getattr(item, "Method62", None)
                    
                    if opp_val == self:
                        setattr(item, "Method62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method62"):
                    opp_val = getattr(item, "Method62", None)
                    
                    setattr(item, "Method62", self)
                    

    @property
    def SQL2003_StructuredType56(self):
        return self.__SQL2003_StructuredType56

    @SQL2003_StructuredType56.setter
    def SQL2003_StructuredType56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuredType__SQL2003_StructuredType56", None)
        self.__SQL2003_StructuredType56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_StructuredType58"):
                opp_val = getattr(old_value, "SQL2003_StructuredType58", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_StructuredType58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_StructuredType58"):
                opp_val = getattr(value, "SQL2003_StructuredType58", None)
                setattr(value, "SQL2003_StructuredType58", self)

    @property
    def StructuredType18(self):
        return self.__StructuredType18

    @StructuredType18.setter
    def StructuredType18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuredType__StructuredType18", None)
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
    def StructuredType(self):
        return self.__StructuredType

    @StructuredType.setter
    def StructuredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuredType__StructuredType", None)
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
    def SQL2003_StructuredType58(self):
        return self.__SQL2003_StructuredType58

    @SQL2003_StructuredType58.setter
    def SQL2003_StructuredType58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuredType__SQL2003_StructuredType58", None)
        self.__SQL2003_StructuredType58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_StructuredType56"):
                opp_val = getattr(old_value, "SQL2003_StructuredType56", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_StructuredType56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_StructuredType56"):
                opp_val = getattr(value, "SQL2003_StructuredType56", None)
                setattr(value, "SQL2003_StructuredType56", self)

    @property
    def structured64(self):
        return self.__structured64

    @structured64.setter
    def structured64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuredType__structured64", None)
        self.__structured64 = value if value is not None else set()
        
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
    def structured(self):
        return self.__structured

    @structured.setter
    def structured(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuredType__structured", None)
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
    def SQL2003_StructuredType(self):
        return self.__SQL2003_StructuredType

    @SQL2003_StructuredType.setter
    def SQL2003_StructuredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_StructuredType__SQL2003_StructuredType", None)
        self.__SQL2003_StructuredType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQL2003_ReferenceType"):
                opp_val = getattr(old_value, "SQL2003_ReferenceType", None)
                if opp_val == self:
                    setattr(old_value, "SQL2003_ReferenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQL2003_ReferenceType"):
                opp_val = getattr(value, "SQL2003_ReferenceType", None)
                setattr(value, "SQL2003_ReferenceType", self)

class StructuralComponent:

    pass
class SQL2003_Column(StructuralComponent):

    def __init__(self, default: str, columns: "SQL2003_Table" = None, Column: "SQL2003_Table" = None):
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
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Column__columns", None)
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

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SQL2003_Column__Column", None)
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

class SQL2003_Field(StructuralComponent):

    pass
class SQL2003_Attribute(StructuralComponent):

    def __init__(self, default: str, attributes: "SQL2003_StructuredType" = None, Attribute: "SQL2003_StructuredType" = None):
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
        old_value = getattr(self, f"_SQL2003_Attribute__attributes", None)
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
        old_value = getattr(self, f"_SQL2003_Attribute__Attribute", None)
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

class CollectionType:

    pass
class SQL2003_MULTISET(CollectionType):

    pass
class SQL2003_ARRAY(CollectionType):

    def __init__(self, num_elements: str):
        self.num_elements = num_elements
        
    @property
    def num_elements(self) -> str:
        return self.__num_elements

    @num_elements.setter
    def num_elements(self, num_elements: str):
        self.__num_elements = num_elements
