from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RelationalOperatorKind(Enum):
    LESS = "LESS"
    GREATER_EQUALS = "GREATER_EQUALS"
    LESS_EQUALS = "LESS_EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    EQUALS = "EQUALS"
    none = "none"
    GREATER = "GREATER"
class RelationalConectorKind(Enum):
    none = "none"
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
class BinaryOperatorKind(Enum):
    PLUS = "PLUS"
    MINUS = "MINUS"
    TIMES = "TIMES"
    DIVIDED_BY = "DIVIDED_BY"
    MODULE = "MODULE"
class FunctionModifierKind(Enum):
    none = "none"
    interrupt = "interrupt"
    cdecl = "cdecl"
    pascal = "pascal"
class SimpleLogicOperatorKind(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"
    NOT = "NOT"
class UnaryOperatorKind(Enum):
    MINUS = "MINUS"
    PLUS_PLUS = "PLUS_PLUS"
    MINUS_MINUS = "MINUS_MINUS"
    PLUS_EQUALS = "PLUS_EQUALS"
    MINUS_EQUALS = "MINUS_EQUALS"
    TIMES_EQUALS = "TIMES_EQUALS"
    DIVIDED_BY_EQUALS = "DIVIDED_BY_EQUALS"
class DisplacementLogicOperatorKind(Enum):
    RIGHT_DISPLACEMENT = "RIGHT_DISPLACEMENT"
    LEFT_DISPLACEMENT = "LEFT_DISPLACEMENT"
class ModifierKind(Enum):
    none = "none"
    static = "static"
    volatile = "volatile"
    register = "register"


############################################
# Definition of Classes
############################################

class Commands_LabelCommand:

    pass
class Sequencer:

    pass
class C_Sequencers_Break(Sequencer):

    pass
class C_Sequencers_Goto(Sequencer):

    pass
class Declarations_ArrayDeclaration:

    pass
class Literal:

    pass
class C_Expressions_ShortLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class C_Expressions_DoubleLiteral(Literal):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class C_Expressions_FloatLiteral(Literal):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class C_Expressions_IntLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class C_Expressions_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class C_Expressions_CharLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Declarations_PrototypeFunctionDeclaration:

    pass
class VariableAccess:

    pass
class C_Expressions_PointerVariableAccess(VariableAccess):

    pass
class Declarations_ConstantDeclaration:

    pass
class Access:

    pass
class C_Expressions_VariableAccess(Access):

    pass
class C_Expressions_PrototypeAccess(Access):

    pass
class C_Expressions_ArrayAccess(Access):

    pass
class C_Expressions_ConstantAccess(Access):

    pass
class LogicExpression:

    pass
class C_Expressions_SimpleLogicExpression(LogicExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class C_Expressions_DisplacementLogicExpression(LogicExpression):

    def __init__(self, operator: str, C_Expressions_DisplacementLogicExpression: "Expressions_Expression" = None):
        self.operator = operator
        self.C_Expressions_DisplacementLogicExpression = C_Expressions_DisplacementLogicExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def C_Expressions_DisplacementLogicExpression(self):
        return self.__C_Expressions_DisplacementLogicExpression

    @C_Expressions_DisplacementLogicExpression.setter
    def C_Expressions_DisplacementLogicExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C_Expressions_DisplacementLogicExpression__C_Expressions_DisplacementLogicExpression", None)
        self.__C_Expressions_DisplacementLogicExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expressions_Expression104"):
                opp_val = getattr(old_value, "Expressions_Expression104", None)
                if opp_val == self:
                    setattr(old_value, "Expressions_Expression104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expressions_Expression104"):
                opp_val = getattr(value, "Expressions_Expression104", None)
                setattr(value, "Expressions_Expression104", self)

class ConditionalExpression:

    pass
class C_Expressions_ComposedConditionalExpression(ConditionalExpression):

    def __init__(self, operator: str, C_Expressions_ComposedConditionalExpression: set["Expressions_Expression"] = None):
        self.operator = operator
        self.C_Expressions_ComposedConditionalExpression = C_Expressions_ComposedConditionalExpression if C_Expressions_ComposedConditionalExpression is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def C_Expressions_ComposedConditionalExpression(self):
        return self.__C_Expressions_ComposedConditionalExpression

    @C_Expressions_ComposedConditionalExpression.setter
    def C_Expressions_ComposedConditionalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C_Expressions_ComposedConditionalExpression__C_Expressions_ComposedConditionalExpression", None)
        self.__C_Expressions_ComposedConditionalExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expressions_Expression100"):
                    opp_val = getattr(item, "Expressions_Expression100", None)
                    
                    if opp_val == self:
                        setattr(item, "Expressions_Expression100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expressions_Expression100"):
                    opp_val = getattr(item, "Expressions_Expression100", None)
                    
                    setattr(item, "Expressions_Expression100", self)
                    

class ArithmeticExpression:

    pass
class C_Expressions_BinaryArithmeticExpression(ArithmeticExpression):

    def __init__(self, operator: str, C_Expressions_BinaryArithmeticExpression: "Expressions_Expression" = None):
        self.operator = operator
        self.C_Expressions_BinaryArithmeticExpression = C_Expressions_BinaryArithmeticExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def C_Expressions_BinaryArithmeticExpression(self):
        return self.__C_Expressions_BinaryArithmeticExpression

    @C_Expressions_BinaryArithmeticExpression.setter
    def C_Expressions_BinaryArithmeticExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C_Expressions_BinaryArithmeticExpression__C_Expressions_BinaryArithmeticExpression", None)
        self.__C_Expressions_BinaryArithmeticExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expressions_Expression98"):
                opp_val = getattr(old_value, "Expressions_Expression98", None)
                if opp_val == self:
                    setattr(old_value, "Expressions_Expression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expressions_Expression98"):
                opp_val = getattr(value, "Expressions_Expression98", None)
                setattr(value, "Expressions_Expression98", self)

class C_Expressions_UnaryArithmeticExpression(ArithmeticExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class Expression:

    pass
class C_Expressions_ConstantExpression(Expression):

    pass
class C_Expressions_ArithmeticExpression(Expression):

    pass
class C_Expressions_CastExpression(Expression):

    pass
class C_Expressions_ConditionalExpression(Expression):

    def __init__(self, conector: str):
        self.conector = conector
        
    @property
    def conector(self) -> str:
        return self.__conector

    @conector.setter
    def conector(self, conector: str):
        self.__conector = conector

class C_Expressions_Literal(Expression):

    pass
class C_Expressions_LogicExpression(Expression):

    pass
class C_Expressions_Construction(Expression):

    pass
class C_Expressions_Expression(ABC):

    pass
class C_Commands_CaseOption:

    pass
class IterativeCommand:

    pass
class C_Commands_WhileCommand(IterativeCommand):

    pass
class C_Commands_ForCommand(IterativeCommand):

    pass
class C_Commands_DefaultOption:

    pass
class Commands_DefaultOption:

    pass
class Commands_CaseOption:

    pass
class Expressions_VariableAccess:

    pass
class Expressions_Access:

    pass
class Command:

    pass
class C_Commands_IterativeCommand(Command):

    pass
class C_Commands_Assignment(Command):

    pass
class Expressions_ConditionalExpression:

    pass
class DecisionCommand:

    pass
class C_Commands_SwitchCommand(DecisionCommand):

    pass
class C_Commands_IfCommand(DecisionCommand):

    pass
class C_Commands_ExpressionCommand(Command):

    pass
class FlowControlCommand:

    pass
class C_Commands_ReturnCommand(FlowControlCommand):

    pass
class C_Commands_DecisionCommand(FlowControlCommand):

    pass
class C_Commands_FlowControlCommand(Command):

    pass
class Commands_Command:

    pass
class BlockedElement:

    pass
class C_Sequencers_Sequencer(BlockedElement):

    pass
class C_Commands_Command(BlockedElement):

    pass
class C_CompilationDirectiveDeclarations_Endif:

    pass
class IfDirective:

    pass
class C_CompilationDirectiveDeclarations_Elif(IfDirective):

    pass
class Expressions_ConstantExpression:

    pass
class C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration(ABC):

    pass
class ComplexDirectiveDeclaration:

    pass
class C_CompilationDirectiveDeclarations_IfDirective(ComplexDirectiveDeclaration):

    pass
class C_CompilationDirectiveDeclarations_ElseDirective(ComplexDirectiveDeclaration):

    pass
class C_CompilationDirectiveDeclarations_Ifndef(ComplexDirectiveDeclaration):

    pass
class CompilationDirectiveDeclarations_Endif:

    pass
class CompilationDirectiveDeclarations_ComplexDirectiveDeclaration:

    pass
class SimpleDirectiveDeclaration:

    pass
class C_CompilationDirectiveDeclarations_Include(SimpleDirectiveDeclaration):

    pass
class C_CompilationDirectiveDeclarations_Define(SimpleDirectiveDeclaration):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class CompilationDirectiveDeclaration:

    pass
class C_CompilationDirectiveDeclarations_ComplexDirectiveDeclaration(CompilationDirectiveDeclaration):

    pass
class Declarations_SimpleVariableDeclaration:

    pass
class Expressions_Construction:

    pass
class Declarations_CompositeVariableDeclaration:

    pass
class Expressions_Literal:

    pass
class CompositeVariableDeclaration:

    pass
class C_Declarations_TypeDefDeclaration(CompositeVariableDeclaration):

    pass
class C_Declarations_StructDeclaration(CompositeVariableDeclaration):

    pass
class C_Declarations_EnumDeclaration(CompositeVariableDeclaration):

    pass
class VariableDeclaration:

    pass
class C_Declarations_CompositeVariableDeclaration(VariableDeclaration):

    pass
class Declarations_FragmentVariableDeclaration:

    pass
class Declarations_VariableDeclaration:

    pass
class Expressions_Expression:

    pass
class Declaration:

    pass
class C_Declarations_PrototypeFunctionDeclaration(Declaration):

    def __init__(self, isAPointer: str, functionModifier: str, C_Declarations_PrototypeFunctionDeclaration: set["Declarations_VariableDeclaration"] = None, C_Declarations_PrototypeFunctionDeclaration30: "Types_Type" = None):
        self.isAPointer = isAPointer
        self.functionModifier = functionModifier
        self.C_Declarations_PrototypeFunctionDeclaration = C_Declarations_PrototypeFunctionDeclaration if C_Declarations_PrototypeFunctionDeclaration is not None else set()
        self.C_Declarations_PrototypeFunctionDeclaration30 = C_Declarations_PrototypeFunctionDeclaration30
        
    @property
    def functionModifier(self) -> str:
        return self.__functionModifier

    @functionModifier.setter
    def functionModifier(self, functionModifier: str):
        self.__functionModifier = functionModifier

    @property
    def isAPointer(self) -> str:
        return self.__isAPointer

    @isAPointer.setter
    def isAPointer(self, isAPointer: str):
        self.__isAPointer = isAPointer

    @property
    def C_Declarations_PrototypeFunctionDeclaration30(self):
        return self.__C_Declarations_PrototypeFunctionDeclaration30

    @C_Declarations_PrototypeFunctionDeclaration30.setter
    def C_Declarations_PrototypeFunctionDeclaration30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C_Declarations_PrototypeFunctionDeclaration__C_Declarations_PrototypeFunctionDeclaration30", None)
        self.__C_Declarations_PrototypeFunctionDeclaration30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Types_Type31"):
                opp_val = getattr(old_value, "Types_Type31", None)
                if opp_val == self:
                    setattr(old_value, "Types_Type31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Types_Type31"):
                opp_val = getattr(value, "Types_Type31", None)
                setattr(value, "Types_Type31", self)

    @property
    def C_Declarations_PrototypeFunctionDeclaration(self):
        return self.__C_Declarations_PrototypeFunctionDeclaration

    @C_Declarations_PrototypeFunctionDeclaration.setter
    def C_Declarations_PrototypeFunctionDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C_Declarations_PrototypeFunctionDeclaration__C_Declarations_PrototypeFunctionDeclaration", None)
        self.__C_Declarations_PrototypeFunctionDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Declarations_VariableDeclaration"):
                    opp_val = getattr(item, "Declarations_VariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "Declarations_VariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Declarations_VariableDeclaration"):
                    opp_val = getattr(item, "Declarations_VariableDeclaration", None)
                    
                    setattr(item, "Declarations_VariableDeclaration", self)
                    

class C_Declarations_VariableDeclaration(Declaration):

    def __init__(self, isAPointer: str, numberOfPointers: str):
        self.isAPointer = isAPointer
        self.numberOfPointers = numberOfPointers
        
    @property
    def numberOfPointers(self) -> str:
        return self.__numberOfPointers

    @numberOfPointers.setter
    def numberOfPointers(self, numberOfPointers: str):
        self.__numberOfPointers = numberOfPointers

    @property
    def isAPointer(self) -> str:
        return self.__isAPointer

    @isAPointer.setter
    def isAPointer(self, isAPointer: str):
        self.__isAPointer = isAPointer

class C_Declarations_ConstantDeclaration(Declaration):

    pass
class Main_Function:

    pass
class CompilationDirectiveDeclarations_CompilationDirectiveDeclaration:

    pass
class C_Main_Block:

    pass
class Abstractions_BlockedElement:

    pass
class C_Declarations_SimpleVariableDeclaration(Abstractions_BlockedElement, Declarations_VariableDeclaration):

    pass
class C_Declarations_ArrayDeclaration(Abstractions_BlockedElement, Declarations_CompositeVariableDeclaration):

    def __init__(self, dimensions: str, C_Declarations_ArrayDeclaration: "Expressions_Construction" = None, C_Declarations_ArrayDeclaration35: "Types_Type" = None, Abstractions_BlockedElement: "C_Main_Block"):
        self.dimensions = dimensions
        self.C_Declarations_ArrayDeclaration = C_Declarations_ArrayDeclaration
        self.C_Declarations_ArrayDeclaration35 = C_Declarations_ArrayDeclaration35
        
    @property
    def dimensions(self) -> str:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions

    @property
    def C_Declarations_ArrayDeclaration(self):
        return self.__C_Declarations_ArrayDeclaration

    @C_Declarations_ArrayDeclaration.setter
    def C_Declarations_ArrayDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C_Declarations_ArrayDeclaration__C_Declarations_ArrayDeclaration", None)
        self.__C_Declarations_ArrayDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expressions_Construction"):
                opp_val = getattr(old_value, "Expressions_Construction", None)
                if opp_val == self:
                    setattr(old_value, "Expressions_Construction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expressions_Construction"):
                opp_val = getattr(value, "Expressions_Construction", None)
                setattr(value, "Expressions_Construction", self)

    @property
    def C_Declarations_ArrayDeclaration35(self):
        return self.__C_Declarations_ArrayDeclaration35

    @C_Declarations_ArrayDeclaration35.setter
    def C_Declarations_ArrayDeclaration35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C_Declarations_ArrayDeclaration__C_Declarations_ArrayDeclaration35", None)
        self.__C_Declarations_ArrayDeclaration35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Types_Type36"):
                opp_val = getattr(old_value, "Types_Type36", None)
                if opp_val == self:
                    setattr(old_value, "Types_Type36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Types_Type36"):
                opp_val = getattr(value, "Types_Type36", None)
                setattr(value, "Types_Type36", self)

class Main_DeclarationsBlock:

    pass
class Declarations_Declaration:

    pass
class Element:

    pass
class C_Main_FunctionsBlock(Element):

    pass
class C_Main_DeclarationsBlock(Element):

    pass
class C_Main_Function(Element):

    def __init__(self, modifier: str, functionModifier: str, C_Main_Function: "Types_Type" = None, C_Main_Function7: "Main_Block" = None, C_Main_Function10: set["Declarations_Declaration"] = None):
        self.modifier = modifier
        self.functionModifier = functionModifier
        self.C_Main_Function = C_Main_Function
        self.C_Main_Function7 = C_Main_Function7
        self.C_Main_Function10 = C_Main_Function10 if C_Main_Function10 is not None else set()
        
    @property
    def functionModifier(self) -> str:
        return self.__functionModifier

    @functionModifier.setter
    def functionModifier(self, functionModifier: str):
        self.__functionModifier = functionModifier

    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def C_Main_Function10(self):
        return self.__C_Main_Function10

    @C_Main_Function10.setter
    def C_Main_Function10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C_Main_Function__C_Main_Function10", None)
        self.__C_Main_Function10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Declarations_Declaration"):
                    opp_val = getattr(item, "Declarations_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "Declarations_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Declarations_Declaration"):
                    opp_val = getattr(item, "Declarations_Declaration", None)
                    
                    setattr(item, "Declarations_Declaration", self)
                    

    @property
    def C_Main_Function7(self):
        return self.__C_Main_Function7

    @C_Main_Function7.setter
    def C_Main_Function7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C_Main_Function__C_Main_Function7", None)
        self.__C_Main_Function7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Main_Block8"):
                opp_val = getattr(old_value, "Main_Block8", None)
                if opp_val == self:
                    setattr(old_value, "Main_Block8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Main_Block8"):
                opp_val = getattr(value, "Main_Block8", None)
                setattr(value, "Main_Block8", self)

    @property
    def C_Main_Function(self):
        return self.__C_Main_Function

    @C_Main_Function.setter
    def C_Main_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C_Main_Function__C_Main_Function", None)
        self.__C_Main_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Types_Type"):
                opp_val = getattr(old_value, "Types_Type", None)
                if opp_val == self:
                    setattr(old_value, "Types_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Types_Type"):
                opp_val = getattr(value, "Types_Type", None)
                setattr(value, "Types_Type", self)

class C_Main_Program:

    def __init__(self, description: str, C_Main_Program: set["Main_Unit"] = None):
        self.description = description
        self.C_Main_Program = C_Main_Program if C_Main_Program is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def C_Main_Program(self):
        return self.__C_Main_Program

    @C_Main_Program.setter
    def C_Main_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C_Main_Program__C_Main_Program", None)
        self.__C_Main_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Main_Unit"):
                    opp_val = getattr(item, "Main_Unit", None)
                    
                    if opp_val == self:
                        setattr(item, "Main_Unit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Main_Unit"):
                    opp_val = getattr(item, "Main_Unit", None)
                    
                    setattr(item, "Main_Unit", self)
                    

class Main_Element:

    pass
class Unit:

    pass
class C_Main_H_Unit(Unit):

    pass
class C_Main_C_Unit(Unit):

    pass
class Main_Comment:

    pass
class NamedElement:

    pass
class C_Declarations_Declaration(NamedElement):

    def __init__(self, modifier: str):
        self.modifier = modifier
        
    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

class C_Main_Element(NamedElement):

    pass
class C_Main_Comment(NamedElement):

    pass
class C_Main_Unit(NamedElement):

    pass
class Main_Unit:

    pass
class Main_Block:

    pass
class C_Abstractions_BlockedElement(ABC):

    pass
class C_Abstractions_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Abstractions_NamedElement:

    pass
class C_CompilationDirectiveDeclarations_SimpleDirectiveDeclaration(Abstractions_NamedElement, CompilationDirectiveDeclarations_CompilationDirectiveDeclaration):

    pass
class C_Declarations_FragmentVariableDeclaration(Abstractions_NamedElement, Declarations_VariableDeclaration):

    pass
class C_Expressions_AtomicConditionalExpression(Expressions_ConditionalExpression, Abstractions_NamedElement):

    pass
class C_Commands_LabelCommand(Abstractions_NamedElement, Commands_Command):

    pass
class C_Expressions_FunctionCall(Abstractions_NamedElement, Expressions_Expression):

    pass
class C_Expressions_Access(Abstractions_NamedElement, Expressions_Expression):

    pass
class C_CompilationDirectiveDeclarations_Ifdef(Abstractions_NamedElement, CompilationDirectiveDeclarations_ComplexDirectiveDeclaration):

    pass
class Types_Type:

    pass
class C_Types_FromHeader(Abstractions_NamedElement, Types_Type):

    pass
class Type:

    pass
class C_Types_CompositeType(Type):

    pass
class C_Types_PrimitiveType(Type):

    pass
class CompositeType:

    pass
class C_Types_Struct(CompositeType):

    pass
class C_Types_Enum(CompositeType):

    pass
class C_Types_Array(CompositeType):

    pass
class C_Types_Typedef(CompositeType):

    pass
class Types_Array:

    pass
class Types_PrimitiveType:

    pass
class C_Types_Int(Types_Array, Types_PrimitiveType):

    pass
class PrimitiveType:

    pass
class C_Types_Short(PrimitiveType):

    pass
class C_Types_Float(PrimitiveType):

    pass
class C_Types_Void(PrimitiveType):

    pass
class C_Types_Double(PrimitiveType):

    pass
class C_Types_Char(PrimitiveType):

    pass
class C_Types_Type(ABC):

    pass