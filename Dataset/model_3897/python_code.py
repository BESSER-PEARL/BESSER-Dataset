from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TypeEnum(Enum):
    string = "string"
    int = "int"
    boolean = "boolean"
    float = "float"
    location = "location"
    locationset = "locationset"
    entity = "entity"
    entityset = "entityset"
class ComparisonBooleanFunctionEnum(Enum):
    GreaterOrEequalThan = "GreaterOrEequalThan"
    GreaterThan = "GreaterThan"
    NotEqual = "NotEqual"
    LessThan = "LessThan"
    LessOrEqualThan = "LessOrEqualThan"
    Equal = "Equal"
class UnaryLocationEnum(Enum):
    oneof = "oneof"
    oneofneighbour = "oneofneighbour"
    toplocation = "toplocation"
class DurationTypeEnum(Enum):
    weekly = "weekly"
    monthly = "monthly"
class EntitySetPrimiveEnum(Enum):
    all = "all"
    neighbours = "neighbours"
class MonthsEnum(Enum):
    January = "January"
    Februrary = "Februrary"
    March = "March"
    April = "April"
    May = "May"
    June = "June"
    July = "July"
    August = "August"
    September = "September"
    October = "October"
    November = "November"
    December = "December"
class UnaryStringFunctionEnum(Enum):
    Get = "Get"
class LocationPrimiveEnum(Enum):
    here = "here"
    top = "top"
    left = "left"
    right = "right"
    bottom = "bottom"
class UnaryEntityFunctionEnum(Enum):
    oneof = "oneof"
class UnaryLocationFunctionEnum(Enum):
    RandomLocation = "RandomLocation"
    RandomNeighbourhoodLocation = "RandomNeighbourhoodLocation"
    TopLocation = "TopLocation"
    TopLeftLocation = "TopLeftLocation"
    TopRightLocation = "TopRightLocation"
    BottomLocation = "BottomLocation"
    BottomLeftLocation = "BottomLeftLocation"
    BottomRightLocation = "BottomRightLocation"
    RightLocation = "RightLocation"
    LeftLocation = "LeftLocation"
    OneOf = "OneOf"
class WeekDaysEnum(Enum):
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"
    saturday = "saturday"
    sunday = "sunday"
