from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lua_Environment:

    def __init__(self, lua_Environment: "lua_Environment" = None, lua_Environment179: "lua_Environment" = None):
        self.lua_Environment = lua_Environment
        self.lua_Environment179 = lua_Environment179
        
    @property
    def lua_Environment(self):
        return self.__lua_Environment

    @lua_Environment.setter
    def lua_Environment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Environment__lua_Environment", None)
        self.__lua_Environment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Environment179"):
                opp_val = getattr(old_value, "lua_Environment179", None)
                if opp_val == self:
                    setattr(old_value, "lua_Environment179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Environment179"):
                opp_val = getattr(value, "lua_Environment179", None)
                setattr(value, "lua_Environment179", self)

    @property
    def lua_Environment179(self):
        return self.__lua_Environment179

    @lua_Environment179.setter
    def lua_Environment179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Environment__lua_Environment179", None)
        self.__lua_Environment179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Environment"):
                opp_val = getattr(old_value, "lua_Environment", None)
                if opp_val == self:
                    setattr(old_value, "lua_Environment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Environment"):
                opp_val = getattr(value, "lua_Environment", None)
                setattr(value, "lua_Environment", self)

    def putAllVariables(self, v: str):
        # TODO: Implement putAllVariables method
        pass

    def getVariables(self):
        # TODO: Implement getVariables method
        pass

    def getValues(self) -> str:
        # TODO: Implement getValues method
        pass

    def getFunctions(self):
        # TODO: Implement getFunctions method
        pass

    def putVariable(self, s: str, o: str):
        # TODO: Implement putVariable method
        pass

    def putFunction(self, s: str, f: str):
        # TODO: Implement putFunction method
        pass

    def pushAllValues(self, v: str):
        # TODO: Implement pushAllValues method
        pass

    def popValue(self) -> str:
        # TODO: Implement popValue method
        pass

    def putAllFunctions(self, f: str):
        # TODO: Implement putAllFunctions method
        pass

    def pushValue(self, o: str):
        # TODO: Implement pushValue method
        pass

    def getVariable(self, s: str) -> str:
        # TODO: Implement getVariable method
        pass

    def getFunction(self, s: str) -> str:
        # TODO: Implement getFunction method
        pass

class LastStatement_Return:

    pass
