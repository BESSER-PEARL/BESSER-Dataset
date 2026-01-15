from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class VariableReference:

    pass
class arduinoDSL_VarRef(VariableReference):

    pass
class CompareOperator:

    pass
class arduinoDSL_SmallerThanEquals(CompareOperator):

    pass
class arduinoDSL_Greater(CompareOperator):

    pass
class arduinoDSL_Smaller(CompareOperator):

    pass
class arduinoDSL_NotEquals(CompareOperator):

    pass
class arduinoDSL_GreaterThanEquals(CompareOperator):

    pass
class arduinoDSL_Equals(CompareOperator):

    pass
class BooleanOperator:

    pass
class arduinoDSL_Or(BooleanOperator):

    pass
class arduinoDSL_And(BooleanOperator):

    pass
class arduinoDSL_Range:

    def __init__(self, low: float, high: float, arduinoDSL_Range: "arduinoDSL_Map" = None, arduinoDSL_Range42: "arduinoDSL_Map" = None):
        self.low = low
        self.high = high
        self.arduinoDSL_Range = arduinoDSL_Range
        self.arduinoDSL_Range42 = arduinoDSL_Range42
        
    @property
    def high(self) -> float:
        return self.__high

    @high.setter
    def high(self, high: float):
        self.__high = high

    @property
    def low(self) -> float:
        return self.__low

    @low.setter
    def low(self, low: float):
        self.__low = low

    @property
    def arduinoDSL_Range42(self):
        return self.__arduinoDSL_Range42

    @arduinoDSL_Range42.setter
    def arduinoDSL_Range42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Range__arduinoDSL_Range42", None)
        self.__arduinoDSL_Range42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_Map41"):
                opp_val = getattr(old_value, "arduinoDSL_Map41", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_Map41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_Map41"):
                opp_val = getattr(value, "arduinoDSL_Map41", None)
                setattr(value, "arduinoDSL_Map41", self)

    @property
    def arduinoDSL_Range(self):
        return self.__arduinoDSL_Range

    @arduinoDSL_Range.setter
    def arduinoDSL_Range(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Range__arduinoDSL_Range", None)
        self.__arduinoDSL_Range = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_Map39"):
                opp_val = getattr(old_value, "arduinoDSL_Map39", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_Map39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_Map39"):
                opp_val = getattr(value, "arduinoDSL_Map39", None)
                setattr(value, "arduinoDSL_Map39", self)

class arduinoDSL_Smoothing:

    def __init__(self, value: float, arduinoDSL_Smoothing: "arduinoDSL_ComponentBody" = None):
        self.value = value
        self.arduinoDSL_Smoothing = arduinoDSL_Smoothing
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def arduinoDSL_Smoothing(self):
        return self.__arduinoDSL_Smoothing

    @arduinoDSL_Smoothing.setter
    def arduinoDSL_Smoothing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Smoothing__arduinoDSL_Smoothing", None)
        self.__arduinoDSL_Smoothing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_ComponentBody37"):
                opp_val = getattr(old_value, "arduinoDSL_ComponentBody37", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_ComponentBody37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_ComponentBody37"):
                opp_val = getattr(value, "arduinoDSL_ComponentBody37", None)
                setattr(value, "arduinoDSL_ComponentBody37", self)

class arduinoDSL_Map:

    pass
class arduinoDSL_Rate:

    def __init__(self, value: int, arduinoDSL_Rate: "arduinoDSL_ComponentBody" = None):
        self.value = value
        self.arduinoDSL_Rate = arduinoDSL_Rate
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def arduinoDSL_Rate(self):
        return self.__arduinoDSL_Rate

    @arduinoDSL_Rate.setter
    def arduinoDSL_Rate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Rate__arduinoDSL_Rate", None)
        self.__arduinoDSL_Rate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_ComponentBody33"):
                opp_val = getattr(old_value, "arduinoDSL_ComponentBody33", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_ComponentBody33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_ComponentBody33"):
                opp_val = getattr(value, "arduinoDSL_ComponentBody33", None)
                setattr(value, "arduinoDSL_ComponentBody33", self)

class arduinoDSL_ComponentBody:

    def __init__(self, io: str, type: str, pin: int, arduinoDSL_ComponentBody: "arduinoDSL_Component" = None, arduinoDSL_ComponentBody33: "arduinoDSL_Rate" = None, arduinoDSL_ComponentBody35: "arduinoDSL_Map" = None, arduinoDSL_ComponentBody37: "arduinoDSL_Smoothing" = None):
        self.io = io
        self.type = type
        self.pin = pin
        self.arduinoDSL_ComponentBody = arduinoDSL_ComponentBody
        self.arduinoDSL_ComponentBody33 = arduinoDSL_ComponentBody33
        self.arduinoDSL_ComponentBody35 = arduinoDSL_ComponentBody35
        self.arduinoDSL_ComponentBody37 = arduinoDSL_ComponentBody37
        
    @property
    def pin(self) -> int:
        return self.__pin

    @pin.setter
    def pin(self, pin: int):
        self.__pin = pin

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def io(self) -> str:
        return self.__io

    @io.setter
    def io(self, io: str):
        self.__io = io

    @property
    def arduinoDSL_ComponentBody33(self):
        return self.__arduinoDSL_ComponentBody33

    @arduinoDSL_ComponentBody33.setter
    def arduinoDSL_ComponentBody33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_ComponentBody__arduinoDSL_ComponentBody33", None)
        self.__arduinoDSL_ComponentBody33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_Rate"):
                opp_val = getattr(old_value, "arduinoDSL_Rate", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_Rate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_Rate"):
                opp_val = getattr(value, "arduinoDSL_Rate", None)
                setattr(value, "arduinoDSL_Rate", self)

    @property
    def arduinoDSL_ComponentBody37(self):
        return self.__arduinoDSL_ComponentBody37

    @arduinoDSL_ComponentBody37.setter
    def arduinoDSL_ComponentBody37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_ComponentBody__arduinoDSL_ComponentBody37", None)
        self.__arduinoDSL_ComponentBody37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_Smoothing"):
                opp_val = getattr(old_value, "arduinoDSL_Smoothing", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_Smoothing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_Smoothing"):
                opp_val = getattr(value, "arduinoDSL_Smoothing", None)
                setattr(value, "arduinoDSL_Smoothing", self)

    @property
    def arduinoDSL_ComponentBody35(self):
        return self.__arduinoDSL_ComponentBody35

    @arduinoDSL_ComponentBody35.setter
    def arduinoDSL_ComponentBody35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_ComponentBody__arduinoDSL_ComponentBody35", None)
        self.__arduinoDSL_ComponentBody35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_Map"):
                opp_val = getattr(old_value, "arduinoDSL_Map", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_Map", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_Map"):
                opp_val = getattr(value, "arduinoDSL_Map", None)
                setattr(value, "arduinoDSL_Map", self)

    @property
    def arduinoDSL_ComponentBody(self):
        return self.__arduinoDSL_ComponentBody

    @arduinoDSL_ComponentBody.setter
    def arduinoDSL_ComponentBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_ComponentBody__arduinoDSL_ComponentBody", None)
        self.__arduinoDSL_ComponentBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_Component31"):
                opp_val = getattr(old_value, "arduinoDSL_Component31", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_Component31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_Component31"):
                opp_val = getattr(value, "arduinoDSL_Component31", None)
                setattr(value, "arduinoDSL_Component31", self)

class arduinoDSL_Board:

    def __init__(self, b: str, arduinoDSL_Board: "arduinoDSL_NodeDefinition" = None):
        self.b = b
        self.arduinoDSL_Board = arduinoDSL_Board
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def arduinoDSL_Board(self):
        return self.__arduinoDSL_Board

    @arduinoDSL_Board.setter
    def arduinoDSL_Board(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Board__arduinoDSL_Board", None)
        self.__arduinoDSL_Board = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_NodeDefinition"):
                opp_val = getattr(old_value, "arduinoDSL_NodeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_NodeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_NodeDefinition"):
                opp_val = getattr(value, "arduinoDSL_NodeDefinition", None)
                setattr(value, "arduinoDSL_NodeDefinition", self)

class arduinoDSL_NodeDefinition:

    pass
class arduinoDSL_SimpleStatement:

    pass
class arduinoDSL_State:

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class arduinoDSL_BooleanLiteral:

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class arduinoDSL_Component:

    def __init__(self, name: str, arduinoDSL_Component: "arduinoDSL_Attribute" = None, arduinoDSL_Component29: "arduinoDSL_Node" = None, arduinoDSL_Component31: "arduinoDSL_ComponentBody" = None):
        self.name = name
        self.arduinoDSL_Component = arduinoDSL_Component
        self.arduinoDSL_Component29 = arduinoDSL_Component29
        self.arduinoDSL_Component31 = arduinoDSL_Component31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduinoDSL_Component29(self):
        return self.__arduinoDSL_Component29

    @arduinoDSL_Component29.setter
    def arduinoDSL_Component29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Component__arduinoDSL_Component29", None)
        self.__arduinoDSL_Component29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_Node28"):
                opp_val = getattr(old_value, "arduinoDSL_Node28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_Node28"):
                opp_val = getattr(value, "arduinoDSL_Node28", None)
                if opp_val is None:
                    setattr(value, "arduinoDSL_Node28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduinoDSL_Component31(self):
        return self.__arduinoDSL_Component31

    @arduinoDSL_Component31.setter
    def arduinoDSL_Component31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Component__arduinoDSL_Component31", None)
        self.__arduinoDSL_Component31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_ComponentBody"):
                opp_val = getattr(old_value, "arduinoDSL_ComponentBody", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_ComponentBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_ComponentBody"):
                opp_val = getattr(value, "arduinoDSL_ComponentBody", None)
                setattr(value, "arduinoDSL_ComponentBody", self)

    @property
    def arduinoDSL_Component(self):
        return self.__arduinoDSL_Component

    @arduinoDSL_Component.setter
    def arduinoDSL_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Component__arduinoDSL_Component", None)
        self.__arduinoDSL_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_Attribute9"):
                opp_val = getattr(old_value, "arduinoDSL_Attribute9", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_Attribute9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_Attribute9"):
                opp_val = getattr(value, "arduinoDSL_Attribute9", None)
                setattr(value, "arduinoDSL_Attribute9", self)

class arduinoDSL_Node:

    def __init__(self, name: str, arduinoDSL_Node: "arduinoDSL_Attribute" = None, arduinoDSL_Node26: "arduinoDSL_NodeDefinition" = None, arduinoDSL_Node28: set["arduinoDSL_Component"] = None):
        self.name = name
        self.arduinoDSL_Node = arduinoDSL_Node
        self.arduinoDSL_Node26 = arduinoDSL_Node26
        self.arduinoDSL_Node28 = arduinoDSL_Node28 if arduinoDSL_Node28 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduinoDSL_Node(self):
        return self.__arduinoDSL_Node

    @arduinoDSL_Node.setter
    def arduinoDSL_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Node__arduinoDSL_Node", None)
        self.__arduinoDSL_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_Attribute"):
                opp_val = getattr(old_value, "arduinoDSL_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_Attribute"):
                opp_val = getattr(value, "arduinoDSL_Attribute", None)
                setattr(value, "arduinoDSL_Attribute", self)

    @property
    def arduinoDSL_Node28(self):
        return self.__arduinoDSL_Node28

    @arduinoDSL_Node28.setter
    def arduinoDSL_Node28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Node__arduinoDSL_Node28", None)
        self.__arduinoDSL_Node28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoDSL_Component29"):
                    opp_val = getattr(item, "arduinoDSL_Component29", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoDSL_Component29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoDSL_Component29"):
                    opp_val = getattr(item, "arduinoDSL_Component29", None)
                    
                    setattr(item, "arduinoDSL_Component29", self)
                    

    @property
    def arduinoDSL_Node26(self):
        return self.__arduinoDSL_Node26

    @arduinoDSL_Node26.setter
    def arduinoDSL_Node26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Node__arduinoDSL_Node26", None)
        self.__arduinoDSL_Node26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_NodeDefinition25"):
                opp_val = getattr(old_value, "arduinoDSL_NodeDefinition25", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_NodeDefinition25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_NodeDefinition25"):
                opp_val = getattr(value, "arduinoDSL_NodeDefinition25", None)
                setattr(value, "arduinoDSL_NodeDefinition25", self)

class Value:

    pass
class arduinoDSL_Delta(Value):

    pass
class arduinoDSL_NumberLiteral(Value):

    def __init__(self, floatVal: str, intVal: int):
        self.floatVal = floatVal
        self.intVal = intVal
        
    @property
    def floatVal(self) -> str:
        return self.__floatVal

    @floatVal.setter
    def floatVal(self, floatVal: str):
        self.__floatVal = floatVal

    @property
    def intVal(self) -> int:
        return self.__intVal

    @intVal.setter
    def intVal(self, intVal: int):
        self.__intVal = intVal

class arduinoDSL_Attribute(Value):

    pass
class NumberExpression:

    pass
class arduinoDSL_Minus(NumberExpression):

    pass
class arduinoDSL_Value(NumberExpression):

    pass
class arduinoDSL_Div(NumberExpression):

    pass
class arduinoDSL_Mod(NumberExpression):

    pass
class arduinoDSL_Plus(NumberExpression):

    pass
class arduinoDSL_Mult(NumberExpression):

    pass
class arduinoDSL_NumberExpressionBlock(NumberExpression):

    pass
class arduinoDSL_CompareOperator:

    pass
class arduinoDSL_BooleanOperator:

    pass
class BooleanExpression:

    pass
class arduinoDSL_AndOr(BooleanExpression):

    pass
class arduinoDSL_Comparison(BooleanExpression):

    pass
class arduinoDSL_BooleanExpressionBlock(BooleanExpression):

    pass
class arduinoDSL_NumberExpression:

    pass
class arduinoDSL_Cast:

    def __init__(self, castType: str, arduinoDSL_Cast: "arduinoDSL_VariableDeclaration" = None, arduinoDSL_Cast110: "arduinoDSL_VarRef" = None):
        self.castType = castType
        self.arduinoDSL_Cast = arduinoDSL_Cast
        self.arduinoDSL_Cast110 = arduinoDSL_Cast110
        
    @property
    def castType(self) -> str:
        return self.__castType

    @castType.setter
    def castType(self, castType: str):
        self.__castType = castType

    @property
    def arduinoDSL_Cast(self):
        return self.__arduinoDSL_Cast

    @arduinoDSL_Cast.setter
    def arduinoDSL_Cast(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Cast__arduinoDSL_Cast", None)
        self.__arduinoDSL_Cast = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_VariableDeclaration"):
                opp_val = getattr(old_value, "arduinoDSL_VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_VariableDeclaration"):
                opp_val = getattr(value, "arduinoDSL_VariableDeclaration", None)
                setattr(value, "arduinoDSL_VariableDeclaration", self)

    @property
    def arduinoDSL_Cast110(self):
        return self.__arduinoDSL_Cast110

    @arduinoDSL_Cast110.setter
    def arduinoDSL_Cast110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Cast__arduinoDSL_Cast110", None)
        self.__arduinoDSL_Cast110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_VarRef109"):
                opp_val = getattr(old_value, "arduinoDSL_VarRef109", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_VarRef109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_VarRef109"):
                opp_val = getattr(value, "arduinoDSL_VarRef109", None)
                setattr(value, "arduinoDSL_VarRef109", self)

class SimpleStatement:

    pass
class arduinoDSL_ElseIfStatement(SimpleStatement):

    pass
class arduinoDSL_ElseStatement(SimpleStatement):

    pass
class arduinoDSL_VariableReference(SimpleStatement, Value):

    pass
class arduinoDSL_IfStatement(SimpleStatement):

    pass
class arduinoDSL_VariableDeclaration(SimpleStatement):

    def __init__(self, type: str, name: str, arduinoDSL_VariableDeclaration: "arduinoDSL_Cast" = None, arduinoDSL_VariableDeclaration21: "arduinoDSL_EObject" = None, arduinoDSL_VariableDeclaration107: "arduinoDSL_VarRef" = None):
        self.type = type
        self.name = name
        self.arduinoDSL_VariableDeclaration = arduinoDSL_VariableDeclaration
        self.arduinoDSL_VariableDeclaration21 = arduinoDSL_VariableDeclaration21
        self.arduinoDSL_VariableDeclaration107 = arduinoDSL_VariableDeclaration107
        
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
    def arduinoDSL_VariableDeclaration21(self):
        return self.__arduinoDSL_VariableDeclaration21

    @arduinoDSL_VariableDeclaration21.setter
    def arduinoDSL_VariableDeclaration21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_VariableDeclaration__arduinoDSL_VariableDeclaration21", None)
        self.__arduinoDSL_VariableDeclaration21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_EObject22"):
                opp_val = getattr(old_value, "arduinoDSL_EObject22", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_EObject22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_EObject22"):
                opp_val = getattr(value, "arduinoDSL_EObject22", None)
                setattr(value, "arduinoDSL_EObject22", self)

    @property
    def arduinoDSL_VariableDeclaration107(self):
        return self.__arduinoDSL_VariableDeclaration107

    @arduinoDSL_VariableDeclaration107.setter
    def arduinoDSL_VariableDeclaration107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_VariableDeclaration__arduinoDSL_VariableDeclaration107", None)
        self.__arduinoDSL_VariableDeclaration107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_VarRef"):
                opp_val = getattr(old_value, "arduinoDSL_VarRef", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_VarRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_VarRef"):
                opp_val = getattr(value, "arduinoDSL_VarRef", None)
                setattr(value, "arduinoDSL_VarRef", self)

    @property
    def arduinoDSL_VariableDeclaration(self):
        return self.__arduinoDSL_VariableDeclaration

    @arduinoDSL_VariableDeclaration.setter
    def arduinoDSL_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_VariableDeclaration__arduinoDSL_VariableDeclaration", None)
        self.__arduinoDSL_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_Cast"):
                opp_val = getattr(old_value, "arduinoDSL_Cast", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_Cast", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_Cast"):
                opp_val = getattr(value, "arduinoDSL_Cast", None)
                setattr(value, "arduinoDSL_Cast", self)

class arduinoDSL_Assignment(SimpleStatement):

    pass
class arduinoDSL_RuleBody:

    pass
class arduinoDSL_BooleanExpression:

    pass
class arduinoDSL_Rule:

    def __init__(self, type: str, arduinoDSL_Rule: "arduinoDSL_BooleanExpression" = None, arduinoDSL_Rule3: "arduinoDSL_RuleBody" = None):
        self.type = type
        self.arduinoDSL_Rule = arduinoDSL_Rule
        self.arduinoDSL_Rule3 = arduinoDSL_Rule3
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def arduinoDSL_Rule3(self):
        return self.__arduinoDSL_Rule3

    @arduinoDSL_Rule3.setter
    def arduinoDSL_Rule3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Rule__arduinoDSL_Rule3", None)
        self.__arduinoDSL_Rule3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_RuleBody"):
                opp_val = getattr(old_value, "arduinoDSL_RuleBody", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_RuleBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_RuleBody"):
                opp_val = getattr(value, "arduinoDSL_RuleBody", None)
                setattr(value, "arduinoDSL_RuleBody", self)

    @property
    def arduinoDSL_Rule(self):
        return self.__arduinoDSL_Rule

    @arduinoDSL_Rule.setter
    def arduinoDSL_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoDSL_Rule__arduinoDSL_Rule", None)
        self.__arduinoDSL_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoDSL_BooleanExpression"):
                opp_val = getattr(old_value, "arduinoDSL_BooleanExpression", None)
                if opp_val == self:
                    setattr(old_value, "arduinoDSL_BooleanExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoDSL_BooleanExpression"):
                opp_val = getattr(value, "arduinoDSL_BooleanExpression", None)
                setattr(value, "arduinoDSL_BooleanExpression", self)

class arduinoDSL_EObject:

    pass
class arduinoDSL_Program:

    pass