class LogicBooleanFunctionEnum(Enum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
class EntityPrimitiveEnum(Enum):
    oneOf = "oneOf"
class OccupationBooleanFunctionEnum(Enum):
    Occupied = "Occupied"
class LocationSetPrimiveEnum(Enum):
    neighbourhood = "neighbourhood"
    space = "space"
class ArithmeticFunctionEnum(Enum):
    Sum = "Sum"
    Minus = "Minus"
    Times = "Times"
    Division = "Division"
class UnaryNumericFunctionEnum(Enum):
    random = "random"
class BooleanPrimitiveEnum(Enum):
    true = "true"
    false = "false"


############################################
# Definition of Classes
############################################

class LocationExpression:

    pass
class behaviour_NameLocationExpression(LocationExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class behaviour_NumericPrimitive:

    pass
class NamedFunction:

    pass
class behaviour_UnaryFunction(NamedFunction):

    pass
class behaviour_BinaryFunction(NamedFunction):

    pass
class Duration:

    pass
class behaviour_MonthDuration(Duration):

    def __init__(self, month: str):
        self.month = month
        
    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

class behaviour_CoordinateLocationExpression(LocationExpression):

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

class PrimitiveActivity:

    pass
class behaviour_Move(PrimitiveActivity):

    pass
class TimeExpression:

    pass
class behaviour_While(TimeExpression):

    pass
class behaviour_Remove(PrimitiveActivity):

    pass
class behaviour_Add(PrimitiveActivity):

    pass
class behaviour_Reproduce(PrimitiveActivity):

    pass
class behaviour_Die(PrimitiveActivity):

    pass
class behaviour_Node(ABC):

    pass
class behaviour_Edge(ABC):

    pass
class ControlNode:

    pass
class behaviour_Decision(ControlNode):

    pass
class behaviour_Merge(ControlNode):

    pass
class behaviour_Fork(ControlNode):

    pass
class behaviour_Join(ControlNode):

    pass
class behaviour_TimeExpression(ControlNode):

    pass
class Node:

    pass
class behaviour_ExecutableNode(Node):

    pass
class behaviour_ControlNode(Node):

    pass
class BinaryBooleanFunction:

    pass
class behaviour_LogicBooleanFunction(BinaryBooleanFunction):

    def __init__(self, functionName: str):
        self.functionName = functionName
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

class behaviour_OccupationBooleanFunction(BinaryBooleanFunction):

    def __init__(self, functionName: str):
        self.functionName = functionName
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

class behaviour_ComparisonBooleanFunction(BinaryBooleanFunction):

    def __init__(self, functionName: str):
        self.functionName = functionName
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

class BinaryFunction:

    pass
class behaviour_BinaryLocationFunction(BinaryFunction):

    pass
class behaviour_BinaryArithmeticFunction(BinaryFunction):

    def __init__(self, functionName: str):
        self.functionName = functionName
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

class behaviour_BinaryBooleanFunction(BinaryFunction):

    pass
class UnaryFunction:

    pass
class behaviour_UnaryEntityFunction(UnaryFunction):

    def __init__(self, functionName: str):
        self.functionName = functionName
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

class behaviour_UnaryNumericFunction(UnaryFunction):

    def __init__(self, functionName: str):
        self.functionName = functionName
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

class behaviour_UnaryLocationFunction(UnaryFunction):

    def __init__(self, functionName: str):
        self.functionName = functionName
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

class behaviour_UnaryStringFunction(UnaryFunction):

    def __init__(self, functionName: str):
        self.functionName = functionName
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

class Edge:

    pass
class behaviour_FalseEdge(Edge):

    pass
class behaviour_TrueEdge(Edge):

    pass
class behaviour_UnconditionedEdge(Edge):

    pass
class Function:

    pass
class behaviour_NamedFunction(Function):

    pass
class behaviour_AnonymousFunction(Function):

    pass
class behaviour_End(ControlNode):

    pass
class behaviour_Start(ControlNode):

    pass
class ExecutableNode:

    pass
class behaviour_PrimitiveActivity(ExecutableNode):

    pass
class behaviour_Equation:

    pass
class Behavior:

    pass
class behaviour_ActivityDiagramBehavior(ExecutableNode, Behavior):

    pass
class behaviour_EquationBehaviour(Behavior):

    pass
class behaviour_Duration(ABC):

    def __init__(self, durationTime: int, behaviour_Duration: "behaviour_Behavior" = None, behaviour_Duration18: "behaviour_Behavior" = None):
        self.durationTime = durationTime
        self.behaviour_Duration = behaviour_Duration
        self.behaviour_Duration18 = behaviour_Duration18
        
    @property
    def durationTime(self) -> int:
        return self.__durationTime

    @durationTime.setter
    def durationTime(self, durationTime: int):
        self.__durationTime = durationTime

    @property
    def behaviour_Duration18(self):
        return self.__behaviour_Duration18

    @behaviour_Duration18.setter
    def behaviour_Duration18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Duration__behaviour_Duration18", None)
        self.__behaviour_Duration18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Behavior17"):
                opp_val = getattr(old_value, "behaviour_Behavior17", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Behavior17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Behavior17"):
                opp_val = getattr(value, "behaviour_Behavior17", None)
                setattr(value, "behaviour_Behavior17", self)

    @property
    def behaviour_Duration(self):
        return self.__behaviour_Duration

    @behaviour_Duration.setter
    def behaviour_Duration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Duration__behaviour_Duration", None)
        self.__behaviour_Duration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Behavior15"):
                opp_val = getattr(old_value, "behaviour_Behavior15", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Behavior15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Behavior15"):
                opp_val = getattr(value, "behaviour_Behavior15", None)
                setattr(value, "behaviour_Behavior15", self)

class behaviour_Behavior(ABC):

    def __init__(self, behaviorName: str, frequency: str, behaviour_Behavior: "behaviour_EntityClass" = None, behaviour_Behavior15: "behaviour_Duration" = None, behaviour_Behavior17: "behaviour_Duration" = None, behaviour_Behavior20: set["behaviour_ParameterClass"] = None):
        self.behaviorName = behaviorName
        self.frequency = frequency
        self.behaviour_Behavior = behaviour_Behavior
        self.behaviour_Behavior15 = behaviour_Behavior15
        self.behaviour_Behavior17 = behaviour_Behavior17
        self.behaviour_Behavior20 = behaviour_Behavior20 if behaviour_Behavior20 is not None else set()
        
    @property
    def frequency(self) -> str:
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: str):
        self.__frequency = frequency

    @property
    def behaviorName(self) -> str:
        return self.__behaviorName

    @behaviorName.setter
    def behaviorName(self, behaviorName: str):
        self.__behaviorName = behaviorName

    @property
    def behaviour_Behavior17(self):
        return self.__behaviour_Behavior17

    @behaviour_Behavior17.setter
    def behaviour_Behavior17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Behavior__behaviour_Behavior17", None)
        self.__behaviour_Behavior17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Duration18"):
                opp_val = getattr(old_value, "behaviour_Duration18", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Duration18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Duration18"):
                opp_val = getattr(value, "behaviour_Duration18", None)
                setattr(value, "behaviour_Duration18", self)

    @property
    def behaviour_Behavior20(self):
        return self.__behaviour_Behavior20

    @behaviour_Behavior20.setter
    def behaviour_Behavior20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Behavior__behaviour_Behavior20", None)
        self.__behaviour_Behavior20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_ParameterClass"):
                    opp_val = getattr(item, "behaviour_ParameterClass", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_ParameterClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_ParameterClass"):
                    opp_val = getattr(item, "behaviour_ParameterClass", None)
                    
                    setattr(item, "behaviour_ParameterClass", self)
                    

    @property
    def behaviour_Behavior(self):
        return self.__behaviour_Behavior

    @behaviour_Behavior.setter
    def behaviour_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Behavior__behaviour_Behavior", None)
        self.__behaviour_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_EntityClass"):
                opp_val = getattr(old_value, "behaviour_EntityClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_EntityClass"):
                opp_val = getattr(value, "behaviour_EntityClass", None)
                if opp_val is None:
                    setattr(value, "behaviour_EntityClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_Behavior15(self):
        return self.__behaviour_Behavior15

    @behaviour_Behavior15.setter
    def behaviour_Behavior15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Behavior__behaviour_Behavior15", None)
        self.__behaviour_Behavior15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Duration"):
                opp_val = getattr(old_value, "behaviour_Duration", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Duration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Duration"):
                opp_val = getattr(value, "behaviour_Duration", None)
                setattr(value, "behaviour_Duration", self)

class behaviour_EntityClass:

    def __init__(self, entityName: str, behaviour_EntityClass: set["behaviour_Behavior"] = None, behaviour_EntityClass13: set["behaviour_AttributeClass"] = None):
        self.entityName = entityName
        self.behaviour_EntityClass = behaviour_EntityClass if behaviour_EntityClass is not None else set()
        self.behaviour_EntityClass13 = behaviour_EntityClass13 if behaviour_EntityClass13 is not None else set()
        
    @property
    def entityName(self) -> str:
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName

    @property
    def behaviour_EntityClass13(self):
        return self.__behaviour_EntityClass13

    @behaviour_EntityClass13.setter
    def behaviour_EntityClass13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_EntityClass__behaviour_EntityClass13", None)
        self.__behaviour_EntityClass13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_AttributeClass"):
                    opp_val = getattr(item, "behaviour_AttributeClass", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_AttributeClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_AttributeClass"):
                    opp_val = getattr(item, "behaviour_AttributeClass", None)
                    
                    setattr(item, "behaviour_AttributeClass", self)
                    

    @property
    def behaviour_EntityClass(self):
        return self.__behaviour_EntityClass

    @behaviour_EntityClass.setter
    def behaviour_EntityClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_EntityClass__behaviour_EntityClass", None)
        self.__behaviour_EntityClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Behavior"):
                    opp_val = getattr(item, "behaviour_Behavior", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Behavior", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Behavior"):
                    opp_val = getattr(item, "behaviour_Behavior", None)
                    
                    setattr(item, "behaviour_Behavior", self)
                    

class behaviour_Type:

    def __init__(self, type: str, behaviour_Type7: "behaviour_Function" = None, behaviour_Type10: "behaviour_Function" = None, behaviour_Type: "behaviour_VariableClass" = None):
        self.type = type
        self.behaviour_Type7 = behaviour_Type7
        self.behaviour_Type10 = behaviour_Type10
        self.behaviour_Type = behaviour_Type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def behaviour_Type10(self):
        return self.__behaviour_Type10

    @behaviour_Type10.setter
    def behaviour_Type10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Type__behaviour_Type10", None)
        self.__behaviour_Type10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Function9"):
                opp_val = getattr(old_value, "behaviour_Function9", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Function9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Function9"):
                opp_val = getattr(value, "behaviour_Function9", None)
                setattr(value, "behaviour_Function9", self)

    @property
    def behaviour_Type7(self):
        return self.__behaviour_Type7

    @behaviour_Type7.setter
    def behaviour_Type7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Type__behaviour_Type7", None)
        self.__behaviour_Type7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Function6"):
                opp_val = getattr(old_value, "behaviour_Function6", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Function6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Function6"):
                opp_val = getattr(value, "behaviour_Function6", None)
                setattr(value, "behaviour_Function6", self)

    @property
    def behaviour_Type(self):
        return self.__behaviour_Type

    @behaviour_Type.setter
    def behaviour_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Type__behaviour_Type", None)
        self.__behaviour_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_VariableClass"):
                opp_val = getattr(old_value, "behaviour_VariableClass", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_VariableClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_VariableClass"):
                opp_val = getattr(value, "behaviour_VariableClass", None)
                setattr(value, "behaviour_VariableClass", self)

class Expression:

    pass
class behaviour_LocationExpression(Expression):

    pass
class behaviour_VariableClass(Expression):

    def __init__(self, variableName: str, behaviour_VariableClass: "behaviour_Type" = None, behaviour_VariableClass2: "behaviour_FunctionCallExpression" = None):
        self.variableName = variableName
        self.behaviour_VariableClass = behaviour_VariableClass
        self.behaviour_VariableClass2 = behaviour_VariableClass2
        
    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

    @property
    def behaviour_VariableClass(self):
        return self.__behaviour_VariableClass

    @behaviour_VariableClass.setter
    def behaviour_VariableClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_VariableClass__behaviour_VariableClass", None)
        self.__behaviour_VariableClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Type"):
                opp_val = getattr(old_value, "behaviour_Type", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Type"):
                opp_val = getattr(value, "behaviour_Type", None)
                setattr(value, "behaviour_Type", self)

    @property
    def behaviour_VariableClass2(self):
        return self.__behaviour_VariableClass2

    @behaviour_VariableClass2.setter
    def behaviour_VariableClass2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_VariableClass__behaviour_VariableClass2", None)
        self.__behaviour_VariableClass2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_FunctionCallExpression"):
                opp_val = getattr(old_value, "behaviour_FunctionCallExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_FunctionCallExpression"):
                opp_val = getattr(value, "behaviour_FunctionCallExpression", None)
                if opp_val is None:
                    setattr(value, "behaviour_FunctionCallExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class behaviour_Expression(ABC):

    pass
class PrimitiveExpression:

    pass
class behaviour_LocationSetPrimitive(PrimitiveExpression):

    def __init__(self, primitive: str):
        self.primitive = primitive
        
    @property
    def primitive(self) -> str:
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: str):
        self.__primitive = primitive

class behaviour_BooleanPrimitive(PrimitiveExpression):

    def __init__(self, primitive: str):
        self.primitive = primitive
        
    @property
    def primitive(self) -> str:
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: str):
        self.__primitive = primitive

class behaviour_EntitySetPrimitive(PrimitiveExpression):

    def __init__(self, primitive: str):
        self.primitive = primitive
        
    @property
    def primitive(self) -> str:
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: str):
        self.__primitive = primitive

class behaviour_LocationPrimitive(PrimitiveExpression):

    def __init__(self, primitive: str):
        self.primitive = primitive
        
    @property
    def primitive(self) -> str:
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: str):
        self.__primitive = primitive

class behaviour_EntityPrimive(PrimitiveExpression):

    def __init__(self, primitive: str):
        self.primitive = primitive
        
    @property
    def primitive(self) -> str:
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: str):
        self.__primitive = primitive

class behaviour_PrimitiveExpression(Expression):

    pass
class ConstantExpression:

    pass
class behaviour_StringConstantExpression(ConstantExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class behaviour_FloatConstantExpression(ConstantExpression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class behaviour_IntConstantExpression(ConstantExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class behaviour_ConstantExpression(Expression):

    pass
class behaviour_Function:

    pass
class behaviour_FunctionCallExpression(Expression):

    pass
class VariableClass:

    pass
class behaviour_ParameterClass(VariableClass):

    pass
class behaviour_AttributeClass(VariableClass):

    pass