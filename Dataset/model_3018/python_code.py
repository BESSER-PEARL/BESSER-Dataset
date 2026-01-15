from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveType(Enum):
    Int = "Int"
    Real = "Real"
    Bool = "Bool"


############################################
# Definition of Classes
############################################

class ItemIdValue:

    pass
class ir_ItemIdValueCall(ItemIdValue):

    pass
class ir_ItemIdValueIterator(ItemIdValue):

    def __init__(self, shift: int, ir_ItemIdValueIterator: "ir_Iterator" = None):
        self.shift = shift
        self.ir_ItemIdValueIterator = ir_ItemIdValueIterator
        
    @property
    def shift(self) -> int:
        return self.__shift

    @shift.setter
    def shift(self, shift: int):
        self.__shift = shift

    @property
    def ir_ItemIdValueIterator(self):
        return self.__ir_ItemIdValueIterator

    @ir_ItemIdValueIterator.setter
    def ir_ItemIdValueIterator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ItemIdValueIterator__ir_ItemIdValueIterator", None)
        self.__ir_ItemIdValueIterator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Iterator216"):
                opp_val = getattr(old_value, "ir_Iterator216", None)
                if opp_val == self:
                    setattr(old_value, "ir_Iterator216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Iterator216"):
                opp_val = getattr(value, "ir_Iterator216", None)
                setattr(value, "ir_Iterator216", self)

class Container:

    pass
class ir_SetRef(Container):

    pass
class IrType:

    pass
class Expression:

    pass
class ir_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class ir_Parenthesis(Expression):

    pass
class ir_MinConstant(Expression):

    pass
class ir_UnaryExpression(Expression):

    def __init__(self, operator: str, ir_UnaryExpression: "ir_Expression" = None):
        self.operator = operator
        self.ir_UnaryExpression = ir_UnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ir_UnaryExpression(self):
        return self.__ir_UnaryExpression

    @ir_UnaryExpression.setter
    def ir_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_UnaryExpression__ir_UnaryExpression", None)
        self.__ir_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Expression167"):
                opp_val = getattr(old_value, "ir_Expression167", None)
                if opp_val == self:
                    setattr(old_value, "ir_Expression167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Expression167"):
                opp_val = getattr(value, "ir_Expression167", None)
                setattr(value, "ir_Expression167", self)

class ir_BaseTypeConstant(Expression):

    pass
