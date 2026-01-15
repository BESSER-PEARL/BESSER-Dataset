from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class wh_ExprEq:

    def __init__(self, sym: str, wh_ExprEq74: "wh_Expr" = None, wh_ExprEq: "wh_ExprNot" = None, wh_ExprEq65: "wh_ExprSimple" = None, wh_ExprEq68: "wh_ExprSimple" = None, wh_ExprEq71: "wh_LExpr" = None):
        self.sym = sym
        self.wh_ExprEq74 = wh_ExprEq74
        self.wh_ExprEq = wh_ExprEq
        self.wh_ExprEq65 = wh_ExprEq65
        self.wh_ExprEq68 = wh_ExprEq68
        self.wh_ExprEq71 = wh_ExprEq71
        
    @property
    def sym(self) -> str:
        return self.__sym

    @sym.setter
    def sym(self, sym: str):
        self.__sym = sym

    @property
    def wh_ExprEq74(self):
        return self.__wh_ExprEq74

    @wh_ExprEq74.setter
    def wh_ExprEq74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprEq__wh_ExprEq74", None)
        self.__wh_ExprEq74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Expr75"):
                opp_val = getattr(old_value, "wh_Expr75", None)
                if opp_val == self:
                    setattr(old_value, "wh_Expr75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Expr75"):
                opp_val = getattr(value, "wh_Expr75", None)
                setattr(value, "wh_Expr75", self)

    @property
    def wh_ExprEq68(self):
        return self.__wh_ExprEq68

    @wh_ExprEq68.setter
    def wh_ExprEq68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprEq__wh_ExprEq68", None)
        self.__wh_ExprEq68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprSimple69"):
                opp_val = getattr(old_value, "wh_ExprSimple69", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprSimple69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprSimple69"):
                opp_val = getattr(value, "wh_ExprSimple69", None)
                setattr(value, "wh_ExprSimple69", self)

    @property
    def wh_ExprEq(self):
        return self.__wh_ExprEq

    @wh_ExprEq.setter
    def wh_ExprEq(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprEq__wh_ExprEq", None)
        self.__wh_ExprEq = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprNot63"):
                opp_val = getattr(old_value, "wh_ExprNot63", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprNot63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprNot63"):
                opp_val = getattr(value, "wh_ExprNot63", None)
                setattr(value, "wh_ExprNot63", self)

    @property
    def wh_ExprEq71(self):
        return self.__wh_ExprEq71

    @wh_ExprEq71.setter
    def wh_ExprEq71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprEq__wh_ExprEq71", None)
        self.__wh_ExprEq71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_LExpr72"):
                opp_val = getattr(old_value, "wh_LExpr72", None)
                if opp_val == self:
                    setattr(old_value, "wh_LExpr72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_LExpr72"):
                opp_val = getattr(value, "wh_LExpr72", None)
                setattr(value, "wh_LExpr72", self)

    @property
    def wh_ExprEq65(self):
        return self.__wh_ExprEq65

    @wh_ExprEq65.setter
    def wh_ExprEq65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprEq__wh_ExprEq65", None)
        self.__wh_ExprEq65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprSimple66"):
                opp_val = getattr(old_value, "wh_ExprSimple66", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprSimple66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprSimple66"):
                opp_val = getattr(value, "wh_ExprSimple66", None)
                setattr(value, "wh_ExprSimple66", self)

class wh_ExprNot:

    def __init__(self, hasNot: str, wh_ExprNot: "wh_ExprOr" = None, wh_ExprNot63: "wh_ExprEq" = None):
        self.hasNot = hasNot
        self.wh_ExprNot = wh_ExprNot
        self.wh_ExprNot63 = wh_ExprNot63
        
    @property
    def hasNot(self) -> str:
        return self.__hasNot

    @hasNot.setter
    def hasNot(self, hasNot: str):
        self.__hasNot = hasNot

    @property
    def wh_ExprNot(self):
        return self.__wh_ExprNot

    @wh_ExprNot.setter
    def wh_ExprNot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprNot__wh_ExprNot", None)
        self.__wh_ExprNot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprOr61"):
                opp_val = getattr(old_value, "wh_ExprOr61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprOr61"):
                opp_val = getattr(value, "wh_ExprOr61", None)
                if opp_val is None:
                    setattr(value, "wh_ExprOr61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wh_ExprNot63(self):
        return self.__wh_ExprNot63

    @wh_ExprNot63.setter
    def wh_ExprNot63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprNot__wh_ExprNot63", None)
        self.__wh_ExprNot63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprEq"):
                opp_val = getattr(old_value, "wh_ExprEq", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprEq", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprEq"):
                opp_val = getattr(value, "wh_ExprEq", None)
                setattr(value, "wh_ExprEq", self)

class wh_ExprOr:

    pass
class wh_ExprSimple:

    def __init__(self, sym: str, nil: str, variable: str, wh_ExprSimple: "wh_LExpr" = None, wh_ExprSimple50: "wh_LExpr" = None, wh_ExprSimple53: "wh_Expr" = None, wh_ExprSimple56: "wh_Expr" = None, wh_ExprSimple66: "wh_ExprEq" = None, wh_ExprSimple69: "wh_ExprEq" = None):
        self.sym = sym
        self.nil = nil
        self.variable = variable
        self.wh_ExprSimple = wh_ExprSimple
        self.wh_ExprSimple50 = wh_ExprSimple50
        self.wh_ExprSimple53 = wh_ExprSimple53
        self.wh_ExprSimple56 = wh_ExprSimple56
        self.wh_ExprSimple66 = wh_ExprSimple66
        self.wh_ExprSimple69 = wh_ExprSimple69
        
    @property
    def nil(self) -> str:
        return self.__nil

    @nil.setter
    def nil(self, nil: str):
        self.__nil = nil

    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def sym(self) -> str:
        return self.__sym

    @sym.setter
    def sym(self, sym: str):
        self.__sym = sym

    @property
    def wh_ExprSimple56(self):
        return self.__wh_ExprSimple56

    @wh_ExprSimple56.setter
    def wh_ExprSimple56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSimple__wh_ExprSimple56", None)
        self.__wh_ExprSimple56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Expr57"):
                opp_val = getattr(old_value, "wh_Expr57", None)
                if opp_val == self:
                    setattr(old_value, "wh_Expr57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Expr57"):
                opp_val = getattr(value, "wh_Expr57", None)
                setattr(value, "wh_Expr57", self)

    @property
    def wh_ExprSimple53(self):
        return self.__wh_ExprSimple53

    @wh_ExprSimple53.setter
    def wh_ExprSimple53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSimple__wh_ExprSimple53", None)
        self.__wh_ExprSimple53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Expr54"):
                opp_val = getattr(old_value, "wh_Expr54", None)
                if opp_val == self:
                    setattr(old_value, "wh_Expr54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Expr54"):
                opp_val = getattr(value, "wh_Expr54", None)
                setattr(value, "wh_Expr54", self)

    @property
    def wh_ExprSimple69(self):
        return self.__wh_ExprSimple69

    @wh_ExprSimple69.setter
    def wh_ExprSimple69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSimple__wh_ExprSimple69", None)
        self.__wh_ExprSimple69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprEq68"):
                opp_val = getattr(old_value, "wh_ExprEq68", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprEq68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprEq68"):
                opp_val = getattr(value, "wh_ExprEq68", None)
                setattr(value, "wh_ExprEq68", self)

    @property
    def wh_ExprSimple50(self):
        return self.__wh_ExprSimple50

    @wh_ExprSimple50.setter
    def wh_ExprSimple50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSimple__wh_ExprSimple50", None)
        self.__wh_ExprSimple50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_LExpr51"):
                opp_val = getattr(old_value, "wh_LExpr51", None)
                if opp_val == self:
                    setattr(old_value, "wh_LExpr51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_LExpr51"):
                opp_val = getattr(value, "wh_LExpr51", None)
                setattr(value, "wh_LExpr51", self)

    @property
    def wh_ExprSimple(self):
        return self.__wh_ExprSimple

    @wh_ExprSimple.setter
    def wh_ExprSimple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSimple__wh_ExprSimple", None)
        self.__wh_ExprSimple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_LExpr"):
                opp_val = getattr(old_value, "wh_LExpr", None)
                if opp_val == self:
                    setattr(old_value, "wh_LExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_LExpr"):
                opp_val = getattr(value, "wh_LExpr", None)
                setattr(value, "wh_LExpr", self)

    @property
    def wh_ExprSimple66(self):
        return self.__wh_ExprSimple66

    @wh_ExprSimple66.setter
    def wh_ExprSimple66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_ExprSimple__wh_ExprSimple66", None)
        self.__wh_ExprSimple66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_ExprEq65"):
                opp_val = getattr(old_value, "wh_ExprEq65", None)
                if opp_val == self:
                    setattr(old_value, "wh_ExprEq65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_ExprEq65"):
                opp_val = getattr(value, "wh_ExprEq65", None)
                setattr(value, "wh_ExprEq65", self)

class wh_ExprAnd:

    pass
class wh_Foreach:

    pass
class wh_LExpr:

    pass
class wh_If:

    pass
class wh_For:

    pass
class wh_Expr:

    pass
class wh_While:

    pass
class wh_Exprs:

    pass
class wh_Vars:

    def __init__(self, variables: str, wh_Vars: "wh_Assign" = None):
        self.variables = variables
        self.wh_Vars = wh_Vars
        
    @property
    def variables(self) -> str:
        return self.__variables

    @variables.setter
    def variables(self, variables: str):
        self.__variables = variables

    @property
    def wh_Vars(self):
        return self.__wh_Vars

    @wh_Vars.setter
    def wh_Vars(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Vars__wh_Vars", None)
        self.__wh_Vars = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Assign"):
                opp_val = getattr(old_value, "wh_Assign", None)
                if opp_val == self:
                    setattr(old_value, "wh_Assign", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Assign"):
                opp_val = getattr(value, "wh_Assign", None)
                setattr(value, "wh_Assign", self)

class wh_Assign:

    pass
class wh_Nop:

    def __init__(self, nop: str):
        self.nop = nop
        
    @property
    def nop(self) -> str:
        return self.__nop

    @nop.setter
    def nop(self, nop: str):
        self.__nop = nop

class wh_EObject:

    pass
class wh_Command:

    pass
class wh_Output:

    def __init__(self, r_values: str, wh_Output: "wh_Definition" = None):
        self.r_values = r_values
        self.wh_Output = wh_Output
        
    @property
    def r_values(self) -> str:
        return self.__r_values

    @r_values.setter
    def r_values(self, r_values: str):
        self.__r_values = r_values

    @property
    def wh_Output(self):
        return self.__wh_Output

    @wh_Output.setter
    def wh_Output(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Output__wh_Output", None)
        self.__wh_Output = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Definition10"):
                opp_val = getattr(old_value, "wh_Definition10", None)
                if opp_val == self:
                    setattr(old_value, "wh_Definition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Definition10"):
                opp_val = getattr(value, "wh_Definition10", None)
                setattr(value, "wh_Definition10", self)

class wh_Commands:

    pass
class wh_Input:

    def __init__(self, params: str, wh_Input: "wh_Definition" = None):
        self.params = params
        self.wh_Input = wh_Input
        
    @property
    def params(self) -> str:
        return self.__params

    @params.setter
    def params(self, params: str):
        self.__params = params

    @property
    def wh_Input(self):
        return self.__wh_Input

    @wh_Input.setter
    def wh_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Input__wh_Input", None)
        self.__wh_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Definition6"):
                opp_val = getattr(old_value, "wh_Definition6", None)
                if opp_val == self:
                    setattr(old_value, "wh_Definition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Definition6"):
                opp_val = getattr(value, "wh_Definition6", None)
                setattr(value, "wh_Definition6", self)

class wh_Definition:

    pass
class wh_Function:

    def __init__(self, fname: str, wh_Function: "wh_Program" = None, wh_Function4: "wh_Definition" = None):
        self.fname = fname
        self.wh_Function = wh_Function
        self.wh_Function4 = wh_Function4
        
    @property
    def fname(self) -> str:
        return self.__fname

    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

    @property
    def wh_Function(self):
        return self.__wh_Function

    @wh_Function.setter
    def wh_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Function__wh_Function", None)
        self.__wh_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Program2"):
                opp_val = getattr(old_value, "wh_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Program2"):
                opp_val = getattr(value, "wh_Program2", None)
                if opp_val is None:
                    setattr(value, "wh_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wh_Function4(self):
        return self.__wh_Function4

    @wh_Function4.setter
    def wh_Function4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wh_Function__wh_Function4", None)
        self.__wh_Function4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wh_Definition"):
                opp_val = getattr(old_value, "wh_Definition", None)
                if opp_val == self:
                    setattr(old_value, "wh_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wh_Definition"):
                opp_val = getattr(value, "wh_Definition", None)
                setattr(value, "wh_Definition", self)

class wh_Program:

    pass
class wh_Model:

    pass