from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class LastStatement_Return:

    pass
class activityecorelua_LastStatement_ReturnWithValue(LastStatement_Return):

    pass
class Field:

    pass
class activityecorelua_Field_AddEntryToTable(Field):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class activityecorelua_Field_AppendEntryToTable(Field):

    pass
class activityecorelua_Field_AddEntryToTable_Brackets(Field):

    pass
class activityecorelua_Functioncall_Arguments:

    pass
class activityecorelua_Field:

    pass
class Expression:

    pass
class activityecorelua_Expression_Or(Expression):

    pass
class activityecorelua_Expression_CallMemberFunction(Expression):

    def __init__(self, memberFunctionName: str, activityecorelua_Expression_CallMemberFunction: "activityecorelua_Expression" = None, activityecorelua_Expression_CallMemberFunction306: "activityecorelua_Functioncall_Arguments" = None):
        self.memberFunctionName = memberFunctionName
        self.activityecorelua_Expression_CallMemberFunction = activityecorelua_Expression_CallMemberFunction
        self.activityecorelua_Expression_CallMemberFunction306 = activityecorelua_Expression_CallMemberFunction306
        
    @property
    def memberFunctionName(self) -> str:
        return self.__memberFunctionName

    @memberFunctionName.setter
    def memberFunctionName(self, memberFunctionName: str):
        self.__memberFunctionName = memberFunctionName

    @property
    def activityecorelua_Expression_CallMemberFunction306(self):
        return self.__activityecorelua_Expression_CallMemberFunction306

    @activityecorelua_Expression_CallMemberFunction306.setter
    def activityecorelua_Expression_CallMemberFunction306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Expression_CallMemberFunction__activityecorelua_Expression_CallMemberFunction306", None)
        self.__activityecorelua_Expression_CallMemberFunction306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Functioncall_Arguments307"):
                opp_val = getattr(old_value, "activityecorelua_Functioncall_Arguments307", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Functioncall_Arguments307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Functioncall_Arguments307"):
                opp_val = getattr(value, "activityecorelua_Functioncall_Arguments307", None)
                setattr(value, "activityecorelua_Functioncall_Arguments307", self)

    @property
    def activityecorelua_Expression_CallMemberFunction(self):
        return self.__activityecorelua_Expression_CallMemberFunction

    @activityecorelua_Expression_CallMemberFunction.setter
    def activityecorelua_Expression_CallMemberFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Expression_CallMemberFunction__activityecorelua_Expression_CallMemberFunction", None)
        self.__activityecorelua_Expression_CallMemberFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Expression304"):
                opp_val = getattr(old_value, "activityecorelua_Expression304", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Expression304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Expression304"):
                opp_val = getattr(value, "activityecorelua_Expression304", None)
                setattr(value, "activityecorelua_Expression304", self)

class activityecorelua_Expression_Concatenation(Expression):

    pass
class activityecorelua_Expression_Length(Expression):

    pass
class activityecorelua_Expression_Not_Equal(Expression):

    pass
class activityecorelua_Expression_Larger_Equal(Expression):

    pass
class activityecorelua_Expression_String(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class activityecorelua_Expression_Equal(Expression):

    pass
class activityecorelua_Expression_AccessMember(Expression):

    def __init__(self, memberName: str, activityecorelua_Expression_AccessMember: "activityecorelua_Expression" = None):
        self.memberName = memberName
        self.activityecorelua_Expression_AccessMember = activityecorelua_Expression_AccessMember
        
    @property
    def memberName(self) -> str:
        return self.__memberName

    @memberName.setter
    def memberName(self, memberName: str):
        self.__memberName = memberName

    @property
    def activityecorelua_Expression_AccessMember(self):
        return self.__activityecorelua_Expression_AccessMember

    @activityecorelua_Expression_AccessMember.setter
    def activityecorelua_Expression_AccessMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Expression_AccessMember__activityecorelua_Expression_AccessMember", None)
        self.__activityecorelua_Expression_AccessMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Expression319"):
                opp_val = getattr(old_value, "activityecorelua_Expression319", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Expression319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Expression319"):
                opp_val = getattr(value, "activityecorelua_Expression319", None)
                setattr(value, "activityecorelua_Expression319", self)

class activityecorelua_Expression_Smaller_Equal(Expression):

    pass
class activityecorelua_Expression_Smaller(Expression):

    pass
class activityecorelua_Expression_VarArgs(Expression):

    pass
class activityecorelua_Expression_Negate(Expression):

    pass
class activityecorelua_Expression_And(Expression):

    pass
class activityecorelua_Expression_Plus(Expression):

    pass
class activityecorelua_Expression_Invert(Expression):

    pass
class activityecorelua_Expression_AccessArray(Expression):

    pass
class activityecorelua_Expression_CallFunction(Expression):

    pass
class activityecorelua_Expression_Minus(Expression):

    pass
class activityecorelua_Expression_False(Expression):

    pass
class activityecorelua_Expression_Modulo(Expression):

    pass
class activityecorelua_Expression_Multiplication(Expression):

    pass
class activityecorelua_Expression_VariableName(Expression):

    def __init__(self, variable: str):
        self.variable = variable
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

class activityecorelua_Expression_Exponentiation(Expression):

    pass
class activityecorelua_Expression_Number(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class activityecorelua_Expression_Division(Expression):

    pass
class activityecorelua_Expression_Function(Expression):

    pass
class activityecorelua_Expression_True(Expression):

    pass
class activityecorelua_Expression_Larger(Expression):

    pass
class activityecorelua_Expression_TableConstructor(Expression):

    pass
class activityecorelua_Expression_Nil(Expression):

    pass
class Statement_FunctioncallOrAssignment:

    pass
class activityecorelua_Statement_CallMemberFunction(Statement_FunctioncallOrAssignment):

    def __init__(self, memberFunctionName: str, activityecorelua_Statement_CallMemberFunction: "activityecorelua_Expression" = None, activityecorelua_Statement_CallMemberFunction215: "activityecorelua_Functioncall_Arguments" = None):
        self.memberFunctionName = memberFunctionName
        self.activityecorelua_Statement_CallMemberFunction = activityecorelua_Statement_CallMemberFunction
        self.activityecorelua_Statement_CallMemberFunction215 = activityecorelua_Statement_CallMemberFunction215
        
    @property
    def memberFunctionName(self) -> str:
        return self.__memberFunctionName

    @memberFunctionName.setter
    def memberFunctionName(self, memberFunctionName: str):
        self.__memberFunctionName = memberFunctionName

    @property
    def activityecorelua_Statement_CallMemberFunction215(self):
        return self.__activityecorelua_Statement_CallMemberFunction215

    @activityecorelua_Statement_CallMemberFunction215.setter
    def activityecorelua_Statement_CallMemberFunction215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Statement_CallMemberFunction__activityecorelua_Statement_CallMemberFunction215", None)
        self.__activityecorelua_Statement_CallMemberFunction215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Functioncall_Arguments216"):
                opp_val = getattr(old_value, "activityecorelua_Functioncall_Arguments216", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Functioncall_Arguments216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Functioncall_Arguments216"):
                opp_val = getattr(value, "activityecorelua_Functioncall_Arguments216", None)
                setattr(value, "activityecorelua_Functioncall_Arguments216", self)

    @property
    def activityecorelua_Statement_CallMemberFunction(self):
        return self.__activityecorelua_Statement_CallMemberFunction

    @activityecorelua_Statement_CallMemberFunction.setter
    def activityecorelua_Statement_CallMemberFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Statement_CallMemberFunction__activityecorelua_Statement_CallMemberFunction", None)
        self.__activityecorelua_Statement_CallMemberFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Expression213"):
                opp_val = getattr(old_value, "activityecorelua_Expression213", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Expression213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Expression213"):
                opp_val = getattr(value, "activityecorelua_Expression213", None)
                setattr(value, "activityecorelua_Expression213", self)

class activityecorelua_Statement_CallFunction(Statement_FunctioncallOrAssignment):

    pass
class activityecorelua_Statement_Assignment(Statement_FunctioncallOrAssignment):

    pass
class activityecorelua_Function:

    def __init__(self, parameters: str, varArgs: bool, activityecorelua_Function: "activityecorelua_Statement_GlobalFunction_Declaration" = None, activityecorelua_Function189: "activityecorelua_Statement_LocalFunction_Declaration" = None, activityecorelua_Function193: "activityecorelua_Expression_Function" = None, activityecorelua_Function196: "activityecorelua_Block" = None):
        self.parameters = parameters
        self.varArgs = varArgs
        self.activityecorelua_Function = activityecorelua_Function
        self.activityecorelua_Function189 = activityecorelua_Function189
        self.activityecorelua_Function193 = activityecorelua_Function193
        self.activityecorelua_Function196 = activityecorelua_Function196
        
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
    def activityecorelua_Function196(self):
        return self.__activityecorelua_Function196

    @activityecorelua_Function196.setter
    def activityecorelua_Function196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Function__activityecorelua_Function196", None)
        self.__activityecorelua_Function196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Block197"):
                opp_val = getattr(old_value, "activityecorelua_Block197", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Block197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Block197"):
                opp_val = getattr(value, "activityecorelua_Block197", None)
                setattr(value, "activityecorelua_Block197", self)

    @property
    def activityecorelua_Function189(self):
        return self.__activityecorelua_Function189

    @activityecorelua_Function189.setter
    def activityecorelua_Function189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Function__activityecorelua_Function189", None)
        self.__activityecorelua_Function189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Statement_LocalFunction_Declaration"):
                opp_val = getattr(old_value, "activityecorelua_Statement_LocalFunction_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Statement_LocalFunction_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Statement_LocalFunction_Declaration"):
                opp_val = getattr(value, "activityecorelua_Statement_LocalFunction_Declaration", None)
                setattr(value, "activityecorelua_Statement_LocalFunction_Declaration", self)

    @property
    def activityecorelua_Function(self):
        return self.__activityecorelua_Function

    @activityecorelua_Function.setter
    def activityecorelua_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Function__activityecorelua_Function", None)
        self.__activityecorelua_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Statement_GlobalFunction_Declaration"):
                opp_val = getattr(old_value, "activityecorelua_Statement_GlobalFunction_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Statement_GlobalFunction_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Statement_GlobalFunction_Declaration"):
                opp_val = getattr(value, "activityecorelua_Statement_GlobalFunction_Declaration", None)
                setattr(value, "activityecorelua_Statement_GlobalFunction_Declaration", self)

    @property
    def activityecorelua_Function193(self):
        return self.__activityecorelua_Function193

    @activityecorelua_Function193.setter
    def activityecorelua_Function193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Function__activityecorelua_Function193", None)
        self.__activityecorelua_Function193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Expression_Function"):
                opp_val = getattr(old_value, "activityecorelua_Expression_Function", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Expression_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Expression_Function"):
                opp_val = getattr(value, "activityecorelua_Expression_Function", None)
                setattr(value, "activityecorelua_Expression_Function", self)

class activityecorelua_Statement_If_Then_Else_ElseIfPart:

    pass
class Statement:

    pass
class activityecorelua_Statement_LocalFunction_Declaration(Statement):

    def __init__(self, functionName: str, activityecorelua_Statement_LocalFunction_Declaration: "activityecorelua_Function" = None):
        self.functionName = functionName
        self.activityecorelua_Statement_LocalFunction_Declaration = activityecorelua_Statement_LocalFunction_Declaration
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def activityecorelua_Statement_LocalFunction_Declaration(self):
        return self.__activityecorelua_Statement_LocalFunction_Declaration

    @activityecorelua_Statement_LocalFunction_Declaration.setter
    def activityecorelua_Statement_LocalFunction_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Statement_LocalFunction_Declaration__activityecorelua_Statement_LocalFunction_Declaration", None)
        self.__activityecorelua_Statement_LocalFunction_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Function189"):
                opp_val = getattr(old_value, "activityecorelua_Function189", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Function189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Function189"):
                opp_val = getattr(value, "activityecorelua_Function189", None)
                setattr(value, "activityecorelua_Function189", self)

class activityecorelua_Statement_FunctioncallOrAssignment(Statement):

    pass
class activityecorelua_Statement_While(Statement):

    pass
class activityecorelua_Statement_If_Then_Else(Statement):

    pass
class activityecorelua_Statement_For_Generic(Statement):

    def __init__(self, names: str, activityecorelua_Statement_For_Generic: set["activityecorelua_Expression"] = None, activityecorelua_Statement_For_Generic185: "activityecorelua_Block" = None):
        self.names = names
        self.activityecorelua_Statement_For_Generic = activityecorelua_Statement_For_Generic if activityecorelua_Statement_For_Generic is not None else set()
        self.activityecorelua_Statement_For_Generic185 = activityecorelua_Statement_For_Generic185
        
    @property
    def names(self) -> str:
        return self.__names

    @names.setter
    def names(self, names: str):
        self.__names = names

    @property
    def activityecorelua_Statement_For_Generic185(self):
        return self.__activityecorelua_Statement_For_Generic185

    @activityecorelua_Statement_For_Generic185.setter
    def activityecorelua_Statement_For_Generic185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Statement_For_Generic__activityecorelua_Statement_For_Generic185", None)
        self.__activityecorelua_Statement_For_Generic185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Block186"):
                opp_val = getattr(old_value, "activityecorelua_Block186", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Block186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Block186"):
                opp_val = getattr(value, "activityecorelua_Block186", None)
                setattr(value, "activityecorelua_Block186", self)

    @property
    def activityecorelua_Statement_For_Generic(self):
        return self.__activityecorelua_Statement_For_Generic

    @activityecorelua_Statement_For_Generic.setter
    def activityecorelua_Statement_For_Generic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Statement_For_Generic__activityecorelua_Statement_For_Generic", None)
        self.__activityecorelua_Statement_For_Generic = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_Expression183"):
                    opp_val = getattr(item, "activityecorelua_Expression183", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_Expression183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_Expression183"):
                    opp_val = getattr(item, "activityecorelua_Expression183", None)
                    
                    setattr(item, "activityecorelua_Expression183", self)
                    

class activityecorelua_Statement_Local_Variable_Declaration(Statement):

    def __init__(self, variableNames: str, activityecorelua_Statement_Local_Variable_Declaration: set["activityecorelua_Expression"] = None):
        self.variableNames = variableNames
        self.activityecorelua_Statement_Local_Variable_Declaration = activityecorelua_Statement_Local_Variable_Declaration if activityecorelua_Statement_Local_Variable_Declaration is not None else set()
        
    @property
    def variableNames(self) -> str:
        return self.__variableNames

    @variableNames.setter
    def variableNames(self, variableNames: str):
        self.__variableNames = variableNames

    @property
    def activityecorelua_Statement_Local_Variable_Declaration(self):
        return self.__activityecorelua_Statement_Local_Variable_Declaration

    @activityecorelua_Statement_Local_Variable_Declaration.setter
    def activityecorelua_Statement_Local_Variable_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Statement_Local_Variable_Declaration__activityecorelua_Statement_Local_Variable_Declaration", None)
        self.__activityecorelua_Statement_Local_Variable_Declaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_Expression191"):
                    opp_val = getattr(item, "activityecorelua_Expression191", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_Expression191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_Expression191"):
                    opp_val = getattr(item, "activityecorelua_Expression191", None)
                    
                    setattr(item, "activityecorelua_Expression191", self)
                    

class activityecorelua_Statement_GlobalFunction_Declaration(Statement):

    def __init__(self, prefix: str, functionName: str, activityecorelua_Statement_GlobalFunction_Declaration: "activityecorelua_Function" = None):
        self.prefix = prefix
        self.functionName = functionName
        self.activityecorelua_Statement_GlobalFunction_Declaration = activityecorelua_Statement_GlobalFunction_Declaration
        
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
    def activityecorelua_Statement_GlobalFunction_Declaration(self):
        return self.__activityecorelua_Statement_GlobalFunction_Declaration

    @activityecorelua_Statement_GlobalFunction_Declaration.setter
    def activityecorelua_Statement_GlobalFunction_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Statement_GlobalFunction_Declaration__activityecorelua_Statement_GlobalFunction_Declaration", None)
        self.__activityecorelua_Statement_GlobalFunction_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Function"):
                opp_val = getattr(old_value, "activityecorelua_Function", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Function"):
                opp_val = getattr(value, "activityecorelua_Function", None)
                setattr(value, "activityecorelua_Function", self)

class activityecorelua_Statement_For_Numeric(Statement):

    def __init__(self, iteratorName: str, activityecorelua_Statement_For_Numeric: "activityecorelua_Expression" = None, activityecorelua_Statement_For_Numeric174: "activityecorelua_Expression" = None, activityecorelua_Statement_For_Numeric177: "activityecorelua_Expression" = None, activityecorelua_Statement_For_Numeric180: "activityecorelua_Block" = None):
        self.iteratorName = iteratorName
        self.activityecorelua_Statement_For_Numeric = activityecorelua_Statement_For_Numeric
        self.activityecorelua_Statement_For_Numeric174 = activityecorelua_Statement_For_Numeric174
        self.activityecorelua_Statement_For_Numeric177 = activityecorelua_Statement_For_Numeric177
        self.activityecorelua_Statement_For_Numeric180 = activityecorelua_Statement_For_Numeric180
        
    @property
    def iteratorName(self) -> str:
        return self.__iteratorName

    @iteratorName.setter
    def iteratorName(self, iteratorName: str):
        self.__iteratorName = iteratorName

    @property
    def activityecorelua_Statement_For_Numeric180(self):
        return self.__activityecorelua_Statement_For_Numeric180

    @activityecorelua_Statement_For_Numeric180.setter
    def activityecorelua_Statement_For_Numeric180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Statement_For_Numeric__activityecorelua_Statement_For_Numeric180", None)
        self.__activityecorelua_Statement_For_Numeric180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Block181"):
                opp_val = getattr(old_value, "activityecorelua_Block181", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Block181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Block181"):
                opp_val = getattr(value, "activityecorelua_Block181", None)
                setattr(value, "activityecorelua_Block181", self)

    @property
    def activityecorelua_Statement_For_Numeric(self):
        return self.__activityecorelua_Statement_For_Numeric

    @activityecorelua_Statement_For_Numeric.setter
    def activityecorelua_Statement_For_Numeric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Statement_For_Numeric__activityecorelua_Statement_For_Numeric", None)
        self.__activityecorelua_Statement_For_Numeric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Expression172"):
                opp_val = getattr(old_value, "activityecorelua_Expression172", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Expression172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Expression172"):
                opp_val = getattr(value, "activityecorelua_Expression172", None)
                setattr(value, "activityecorelua_Expression172", self)

    @property
    def activityecorelua_Statement_For_Numeric174(self):
        return self.__activityecorelua_Statement_For_Numeric174

    @activityecorelua_Statement_For_Numeric174.setter
    def activityecorelua_Statement_For_Numeric174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Statement_For_Numeric__activityecorelua_Statement_For_Numeric174", None)
        self.__activityecorelua_Statement_For_Numeric174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Expression175"):
                opp_val = getattr(old_value, "activityecorelua_Expression175", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Expression175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Expression175"):
                opp_val = getattr(value, "activityecorelua_Expression175", None)
                setattr(value, "activityecorelua_Expression175", self)

    @property
    def activityecorelua_Statement_For_Numeric177(self):
        return self.__activityecorelua_Statement_For_Numeric177

    @activityecorelua_Statement_For_Numeric177.setter
    def activityecorelua_Statement_For_Numeric177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Statement_For_Numeric__activityecorelua_Statement_For_Numeric177", None)
        self.__activityecorelua_Statement_For_Numeric177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Expression178"):
                opp_val = getattr(old_value, "activityecorelua_Expression178", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Expression178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Expression178"):
                opp_val = getattr(value, "activityecorelua_Expression178", None)
                setattr(value, "activityecorelua_Expression178", self)

class activityecorelua_Statement_Block(Statement):

    pass
class LastStatement:

    pass
class activityecorelua_LastStatement_Break(LastStatement):

    pass
class activityecorelua_LastStatement_Return(LastStatement):

    pass
class activityecorelua_LastStatement:

    pass
class activityecorelua_Statement:

    pass
class Chunk:

    pass
class activityecorelua_Block(Chunk):

    pass
class activityecorelua_Chunk:

    pass
class activityecorelua_Input:

    pass
class activityecorelua_InputValue:

    pass
class Value:

    pass
class activityecorelua_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class activityecorelua_BooleanValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class Variable:

    pass
class activityecorelua_IntegerVariable(Variable):

    pass
class activityecorelua_Statement_Repeat(Statement):

    pass
class FinalNode:

    pass
class activityecorelua_ActivityFinalNode(FinalNode):

    pass
class ControlNode:

    pass
class activityecorelua_FinalNode(ControlNode):

    pass
class activityecorelua_JoinNode(ControlNode):

    pass
class activityecorelua_DecisionNode(ControlNode):

    pass
class activityecorelua_ForkNode(ControlNode):

    pass
class activityecorelua_MergeNode(ControlNode):

    pass
class activityecorelua_InitialNode(ControlNode):

    pass
class activityecorelua_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class activityecorelua_Expression(Statement_FunctioncallOrAssignment):

    pass
class Action:

    pass
class activityecorelua_OpaqueAction(Action):

    pass
class ExecutableNode:

    pass
class activityecorelua_Action(ExecutableNode):

    pass
class ActivityNode:

    pass
class activityecorelua_ExecutableNode(ActivityNode):

    pass
class activityecorelua_ControlNode(ActivityNode):

    pass
class activityecorelua_BooleanVariable(Variable):

    pass
class ActivityEdge:

    pass
class activityecorelua_ControlFlow(ActivityEdge):

    pass
class activityecorelua_Value(ABC):

    pass
class NamedElement:

    pass
class activityecorelua_ActivityEdge(NamedElement):

    pass
class activityecorelua_ActivityNode(NamedElement):

    def __init__(self, running: bool, ActivityNode: "activityecorelua_Activity" = None, source: set["activityecorelua_ActivityEdge"] = None, target: set["activityecorelua_ActivityEdge"] = None, nodes: "activityecorelua_Activity" = None, ActivityNode123: "activityecorelua_ActivityEdge" = None, ActivityNode125: "activityecorelua_ActivityEdge" = None):
        self.running = running
        self.ActivityNode = ActivityNode
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.nodes = nodes
        self.ActivityNode123 = ActivityNode123
        self.ActivityNode125 = ActivityNode125
        
    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_ActivityNode__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    setattr(item, "ActivityEdge", self)
                    

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_ActivityNode__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity"):
                opp_val = getattr(old_value, "Activity", None)
                if opp_val == self:
                    setattr(old_value, "Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity"):
                opp_val = getattr(value, "Activity", None)
                setattr(value, "Activity", self)

    @property
    def ActivityNode(self):
        return self.__ActivityNode

    @ActivityNode.setter
    def ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_ActivityNode__ActivityNode", None)
        self.__ActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity"):
                opp_val = getattr(old_value, "activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity"):
                opp_val = getattr(value, "activity", None)
                if opp_val is None:
                    setattr(value, "activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ActivityNode123(self):
        return self.__ActivityNode123

    @ActivityNode123.setter
    def ActivityNode123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_ActivityNode__ActivityNode123", None)
        self.__ActivityNode123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_ActivityNode__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge120"):
                    opp_val = getattr(item, "ActivityEdge120", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge120"):
                    opp_val = getattr(item, "ActivityEdge120", None)
                    
                    setattr(item, "ActivityEdge120", self)
                    

    @property
    def ActivityNode125(self):
        return self.__ActivityNode125

    @ActivityNode125.setter
    def ActivityNode125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_ActivityNode__ActivityNode125", None)
        self.__ActivityNode125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

class activityecorelua_Variable(ABC):

    def __init__(self, name: str, activityecorelua_Variable: "activityecorelua_Activity" = None, activityecorelua_Variable117: "activityecorelua_Activity" = None, activityecorelua_Variable129: "activityecorelua_Value" = None, activityecorelua_Variable131: "activityecorelua_Value" = None, activityecorelua_Variable137: "activityecorelua_InputValue" = None):
        self.name = name
        self.activityecorelua_Variable = activityecorelua_Variable
        self.activityecorelua_Variable117 = activityecorelua_Variable117
        self.activityecorelua_Variable129 = activityecorelua_Variable129
        self.activityecorelua_Variable131 = activityecorelua_Variable131
        self.activityecorelua_Variable137 = activityecorelua_Variable137
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def activityecorelua_Variable117(self):
        return self.__activityecorelua_Variable117

    @activityecorelua_Variable117.setter
    def activityecorelua_Variable117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Variable__activityecorelua_Variable117", None)
        self.__activityecorelua_Variable117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Activity116"):
                opp_val = getattr(old_value, "activityecorelua_Activity116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Activity116"):
                opp_val = getattr(value, "activityecorelua_Activity116", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_Activity116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activityecorelua_Variable129(self):
        return self.__activityecorelua_Variable129

    @activityecorelua_Variable129.setter
    def activityecorelua_Variable129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Variable__activityecorelua_Variable129", None)
        self.__activityecorelua_Variable129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Value"):
                opp_val = getattr(old_value, "activityecorelua_Value", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Value"):
                opp_val = getattr(value, "activityecorelua_Value", None)
                setattr(value, "activityecorelua_Value", self)

    @property
    def activityecorelua_Variable137(self):
        return self.__activityecorelua_Variable137

    @activityecorelua_Variable137.setter
    def activityecorelua_Variable137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Variable__activityecorelua_Variable137", None)
        self.__activityecorelua_Variable137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_InputValue136"):
                opp_val = getattr(old_value, "activityecorelua_InputValue136", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_InputValue136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_InputValue136"):
                opp_val = getattr(value, "activityecorelua_InputValue136", None)
                setattr(value, "activityecorelua_InputValue136", self)

    @property
    def activityecorelua_Variable131(self):
        return self.__activityecorelua_Variable131

    @activityecorelua_Variable131.setter
    def activityecorelua_Variable131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Variable__activityecorelua_Variable131", None)
        self.__activityecorelua_Variable131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Value132"):
                opp_val = getattr(old_value, "activityecorelua_Value132", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Value132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Value132"):
                opp_val = getattr(value, "activityecorelua_Value132", None)
                setattr(value, "activityecorelua_Value132", self)

    @property
    def activityecorelua_Variable(self):
        return self.__activityecorelua_Variable

    @activityecorelua_Variable.setter
    def activityecorelua_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_Variable__activityecorelua_Variable", None)
        self.__activityecorelua_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Activity114"):
                opp_val = getattr(old_value, "activityecorelua_Activity114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Activity114"):
                opp_val = getattr(value, "activityecorelua_Activity114", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_Activity114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class activityecorelua_Activity(NamedElement):

    pass
class ETypedElement:

    pass
class activityecorelua_EParameter(ETypedElement):

    pass
class ENamedElement:

    pass
class activityecorelua_ETypeParameter(ENamedElement):

    pass
class activityecorelua_EEnumLiteral(ENamedElement):

    def __init__(self, value: int, instance: str, literal: str, EEnumLiteral: "activityecorelua_EEnum" = None, eLiterals: "activityecorelua_EEnum" = None):
        self.value = value
        self.instance = instance
        self.literal = literal
        self.EEnumLiteral = EEnumLiteral
        self.eLiterals = eLiterals
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def instance(self) -> str:
        return self.__instance

    @instance.setter
    def instance(self, instance: str):
        self.__instance = instance

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def eLiterals(self):
        return self.__eLiterals

    @eLiterals.setter
    def eLiterals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EEnumLiteral__eLiterals", None)
        self.__eLiterals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EEnum"):
                opp_val = getattr(old_value, "EEnum", None)
                if opp_val == self:
                    setattr(old_value, "EEnum", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EEnum"):
                opp_val = getattr(value, "EEnum", None)
                setattr(value, "EEnum", self)

    @property
    def EEnumLiteral(self):
        return self.__EEnumLiteral

    @EEnumLiteral.setter
    def EEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EEnumLiteral__EEnumLiteral", None)
        self.__EEnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eEnum"):
                opp_val = getattr(old_value, "eEnum", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eEnum"):
                opp_val = getattr(value, "eEnum", None)
                if opp_val is None:
                    setattr(value, "eEnum", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class activityecorelua_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, EPackage: "activityecorelua_EClassifier" = None, EPackage47: "activityecorelua_EFactory" = None, ePackage: "activityecorelua_EFactory" = None, ePackage64: set["activityecorelua_EClassifier"] = None, EPackage67: "activityecorelua_EPackage" = None, eSuperPackage: set["activityecorelua_EPackage"] = None, EPackage70: "activityecorelua_EPackage" = None, eSubpackages: "activityecorelua_EPackage" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.EPackage = EPackage
        self.EPackage47 = EPackage47
        self.ePackage = ePackage
        self.ePackage64 = ePackage64 if ePackage64 is not None else set()
        self.EPackage67 = EPackage67
        self.eSuperPackage = eSuperPackage if eSuperPackage is not None else set()
        self.EPackage70 = EPackage70
        self.eSubpackages = eSubpackages
        
    @property
    def nsPrefix(self) -> str:
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix

    @property
    def nsURI(self) -> str:
        return self.__nsURI

    @nsURI.setter
    def nsURI(self, nsURI: str):
        self.__nsURI = nsURI

    @property
    def ePackage64(self):
        return self.__ePackage64

    @ePackage64.setter
    def ePackage64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EPackage__ePackage64", None)
        self.__ePackage64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EClassifier"):
                    opp_val = getattr(item, "EClassifier", None)
                    
                    if opp_val == self:
                        setattr(item, "EClassifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EClassifier"):
                    opp_val = getattr(item, "EClassifier", None)
                    
                    setattr(item, "EClassifier", self)
                    

    @property
    def eSubpackages(self):
        return self.__eSubpackages

    @eSubpackages.setter
    def eSubpackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EPackage__eSubpackages", None)
        self.__eSubpackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage70"):
                opp_val = getattr(old_value, "EPackage70", None)
                if opp_val == self:
                    setattr(old_value, "EPackage70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage70"):
                opp_val = getattr(value, "EPackage70", None)
                setattr(value, "EPackage70", self)

    @property
    def EPackage70(self):
        return self.__EPackage70

    @EPackage70.setter
    def EPackage70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EPackage__EPackage70", None)
        self.__EPackage70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSubpackages"):
                opp_val = getattr(old_value, "eSubpackages", None)
                if opp_val == self:
                    setattr(old_value, "eSubpackages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSubpackages"):
                opp_val = getattr(value, "eSubpackages", None)
                setattr(value, "eSubpackages", self)

    @property
    def EPackage67(self):
        return self.__EPackage67

    @EPackage67.setter
    def EPackage67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EPackage__EPackage67", None)
        self.__EPackage67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSuperPackage"):
                opp_val = getattr(old_value, "eSuperPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSuperPackage"):
                opp_val = getattr(value, "eSuperPackage", None)
                if opp_val is None:
                    setattr(value, "eSuperPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eSuperPackage(self):
        return self.__eSuperPackage

    @eSuperPackage.setter
    def eSuperPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EPackage__eSuperPackage", None)
        self.__eSuperPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EPackage67"):
                    opp_val = getattr(item, "EPackage67", None)
                    
                    if opp_val == self:
                        setattr(item, "EPackage67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EPackage67"):
                    opp_val = getattr(item, "EPackage67", None)
                    
                    setattr(item, "EPackage67", self)
                    

    @property
    def EPackage(self):
        return self.__EPackage

    @EPackage.setter
    def EPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EPackage__EPackage", None)
        self.__EPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eClassifiers"):
                opp_val = getattr(old_value, "eClassifiers", None)
                if opp_val == self:
                    setattr(old_value, "eClassifiers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eClassifiers"):
                opp_val = getattr(value, "eClassifiers", None)
                setattr(value, "eClassifiers", self)

    @property
    def EPackage47(self):
        return self.__EPackage47

    @EPackage47.setter
    def EPackage47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EPackage__EPackage47", None)
        self.__EPackage47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eFactoryInstance"):
                opp_val = getattr(old_value, "eFactoryInstance", None)
                if opp_val == self:
                    setattr(old_value, "eFactoryInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eFactoryInstance"):
                opp_val = getattr(value, "eFactoryInstance", None)
                setattr(value, "eFactoryInstance", self)

    @property
    def ePackage(self):
        return self.__ePackage

    @ePackage.setter
    def ePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EPackage__ePackage", None)
        self.__ePackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFactory"):
                opp_val = getattr(old_value, "EFactory", None)
                if opp_val == self:
                    setattr(old_value, "EFactory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFactory"):
                opp_val = getattr(value, "EFactory", None)
                setattr(value, "EFactory", self)

    def getEClassifier(self, name: str) -> EClassifier:
        # TODO: Implement getEClassifier method
        pass

class activityecorelua_ETypedElement(ENamedElement):

    def __init__(self, ordered: bool, unique: bool, lowerBound: int, upperBound: int, many: bool, required: bool, activityecorelua_ETypedElement: "activityecorelua_EClassifier" = None, activityecorelua_ETypedElement87: "activityecorelua_EGenericType" = None):
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.activityecorelua_ETypedElement = activityecorelua_ETypedElement
        self.activityecorelua_ETypedElement87 = activityecorelua_ETypedElement87
        
    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def activityecorelua_ETypedElement(self):
        return self.__activityecorelua_ETypedElement

    @activityecorelua_ETypedElement.setter
    def activityecorelua_ETypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_ETypedElement__activityecorelua_ETypedElement", None)
        self.__activityecorelua_ETypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EClassifier85"):
                opp_val = getattr(old_value, "activityecorelua_EClassifier85", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_EClassifier85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EClassifier85"):
                opp_val = getattr(value, "activityecorelua_EClassifier85", None)
                setattr(value, "activityecorelua_EClassifier85", self)

    @property
    def activityecorelua_ETypedElement87(self):
        return self.__activityecorelua_ETypedElement87

    @activityecorelua_ETypedElement87.setter
    def activityecorelua_ETypedElement87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_ETypedElement__activityecorelua_ETypedElement87", None)
        self.__activityecorelua_ETypedElement87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EGenericType88"):
                opp_val = getattr(old_value, "activityecorelua_EGenericType88", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_EGenericType88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EGenericType88"):
                opp_val = getattr(value, "activityecorelua_EGenericType88", None)
                setattr(value, "activityecorelua_EGenericType88", self)

class activityecorelua_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, instanceClass: str, defaultValue: str, instanceTypeName: str, eClassifiers: "activityecorelua_EPackage" = None, activityecorelua_EClassifier: set["activityecorelua_ETypeParameter"] = None, activityecorelua_EClassifier58: "activityecorelua_EOperation" = None, EClassifier: "activityecorelua_EPackage" = None, activityecorelua_EClassifier85: "activityecorelua_ETypedElement" = None, activityecorelua_EClassifier97: "activityecorelua_EGenericType" = None, activityecorelua_EClassifier106: "activityecorelua_EGenericType" = None):
        self.instanceClassName = instanceClassName
        self.instanceClass = instanceClass
        self.defaultValue = defaultValue
        self.instanceTypeName = instanceTypeName
        self.eClassifiers = eClassifiers
        self.activityecorelua_EClassifier = activityecorelua_EClassifier if activityecorelua_EClassifier is not None else set()
        self.activityecorelua_EClassifier58 = activityecorelua_EClassifier58
        self.EClassifier = EClassifier
        self.activityecorelua_EClassifier85 = activityecorelua_EClassifier85
        self.activityecorelua_EClassifier97 = activityecorelua_EClassifier97
        self.activityecorelua_EClassifier106 = activityecorelua_EClassifier106
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

    @property
    def instanceTypeName(self) -> str:
        return self.__instanceTypeName

    @instanceTypeName.setter
    def instanceTypeName(self, instanceTypeName: str):
        self.__instanceTypeName = instanceTypeName

    @property
    def instanceClass(self) -> str:
        return self.__instanceClass

    @instanceClass.setter
    def instanceClass(self, instanceClass: str):
        self.__instanceClass = instanceClass

    @property
    def activityecorelua_EClassifier106(self):
        return self.__activityecorelua_EClassifier106

    @activityecorelua_EClassifier106.setter
    def activityecorelua_EClassifier106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClassifier__activityecorelua_EClassifier106", None)
        self.__activityecorelua_EClassifier106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EGenericType105"):
                opp_val = getattr(old_value, "activityecorelua_EGenericType105", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_EGenericType105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EGenericType105"):
                opp_val = getattr(value, "activityecorelua_EGenericType105", None)
                setattr(value, "activityecorelua_EGenericType105", self)

    @property
    def activityecorelua_EClassifier58(self):
        return self.__activityecorelua_EClassifier58

    @activityecorelua_EClassifier58.setter
    def activityecorelua_EClassifier58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClassifier__activityecorelua_EClassifier58", None)
        self.__activityecorelua_EClassifier58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EOperation57"):
                opp_val = getattr(old_value, "activityecorelua_EOperation57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EOperation57"):
                opp_val = getattr(value, "activityecorelua_EOperation57", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EOperation57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activityecorelua_EClassifier97(self):
        return self.__activityecorelua_EClassifier97

    @activityecorelua_EClassifier97.setter
    def activityecorelua_EClassifier97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClassifier__activityecorelua_EClassifier97", None)
        self.__activityecorelua_EClassifier97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EGenericType96"):
                opp_val = getattr(old_value, "activityecorelua_EGenericType96", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_EGenericType96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EGenericType96"):
                opp_val = getattr(value, "activityecorelua_EGenericType96", None)
                setattr(value, "activityecorelua_EGenericType96", self)

    @property
    def activityecorelua_EClassifier85(self):
        return self.__activityecorelua_EClassifier85

    @activityecorelua_EClassifier85.setter
    def activityecorelua_EClassifier85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClassifier__activityecorelua_EClassifier85", None)
        self.__activityecorelua_EClassifier85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_ETypedElement"):
                opp_val = getattr(old_value, "activityecorelua_ETypedElement", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_ETypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_ETypedElement"):
                opp_val = getattr(value, "activityecorelua_ETypedElement", None)
                setattr(value, "activityecorelua_ETypedElement", self)

    @property
    def EClassifier(self):
        return self.__EClassifier

    @EClassifier.setter
    def EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClassifier__EClassifier", None)
        self.__EClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ePackage64"):
                opp_val = getattr(old_value, "ePackage64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage64"):
                opp_val = getattr(value, "ePackage64", None)
                if opp_val is None:
                    setattr(value, "ePackage64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activityecorelua_EClassifier(self):
        return self.__activityecorelua_EClassifier

    @activityecorelua_EClassifier.setter
    def activityecorelua_EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClassifier__activityecorelua_EClassifier", None)
        self.__activityecorelua_EClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_ETypeParameter"):
                    opp_val = getattr(item, "activityecorelua_ETypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_ETypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_ETypeParameter"):
                    opp_val = getattr(item, "activityecorelua_ETypeParameter", None)
                    
                    setattr(item, "activityecorelua_ETypeParameter", self)
                    

    @property
    def eClassifiers(self):
        return self.__eClassifiers

    @eClassifiers.setter
    def eClassifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClassifier__eClassifiers", None)
        self.__eClassifiers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage"):
                opp_val = getattr(old_value, "EPackage", None)
                if opp_val == self:
                    setattr(old_value, "EPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage"):
                opp_val = getattr(value, "EPackage", None)
                setattr(value, "EPackage", self)

    def isInstance(self, object: str) -> bool:
        # TODO: Implement isInstance method
        pass

    def getClassifierID(self) -> int:
        # TODO: Implement getClassifierID method
        pass

class activityecorelua_EGenericType:

    pass
class EDataType:

    pass
class activityecorelua_EEnum(EDataType):

    def __init__(self, eEnum: set["activityecorelua_EEnumLiteral"] = None, EEnum: "activityecorelua_EEnumLiteral" = None):
        self.eEnum = eEnum if eEnum is not None else set()
        self.EEnum = EEnum
        
    @property
    def eEnum(self):
        return self.__eEnum

    @eEnum.setter
    def eEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EEnum__eEnum", None)
        self.__eEnum = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EEnumLiteral"):
                    opp_val = getattr(item, "EEnumLiteral", None)
                    
                    if opp_val == self:
                        setattr(item, "EEnumLiteral", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EEnumLiteral"):
                    opp_val = getattr(item, "EEnumLiteral", None)
                    
                    setattr(item, "EEnumLiteral", self)
                    

    @property
    def EEnum(self):
        return self.__EEnum

    @EEnum.setter
    def EEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EEnum__EEnum", None)
        self.__EEnum = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eLiterals"):
                opp_val = getattr(old_value, "eLiterals", None)
                if opp_val == self:
                    setattr(old_value, "eLiterals", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eLiterals"):
                opp_val = getattr(value, "eLiterals", None)
                setattr(value, "eLiterals", self)

    def getEEnumLiteralByLiteral(self, literal: str) -> str:
        # TODO: Implement getEEnumLiteralByLiteral method
        pass

    def getEEnumLiteral(self, name: str) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteral(self, value: int) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

class activityecorelua_EOperation(ETypedElement):

    def __init__(self, EOperation: "activityecorelua_EClass" = None, activityecorelua_EOperation: "activityecorelua_EClass" = None, eOperations: "activityecorelua_EClass" = None, activityecorelua_EOperation51: set["activityecorelua_ETypeParameter"] = None, eOperation: set["activityecorelua_EParameter"] = None, activityecorelua_EOperation55: "activityecorelua_Activity" = None, activityecorelua_EOperation57: set["activityecorelua_EClassifier"] = None, activityecorelua_EOperation60: set["activityecorelua_EGenericType"] = None, EOperation72: "activityecorelua_EParameter" = None):
        self.EOperation = EOperation
        self.activityecorelua_EOperation = activityecorelua_EOperation
        self.eOperations = eOperations
        self.activityecorelua_EOperation51 = activityecorelua_EOperation51 if activityecorelua_EOperation51 is not None else set()
        self.eOperation = eOperation if eOperation is not None else set()
        self.activityecorelua_EOperation55 = activityecorelua_EOperation55
        self.activityecorelua_EOperation57 = activityecorelua_EOperation57 if activityecorelua_EOperation57 is not None else set()
        self.activityecorelua_EOperation60 = activityecorelua_EOperation60 if activityecorelua_EOperation60 is not None else set()
        self.EOperation72 = EOperation72
        
    @property
    def activityecorelua_EOperation60(self):
        return self.__activityecorelua_EOperation60

    @activityecorelua_EOperation60.setter
    def activityecorelua_EOperation60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EOperation__activityecorelua_EOperation60", None)
        self.__activityecorelua_EOperation60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EGenericType61"):
                    opp_val = getattr(item, "activityecorelua_EGenericType61", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EGenericType61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EGenericType61"):
                    opp_val = getattr(item, "activityecorelua_EGenericType61", None)
                    
                    setattr(item, "activityecorelua_EGenericType61", self)
                    

    @property
    def activityecorelua_EOperation51(self):
        return self.__activityecorelua_EOperation51

    @activityecorelua_EOperation51.setter
    def activityecorelua_EOperation51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EOperation__activityecorelua_EOperation51", None)
        self.__activityecorelua_EOperation51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_ETypeParameter52"):
                    opp_val = getattr(item, "activityecorelua_ETypeParameter52", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_ETypeParameter52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_ETypeParameter52"):
                    opp_val = getattr(item, "activityecorelua_ETypeParameter52", None)
                    
                    setattr(item, "activityecorelua_ETypeParameter52", self)
                    

    @property
    def EOperation72(self):
        return self.__EOperation72

    @EOperation72.setter
    def EOperation72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EOperation__EOperation72", None)
        self.__EOperation72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eParameters"):
                opp_val = getattr(old_value, "eParameters", None)
                if opp_val == self:
                    setattr(old_value, "eParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eParameters"):
                opp_val = getattr(value, "eParameters", None)
                setattr(value, "eParameters", self)

    @property
    def activityecorelua_EOperation(self):
        return self.__activityecorelua_EOperation

    @activityecorelua_EOperation.setter
    def activityecorelua_EOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EOperation__activityecorelua_EOperation", None)
        self.__activityecorelua_EOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EClass26"):
                opp_val = getattr(old_value, "activityecorelua_EClass26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EClass26"):
                opp_val = getattr(value, "activityecorelua_EClass26", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EClass26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eOperations(self):
        return self.__eOperations

    @eOperations.setter
    def eOperations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EOperation__eOperations", None)
        self.__eOperations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClass"):
                opp_val = getattr(old_value, "EClass", None)
                if opp_val == self:
                    setattr(old_value, "EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass"):
                opp_val = getattr(value, "EClass", None)
                setattr(value, "EClass", self)

    @property
    def EOperation(self):
        return self.__EOperation

    @EOperation.setter
    def EOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EOperation__EOperation", None)
        self.__EOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eContainingClass"):
                opp_val = getattr(old_value, "eContainingClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eContainingClass"):
                opp_val = getattr(value, "eContainingClass", None)
                if opp_val is None:
                    setattr(value, "eContainingClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activityecorelua_EOperation57(self):
        return self.__activityecorelua_EOperation57

    @activityecorelua_EOperation57.setter
    def activityecorelua_EOperation57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EOperation__activityecorelua_EOperation57", None)
        self.__activityecorelua_EOperation57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EClassifier58"):
                    opp_val = getattr(item, "activityecorelua_EClassifier58", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EClassifier58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EClassifier58"):
                    opp_val = getattr(item, "activityecorelua_EClassifier58", None)
                    
                    setattr(item, "activityecorelua_EClassifier58", self)
                    

    @property
    def activityecorelua_EOperation55(self):
        return self.__activityecorelua_EOperation55

    @activityecorelua_EOperation55.setter
    def activityecorelua_EOperation55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EOperation__activityecorelua_EOperation55", None)
        self.__activityecorelua_EOperation55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_Activity"):
                opp_val = getattr(old_value, "activityecorelua_Activity", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_Activity"):
                opp_val = getattr(value, "activityecorelua_Activity", None)
                setattr(value, "activityecorelua_Activity", self)

    @property
    def eOperation(self):
        return self.__eOperation

    @eOperation.setter
    def eOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EOperation__eOperation", None)
        self.__eOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EParameter"):
                    opp_val = getattr(item, "EParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "EParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EParameter"):
                    opp_val = getattr(item, "EParameter", None)
                    
                    setattr(item, "EParameter", self)
                    

    def isOverrideOf(self, someOperation: str) -> bool:
        # TODO: Implement isOverrideOf method
        pass

    def getOperationID(self) -> int:
        # TODO: Implement getOperationID method
        pass

class activityecorelua_EStructuralFeature(ETypedElement):

    def __init__(self, changeable: bool, volatile: bool, transient: bool, defaultValueLiteral: str, defaultValue: str, unsettable: bool, derived: bool, activityecorelua_EStructuralFeature: "activityecorelua_EClass" = None, EStructuralFeature: "activityecorelua_EClass" = None, eStructuralFeatures: "activityecorelua_EClass" = None):
        self.changeable = changeable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.unsettable = unsettable
        self.derived = derived
        self.activityecorelua_EStructuralFeature = activityecorelua_EStructuralFeature
        self.EStructuralFeature = EStructuralFeature
        self.eStructuralFeatures = eStructuralFeatures
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def unsettable(self) -> bool:
        return self.__unsettable

    @unsettable.setter
    def unsettable(self, unsettable: bool):
        self.__unsettable = unsettable

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def defaultValueLiteral(self) -> str:
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral

    @property
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def EStructuralFeature(self):
        return self.__EStructuralFeature

    @EStructuralFeature.setter
    def EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EStructuralFeature__EStructuralFeature", None)
        self.__EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eContainingClass36"):
                opp_val = getattr(old_value, "eContainingClass36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eContainingClass36"):
                opp_val = getattr(value, "eContainingClass36", None)
                if opp_val is None:
                    setattr(value, "eContainingClass36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eStructuralFeatures(self):
        return self.__eStructuralFeatures

    @eStructuralFeatures.setter
    def eStructuralFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EStructuralFeature__eStructuralFeatures", None)
        self.__eStructuralFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClass83"):
                opp_val = getattr(old_value, "EClass83", None)
                if opp_val == self:
                    setattr(old_value, "EClass83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass83"):
                opp_val = getattr(value, "EClass83", None)
                setattr(value, "EClass83", self)

    @property
    def activityecorelua_EStructuralFeature(self):
        return self.__activityecorelua_EStructuralFeature

    @activityecorelua_EStructuralFeature.setter
    def activityecorelua_EStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EStructuralFeature__activityecorelua_EStructuralFeature", None)
        self.__activityecorelua_EStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EClass28"):
                opp_val = getattr(old_value, "activityecorelua_EClass28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EClass28"):
                opp_val = getattr(value, "activityecorelua_EClass28", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EClass28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getContainerClass(self):
        # TODO: Implement getContainerClass method
        pass

    def getFeatureID(self) -> int:
        # TODO: Implement getFeatureID method
        pass

class EClassifier:

    pass
class activityecorelua_EClass(EClassifier):

    def __init__(self, abstract: bool, interface: bool, activityecorelua_EClass28: set["activityecorelua_EStructuralFeature"] = None, activityecorelua_EClass: "activityecorelua_EClass" = None, activityecorelua_EClass8: set["activityecorelua_EClass"] = None, eContainingClass: set["activityecorelua_EOperation"] = None, activityecorelua_EClass12: set["activityecorelua_EAttribute"] = None, activityecorelua_EClass15: set["activityecorelua_EReference"] = None, activityecorelua_EClass17: set["activityecorelua_EReference"] = None, activityecorelua_EClass20: set["activityecorelua_EAttribute"] = None, activityecorelua_EClass23: set["activityecorelua_EReference"] = None, activityecorelua_EClass26: set["activityecorelua_EOperation"] = None, activityecorelua_EClass31: "activityecorelua_EClass" = None, activityecorelua_EClass29: set["activityecorelua_EClass"] = None, activityecorelua_EClass33: "activityecorelua_EAttribute" = None, eContainingClass36: set["activityecorelua_EStructuralFeature"] = None, activityecorelua_EClass38: set["activityecorelua_EGenericType"] = None, activityecorelua_EClass40: set["activityecorelua_EGenericType"] = None, EClass: "activityecorelua_EOperation" = None, activityecorelua_EClass78: "activityecorelua_EReference" = None, EClass83: "activityecorelua_EStructuralFeature" = None):
        self.abstract = abstract
        self.interface = interface
        self.activityecorelua_EClass28 = activityecorelua_EClass28 if activityecorelua_EClass28 is not None else set()
        self.activityecorelua_EClass = activityecorelua_EClass
        self.activityecorelua_EClass8 = activityecorelua_EClass8 if activityecorelua_EClass8 is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.activityecorelua_EClass12 = activityecorelua_EClass12 if activityecorelua_EClass12 is not None else set()
        self.activityecorelua_EClass15 = activityecorelua_EClass15 if activityecorelua_EClass15 is not None else set()
        self.activityecorelua_EClass17 = activityecorelua_EClass17 if activityecorelua_EClass17 is not None else set()
        self.activityecorelua_EClass20 = activityecorelua_EClass20 if activityecorelua_EClass20 is not None else set()
        self.activityecorelua_EClass23 = activityecorelua_EClass23 if activityecorelua_EClass23 is not None else set()
        self.activityecorelua_EClass26 = activityecorelua_EClass26 if activityecorelua_EClass26 is not None else set()
        self.activityecorelua_EClass31 = activityecorelua_EClass31
        self.activityecorelua_EClass29 = activityecorelua_EClass29 if activityecorelua_EClass29 is not None else set()
        self.activityecorelua_EClass33 = activityecorelua_EClass33
        self.eContainingClass36 = eContainingClass36 if eContainingClass36 is not None else set()
        self.activityecorelua_EClass38 = activityecorelua_EClass38 if activityecorelua_EClass38 is not None else set()
        self.activityecorelua_EClass40 = activityecorelua_EClass40 if activityecorelua_EClass40 is not None else set()
        self.EClass = EClass
        self.activityecorelua_EClass78 = activityecorelua_EClass78
        self.EClass83 = EClass83
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def interface(self) -> bool:
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface

    @property
    def activityecorelua_EClass12(self):
        return self.__activityecorelua_EClass12

    @activityecorelua_EClass12.setter
    def activityecorelua_EClass12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass12", None)
        self.__activityecorelua_EClass12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EAttribute13"):
                    opp_val = getattr(item, "activityecorelua_EAttribute13", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EAttribute13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EAttribute13"):
                    opp_val = getattr(item, "activityecorelua_EAttribute13", None)
                    
                    setattr(item, "activityecorelua_EAttribute13", self)
                    

    @property
    def activityecorelua_EClass17(self):
        return self.__activityecorelua_EClass17

    @activityecorelua_EClass17.setter
    def activityecorelua_EClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass17", None)
        self.__activityecorelua_EClass17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EReference18"):
                    opp_val = getattr(item, "activityecorelua_EReference18", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EReference18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EReference18"):
                    opp_val = getattr(item, "activityecorelua_EReference18", None)
                    
                    setattr(item, "activityecorelua_EReference18", self)
                    

    @property
    def activityecorelua_EClass28(self):
        return self.__activityecorelua_EClass28

    @activityecorelua_EClass28.setter
    def activityecorelua_EClass28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass28", None)
        self.__activityecorelua_EClass28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EStructuralFeature"):
                    opp_val = getattr(item, "activityecorelua_EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EStructuralFeature"):
                    opp_val = getattr(item, "activityecorelua_EStructuralFeature", None)
                    
                    setattr(item, "activityecorelua_EStructuralFeature", self)
                    

    @property
    def activityecorelua_EClass78(self):
        return self.__activityecorelua_EClass78

    @activityecorelua_EClass78.setter
    def activityecorelua_EClass78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass78", None)
        self.__activityecorelua_EClass78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EReference77"):
                opp_val = getattr(old_value, "activityecorelua_EReference77", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_EReference77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EReference77"):
                opp_val = getattr(value, "activityecorelua_EReference77", None)
                setattr(value, "activityecorelua_EReference77", self)

    @property
    def activityecorelua_EClass8(self):
        return self.__activityecorelua_EClass8

    @activityecorelua_EClass8.setter
    def activityecorelua_EClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass8", None)
        self.__activityecorelua_EClass8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EClass"):
                    opp_val = getattr(item, "activityecorelua_EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EClass"):
                    opp_val = getattr(item, "activityecorelua_EClass", None)
                    
                    setattr(item, "activityecorelua_EClass", self)
                    

    @property
    def EClass(self):
        return self.__EClass

    @EClass.setter
    def EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__EClass", None)
        self.__EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eOperations"):
                opp_val = getattr(old_value, "eOperations", None)
                if opp_val == self:
                    setattr(old_value, "eOperations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eOperations"):
                opp_val = getattr(value, "eOperations", None)
                setattr(value, "eOperations", self)

    @property
    def activityecorelua_EClass38(self):
        return self.__activityecorelua_EClass38

    @activityecorelua_EClass38.setter
    def activityecorelua_EClass38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass38", None)
        self.__activityecorelua_EClass38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EGenericType"):
                    opp_val = getattr(item, "activityecorelua_EGenericType", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EGenericType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EGenericType"):
                    opp_val = getattr(item, "activityecorelua_EGenericType", None)
                    
                    setattr(item, "activityecorelua_EGenericType", self)
                    

    @property
    def activityecorelua_EClass20(self):
        return self.__activityecorelua_EClass20

    @activityecorelua_EClass20.setter
    def activityecorelua_EClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass20", None)
        self.__activityecorelua_EClass20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EAttribute21"):
                    opp_val = getattr(item, "activityecorelua_EAttribute21", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EAttribute21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EAttribute21"):
                    opp_val = getattr(item, "activityecorelua_EAttribute21", None)
                    
                    setattr(item, "activityecorelua_EAttribute21", self)
                    

    @property
    def EClass83(self):
        return self.__EClass83

    @EClass83.setter
    def EClass83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__EClass83", None)
        self.__EClass83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eStructuralFeatures"):
                opp_val = getattr(old_value, "eStructuralFeatures", None)
                if opp_val == self:
                    setattr(old_value, "eStructuralFeatures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eStructuralFeatures"):
                opp_val = getattr(value, "eStructuralFeatures", None)
                setattr(value, "eStructuralFeatures", self)

    @property
    def activityecorelua_EClass26(self):
        return self.__activityecorelua_EClass26

    @activityecorelua_EClass26.setter
    def activityecorelua_EClass26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass26", None)
        self.__activityecorelua_EClass26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EOperation"):
                    opp_val = getattr(item, "activityecorelua_EOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EOperation"):
                    opp_val = getattr(item, "activityecorelua_EOperation", None)
                    
                    setattr(item, "activityecorelua_EOperation", self)
                    

    @property
    def eContainingClass(self):
        return self.__eContainingClass

    @eContainingClass.setter
    def eContainingClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__eContainingClass", None)
        self.__eContainingClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EOperation"):
                    opp_val = getattr(item, "EOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "EOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EOperation"):
                    opp_val = getattr(item, "EOperation", None)
                    
                    setattr(item, "EOperation", self)
                    

    @property
    def activityecorelua_EClass40(self):
        return self.__activityecorelua_EClass40

    @activityecorelua_EClass40.setter
    def activityecorelua_EClass40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass40", None)
        self.__activityecorelua_EClass40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EGenericType41"):
                    opp_val = getattr(item, "activityecorelua_EGenericType41", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EGenericType41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EGenericType41"):
                    opp_val = getattr(item, "activityecorelua_EGenericType41", None)
                    
                    setattr(item, "activityecorelua_EGenericType41", self)
                    

    @property
    def activityecorelua_EClass(self):
        return self.__activityecorelua_EClass

    @activityecorelua_EClass.setter
    def activityecorelua_EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass", None)
        self.__activityecorelua_EClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EClass8"):
                opp_val = getattr(old_value, "activityecorelua_EClass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EClass8"):
                opp_val = getattr(value, "activityecorelua_EClass8", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EClass8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eContainingClass36(self):
        return self.__eContainingClass36

    @eContainingClass36.setter
    def eContainingClass36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__eContainingClass36", None)
        self.__eContainingClass36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EStructuralFeature"):
                    opp_val = getattr(item, "EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EStructuralFeature"):
                    opp_val = getattr(item, "EStructuralFeature", None)
                    
                    setattr(item, "EStructuralFeature", self)
                    

    @property
    def activityecorelua_EClass29(self):
        return self.__activityecorelua_EClass29

    @activityecorelua_EClass29.setter
    def activityecorelua_EClass29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass29", None)
        self.__activityecorelua_EClass29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EClass31"):
                    opp_val = getattr(item, "activityecorelua_EClass31", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EClass31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EClass31"):
                    opp_val = getattr(item, "activityecorelua_EClass31", None)
                    
                    setattr(item, "activityecorelua_EClass31", self)
                    

    @property
    def activityecorelua_EClass23(self):
        return self.__activityecorelua_EClass23

    @activityecorelua_EClass23.setter
    def activityecorelua_EClass23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass23", None)
        self.__activityecorelua_EClass23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EReference24"):
                    opp_val = getattr(item, "activityecorelua_EReference24", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EReference24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EReference24"):
                    opp_val = getattr(item, "activityecorelua_EReference24", None)
                    
                    setattr(item, "activityecorelua_EReference24", self)
                    

    @property
    def activityecorelua_EClass33(self):
        return self.__activityecorelua_EClass33

    @activityecorelua_EClass33.setter
    def activityecorelua_EClass33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass33", None)
        self.__activityecorelua_EClass33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EAttribute34"):
                opp_val = getattr(old_value, "activityecorelua_EAttribute34", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_EAttribute34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EAttribute34"):
                opp_val = getattr(value, "activityecorelua_EAttribute34", None)
                setattr(value, "activityecorelua_EAttribute34", self)

    @property
    def activityecorelua_EClass15(self):
        return self.__activityecorelua_EClass15

    @activityecorelua_EClass15.setter
    def activityecorelua_EClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass15", None)
        self.__activityecorelua_EClass15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EReference"):
                    opp_val = getattr(item, "activityecorelua_EReference", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EReference"):
                    opp_val = getattr(item, "activityecorelua_EReference", None)
                    
                    setattr(item, "activityecorelua_EReference", self)
                    

    @property
    def activityecorelua_EClass31(self):
        return self.__activityecorelua_EClass31

    @activityecorelua_EClass31.setter
    def activityecorelua_EClass31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EClass__activityecorelua_EClass31", None)
        self.__activityecorelua_EClass31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EClass29"):
                opp_val = getattr(old_value, "activityecorelua_EClass29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EClass29"):
                opp_val = getattr(value, "activityecorelua_EClass29", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EClass29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getEStructuralFeature(self, featureName: str) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getFeatureID(self, feature: EStructuralFeature) -> int:
        # TODO: Implement getFeatureID method
        pass

    def getFeatureCount(self) -> int:
        # TODO: Implement getFeatureCount method
        pass

    def isSuperTypeOf(self, someClass: str) -> bool:
        # TODO: Implement isSuperTypeOf method
        pass

    def getEOperation(self, operationID: int) -> str:
        # TODO: Implement getEOperation method
        pass

    def getEStructuralFeature(self, featureID: int) -> EStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getOverride(self, operation: str) -> str:
        # TODO: Implement getOverride method
        pass

    def getOperationCount(self) -> int:
        # TODO: Implement getOperationCount method
        pass

    def getOperationID(self, operation: str) -> int:
        # TODO: Implement getOperationID method
        pass

class activityecorelua_EObject:

    def __init__(self, activityecorelua_EObject: "activityecorelua_EAnnotation" = None, activityecorelua_EObject7: "activityecorelua_EAnnotation" = None):
        self.activityecorelua_EObject = activityecorelua_EObject
        self.activityecorelua_EObject7 = activityecorelua_EObject7
        
    @property
    def activityecorelua_EObject(self):
        return self.__activityecorelua_EObject

    @activityecorelua_EObject.setter
    def activityecorelua_EObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EObject__activityecorelua_EObject", None)
        self.__activityecorelua_EObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EAnnotation4"):
                opp_val = getattr(old_value, "activityecorelua_EAnnotation4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EAnnotation4"):
                opp_val = getattr(value, "activityecorelua_EAnnotation4", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EAnnotation4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activityecorelua_EObject7(self):
        return self.__activityecorelua_EObject7

    @activityecorelua_EObject7.setter
    def activityecorelua_EObject7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EObject__activityecorelua_EObject7", None)
        self.__activityecorelua_EObject7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EAnnotation6"):
                opp_val = getattr(old_value, "activityecorelua_EAnnotation6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EAnnotation6"):
                opp_val = getattr(value, "activityecorelua_EAnnotation6", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EAnnotation6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def eeClass(self) -> str:
        # TODO: Implement eeClass method
        pass

class activityecorelua_EModelElement(ABC):

    def __init__(self, EModelElement: "activityecorelua_EAnnotation" = None, eModelElement: set["activityecorelua_EAnnotation"] = None):
        self.EModelElement = EModelElement
        self.eModelElement = eModelElement if eModelElement is not None else set()
        
    @property
    def EModelElement(self):
        return self.__EModelElement

    @EModelElement.setter
    def EModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EModelElement__EModelElement", None)
        self.__EModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eAnnotations"):
                opp_val = getattr(old_value, "eAnnotations", None)
                if opp_val == self:
                    setattr(old_value, "eAnnotations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eAnnotations"):
                opp_val = getattr(value, "eAnnotations", None)
                setattr(value, "eAnnotations", self)

    @property
    def eModelElement(self):
        return self.__eModelElement

    @eModelElement.setter
    def eModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EModelElement__eModelElement", None)
        self.__eModelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EAnnotation"):
                    opp_val = getattr(item, "EAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "EAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EAnnotation"):
                    opp_val = getattr(item, "EAnnotation", None)
                    
                    setattr(item, "EAnnotation", self)
                    

    def getEAnnotation(self, source: str) -> str:
        # TODO: Implement getEAnnotation method
        pass

class activityecorelua_EStringToStringMapEntry:

    def __init__(self, key: str, value: str, activityecorelua_EStringToStringMapEntry: "activityecorelua_EAnnotation" = None):
        self.key = key
        self.value = value
        self.activityecorelua_EStringToStringMapEntry = activityecorelua_EStringToStringMapEntry
        
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

    @property
    def activityecorelua_EStringToStringMapEntry(self):
        return self.__activityecorelua_EStringToStringMapEntry

    @activityecorelua_EStringToStringMapEntry.setter
    def activityecorelua_EStringToStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EStringToStringMapEntry__activityecorelua_EStringToStringMapEntry", None)
        self.__activityecorelua_EStringToStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EAnnotation"):
                opp_val = getattr(old_value, "activityecorelua_EAnnotation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EAnnotation"):
                opp_val = getattr(value, "activityecorelua_EAnnotation", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EAnnotation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EModelElement:

    pass
class activityecorelua_EFactory(EModelElement):

    def __init__(self, eFactoryInstance: "activityecorelua_EPackage" = None, EFactory: "activityecorelua_EPackage" = None):
        self.eFactoryInstance = eFactoryInstance
        self.EFactory = EFactory
        
    @property
    def eFactoryInstance(self):
        return self.__eFactoryInstance

    @eFactoryInstance.setter
    def eFactoryInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EFactory__eFactoryInstance", None)
        self.__eFactoryInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EPackage47"):
                opp_val = getattr(old_value, "EPackage47", None)
                if opp_val == self:
                    setattr(old_value, "EPackage47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EPackage47"):
                opp_val = getattr(value, "EPackage47", None)
                setattr(value, "EPackage47", self)

    @property
    def EFactory(self):
        return self.__EFactory

    @EFactory.setter
    def EFactory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EFactory__EFactory", None)
        self.__EFactory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ePackage"):
                opp_val = getattr(old_value, "ePackage", None)
                if opp_val == self:
                    setattr(old_value, "ePackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage"):
                opp_val = getattr(value, "ePackage", None)
                setattr(value, "ePackage", self)

    def createFromString(self, literalValue: str, eDataType: EDataType) -> str:
        # TODO: Implement createFromString method
        pass

    def convertToString(self, instanceValue: str, eDataType: EDataType) -> str:
        # TODO: Implement convertToString method
        pass

    def create(self, eClass: str) -> str:
        # TODO: Implement create method
        pass

class activityecorelua_ENamedElement(EModelElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class activityecorelua_EAnnotation(EModelElement):

    def __init__(self, source: str, activityecorelua_EAnnotation: set["activityecorelua_EStringToStringMapEntry"] = None, eAnnotations: "activityecorelua_EModelElement" = None, activityecorelua_EAnnotation4: set["activityecorelua_EObject"] = None, activityecorelua_EAnnotation6: set["activityecorelua_EObject"] = None, EAnnotation: "activityecorelua_EModelElement" = None):
        self.source = source
        self.activityecorelua_EAnnotation = activityecorelua_EAnnotation if activityecorelua_EAnnotation is not None else set()
        self.eAnnotations = eAnnotations
        self.activityecorelua_EAnnotation4 = activityecorelua_EAnnotation4 if activityecorelua_EAnnotation4 is not None else set()
        self.activityecorelua_EAnnotation6 = activityecorelua_EAnnotation6 if activityecorelua_EAnnotation6 is not None else set()
        self.EAnnotation = EAnnotation
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def activityecorelua_EAnnotation6(self):
        return self.__activityecorelua_EAnnotation6

    @activityecorelua_EAnnotation6.setter
    def activityecorelua_EAnnotation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EAnnotation__activityecorelua_EAnnotation6", None)
        self.__activityecorelua_EAnnotation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EObject7"):
                    opp_val = getattr(item, "activityecorelua_EObject7", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EObject7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EObject7"):
                    opp_val = getattr(item, "activityecorelua_EObject7", None)
                    
                    setattr(item, "activityecorelua_EObject7", self)
                    

    @property
    def activityecorelua_EAnnotation4(self):
        return self.__activityecorelua_EAnnotation4

    @activityecorelua_EAnnotation4.setter
    def activityecorelua_EAnnotation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EAnnotation__activityecorelua_EAnnotation4", None)
        self.__activityecorelua_EAnnotation4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EObject"):
                    opp_val = getattr(item, "activityecorelua_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EObject"):
                    opp_val = getattr(item, "activityecorelua_EObject", None)
                    
                    setattr(item, "activityecorelua_EObject", self)
                    

    @property
    def EAnnotation(self):
        return self.__EAnnotation

    @EAnnotation.setter
    def EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EAnnotation__EAnnotation", None)
        self.__EAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eModelElement"):
                opp_val = getattr(old_value, "eModelElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eModelElement"):
                opp_val = getattr(value, "eModelElement", None)
                if opp_val is None:
                    setattr(value, "eModelElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activityecorelua_EAnnotation(self):
        return self.__activityecorelua_EAnnotation

    @activityecorelua_EAnnotation.setter
    def activityecorelua_EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EAnnotation__activityecorelua_EAnnotation", None)
        self.__activityecorelua_EAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EStringToStringMapEntry"):
                    opp_val = getattr(item, "activityecorelua_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EStringToStringMapEntry"):
                    opp_val = getattr(item, "activityecorelua_EStringToStringMapEntry", None)
                    
                    setattr(item, "activityecorelua_EStringToStringMapEntry", self)
                    

    @property
    def eAnnotations(self):
        return self.__eAnnotations

    @eAnnotations.setter
    def eAnnotations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EAnnotation__eAnnotations", None)
        self.__eAnnotations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EModelElement"):
                opp_val = getattr(old_value, "EModelElement", None)
                if opp_val == self:
                    setattr(old_value, "EModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EModelElement"):
                opp_val = getattr(value, "EModelElement", None)
                setattr(value, "EModelElement", self)

class activityecorelua_EDataType(EClassifier):

    def __init__(self, serializable: bool, activityecorelua_EDataType: "activityecorelua_EAttribute" = None):
        self.serializable = serializable
        self.activityecorelua_EDataType = activityecorelua_EDataType
        
    @property
    def serializable(self) -> bool:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: bool):
        self.__serializable = serializable

    @property
    def activityecorelua_EDataType(self):
        return self.__activityecorelua_EDataType

    @activityecorelua_EDataType.setter
    def activityecorelua_EDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EDataType__activityecorelua_EDataType", None)
        self.__activityecorelua_EDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EAttribute"):
                opp_val = getattr(old_value, "activityecorelua_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EAttribute"):
                opp_val = getattr(value, "activityecorelua_EAttribute", None)
                setattr(value, "activityecorelua_EAttribute", self)

class EStructuralFeature:

    pass
class activityecorelua_EReference(EStructuralFeature):

    def __init__(self, containment: bool, container: bool, resolveProxies: bool, activityecorelua_EReference: "activityecorelua_EClass" = None, activityecorelua_EReference18: "activityecorelua_EClass" = None, activityecorelua_EReference24: "activityecorelua_EClass" = None, activityecorelua_EReference75: "activityecorelua_EReference" = None, activityecorelua_EReference73: "activityecorelua_EReference" = None, activityecorelua_EReference77: "activityecorelua_EClass" = None, activityecorelua_EReference80: set["activityecorelua_EAttribute"] = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.activityecorelua_EReference = activityecorelua_EReference
        self.activityecorelua_EReference18 = activityecorelua_EReference18
        self.activityecorelua_EReference24 = activityecorelua_EReference24
        self.activityecorelua_EReference75 = activityecorelua_EReference75
        self.activityecorelua_EReference73 = activityecorelua_EReference73
        self.activityecorelua_EReference77 = activityecorelua_EReference77
        self.activityecorelua_EReference80 = activityecorelua_EReference80 if activityecorelua_EReference80 is not None else set()
        
    @property
    def containment(self) -> bool:
        return self.__containment

    @containment.setter
    def containment(self, containment: bool):
        self.__containment = containment

    @property
    def container(self) -> bool:
        return self.__container

    @container.setter
    def container(self, container: bool):
        self.__container = container

    @property
    def resolveProxies(self) -> bool:
        return self.__resolveProxies

    @resolveProxies.setter
    def resolveProxies(self, resolveProxies: bool):
        self.__resolveProxies = resolveProxies

    @property
    def activityecorelua_EReference77(self):
        return self.__activityecorelua_EReference77

    @activityecorelua_EReference77.setter
    def activityecorelua_EReference77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EReference__activityecorelua_EReference77", None)
        self.__activityecorelua_EReference77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EClass78"):
                opp_val = getattr(old_value, "activityecorelua_EClass78", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_EClass78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EClass78"):
                opp_val = getattr(value, "activityecorelua_EClass78", None)
                setattr(value, "activityecorelua_EClass78", self)

    @property
    def activityecorelua_EReference18(self):
        return self.__activityecorelua_EReference18

    @activityecorelua_EReference18.setter
    def activityecorelua_EReference18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EReference__activityecorelua_EReference18", None)
        self.__activityecorelua_EReference18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EClass17"):
                opp_val = getattr(old_value, "activityecorelua_EClass17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EClass17"):
                opp_val = getattr(value, "activityecorelua_EClass17", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EClass17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activityecorelua_EReference24(self):
        return self.__activityecorelua_EReference24

    @activityecorelua_EReference24.setter
    def activityecorelua_EReference24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EReference__activityecorelua_EReference24", None)
        self.__activityecorelua_EReference24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EClass23"):
                opp_val = getattr(old_value, "activityecorelua_EClass23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EClass23"):
                opp_val = getattr(value, "activityecorelua_EClass23", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EClass23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activityecorelua_EReference(self):
        return self.__activityecorelua_EReference

    @activityecorelua_EReference.setter
    def activityecorelua_EReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EReference__activityecorelua_EReference", None)
        self.__activityecorelua_EReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EClass15"):
                opp_val = getattr(old_value, "activityecorelua_EClass15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EClass15"):
                opp_val = getattr(value, "activityecorelua_EClass15", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EClass15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activityecorelua_EReference80(self):
        return self.__activityecorelua_EReference80

    @activityecorelua_EReference80.setter
    def activityecorelua_EReference80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EReference__activityecorelua_EReference80", None)
        self.__activityecorelua_EReference80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "activityecorelua_EAttribute81"):
                    opp_val = getattr(item, "activityecorelua_EAttribute81", None)
                    
                    if opp_val == self:
                        setattr(item, "activityecorelua_EAttribute81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "activityecorelua_EAttribute81"):
                    opp_val = getattr(item, "activityecorelua_EAttribute81", None)
                    
                    setattr(item, "activityecorelua_EAttribute81", self)
                    

    @property
    def activityecorelua_EReference75(self):
        return self.__activityecorelua_EReference75

    @activityecorelua_EReference75.setter
    def activityecorelua_EReference75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EReference__activityecorelua_EReference75", None)
        self.__activityecorelua_EReference75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EReference73"):
                opp_val = getattr(old_value, "activityecorelua_EReference73", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_EReference73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EReference73"):
                opp_val = getattr(value, "activityecorelua_EReference73", None)
                setattr(value, "activityecorelua_EReference73", self)

    @property
    def activityecorelua_EReference73(self):
        return self.__activityecorelua_EReference73

    @activityecorelua_EReference73.setter
    def activityecorelua_EReference73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EReference__activityecorelua_EReference73", None)
        self.__activityecorelua_EReference73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EReference75"):
                opp_val = getattr(old_value, "activityecorelua_EReference75", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_EReference75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EReference75"):
                opp_val = getattr(value, "activityecorelua_EReference75", None)
                setattr(value, "activityecorelua_EReference75", self)

class activityecorelua_EAttribute(EStructuralFeature):

    def __init__(self, iD: bool, activityecorelua_EAttribute: "activityecorelua_EDataType" = None, activityecorelua_EAttribute13: "activityecorelua_EClass" = None, activityecorelua_EAttribute21: "activityecorelua_EClass" = None, activityecorelua_EAttribute34: "activityecorelua_EClass" = None, activityecorelua_EAttribute81: "activityecorelua_EReference" = None):
        self.iD = iD
        self.activityecorelua_EAttribute = activityecorelua_EAttribute
        self.activityecorelua_EAttribute13 = activityecorelua_EAttribute13
        self.activityecorelua_EAttribute21 = activityecorelua_EAttribute21
        self.activityecorelua_EAttribute34 = activityecorelua_EAttribute34
        self.activityecorelua_EAttribute81 = activityecorelua_EAttribute81
        
    @property
    def iD(self) -> bool:
        return self.__iD

    @iD.setter
    def iD(self, iD: bool):
        self.__iD = iD

    @property
    def activityecorelua_EAttribute21(self):
        return self.__activityecorelua_EAttribute21

    @activityecorelua_EAttribute21.setter
    def activityecorelua_EAttribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EAttribute__activityecorelua_EAttribute21", None)
        self.__activityecorelua_EAttribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EClass20"):
                opp_val = getattr(old_value, "activityecorelua_EClass20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EClass20"):
                opp_val = getattr(value, "activityecorelua_EClass20", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EClass20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activityecorelua_EAttribute81(self):
        return self.__activityecorelua_EAttribute81

    @activityecorelua_EAttribute81.setter
    def activityecorelua_EAttribute81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EAttribute__activityecorelua_EAttribute81", None)
        self.__activityecorelua_EAttribute81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EReference80"):
                opp_val = getattr(old_value, "activityecorelua_EReference80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EReference80"):
                opp_val = getattr(value, "activityecorelua_EReference80", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EReference80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activityecorelua_EAttribute34(self):
        return self.__activityecorelua_EAttribute34

    @activityecorelua_EAttribute34.setter
    def activityecorelua_EAttribute34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EAttribute__activityecorelua_EAttribute34", None)
        self.__activityecorelua_EAttribute34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EClass33"):
                opp_val = getattr(old_value, "activityecorelua_EClass33", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_EClass33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EClass33"):
                opp_val = getattr(value, "activityecorelua_EClass33", None)
                setattr(value, "activityecorelua_EClass33", self)

    @property
    def activityecorelua_EAttribute(self):
        return self.__activityecorelua_EAttribute

    @activityecorelua_EAttribute.setter
    def activityecorelua_EAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EAttribute__activityecorelua_EAttribute", None)
        self.__activityecorelua_EAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EDataType"):
                opp_val = getattr(old_value, "activityecorelua_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "activityecorelua_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EDataType"):
                opp_val = getattr(value, "activityecorelua_EDataType", None)
                setattr(value, "activityecorelua_EDataType", self)

    @property
    def activityecorelua_EAttribute13(self):
        return self.__activityecorelua_EAttribute13

    @activityecorelua_EAttribute13.setter
    def activityecorelua_EAttribute13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_activityecorelua_EAttribute__activityecorelua_EAttribute13", None)
        self.__activityecorelua_EAttribute13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activityecorelua_EClass12"):
                opp_val = getattr(old_value, "activityecorelua_EClass12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activityecorelua_EClass12"):
                opp_val = getattr(value, "activityecorelua_EClass12", None)
                if opp_val is None:
                    setattr(value, "activityecorelua_EClass12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
