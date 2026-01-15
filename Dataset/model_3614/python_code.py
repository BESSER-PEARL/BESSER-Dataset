from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DateTimePrecision(Enum):
    Year = "Year"
    Month = "Month"
    Week = "Week"
    Day = "Day"
    Hour = "Hour"
    Minute = "Minute"
    Second = "Second"
    Millisecond = "Millisecond"
class SortDirection(Enum):
    asc = "asc"
    ascending = "ascending"
    desc = "desc"
    descending = "descending"
class AccessModifier(Enum):
    Public = "Public"
    Private = "Private"


############################################
# Definition of Classes
############################################

class RelationshipClause:

    pass
class r1_Without(RelationshipClause):

    pass
class r1_With(RelationshipClause):

    pass
class r1_TupleElement:

    def __init__(self, name: str, r1_TupleElement: "r1_Tuple" = None, r1_TupleElement209: "r1_Expression" = None):
        self.name = name
        self.r1_TupleElement = r1_TupleElement
        self.r1_TupleElement209 = r1_TupleElement209
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def r1_TupleElement(self):
        return self.__r1_TupleElement

    @r1_TupleElement.setter
    def r1_TupleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_TupleElement__r1_TupleElement", None)
        self.__r1_TupleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Tuple"):
                opp_val = getattr(old_value, "r1_Tuple", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Tuple"):
                opp_val = getattr(value, "r1_Tuple", None)
                if opp_val is None:
                    setattr(value, "r1_Tuple", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def r1_TupleElement209(self):
        return self.__r1_TupleElement209

    @r1_TupleElement209.setter
    def r1_TupleElement209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_TupleElement__r1_TupleElement209", None)
        self.__r1_TupleElement209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression210"):
                opp_val = getattr(old_value, "r1_Expression210", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression210"):
                opp_val = getattr(value, "r1_Expression210", None)
                setattr(value, "r1_Expression210", self)

class AliasedQuerySource:

    pass
class r1_RelationshipClause(AliasedQuerySource):

    pass
class TypeSpecifier:

    pass
class r1_TupleTypeSpecifier(TypeSpecifier):

    pass
class r1_NamedTypeSpecifier(TypeSpecifier):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class r1_ListTypeSpecifier(TypeSpecifier):

    pass
class r1_IntervalTypeSpecifier(TypeSpecifier):

    pass
class r1_InstanceElement:

    def __init__(self, name: str, r1_InstanceElement94: "r1_Expression" = None, r1_InstanceElement: "r1_Instance" = None):
        self.name = name
        self.r1_InstanceElement94 = r1_InstanceElement94
        self.r1_InstanceElement = r1_InstanceElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def r1_InstanceElement(self):
        return self.__r1_InstanceElement

    @r1_InstanceElement.setter
    def r1_InstanceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_InstanceElement__r1_InstanceElement", None)
        self.__r1_InstanceElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Instance"):
                opp_val = getattr(old_value, "r1_Instance", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Instance"):
                opp_val = getattr(value, "r1_Instance", None)
                if opp_val is None:
                    setattr(value, "r1_Instance", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def r1_InstanceElement94(self):
        return self.__r1_InstanceElement94

    @r1_InstanceElement94.setter
    def r1_InstanceElement94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_InstanceElement__r1_InstanceElement94", None)
        self.__r1_InstanceElement94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression95"):
                opp_val = getattr(old_value, "r1_Expression95", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression95"):
                opp_val = getattr(value, "r1_Expression95", None)
                setattr(value, "r1_Expression95", self)

class ExpressionRef:

    pass
class r1_FunctionRef(ExpressionRef):

    pass
class ExpressionDef:

    pass
class r1_FunctionDef(ExpressionDef):

    pass
class r1_EObject:

    pass
class r1_Element(ABC):

    def __init__(self, localId: str, r1_Element: set["r1_EObject"] = None):
        self.localId = localId
        self.r1_Element = r1_Element if r1_Element is not None else set()
        
    @property
    def localId(self) -> str:
        return self.__localId

    @localId.setter
    def localId(self, localId: str):
        self.__localId = localId

    @property
    def r1_Element(self):
        return self.__r1_Element

    @r1_Element.setter
    def r1_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Element__r1_Element", None)
        self.__r1_Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "r1_EObject"):
                    opp_val = getattr(item, "r1_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "r1_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "r1_EObject"):
                    opp_val = getattr(item, "r1_EObject", None)
                    
                    setattr(item, "r1_EObject", self)
                    

class NaryExpression:

    pass
class r1_Concatenate(NaryExpression):

    pass
class r1_Coalesce(NaryExpression):

    pass
class SortByItem:

    pass
class r1_ByExpression(SortByItem):

    pass
class r1_ByDirection(SortByItem):

    pass
class r1_ByColumn(SortByItem):

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class AggregateExpression:

    pass
class r1_Median(AggregateExpression):

    pass
class r1_Min(AggregateExpression):

    pass
class r1_Variance(AggregateExpression):

    pass
class r1_Mode(AggregateExpression):

    pass
class r1_Avg(AggregateExpression):

    pass
class r1_Count(AggregateExpression):

    pass
class r1_PopulationVariance(AggregateExpression):

    pass
class r1_StdDev(AggregateExpression):

    pass
class r1_AnyTrue(AggregateExpression):

    pass
class r1_Max(AggregateExpression):

    pass
class r1_PopulationStdDev(AggregateExpression):

    pass
class r1_Sum(AggregateExpression):

    pass
class r1_AllTrue(AggregateExpression):

    pass
class Element:

    pass
class r1_CaseItem(Element):

    pass
class r1_SortByItem(Element):

    def __init__(self, direction: str, r1_SortByItem: "r1_Sort" = None, r1_SortByItem177: "r1_SortClause" = None):
        self.direction = direction
        self.r1_SortByItem = r1_SortByItem
        self.r1_SortByItem177 = r1_SortByItem177
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def r1_SortByItem(self):
        return self.__r1_SortByItem

    @r1_SortByItem.setter
    def r1_SortByItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_SortByItem__r1_SortByItem", None)
        self.__r1_SortByItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Sort174"):
                opp_val = getattr(old_value, "r1_Sort174", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Sort174"):
                opp_val = getattr(value, "r1_Sort174", None)
                if opp_val is None:
                    setattr(value, "r1_Sort174", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def r1_SortByItem177(self):
        return self.__r1_SortByItem177

    @r1_SortByItem177.setter
    def r1_SortByItem177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_SortByItem__r1_SortByItem177", None)
        self.__r1_SortByItem177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_SortClause176"):
                opp_val = getattr(old_value, "r1_SortClause176", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_SortClause176"):
                opp_val = getattr(value, "r1_SortClause176", None)
                if opp_val is None:
                    setattr(value, "r1_SortClause176", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class r1_SortClause(Element):

    pass
class r1_OperandDef(Element):

    def __init__(self, name: str, operandType: str, r1_OperandDef: "r1_FunctionDef" = None, r1_OperandDef127: "r1_TypeSpecifier" = None):
        self.name = name
        self.operandType = operandType
        self.r1_OperandDef = r1_OperandDef
        self.r1_OperandDef127 = r1_OperandDef127
        
    @property
    def operandType(self) -> str:
        return self.__operandType

    @operandType.setter
    def operandType(self, operandType: str):
        self.__operandType = operandType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def r1_OperandDef127(self):
        return self.__r1_OperandDef127

    @r1_OperandDef127.setter
    def r1_OperandDef127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_OperandDef__r1_OperandDef127", None)
        self.__r1_OperandDef127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_TypeSpecifier128"):
                opp_val = getattr(old_value, "r1_TypeSpecifier128", None)
                if opp_val == self:
                    setattr(old_value, "r1_TypeSpecifier128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_TypeSpecifier128"):
                opp_val = getattr(value, "r1_TypeSpecifier128", None)
                setattr(value, "r1_TypeSpecifier128", self)

    @property
    def r1_OperandDef(self):
        return self.__r1_OperandDef

    @r1_OperandDef.setter
    def r1_OperandDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_OperandDef__r1_OperandDef", None)
        self.__r1_OperandDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_FunctionDef"):
                opp_val = getattr(old_value, "r1_FunctionDef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_FunctionDef"):
                opp_val = getattr(value, "r1_FunctionDef", None)
                if opp_val is None:
                    setattr(value, "r1_FunctionDef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class r1_CodeSystemDef(Element):

    def __init__(self, accessLevel: str, id: str, name: str, version: str):
        self.accessLevel = accessLevel
        self.id = id
        self.name = name
        self.version = version
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def accessLevel(self) -> str:
        return self.__accessLevel

    @accessLevel.setter
    def accessLevel(self, accessLevel: str):
        self.__accessLevel = accessLevel

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class r1_ExpressionDef(Element):

    def __init__(self, accessLevel: str, name: str, context: str, r1_ExpressionDef: "r1_Expression" = None):
        self.accessLevel = accessLevel
        self.name = name
        self.context = context
        self.r1_ExpressionDef = r1_ExpressionDef
        
    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def accessLevel(self) -> str:
        return self.__accessLevel

    @accessLevel.setter
    def accessLevel(self, accessLevel: str):
        self.__accessLevel = accessLevel

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def r1_ExpressionDef(self):
        return self.__r1_ExpressionDef

    @r1_ExpressionDef.setter
    def r1_ExpressionDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_ExpressionDef__r1_ExpressionDef", None)
        self.__r1_ExpressionDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression58"):
                opp_val = getattr(old_value, "r1_Expression58", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression58"):
                opp_val = getattr(value, "r1_Expression58", None)
                setattr(value, "r1_Expression58", self)

class r1_TypeSpecifier(Element):

    pass
class r1_ReturnClause(Element):

    def __init__(self, distinct: str, r1_ReturnClause: "r1_Query" = None, r1_ReturnClause164: "r1_Expression" = None):
        self.distinct = distinct
        self.r1_ReturnClause = r1_ReturnClause
        self.r1_ReturnClause164 = r1_ReturnClause164
        
    @property
    def distinct(self) -> str:
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: str):
        self.__distinct = distinct

    @property
    def r1_ReturnClause(self):
        return self.__r1_ReturnClause

    @r1_ReturnClause.setter
    def r1_ReturnClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_ReturnClause__r1_ReturnClause", None)
        self.__r1_ReturnClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Query152"):
                opp_val = getattr(old_value, "r1_Query152", None)
                if opp_val == self:
                    setattr(old_value, "r1_Query152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Query152"):
                opp_val = getattr(value, "r1_Query152", None)
                setattr(value, "r1_Query152", self)

    @property
    def r1_ReturnClause164(self):
        return self.__r1_ReturnClause164

    @r1_ReturnClause164.setter
    def r1_ReturnClause164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_ReturnClause__r1_ReturnClause164", None)
        self.__r1_ReturnClause164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression165"):
                opp_val = getattr(old_value, "r1_Expression165", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression165"):
                opp_val = getattr(value, "r1_Expression165", None)
                setattr(value, "r1_Expression165", self)

class r1_ParameterDef(Element):

    def __init__(self, accessLevel: str, name: str, parameterType: str, r1_ParameterDef: "r1_Expression" = None, r1_ParameterDef132: "r1_TypeSpecifier" = None):
        self.accessLevel = accessLevel
        self.name = name
        self.parameterType = parameterType
        self.r1_ParameterDef = r1_ParameterDef
        self.r1_ParameterDef132 = r1_ParameterDef132
        
    @property
    def accessLevel(self) -> str:
        return self.__accessLevel

    @accessLevel.setter
    def accessLevel(self, accessLevel: str):
        self.__accessLevel = accessLevel

    @property
    def parameterType(self) -> str:
        return self.__parameterType

    @parameterType.setter
    def parameterType(self, parameterType: str):
        self.__parameterType = parameterType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def r1_ParameterDef(self):
        return self.__r1_ParameterDef

    @r1_ParameterDef.setter
    def r1_ParameterDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_ParameterDef__r1_ParameterDef", None)
        self.__r1_ParameterDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression130"):
                opp_val = getattr(old_value, "r1_Expression130", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression130"):
                opp_val = getattr(value, "r1_Expression130", None)
                setattr(value, "r1_Expression130", self)

    @property
    def r1_ParameterDef132(self):
        return self.__r1_ParameterDef132

    @r1_ParameterDef132.setter
    def r1_ParameterDef132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_ParameterDef__r1_ParameterDef132", None)
        self.__r1_ParameterDef132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_TypeSpecifier133"):
                opp_val = getattr(old_value, "r1_TypeSpecifier133", None)
                if opp_val == self:
                    setattr(old_value, "r1_TypeSpecifier133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_TypeSpecifier133"):
                opp_val = getattr(value, "r1_TypeSpecifier133", None)
                setattr(value, "r1_TypeSpecifier133", self)

class r1_ValueSetDef(Element):

    def __init__(self, accessLevel: str, id: str, name: str, version: str, r1_ValueSetDef: set["r1_CodeSystemRef"] = None):
        self.accessLevel = accessLevel
        self.id = id
        self.name = name
        self.version = version
        self.r1_ValueSetDef = r1_ValueSetDef if r1_ValueSetDef is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accessLevel(self) -> str:
        return self.__accessLevel

    @accessLevel.setter
    def accessLevel(self, accessLevel: str):
        self.__accessLevel = accessLevel

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def r1_ValueSetDef(self):
        return self.__r1_ValueSetDef

    @r1_ValueSetDef.setter
    def r1_ValueSetDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_ValueSetDef__r1_ValueSetDef", None)
        self.__r1_ValueSetDef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "r1_CodeSystemRef218"):
                    opp_val = getattr(item, "r1_CodeSystemRef218", None)
                    
                    if opp_val == self:
                        setattr(item, "r1_CodeSystemRef218", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "r1_CodeSystemRef218"):
                    opp_val = getattr(item, "r1_CodeSystemRef218", None)
                    
                    setattr(item, "r1_CodeSystemRef218", self)
                    

class r1_DefineClause(Element):

    def __init__(self, identifier: str, r1_DefineClause: "r1_Expression" = None, r1_DefineClause145: "r1_Query" = None):
        self.identifier = identifier
        self.r1_DefineClause = r1_DefineClause
        self.r1_DefineClause145 = r1_DefineClause145
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def r1_DefineClause(self):
        return self.__r1_DefineClause

    @r1_DefineClause.setter
    def r1_DefineClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_DefineClause__r1_DefineClause", None)
        self.__r1_DefineClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression55"):
                opp_val = getattr(old_value, "r1_Expression55", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression55"):
                opp_val = getattr(value, "r1_Expression55", None)
                setattr(value, "r1_Expression55", self)

    @property
    def r1_DefineClause145(self):
        return self.__r1_DefineClause145

    @r1_DefineClause145.setter
    def r1_DefineClause145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_DefineClause__r1_DefineClause145", None)
        self.__r1_DefineClause145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Query144"):
                opp_val = getattr(old_value, "r1_Query144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Query144"):
                opp_val = getattr(value, "r1_Query144", None)
                if opp_val is None:
                    setattr(value, "r1_Query144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class r1_TupleElementDefinition(Element):

    def __init__(self, name: str, r1_TupleElementDefinition: "r1_TypeSpecifier" = None, r1_TupleElementDefinition214: "r1_TupleTypeSpecifier" = None):
        self.name = name
        self.r1_TupleElementDefinition = r1_TupleElementDefinition
        self.r1_TupleElementDefinition214 = r1_TupleElementDefinition214
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def r1_TupleElementDefinition214(self):
        return self.__r1_TupleElementDefinition214

    @r1_TupleElementDefinition214.setter
    def r1_TupleElementDefinition214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_TupleElementDefinition__r1_TupleElementDefinition214", None)
        self.__r1_TupleElementDefinition214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_TupleTypeSpecifier"):
                opp_val = getattr(old_value, "r1_TupleTypeSpecifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_TupleTypeSpecifier"):
                opp_val = getattr(value, "r1_TupleTypeSpecifier", None)
                if opp_val is None:
                    setattr(value, "r1_TupleTypeSpecifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def r1_TupleElementDefinition(self):
        return self.__r1_TupleElementDefinition

    @r1_TupleElementDefinition.setter
    def r1_TupleElementDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_TupleElementDefinition__r1_TupleElementDefinition", None)
        self.__r1_TupleElementDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_TypeSpecifier212"):
                opp_val = getattr(old_value, "r1_TypeSpecifier212", None)
                if opp_val == self:
                    setattr(old_value, "r1_TypeSpecifier212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_TypeSpecifier212"):
                opp_val = getattr(value, "r1_TypeSpecifier212", None)
                setattr(value, "r1_TypeSpecifier212", self)

class r1_AliasedQuerySource(Element):

    def __init__(self, alias: str, r1_AliasedQuerySource: "r1_Expression" = None, r1_AliasedQuerySource142: "r1_Query" = None):
        self.alias = alias
        self.r1_AliasedQuerySource = r1_AliasedQuerySource
        self.r1_AliasedQuerySource142 = r1_AliasedQuerySource142
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def r1_AliasedQuerySource142(self):
        return self.__r1_AliasedQuerySource142

    @r1_AliasedQuerySource142.setter
    def r1_AliasedQuerySource142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_AliasedQuerySource__r1_AliasedQuerySource142", None)
        self.__r1_AliasedQuerySource142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Query"):
                opp_val = getattr(old_value, "r1_Query", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Query"):
                opp_val = getattr(value, "r1_Query", None)
                if opp_val is None:
                    setattr(value, "r1_Query", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def r1_AliasedQuerySource(self):
        return self.__r1_AliasedQuerySource

    @r1_AliasedQuerySource.setter
    def r1_AliasedQuerySource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_AliasedQuerySource__r1_AliasedQuerySource", None)
        self.__r1_AliasedQuerySource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression2"):
                opp_val = getattr(old_value, "r1_Expression2", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression2"):
                opp_val = getattr(value, "r1_Expression2", None)
                setattr(value, "r1_Expression2", self)

class r1_Expression(Element):

    pass
class Expression:

    pass
class r1_InValueSet(Expression):

    pass
class r1_Query(Expression):

    pass
class r1_DateTime(Expression):

    pass
class r1_MaxValue(Expression):

    def __init__(self, valueType: str):
        self.valueType = valueType
        
    @property
    def valueType(self) -> str:
        return self.__valueType

    @valueType.setter
    def valueType(self, valueType: str):
        self.__valueType = valueType

class r1_Sort(Expression):

    pass
class r1_Round(Expression):

    pass
class r1_Quantity(Expression):

    def __init__(self, unit: str, value: str):
        self.unit = unit
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class r1_Interval(Expression):

    def __init__(self, lowClosed: str, highClosed: str, r1_Interval: "r1_Expression" = None, r1_Interval99: "r1_Expression" = None, r1_Interval102: "r1_Expression" = None, r1_Interval105: "r1_Expression" = None):
        self.lowClosed = lowClosed
        self.highClosed = highClosed
        self.r1_Interval = r1_Interval
        self.r1_Interval99 = r1_Interval99
        self.r1_Interval102 = r1_Interval102
        self.r1_Interval105 = r1_Interval105
        
    @property
    def lowClosed(self) -> str:
        return self.__lowClosed

    @lowClosed.setter
    def lowClosed(self, lowClosed: str):
        self.__lowClosed = lowClosed

    @property
    def highClosed(self) -> str:
        return self.__highClosed

    @highClosed.setter
    def highClosed(self, highClosed: str):
        self.__highClosed = highClosed

    @property
    def r1_Interval(self):
        return self.__r1_Interval

    @r1_Interval.setter
    def r1_Interval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Interval__r1_Interval", None)
        self.__r1_Interval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression97"):
                opp_val = getattr(old_value, "r1_Expression97", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression97"):
                opp_val = getattr(value, "r1_Expression97", None)
                setattr(value, "r1_Expression97", self)

    @property
    def r1_Interval105(self):
        return self.__r1_Interval105

    @r1_Interval105.setter
    def r1_Interval105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Interval__r1_Interval105", None)
        self.__r1_Interval105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression106"):
                opp_val = getattr(old_value, "r1_Expression106", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression106"):
                opp_val = getattr(value, "r1_Expression106", None)
                setattr(value, "r1_Expression106", self)

    @property
    def r1_Interval99(self):
        return self.__r1_Interval99

    @r1_Interval99.setter
    def r1_Interval99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Interval__r1_Interval99", None)
        self.__r1_Interval99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression100"):
                opp_val = getattr(old_value, "r1_Expression100", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression100"):
                opp_val = getattr(value, "r1_Expression100", None)
                setattr(value, "r1_Expression100", self)

    @property
    def r1_Interval102(self):
        return self.__r1_Interval102

    @r1_Interval102.setter
    def r1_Interval102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Interval__r1_Interval102", None)
        self.__r1_Interval102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression103"):
                opp_val = getattr(old_value, "r1_Expression103", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression103"):
                opp_val = getattr(value, "r1_Expression103", None)
                setattr(value, "r1_Expression103", self)

class r1_Filter(Expression):

    def __init__(self, scope: str, r1_Filter: "r1_Expression" = None, r1_Filter62: "r1_Expression" = None):
        self.scope = scope
        self.r1_Filter = r1_Filter
        self.r1_Filter62 = r1_Filter62
        
    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def r1_Filter62(self):
        return self.__r1_Filter62

    @r1_Filter62.setter
    def r1_Filter62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Filter__r1_Filter62", None)
        self.__r1_Filter62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression63"):
                opp_val = getattr(old_value, "r1_Expression63", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression63"):
                opp_val = getattr(value, "r1_Expression63", None)
                setattr(value, "r1_Expression63", self)

    @property
    def r1_Filter(self):
        return self.__r1_Filter

    @r1_Filter.setter
    def r1_Filter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Filter__r1_Filter", None)
        self.__r1_Filter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression60"):
                opp_val = getattr(old_value, "r1_Expression60", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression60"):
                opp_val = getattr(value, "r1_Expression60", None)
                setattr(value, "r1_Expression60", self)

class r1_Code(Expression):

    def __init__(self, code: str, display: str, r1_Code: "r1_CodeSystemRef" = None, r1_Code28: "r1_Concept" = None):
        self.code = code
        self.display = display
        self.r1_Code = r1_Code
        self.r1_Code28 = r1_Code28
        
    @property
    def display(self) -> str:
        return self.__display

    @display.setter
    def display(self, display: str):
        self.__display = display

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def r1_Code(self):
        return self.__r1_Code

    @r1_Code.setter
    def r1_Code(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Code__r1_Code", None)
        self.__r1_Code = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_CodeSystemRef"):
                opp_val = getattr(old_value, "r1_CodeSystemRef", None)
                if opp_val == self:
                    setattr(old_value, "r1_CodeSystemRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_CodeSystemRef"):
                opp_val = getattr(value, "r1_CodeSystemRef", None)
                setattr(value, "r1_CodeSystemRef", self)

    @property
    def r1_Code28(self):
        return self.__r1_Code28

    @r1_Code28.setter
    def r1_Code28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Code__r1_Code28", None)
        self.__r1_Code28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Concept"):
                opp_val = getattr(old_value, "r1_Concept", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Concept"):
                opp_val = getattr(value, "r1_Concept", None)
                if opp_val is None:
                    setattr(value, "r1_Concept", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class r1_Split(Expression):

    pass
class r1_QueryDefineRef(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class r1_Time(Expression):

    pass
class r1_NaryExpression(Expression):

    pass
class r1_MinValue(Expression):

    def __init__(self, valueType: str):
        self.valueType = valueType
        
    @property
    def valueType(self) -> str:
        return self.__valueType

    @valueType.setter
    def valueType(self, valueType: str):
        self.__valueType = valueType

class r1_Tuple(Expression):

    pass
class r1_Last(Expression):

    def __init__(self, orderBy: str, r1_Last: "r1_Expression" = None):
        self.orderBy = orderBy
        self.r1_Last = r1_Last
        
    @property
    def orderBy(self) -> str:
        return self.__orderBy

    @orderBy.setter
    def orderBy(self, orderBy: str):
        self.__orderBy = orderBy

    @property
    def r1_Last(self):
        return self.__r1_Last

    @r1_Last.setter
    def r1_Last(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Last__r1_Last", None)
        self.__r1_Last = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression116"):
                opp_val = getattr(old_value, "r1_Expression116", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression116"):
                opp_val = getattr(value, "r1_Expression116", None)
                setattr(value, "r1_Expression116", self)

class r1_ExpressionRef(Expression):

    def __init__(self, libraryName: str, name: str):
        self.libraryName = libraryName
        self.name = name
        
    @property
    def libraryName(self) -> str:
        return self.__libraryName

    @libraryName.setter
    def libraryName(self, libraryName: str):
        self.__libraryName = libraryName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class r1_Instance(Expression):

    def __init__(self, classType: str, r1_Instance: set["r1_InstanceElement"] = None):
        self.classType = classType
        self.r1_Instance = r1_Instance if r1_Instance is not None else set()
        
    @property
    def classType(self) -> str:
        return self.__classType

    @classType.setter
    def classType(self, classType: str):
        self.__classType = classType

    @property
    def r1_Instance(self):
        return self.__r1_Instance

    @r1_Instance.setter
    def r1_Instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Instance__r1_Instance", None)
        self.__r1_Instance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "r1_InstanceElement"):
                    opp_val = getattr(item, "r1_InstanceElement", None)
                    
                    if opp_val == self:
                        setattr(item, "r1_InstanceElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "r1_InstanceElement"):
                    opp_val = getattr(item, "r1_InstanceElement", None)
                    
                    setattr(item, "r1_InstanceElement", self)
                    

class r1_UnaryExpression(Expression):

    pass
class r1_Retrieve(Expression):

    def __init__(self, dataType: str, dateHighProperty: str, dateLowProperty: str, dateProperty: str, idProperty: str, scope: str, templateId: str, codeProperty: str, r1_Retrieve: "r1_Expression" = None, r1_Retrieve161: "r1_Expression" = None):
        self.dataType = dataType
        self.dateHighProperty = dateHighProperty
        self.dateLowProperty = dateLowProperty
        self.dateProperty = dateProperty
        self.idProperty = idProperty
        self.scope = scope
        self.templateId = templateId
        self.codeProperty = codeProperty
        self.r1_Retrieve = r1_Retrieve
        self.r1_Retrieve161 = r1_Retrieve161
        
    @property
    def dateProperty(self) -> str:
        return self.__dateProperty

    @dateProperty.setter
    def dateProperty(self, dateProperty: str):
        self.__dateProperty = dateProperty

    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def dateHighProperty(self) -> str:
        return self.__dateHighProperty

    @dateHighProperty.setter
    def dateHighProperty(self, dateHighProperty: str):
        self.__dateHighProperty = dateHighProperty

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def codeProperty(self) -> str:
        return self.__codeProperty

    @codeProperty.setter
    def codeProperty(self, codeProperty: str):
        self.__codeProperty = codeProperty

    @property
    def templateId(self) -> str:
        return self.__templateId

    @templateId.setter
    def templateId(self, templateId: str):
        self.__templateId = templateId

    @property
    def idProperty(self) -> str:
        return self.__idProperty

    @idProperty.setter
    def idProperty(self, idProperty: str):
        self.__idProperty = idProperty

    @property
    def dateLowProperty(self) -> str:
        return self.__dateLowProperty

    @dateLowProperty.setter
    def dateLowProperty(self, dateLowProperty: str):
        self.__dateLowProperty = dateLowProperty

    @property
    def r1_Retrieve(self):
        return self.__r1_Retrieve

    @r1_Retrieve.setter
    def r1_Retrieve(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Retrieve__r1_Retrieve", None)
        self.__r1_Retrieve = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression159"):
                opp_val = getattr(old_value, "r1_Expression159", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression159"):
                opp_val = getattr(value, "r1_Expression159", None)
                setattr(value, "r1_Expression159", self)

    @property
    def r1_Retrieve161(self):
        return self.__r1_Retrieve161

    @r1_Retrieve161.setter
    def r1_Retrieve161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Retrieve__r1_Retrieve161", None)
        self.__r1_Retrieve161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression162"):
                opp_val = getattr(old_value, "r1_Expression162", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression162"):
                opp_val = getattr(value, "r1_Expression162", None)
                setattr(value, "r1_Expression162", self)

class r1_First(Expression):

    def __init__(self, orderBy: str, r1_First: "r1_Expression" = None):
        self.orderBy = orderBy
        self.r1_First = r1_First
        
    @property
    def orderBy(self) -> str:
        return self.__orderBy

    @orderBy.setter
    def orderBy(self, orderBy: str):
        self.__orderBy = orderBy

    @property
    def r1_First(self):
        return self.__r1_First

    @r1_First.setter
    def r1_First(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_First__r1_First", None)
        self.__r1_First = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression65"):
                opp_val = getattr(old_value, "r1_Expression65", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression65"):
                opp_val = getattr(value, "r1_Expression65", None)
                setattr(value, "r1_Expression65", self)

class r1_Property(Expression):

    def __init__(self, path: str, scope: str, r1_Property: "r1_Expression" = None):
        self.path = path
        self.scope = scope
        self.r1_Property = r1_Property
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def r1_Property(self):
        return self.__r1_Property

    @r1_Property.setter
    def r1_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Property__r1_Property", None)
        self.__r1_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression140"):
                opp_val = getattr(old_value, "r1_Expression140", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression140"):
                opp_val = getattr(value, "r1_Expression140", None)
                setattr(value, "r1_Expression140", self)

class r1_Now(Expression):

    pass
class r1_BinaryExpression(Expression):

    pass
class r1_PositionOf(Expression):

    pass
class r1_List(Expression):

    pass
class r1_IdentifierRef(Expression):

    def __init__(self, libraryName: str, name: str):
        self.libraryName = libraryName
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def libraryName(self) -> str:
        return self.__libraryName

    @libraryName.setter
    def libraryName(self, libraryName: str):
        self.__libraryName = libraryName

class r1_TernaryExpression(Expression):

    pass
class r1_ValueSetRef(Expression):

    def __init__(self, libraryName: str, name: str, r1_ValueSetRef: "r1_InValueSet" = None):
        self.libraryName = libraryName
        self.name = name
        self.r1_ValueSetRef = r1_ValueSetRef
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def libraryName(self) -> str:
        return self.__libraryName

    @libraryName.setter
    def libraryName(self, libraryName: str):
        self.__libraryName = libraryName

    @property
    def r1_ValueSetRef(self):
        return self.__r1_ValueSetRef

    @r1_ValueSetRef.setter
    def r1_ValueSetRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_ValueSetRef__r1_ValueSetRef", None)
        self.__r1_ValueSetRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_InValueSet112"):
                opp_val = getattr(old_value, "r1_InValueSet112", None)
                if opp_val == self:
                    setattr(old_value, "r1_InValueSet112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_InValueSet112"):
                opp_val = getattr(value, "r1_InValueSet112", None)
                setattr(value, "r1_InValueSet112", self)

class r1_ForEach(Expression):

    def __init__(self, scope: str, r1_ForEach: "r1_Expression" = None, r1_ForEach69: "r1_Expression" = None):
        self.scope = scope
        self.r1_ForEach = r1_ForEach
        self.r1_ForEach69 = r1_ForEach69
        
    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def r1_ForEach69(self):
        return self.__r1_ForEach69

    @r1_ForEach69.setter
    def r1_ForEach69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_ForEach__r1_ForEach69", None)
        self.__r1_ForEach69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression70"):
                opp_val = getattr(old_value, "r1_Expression70", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression70"):
                opp_val = getattr(value, "r1_Expression70", None)
                setattr(value, "r1_Expression70", self)

    @property
    def r1_ForEach(self):
        return self.__r1_ForEach

    @r1_ForEach.setter
    def r1_ForEach(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_ForEach__r1_ForEach", None)
        self.__r1_ForEach = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression67"):
                opp_val = getattr(old_value, "r1_Expression67", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression67"):
                opp_val = getattr(value, "r1_Expression67", None)
                setattr(value, "r1_Expression67", self)

class r1_ParameterRef(Expression):

    def __init__(self, libraryName: str, name: str):
        self.libraryName = libraryName
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def libraryName(self) -> str:
        return self.__libraryName

    @libraryName.setter
    def libraryName(self, libraryName: str):
        self.__libraryName = libraryName

class r1_Current(Expression):

    def __init__(self, scope: str):
        self.scope = scope
        
    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

class r1_IndexOf(Expression):

    pass
class r1_Substring(Expression):

    pass
class r1_Concept(Expression):

    def __init__(self, display: str, r1_Concept: set["r1_Code"] = None):
        self.display = display
        self.r1_Concept = r1_Concept if r1_Concept is not None else set()
        
    @property
    def display(self) -> str:
        return self.__display

    @display.setter
    def display(self, display: str):
        self.__display = display

    @property
    def r1_Concept(self):
        return self.__r1_Concept

    @r1_Concept.setter
    def r1_Concept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Concept__r1_Concept", None)
        self.__r1_Concept = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "r1_Code28"):
                    opp_val = getattr(item, "r1_Code28", None)
                    
                    if opp_val == self:
                        setattr(item, "r1_Code28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "r1_Code28"):
                    opp_val = getattr(item, "r1_Code28", None)
                    
                    setattr(item, "r1_Code28", self)
                    

class r1_Case(Expression):

    pass
class r1_AliasRef(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class r1_TimeOfDay(Expression):

    pass
class r1_InCodeSystem(Expression):

    pass
class r1_Combine(Expression):

    pass
class r1_Literal(Expression):

    def __init__(self, value: str, valueType: str):
        self.value = value
        self.valueType = valueType
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def valueType(self) -> str:
        return self.__valueType

    @valueType.setter
    def valueType(self, valueType: str):
        self.__valueType = valueType

class r1_CodeSystemRef(Expression):

    def __init__(self, libraryName: str, name: str, r1_CodeSystemRef: "r1_Code" = None, r1_CodeSystemRef86: "r1_InCodeSystem" = None, r1_CodeSystemRef218: "r1_ValueSetDef" = None):
        self.libraryName = libraryName
        self.name = name
        self.r1_CodeSystemRef = r1_CodeSystemRef
        self.r1_CodeSystemRef86 = r1_CodeSystemRef86
        self.r1_CodeSystemRef218 = r1_CodeSystemRef218
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def libraryName(self) -> str:
        return self.__libraryName

    @libraryName.setter
    def libraryName(self, libraryName: str):
        self.__libraryName = libraryName

    @property
    def r1_CodeSystemRef86(self):
        return self.__r1_CodeSystemRef86

    @r1_CodeSystemRef86.setter
    def r1_CodeSystemRef86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_CodeSystemRef__r1_CodeSystemRef86", None)
        self.__r1_CodeSystemRef86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_InCodeSystem85"):
                opp_val = getattr(old_value, "r1_InCodeSystem85", None)
                if opp_val == self:
                    setattr(old_value, "r1_InCodeSystem85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_InCodeSystem85"):
                opp_val = getattr(value, "r1_InCodeSystem85", None)
                setattr(value, "r1_InCodeSystem85", self)

    @property
    def r1_CodeSystemRef218(self):
        return self.__r1_CodeSystemRef218

    @r1_CodeSystemRef218.setter
    def r1_CodeSystemRef218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_CodeSystemRef__r1_CodeSystemRef218", None)
        self.__r1_CodeSystemRef218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_ValueSetDef"):
                opp_val = getattr(old_value, "r1_ValueSetDef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_ValueSetDef"):
                opp_val = getattr(value, "r1_ValueSetDef", None)
                if opp_val is None:
                    setattr(value, "r1_ValueSetDef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def r1_CodeSystemRef(self):
        return self.__r1_CodeSystemRef

    @r1_CodeSystemRef.setter
    def r1_CodeSystemRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_CodeSystemRef__r1_CodeSystemRef", None)
        self.__r1_CodeSystemRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Code"):
                opp_val = getattr(old_value, "r1_Code", None)
                if opp_val == self:
                    setattr(old_value, "r1_Code", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Code"):
                opp_val = getattr(value, "r1_Code", None)
                setattr(value, "r1_Code", self)

class r1_Null(Expression):

    def __init__(self, valueType: str):
        self.valueType = valueType
        
    @property
    def valueType(self) -> str:
        return self.__valueType

    @valueType.setter
    def valueType(self, valueType: str):
        self.__valueType = valueType

class r1_OperandRef(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class r1_If(Expression):

    pass
class r1_Today(Expression):

    pass
class r1_AggregateExpression(Expression):

    def __init__(self, path: str, r1_AggregateExpression: "r1_Expression" = None):
        self.path = path
        self.r1_AggregateExpression = r1_AggregateExpression
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def r1_AggregateExpression(self):
        return self.__r1_AggregateExpression

    @r1_AggregateExpression.setter
    def r1_AggregateExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_AggregateExpression__r1_AggregateExpression", None)
        self.__r1_AggregateExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_Expression"):
                opp_val = getattr(old_value, "r1_Expression", None)
                if opp_val == self:
                    setattr(old_value, "r1_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_Expression"):
                opp_val = getattr(value, "r1_Expression", None)
                setattr(value, "r1_Expression", self)

class BinaryExpression:

    pass
class r1_Divide(BinaryExpression):

    pass
class r1_ProperIn(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_IncludedIn(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Greater(BinaryExpression):

    pass
class r1_ProperIncludes(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_DifferenceBetween(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_LessOrEqual(BinaryExpression):

    pass
class r1_TruncatedDivide(BinaryExpression):

    pass
class r1_NotEqual(BinaryExpression):

    pass
class r1_Log(BinaryExpression):

    pass
class r1_Or(BinaryExpression):

    pass
class r1_Power(BinaryExpression):

    pass
class r1_Times(BinaryExpression):

    pass
class r1_CalculateAgeAt(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Intersect(BinaryExpression):

    pass
class r1_OverlapsAfter(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_SameOrAfter(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_ProperIncludedIn(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Xor(BinaryExpression):

    pass
class r1_Multiply(BinaryExpression):

    pass
class r1_MeetsAfter(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Union(BinaryExpression):

    pass
class r1_OverlapsBefore(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Indexer(BinaryExpression):

    pass
class r1_And(BinaryExpression):

    pass
class r1_Except(BinaryExpression):

    pass
class r1_Overlaps(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Equal(BinaryExpression):

    pass
class r1_Subtract(BinaryExpression):

    pass
class r1_Before(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_In(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Starts(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_SameOrBefore(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Matches(BinaryExpression):

    pass
class r1_Modulo(BinaryExpression):

    pass
class r1_DurationBetween(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_GreaterOrEqual(BinaryExpression):

    pass
class r1_Meets(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Less(BinaryExpression):

    pass
class r1_SameAs(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Ends(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_After(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_ProperContains(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Contains(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Includes(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_MeetsBefore(BinaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Add(BinaryExpression):

    pass
class UnaryExpression:

    pass
class r1_CalculateAge(UnaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Not(UnaryExpression):

    pass
class r1_Predecessor(UnaryExpression):

    pass
class r1_Collapse(UnaryExpression):

    pass
class r1_Start(UnaryExpression):

    pass
class r1_Convert(UnaryExpression):

    def __init__(self, toType: str, r1_Convert: "r1_TypeSpecifier" = None):
        self.toType = toType
        self.r1_Convert = r1_Convert
        
    @property
    def toType(self) -> str:
        return self.__toType

    @toType.setter
    def toType(self, toType: str):
        self.__toType = toType

    @property
    def r1_Convert(self):
        return self.__r1_Convert

    @r1_Convert.setter
    def r1_Convert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Convert__r1_Convert", None)
        self.__r1_Convert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_TypeSpecifier30"):
                opp_val = getattr(old_value, "r1_TypeSpecifier30", None)
                if opp_val == self:
                    setattr(old_value, "r1_TypeSpecifier30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_TypeSpecifier30"):
                opp_val = getattr(value, "r1_TypeSpecifier30", None)
                setattr(value, "r1_TypeSpecifier30", self)

class r1_Length(UnaryExpression):

    pass
class r1_TimeFrom(UnaryExpression):

    pass
class r1_Upper(UnaryExpression):

    pass
class r1_Floor(UnaryExpression):

    pass
class r1_DateFrom(UnaryExpression):

    pass
class r1_End(UnaryExpression):

    pass
class r1_SingletonFrom(UnaryExpression):

    pass
class r1_Ceiling(UnaryExpression):

    pass
class r1_Distinct(UnaryExpression):

    pass
class r1_Truncate(UnaryExpression):

    pass
class r1_Negate(UnaryExpression):

    pass
class r1_IsTrue(UnaryExpression):

    pass
class r1_Width(UnaryExpression):

    pass
class r1_Successor(UnaryExpression):

    pass
class r1_Lower(UnaryExpression):

    pass
class r1_DateTimeComponentFrom(UnaryExpression):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class r1_Expand(UnaryExpression):

    pass
class r1_As(UnaryExpression):

    def __init__(self, asType: str, strict: str, r1_As: "r1_TypeSpecifier" = None):
        self.asType = asType
        self.strict = strict
        self.r1_As = r1_As
        
    @property
    def strict(self) -> str:
        return self.__strict

    @strict.setter
    def strict(self, strict: str):
        self.__strict = strict

    @property
    def asType(self) -> str:
        return self.__asType

    @asType.setter
    def asType(self, asType: str):
        self.__asType = asType

    @property
    def r1_As(self):
        return self.__r1_As

    @r1_As.setter
    def r1_As(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_As__r1_As", None)
        self.__r1_As = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_TypeSpecifier"):
                opp_val = getattr(old_value, "r1_TypeSpecifier", None)
                if opp_val == self:
                    setattr(old_value, "r1_TypeSpecifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_TypeSpecifier"):
                opp_val = getattr(value, "r1_TypeSpecifier", None)
                setattr(value, "r1_TypeSpecifier", self)

class r1_IsNull(UnaryExpression):

    pass
class r1_Ln(UnaryExpression):

    pass
class r1_Is(UnaryExpression):

    def __init__(self, isType: str, r1_Is: "r1_TypeSpecifier" = None):
        self.isType = isType
        self.r1_Is = r1_Is
        
    @property
    def isType(self) -> str:
        return self.__isType

    @isType.setter
    def isType(self, isType: str):
        self.__isType = isType

    @property
    def r1_Is(self):
        return self.__r1_Is

    @r1_Is.setter
    def r1_Is(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_r1_Is__r1_Is", None)
        self.__r1_Is = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "r1_TypeSpecifier114"):
                opp_val = getattr(old_value, "r1_TypeSpecifier114", None)
                if opp_val == self:
                    setattr(old_value, "r1_TypeSpecifier114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "r1_TypeSpecifier114"):
                opp_val = getattr(value, "r1_TypeSpecifier114", None)
                setattr(value, "r1_TypeSpecifier114", self)

class r1_TimezoneFrom(UnaryExpression):

    pass
class r1_Exists(UnaryExpression):

    pass
class r1_IsFalse(UnaryExpression):

    pass
class r1_Abs(UnaryExpression):

    pass