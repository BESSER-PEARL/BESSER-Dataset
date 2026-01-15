from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ComparsionOperator:

    pass
class behaviouralProgramMM_Equals(ComparsionOperator):

    pass
class FunctionCallStatement:

    pass
class behaviouralProgramMM_WriteLineStatement(FunctionCallStatement):

    pass
class behaviouralProgramMM_ReadLineStatement(FunctionCallStatement):

    pass
class ArithmeticInfixOperator:

    pass
class behaviouralProgramMM_Plus(ArithmeticInfixOperator):

    pass
class BinaryOperator:

    pass
class behaviouralProgramMM_ComparsionOperator(BinaryOperator):

    pass
class behaviouralProgramMM_ArithmeticInfixOperator(BinaryOperator):

    pass
class behaviouralProgramMM_Expression(ABC):

    pass
class Statement:

    pass
class behaviouralProgramMM_FunctionCallStatement(Statement):

    def __init__(self, FuncName: str, behaviouralProgramMM_FunctionCallStatement: set["behaviouralProgramMM_Expression"] = None):
        self.FuncName = FuncName
        self.behaviouralProgramMM_FunctionCallStatement = behaviouralProgramMM_FunctionCallStatement if behaviouralProgramMM_FunctionCallStatement is not None else set()
        
    @property
    def FuncName(self) -> str:
        return self.__FuncName

    @FuncName.setter
    def FuncName(self, FuncName: str):
        self.__FuncName = FuncName

    @property
    def behaviouralProgramMM_FunctionCallStatement(self):
        return self.__behaviouralProgramMM_FunctionCallStatement

    @behaviouralProgramMM_FunctionCallStatement.setter
    def behaviouralProgramMM_FunctionCallStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviouralProgramMM_FunctionCallStatement__behaviouralProgramMM_FunctionCallStatement", None)
        self.__behaviouralProgramMM_FunctionCallStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviouralProgramMM_Expression34"):
                    opp_val = getattr(item, "behaviouralProgramMM_Expression34", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviouralProgramMM_Expression34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviouralProgramMM_Expression34"):
                    opp_val = getattr(item, "behaviouralProgramMM_Expression34", None)
                    
                    setattr(item, "behaviouralProgramMM_Expression34", self)
                    

class behaviouralProgramMM_ConditionalBranch(Statement):

    pass
class behaviouralProgramMM_Loop(Statement):

    pass
class behaviouralProgramMM_Return(Statement):

    pass
class behaviouralProgramMM_TryCatch(Statement):

    pass
class behaviouralProgramMM_RaiseException(Statement):

    pass
class behaviouralProgramMM_Assignment(Statement):

    def __init__(self, VariableName: str, behaviouralProgramMM_Assignment: "behaviouralProgramMM_Expression" = None):
        self.VariableName = VariableName
        self.behaviouralProgramMM_Assignment = behaviouralProgramMM_Assignment
        
    @property
    def VariableName(self) -> str:
        return self.__VariableName

    @VariableName.setter
    def VariableName(self, VariableName: str):
        self.__VariableName = VariableName

    @property
    def behaviouralProgramMM_Assignment(self):
        return self.__behaviouralProgramMM_Assignment

    @behaviouralProgramMM_Assignment.setter
    def behaviouralProgramMM_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviouralProgramMM_Assignment__behaviouralProgramMM_Assignment", None)
        self.__behaviouralProgramMM_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviouralProgramMM_Expression"):
                opp_val = getattr(old_value, "behaviouralProgramMM_Expression", None)
                if opp_val == self:
                    setattr(old_value, "behaviouralProgramMM_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviouralProgramMM_Expression"):
                opp_val = getattr(value, "behaviouralProgramMM_Expression", None)
                setattr(value, "behaviouralProgramMM_Expression", self)

class behaviouralProgramMM_Statement(ABC):

    pass
class behaviouralProgramMM_Function:

    def __init__(self, Name: str, behaviouralProgramMM_Function: "behaviouralProgramMM_Behaviour" = None, behaviouralProgramMM_Function3: "behaviouralProgramMM_Behaviour" = None, behaviouralProgramMM_Function5: set["behaviouralProgramMM_Statement"] = None):
        self.Name = Name
        self.behaviouralProgramMM_Function = behaviouralProgramMM_Function
        self.behaviouralProgramMM_Function3 = behaviouralProgramMM_Function3
        self.behaviouralProgramMM_Function5 = behaviouralProgramMM_Function5 if behaviouralProgramMM_Function5 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def behaviouralProgramMM_Function(self):
        return self.__behaviouralProgramMM_Function

    @behaviouralProgramMM_Function.setter
    def behaviouralProgramMM_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviouralProgramMM_Function__behaviouralProgramMM_Function", None)
        self.__behaviouralProgramMM_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviouralProgramMM_Behaviour"):
                opp_val = getattr(old_value, "behaviouralProgramMM_Behaviour", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviouralProgramMM_Behaviour"):
                opp_val = getattr(value, "behaviouralProgramMM_Behaviour", None)
                if opp_val is None:
                    setattr(value, "behaviouralProgramMM_Behaviour", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviouralProgramMM_Function5(self):
        return self.__behaviouralProgramMM_Function5

    @behaviouralProgramMM_Function5.setter
    def behaviouralProgramMM_Function5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviouralProgramMM_Function__behaviouralProgramMM_Function5", None)
        self.__behaviouralProgramMM_Function5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviouralProgramMM_Statement"):
                    opp_val = getattr(item, "behaviouralProgramMM_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviouralProgramMM_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviouralProgramMM_Statement"):
                    opp_val = getattr(item, "behaviouralProgramMM_Statement", None)
                    
                    setattr(item, "behaviouralProgramMM_Statement", self)
                    

    @property
    def behaviouralProgramMM_Function3(self):
        return self.__behaviouralProgramMM_Function3

    @behaviouralProgramMM_Function3.setter
    def behaviouralProgramMM_Function3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviouralProgramMM_Function__behaviouralProgramMM_Function3", None)
        self.__behaviouralProgramMM_Function3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviouralProgramMM_Behaviour2"):
                opp_val = getattr(old_value, "behaviouralProgramMM_Behaviour2", None)
                if opp_val == self:
                    setattr(old_value, "behaviouralProgramMM_Behaviour2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviouralProgramMM_Behaviour2"):
                opp_val = getattr(value, "behaviouralProgramMM_Behaviour2", None)
                setattr(value, "behaviouralProgramMM_Behaviour2", self)

class behaviouralProgramMM_Behaviour:

    pass
class behaviouralProgramMM_Instantiation(Statement):

    def __init__(self, VarName: str, VarType: str, behaviouralProgramMM_Instantiation: "behaviouralProgramMM_Expression" = None):
        self.VarName = VarName
        self.VarType = VarType
        self.behaviouralProgramMM_Instantiation = behaviouralProgramMM_Instantiation
        
    @property
    def VarType(self) -> str:
        return self.__VarType

    @VarType.setter
    def VarType(self, VarType: str):
        self.__VarType = VarType

    @property
    def VarName(self) -> str:
        return self.__VarName

    @VarName.setter
    def VarName(self, VarName: str):
        self.__VarName = VarName

    @property
    def behaviouralProgramMM_Instantiation(self):
        return self.__behaviouralProgramMM_Instantiation

    @behaviouralProgramMM_Instantiation.setter
    def behaviouralProgramMM_Instantiation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviouralProgramMM_Instantiation__behaviouralProgramMM_Instantiation", None)
        self.__behaviouralProgramMM_Instantiation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviouralProgramMM_Expression23"):
                opp_val = getattr(old_value, "behaviouralProgramMM_Expression23", None)
                if opp_val == self:
                    setattr(old_value, "behaviouralProgramMM_Expression23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviouralProgramMM_Expression23"):
                opp_val = getattr(value, "behaviouralProgramMM_Expression23", None)
                setattr(value, "behaviouralProgramMM_Expression23", self)

class Expression:

    pass
class behaviouralProgramMM_BinaryOperator(Expression):

    pass
class behaviouralProgramMM_Literal(Expression):

    def __init__(self, Value: str):
        self.Value = Value
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

class behaviouralProgramMM_Variable(Expression):

    def __init__(self, VarName: str):
        self.VarName = VarName
        
    @property
    def VarName(self) -> str:
        return self.__VarName

    @VarName.setter
    def VarName(self, VarName: str):
        self.__VarName = VarName

class behaviouralProgramMM_ReadLine(Expression):

    pass
class behaviouralProgramMM_FunctionCall(Expression):

    def __init__(self, FuncName: str, behaviouralProgramMM_FunctionCall: set["behaviouralProgramMM_Expression"] = None):
        self.FuncName = FuncName
        self.behaviouralProgramMM_FunctionCall = behaviouralProgramMM_FunctionCall if behaviouralProgramMM_FunctionCall is not None else set()
        
    @property
    def FuncName(self) -> str:
        return self.__FuncName

    @FuncName.setter
    def FuncName(self, FuncName: str):
        self.__FuncName = FuncName

    @property
    def behaviouralProgramMM_FunctionCall(self):
        return self.__behaviouralProgramMM_FunctionCall

    @behaviouralProgramMM_FunctionCall.setter
    def behaviouralProgramMM_FunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviouralProgramMM_FunctionCall__behaviouralProgramMM_FunctionCall", None)
        self.__behaviouralProgramMM_FunctionCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviouralProgramMM_Expression21"):
                    opp_val = getattr(item, "behaviouralProgramMM_Expression21", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviouralProgramMM_Expression21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviouralProgramMM_Expression21"):
                    opp_val = getattr(item, "behaviouralProgramMM_Expression21", None)
                    
                    setattr(item, "behaviouralProgramMM_Expression21", self)
                    
