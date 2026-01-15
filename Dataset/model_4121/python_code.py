from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class whileDsl_ExprNot:

    def __init__(self, negation: bool, whileDsl_ExprNot55: "whileDsl_ExprEq" = None, whileDsl_ExprNot: "whileDsl_ExprOr" = None):
        self.negation = negation
        self.whileDsl_ExprNot55 = whileDsl_ExprNot55
        self.whileDsl_ExprNot = whileDsl_ExprNot
        
    @property
    def negation(self) -> bool:
        return self.__negation

    @negation.setter
    def negation(self, negation: bool):
        self.__negation = negation

    @property
    def whileDsl_ExprNot55(self):
        return self.__whileDsl_ExprNot55

    @whileDsl_ExprNot55.setter
    def whileDsl_ExprNot55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_ExprNot__whileDsl_ExprNot55", None)
        self.__whileDsl_ExprNot55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_ExprEq"):
                opp_val = getattr(old_value, "whileDsl_ExprEq", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_ExprEq", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_ExprEq"):
                opp_val = getattr(value, "whileDsl_ExprEq", None)
                setattr(value, "whileDsl_ExprEq", self)

    @property
    def whileDsl_ExprNot(self):
        return self.__whileDsl_ExprNot

    @whileDsl_ExprNot.setter
    def whileDsl_ExprNot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_ExprNot__whileDsl_ExprNot", None)
        self.__whileDsl_ExprNot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_ExprOr53"):
                opp_val = getattr(old_value, "whileDsl_ExprOr53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_ExprOr53"):
                opp_val = getattr(value, "whileDsl_ExprOr53", None)
                if opp_val is None:
                    setattr(value, "whileDsl_ExprOr53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class whileDsl_ExprOr:

    pass
class whileDsl_ExprAnd:

    pass
class whileDsl_ExprSimpleWithSymbolLExpr:

    def __init__(self, symbol: str, whileDsl_ExprSimpleWithSymbolLExpr: "whileDsl_LExpr" = None):
        self.symbol = symbol
        self.whileDsl_ExprSimpleWithSymbolLExpr = whileDsl_ExprSimpleWithSymbolLExpr
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def whileDsl_ExprSimpleWithSymbolLExpr(self):
        return self.__whileDsl_ExprSimpleWithSymbolLExpr

    @whileDsl_ExprSimpleWithSymbolLExpr.setter
    def whileDsl_ExprSimpleWithSymbolLExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_ExprSimpleWithSymbolLExpr__whileDsl_ExprSimpleWithSymbolLExpr", None)
        self.__whileDsl_ExprSimpleWithSymbolLExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_LExpr41"):
                opp_val = getattr(old_value, "whileDsl_LExpr41", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_LExpr41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_LExpr41"):
                opp_val = getattr(value, "whileDsl_LExpr41", None)
                setattr(value, "whileDsl_LExpr41", self)

class whileDsl_ExprSimpleWithExpr:

    def __init__(self, operation: str, whileDsl_ExprSimpleWithExpr: "whileDsl_Expr" = None):
        self.operation = operation
        self.whileDsl_ExprSimpleWithExpr = whileDsl_ExprSimpleWithExpr
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def whileDsl_ExprSimpleWithExpr(self):
        return self.__whileDsl_ExprSimpleWithExpr

    @whileDsl_ExprSimpleWithExpr.setter
    def whileDsl_ExprSimpleWithExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_ExprSimpleWithExpr__whileDsl_ExprSimpleWithExpr", None)
        self.__whileDsl_ExprSimpleWithExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_Expr39"):
                opp_val = getattr(old_value, "whileDsl_Expr39", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_Expr39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_Expr39"):
                opp_val = getattr(value, "whileDsl_Expr39", None)
                setattr(value, "whileDsl_Expr39", self)

class whileDsl_LExpr:

    pass
class whileDsl_ExprSimpleWithLExpr:

    def __init__(self, operation: str, whileDsl_ExprSimpleWithLExpr: "whileDsl_LExpr" = None):
        self.operation = operation
        self.whileDsl_ExprSimpleWithLExpr = whileDsl_ExprSimpleWithLExpr
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def whileDsl_ExprSimpleWithLExpr(self):
        return self.__whileDsl_ExprSimpleWithLExpr

    @whileDsl_ExprSimpleWithLExpr.setter
    def whileDsl_ExprSimpleWithLExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_ExprSimpleWithLExpr__whileDsl_ExprSimpleWithLExpr", None)
        self.__whileDsl_ExprSimpleWithLExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_LExpr"):
                opp_val = getattr(old_value, "whileDsl_LExpr", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_LExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_LExpr"):
                opp_val = getattr(value, "whileDsl_LExpr", None)
                setattr(value, "whileDsl_LExpr", self)

class whileDsl_EObject:

    pass
class whileDsl_ExprSimple:

    def __init__(self, term: str, whileDsl_ExprSimple: "whileDsl_EObject" = None, whileDsl_ExprSimple58: "whileDsl_ExprEq" = None, whileDsl_ExprSimple61: "whileDsl_ExprEq" = None):
        self.term = term
        self.whileDsl_ExprSimple = whileDsl_ExprSimple
        self.whileDsl_ExprSimple58 = whileDsl_ExprSimple58
        self.whileDsl_ExprSimple61 = whileDsl_ExprSimple61
        
    @property
    def term(self) -> str:
        return self.__term

    @term.setter
    def term(self, term: str):
        self.__term = term

    @property
    def whileDsl_ExprSimple58(self):
        return self.__whileDsl_ExprSimple58

    @whileDsl_ExprSimple58.setter
    def whileDsl_ExprSimple58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_ExprSimple__whileDsl_ExprSimple58", None)
        self.__whileDsl_ExprSimple58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_ExprEq57"):
                opp_val = getattr(old_value, "whileDsl_ExprEq57", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_ExprEq57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_ExprEq57"):
                opp_val = getattr(value, "whileDsl_ExprEq57", None)
                setattr(value, "whileDsl_ExprEq57", self)

    @property
    def whileDsl_ExprSimple(self):
        return self.__whileDsl_ExprSimple

    @whileDsl_ExprSimple.setter
    def whileDsl_ExprSimple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_ExprSimple__whileDsl_ExprSimple", None)
        self.__whileDsl_ExprSimple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_EObject"):
                opp_val = getattr(old_value, "whileDsl_EObject", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_EObject"):
                opp_val = getattr(value, "whileDsl_EObject", None)
                setattr(value, "whileDsl_EObject", self)

    @property
    def whileDsl_ExprSimple61(self):
        return self.__whileDsl_ExprSimple61

    @whileDsl_ExprSimple61.setter
    def whileDsl_ExprSimple61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_ExprSimple__whileDsl_ExprSimple61", None)
        self.__whileDsl_ExprSimple61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_ExprEq60"):
                opp_val = getattr(old_value, "whileDsl_ExprEq60", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_ExprEq60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_ExprEq60"):
                opp_val = getattr(value, "whileDsl_ExprEq60", None)
                setattr(value, "whileDsl_ExprEq60", self)

class whileDsl_Exprs:

    pass
class whileDsl_Vars:

    def __init__(self, variables: str, whileDsl_Vars: "whileDsl_VarsCommand" = None):
        self.variables = variables
        self.whileDsl_Vars = whileDsl_Vars
        
    @property
    def variables(self) -> str:
        return self.__variables

    @variables.setter
    def variables(self, variables: str):
        self.__variables = variables

    @property
    def whileDsl_Vars(self):
        return self.__whileDsl_Vars

    @whileDsl_Vars.setter
    def whileDsl_Vars(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_Vars__whileDsl_Vars", None)
        self.__whileDsl_Vars = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_VarsCommand"):
                opp_val = getattr(old_value, "whileDsl_VarsCommand", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_VarsCommand", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_VarsCommand"):
                opp_val = getattr(value, "whileDsl_VarsCommand", None)
                setattr(value, "whileDsl_VarsCommand", self)

class whileDsl_ExprEq:

    pass
class whileDsl_Expr:

    pass
class Command:

    pass
class whileDsl_IfCommand(Command):

    pass
class whileDsl_VarsCommand(Command):

    pass
class whileDsl_NopCommand(Command):

    pass
class whileDsl_ForCommand(Command):

    pass
class whileDsl_WhileCommand(Command):

    pass
class whileDsl_Command:

    pass
class whileDsl_Output:

    def __init__(self, variables: str, whileDsl_Output: "whileDsl_Definition" = None):
        self.variables = variables
        self.whileDsl_Output = whileDsl_Output
        
    @property
    def variables(self) -> str:
        return self.__variables

    @variables.setter
    def variables(self, variables: str):
        self.__variables = variables

    @property
    def whileDsl_Output(self):
        return self.__whileDsl_Output

    @whileDsl_Output.setter
    def whileDsl_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_Output__whileDsl_Output", None)
        self.__whileDsl_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_Definition8"):
                opp_val = getattr(old_value, "whileDsl_Definition8", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_Definition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_Definition8"):
                opp_val = getattr(value, "whileDsl_Definition8", None)
                setattr(value, "whileDsl_Definition8", self)

class whileDsl_Commands:

    pass
class whileDsl_Input:

    def __init__(self, variables: str, whileDsl_Input: "whileDsl_Definition" = None):
        self.variables = variables
        self.whileDsl_Input = whileDsl_Input
        
    @property
    def variables(self) -> str:
        return self.__variables

    @variables.setter
    def variables(self, variables: str):
        self.__variables = variables

    @property
    def whileDsl_Input(self):
        return self.__whileDsl_Input

    @whileDsl_Input.setter
    def whileDsl_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_Input__whileDsl_Input", None)
        self.__whileDsl_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_Definition4"):
                opp_val = getattr(old_value, "whileDsl_Definition4", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_Definition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_Definition4"):
                opp_val = getattr(value, "whileDsl_Definition4", None)
                setattr(value, "whileDsl_Definition4", self)

class whileDsl_Definition:

    pass
class whileDsl_Function:

    def __init__(self, functionName: str, whileDsl_Function: "whileDsl_Model" = None, whileDsl_Function2: "whileDsl_Definition" = None):
        self.functionName = functionName
        self.whileDsl_Function = whileDsl_Function
        self.whileDsl_Function2 = whileDsl_Function2
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def whileDsl_Function2(self):
        return self.__whileDsl_Function2

    @whileDsl_Function2.setter
    def whileDsl_Function2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_Function__whileDsl_Function2", None)
        self.__whileDsl_Function2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_Definition"):
                opp_val = getattr(old_value, "whileDsl_Definition", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_Definition"):
                opp_val = getattr(value, "whileDsl_Definition", None)
                setattr(value, "whileDsl_Definition", self)

    @property
    def whileDsl_Function(self):
        return self.__whileDsl_Function

    @whileDsl_Function.setter
    def whileDsl_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_Function__whileDsl_Function", None)
        self.__whileDsl_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_Model"):
                opp_val = getattr(old_value, "whileDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_Model"):
                opp_val = getattr(value, "whileDsl_Model", None)
                if opp_val is None:
                    setattr(value, "whileDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class whileDsl_ForeachCommand(Command):

    def __init__(self, expElement: str, whileDsl_ForeachCommand: "whileDsl_Expr" = None, whileDsl_ForeachCommand31: "whileDsl_Commands" = None):
        self.expElement = expElement
        self.whileDsl_ForeachCommand = whileDsl_ForeachCommand
        self.whileDsl_ForeachCommand31 = whileDsl_ForeachCommand31
        
    @property
    def expElement(self) -> str:
        return self.__expElement

    @expElement.setter
    def expElement(self, expElement: str):
        self.__expElement = expElement

    @property
    def whileDsl_ForeachCommand31(self):
        return self.__whileDsl_ForeachCommand31

    @whileDsl_ForeachCommand31.setter
    def whileDsl_ForeachCommand31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_ForeachCommand__whileDsl_ForeachCommand31", None)
        self.__whileDsl_ForeachCommand31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_Commands32"):
                opp_val = getattr(old_value, "whileDsl_Commands32", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_Commands32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_Commands32"):
                opp_val = getattr(value, "whileDsl_Commands32", None)
                setattr(value, "whileDsl_Commands32", self)

    @property
    def whileDsl_ForeachCommand(self):
        return self.__whileDsl_ForeachCommand

    @whileDsl_ForeachCommand.setter
    def whileDsl_ForeachCommand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_whileDsl_ForeachCommand__whileDsl_ForeachCommand", None)
        self.__whileDsl_ForeachCommand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whileDsl_Expr29"):
                opp_val = getattr(old_value, "whileDsl_Expr29", None)
                if opp_val == self:
                    setattr(old_value, "whileDsl_Expr29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whileDsl_Expr29"):
                opp_val = getattr(value, "whileDsl_Expr29", None)
                setattr(value, "whileDsl_Expr29", self)

class whileDsl_Model:

    pass