from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lua_Field:

    pass
class Expression:

    pass
class lua_Expression_Smaller_Equal(Expression):

    pass
class lua_Expression_Larger(Expression):

    pass
class lua_Expression_Division(Expression):

    pass
class lua_Expression_Or(Expression):

    pass
class lua_Expression_CallFunction(Expression):

    pass
class lua_Expression_Multiplication(Expression):

    pass
class lua_Expression_Invert(Expression):

    pass
class lua_Expression_Concatenation(Expression):

    pass
class lua_Expression_Exponentiation(Expression):

    pass
class lua_Expression_VarArgs(Expression):

    pass
class lua_Expression_Smaller(Expression):

    pass
class lua_Expression_VariableName(Expression):

    def __init__(self, variable: str):
        self.variable = variable
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

class lua_Expression_Negate(Expression):

    pass
class lua_Expression_Not_Equal(Expression):

    pass
class lua_Expression_Equal(Expression):

    pass
class lua_Expression_Modulo(Expression):

    pass
class lua_Expression_And(Expression):

    pass
class lua_Expression_AccessArray(Expression):

    pass
class lua_Expression_True(Expression):

    pass
class lua_Expression_AccessMember(Expression):

    def __init__(self, memberName: str, lua_Expression_AccessMember: "lua_Expression" = None):
        self.memberName = memberName
        self.lua_Expression_AccessMember = lua_Expression_AccessMember
        
    @property
    def memberName(self) -> str:
        return self.__memberName

    @memberName.setter
    def memberName(self, memberName: str):
        self.__memberName = memberName

    @property
    def lua_Expression_AccessMember(self):
        return self.__lua_Expression_AccessMember

    @lua_Expression_AccessMember.setter
    def lua_Expression_AccessMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_AccessMember__lua_Expression_AccessMember", None)
        self.__lua_Expression_AccessMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression178"):
                opp_val = getattr(old_value, "lua_Expression178", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression178"):
                opp_val = getattr(value, "lua_Expression178", None)
                setattr(value, "lua_Expression178", self)

class lua_Expression_String(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class lua_Expression_Function(Expression):

    pass
class lua_Expression_Larger_Equal(Expression):

    pass
class lua_Expression_Number(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class lua_Expression_Minus(Expression):

    pass
class lua_Expression_Plus(Expression):

    pass
class lua_Expression_CallMemberFunction(Expression):

    def __init__(self, memberFunctionName: str, lua_Expression_CallMemberFunction: "lua_Expression" = None, lua_Expression_CallMemberFunction165: "lua_Functioncall_Arguments" = None):
        self.memberFunctionName = memberFunctionName
        self.lua_Expression_CallMemberFunction = lua_Expression_CallMemberFunction
        self.lua_Expression_CallMemberFunction165 = lua_Expression_CallMemberFunction165
        
    @property
    def memberFunctionName(self) -> str:
        return self.__memberFunctionName

    @memberFunctionName.setter
    def memberFunctionName(self, memberFunctionName: str):
        self.__memberFunctionName = memberFunctionName

    @property
    def lua_Expression_CallMemberFunction165(self):
        return self.__lua_Expression_CallMemberFunction165

    @lua_Expression_CallMemberFunction165.setter
    def lua_Expression_CallMemberFunction165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_CallMemberFunction__lua_Expression_CallMemberFunction165", None)
        self.__lua_Expression_CallMemberFunction165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Functioncall_Arguments166"):
                opp_val = getattr(old_value, "lua_Functioncall_Arguments166", None)
                if opp_val == self:
                    setattr(old_value, "lua_Functioncall_Arguments166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Functioncall_Arguments166"):
                opp_val = getattr(value, "lua_Functioncall_Arguments166", None)
                setattr(value, "lua_Functioncall_Arguments166", self)

    @property
    def lua_Expression_CallMemberFunction(self):
        return self.__lua_Expression_CallMemberFunction

    @lua_Expression_CallMemberFunction.setter
    def lua_Expression_CallMemberFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_CallMemberFunction__lua_Expression_CallMemberFunction", None)
        self.__lua_Expression_CallMemberFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression163"):
                opp_val = getattr(old_value, "lua_Expression163", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression163"):
                opp_val = getattr(value, "lua_Expression163", None)
                setattr(value, "lua_Expression163", self)

class lua_Expression_Length(Expression):

    pass
class lua_Expression_TableConstructor(Expression):

    pass
class lua_Expression_False(Expression):

    pass
class lua_Expression_Nil(Expression):

    pass
class Statement_FunctioncallOrAssignment:

    pass
class lua_Statement_CallMemberFunction(Statement_FunctioncallOrAssignment):

    def __init__(self, memberFunctionName: str, lua_Statement_CallMemberFunction: "lua_Expression" = None, lua_Statement_CallMemberFunction74: "lua_Functioncall_Arguments" = None):
        self.memberFunctionName = memberFunctionName
        self.lua_Statement_CallMemberFunction = lua_Statement_CallMemberFunction
        self.lua_Statement_CallMemberFunction74 = lua_Statement_CallMemberFunction74
        
    @property
    def memberFunctionName(self) -> str:
        return self.__memberFunctionName

    @memberFunctionName.setter
    def memberFunctionName(self, memberFunctionName: str):
        self.__memberFunctionName = memberFunctionName

    @property
    def lua_Statement_CallMemberFunction74(self):
        return self.__lua_Statement_CallMemberFunction74

    @lua_Statement_CallMemberFunction74.setter
    def lua_Statement_CallMemberFunction74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_CallMemberFunction__lua_Statement_CallMemberFunction74", None)
        self.__lua_Statement_CallMemberFunction74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Functioncall_Arguments75"):
                opp_val = getattr(old_value, "lua_Functioncall_Arguments75", None)
                if opp_val == self:
                    setattr(old_value, "lua_Functioncall_Arguments75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Functioncall_Arguments75"):
                opp_val = getattr(value, "lua_Functioncall_Arguments75", None)
                setattr(value, "lua_Functioncall_Arguments75", self)

    @property
    def lua_Statement_CallMemberFunction(self):
        return self.__lua_Statement_CallMemberFunction

    @lua_Statement_CallMemberFunction.setter
    def lua_Statement_CallMemberFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_CallMemberFunction__lua_Statement_CallMemberFunction", None)
        self.__lua_Statement_CallMemberFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression72"):
                opp_val = getattr(old_value, "lua_Expression72", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression72"):
                opp_val = getattr(value, "lua_Expression72", None)
                setattr(value, "lua_Expression72", self)

class lua_Statement_CallFunction(Statement_FunctioncallOrAssignment):

    pass
class lua_Statement_Assignment(Statement_FunctioncallOrAssignment):

    pass
class LastStatement_Return:

    pass
class lua_LastStatement_ReturnWithValue(LastStatement_Return):

    pass
class Field:

    pass
class lua_Field_AddEntryToTable(Field):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class lua_Field_AppendEntryToTable(Field):

    pass
class lua_Field_AddEntryToTable_Brackets(Field):

    pass
class lua_Functioncall_Arguments:

    pass
class lua_Statement_If_Then_Else_ElseIfPart:

    pass
class lua_Function:

    def __init__(self, parameters: str, varArgs: bool, lua_Function: "lua_Statement_GlobalFunction_Declaration" = None, lua_Function48: "lua_Statement_LocalFunction_Declaration" = None, lua_Function52: "lua_Expression_Function" = None, lua_Function55: "lua_Block" = None):
        self.parameters = parameters
        self.varArgs = varArgs
        self.lua_Function = lua_Function
        self.lua_Function48 = lua_Function48
        self.lua_Function52 = lua_Function52
        self.lua_Function55 = lua_Function55
        
    @property
    def varArgs(self) -> bool:
        return self.__varArgs

    @varArgs.setter
    def varArgs(self, varArgs: bool):
        self.__varArgs = varArgs

    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def lua_Function48(self):
        return self.__lua_Function48

    @lua_Function48.setter
    def lua_Function48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Function__lua_Function48", None)
        self.__lua_Function48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_LocalFunction_Declaration"):
                opp_val = getattr(old_value, "lua_Statement_LocalFunction_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_LocalFunction_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_LocalFunction_Declaration"):
                opp_val = getattr(value, "lua_Statement_LocalFunction_Declaration", None)
                setattr(value, "lua_Statement_LocalFunction_Declaration", self)

    @property
    def lua_Function55(self):
        return self.__lua_Function55

    @lua_Function55.setter
    def lua_Function55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Function__lua_Function55", None)
        self.__lua_Function55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Block56"):
                opp_val = getattr(old_value, "lua_Block56", None)
                if opp_val == self:
                    setattr(old_value, "lua_Block56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Block56"):
                opp_val = getattr(value, "lua_Block56", None)
                setattr(value, "lua_Block56", self)

    @property
    def lua_Function52(self):
        return self.__lua_Function52

    @lua_Function52.setter
    def lua_Function52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Function__lua_Function52", None)
        self.__lua_Function52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Function"):
                opp_val = getattr(old_value, "lua_Expression_Function", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Function"):
                opp_val = getattr(value, "lua_Expression_Function", None)
                setattr(value, "lua_Expression_Function", self)

    @property
    def lua_Function(self):
        return self.__lua_Function

    @lua_Function.setter
    def lua_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Function__lua_Function", None)
        self.__lua_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_GlobalFunction_Declaration"):
                opp_val = getattr(old_value, "lua_Statement_GlobalFunction_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_GlobalFunction_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_GlobalFunction_Declaration"):
                opp_val = getattr(value, "lua_Statement_GlobalFunction_Declaration", None)
                setattr(value, "lua_Statement_GlobalFunction_Declaration", self)

class lua_LastStatement:

    pass
class lua_Statement:

    pass
class Chunk:

    pass
class lua_Block(Chunk):

    pass
class lua_Chunk:

    pass
class lua_Expression(Statement_FunctioncallOrAssignment):

    pass
class Statement:

    pass
class lua_Statement_While(Statement):

    pass
class lua_Statement_FunctioncallOrAssignment(Statement):

    pass
class lua_Statement_For_Numeric(Statement):

    def __init__(self, iteratorName: str, lua_Statement_For_Numeric: "lua_Expression" = None, lua_Statement_For_Numeric33: "lua_Expression" = None, lua_Statement_For_Numeric36: "lua_Expression" = None, lua_Statement_For_Numeric39: "lua_Block" = None):
        self.iteratorName = iteratorName
        self.lua_Statement_For_Numeric = lua_Statement_For_Numeric
        self.lua_Statement_For_Numeric33 = lua_Statement_For_Numeric33
        self.lua_Statement_For_Numeric36 = lua_Statement_For_Numeric36
        self.lua_Statement_For_Numeric39 = lua_Statement_For_Numeric39
        
    @property
    def iteratorName(self) -> str:
        return self.__iteratorName

    @iteratorName.setter
    def iteratorName(self, iteratorName: str):
        self.__iteratorName = iteratorName

    @property
    def lua_Statement_For_Numeric39(self):
        return self.__lua_Statement_For_Numeric39

    @lua_Statement_For_Numeric39.setter
    def lua_Statement_For_Numeric39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_For_Numeric__lua_Statement_For_Numeric39", None)
        self.__lua_Statement_For_Numeric39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Block40"):
                opp_val = getattr(old_value, "lua_Block40", None)
                if opp_val == self:
                    setattr(old_value, "lua_Block40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Block40"):
                opp_val = getattr(value, "lua_Block40", None)
                setattr(value, "lua_Block40", self)

    @property
    def lua_Statement_For_Numeric36(self):
        return self.__lua_Statement_For_Numeric36

    @lua_Statement_For_Numeric36.setter
    def lua_Statement_For_Numeric36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_For_Numeric__lua_Statement_For_Numeric36", None)
        self.__lua_Statement_For_Numeric36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression37"):
                opp_val = getattr(old_value, "lua_Expression37", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression37"):
                opp_val = getattr(value, "lua_Expression37", None)
                setattr(value, "lua_Expression37", self)

    @property
    def lua_Statement_For_Numeric(self):
        return self.__lua_Statement_For_Numeric

    @lua_Statement_For_Numeric.setter
    def lua_Statement_For_Numeric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_For_Numeric__lua_Statement_For_Numeric", None)
        self.__lua_Statement_For_Numeric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression31"):
                opp_val = getattr(old_value, "lua_Expression31", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression31"):
                opp_val = getattr(value, "lua_Expression31", None)
                setattr(value, "lua_Expression31", self)

    @property
    def lua_Statement_For_Numeric33(self):
        return self.__lua_Statement_For_Numeric33

    @lua_Statement_For_Numeric33.setter
    def lua_Statement_For_Numeric33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_For_Numeric__lua_Statement_For_Numeric33", None)
        self.__lua_Statement_For_Numeric33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression34"):
                opp_val = getattr(old_value, "lua_Expression34", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression34"):
                opp_val = getattr(value, "lua_Expression34", None)
                setattr(value, "lua_Expression34", self)

class lua_Statement_Repeat(Statement):

    pass
class lua_Statement_Local_Variable_Declaration(Statement):

    def __init__(self, variableNames: str, lua_Statement_Local_Variable_Declaration: set["lua_Expression"] = None):
        self.variableNames = variableNames
        self.lua_Statement_Local_Variable_Declaration = lua_Statement_Local_Variable_Declaration if lua_Statement_Local_Variable_Declaration is not None else set()
        
    @property
    def variableNames(self) -> str:
        return self.__variableNames

    @variableNames.setter
    def variableNames(self, variableNames: str):
        self.__variableNames = variableNames

    @property
    def lua_Statement_Local_Variable_Declaration(self):
        return self.__lua_Statement_Local_Variable_Declaration

    @lua_Statement_Local_Variable_Declaration.setter
    def lua_Statement_Local_Variable_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_Local_Variable_Declaration__lua_Statement_Local_Variable_Declaration", None)
        self.__lua_Statement_Local_Variable_Declaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lua_Expression50"):
                    opp_val = getattr(item, "lua_Expression50", None)
                    
                    if opp_val == self:
                        setattr(item, "lua_Expression50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lua_Expression50"):
                    opp_val = getattr(item, "lua_Expression50", None)
                    
                    setattr(item, "lua_Expression50", self)
                    

class lua_Statement_If_Then_Else(Statement):

    pass
class lua_Statement_GlobalFunction_Declaration(Statement):

    def __init__(self, prefix: str, functionName: str, lua_Statement_GlobalFunction_Declaration: "lua_Function" = None):
        self.prefix = prefix
        self.functionName = functionName
        self.lua_Statement_GlobalFunction_Declaration = lua_Statement_GlobalFunction_Declaration
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def lua_Statement_GlobalFunction_Declaration(self):
        return self.__lua_Statement_GlobalFunction_Declaration

    @lua_Statement_GlobalFunction_Declaration.setter
    def lua_Statement_GlobalFunction_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_GlobalFunction_Declaration__lua_Statement_GlobalFunction_Declaration", None)
        self.__lua_Statement_GlobalFunction_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Function"):
                opp_val = getattr(old_value, "lua_Function", None)
                if opp_val == self:
                    setattr(old_value, "lua_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Function"):
                opp_val = getattr(value, "lua_Function", None)
                setattr(value, "lua_Function", self)

class lua_Statement_For_Generic(Statement):

    def __init__(self, names: str, lua_Statement_For_Generic: set["lua_Expression"] = None, lua_Statement_For_Generic44: "lua_Block" = None):
        self.names = names
        self.lua_Statement_For_Generic = lua_Statement_For_Generic if lua_Statement_For_Generic is not None else set()
        self.lua_Statement_For_Generic44 = lua_Statement_For_Generic44
        
    @property
    def names(self) -> str:
        return self.__names

    @names.setter
    def names(self, names: str):
        self.__names = names

    @property
    def lua_Statement_For_Generic(self):
        return self.__lua_Statement_For_Generic

    @lua_Statement_For_Generic.setter
    def lua_Statement_For_Generic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_For_Generic__lua_Statement_For_Generic", None)
        self.__lua_Statement_For_Generic = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lua_Expression42"):
                    opp_val = getattr(item, "lua_Expression42", None)
                    
                    if opp_val == self:
                        setattr(item, "lua_Expression42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lua_Expression42"):
                    opp_val = getattr(item, "lua_Expression42", None)
                    
                    setattr(item, "lua_Expression42", self)
                    

    @property
    def lua_Statement_For_Generic44(self):
        return self.__lua_Statement_For_Generic44

    @lua_Statement_For_Generic44.setter
    def lua_Statement_For_Generic44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_For_Generic__lua_Statement_For_Generic44", None)
        self.__lua_Statement_For_Generic44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Block45"):
                opp_val = getattr(old_value, "lua_Block45", None)
                if opp_val == self:
                    setattr(old_value, "lua_Block45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Block45"):
                opp_val = getattr(value, "lua_Block45", None)
                setattr(value, "lua_Block45", self)

class lua_Statement_LocalFunction_Declaration(Statement):

    def __init__(self, functionName: str, lua_Statement_LocalFunction_Declaration: "lua_Function" = None):
        self.functionName = functionName
        self.lua_Statement_LocalFunction_Declaration = lua_Statement_LocalFunction_Declaration
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def lua_Statement_LocalFunction_Declaration(self):
        return self.__lua_Statement_LocalFunction_Declaration

    @lua_Statement_LocalFunction_Declaration.setter
    def lua_Statement_LocalFunction_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_LocalFunction_Declaration__lua_Statement_LocalFunction_Declaration", None)
        self.__lua_Statement_LocalFunction_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Function48"):
                opp_val = getattr(old_value, "lua_Function48", None)
                if opp_val == self:
                    setattr(old_value, "lua_Function48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Function48"):
                opp_val = getattr(value, "lua_Function48", None)
                setattr(value, "lua_Function48", self)

class lua_Statement_Block(Statement):

    pass
class LastStatement:

    pass
class lua_LastStatement_Break(LastStatement):

    pass
class lua_LastStatement_Return(LastStatement):

    pass