class ir_BoolConstant(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class ir_VectorConstant(Expression):

    pass
class ir_Cardinality(Expression):

    pass
class ir_RealConstant(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class ir_BinaryExpression(Expression):

    def __init__(self, operator: str, ir_BinaryExpression: "ir_Expression" = None, ir_BinaryExpression164: "ir_Expression" = None):
        self.operator = operator
        self.ir_BinaryExpression = ir_BinaryExpression
        self.ir_BinaryExpression164 = ir_BinaryExpression164
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ir_BinaryExpression164(self):
        return self.__ir_BinaryExpression164

    @ir_BinaryExpression164.setter
    def ir_BinaryExpression164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_BinaryExpression__ir_BinaryExpression164", None)
        self.__ir_BinaryExpression164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Expression165"):
                opp_val = getattr(old_value, "ir_Expression165", None)
                if opp_val == self:
                    setattr(old_value, "ir_Expression165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Expression165"):
                opp_val = getattr(value, "ir_Expression165", None)
                setattr(value, "ir_Expression165", self)

    @property
    def ir_BinaryExpression(self):
        return self.__ir_BinaryExpression

    @ir_BinaryExpression.setter
    def ir_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_BinaryExpression__ir_BinaryExpression", None)
        self.__ir_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Expression162"):
                opp_val = getattr(old_value, "ir_Expression162", None)
                if opp_val == self:
                    setattr(old_value, "ir_Expression162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Expression162"):
                opp_val = getattr(value, "ir_Expression162", None)
                setattr(value, "ir_Expression162", self)

class ir_ContractedIf(Expression):

    pass
class ir_FunctionCall(Expression):

    pass
class ir_MaxConstant(Expression):

    pass
class IterationBlock:

    pass
class ir_Interval(IterationBlock):

    pass
class ir_Iterator(IterationBlock):

    pass
class ir_ConnectivityCall(Container):

    pass
class IterableInstruction:

    pass
class ir_ReductionInstruction(IterableInstruction):

    pass
class Instruction:

    pass
class ir_VariableDefinition(Instruction):

    pass
class ir_Exit(Instruction):

    def __init__(self, message: str):
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

class ir_SetDefinition(Instruction):

    def __init__(self, name: str, ir_SetDefinition: "ir_ConnectivityCall" = None, ir_SetDefinition214: "ir_SetRef" = None):
        self.name = name
        self.ir_SetDefinition = ir_SetDefinition
        self.ir_SetDefinition214 = ir_SetDefinition214
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_SetDefinition(self):
        return self.__ir_SetDefinition

    @ir_SetDefinition.setter
    def ir_SetDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_SetDefinition__ir_SetDefinition", None)
        self.__ir_SetDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ConnectivityCall"):
                opp_val = getattr(old_value, "ir_ConnectivityCall", None)
                if opp_val == self:
                    setattr(old_value, "ir_ConnectivityCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ConnectivityCall"):
                opp_val = getattr(value, "ir_ConnectivityCall", None)
                setattr(value, "ir_ConnectivityCall", self)

    @property
    def ir_SetDefinition214(self):
        return self.__ir_SetDefinition214

    @ir_SetDefinition214.setter
    def ir_SetDefinition214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_SetDefinition__ir_SetDefinition214", None)
        self.__ir_SetDefinition214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_SetRef"):
                opp_val = getattr(old_value, "ir_SetRef", None)
                if opp_val == self:
                    setattr(old_value, "ir_SetRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_SetRef"):
                opp_val = getattr(value, "ir_SetRef", None)
                setattr(value, "ir_SetRef", self)

class ir_IterableInstruction(Instruction):

    pass
class ir_ItemIdDefinition(Instruction):

    pass
class ir_Return(Instruction):

    pass
class ir_If(Instruction):

    pass
class ir_Affectation(Instruction):

    pass
class ir_ItemIndexDefinition(Instruction):

    pass
class ir_InstructionBlock(Instruction):

    pass
class ir_Loop(IterableInstruction):

    def __init__(self, multithreadable: bool, ir_Loop: "ir_Instruction" = None):
        self.multithreadable = multithreadable
        self.ir_Loop = ir_Loop
        
    @property
    def multithreadable(self) -> bool:
        return self.__multithreadable

    @multithreadable.setter
    def multithreadable(self, multithreadable: bool):
        self.__multithreadable = multithreadable

    @property
    def ir_Loop(self):
        return self.__ir_Loop

    @ir_Loop.setter
    def ir_Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Loop__ir_Loop", None)
        self.__ir_Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Instruction121"):
                opp_val = getattr(old_value, "ir_Instruction121", None)
                if opp_val == self:
                    setattr(old_value, "ir_Instruction121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Instruction121"):
                opp_val = getattr(value, "ir_Instruction121", None)
                setattr(value, "ir_Instruction121", self)

class TimeLoopCopyJob:

    pass
class ir_BeforeTimeLoopJob(TimeLoopCopyJob):

    pass
class ir_AfterTimeLoopJob(TimeLoopCopyJob):

    pass
class Job:

    pass
class ir_InstructionJob(Job):

    pass
class ir_ArgOrVarRef(Expression):

    pass
class ir_ConnectivityType(IrType):

    pass
class ir_TimeLoopCopyJob(Job):

    pass
class ir_BaseType(IrType):

    def __init__(self, primitive: str, ir_BaseType: "ir_Arg" = None, ir_BaseType58: "ir_SimpleVariable" = None, ir_BaseType68: "ir_Function" = None, ir_BaseType190: set["ir_Expression"] = None, ir_BaseType197: "ir_ConnectivityType" = None):
        self.primitive = primitive
        self.ir_BaseType = ir_BaseType
        self.ir_BaseType58 = ir_BaseType58
        self.ir_BaseType68 = ir_BaseType68
        self.ir_BaseType190 = ir_BaseType190 if ir_BaseType190 is not None else set()
        self.ir_BaseType197 = ir_BaseType197
        
    @property
    def primitive(self) -> str:
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: str):
        self.__primitive = primitive

    @property
    def ir_BaseType58(self):
        return self.__ir_BaseType58

    @ir_BaseType58.setter
    def ir_BaseType58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_BaseType__ir_BaseType58", None)
        self.__ir_BaseType58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_SimpleVariable57"):
                opp_val = getattr(old_value, "ir_SimpleVariable57", None)
                if opp_val == self:
                    setattr(old_value, "ir_SimpleVariable57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_SimpleVariable57"):
                opp_val = getattr(value, "ir_SimpleVariable57", None)
                setattr(value, "ir_SimpleVariable57", self)

    @property
    def ir_BaseType68(self):
        return self.__ir_BaseType68

    @ir_BaseType68.setter
    def ir_BaseType68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_BaseType__ir_BaseType68", None)
        self.__ir_BaseType68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Function67"):
                opp_val = getattr(old_value, "ir_Function67", None)
                if opp_val == self:
                    setattr(old_value, "ir_Function67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Function67"):
                opp_val = getattr(value, "ir_Function67", None)
                setattr(value, "ir_Function67", self)

    @property
    def ir_BaseType(self):
        return self.__ir_BaseType

    @ir_BaseType.setter
    def ir_BaseType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_BaseType__ir_BaseType", None)
        self.__ir_BaseType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Arg"):
                opp_val = getattr(old_value, "ir_Arg", None)
                if opp_val == self:
                    setattr(old_value, "ir_Arg", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Arg"):
                opp_val = getattr(value, "ir_Arg", None)
                setattr(value, "ir_Arg", self)

    @property
    def ir_BaseType197(self):
        return self.__ir_BaseType197

    @ir_BaseType197.setter
    def ir_BaseType197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_BaseType__ir_BaseType197", None)
        self.__ir_BaseType197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ConnectivityType196"):
                opp_val = getattr(old_value, "ir_ConnectivityType196", None)
                if opp_val == self:
                    setattr(old_value, "ir_ConnectivityType196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ConnectivityType196"):
                opp_val = getattr(value, "ir_ConnectivityType196", None)
                setattr(value, "ir_ConnectivityType196", self)

    @property
    def ir_BaseType190(self):
        return self.__ir_BaseType190

    @ir_BaseType190.setter
    def ir_BaseType190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_BaseType__ir_BaseType190", None)
        self.__ir_BaseType190 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Expression191"):
                    opp_val = getattr(item, "ir_Expression191", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Expression191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Expression191"):
                    opp_val = getattr(item, "ir_Expression191", None)
                    
                    setattr(item, "ir_Expression191", self)
                    

class ArgOrVar:

    pass
class ir_Arg(ArgOrVar):

    pass
class Variable:

    pass
class ir_ConnectivityVariable(Variable):

    pass
class ir_Variable(ArgOrVar):

    def __init__(self, persistenceName: str, const: bool, ir_Variable: "ir_IrModule" = None, ir_Variable34: "ir_PostProcessingInfo" = None, ir_Variable92: "ir_TimeLoopCopy" = None, ir_Variable95: "ir_TimeLoopCopy" = None, ir_Variable97: "ir_InstructionBlock" = None, ir_Variable102: "ir_VariableDefinition" = None, ir_Variable200: "ir_TimeLoopVariable" = None, ir_Variable203: "ir_TimeLoopVariable" = None, ir_Variable206: "ir_TimeLoopVariable" = None):
        self.persistenceName = persistenceName
        self.const = const
        self.ir_Variable = ir_Variable
        self.ir_Variable34 = ir_Variable34
        self.ir_Variable92 = ir_Variable92
        self.ir_Variable95 = ir_Variable95
        self.ir_Variable97 = ir_Variable97
        self.ir_Variable102 = ir_Variable102
        self.ir_Variable200 = ir_Variable200
        self.ir_Variable203 = ir_Variable203
        self.ir_Variable206 = ir_Variable206
        
    @property
    def const(self) -> bool:
        return self.__const

    @const.setter
    def const(self, const: bool):
        self.__const = const

    @property
    def persistenceName(self) -> str:
        return self.__persistenceName

    @persistenceName.setter
    def persistenceName(self, persistenceName: str):
        self.__persistenceName = persistenceName

    @property
    def ir_Variable200(self):
        return self.__ir_Variable200

    @ir_Variable200.setter
    def ir_Variable200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable200", None)
        self.__ir_Variable200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TimeLoopVariable199"):
                opp_val = getattr(old_value, "ir_TimeLoopVariable199", None)
                if opp_val == self:
                    setattr(old_value, "ir_TimeLoopVariable199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TimeLoopVariable199"):
                opp_val = getattr(value, "ir_TimeLoopVariable199", None)
                setattr(value, "ir_TimeLoopVariable199", self)

    @property
    def ir_Variable34(self):
        return self.__ir_Variable34

    @ir_Variable34.setter
    def ir_Variable34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable34", None)
        self.__ir_Variable34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_PostProcessingInfo33"):
                opp_val = getattr(old_value, "ir_PostProcessingInfo33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_PostProcessingInfo33"):
                opp_val = getattr(value, "ir_PostProcessingInfo33", None)
                if opp_val is None:
                    setattr(value, "ir_PostProcessingInfo33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Variable97(self):
        return self.__ir_Variable97

    @ir_Variable97.setter
    def ir_Variable97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable97", None)
        self.__ir_Variable97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_InstructionBlock"):
                opp_val = getattr(old_value, "ir_InstructionBlock", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_InstructionBlock"):
                opp_val = getattr(value, "ir_InstructionBlock", None)
                if opp_val is None:
                    setattr(value, "ir_InstructionBlock", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Variable(self):
        return self.__ir_Variable

    @ir_Variable.setter
    def ir_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable", None)
        self.__ir_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_IrModule14"):
                opp_val = getattr(old_value, "ir_IrModule14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_IrModule14"):
                opp_val = getattr(value, "ir_IrModule14", None)
                if opp_val is None:
                    setattr(value, "ir_IrModule14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Variable95(self):
        return self.__ir_Variable95

    @ir_Variable95.setter
    def ir_Variable95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable95", None)
        self.__ir_Variable95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TimeLoopCopy94"):
                opp_val = getattr(old_value, "ir_TimeLoopCopy94", None)
                if opp_val == self:
                    setattr(old_value, "ir_TimeLoopCopy94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TimeLoopCopy94"):
                opp_val = getattr(value, "ir_TimeLoopCopy94", None)
                setattr(value, "ir_TimeLoopCopy94", self)

    @property
    def ir_Variable206(self):
        return self.__ir_Variable206

    @ir_Variable206.setter
    def ir_Variable206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable206", None)
        self.__ir_Variable206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TimeLoopVariable205"):
                opp_val = getattr(old_value, "ir_TimeLoopVariable205", None)
                if opp_val == self:
                    setattr(old_value, "ir_TimeLoopVariable205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TimeLoopVariable205"):
                opp_val = getattr(value, "ir_TimeLoopVariable205", None)
                setattr(value, "ir_TimeLoopVariable205", self)

    @property
    def ir_Variable92(self):
        return self.__ir_Variable92

    @ir_Variable92.setter
    def ir_Variable92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable92", None)
        self.__ir_Variable92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TimeLoopCopy91"):
                opp_val = getattr(old_value, "ir_TimeLoopCopy91", None)
                if opp_val == self:
                    setattr(old_value, "ir_TimeLoopCopy91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TimeLoopCopy91"):
                opp_val = getattr(value, "ir_TimeLoopCopy91", None)
                setattr(value, "ir_TimeLoopCopy91", self)

    @property
    def ir_Variable102(self):
        return self.__ir_Variable102

    @ir_Variable102.setter
    def ir_Variable102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable102", None)
        self.__ir_Variable102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_VariableDefinition"):
                opp_val = getattr(old_value, "ir_VariableDefinition", None)
                if opp_val == self:
                    setattr(old_value, "ir_VariableDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_VariableDefinition"):
                opp_val = getattr(value, "ir_VariableDefinition", None)
                setattr(value, "ir_VariableDefinition", self)

    @property
    def ir_Variable203(self):
        return self.__ir_Variable203

    @ir_Variable203.setter
    def ir_Variable203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Variable__ir_Variable203", None)
        self.__ir_Variable203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TimeLoopVariable202"):
                opp_val = getattr(old_value, "ir_TimeLoopVariable202", None)
                if opp_val == self:
                    setattr(old_value, "ir_TimeLoopVariable202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TimeLoopVariable202"):
                opp_val = getattr(value, "ir_TimeLoopVariable202", None)
                setattr(value, "ir_TimeLoopVariable202", self)

class ir_SimpleVariable(Variable):

    pass
class JobContainer:

    pass
class ir_TimeLoopJob(TimeLoopCopyJob, JobContainer):

    pass
class ir_IrModule(JobContainer):

    def __init__(self, name: str, ir_IrModule24: "ir_SimpleVariable" = None, ir_IrModule27: set["ir_Job"] = None, ir_IrModule: set["ir_Import"] = None, ir_IrModule6: set["ir_ItemType"] = None, ir_IrModule8: set["ir_Function"] = None, ir_IrModule10: set["ir_Connectivity"] = None, ir_IrModule12: set["ir_SimpleVariable"] = None, ir_IrModule14: set["ir_Variable"] = None, ir_IrModule16: "ir_ConnectivityVariable" = None, ir_IrModule18: "ir_ConnectivityVariable" = None, ir_IrModule21: "ir_SimpleVariable" = None, ir_IrModule29: "ir_TimeLoop" = None, ir_IrModule31: "ir_PostProcessingInfo" = None):
        self.name = name
        self.ir_IrModule24 = ir_IrModule24
        self.ir_IrModule27 = ir_IrModule27 if ir_IrModule27 is not None else set()
        self.ir_IrModule = ir_IrModule if ir_IrModule is not None else set()
        self.ir_IrModule6 = ir_IrModule6 if ir_IrModule6 is not None else set()
        self.ir_IrModule8 = ir_IrModule8 if ir_IrModule8 is not None else set()
        self.ir_IrModule10 = ir_IrModule10 if ir_IrModule10 is not None else set()
        self.ir_IrModule12 = ir_IrModule12 if ir_IrModule12 is not None else set()
        self.ir_IrModule14 = ir_IrModule14 if ir_IrModule14 is not None else set()
        self.ir_IrModule16 = ir_IrModule16
        self.ir_IrModule18 = ir_IrModule18
        self.ir_IrModule21 = ir_IrModule21
        self.ir_IrModule29 = ir_IrModule29
        self.ir_IrModule31 = ir_IrModule31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_IrModule18(self):
        return self.__ir_IrModule18

    @ir_IrModule18.setter
    def ir_IrModule18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule18", None)
        self.__ir_IrModule18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ConnectivityVariable19"):
                opp_val = getattr(old_value, "ir_ConnectivityVariable19", None)
                if opp_val == self:
                    setattr(old_value, "ir_ConnectivityVariable19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ConnectivityVariable19"):
                opp_val = getattr(value, "ir_ConnectivityVariable19", None)
                setattr(value, "ir_ConnectivityVariable19", self)

    @property
    def ir_IrModule10(self):
        return self.__ir_IrModule10

    @ir_IrModule10.setter
    def ir_IrModule10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule10", None)
        self.__ir_IrModule10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Connectivity"):
                    opp_val = getattr(item, "ir_Connectivity", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Connectivity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Connectivity"):
                    opp_val = getattr(item, "ir_Connectivity", None)
                    
                    setattr(item, "ir_Connectivity", self)
                    

    @property
    def ir_IrModule14(self):
        return self.__ir_IrModule14

    @ir_IrModule14.setter
    def ir_IrModule14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule14", None)
        self.__ir_IrModule14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Variable"):
                    opp_val = getattr(item, "ir_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Variable"):
                    opp_val = getattr(item, "ir_Variable", None)
                    
                    setattr(item, "ir_Variable", self)
                    

    @property
    def ir_IrModule31(self):
        return self.__ir_IrModule31

    @ir_IrModule31.setter
    def ir_IrModule31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule31", None)
        self.__ir_IrModule31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_PostProcessingInfo"):
                opp_val = getattr(old_value, "ir_PostProcessingInfo", None)
                if opp_val == self:
                    setattr(old_value, "ir_PostProcessingInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_PostProcessingInfo"):
                opp_val = getattr(value, "ir_PostProcessingInfo", None)
                setattr(value, "ir_PostProcessingInfo", self)

    @property
    def ir_IrModule16(self):
        return self.__ir_IrModule16

    @ir_IrModule16.setter
    def ir_IrModule16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule16", None)
        self.__ir_IrModule16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ConnectivityVariable"):
                opp_val = getattr(old_value, "ir_ConnectivityVariable", None)
                if opp_val == self:
                    setattr(old_value, "ir_ConnectivityVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ConnectivityVariable"):
                opp_val = getattr(value, "ir_ConnectivityVariable", None)
                setattr(value, "ir_ConnectivityVariable", self)

    @property
    def ir_IrModule29(self):
        return self.__ir_IrModule29

    @ir_IrModule29.setter
    def ir_IrModule29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule29", None)
        self.__ir_IrModule29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TimeLoop"):
                opp_val = getattr(old_value, "ir_TimeLoop", None)
                if opp_val == self:
                    setattr(old_value, "ir_TimeLoop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TimeLoop"):
                opp_val = getattr(value, "ir_TimeLoop", None)
                setattr(value, "ir_TimeLoop", self)

    @property
    def ir_IrModule(self):
        return self.__ir_IrModule

    @ir_IrModule.setter
    def ir_IrModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule", None)
        self.__ir_IrModule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Import"):
                    opp_val = getattr(item, "ir_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Import"):
                    opp_val = getattr(item, "ir_Import", None)
                    
                    setattr(item, "ir_Import", self)
                    

    @property
    def ir_IrModule12(self):
        return self.__ir_IrModule12

    @ir_IrModule12.setter
    def ir_IrModule12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule12", None)
        self.__ir_IrModule12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_SimpleVariable"):
                    opp_val = getattr(item, "ir_SimpleVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_SimpleVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_SimpleVariable"):
                    opp_val = getattr(item, "ir_SimpleVariable", None)
                    
                    setattr(item, "ir_SimpleVariable", self)
                    

    @property
    def ir_IrModule27(self):
        return self.__ir_IrModule27

    @ir_IrModule27.setter
    def ir_IrModule27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule27", None)
        self.__ir_IrModule27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Job"):
                    opp_val = getattr(item, "ir_Job", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Job", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Job"):
                    opp_val = getattr(item, "ir_Job", None)
                    
                    setattr(item, "ir_Job", self)
                    

    @property
    def ir_IrModule24(self):
        return self.__ir_IrModule24

    @ir_IrModule24.setter
    def ir_IrModule24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule24", None)
        self.__ir_IrModule24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_SimpleVariable25"):
                opp_val = getattr(old_value, "ir_SimpleVariable25", None)
                if opp_val == self:
                    setattr(old_value, "ir_SimpleVariable25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_SimpleVariable25"):
                opp_val = getattr(value, "ir_SimpleVariable25", None)
                setattr(value, "ir_SimpleVariable25", self)

    @property
    def ir_IrModule21(self):
        return self.__ir_IrModule21

    @ir_IrModule21.setter
    def ir_IrModule21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule21", None)
        self.__ir_IrModule21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_SimpleVariable22"):
                opp_val = getattr(old_value, "ir_SimpleVariable22", None)
                if opp_val == self:
                    setattr(old_value, "ir_SimpleVariable22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_SimpleVariable22"):
                opp_val = getattr(value, "ir_SimpleVariable22", None)
                setattr(value, "ir_SimpleVariable22", self)

    @property
    def ir_IrModule8(self):
        return self.__ir_IrModule8

    @ir_IrModule8.setter
    def ir_IrModule8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule8", None)
        self.__ir_IrModule8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Function"):
                    opp_val = getattr(item, "ir_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Function"):
                    opp_val = getattr(item, "ir_Function", None)
                    
                    setattr(item, "ir_Function", self)
                    

    @property
    def ir_IrModule6(self):
        return self.__ir_IrModule6

    @ir_IrModule6.setter
    def ir_IrModule6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrModule__ir_IrModule6", None)
        self.__ir_IrModule6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_ItemType"):
                    opp_val = getattr(item, "ir_ItemType", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_ItemType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_ItemType"):
                    opp_val = getattr(item, "ir_ItemType", None)
                    
                    setattr(item, "ir_ItemType", self)
                    

class IrAnnotable:

    pass
class ir_IterationBlock(IrAnnotable):

    pass
class ir_ItemId(IrAnnotable):

    def __init__(self, name: str, itemName: str, ir_ItemId: "ir_ItemIdDefinition" = None, ir_ItemId212: "ir_ConnectivityCall" = None, ir_ItemId221: "ir_ItemIndexValue" = None):
        self.name = name
        self.itemName = itemName
        self.ir_ItemId = ir_ItemId
        self.ir_ItemId212 = ir_ItemId212
        self.ir_ItemId221 = ir_ItemId221
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def itemName(self) -> str:
        return self.__itemName

    @itemName.setter
    def itemName(self, itemName: str):
        self.__itemName = itemName

    @property
    def ir_ItemId221(self):
        return self.__ir_ItemId221

    @ir_ItemId221.setter
    def ir_ItemId221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ItemId__ir_ItemId221", None)
        self.__ir_ItemId221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ItemIndexValue220"):
                opp_val = getattr(old_value, "ir_ItemIndexValue220", None)
                if opp_val == self:
                    setattr(old_value, "ir_ItemIndexValue220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ItemIndexValue220"):
                opp_val = getattr(value, "ir_ItemIndexValue220", None)
                setattr(value, "ir_ItemIndexValue220", self)

    @property
    def ir_ItemId(self):
        return self.__ir_ItemId

    @ir_ItemId.setter
    def ir_ItemId(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ItemId__ir_ItemId", None)
        self.__ir_ItemId = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ItemIdDefinition"):
                opp_val = getattr(old_value, "ir_ItemIdDefinition", None)
                if opp_val == self:
                    setattr(old_value, "ir_ItemIdDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ItemIdDefinition"):
                opp_val = getattr(value, "ir_ItemIdDefinition", None)
                setattr(value, "ir_ItemIdDefinition", self)

    @property
    def ir_ItemId212(self):
        return self.__ir_ItemId212

    @ir_ItemId212.setter
    def ir_ItemId212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ItemId__ir_ItemId212", None)
        self.__ir_ItemId212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ConnectivityCall211"):
                opp_val = getattr(old_value, "ir_ConnectivityCall211", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ConnectivityCall211"):
                opp_val = getattr(value, "ir_ConnectivityCall211", None)
                if opp_val is None:
                    setattr(value, "ir_ConnectivityCall211", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ir_ItemIdValue(IrAnnotable):

    pass
class ir_TimeLoopVariable(IrAnnotable):

    def __init__(self, name: str, ir_TimeLoopVariable: "ir_TimeLoop" = None, ir_TimeLoopVariable199: "ir_Variable" = None, ir_TimeLoopVariable202: "ir_Variable" = None, ir_TimeLoopVariable205: "ir_Variable" = None):
        self.name = name
        self.ir_TimeLoopVariable = ir_TimeLoopVariable
        self.ir_TimeLoopVariable199 = ir_TimeLoopVariable199
        self.ir_TimeLoopVariable202 = ir_TimeLoopVariable202
        self.ir_TimeLoopVariable205 = ir_TimeLoopVariable205
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_TimeLoopVariable199(self):
        return self.__ir_TimeLoopVariable199

    @ir_TimeLoopVariable199.setter
    def ir_TimeLoopVariable199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoopVariable__ir_TimeLoopVariable199", None)
        self.__ir_TimeLoopVariable199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Variable200"):
                opp_val = getattr(old_value, "ir_Variable200", None)
                if opp_val == self:
                    setattr(old_value, "ir_Variable200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Variable200"):
                opp_val = getattr(value, "ir_Variable200", None)
                setattr(value, "ir_Variable200", self)

    @property
    def ir_TimeLoopVariable(self):
        return self.__ir_TimeLoopVariable

    @ir_TimeLoopVariable.setter
    def ir_TimeLoopVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoopVariable__ir_TimeLoopVariable", None)
        self.__ir_TimeLoopVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TimeLoop47"):
                opp_val = getattr(old_value, "ir_TimeLoop47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TimeLoop47"):
                opp_val = getattr(value, "ir_TimeLoop47", None)
                if opp_val is None:
                    setattr(value, "ir_TimeLoop47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_TimeLoopVariable205(self):
        return self.__ir_TimeLoopVariable205

    @ir_TimeLoopVariable205.setter
    def ir_TimeLoopVariable205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoopVariable__ir_TimeLoopVariable205", None)
        self.__ir_TimeLoopVariable205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Variable206"):
                opp_val = getattr(old_value, "ir_Variable206", None)
                if opp_val == self:
                    setattr(old_value, "ir_Variable206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Variable206"):
                opp_val = getattr(value, "ir_Variable206", None)
                setattr(value, "ir_Variable206", self)

    @property
    def ir_TimeLoopVariable202(self):
        return self.__ir_TimeLoopVariable202

    @ir_TimeLoopVariable202.setter
    def ir_TimeLoopVariable202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoopVariable__ir_TimeLoopVariable202", None)
        self.__ir_TimeLoopVariable202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Variable203"):
                opp_val = getattr(old_value, "ir_Variable203", None)
                if opp_val == self:
                    setattr(old_value, "ir_Variable203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Variable203"):
                opp_val = getattr(value, "ir_Variable203", None)
                setattr(value, "ir_Variable203", self)

class ir_PostProcessingInfo(IrAnnotable):

    def __init__(self, periodValue: float, ir_PostProcessingInfo: "ir_IrModule" = None, ir_PostProcessingInfo33: set["ir_Variable"] = None, ir_PostProcessingInfo36: "ir_SimpleVariable" = None, ir_PostProcessingInfo39: "ir_SimpleVariable" = None):
        self.periodValue = periodValue
        self.ir_PostProcessingInfo = ir_PostProcessingInfo
        self.ir_PostProcessingInfo33 = ir_PostProcessingInfo33 if ir_PostProcessingInfo33 is not None else set()
        self.ir_PostProcessingInfo36 = ir_PostProcessingInfo36
        self.ir_PostProcessingInfo39 = ir_PostProcessingInfo39
        
    @property
    def periodValue(self) -> float:
        return self.__periodValue

    @periodValue.setter
    def periodValue(self, periodValue: float):
        self.__periodValue = periodValue

    @property
    def ir_PostProcessingInfo36(self):
        return self.__ir_PostProcessingInfo36

    @ir_PostProcessingInfo36.setter
    def ir_PostProcessingInfo36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PostProcessingInfo__ir_PostProcessingInfo36", None)
        self.__ir_PostProcessingInfo36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_SimpleVariable37"):
                opp_val = getattr(old_value, "ir_SimpleVariable37", None)
                if opp_val == self:
                    setattr(old_value, "ir_SimpleVariable37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_SimpleVariable37"):
                opp_val = getattr(value, "ir_SimpleVariable37", None)
                setattr(value, "ir_SimpleVariable37", self)

    @property
    def ir_PostProcessingInfo33(self):
        return self.__ir_PostProcessingInfo33

    @ir_PostProcessingInfo33.setter
    def ir_PostProcessingInfo33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PostProcessingInfo__ir_PostProcessingInfo33", None)
        self.__ir_PostProcessingInfo33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Variable34"):
                    opp_val = getattr(item, "ir_Variable34", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Variable34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Variable34"):
                    opp_val = getattr(item, "ir_Variable34", None)
                    
                    setattr(item, "ir_Variable34", self)
                    

    @property
    def ir_PostProcessingInfo39(self):
        return self.__ir_PostProcessingInfo39

    @ir_PostProcessingInfo39.setter
    def ir_PostProcessingInfo39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PostProcessingInfo__ir_PostProcessingInfo39", None)
        self.__ir_PostProcessingInfo39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_SimpleVariable40"):
                opp_val = getattr(old_value, "ir_SimpleVariable40", None)
                if opp_val == self:
                    setattr(old_value, "ir_SimpleVariable40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_SimpleVariable40"):
                opp_val = getattr(value, "ir_SimpleVariable40", None)
                setattr(value, "ir_SimpleVariable40", self)

    @property
    def ir_PostProcessingInfo(self):
        return self.__ir_PostProcessingInfo

    @ir_PostProcessingInfo.setter
    def ir_PostProcessingInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_PostProcessingInfo__ir_PostProcessingInfo", None)
        self.__ir_PostProcessingInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_IrModule31"):
                opp_val = getattr(old_value, "ir_IrModule31", None)
                if opp_val == self:
                    setattr(old_value, "ir_IrModule31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_IrModule31"):
                opp_val = getattr(value, "ir_IrModule31", None)
                setattr(value, "ir_IrModule31", self)

class ir_ArgOrVar(IrAnnotable):

    def __init__(self, name: str, ir_ArgOrVar: "ir_ArgOrVarRef" = None):
        self.name = name
        self.ir_ArgOrVar = ir_ArgOrVar
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_ArgOrVar(self):
        return self.__ir_ArgOrVar

    @ir_ArgOrVar.setter
    def ir_ArgOrVar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ArgOrVar__ir_ArgOrVar", None)
        self.__ir_ArgOrVar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ArgOrVarRef182"):
                opp_val = getattr(old_value, "ir_ArgOrVarRef182", None)
                if opp_val == self:
                    setattr(old_value, "ir_ArgOrVarRef182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ArgOrVarRef182"):
                opp_val = getattr(value, "ir_ArgOrVarRef182", None)
                setattr(value, "ir_ArgOrVarRef182", self)

class ir_Connectivity(IrAnnotable):

    def __init__(self, name: str, indexEqualId: bool, multiple: bool, ir_Connectivity: "ir_IrModule" = None, ir_Connectivity78: set["ir_ItemType"] = None, ir_Connectivity81: "ir_ItemType" = None, ir_Connectivity194: "ir_ConnectivityType" = None, ir_Connectivity209: "ir_ConnectivityCall" = None):
        self.name = name
        self.indexEqualId = indexEqualId
        self.multiple = multiple
        self.ir_Connectivity = ir_Connectivity
        self.ir_Connectivity78 = ir_Connectivity78 if ir_Connectivity78 is not None else set()
        self.ir_Connectivity81 = ir_Connectivity81
        self.ir_Connectivity194 = ir_Connectivity194
        self.ir_Connectivity209 = ir_Connectivity209
        
    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def indexEqualId(self) -> bool:
        return self.__indexEqualId

    @indexEqualId.setter
    def indexEqualId(self, indexEqualId: bool):
        self.__indexEqualId = indexEqualId

    @property
    def ir_Connectivity81(self):
        return self.__ir_Connectivity81

    @ir_Connectivity81.setter
    def ir_Connectivity81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Connectivity__ir_Connectivity81", None)
        self.__ir_Connectivity81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ItemType82"):
                opp_val = getattr(old_value, "ir_ItemType82", None)
                if opp_val == self:
                    setattr(old_value, "ir_ItemType82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ItemType82"):
                opp_val = getattr(value, "ir_ItemType82", None)
                setattr(value, "ir_ItemType82", self)

    @property
    def ir_Connectivity(self):
        return self.__ir_Connectivity

    @ir_Connectivity.setter
    def ir_Connectivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Connectivity__ir_Connectivity", None)
        self.__ir_Connectivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_IrModule10"):
                opp_val = getattr(old_value, "ir_IrModule10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_IrModule10"):
                opp_val = getattr(value, "ir_IrModule10", None)
                if opp_val is None:
                    setattr(value, "ir_IrModule10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Connectivity78(self):
        return self.__ir_Connectivity78

    @ir_Connectivity78.setter
    def ir_Connectivity78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Connectivity__ir_Connectivity78", None)
        self.__ir_Connectivity78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_ItemType79"):
                    opp_val = getattr(item, "ir_ItemType79", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_ItemType79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_ItemType79"):
                    opp_val = getattr(item, "ir_ItemType79", None)
                    
                    setattr(item, "ir_ItemType79", self)
                    

    @property
    def ir_Connectivity194(self):
        return self.__ir_Connectivity194

    @ir_Connectivity194.setter
    def ir_Connectivity194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Connectivity__ir_Connectivity194", None)
        self.__ir_Connectivity194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ConnectivityType193"):
                opp_val = getattr(old_value, "ir_ConnectivityType193", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ConnectivityType193"):
                opp_val = getattr(value, "ir_ConnectivityType193", None)
                if opp_val is None:
                    setattr(value, "ir_ConnectivityType193", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Connectivity209(self):
        return self.__ir_Connectivity209

    @ir_Connectivity209.setter
    def ir_Connectivity209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Connectivity__ir_Connectivity209", None)
        self.__ir_Connectivity209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ConnectivityCall208"):
                opp_val = getattr(old_value, "ir_ConnectivityCall208", None)
                if opp_val == self:
                    setattr(old_value, "ir_ConnectivityCall208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ConnectivityCall208"):
                opp_val = getattr(value, "ir_ConnectivityCall208", None)
                setattr(value, "ir_ConnectivityCall208", self)

class ir_ItemType(IrAnnotable):

    def __init__(self, name: str, ir_ItemType: "ir_IrModule" = None, ir_ItemType79: "ir_Connectivity" = None, ir_ItemType82: "ir_Connectivity" = None):
        self.name = name
        self.ir_ItemType = ir_ItemType
        self.ir_ItemType79 = ir_ItemType79
        self.ir_ItemType82 = ir_ItemType82
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_ItemType(self):
        return self.__ir_ItemType

    @ir_ItemType.setter
    def ir_ItemType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ItemType__ir_ItemType", None)
        self.__ir_ItemType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_IrModule6"):
                opp_val = getattr(old_value, "ir_IrModule6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_IrModule6"):
                opp_val = getattr(value, "ir_IrModule6", None)
                if opp_val is None:
                    setattr(value, "ir_IrModule6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_ItemType79(self):
        return self.__ir_ItemType79

    @ir_ItemType79.setter
    def ir_ItemType79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ItemType__ir_ItemType79", None)
        self.__ir_ItemType79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Connectivity78"):
                opp_val = getattr(old_value, "ir_Connectivity78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Connectivity78"):
                opp_val = getattr(value, "ir_Connectivity78", None)
                if opp_val is None:
                    setattr(value, "ir_Connectivity78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_ItemType82(self):
        return self.__ir_ItemType82

    @ir_ItemType82.setter
    def ir_ItemType82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ItemType__ir_ItemType82", None)
        self.__ir_ItemType82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Connectivity81"):
                opp_val = getattr(old_value, "ir_Connectivity81", None)
                if opp_val == self:
                    setattr(old_value, "ir_Connectivity81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Connectivity81"):
                opp_val = getattr(value, "ir_Connectivity81", None)
                setattr(value, "ir_Connectivity81", self)

class ir_Job(IrAnnotable):

    def __init__(self, name: str, at: float, onCycle: bool, ir_Job: "ir_IrModule" = None, Job: "ir_JobContainer" = None, innerJobs: "ir_JobContainer" = None):
        self.name = name
        self.at = at
        self.onCycle = onCycle
        self.ir_Job = ir_Job
        self.Job = Job
        self.innerJobs = innerJobs
        
    @property
    def at(self) -> float:
        return self.__at

    @at.setter
    def at(self, at: float):
        self.__at = at

    @property
    def onCycle(self) -> bool:
        return self.__onCycle

    @onCycle.setter
    def onCycle(self, onCycle: bool):
        self.__onCycle = onCycle

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_Job(self):
        return self.__ir_Job

    @ir_Job.setter
    def ir_Job(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Job__ir_Job", None)
        self.__ir_Job = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_IrModule27"):
                opp_val = getattr(old_value, "ir_IrModule27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_IrModule27"):
                opp_val = getattr(value, "ir_IrModule27", None)
                if opp_val is None:
                    setattr(value, "ir_IrModule27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def innerJobs(self):
        return self.__innerJobs

    @innerJobs.setter
    def innerJobs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Job__innerJobs", None)
        self.__innerJobs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JobContainer"):
                opp_val = getattr(old_value, "JobContainer", None)
                if opp_val == self:
                    setattr(old_value, "JobContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JobContainer"):
                opp_val = getattr(value, "JobContainer", None)
                setattr(value, "JobContainer", self)

    @property
    def Job(self):
        return self.__Job

    @Job.setter
    def Job(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Job__Job", None)
        self.__Job = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jobContainer"):
                opp_val = getattr(old_value, "jobContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jobContainer"):
                opp_val = getattr(value, "jobContainer", None)
                if opp_val is None:
                    setattr(value, "jobContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ir_Import(IrAnnotable):

    def __init__(self, importedNamespace: str, ir_Import: "ir_IrModule" = None):
        self.importedNamespace = importedNamespace
        self.ir_Import = ir_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def ir_Import(self):
        return self.__ir_Import

    @ir_Import.setter
    def ir_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Import__ir_Import", None)
        self.__ir_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_IrModule"):
                opp_val = getattr(old_value, "ir_IrModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_IrModule"):
                opp_val = getattr(value, "ir_IrModule", None)
                if opp_val is None:
                    setattr(value, "ir_IrModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ir_ItemIndex(IrAnnotable):

    def __init__(self, name: str, itemName: str, ir_ItemIndex: "ir_ItemIndexDefinition" = None, ir_ItemIndex140: "ir_Iterator" = None, ir_ItemIndex185: "ir_ArgOrVarRef" = None):
        self.name = name
        self.itemName = itemName
        self.ir_ItemIndex = ir_ItemIndex
        self.ir_ItemIndex140 = ir_ItemIndex140
        self.ir_ItemIndex185 = ir_ItemIndex185
        
    @property
    def itemName(self) -> str:
        return self.__itemName

    @itemName.setter
    def itemName(self, itemName: str):
        self.__itemName = itemName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_ItemIndex185(self):
        return self.__ir_ItemIndex185

    @ir_ItemIndex185.setter
    def ir_ItemIndex185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ItemIndex__ir_ItemIndex185", None)
        self.__ir_ItemIndex185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ArgOrVarRef184"):
                opp_val = getattr(old_value, "ir_ArgOrVarRef184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ArgOrVarRef184"):
                opp_val = getattr(value, "ir_ArgOrVarRef184", None)
                if opp_val is None:
                    setattr(value, "ir_ArgOrVarRef184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_ItemIndex140(self):
        return self.__ir_ItemIndex140

    @ir_ItemIndex140.setter
    def ir_ItemIndex140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ItemIndex__ir_ItemIndex140", None)
        self.__ir_ItemIndex140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Iterator"):
                opp_val = getattr(old_value, "ir_Iterator", None)
                if opp_val == self:
                    setattr(old_value, "ir_Iterator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Iterator"):
                opp_val = getattr(value, "ir_Iterator", None)
                setattr(value, "ir_Iterator", self)

    @property
    def ir_ItemIndex(self):
        return self.__ir_ItemIndex

    @ir_ItemIndex.setter
    def ir_ItemIndex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_ItemIndex__ir_ItemIndex", None)
        self.__ir_ItemIndex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ItemIndexDefinition"):
                opp_val = getattr(old_value, "ir_ItemIndexDefinition", None)
                if opp_val == self:
                    setattr(old_value, "ir_ItemIndexDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ItemIndexDefinition"):
                opp_val = getattr(value, "ir_ItemIndexDefinition", None)
                setattr(value, "ir_ItemIndexDefinition", self)

class ir_Container(IrAnnotable):

    pass
class ir_ItemIndexValue(IrAnnotable):

    pass
class ir_TimeLoopCopy(IrAnnotable):

    pass
class ir_Function(IrAnnotable):

    def __init__(self, provider: str, name: str, ir_Function: "ir_IrModule" = None, ir_Function67: "ir_BaseType" = None, ir_Function70: set["ir_SimpleVariable"] = None, ir_Function73: set["ir_Arg"] = None, ir_Function76: "ir_Instruction" = None, ir_Function113: "ir_ReductionInstruction" = None, ir_Function171: "ir_FunctionCall" = None):
        self.provider = provider
        self.name = name
        self.ir_Function = ir_Function
        self.ir_Function67 = ir_Function67
        self.ir_Function70 = ir_Function70 if ir_Function70 is not None else set()
        self.ir_Function73 = ir_Function73 if ir_Function73 is not None else set()
        self.ir_Function76 = ir_Function76
        self.ir_Function113 = ir_Function113
        self.ir_Function171 = ir_Function171
        
    @property
    def provider(self) -> str:
        return self.__provider

    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ir_Function113(self):
        return self.__ir_Function113

    @ir_Function113.setter
    def ir_Function113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Function__ir_Function113", None)
        self.__ir_Function113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_ReductionInstruction112"):
                opp_val = getattr(old_value, "ir_ReductionInstruction112", None)
                if opp_val == self:
                    setattr(old_value, "ir_ReductionInstruction112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_ReductionInstruction112"):
                opp_val = getattr(value, "ir_ReductionInstruction112", None)
                setattr(value, "ir_ReductionInstruction112", self)

    @property
    def ir_Function(self):
        return self.__ir_Function

    @ir_Function.setter
    def ir_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Function__ir_Function", None)
        self.__ir_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_IrModule8"):
                opp_val = getattr(old_value, "ir_IrModule8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_IrModule8"):
                opp_val = getattr(value, "ir_IrModule8", None)
                if opp_val is None:
                    setattr(value, "ir_IrModule8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_Function70(self):
        return self.__ir_Function70

    @ir_Function70.setter
    def ir_Function70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Function__ir_Function70", None)
        self.__ir_Function70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_SimpleVariable71"):
                    opp_val = getattr(item, "ir_SimpleVariable71", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_SimpleVariable71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_SimpleVariable71"):
                    opp_val = getattr(item, "ir_SimpleVariable71", None)
                    
                    setattr(item, "ir_SimpleVariable71", self)
                    

    @property
    def ir_Function73(self):
        return self.__ir_Function73

    @ir_Function73.setter
    def ir_Function73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Function__ir_Function73", None)
        self.__ir_Function73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_Arg74"):
                    opp_val = getattr(item, "ir_Arg74", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_Arg74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_Arg74"):
                    opp_val = getattr(item, "ir_Arg74", None)
                    
                    setattr(item, "ir_Arg74", self)
                    

    @property
    def ir_Function76(self):
        return self.__ir_Function76

    @ir_Function76.setter
    def ir_Function76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Function__ir_Function76", None)
        self.__ir_Function76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Instruction"):
                opp_val = getattr(old_value, "ir_Instruction", None)
                if opp_val == self:
                    setattr(old_value, "ir_Instruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Instruction"):
                opp_val = getattr(value, "ir_Instruction", None)
                setattr(value, "ir_Instruction", self)

    @property
    def ir_Function67(self):
        return self.__ir_Function67

    @ir_Function67.setter
    def ir_Function67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Function__ir_Function67", None)
        self.__ir_Function67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_BaseType68"):
                opp_val = getattr(old_value, "ir_BaseType68", None)
                if opp_val == self:
                    setattr(old_value, "ir_BaseType68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_BaseType68"):
                opp_val = getattr(value, "ir_BaseType68", None)
                setattr(value, "ir_BaseType68", self)

    @property
    def ir_Function171(self):
        return self.__ir_Function171

    @ir_Function171.setter
    def ir_Function171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_Function__ir_Function171", None)
        self.__ir_Function171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_FunctionCall"):
                opp_val = getattr(old_value, "ir_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "ir_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_FunctionCall"):
                opp_val = getattr(value, "ir_FunctionCall", None)
                setattr(value, "ir_FunctionCall", self)

class ir_Expression(IrAnnotable):

    pass
class ir_Instruction(IrAnnotable):

    pass
class ir_TimeLoop(IrAnnotable):

    def __init__(self, name: str, ir_TimeLoop: "ir_IrModule" = None, TimeLoop: "ir_TimeLoop" = None, outerTimeLoop: "ir_TimeLoop" = None, TimeLoop45: "ir_TimeLoop" = None, innerTimeLoop: "ir_TimeLoop" = None, ir_TimeLoop47: set["ir_TimeLoopVariable"] = None, ir_TimeLoop49: "ir_Expression" = None, ir_TimeLoop51: "ir_TimeLoopJob" = None, ir_TimeLoop53: "ir_SimpleVariable" = None, ir_TimeLoop89: "ir_TimeLoopCopyJob" = None):
        self.name = name
        self.ir_TimeLoop = ir_TimeLoop
        self.TimeLoop = TimeLoop
        self.outerTimeLoop = outerTimeLoop
        self.TimeLoop45 = TimeLoop45
        self.innerTimeLoop = innerTimeLoop
        self.ir_TimeLoop47 = ir_TimeLoop47 if ir_TimeLoop47 is not None else set()
        self.ir_TimeLoop49 = ir_TimeLoop49
        self.ir_TimeLoop51 = ir_TimeLoop51
        self.ir_TimeLoop53 = ir_TimeLoop53
        self.ir_TimeLoop89 = ir_TimeLoop89
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TimeLoop(self):
        return self.__TimeLoop

    @TimeLoop.setter
    def TimeLoop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoop__TimeLoop", None)
        self.__TimeLoop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outerTimeLoop"):
                opp_val = getattr(old_value, "outerTimeLoop", None)
                if opp_val == self:
                    setattr(old_value, "outerTimeLoop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outerTimeLoop"):
                opp_val = getattr(value, "outerTimeLoop", None)
                setattr(value, "outerTimeLoop", self)

    @property
    def ir_TimeLoop53(self):
        return self.__ir_TimeLoop53

    @ir_TimeLoop53.setter
    def ir_TimeLoop53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoop__ir_TimeLoop53", None)
        self.__ir_TimeLoop53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_SimpleVariable54"):
                opp_val = getattr(old_value, "ir_SimpleVariable54", None)
                if opp_val == self:
                    setattr(old_value, "ir_SimpleVariable54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_SimpleVariable54"):
                opp_val = getattr(value, "ir_SimpleVariable54", None)
                setattr(value, "ir_SimpleVariable54", self)

    @property
    def innerTimeLoop(self):
        return self.__innerTimeLoop

    @innerTimeLoop.setter
    def innerTimeLoop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoop__innerTimeLoop", None)
        self.__innerTimeLoop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TimeLoop45"):
                opp_val = getattr(old_value, "TimeLoop45", None)
                if opp_val == self:
                    setattr(old_value, "TimeLoop45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TimeLoop45"):
                opp_val = getattr(value, "TimeLoop45", None)
                setattr(value, "TimeLoop45", self)

    @property
    def ir_TimeLoop49(self):
        return self.__ir_TimeLoop49

    @ir_TimeLoop49.setter
    def ir_TimeLoop49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoop__ir_TimeLoop49", None)
        self.__ir_TimeLoop49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_Expression"):
                opp_val = getattr(old_value, "ir_Expression", None)
                if opp_val == self:
                    setattr(old_value, "ir_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_Expression"):
                opp_val = getattr(value, "ir_Expression", None)
                setattr(value, "ir_Expression", self)

    @property
    def ir_TimeLoop89(self):
        return self.__ir_TimeLoop89

    @ir_TimeLoop89.setter
    def ir_TimeLoop89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoop__ir_TimeLoop89", None)
        self.__ir_TimeLoop89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TimeLoopCopyJob88"):
                opp_val = getattr(old_value, "ir_TimeLoopCopyJob88", None)
                if opp_val == self:
                    setattr(old_value, "ir_TimeLoopCopyJob88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TimeLoopCopyJob88"):
                opp_val = getattr(value, "ir_TimeLoopCopyJob88", None)
                setattr(value, "ir_TimeLoopCopyJob88", self)

    @property
    def ir_TimeLoop47(self):
        return self.__ir_TimeLoop47

    @ir_TimeLoop47.setter
    def ir_TimeLoop47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoop__ir_TimeLoop47", None)
        self.__ir_TimeLoop47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_TimeLoopVariable"):
                    opp_val = getattr(item, "ir_TimeLoopVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_TimeLoopVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_TimeLoopVariable"):
                    opp_val = getattr(item, "ir_TimeLoopVariable", None)
                    
                    setattr(item, "ir_TimeLoopVariable", self)
                    

    @property
    def ir_TimeLoop(self):
        return self.__ir_TimeLoop

    @ir_TimeLoop.setter
    def ir_TimeLoop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoop__ir_TimeLoop", None)
        self.__ir_TimeLoop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_IrModule29"):
                opp_val = getattr(old_value, "ir_IrModule29", None)
                if opp_val == self:
                    setattr(old_value, "ir_IrModule29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_IrModule29"):
                opp_val = getattr(value, "ir_IrModule29", None)
                setattr(value, "ir_IrModule29", self)

    @property
    def TimeLoop45(self):
        return self.__TimeLoop45

    @TimeLoop45.setter
    def TimeLoop45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoop__TimeLoop45", None)
        self.__TimeLoop45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "innerTimeLoop"):
                opp_val = getattr(old_value, "innerTimeLoop", None)
                if opp_val == self:
                    setattr(old_value, "innerTimeLoop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "innerTimeLoop"):
                opp_val = getattr(value, "innerTimeLoop", None)
                setattr(value, "innerTimeLoop", self)

    @property
    def outerTimeLoop(self):
        return self.__outerTimeLoop

    @outerTimeLoop.setter
    def outerTimeLoop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoop__outerTimeLoop", None)
        self.__outerTimeLoop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TimeLoop"):
                opp_val = getattr(old_value, "TimeLoop", None)
                if opp_val == self:
                    setattr(old_value, "TimeLoop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TimeLoop"):
                opp_val = getattr(value, "TimeLoop", None)
                setattr(value, "TimeLoop", self)

    @property
    def ir_TimeLoop51(self):
        return self.__ir_TimeLoop51

    @ir_TimeLoop51.setter
    def ir_TimeLoop51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_TimeLoop__ir_TimeLoop51", None)
        self.__ir_TimeLoop51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_TimeLoopJob"):
                opp_val = getattr(old_value, "ir_TimeLoopJob", None)
                if opp_val == self:
                    setattr(old_value, "ir_TimeLoopJob", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_TimeLoopJob"):
                opp_val = getattr(value, "ir_TimeLoopJob", None)
                setattr(value, "ir_TimeLoopJob", self)

class ir_IrType(IrAnnotable):

    pass
class ir_JobContainer(IrAnnotable):

    pass
class ir_EStringToStringMapEntry:

    pass
class ir_IrAnnotation:

    def __init__(self, source: str, ir_IrAnnotation: "ir_IrAnnotable" = None, ir_IrAnnotation2: set["ir_EStringToStringMapEntry"] = None):
        self.source = source
        self.ir_IrAnnotation = ir_IrAnnotation
        self.ir_IrAnnotation2 = ir_IrAnnotation2 if ir_IrAnnotation2 is not None else set()
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def ir_IrAnnotation(self):
        return self.__ir_IrAnnotation

    @ir_IrAnnotation.setter
    def ir_IrAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrAnnotation__ir_IrAnnotation", None)
        self.__ir_IrAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ir_IrAnnotable"):
                opp_val = getattr(old_value, "ir_IrAnnotable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ir_IrAnnotable"):
                opp_val = getattr(value, "ir_IrAnnotable", None)
                if opp_val is None:
                    setattr(value, "ir_IrAnnotable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ir_IrAnnotation2(self):
        return self.__ir_IrAnnotation2

    @ir_IrAnnotation2.setter
    def ir_IrAnnotation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ir_IrAnnotation__ir_IrAnnotation2", None)
        self.__ir_IrAnnotation2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ir_EStringToStringMapEntry"):
                    opp_val = getattr(item, "ir_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "ir_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ir_EStringToStringMapEntry"):
                    opp_val = getattr(item, "ir_EStringToStringMapEntry", None)
                    
                    setattr(item, "ir_EStringToStringMapEntry", self)
                    

class ir_IrAnnotable(ABC):

    pass