class lua_LastStatement_ReturnWithValue(LastStatement_Return):

    def __init__(self, lua_LastStatement_ReturnWithValue: set["lua_Expression"] = None):
        self.lua_LastStatement_ReturnWithValue = lua_LastStatement_ReturnWithValue if lua_LastStatement_ReturnWithValue is not None else set()
        
    @property
    def lua_LastStatement_ReturnWithValue(self):
        return self.__lua_LastStatement_ReturnWithValue

    @lua_LastStatement_ReturnWithValue.setter
    def lua_LastStatement_ReturnWithValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_LastStatement_ReturnWithValue__lua_LastStatement_ReturnWithValue", None)
        self.__lua_LastStatement_ReturnWithValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lua_Expression65"):
                    opp_val = getattr(item, "lua_Expression65", None)
                    
                    if opp_val == self:
                        setattr(item, "lua_Expression65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lua_Expression65"):
                    opp_val = getattr(item, "lua_Expression65", None)
                    
                    setattr(item, "lua_Expression65", self)
                    

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Field:

    def __init__(self, lua_Field60: "lua_Expression" = None, lua_Field: "lua_Expression_TableConstructor" = None):
        self.lua_Field60 = lua_Field60
        self.lua_Field = lua_Field
        
    @property
    def lua_Field60(self):
        return self.__lua_Field60

    @lua_Field60.setter
    def lua_Field60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Field__lua_Field60", None)
        self.__lua_Field60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression61"):
                opp_val = getattr(old_value, "lua_Expression61", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression61"):
                opp_val = getattr(value, "lua_Expression61", None)
                setattr(value, "lua_Expression61", self)

    @property
    def lua_Field(self):
        return self.__lua_Field

    @lua_Field.setter
    def lua_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Field__lua_Field", None)
        self.__lua_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_TableConstructor"):
                opp_val = getattr(old_value, "lua_Expression_TableConstructor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_TableConstructor"):
                opp_val = getattr(value, "lua_Expression_TableConstructor", None)
                if opp_val is None:
                    setattr(value, "lua_Expression_TableConstructor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def execute(self, c: str):
        # TODO: Implement execute method
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

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Field_AppendEntryToTable(Field):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Field_AddEntryToTable_Brackets(Field):

    def __init__(self, lua_Field_AddEntryToTable_Brackets: "lua_Expression" = None):
        self.lua_Field_AddEntryToTable_Brackets = lua_Field_AddEntryToTable_Brackets
        
    @property
    def lua_Field_AddEntryToTable_Brackets(self):
        return self.__lua_Field_AddEntryToTable_Brackets

    @lua_Field_AddEntryToTable_Brackets.setter
    def lua_Field_AddEntryToTable_Brackets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Field_AddEntryToTable_Brackets__lua_Field_AddEntryToTable_Brackets", None)
        self.__lua_Field_AddEntryToTable_Brackets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression63"):
                opp_val = getattr(old_value, "lua_Expression63", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression63"):
                opp_val = getattr(value, "lua_Expression63", None)
                setattr(value, "lua_Expression63", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Functioncall_Arguments:

    def __init__(self, lua_Functioncall_Arguments: set["lua_Expression"] = None, lua_Functioncall_Arguments80: "lua_Statement_CallFunction" = None, lua_Functioncall_Arguments75: "lua_Statement_CallMemberFunction" = None, lua_Functioncall_Arguments166: "lua_Expression_CallMemberFunction" = None, lua_Functioncall_Arguments171: "lua_Expression_CallFunction" = None):
        self.lua_Functioncall_Arguments = lua_Functioncall_Arguments if lua_Functioncall_Arguments is not None else set()
        self.lua_Functioncall_Arguments80 = lua_Functioncall_Arguments80
        self.lua_Functioncall_Arguments75 = lua_Functioncall_Arguments75
        self.lua_Functioncall_Arguments166 = lua_Functioncall_Arguments166
        self.lua_Functioncall_Arguments171 = lua_Functioncall_Arguments171
        
    @property
    def lua_Functioncall_Arguments(self):
        return self.__lua_Functioncall_Arguments

    @lua_Functioncall_Arguments.setter
    def lua_Functioncall_Arguments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Functioncall_Arguments__lua_Functioncall_Arguments", None)
        self.__lua_Functioncall_Arguments = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lua_Expression58"):
                    opp_val = getattr(item, "lua_Expression58", None)
                    
                    if opp_val == self:
                        setattr(item, "lua_Expression58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lua_Expression58"):
                    opp_val = getattr(item, "lua_Expression58", None)
                    
                    setattr(item, "lua_Expression58", self)
                    

    @property
    def lua_Functioncall_Arguments171(self):
        return self.__lua_Functioncall_Arguments171

    @lua_Functioncall_Arguments171.setter
    def lua_Functioncall_Arguments171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Functioncall_Arguments__lua_Functioncall_Arguments171", None)
        self.__lua_Functioncall_Arguments171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_CallFunction170"):
                opp_val = getattr(old_value, "lua_Expression_CallFunction170", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_CallFunction170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_CallFunction170"):
                opp_val = getattr(value, "lua_Expression_CallFunction170", None)
                setattr(value, "lua_Expression_CallFunction170", self)

    @property
    def lua_Functioncall_Arguments75(self):
        return self.__lua_Functioncall_Arguments75

    @lua_Functioncall_Arguments75.setter
    def lua_Functioncall_Arguments75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Functioncall_Arguments__lua_Functioncall_Arguments75", None)
        self.__lua_Functioncall_Arguments75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_CallMemberFunction74"):
                opp_val = getattr(old_value, "lua_Statement_CallMemberFunction74", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_CallMemberFunction74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_CallMemberFunction74"):
                opp_val = getattr(value, "lua_Statement_CallMemberFunction74", None)
                setattr(value, "lua_Statement_CallMemberFunction74", self)

    @property
    def lua_Functioncall_Arguments80(self):
        return self.__lua_Functioncall_Arguments80

    @lua_Functioncall_Arguments80.setter
    def lua_Functioncall_Arguments80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Functioncall_Arguments__lua_Functioncall_Arguments80", None)
        self.__lua_Functioncall_Arguments80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_CallFunction79"):
                opp_val = getattr(old_value, "lua_Statement_CallFunction79", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_CallFunction79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_CallFunction79"):
                opp_val = getattr(value, "lua_Statement_CallFunction79", None)
                setattr(value, "lua_Statement_CallFunction79", self)

    @property
    def lua_Functioncall_Arguments166(self):
        return self.__lua_Functioncall_Arguments166

    @lua_Functioncall_Arguments166.setter
    def lua_Functioncall_Arguments166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Functioncall_Arguments__lua_Functioncall_Arguments166", None)
        self.__lua_Functioncall_Arguments166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_CallMemberFunction165"):
                opp_val = getattr(old_value, "lua_Expression_CallMemberFunction165", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_CallMemberFunction165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_CallMemberFunction165"):
                opp_val = getattr(value, "lua_Expression_CallMemberFunction165", None)
                setattr(value, "lua_Expression_CallMemberFunction165", self)

    def execute(self, c: str):
        # TODO: Implement execute method
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

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Expression:

    pass
class lua_Expression_CallFunction(Expression):

    def __init__(self, lua_Expression_CallFunction: "lua_Expression" = None, lua_Expression_CallFunction170: "lua_Functioncall_Arguments" = None):
        self.lua_Expression_CallFunction = lua_Expression_CallFunction
        self.lua_Expression_CallFunction170 = lua_Expression_CallFunction170
        
    @property
    def lua_Expression_CallFunction170(self):
        return self.__lua_Expression_CallFunction170

    @lua_Expression_CallFunction170.setter
    def lua_Expression_CallFunction170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_CallFunction__lua_Expression_CallFunction170", None)
        self.__lua_Expression_CallFunction170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Functioncall_Arguments171"):
                opp_val = getattr(old_value, "lua_Functioncall_Arguments171", None)
                if opp_val == self:
                    setattr(old_value, "lua_Functioncall_Arguments171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Functioncall_Arguments171"):
                opp_val = getattr(value, "lua_Functioncall_Arguments171", None)
                setattr(value, "lua_Functioncall_Arguments171", self)

    @property
    def lua_Expression_CallFunction(self):
        return self.__lua_Expression_CallFunction

    @lua_Expression_CallFunction.setter
    def lua_Expression_CallFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_CallFunction__lua_Expression_CallFunction", None)
        self.__lua_Expression_CallFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression168"):
                opp_val = getattr(old_value, "lua_Expression168", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression168"):
                opp_val = getattr(value, "lua_Expression168", None)
                setattr(value, "lua_Expression168", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Not_Equal(Expression):

    def __init__(self, lua_Expression_Not_Equal: "lua_Expression" = None, lua_Expression_Not_Equal119: "lua_Expression" = None):
        self.lua_Expression_Not_Equal = lua_Expression_Not_Equal
        self.lua_Expression_Not_Equal119 = lua_Expression_Not_Equal119
        
    @property
    def lua_Expression_Not_Equal(self):
        return self.__lua_Expression_Not_Equal

    @lua_Expression_Not_Equal.setter
    def lua_Expression_Not_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Not_Equal__lua_Expression_Not_Equal", None)
        self.__lua_Expression_Not_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression117"):
                opp_val = getattr(old_value, "lua_Expression117", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression117"):
                opp_val = getattr(value, "lua_Expression117", None)
                setattr(value, "lua_Expression117", self)

    @property
    def lua_Expression_Not_Equal119(self):
        return self.__lua_Expression_Not_Equal119

    @lua_Expression_Not_Equal119.setter
    def lua_Expression_Not_Equal119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Not_Equal__lua_Expression_Not_Equal119", None)
        self.__lua_Expression_Not_Equal119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression120"):
                opp_val = getattr(old_value, "lua_Expression120", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression120"):
                opp_val = getattr(value, "lua_Expression120", None)
                setattr(value, "lua_Expression120", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Or(Expression):

    def __init__(self, lua_Expression_Or: "lua_Expression" = None, lua_Expression_Or84: "lua_Expression" = None):
        self.lua_Expression_Or = lua_Expression_Or
        self.lua_Expression_Or84 = lua_Expression_Or84
        
    @property
    def lua_Expression_Or84(self):
        return self.__lua_Expression_Or84

    @lua_Expression_Or84.setter
    def lua_Expression_Or84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Or__lua_Expression_Or84", None)
        self.__lua_Expression_Or84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression85"):
                opp_val = getattr(old_value, "lua_Expression85", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression85"):
                opp_val = getattr(value, "lua_Expression85", None)
                setattr(value, "lua_Expression85", self)

    @property
    def lua_Expression_Or(self):
        return self.__lua_Expression_Or

    @lua_Expression_Or.setter
    def lua_Expression_Or(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Or__lua_Expression_Or", None)
        self.__lua_Expression_Or = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression82"):
                opp_val = getattr(old_value, "lua_Expression82", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression82"):
                opp_val = getattr(value, "lua_Expression82", None)
                setattr(value, "lua_Expression82", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Concatenation(Expression):

    def __init__(self, lua_Expression_Concatenation: "lua_Expression" = None, lua_Expression_Concatenation124: "lua_Expression" = None):
        self.lua_Expression_Concatenation = lua_Expression_Concatenation
        self.lua_Expression_Concatenation124 = lua_Expression_Concatenation124
        
    @property
    def lua_Expression_Concatenation124(self):
        return self.__lua_Expression_Concatenation124

    @lua_Expression_Concatenation124.setter
    def lua_Expression_Concatenation124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Concatenation__lua_Expression_Concatenation124", None)
        self.__lua_Expression_Concatenation124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression125"):
                opp_val = getattr(old_value, "lua_Expression125", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression125"):
                opp_val = getattr(value, "lua_Expression125", None)
                setattr(value, "lua_Expression125", self)

    @property
    def lua_Expression_Concatenation(self):
        return self.__lua_Expression_Concatenation

    @lua_Expression_Concatenation.setter
    def lua_Expression_Concatenation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Concatenation__lua_Expression_Concatenation", None)
        self.__lua_Expression_Concatenation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression122"):
                opp_val = getattr(old_value, "lua_Expression122", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression122"):
                opp_val = getattr(value, "lua_Expression122", None)
                setattr(value, "lua_Expression122", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Plus(Expression):

    def __init__(self, lua_Expression_Plus: "lua_Expression" = None, lua_Expression_Plus129: "lua_Expression" = None):
        self.lua_Expression_Plus = lua_Expression_Plus
        self.lua_Expression_Plus129 = lua_Expression_Plus129
        
    @property
    def lua_Expression_Plus(self):
        return self.__lua_Expression_Plus

    @lua_Expression_Plus.setter
    def lua_Expression_Plus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Plus__lua_Expression_Plus", None)
        self.__lua_Expression_Plus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression127"):
                opp_val = getattr(old_value, "lua_Expression127", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression127"):
                opp_val = getattr(value, "lua_Expression127", None)
                setattr(value, "lua_Expression127", self)

    @property
    def lua_Expression_Plus129(self):
        return self.__lua_Expression_Plus129

    @lua_Expression_Plus129.setter
    def lua_Expression_Plus129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Plus__lua_Expression_Plus129", None)
        self.__lua_Expression_Plus129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression130"):
                opp_val = getattr(old_value, "lua_Expression130", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression130"):
                opp_val = getattr(value, "lua_Expression130", None)
                setattr(value, "lua_Expression130", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_TableConstructor(Expression):

    def __init__(self, lua_Expression_TableConstructor: set["lua_Field"] = None):
        self.lua_Expression_TableConstructor = lua_Expression_TableConstructor if lua_Expression_TableConstructor is not None else set()
        
    @property
    def lua_Expression_TableConstructor(self):
        return self.__lua_Expression_TableConstructor

    @lua_Expression_TableConstructor.setter
    def lua_Expression_TableConstructor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_TableConstructor__lua_Expression_TableConstructor", None)
        self.__lua_Expression_TableConstructor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lua_Field"):
                    opp_val = getattr(item, "lua_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "lua_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lua_Field"):
                    opp_val = getattr(item, "lua_Field", None)
                    
                    setattr(item, "lua_Field", self)
                    

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_VarArgs(Expression):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
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

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Smaller(Expression):

    def __init__(self, lua_Expression_Smaller104: "lua_Expression" = None, lua_Expression_Smaller: "lua_Expression" = None):
        self.lua_Expression_Smaller104 = lua_Expression_Smaller104
        self.lua_Expression_Smaller = lua_Expression_Smaller
        
    @property
    def lua_Expression_Smaller(self):
        return self.__lua_Expression_Smaller

    @lua_Expression_Smaller.setter
    def lua_Expression_Smaller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Smaller__lua_Expression_Smaller", None)
        self.__lua_Expression_Smaller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression102"):
                opp_val = getattr(old_value, "lua_Expression102", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression102"):
                opp_val = getattr(value, "lua_Expression102", None)
                setattr(value, "lua_Expression102", self)

    @property
    def lua_Expression_Smaller104(self):
        return self.__lua_Expression_Smaller104

    @lua_Expression_Smaller104.setter
    def lua_Expression_Smaller104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Smaller__lua_Expression_Smaller104", None)
        self.__lua_Expression_Smaller104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression105"):
                opp_val = getattr(old_value, "lua_Expression105", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression105"):
                opp_val = getattr(value, "lua_Expression105", None)
                setattr(value, "lua_Expression105", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Negate(Expression):

    def __init__(self, lua_Expression_Negate: "lua_Expression" = None):
        self.lua_Expression_Negate = lua_Expression_Negate
        
    @property
    def lua_Expression_Negate(self):
        return self.__lua_Expression_Negate

    @lua_Expression_Negate.setter
    def lua_Expression_Negate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Negate__lua_Expression_Negate", None)
        self.__lua_Expression_Negate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression152"):
                opp_val = getattr(old_value, "lua_Expression152", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression152"):
                opp_val = getattr(value, "lua_Expression152", None)
                setattr(value, "lua_Expression152", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Smaller_Equal(Expression):

    def __init__(self, lua_Expression_Smaller_Equal: "lua_Expression" = None, lua_Expression_Smaller_Equal109: "lua_Expression" = None):
        self.lua_Expression_Smaller_Equal = lua_Expression_Smaller_Equal
        self.lua_Expression_Smaller_Equal109 = lua_Expression_Smaller_Equal109
        
    @property
    def lua_Expression_Smaller_Equal(self):
        return self.__lua_Expression_Smaller_Equal

    @lua_Expression_Smaller_Equal.setter
    def lua_Expression_Smaller_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Smaller_Equal__lua_Expression_Smaller_Equal", None)
        self.__lua_Expression_Smaller_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression107"):
                opp_val = getattr(old_value, "lua_Expression107", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression107"):
                opp_val = getattr(value, "lua_Expression107", None)
                setattr(value, "lua_Expression107", self)

    @property
    def lua_Expression_Smaller_Equal109(self):
        return self.__lua_Expression_Smaller_Equal109

    @lua_Expression_Smaller_Equal109.setter
    def lua_Expression_Smaller_Equal109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Smaller_Equal__lua_Expression_Smaller_Equal109", None)
        self.__lua_Expression_Smaller_Equal109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression110"):
                opp_val = getattr(old_value, "lua_Expression110", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression110"):
                opp_val = getattr(value, "lua_Expression110", None)
                setattr(value, "lua_Expression110", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Minus(Expression):

    def __init__(self, lua_Expression_Minus: "lua_Expression" = None, lua_Expression_Minus134: "lua_Expression" = None):
        self.lua_Expression_Minus = lua_Expression_Minus
        self.lua_Expression_Minus134 = lua_Expression_Minus134
        
    @property
    def lua_Expression_Minus(self):
        return self.__lua_Expression_Minus

    @lua_Expression_Minus.setter
    def lua_Expression_Minus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Minus__lua_Expression_Minus", None)
        self.__lua_Expression_Minus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression132"):
                opp_val = getattr(old_value, "lua_Expression132", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression132"):
                opp_val = getattr(value, "lua_Expression132", None)
                setattr(value, "lua_Expression132", self)

    @property
    def lua_Expression_Minus134(self):
        return self.__lua_Expression_Minus134

    @lua_Expression_Minus134.setter
    def lua_Expression_Minus134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Minus__lua_Expression_Minus134", None)
        self.__lua_Expression_Minus134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression135"):
                opp_val = getattr(old_value, "lua_Expression135", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression135"):
                opp_val = getattr(value, "lua_Expression135", None)
                setattr(value, "lua_Expression135", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Function(Expression):

    def __init__(self, lua_Expression_Function: "lua_Function" = None):
        self.lua_Expression_Function = lua_Expression_Function
        
    @property
    def lua_Expression_Function(self):
        return self.__lua_Expression_Function

    @lua_Expression_Function.setter
    def lua_Expression_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Function__lua_Expression_Function", None)
        self.__lua_Expression_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Function52"):
                opp_val = getattr(old_value, "lua_Function52", None)
                if opp_val == self:
                    setattr(old_value, "lua_Function52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Function52"):
                opp_val = getattr(value, "lua_Function52", None)
                setattr(value, "lua_Function52", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Invert(Expression):

    def __init__(self, lua_Expression_Invert: "lua_Expression" = None):
        self.lua_Expression_Invert = lua_Expression_Invert
        
    @property
    def lua_Expression_Invert(self):
        return self.__lua_Expression_Invert

    @lua_Expression_Invert.setter
    def lua_Expression_Invert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Invert__lua_Expression_Invert", None)
        self.__lua_Expression_Invert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression156"):
                opp_val = getattr(old_value, "lua_Expression156", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression156"):
                opp_val = getattr(value, "lua_Expression156", None)
                setattr(value, "lua_Expression156", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_True(Expression):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Division(Expression):

    def __init__(self, lua_Expression_Division144: "lua_Expression" = None, lua_Expression_Division: "lua_Expression" = None):
        self.lua_Expression_Division144 = lua_Expression_Division144
        self.lua_Expression_Division = lua_Expression_Division
        
    @property
    def lua_Expression_Division144(self):
        return self.__lua_Expression_Division144

    @lua_Expression_Division144.setter
    def lua_Expression_Division144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Division__lua_Expression_Division144", None)
        self.__lua_Expression_Division144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression145"):
                opp_val = getattr(old_value, "lua_Expression145", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression145"):
                opp_val = getattr(value, "lua_Expression145", None)
                setattr(value, "lua_Expression145", self)

    @property
    def lua_Expression_Division(self):
        return self.__lua_Expression_Division

    @lua_Expression_Division.setter
    def lua_Expression_Division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Division__lua_Expression_Division", None)
        self.__lua_Expression_Division = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression142"):
                opp_val = getattr(old_value, "lua_Expression142", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression142"):
                opp_val = getattr(value, "lua_Expression142", None)
                setattr(value, "lua_Expression142", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_String(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Larger_Equal(Expression):

    def __init__(self, lua_Expression_Larger_Equal: "lua_Expression" = None, lua_Expression_Larger_Equal99: "lua_Expression" = None):
        self.lua_Expression_Larger_Equal = lua_Expression_Larger_Equal
        self.lua_Expression_Larger_Equal99 = lua_Expression_Larger_Equal99
        
    @property
    def lua_Expression_Larger_Equal(self):
        return self.__lua_Expression_Larger_Equal

    @lua_Expression_Larger_Equal.setter
    def lua_Expression_Larger_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Larger_Equal__lua_Expression_Larger_Equal", None)
        self.__lua_Expression_Larger_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression97"):
                opp_val = getattr(old_value, "lua_Expression97", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression97"):
                opp_val = getattr(value, "lua_Expression97", None)
                setattr(value, "lua_Expression97", self)

    @property
    def lua_Expression_Larger_Equal99(self):
        return self.__lua_Expression_Larger_Equal99

    @lua_Expression_Larger_Equal99.setter
    def lua_Expression_Larger_Equal99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Larger_Equal__lua_Expression_Larger_Equal99", None)
        self.__lua_Expression_Larger_Equal99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression100"):
                opp_val = getattr(old_value, "lua_Expression100", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression100"):
                opp_val = getattr(value, "lua_Expression100", None)
                setattr(value, "lua_Expression100", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Larger(Expression):

    def __init__(self, lua_Expression_Larger: "lua_Expression" = None, lua_Expression_Larger94: "lua_Expression" = None):
        self.lua_Expression_Larger = lua_Expression_Larger
        self.lua_Expression_Larger94 = lua_Expression_Larger94
        
    @property
    def lua_Expression_Larger94(self):
        return self.__lua_Expression_Larger94

    @lua_Expression_Larger94.setter
    def lua_Expression_Larger94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Larger__lua_Expression_Larger94", None)
        self.__lua_Expression_Larger94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression95"):
                opp_val = getattr(old_value, "lua_Expression95", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression95"):
                opp_val = getattr(value, "lua_Expression95", None)
                setattr(value, "lua_Expression95", self)

    @property
    def lua_Expression_Larger(self):
        return self.__lua_Expression_Larger

    @lua_Expression_Larger.setter
    def lua_Expression_Larger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Larger__lua_Expression_Larger", None)
        self.__lua_Expression_Larger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression92"):
                opp_val = getattr(old_value, "lua_Expression92", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression92"):
                opp_val = getattr(value, "lua_Expression92", None)
                setattr(value, "lua_Expression92", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_AccessArray(Expression):

    def __init__(self, lua_Expression_AccessArray: "lua_Expression" = None, lua_Expression_AccessArray175: "lua_Expression" = None):
        self.lua_Expression_AccessArray = lua_Expression_AccessArray
        self.lua_Expression_AccessArray175 = lua_Expression_AccessArray175
        
    @property
    def lua_Expression_AccessArray175(self):
        return self.__lua_Expression_AccessArray175

    @lua_Expression_AccessArray175.setter
    def lua_Expression_AccessArray175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_AccessArray__lua_Expression_AccessArray175", None)
        self.__lua_Expression_AccessArray175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression176"):
                opp_val = getattr(old_value, "lua_Expression176", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression176"):
                opp_val = getattr(value, "lua_Expression176", None)
                setattr(value, "lua_Expression176", self)

    @property
    def lua_Expression_AccessArray(self):
        return self.__lua_Expression_AccessArray

    @lua_Expression_AccessArray.setter
    def lua_Expression_AccessArray(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_AccessArray__lua_Expression_AccessArray", None)
        self.__lua_Expression_AccessArray = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression173"):
                opp_val = getattr(old_value, "lua_Expression173", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression173"):
                opp_val = getattr(value, "lua_Expression173", None)
                setattr(value, "lua_Expression173", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_And(Expression):

    def __init__(self, lua_Expression_And: "lua_Expression" = None, lua_Expression_And89: "lua_Expression" = None):
        self.lua_Expression_And = lua_Expression_And
        self.lua_Expression_And89 = lua_Expression_And89
        
    @property
    def lua_Expression_And(self):
        return self.__lua_Expression_And

    @lua_Expression_And.setter
    def lua_Expression_And(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_And__lua_Expression_And", None)
        self.__lua_Expression_And = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression87"):
                opp_val = getattr(old_value, "lua_Expression87", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression87"):
                opp_val = getattr(value, "lua_Expression87", None)
                setattr(value, "lua_Expression87", self)

    @property
    def lua_Expression_And89(self):
        return self.__lua_Expression_And89

    @lua_Expression_And89.setter
    def lua_Expression_And89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_And__lua_Expression_And89", None)
        self.__lua_Expression_And89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression90"):
                opp_val = getattr(old_value, "lua_Expression90", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression90"):
                opp_val = getattr(value, "lua_Expression90", None)
                setattr(value, "lua_Expression90", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Multiplication(Expression):

    def __init__(self, lua_Expression_Multiplication: "lua_Expression" = None, lua_Expression_Multiplication139: "lua_Expression" = None):
        self.lua_Expression_Multiplication = lua_Expression_Multiplication
        self.lua_Expression_Multiplication139 = lua_Expression_Multiplication139
        
    @property
    def lua_Expression_Multiplication(self):
        return self.__lua_Expression_Multiplication

    @lua_Expression_Multiplication.setter
    def lua_Expression_Multiplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Multiplication__lua_Expression_Multiplication", None)
        self.__lua_Expression_Multiplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression137"):
                opp_val = getattr(old_value, "lua_Expression137", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression137"):
                opp_val = getattr(value, "lua_Expression137", None)
                setattr(value, "lua_Expression137", self)

    @property
    def lua_Expression_Multiplication139(self):
        return self.__lua_Expression_Multiplication139

    @lua_Expression_Multiplication139.setter
    def lua_Expression_Multiplication139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Multiplication__lua_Expression_Multiplication139", None)
        self.__lua_Expression_Multiplication139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression140"):
                opp_val = getattr(old_value, "lua_Expression140", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression140"):
                opp_val = getattr(value, "lua_Expression140", None)
                setattr(value, "lua_Expression140", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Length(Expression):

    def __init__(self, lua_Expression_Length: "lua_Expression" = None):
        self.lua_Expression_Length = lua_Expression_Length
        
    @property
    def lua_Expression_Length(self):
        return self.__lua_Expression_Length

    @lua_Expression_Length.setter
    def lua_Expression_Length(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Length__lua_Expression_Length", None)
        self.__lua_Expression_Length = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression154"):
                opp_val = getattr(old_value, "lua_Expression154", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression154"):
                opp_val = getattr(value, "lua_Expression154", None)
                setattr(value, "lua_Expression154", self)

    def execute(self, c: str):
        # TODO: Implement execute method
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

    def execute(self, c: str):
        # TODO: Implement execute method
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

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Equal(Expression):

    def __init__(self, lua_Expression_Equal: "lua_Expression" = None, lua_Expression_Equal114: "lua_Expression" = None):
        self.lua_Expression_Equal = lua_Expression_Equal
        self.lua_Expression_Equal114 = lua_Expression_Equal114
        
    @property
    def lua_Expression_Equal114(self):
        return self.__lua_Expression_Equal114

    @lua_Expression_Equal114.setter
    def lua_Expression_Equal114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Equal__lua_Expression_Equal114", None)
        self.__lua_Expression_Equal114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression115"):
                opp_val = getattr(old_value, "lua_Expression115", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression115"):
                opp_val = getattr(value, "lua_Expression115", None)
                setattr(value, "lua_Expression115", self)

    @property
    def lua_Expression_Equal(self):
        return self.__lua_Expression_Equal

    @lua_Expression_Equal.setter
    def lua_Expression_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Equal__lua_Expression_Equal", None)
        self.__lua_Expression_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression112"):
                opp_val = getattr(old_value, "lua_Expression112", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression112"):
                opp_val = getattr(value, "lua_Expression112", None)
                setattr(value, "lua_Expression112", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Exponentiation(Expression):

    def __init__(self, lua_Expression_Exponentiation: "lua_Expression" = None, lua_Expression_Exponentiation160: "lua_Expression" = None):
        self.lua_Expression_Exponentiation = lua_Expression_Exponentiation
        self.lua_Expression_Exponentiation160 = lua_Expression_Exponentiation160
        
    @property
    def lua_Expression_Exponentiation160(self):
        return self.__lua_Expression_Exponentiation160

    @lua_Expression_Exponentiation160.setter
    def lua_Expression_Exponentiation160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Exponentiation__lua_Expression_Exponentiation160", None)
        self.__lua_Expression_Exponentiation160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression161"):
                opp_val = getattr(old_value, "lua_Expression161", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression161"):
                opp_val = getattr(value, "lua_Expression161", None)
                setattr(value, "lua_Expression161", self)

    @property
    def lua_Expression_Exponentiation(self):
        return self.__lua_Expression_Exponentiation

    @lua_Expression_Exponentiation.setter
    def lua_Expression_Exponentiation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Exponentiation__lua_Expression_Exponentiation", None)
        self.__lua_Expression_Exponentiation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression158"):
                opp_val = getattr(old_value, "lua_Expression158", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression158"):
                opp_val = getattr(value, "lua_Expression158", None)
                setattr(value, "lua_Expression158", self)

    def execute(self, c: str):
        # TODO: Implement execute method
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

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Modulo(Expression):

    def __init__(self, lua_Expression_Modulo: "lua_Expression" = None, lua_Expression_Modulo149: "lua_Expression" = None):
        self.lua_Expression_Modulo = lua_Expression_Modulo
        self.lua_Expression_Modulo149 = lua_Expression_Modulo149
        
    @property
    def lua_Expression_Modulo149(self):
        return self.__lua_Expression_Modulo149

    @lua_Expression_Modulo149.setter
    def lua_Expression_Modulo149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Modulo__lua_Expression_Modulo149", None)
        self.__lua_Expression_Modulo149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression150"):
                opp_val = getattr(old_value, "lua_Expression150", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression150"):
                opp_val = getattr(value, "lua_Expression150", None)
                setattr(value, "lua_Expression150", self)

    @property
    def lua_Expression_Modulo(self):
        return self.__lua_Expression_Modulo

    @lua_Expression_Modulo.setter
    def lua_Expression_Modulo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression_Modulo__lua_Expression_Modulo", None)
        self.__lua_Expression_Modulo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression147"):
                opp_val = getattr(old_value, "lua_Expression147", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression147"):
                opp_val = getattr(value, "lua_Expression147", None)
                setattr(value, "lua_Expression147", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_False(Expression):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression_Nil(Expression):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Statement_FunctioncallOrAssignment:

    pass
class lua_Statement_CallFunction(Statement_FunctioncallOrAssignment):

    def __init__(self, lua_Statement_CallFunction: "lua_Expression" = None, lua_Statement_CallFunction79: "lua_Functioncall_Arguments" = None):
        self.lua_Statement_CallFunction = lua_Statement_CallFunction
        self.lua_Statement_CallFunction79 = lua_Statement_CallFunction79
        
    @property
    def lua_Statement_CallFunction79(self):
        return self.__lua_Statement_CallFunction79

    @lua_Statement_CallFunction79.setter
    def lua_Statement_CallFunction79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_CallFunction__lua_Statement_CallFunction79", None)
        self.__lua_Statement_CallFunction79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Functioncall_Arguments80"):
                opp_val = getattr(old_value, "lua_Functioncall_Arguments80", None)
                if opp_val == self:
                    setattr(old_value, "lua_Functioncall_Arguments80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Functioncall_Arguments80"):
                opp_val = getattr(value, "lua_Functioncall_Arguments80", None)
                setattr(value, "lua_Functioncall_Arguments80", self)

    @property
    def lua_Statement_CallFunction(self):
        return self.__lua_Statement_CallFunction

    @lua_Statement_CallFunction.setter
    def lua_Statement_CallFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_CallFunction__lua_Statement_CallFunction", None)
        self.__lua_Statement_CallFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression77"):
                opp_val = getattr(old_value, "lua_Expression77", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression77"):
                opp_val = getattr(value, "lua_Expression77", None)
                setattr(value, "lua_Expression77", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Statement_Assignment(Statement_FunctioncallOrAssignment):

    def __init__(self, lua_Statement_Assignment: set["lua_Expression"] = None, lua_Statement_Assignment69: set["lua_Expression"] = None):
        self.lua_Statement_Assignment = lua_Statement_Assignment if lua_Statement_Assignment is not None else set()
        self.lua_Statement_Assignment69 = lua_Statement_Assignment69 if lua_Statement_Assignment69 is not None else set()
        
    @property
    def lua_Statement_Assignment69(self):
        return self.__lua_Statement_Assignment69

    @lua_Statement_Assignment69.setter
    def lua_Statement_Assignment69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_Assignment__lua_Statement_Assignment69", None)
        self.__lua_Statement_Assignment69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lua_Expression70"):
                    opp_val = getattr(item, "lua_Expression70", None)
                    
                    if opp_val == self:
                        setattr(item, "lua_Expression70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lua_Expression70"):
                    opp_val = getattr(item, "lua_Expression70", None)
                    
                    setattr(item, "lua_Expression70", self)
                    

    @property
    def lua_Statement_Assignment(self):
        return self.__lua_Statement_Assignment

    @lua_Statement_Assignment.setter
    def lua_Statement_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_Assignment__lua_Statement_Assignment", None)
        self.__lua_Statement_Assignment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lua_Expression67"):
                    opp_val = getattr(item, "lua_Expression67", None)
                    
                    if opp_val == self:
                        setattr(item, "lua_Expression67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lua_Expression67"):
                    opp_val = getattr(item, "lua_Expression67", None)
                    
                    setattr(item, "lua_Expression67", self)
                    

    def execute(self, c: str):
        # TODO: Implement execute method
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

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Statement_If_Then_Else_ElseIfPart:

    def __init__(self, lua_Statement_If_Then_Else_ElseIfPart: "lua_Statement_If_Then_Else" = None, lua_Statement_If_Then_Else_ElseIfPart25: "lua_Expression" = None, lua_Statement_If_Then_Else_ElseIfPart28: "lua_Block" = None):
        self.lua_Statement_If_Then_Else_ElseIfPart = lua_Statement_If_Then_Else_ElseIfPart
        self.lua_Statement_If_Then_Else_ElseIfPart25 = lua_Statement_If_Then_Else_ElseIfPart25
        self.lua_Statement_If_Then_Else_ElseIfPart28 = lua_Statement_If_Then_Else_ElseIfPart28
        
    @property
    def lua_Statement_If_Then_Else_ElseIfPart25(self):
        return self.__lua_Statement_If_Then_Else_ElseIfPart25

    @lua_Statement_If_Then_Else_ElseIfPart25.setter
    def lua_Statement_If_Then_Else_ElseIfPart25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_If_Then_Else_ElseIfPart__lua_Statement_If_Then_Else_ElseIfPart25", None)
        self.__lua_Statement_If_Then_Else_ElseIfPart25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression26"):
                opp_val = getattr(old_value, "lua_Expression26", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression26"):
                opp_val = getattr(value, "lua_Expression26", None)
                setattr(value, "lua_Expression26", self)

    @property
    def lua_Statement_If_Then_Else_ElseIfPart(self):
        return self.__lua_Statement_If_Then_Else_ElseIfPart

    @lua_Statement_If_Then_Else_ElseIfPart.setter
    def lua_Statement_If_Then_Else_ElseIfPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_If_Then_Else_ElseIfPart__lua_Statement_If_Then_Else_ElseIfPart", None)
        self.__lua_Statement_If_Then_Else_ElseIfPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_If_Then_Else20"):
                opp_val = getattr(old_value, "lua_Statement_If_Then_Else20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_If_Then_Else20"):
                opp_val = getattr(value, "lua_Statement_If_Then_Else20", None)
                if opp_val is None:
                    setattr(value, "lua_Statement_If_Then_Else20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lua_Statement_If_Then_Else_ElseIfPart28(self):
        return self.__lua_Statement_If_Then_Else_ElseIfPart28

    @lua_Statement_If_Then_Else_ElseIfPart28.setter
    def lua_Statement_If_Then_Else_ElseIfPart28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_If_Then_Else_ElseIfPart__lua_Statement_If_Then_Else_ElseIfPart28", None)
        self.__lua_Statement_If_Then_Else_ElseIfPart28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Block29"):
                opp_val = getattr(old_value, "lua_Block29", None)
                if opp_val == self:
                    setattr(old_value, "lua_Block29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Block29"):
                opp_val = getattr(value, "lua_Block29", None)
                setattr(value, "lua_Block29", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Expression(Statement_FunctioncallOrAssignment):

    def __init__(self, lua_Expression13: "lua_Statement_Repeat" = None, lua_Expression: "lua_Statement_While" = None, lua_Expression34: "lua_Statement_For_Numeric" = None, lua_Expression37: "lua_Statement_For_Numeric" = None, lua_Expression15: "lua_Statement_If_Then_Else" = None, lua_Expression26: "lua_Statement_If_Then_Else_ElseIfPart" = None, lua_Expression31: "lua_Statement_For_Numeric" = None, lua_Expression42: "lua_Statement_For_Generic" = None, lua_Expression50: "lua_Statement_Local_Variable_Declaration" = None, lua_Expression58: "lua_Functioncall_Arguments" = None, lua_Expression61: "lua_Field" = None, lua_Expression63: "lua_Field_AddEntryToTable_Brackets" = None, lua_Expression77: "lua_Statement_CallFunction" = None, lua_Expression82: "lua_Expression_Or" = None, lua_Expression85: "lua_Expression_Or" = None, lua_Expression65: "lua_LastStatement_ReturnWithValue" = None, lua_Expression67: "lua_Statement_Assignment" = None, lua_Expression70: "lua_Statement_Assignment" = None, lua_Expression72: "lua_Statement_CallMemberFunction" = None, lua_Expression107: "lua_Expression_Smaller_Equal" = None, lua_Expression110: "lua_Expression_Smaller_Equal" = None, lua_Expression112: "lua_Expression_Equal" = None, lua_Expression87: "lua_Expression_And" = None, lua_Expression90: "lua_Expression_And" = None, lua_Expression92: "lua_Expression_Larger" = None, lua_Expression95: "lua_Expression_Larger" = None, lua_Expression97: "lua_Expression_Larger_Equal" = None, lua_Expression100: "lua_Expression_Larger_Equal" = None, lua_Expression102: "lua_Expression_Smaller" = None, lua_Expression105: "lua_Expression_Smaller" = None, lua_Expression115: "lua_Expression_Equal" = None, lua_Expression117: "lua_Expression_Not_Equal" = None, lua_Expression120: "lua_Expression_Not_Equal" = None, lua_Expression122: "lua_Expression_Concatenation" = None, lua_Expression125: "lua_Expression_Concatenation" = None, lua_Expression127: "lua_Expression_Plus" = None, lua_Expression145: "lua_Expression_Division" = None, lua_Expression147: "lua_Expression_Modulo" = None, lua_Expression150: "lua_Expression_Modulo" = None, lua_Expression130: "lua_Expression_Plus" = None, lua_Expression132: "lua_Expression_Minus" = None, lua_Expression135: "lua_Expression_Minus" = None, lua_Expression137: "lua_Expression_Multiplication" = None, lua_Expression140: "lua_Expression_Multiplication" = None, lua_Expression142: "lua_Expression_Division" = None, lua_Expression163: "lua_Expression_CallMemberFunction" = None, lua_Expression168: "lua_Expression_CallFunction" = None, lua_Expression152: "lua_Expression_Negate" = None, lua_Expression154: "lua_Expression_Length" = None, lua_Expression156: "lua_Expression_Invert" = None, lua_Expression158: "lua_Expression_Exponentiation" = None, lua_Expression161: "lua_Expression_Exponentiation" = None, lua_Expression173: "lua_Expression_AccessArray" = None, lua_Expression176: "lua_Expression_AccessArray" = None, lua_Expression178: "lua_Expression_AccessMember" = None):
        self.lua_Expression13 = lua_Expression13
        self.lua_Expression = lua_Expression
        self.lua_Expression34 = lua_Expression34
        self.lua_Expression37 = lua_Expression37
        self.lua_Expression15 = lua_Expression15
        self.lua_Expression26 = lua_Expression26
        self.lua_Expression31 = lua_Expression31
        self.lua_Expression42 = lua_Expression42
        self.lua_Expression50 = lua_Expression50
        self.lua_Expression58 = lua_Expression58
        self.lua_Expression61 = lua_Expression61
        self.lua_Expression63 = lua_Expression63
        self.lua_Expression77 = lua_Expression77
        self.lua_Expression82 = lua_Expression82
        self.lua_Expression85 = lua_Expression85
        self.lua_Expression65 = lua_Expression65
        self.lua_Expression67 = lua_Expression67
        self.lua_Expression70 = lua_Expression70
        self.lua_Expression72 = lua_Expression72
        self.lua_Expression107 = lua_Expression107
        self.lua_Expression110 = lua_Expression110
        self.lua_Expression112 = lua_Expression112
        self.lua_Expression87 = lua_Expression87
        self.lua_Expression90 = lua_Expression90
        self.lua_Expression92 = lua_Expression92
        self.lua_Expression95 = lua_Expression95
        self.lua_Expression97 = lua_Expression97
        self.lua_Expression100 = lua_Expression100
        self.lua_Expression102 = lua_Expression102
        self.lua_Expression105 = lua_Expression105
        self.lua_Expression115 = lua_Expression115
        self.lua_Expression117 = lua_Expression117
        self.lua_Expression120 = lua_Expression120
        self.lua_Expression122 = lua_Expression122
        self.lua_Expression125 = lua_Expression125
        self.lua_Expression127 = lua_Expression127
        self.lua_Expression145 = lua_Expression145
        self.lua_Expression147 = lua_Expression147
        self.lua_Expression150 = lua_Expression150
        self.lua_Expression130 = lua_Expression130
        self.lua_Expression132 = lua_Expression132
        self.lua_Expression135 = lua_Expression135
        self.lua_Expression137 = lua_Expression137
        self.lua_Expression140 = lua_Expression140
        self.lua_Expression142 = lua_Expression142
        self.lua_Expression163 = lua_Expression163
        self.lua_Expression168 = lua_Expression168
        self.lua_Expression152 = lua_Expression152
        self.lua_Expression154 = lua_Expression154
        self.lua_Expression156 = lua_Expression156
        self.lua_Expression158 = lua_Expression158
        self.lua_Expression161 = lua_Expression161
        self.lua_Expression173 = lua_Expression173
        self.lua_Expression176 = lua_Expression176
        self.lua_Expression178 = lua_Expression178
        
    @property
    def lua_Expression97(self):
        return self.__lua_Expression97

    @lua_Expression97.setter
    def lua_Expression97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression97", None)
        self.__lua_Expression97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Larger_Equal"):
                opp_val = getattr(old_value, "lua_Expression_Larger_Equal", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Larger_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Larger_Equal"):
                opp_val = getattr(value, "lua_Expression_Larger_Equal", None)
                setattr(value, "lua_Expression_Larger_Equal", self)

    @property
    def lua_Expression137(self):
        return self.__lua_Expression137

    @lua_Expression137.setter
    def lua_Expression137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression137", None)
        self.__lua_Expression137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Multiplication"):
                opp_val = getattr(old_value, "lua_Expression_Multiplication", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Multiplication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Multiplication"):
                opp_val = getattr(value, "lua_Expression_Multiplication", None)
                setattr(value, "lua_Expression_Multiplication", self)

    @property
    def lua_Expression135(self):
        return self.__lua_Expression135

    @lua_Expression135.setter
    def lua_Expression135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression135", None)
        self.__lua_Expression135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Minus134"):
                opp_val = getattr(old_value, "lua_Expression_Minus134", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Minus134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Minus134"):
                opp_val = getattr(value, "lua_Expression_Minus134", None)
                setattr(value, "lua_Expression_Minus134", self)

    @property
    def lua_Expression90(self):
        return self.__lua_Expression90

    @lua_Expression90.setter
    def lua_Expression90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression90", None)
        self.__lua_Expression90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_And89"):
                opp_val = getattr(old_value, "lua_Expression_And89", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_And89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_And89"):
                opp_val = getattr(value, "lua_Expression_And89", None)
                setattr(value, "lua_Expression_And89", self)

    @property
    def lua_Expression77(self):
        return self.__lua_Expression77

    @lua_Expression77.setter
    def lua_Expression77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression77", None)
        self.__lua_Expression77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_CallFunction"):
                opp_val = getattr(old_value, "lua_Statement_CallFunction", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_CallFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_CallFunction"):
                opp_val = getattr(value, "lua_Statement_CallFunction", None)
                setattr(value, "lua_Statement_CallFunction", self)

    @property
    def lua_Expression176(self):
        return self.__lua_Expression176

    @lua_Expression176.setter
    def lua_Expression176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression176", None)
        self.__lua_Expression176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_AccessArray175"):
                opp_val = getattr(old_value, "lua_Expression_AccessArray175", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_AccessArray175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_AccessArray175"):
                opp_val = getattr(value, "lua_Expression_AccessArray175", None)
                setattr(value, "lua_Expression_AccessArray175", self)

    @property
    def lua_Expression61(self):
        return self.__lua_Expression61

    @lua_Expression61.setter
    def lua_Expression61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression61", None)
        self.__lua_Expression61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Field60"):
                opp_val = getattr(old_value, "lua_Field60", None)
                if opp_val == self:
                    setattr(old_value, "lua_Field60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Field60"):
                opp_val = getattr(value, "lua_Field60", None)
                setattr(value, "lua_Field60", self)

    @property
    def lua_Expression65(self):
        return self.__lua_Expression65

    @lua_Expression65.setter
    def lua_Expression65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression65", None)
        self.__lua_Expression65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_LastStatement_ReturnWithValue"):
                opp_val = getattr(old_value, "lua_LastStatement_ReturnWithValue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_LastStatement_ReturnWithValue"):
                opp_val = getattr(value, "lua_LastStatement_ReturnWithValue", None)
                if opp_val is None:
                    setattr(value, "lua_LastStatement_ReturnWithValue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lua_Expression117(self):
        return self.__lua_Expression117

    @lua_Expression117.setter
    def lua_Expression117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression117", None)
        self.__lua_Expression117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Not_Equal"):
                opp_val = getattr(old_value, "lua_Expression_Not_Equal", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Not_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Not_Equal"):
                opp_val = getattr(value, "lua_Expression_Not_Equal", None)
                setattr(value, "lua_Expression_Not_Equal", self)

    @property
    def lua_Expression140(self):
        return self.__lua_Expression140

    @lua_Expression140.setter
    def lua_Expression140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression140", None)
        self.__lua_Expression140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Multiplication139"):
                opp_val = getattr(old_value, "lua_Expression_Multiplication139", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Multiplication139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Multiplication139"):
                opp_val = getattr(value, "lua_Expression_Multiplication139", None)
                setattr(value, "lua_Expression_Multiplication139", self)

    @property
    def lua_Expression87(self):
        return self.__lua_Expression87

    @lua_Expression87.setter
    def lua_Expression87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression87", None)
        self.__lua_Expression87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_And"):
                opp_val = getattr(old_value, "lua_Expression_And", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_And", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_And"):
                opp_val = getattr(value, "lua_Expression_And", None)
                setattr(value, "lua_Expression_And", self)

    @property
    def lua_Expression92(self):
        return self.__lua_Expression92

    @lua_Expression92.setter
    def lua_Expression92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression92", None)
        self.__lua_Expression92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Larger"):
                opp_val = getattr(old_value, "lua_Expression_Larger", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Larger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Larger"):
                opp_val = getattr(value, "lua_Expression_Larger", None)
                setattr(value, "lua_Expression_Larger", self)

    @property
    def lua_Expression145(self):
        return self.__lua_Expression145

    @lua_Expression145.setter
    def lua_Expression145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression145", None)
        self.__lua_Expression145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Division144"):
                opp_val = getattr(old_value, "lua_Expression_Division144", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Division144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Division144"):
                opp_val = getattr(value, "lua_Expression_Division144", None)
                setattr(value, "lua_Expression_Division144", self)

    @property
    def lua_Expression(self):
        return self.__lua_Expression

    @lua_Expression.setter
    def lua_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression", None)
        self.__lua_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_While"):
                opp_val = getattr(old_value, "lua_Statement_While", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_While"):
                opp_val = getattr(value, "lua_Statement_While", None)
                setattr(value, "lua_Statement_While", self)

    @property
    def lua_Expression102(self):
        return self.__lua_Expression102

    @lua_Expression102.setter
    def lua_Expression102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression102", None)
        self.__lua_Expression102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Smaller"):
                opp_val = getattr(old_value, "lua_Expression_Smaller", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Smaller", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Smaller"):
                opp_val = getattr(value, "lua_Expression_Smaller", None)
                setattr(value, "lua_Expression_Smaller", self)

    @property
    def lua_Expression100(self):
        return self.__lua_Expression100

    @lua_Expression100.setter
    def lua_Expression100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression100", None)
        self.__lua_Expression100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Larger_Equal99"):
                opp_val = getattr(old_value, "lua_Expression_Larger_Equal99", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Larger_Equal99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Larger_Equal99"):
                opp_val = getattr(value, "lua_Expression_Larger_Equal99", None)
                setattr(value, "lua_Expression_Larger_Equal99", self)

    @property
    def lua_Expression115(self):
        return self.__lua_Expression115

    @lua_Expression115.setter
    def lua_Expression115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression115", None)
        self.__lua_Expression115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Equal114"):
                opp_val = getattr(old_value, "lua_Expression_Equal114", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Equal114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Equal114"):
                opp_val = getattr(value, "lua_Expression_Equal114", None)
                setattr(value, "lua_Expression_Equal114", self)

    @property
    def lua_Expression70(self):
        return self.__lua_Expression70

    @lua_Expression70.setter
    def lua_Expression70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression70", None)
        self.__lua_Expression70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_Assignment69"):
                opp_val = getattr(old_value, "lua_Statement_Assignment69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_Assignment69"):
                opp_val = getattr(value, "lua_Statement_Assignment69", None)
                if opp_val is None:
                    setattr(value, "lua_Statement_Assignment69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lua_Expression120(self):
        return self.__lua_Expression120

    @lua_Expression120.setter
    def lua_Expression120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression120", None)
        self.__lua_Expression120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Not_Equal119"):
                opp_val = getattr(old_value, "lua_Expression_Not_Equal119", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Not_Equal119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Not_Equal119"):
                opp_val = getattr(value, "lua_Expression_Not_Equal119", None)
                setattr(value, "lua_Expression_Not_Equal119", self)

    @property
    def lua_Expression105(self):
        return self.__lua_Expression105

    @lua_Expression105.setter
    def lua_Expression105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression105", None)
        self.__lua_Expression105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Smaller104"):
                opp_val = getattr(old_value, "lua_Expression_Smaller104", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Smaller104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Smaller104"):
                opp_val = getattr(value, "lua_Expression_Smaller104", None)
                setattr(value, "lua_Expression_Smaller104", self)

    @property
    def lua_Expression130(self):
        return self.__lua_Expression130

    @lua_Expression130.setter
    def lua_Expression130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression130", None)
        self.__lua_Expression130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Plus129"):
                opp_val = getattr(old_value, "lua_Expression_Plus129", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Plus129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Plus129"):
                opp_val = getattr(value, "lua_Expression_Plus129", None)
                setattr(value, "lua_Expression_Plus129", self)

    @property
    def lua_Expression147(self):
        return self.__lua_Expression147

    @lua_Expression147.setter
    def lua_Expression147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression147", None)
        self.__lua_Expression147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Modulo"):
                opp_val = getattr(old_value, "lua_Expression_Modulo", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Modulo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Modulo"):
                opp_val = getattr(value, "lua_Expression_Modulo", None)
                setattr(value, "lua_Expression_Modulo", self)

    @property
    def lua_Expression67(self):
        return self.__lua_Expression67

    @lua_Expression67.setter
    def lua_Expression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression67", None)
        self.__lua_Expression67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_Assignment"):
                opp_val = getattr(old_value, "lua_Statement_Assignment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_Assignment"):
                opp_val = getattr(value, "lua_Statement_Assignment", None)
                if opp_val is None:
                    setattr(value, "lua_Statement_Assignment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lua_Expression42(self):
        return self.__lua_Expression42

    @lua_Expression42.setter
    def lua_Expression42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression42", None)
        self.__lua_Expression42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_For_Generic"):
                opp_val = getattr(old_value, "lua_Statement_For_Generic", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_For_Generic"):
                opp_val = getattr(value, "lua_Statement_For_Generic", None)
                if opp_val is None:
                    setattr(value, "lua_Statement_For_Generic", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lua_Expression50(self):
        return self.__lua_Expression50

    @lua_Expression50.setter
    def lua_Expression50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression50", None)
        self.__lua_Expression50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_Local_Variable_Declaration"):
                opp_val = getattr(old_value, "lua_Statement_Local_Variable_Declaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_Local_Variable_Declaration"):
                opp_val = getattr(value, "lua_Statement_Local_Variable_Declaration", None)
                if opp_val is None:
                    setattr(value, "lua_Statement_Local_Variable_Declaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lua_Expression37(self):
        return self.__lua_Expression37

    @lua_Expression37.setter
    def lua_Expression37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression37", None)
        self.__lua_Expression37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_For_Numeric36"):
                opp_val = getattr(old_value, "lua_Statement_For_Numeric36", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_For_Numeric36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_For_Numeric36"):
                opp_val = getattr(value, "lua_Statement_For_Numeric36", None)
                setattr(value, "lua_Statement_For_Numeric36", self)

    @property
    def lua_Expression161(self):
        return self.__lua_Expression161

    @lua_Expression161.setter
    def lua_Expression161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression161", None)
        self.__lua_Expression161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Exponentiation160"):
                opp_val = getattr(old_value, "lua_Expression_Exponentiation160", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Exponentiation160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Exponentiation160"):
                opp_val = getattr(value, "lua_Expression_Exponentiation160", None)
                setattr(value, "lua_Expression_Exponentiation160", self)

    @property
    def lua_Expression63(self):
        return self.__lua_Expression63

    @lua_Expression63.setter
    def lua_Expression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression63", None)
        self.__lua_Expression63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Field_AddEntryToTable_Brackets"):
                opp_val = getattr(old_value, "lua_Field_AddEntryToTable_Brackets", None)
                if opp_val == self:
                    setattr(old_value, "lua_Field_AddEntryToTable_Brackets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Field_AddEntryToTable_Brackets"):
                opp_val = getattr(value, "lua_Field_AddEntryToTable_Brackets", None)
                setattr(value, "lua_Field_AddEntryToTable_Brackets", self)

    @property
    def lua_Expression107(self):
        return self.__lua_Expression107

    @lua_Expression107.setter
    def lua_Expression107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression107", None)
        self.__lua_Expression107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Smaller_Equal"):
                opp_val = getattr(old_value, "lua_Expression_Smaller_Equal", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Smaller_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Smaller_Equal"):
                opp_val = getattr(value, "lua_Expression_Smaller_Equal", None)
                setattr(value, "lua_Expression_Smaller_Equal", self)

    @property
    def lua_Expression26(self):
        return self.__lua_Expression26

    @lua_Expression26.setter
    def lua_Expression26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression26", None)
        self.__lua_Expression26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_If_Then_Else_ElseIfPart25"):
                opp_val = getattr(old_value, "lua_Statement_If_Then_Else_ElseIfPart25", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_If_Then_Else_ElseIfPart25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_If_Then_Else_ElseIfPart25"):
                opp_val = getattr(value, "lua_Statement_If_Then_Else_ElseIfPart25", None)
                setattr(value, "lua_Statement_If_Then_Else_ElseIfPart25", self)

    @property
    def lua_Expression34(self):
        return self.__lua_Expression34

    @lua_Expression34.setter
    def lua_Expression34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression34", None)
        self.__lua_Expression34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_For_Numeric33"):
                opp_val = getattr(old_value, "lua_Statement_For_Numeric33", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_For_Numeric33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_For_Numeric33"):
                opp_val = getattr(value, "lua_Statement_For_Numeric33", None)
                setattr(value, "lua_Statement_For_Numeric33", self)

    @property
    def lua_Expression150(self):
        return self.__lua_Expression150

    @lua_Expression150.setter
    def lua_Expression150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression150", None)
        self.__lua_Expression150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Modulo149"):
                opp_val = getattr(old_value, "lua_Expression_Modulo149", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Modulo149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Modulo149"):
                opp_val = getattr(value, "lua_Expression_Modulo149", None)
                setattr(value, "lua_Expression_Modulo149", self)

    @property
    def lua_Expression122(self):
        return self.__lua_Expression122

    @lua_Expression122.setter
    def lua_Expression122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression122", None)
        self.__lua_Expression122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Concatenation"):
                opp_val = getattr(old_value, "lua_Expression_Concatenation", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Concatenation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Concatenation"):
                opp_val = getattr(value, "lua_Expression_Concatenation", None)
                setattr(value, "lua_Expression_Concatenation", self)

    @property
    def lua_Expression173(self):
        return self.__lua_Expression173

    @lua_Expression173.setter
    def lua_Expression173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression173", None)
        self.__lua_Expression173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_AccessArray"):
                opp_val = getattr(old_value, "lua_Expression_AccessArray", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_AccessArray", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_AccessArray"):
                opp_val = getattr(value, "lua_Expression_AccessArray", None)
                setattr(value, "lua_Expression_AccessArray", self)

    @property
    def lua_Expression168(self):
        return self.__lua_Expression168

    @lua_Expression168.setter
    def lua_Expression168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression168", None)
        self.__lua_Expression168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_CallFunction"):
                opp_val = getattr(old_value, "lua_Expression_CallFunction", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_CallFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_CallFunction"):
                opp_val = getattr(value, "lua_Expression_CallFunction", None)
                setattr(value, "lua_Expression_CallFunction", self)

    @property
    def lua_Expression13(self):
        return self.__lua_Expression13

    @lua_Expression13.setter
    def lua_Expression13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression13", None)
        self.__lua_Expression13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_Repeat12"):
                opp_val = getattr(old_value, "lua_Statement_Repeat12", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_Repeat12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_Repeat12"):
                opp_val = getattr(value, "lua_Statement_Repeat12", None)
                setattr(value, "lua_Statement_Repeat12", self)

    @property
    def lua_Expression31(self):
        return self.__lua_Expression31

    @lua_Expression31.setter
    def lua_Expression31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression31", None)
        self.__lua_Expression31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_For_Numeric"):
                opp_val = getattr(old_value, "lua_Statement_For_Numeric", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_For_Numeric", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_For_Numeric"):
                opp_val = getattr(value, "lua_Statement_For_Numeric", None)
                setattr(value, "lua_Statement_For_Numeric", self)

    @property
    def lua_Expression112(self):
        return self.__lua_Expression112

    @lua_Expression112.setter
    def lua_Expression112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression112", None)
        self.__lua_Expression112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Equal"):
                opp_val = getattr(old_value, "lua_Expression_Equal", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Equal"):
                opp_val = getattr(value, "lua_Expression_Equal", None)
                setattr(value, "lua_Expression_Equal", self)

    @property
    def lua_Expression125(self):
        return self.__lua_Expression125

    @lua_Expression125.setter
    def lua_Expression125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression125", None)
        self.__lua_Expression125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Concatenation124"):
                opp_val = getattr(old_value, "lua_Expression_Concatenation124", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Concatenation124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Concatenation124"):
                opp_val = getattr(value, "lua_Expression_Concatenation124", None)
                setattr(value, "lua_Expression_Concatenation124", self)

    @property
    def lua_Expression154(self):
        return self.__lua_Expression154

    @lua_Expression154.setter
    def lua_Expression154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression154", None)
        self.__lua_Expression154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Length"):
                opp_val = getattr(old_value, "lua_Expression_Length", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Length", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Length"):
                opp_val = getattr(value, "lua_Expression_Length", None)
                setattr(value, "lua_Expression_Length", self)

    @property
    def lua_Expression72(self):
        return self.__lua_Expression72

    @lua_Expression72.setter
    def lua_Expression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression72", None)
        self.__lua_Expression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_CallMemberFunction"):
                opp_val = getattr(old_value, "lua_Statement_CallMemberFunction", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_CallMemberFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_CallMemberFunction"):
                opp_val = getattr(value, "lua_Statement_CallMemberFunction", None)
                setattr(value, "lua_Statement_CallMemberFunction", self)

    @property
    def lua_Expression158(self):
        return self.__lua_Expression158

    @lua_Expression158.setter
    def lua_Expression158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression158", None)
        self.__lua_Expression158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Exponentiation"):
                opp_val = getattr(old_value, "lua_Expression_Exponentiation", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Exponentiation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Exponentiation"):
                opp_val = getattr(value, "lua_Expression_Exponentiation", None)
                setattr(value, "lua_Expression_Exponentiation", self)

    @property
    def lua_Expression82(self):
        return self.__lua_Expression82

    @lua_Expression82.setter
    def lua_Expression82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression82", None)
        self.__lua_Expression82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Or"):
                opp_val = getattr(old_value, "lua_Expression_Or", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Or", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Or"):
                opp_val = getattr(value, "lua_Expression_Or", None)
                setattr(value, "lua_Expression_Or", self)

    @property
    def lua_Expression95(self):
        return self.__lua_Expression95

    @lua_Expression95.setter
    def lua_Expression95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression95", None)
        self.__lua_Expression95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Larger94"):
                opp_val = getattr(old_value, "lua_Expression_Larger94", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Larger94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Larger94"):
                opp_val = getattr(value, "lua_Expression_Larger94", None)
                setattr(value, "lua_Expression_Larger94", self)

    @property
    def lua_Expression156(self):
        return self.__lua_Expression156

    @lua_Expression156.setter
    def lua_Expression156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression156", None)
        self.__lua_Expression156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Invert"):
                opp_val = getattr(old_value, "lua_Expression_Invert", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Invert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Invert"):
                opp_val = getattr(value, "lua_Expression_Invert", None)
                setattr(value, "lua_Expression_Invert", self)

    @property
    def lua_Expression58(self):
        return self.__lua_Expression58

    @lua_Expression58.setter
    def lua_Expression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression58", None)
        self.__lua_Expression58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Functioncall_Arguments"):
                opp_val = getattr(old_value, "lua_Functioncall_Arguments", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Functioncall_Arguments"):
                opp_val = getattr(value, "lua_Functioncall_Arguments", None)
                if opp_val is None:
                    setattr(value, "lua_Functioncall_Arguments", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lua_Expression15(self):
        return self.__lua_Expression15

    @lua_Expression15.setter
    def lua_Expression15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression15", None)
        self.__lua_Expression15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_If_Then_Else"):
                opp_val = getattr(old_value, "lua_Statement_If_Then_Else", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_If_Then_Else", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_If_Then_Else"):
                opp_val = getattr(value, "lua_Statement_If_Then_Else", None)
                setattr(value, "lua_Statement_If_Then_Else", self)

    @property
    def lua_Expression178(self):
        return self.__lua_Expression178

    @lua_Expression178.setter
    def lua_Expression178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression178", None)
        self.__lua_Expression178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_AccessMember"):
                opp_val = getattr(old_value, "lua_Expression_AccessMember", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_AccessMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_AccessMember"):
                opp_val = getattr(value, "lua_Expression_AccessMember", None)
                setattr(value, "lua_Expression_AccessMember", self)

    @property
    def lua_Expression110(self):
        return self.__lua_Expression110

    @lua_Expression110.setter
    def lua_Expression110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression110", None)
        self.__lua_Expression110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Smaller_Equal109"):
                opp_val = getattr(old_value, "lua_Expression_Smaller_Equal109", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Smaller_Equal109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Smaller_Equal109"):
                opp_val = getattr(value, "lua_Expression_Smaller_Equal109", None)
                setattr(value, "lua_Expression_Smaller_Equal109", self)

    @property
    def lua_Expression85(self):
        return self.__lua_Expression85

    @lua_Expression85.setter
    def lua_Expression85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression85", None)
        self.__lua_Expression85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Or84"):
                opp_val = getattr(old_value, "lua_Expression_Or84", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Or84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Or84"):
                opp_val = getattr(value, "lua_Expression_Or84", None)
                setattr(value, "lua_Expression_Or84", self)

    @property
    def lua_Expression152(self):
        return self.__lua_Expression152

    @lua_Expression152.setter
    def lua_Expression152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression152", None)
        self.__lua_Expression152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Negate"):
                opp_val = getattr(old_value, "lua_Expression_Negate", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Negate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Negate"):
                opp_val = getattr(value, "lua_Expression_Negate", None)
                setattr(value, "lua_Expression_Negate", self)

    @property
    def lua_Expression163(self):
        return self.__lua_Expression163

    @lua_Expression163.setter
    def lua_Expression163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression163", None)
        self.__lua_Expression163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_CallMemberFunction"):
                opp_val = getattr(old_value, "lua_Expression_CallMemberFunction", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_CallMemberFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_CallMemberFunction"):
                opp_val = getattr(value, "lua_Expression_CallMemberFunction", None)
                setattr(value, "lua_Expression_CallMemberFunction", self)

    @property
    def lua_Expression127(self):
        return self.__lua_Expression127

    @lua_Expression127.setter
    def lua_Expression127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression127", None)
        self.__lua_Expression127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Plus"):
                opp_val = getattr(old_value, "lua_Expression_Plus", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Plus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Plus"):
                opp_val = getattr(value, "lua_Expression_Plus", None)
                setattr(value, "lua_Expression_Plus", self)

    @property
    def lua_Expression132(self):
        return self.__lua_Expression132

    @lua_Expression132.setter
    def lua_Expression132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression132", None)
        self.__lua_Expression132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Minus"):
                opp_val = getattr(old_value, "lua_Expression_Minus", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Minus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Minus"):
                opp_val = getattr(value, "lua_Expression_Minus", None)
                setattr(value, "lua_Expression_Minus", self)

    @property
    def lua_Expression142(self):
        return self.__lua_Expression142

    @lua_Expression142.setter
    def lua_Expression142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Expression__lua_Expression142", None)
        self.__lua_Expression142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression_Division"):
                opp_val = getattr(old_value, "lua_Expression_Division", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression_Division", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression_Division"):
                opp_val = getattr(value, "lua_Expression_Division", None)
                setattr(value, "lua_Expression_Division", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Statement:

    pass
class lua_Statement_Repeat(Statement):

    def __init__(self, lua_Statement_Repeat12: "lua_Expression" = None, lua_Statement_Repeat: "lua_Block" = None):
        self.lua_Statement_Repeat12 = lua_Statement_Repeat12
        self.lua_Statement_Repeat = lua_Statement_Repeat
        
    @property
    def lua_Statement_Repeat12(self):
        return self.__lua_Statement_Repeat12

    @lua_Statement_Repeat12.setter
    def lua_Statement_Repeat12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_Repeat__lua_Statement_Repeat12", None)
        self.__lua_Statement_Repeat12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression13"):
                opp_val = getattr(old_value, "lua_Expression13", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression13"):
                opp_val = getattr(value, "lua_Expression13", None)
                setattr(value, "lua_Expression13", self)

    @property
    def lua_Statement_Repeat(self):
        return self.__lua_Statement_Repeat

    @lua_Statement_Repeat.setter
    def lua_Statement_Repeat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_Repeat__lua_Statement_Repeat", None)
        self.__lua_Statement_Repeat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Block10"):
                opp_val = getattr(old_value, "lua_Block10", None)
                if opp_val == self:
                    setattr(old_value, "lua_Block10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Block10"):
                opp_val = getattr(value, "lua_Block10", None)
                setattr(value, "lua_Block10", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Statement_FunctioncallOrAssignment(Statement):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Statement_While(Statement):

    def __init__(self, lua_Statement_While: "lua_Expression" = None, lua_Statement_While7: "lua_Block" = None):
        self.lua_Statement_While = lua_Statement_While
        self.lua_Statement_While7 = lua_Statement_While7
        
    @property
    def lua_Statement_While(self):
        return self.__lua_Statement_While

    @lua_Statement_While.setter
    def lua_Statement_While(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_While__lua_Statement_While", None)
        self.__lua_Statement_While = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression"):
                opp_val = getattr(old_value, "lua_Expression", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression"):
                opp_val = getattr(value, "lua_Expression", None)
                setattr(value, "lua_Expression", self)

    @property
    def lua_Statement_While7(self):
        return self.__lua_Statement_While7

    @lua_Statement_While7.setter
    def lua_Statement_While7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_While__lua_Statement_While7", None)
        self.__lua_Statement_While7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Block8"):
                opp_val = getattr(old_value, "lua_Block8", None)
                if opp_val == self:
                    setattr(old_value, "lua_Block8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Block8"):
                opp_val = getattr(value, "lua_Block8", None)
                setattr(value, "lua_Block8", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Statement_GlobalFunction_Declaration(Statement):

    def __init__(self, prefix: str, functionName: str, lua_Statement_GlobalFunction_Declaration: "lua_Function" = None):
        self.prefix = prefix
        self.functionName = functionName
        self.lua_Statement_GlobalFunction_Declaration = lua_Statement_GlobalFunction_Declaration
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

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

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

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

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Statement_For_Numeric(Statement):

    def __init__(self, iteratorName: str, lua_Statement_For_Numeric33: "lua_Expression" = None, lua_Statement_For_Numeric36: "lua_Expression" = None, lua_Statement_For_Numeric39: "lua_Block" = None, lua_Statement_For_Numeric: "lua_Expression" = None):
        self.iteratorName = iteratorName
        self.lua_Statement_For_Numeric33 = lua_Statement_For_Numeric33
        self.lua_Statement_For_Numeric36 = lua_Statement_For_Numeric36
        self.lua_Statement_For_Numeric39 = lua_Statement_For_Numeric39
        self.lua_Statement_For_Numeric = lua_Statement_For_Numeric
        
    @property
    def iteratorName(self) -> str:
        return self.__iteratorName

    @iteratorName.setter
    def iteratorName(self, iteratorName: str):
        self.__iteratorName = iteratorName

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

    def execute(self, c: str):
        # TODO: Implement execute method
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
                    

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

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

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Statement_Block(Statement):

    def __init__(self, lua_Statement_Block: "lua_Block" = None):
        self.lua_Statement_Block = lua_Statement_Block
        
    @property
    def lua_Statement_Block(self):
        return self.__lua_Statement_Block

    @lua_Statement_Block.setter
    def lua_Statement_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_Block__lua_Statement_Block", None)
        self.__lua_Statement_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Block4"):
                opp_val = getattr(old_value, "lua_Block4", None)
                if opp_val == self:
                    setattr(old_value, "lua_Block4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Block4"):
                opp_val = getattr(value, "lua_Block4", None)
                setattr(value, "lua_Block4", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class LastStatement:

    pass
class lua_LastStatement_Break(LastStatement):

    pass
class lua_LastStatement_Return(LastStatement):

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_LastStatement:

    def __init__(self, lua_LastStatement: "lua_Block" = None):
        self.lua_LastStatement = lua_LastStatement
        
    @property
    def lua_LastStatement(self):
        return self.__lua_LastStatement

    @lua_LastStatement.setter
    def lua_LastStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_LastStatement__lua_LastStatement", None)
        self.__lua_LastStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Block2"):
                opp_val = getattr(old_value, "lua_Block2", None)
                if opp_val == self:
                    setattr(old_value, "lua_Block2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Block2"):
                opp_val = getattr(value, "lua_Block2", None)
                setattr(value, "lua_Block2", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Statement:

    def __init__(self, lua_Statement: "lua_Block" = None):
        self.lua_Statement = lua_Statement
        
    @property
    def lua_Statement(self):
        return self.__lua_Statement

    @lua_Statement.setter
    def lua_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement__lua_Statement", None)
        self.__lua_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Block"):
                opp_val = getattr(old_value, "lua_Block", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Block"):
                opp_val = getattr(value, "lua_Block", None)
                if opp_val is None:
                    setattr(value, "lua_Block", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class Chunk:

    pass
class lua_Block(Chunk):

    def __init__(self, lua_Block: set["lua_Statement"] = None, lua_Block2: "lua_LastStatement" = None, lua_Block4: "lua_Statement_Block" = None, lua_Block8: "lua_Statement_While" = None, lua_Block10: "lua_Statement_Repeat" = None, lua_Block40: "lua_Statement_For_Numeric" = None, lua_Block18: "lua_Statement_If_Then_Else" = None, lua_Block23: "lua_Statement_If_Then_Else" = None, lua_Block29: "lua_Statement_If_Then_Else_ElseIfPart" = None, lua_Block45: "lua_Statement_For_Generic" = None, lua_Block56: "lua_Function" = None):
        self.lua_Block = lua_Block if lua_Block is not None else set()
        self.lua_Block2 = lua_Block2
        self.lua_Block4 = lua_Block4
        self.lua_Block8 = lua_Block8
        self.lua_Block10 = lua_Block10
        self.lua_Block40 = lua_Block40
        self.lua_Block18 = lua_Block18
        self.lua_Block23 = lua_Block23
        self.lua_Block29 = lua_Block29
        self.lua_Block45 = lua_Block45
        self.lua_Block56 = lua_Block56
        
    @property
    def lua_Block2(self):
        return self.__lua_Block2

    @lua_Block2.setter
    def lua_Block2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Block__lua_Block2", None)
        self.__lua_Block2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_LastStatement"):
                opp_val = getattr(old_value, "lua_LastStatement", None)
                if opp_val == self:
                    setattr(old_value, "lua_LastStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_LastStatement"):
                opp_val = getattr(value, "lua_LastStatement", None)
                setattr(value, "lua_LastStatement", self)

    @property
    def lua_Block4(self):
        return self.__lua_Block4

    @lua_Block4.setter
    def lua_Block4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Block__lua_Block4", None)
        self.__lua_Block4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_Block"):
                opp_val = getattr(old_value, "lua_Statement_Block", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_Block"):
                opp_val = getattr(value, "lua_Statement_Block", None)
                setattr(value, "lua_Statement_Block", self)

    @property
    def lua_Block18(self):
        return self.__lua_Block18

    @lua_Block18.setter
    def lua_Block18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Block__lua_Block18", None)
        self.__lua_Block18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_If_Then_Else17"):
                opp_val = getattr(old_value, "lua_Statement_If_Then_Else17", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_If_Then_Else17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_If_Then_Else17"):
                opp_val = getattr(value, "lua_Statement_If_Then_Else17", None)
                setattr(value, "lua_Statement_If_Then_Else17", self)

    @property
    def lua_Block45(self):
        return self.__lua_Block45

    @lua_Block45.setter
    def lua_Block45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Block__lua_Block45", None)
        self.__lua_Block45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_For_Generic44"):
                opp_val = getattr(old_value, "lua_Statement_For_Generic44", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_For_Generic44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_For_Generic44"):
                opp_val = getattr(value, "lua_Statement_For_Generic44", None)
                setattr(value, "lua_Statement_For_Generic44", self)

    @property
    def lua_Block(self):
        return self.__lua_Block

    @lua_Block.setter
    def lua_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Block__lua_Block", None)
        self.__lua_Block = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lua_Statement"):
                    opp_val = getattr(item, "lua_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "lua_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lua_Statement"):
                    opp_val = getattr(item, "lua_Statement", None)
                    
                    setattr(item, "lua_Statement", self)
                    

    @property
    def lua_Block23(self):
        return self.__lua_Block23

    @lua_Block23.setter
    def lua_Block23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Block__lua_Block23", None)
        self.__lua_Block23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_If_Then_Else22"):
                opp_val = getattr(old_value, "lua_Statement_If_Then_Else22", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_If_Then_Else22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_If_Then_Else22"):
                opp_val = getattr(value, "lua_Statement_If_Then_Else22", None)
                setattr(value, "lua_Statement_If_Then_Else22", self)

    @property
    def lua_Block56(self):
        return self.__lua_Block56

    @lua_Block56.setter
    def lua_Block56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Block__lua_Block56", None)
        self.__lua_Block56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Function55"):
                opp_val = getattr(old_value, "lua_Function55", None)
                if opp_val == self:
                    setattr(old_value, "lua_Function55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Function55"):
                opp_val = getattr(value, "lua_Function55", None)
                setattr(value, "lua_Function55", self)

    @property
    def lua_Block8(self):
        return self.__lua_Block8

    @lua_Block8.setter
    def lua_Block8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Block__lua_Block8", None)
        self.__lua_Block8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_While7"):
                opp_val = getattr(old_value, "lua_Statement_While7", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_While7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_While7"):
                opp_val = getattr(value, "lua_Statement_While7", None)
                setattr(value, "lua_Statement_While7", self)

    @property
    def lua_Block10(self):
        return self.__lua_Block10

    @lua_Block10.setter
    def lua_Block10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Block__lua_Block10", None)
        self.__lua_Block10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_Repeat"):
                opp_val = getattr(old_value, "lua_Statement_Repeat", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_Repeat", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_Repeat"):
                opp_val = getattr(value, "lua_Statement_Repeat", None)
                setattr(value, "lua_Statement_Repeat", self)

    @property
    def lua_Block29(self):
        return self.__lua_Block29

    @lua_Block29.setter
    def lua_Block29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Block__lua_Block29", None)
        self.__lua_Block29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_If_Then_Else_ElseIfPart28"):
                opp_val = getattr(old_value, "lua_Statement_If_Then_Else_ElseIfPart28", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_If_Then_Else_ElseIfPart28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_If_Then_Else_ElseIfPart28"):
                opp_val = getattr(value, "lua_Statement_If_Then_Else_ElseIfPart28", None)
                setattr(value, "lua_Statement_If_Then_Else_ElseIfPart28", self)

    @property
    def lua_Block40(self):
        return self.__lua_Block40

    @lua_Block40.setter
    def lua_Block40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Block__lua_Block40", None)
        self.__lua_Block40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Statement_For_Numeric39"):
                opp_val = getattr(old_value, "lua_Statement_For_Numeric39", None)
                if opp_val == self:
                    setattr(old_value, "lua_Statement_For_Numeric39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Statement_For_Numeric39"):
                opp_val = getattr(value, "lua_Statement_For_Numeric39", None)
                setattr(value, "lua_Statement_For_Numeric39", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Statement_If_Then_Else(Statement):

    def __init__(self, lua_Statement_If_Then_Else: "lua_Expression" = None, lua_Statement_If_Then_Else17: "lua_Block" = None, lua_Statement_If_Then_Else20: set["lua_Statement_If_Then_Else_ElseIfPart"] = None, lua_Statement_If_Then_Else22: "lua_Block" = None):
        self.lua_Statement_If_Then_Else = lua_Statement_If_Then_Else
        self.lua_Statement_If_Then_Else17 = lua_Statement_If_Then_Else17
        self.lua_Statement_If_Then_Else20 = lua_Statement_If_Then_Else20 if lua_Statement_If_Then_Else20 is not None else set()
        self.lua_Statement_If_Then_Else22 = lua_Statement_If_Then_Else22
        
    @property
    def lua_Statement_If_Then_Else20(self):
        return self.__lua_Statement_If_Then_Else20

    @lua_Statement_If_Then_Else20.setter
    def lua_Statement_If_Then_Else20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_If_Then_Else__lua_Statement_If_Then_Else20", None)
        self.__lua_Statement_If_Then_Else20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lua_Statement_If_Then_Else_ElseIfPart"):
                    opp_val = getattr(item, "lua_Statement_If_Then_Else_ElseIfPart", None)
                    
                    if opp_val == self:
                        setattr(item, "lua_Statement_If_Then_Else_ElseIfPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lua_Statement_If_Then_Else_ElseIfPart"):
                    opp_val = getattr(item, "lua_Statement_If_Then_Else_ElseIfPart", None)
                    
                    setattr(item, "lua_Statement_If_Then_Else_ElseIfPart", self)
                    

    @property
    def lua_Statement_If_Then_Else22(self):
        return self.__lua_Statement_If_Then_Else22

    @lua_Statement_If_Then_Else22.setter
    def lua_Statement_If_Then_Else22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_If_Then_Else__lua_Statement_If_Then_Else22", None)
        self.__lua_Statement_If_Then_Else22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Block23"):
                opp_val = getattr(old_value, "lua_Block23", None)
                if opp_val == self:
                    setattr(old_value, "lua_Block23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Block23"):
                opp_val = getattr(value, "lua_Block23", None)
                setattr(value, "lua_Block23", self)

    @property
    def lua_Statement_If_Then_Else(self):
        return self.__lua_Statement_If_Then_Else

    @lua_Statement_If_Then_Else.setter
    def lua_Statement_If_Then_Else(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_If_Then_Else__lua_Statement_If_Then_Else", None)
        self.__lua_Statement_If_Then_Else = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Expression15"):
                opp_val = getattr(old_value, "lua_Expression15", None)
                if opp_val == self:
                    setattr(old_value, "lua_Expression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Expression15"):
                opp_val = getattr(value, "lua_Expression15", None)
                setattr(value, "lua_Expression15", self)

    @property
    def lua_Statement_If_Then_Else17(self):
        return self.__lua_Statement_If_Then_Else17

    @lua_Statement_If_Then_Else17.setter
    def lua_Statement_If_Then_Else17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lua_Statement_If_Then_Else__lua_Statement_If_Then_Else17", None)
        self.__lua_Statement_If_Then_Else17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lua_Block18"):
                opp_val = getattr(old_value, "lua_Block18", None)
                if opp_val == self:
                    setattr(old_value, "lua_Block18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lua_Block18"):
                opp_val = getattr(value, "lua_Block18", None)
                setattr(value, "lua_Block18", self)

    def execute(self, c: str):
        # TODO: Implement execute method
        pass

class lua_Chunk:

    def __init__(self):
        
    def execute(self, c: str):
        # TODO: Implement execute method
        pass
