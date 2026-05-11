from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class IntBinaryOperation:

    pass
class gx10_Time(IntBinaryOperation):

    pass
class gx10_Plus(IntBinaryOperation):

    pass
class IntExpression:

    pass
class gx10_IntVarAccess(IntExpression):

    pass
class gx10_IntBinaryOperation(IntExpression):

    def __init__(self, gx10_IntBinaryOperation: "gx10_IntExpression" = None, gx10_IntBinaryOperation28: "gx10_IntExpression" = None):
        self.gx10_IntBinaryOperation = gx10_IntBinaryOperation
        self.gx10_IntBinaryOperation28 = gx10_IntBinaryOperation28
        
        pass
    @property
    def gx10_IntBinaryOperation28(self):
        return self.__gx10_IntBinaryOperation28

    @gx10_IntBinaryOperation28.setter
    def gx10_IntBinaryOperation28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntBinaryOperation__gx10_IntBinaryOperation28", None)
        self.__gx10_IntBinaryOperation28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntExpression29"):
                opp_val = getattr(old_value, "gx10_IntExpression29", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntExpression29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntExpression29"):
                opp_val = getattr(value, "gx10_IntExpression29", None)
                setattr(value, "gx10_IntExpression29", self)

    @property
    def gx10_IntBinaryOperation(self):
        return self.__gx10_IntBinaryOperation

    @gx10_IntBinaryOperation.setter
    def gx10_IntBinaryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntBinaryOperation__gx10_IntBinaryOperation", None)
        self.__gx10_IntBinaryOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntExpression"):
                opp_val = getattr(old_value, "gx10_IntExpression", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntExpression"):
                opp_val = getattr(value, "gx10_IntExpression", None)
                setattr(value, "gx10_IntExpression", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class gx10_IntConst(IntExpression):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class gx10_Statement(ABC):

    pass
class Statement:

    pass
class gx10_IntVar(Statement):

    def __init__(self, gx10_IntVar: "gx10_IntExpression" = None, gx10_IntVar46: "gx10_Referentiable" = None):
        self.gx10_IntVar = gx10_IntVar
        self.gx10_IntVar46 = gx10_IntVar46
        
        pass
    @property
    def gx10_IntVar46(self):
        return self.__gx10_IntVar46

    @gx10_IntVar46.setter
    def gx10_IntVar46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntVar__gx10_IntVar46", None)
        self.__gx10_IntVar46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Referentiable47"):
                opp_val = getattr(old_value, "gx10_Referentiable47", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Referentiable47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Referentiable47"):
                opp_val = getattr(value, "gx10_Referentiable47", None)
                setattr(value, "gx10_Referentiable47", self)

    @property
    def gx10_IntVar(self):
        return self.__gx10_IntVar

    @gx10_IntVar.setter
    def gx10_IntVar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntVar__gx10_IntVar", None)
        self.__gx10_IntVar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntExpression44"):
                opp_val = getattr(old_value, "gx10_IntExpression44", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntExpression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntExpression44"):
                opp_val = getattr(value, "gx10_IntExpression44", None)
                setattr(value, "gx10_IntExpression44", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class gx10_Finish(Statement):

    pass
class gx10_Print(Statement):

    def __init__(self, gx10_Print: "gx10_Expression" = None):
        self.gx10_Print = gx10_Print
        
        pass
    @property
    def gx10_Print(self):
        return self.__gx10_Print

    @gx10_Print.setter
    def gx10_Print(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Print__gx10_Print", None)
        self.__gx10_Print = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Expression"):
                opp_val = getattr(old_value, "gx10_Expression", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Expression"):
                opp_val = getattr(value, "gx10_Expression", None)
                setattr(value, "gx10_Expression", self)

    def print(self):
        # TODO: Implement print method
        pass

class gx10_Async(Statement):

    pass
class gx10_Expression(Statement):

    pass
class gx10_Referentiable:

    def __init__(self, name: str, gx10_Referentiable: "gx10_Method" = None, gx10_Referentiable51: "gx10_BoolVarAccess" = None, gx10_Referentiable42: "gx10_BoolVar" = None, gx10_Referentiable47: "gx10_IntVar" = None, gx10_Referentiable49: "gx10_IntVarAccess" = None):
        self.name = name
        self.gx10_Referentiable = gx10_Referentiable
        self.gx10_Referentiable51 = gx10_Referentiable51
        self.gx10_Referentiable42 = gx10_Referentiable42
        self.gx10_Referentiable47 = gx10_Referentiable47
        self.gx10_Referentiable49 = gx10_Referentiable49
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def gx10_Referentiable(self):
        return self.__gx10_Referentiable

    @gx10_Referentiable.setter
    def gx10_Referentiable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Referentiable__gx10_Referentiable", None)
        self.__gx10_Referentiable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Method7"):
                opp_val = getattr(old_value, "gx10_Method7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Method7"):
                opp_val = getattr(value, "gx10_Method7", None)
                if opp_val is None:
                    setattr(value, "gx10_Method7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gx10_Referentiable47(self):
        return self.__gx10_Referentiable47

    @gx10_Referentiable47.setter
    def gx10_Referentiable47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Referentiable__gx10_Referentiable47", None)
        self.__gx10_Referentiable47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntVar46"):
                opp_val = getattr(old_value, "gx10_IntVar46", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntVar46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntVar46"):
                opp_val = getattr(value, "gx10_IntVar46", None)
                setattr(value, "gx10_IntVar46", self)

    @property
    def gx10_Referentiable51(self):
        return self.__gx10_Referentiable51

    @gx10_Referentiable51.setter
    def gx10_Referentiable51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Referentiable__gx10_Referentiable51", None)
        self.__gx10_Referentiable51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_BoolVarAccess"):
                opp_val = getattr(old_value, "gx10_BoolVarAccess", None)
                if opp_val == self:
                    setattr(old_value, "gx10_BoolVarAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_BoolVarAccess"):
                opp_val = getattr(value, "gx10_BoolVarAccess", None)
                setattr(value, "gx10_BoolVarAccess", self)

    @property
    def gx10_Referentiable49(self):
        return self.__gx10_Referentiable49

    @gx10_Referentiable49.setter
    def gx10_Referentiable49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Referentiable__gx10_Referentiable49", None)
        self.__gx10_Referentiable49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntVarAccess"):
                opp_val = getattr(old_value, "gx10_IntVarAccess", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntVarAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntVarAccess"):
                opp_val = getattr(value, "gx10_IntVarAccess", None)
                setattr(value, "gx10_IntVarAccess", self)

    @property
    def gx10_Referentiable42(self):
        return self.__gx10_Referentiable42

    @gx10_Referentiable42.setter
    def gx10_Referentiable42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Referentiable__gx10_Referentiable42", None)
        self.__gx10_Referentiable42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_BoolVar41"):
                opp_val = getattr(old_value, "gx10_BoolVar41", None)
                if opp_val == self:
                    setattr(old_value, "gx10_BoolVar41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_BoolVar41"):
                opp_val = getattr(value, "gx10_BoolVar41", None)
                setattr(value, "gx10_BoolVar41", self)

class BoolExpression:

    pass
class gx10_Equal(BoolExpression):

    def __init__(self, gx10_Equal: "gx10_IntExpression" = None, gx10_Equal55: "gx10_IntExpression" = None):
        self.gx10_Equal = gx10_Equal
        self.gx10_Equal55 = gx10_Equal55
        
        pass
    @property
    def gx10_Equal55(self):
        return self.__gx10_Equal55

    @gx10_Equal55.setter
    def gx10_Equal55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Equal__gx10_Equal55", None)
        self.__gx10_Equal55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntExpression56"):
                opp_val = getattr(old_value, "gx10_IntExpression56", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntExpression56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntExpression56"):
                opp_val = getattr(value, "gx10_IntExpression56", None)
                setattr(value, "gx10_IntExpression56", self)

    @property
    def gx10_Equal(self):
        return self.__gx10_Equal

    @gx10_Equal.setter
    def gx10_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Equal__gx10_Equal", None)
        self.__gx10_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntExpression53"):
                opp_val = getattr(old_value, "gx10_IntExpression53", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntExpression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntExpression53"):
                opp_val = getattr(value, "gx10_IntExpression53", None)
                setattr(value, "gx10_IntExpression53", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class gx10_And(BoolExpression):

    pass
class gx10_False(BoolExpression):

    pass
class gx10_BoolVarAccess(BoolExpression):

    pass
class gx10_Not(BoolExpression):

    pass
class gx10_True(BoolExpression):

    pass
class ControlStructure:

    pass
class gx10_While(ControlStructure):

    pass
class gx10_If(ControlStructure):

    pass
class gx10_MethodCallParameter:

    def __init__(self, name: str, inMethodCallParameter: "gx10_IntExpression" = None, methodCallParameters: "gx10_MethodCall" = None, MethodCallParameter: "gx10_IntExpression" = None, MethodCallParameter34: "gx10_MethodCall" = None):
        self.name = name
        self.inMethodCallParameter = inMethodCallParameter
        self.methodCallParameters = methodCallParameters
        self.MethodCallParameter = MethodCallParameter
        self.MethodCallParameter34 = MethodCallParameter34
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def inMethodCallParameter(self):
        return self.__inMethodCallParameter

    @inMethodCallParameter.setter
    def inMethodCallParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCallParameter__inMethodCallParameter", None)
        self.__inMethodCallParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IntExpression"):
                opp_val = getattr(old_value, "IntExpression", None)
                if opp_val == self:
                    setattr(old_value, "IntExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IntExpression"):
                opp_val = getattr(value, "IntExpression", None)
                setattr(value, "IntExpression", self)

    @property
    def MethodCallParameter(self):
        return self.__MethodCallParameter

    @MethodCallParameter.setter
    def MethodCallParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCallParameter__MethodCallParameter", None)
        self.__MethodCallParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methodCallParameterExpr"):
                opp_val = getattr(old_value, "methodCallParameterExpr", None)
                if opp_val == self:
                    setattr(old_value, "methodCallParameterExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methodCallParameterExpr"):
                opp_val = getattr(value, "methodCallParameterExpr", None)
                setattr(value, "methodCallParameterExpr", self)

    @property
    def MethodCallParameter34(self):
        return self.__MethodCallParameter34

    @MethodCallParameter34.setter
    def MethodCallParameter34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCallParameter__MethodCallParameter34", None)
        self.__MethodCallParameter34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inMethodCall"):
                opp_val = getattr(old_value, "inMethodCall", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inMethodCall"):
                opp_val = getattr(value, "inMethodCall", None)
                if opp_val is None:
                    setattr(value, "inMethodCall", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def methodCallParameters(self):
        return self.__methodCallParameters

    @methodCallParameters.setter
    def methodCallParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCallParameter__methodCallParameters", None)
        self.__methodCallParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MethodCall59"):
                opp_val = getattr(old_value, "MethodCall59", None)
                if opp_val == self:
                    setattr(old_value, "MethodCall59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MethodCall59"):
                opp_val = getattr(value, "MethodCall59", None)
                setattr(value, "MethodCall59", self)

class Expression:

    pass
class gx10_BoolVar(Expression):

    def __init__(self, gx10_BoolVar: "gx10_BoolExpression" = None, gx10_BoolVar41: "gx10_Referentiable" = None):
        self.gx10_BoolVar = gx10_BoolVar
        self.gx10_BoolVar41 = gx10_BoolVar41
        
        pass
    @property
    def gx10_BoolVar41(self):
        return self.__gx10_BoolVar41

    @gx10_BoolVar41.setter
    def gx10_BoolVar41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolVar__gx10_BoolVar41", None)
        self.__gx10_BoolVar41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Referentiable42"):
                opp_val = getattr(old_value, "gx10_Referentiable42", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Referentiable42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Referentiable42"):
                opp_val = getattr(value, "gx10_Referentiable42", None)
                setattr(value, "gx10_Referentiable42", self)

    @property
    def gx10_BoolVar(self):
        return self.__gx10_BoolVar

    @gx10_BoolVar.setter
    def gx10_BoolVar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolVar__gx10_BoolVar", None)
        self.__gx10_BoolVar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_BoolExpression39"):
                opp_val = getattr(old_value, "gx10_BoolExpression39", None)
                if opp_val == self:
                    setattr(old_value, "gx10_BoolExpression39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_BoolExpression39"):
                opp_val = getattr(value, "gx10_BoolExpression39", None)
                setattr(value, "gx10_BoolExpression39", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class gx10_MethodCall(Expression):

    def __init__(self, MethodCall59: "gx10_MethodCallParameter" = None, MethodCall: "gx10_Method" = None, calledBy: "gx10_Method" = None, inMethodCall: set["gx10_MethodCallParameter"] = None):
        self.MethodCall59 = MethodCall59
        self.MethodCall = MethodCall
        self.calledBy = calledBy
        self.inMethodCall = inMethodCall if inMethodCall is not None else set()
        
        pass
    @property
    def inMethodCall(self):
        return self.__inMethodCall

    @inMethodCall.setter
    def inMethodCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCall__inMethodCall", None)
        self.__inMethodCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MethodCallParameter34"):
                    opp_val = getattr(item, "MethodCallParameter34", None)
                    
                    if opp_val == self:
                        setattr(item, "MethodCallParameter34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MethodCallParameter34"):
                    opp_val = getattr(item, "MethodCallParameter34", None)
                    
                    setattr(item, "MethodCallParameter34", self)
                    

    @property
    def MethodCall(self):
        return self.__MethodCall

    @MethodCall.setter
    def MethodCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCall__MethodCall", None)
        self.__MethodCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methodToCall"):
                opp_val = getattr(old_value, "methodToCall", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methodToCall"):
                opp_val = getattr(value, "methodToCall", None)
                if opp_val is None:
                    setattr(value, "methodToCall", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MethodCall59(self):
        return self.__MethodCall59

    @MethodCall59.setter
    def MethodCall59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCall__MethodCall59", None)
        self.__MethodCall59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methodCallParameters"):
                opp_val = getattr(old_value, "methodCallParameters", None)
                if opp_val == self:
                    setattr(old_value, "methodCallParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methodCallParameters"):
                opp_val = getattr(value, "methodCallParameters", None)
                setattr(value, "methodCallParameters", self)

    @property
    def calledBy(self):
        return self.__calledBy

    @calledBy.setter
    def calledBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_MethodCall__calledBy", None)
        self.__calledBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Method32"):
                opp_val = getattr(old_value, "Method32", None)
                if opp_val == self:
                    setattr(old_value, "Method32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Method32"):
                opp_val = getattr(value, "Method32", None)
                setattr(value, "Method32", self)

    def call(self):
        # TODO: Implement call method
        pass

class gx10_IntExpression(Expression):

    def __init__(self, gx10_IntExpression53: "gx10_Equal" = None, gx10_IntExpression56: "gx10_Equal" = None, methodCallParameterExpr: "gx10_MethodCallParameter" = None, gx10_IntExpression: "gx10_IntBinaryOperation" = None, gx10_IntExpression29: "gx10_IntBinaryOperation" = None, gx10_IntExpression44: "gx10_IntVar" = None, IntExpression: "gx10_MethodCallParameter" = None):
        self.gx10_IntExpression53 = gx10_IntExpression53
        self.gx10_IntExpression56 = gx10_IntExpression56
        self.methodCallParameterExpr = methodCallParameterExpr
        self.gx10_IntExpression = gx10_IntExpression
        self.gx10_IntExpression29 = gx10_IntExpression29
        self.gx10_IntExpression44 = gx10_IntExpression44
        self.IntExpression = IntExpression
        
        pass
    @property
    def IntExpression(self):
        return self.__IntExpression

    @IntExpression.setter
    def IntExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__IntExpression", None)
        self.__IntExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inMethodCallParameter"):
                opp_val = getattr(old_value, "inMethodCallParameter", None)
                if opp_val == self:
                    setattr(old_value, "inMethodCallParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inMethodCallParameter"):
                opp_val = getattr(value, "inMethodCallParameter", None)
                setattr(value, "inMethodCallParameter", self)

    @property
    def gx10_IntExpression(self):
        return self.__gx10_IntExpression

    @gx10_IntExpression.setter
    def gx10_IntExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__gx10_IntExpression", None)
        self.__gx10_IntExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntBinaryOperation"):
                opp_val = getattr(old_value, "gx10_IntBinaryOperation", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntBinaryOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntBinaryOperation"):
                opp_val = getattr(value, "gx10_IntBinaryOperation", None)
                setattr(value, "gx10_IntBinaryOperation", self)

    @property
    def gx10_IntExpression29(self):
        return self.__gx10_IntExpression29

    @gx10_IntExpression29.setter
    def gx10_IntExpression29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__gx10_IntExpression29", None)
        self.__gx10_IntExpression29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntBinaryOperation28"):
                opp_val = getattr(old_value, "gx10_IntBinaryOperation28", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntBinaryOperation28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntBinaryOperation28"):
                opp_val = getattr(value, "gx10_IntBinaryOperation28", None)
                setattr(value, "gx10_IntBinaryOperation28", self)

    @property
    def gx10_IntExpression56(self):
        return self.__gx10_IntExpression56

    @gx10_IntExpression56.setter
    def gx10_IntExpression56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__gx10_IntExpression56", None)
        self.__gx10_IntExpression56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Equal55"):
                opp_val = getattr(old_value, "gx10_Equal55", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Equal55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Equal55"):
                opp_val = getattr(value, "gx10_Equal55", None)
                setattr(value, "gx10_Equal55", self)

    @property
    def methodCallParameterExpr(self):
        return self.__methodCallParameterExpr

    @methodCallParameterExpr.setter
    def methodCallParameterExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__methodCallParameterExpr", None)
        self.__methodCallParameterExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MethodCallParameter"):
                opp_val = getattr(old_value, "MethodCallParameter", None)
                if opp_val == self:
                    setattr(old_value, "MethodCallParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MethodCallParameter"):
                opp_val = getattr(value, "MethodCallParameter", None)
                setattr(value, "MethodCallParameter", self)

    @property
    def gx10_IntExpression53(self):
        return self.__gx10_IntExpression53

    @gx10_IntExpression53.setter
    def gx10_IntExpression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__gx10_IntExpression53", None)
        self.__gx10_IntExpression53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Equal"):
                opp_val = getattr(old_value, "gx10_Equal", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Equal"):
                opp_val = getattr(value, "gx10_Equal", None)
                setattr(value, "gx10_Equal", self)

    @property
    def gx10_IntExpression44(self):
        return self.__gx10_IntExpression44

    @gx10_IntExpression44.setter
    def gx10_IntExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_IntExpression__gx10_IntExpression44", None)
        self.__gx10_IntExpression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_IntVar"):
                opp_val = getattr(old_value, "gx10_IntVar", None)
                if opp_val == self:
                    setattr(old_value, "gx10_IntVar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_IntVar"):
                opp_val = getattr(value, "gx10_IntVar", None)
                setattr(value, "gx10_IntVar", self)

    def getCurrentValue(self):
        # TODO: Implement getCurrentValue method
        pass

class gx10_BoolExpression(Expression):

    def __init__(self, gx10_BoolExpression: "gx10_ControlStructure" = None, gx10_BoolExpression20: "gx10_Not" = None, gx10_BoolExpression22: "gx10_And" = None, gx10_BoolExpression25: "gx10_And" = None, gx10_BoolExpression39: "gx10_BoolVar" = None):
        self.gx10_BoolExpression = gx10_BoolExpression
        self.gx10_BoolExpression20 = gx10_BoolExpression20
        self.gx10_BoolExpression22 = gx10_BoolExpression22
        self.gx10_BoolExpression25 = gx10_BoolExpression25
        self.gx10_BoolExpression39 = gx10_BoolExpression39
        
        pass
    @property
    def gx10_BoolExpression39(self):
        return self.__gx10_BoolExpression39

    @gx10_BoolExpression39.setter
    def gx10_BoolExpression39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolExpression__gx10_BoolExpression39", None)
        self.__gx10_BoolExpression39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_BoolVar"):
                opp_val = getattr(old_value, "gx10_BoolVar", None)
                if opp_val == self:
                    setattr(old_value, "gx10_BoolVar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_BoolVar"):
                opp_val = getattr(value, "gx10_BoolVar", None)
                setattr(value, "gx10_BoolVar", self)

    @property
    def gx10_BoolExpression25(self):
        return self.__gx10_BoolExpression25

    @gx10_BoolExpression25.setter
    def gx10_BoolExpression25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolExpression__gx10_BoolExpression25", None)
        self.__gx10_BoolExpression25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_And24"):
                opp_val = getattr(old_value, "gx10_And24", None)
                if opp_val == self:
                    setattr(old_value, "gx10_And24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_And24"):
                opp_val = getattr(value, "gx10_And24", None)
                setattr(value, "gx10_And24", self)

    @property
    def gx10_BoolExpression22(self):
        return self.__gx10_BoolExpression22

    @gx10_BoolExpression22.setter
    def gx10_BoolExpression22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolExpression__gx10_BoolExpression22", None)
        self.__gx10_BoolExpression22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_And"):
                opp_val = getattr(old_value, "gx10_And", None)
                if opp_val == self:
                    setattr(old_value, "gx10_And", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_And"):
                opp_val = getattr(value, "gx10_And", None)
                setattr(value, "gx10_And", self)

    @property
    def gx10_BoolExpression(self):
        return self.__gx10_BoolExpression

    @gx10_BoolExpression.setter
    def gx10_BoolExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolExpression__gx10_BoolExpression", None)
        self.__gx10_BoolExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_ControlStructure"):
                opp_val = getattr(old_value, "gx10_ControlStructure", None)
                if opp_val == self:
                    setattr(old_value, "gx10_ControlStructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_ControlStructure"):
                opp_val = getattr(value, "gx10_ControlStructure", None)
                setattr(value, "gx10_ControlStructure", self)

    @property
    def gx10_BoolExpression20(self):
        return self.__gx10_BoolExpression20

    @gx10_BoolExpression20.setter
    def gx10_BoolExpression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_BoolExpression__gx10_BoolExpression20", None)
        self.__gx10_BoolExpression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Not"):
                opp_val = getattr(old_value, "gx10_Not", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Not", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Not"):
                opp_val = getattr(value, "gx10_Not", None)
                setattr(value, "gx10_Not", self)

    def getCurrentValue(self):
        # TODO: Implement getCurrentValue method
        pass

class gx10_ControlStructure(Statement):

    pass
class gx10_Block(Statement):

    def __init__(self, Block: "gx10_Statement" = None, gx10_Block13: "gx10_If" = None, gx10_Block16: "gx10_If" = None, gx10_Block18: "gx10_While" = None, gx10_Block: "gx10_Method" = None, inBlock: set["gx10_Statement"] = None):
        self.Block = Block
        self.gx10_Block13 = gx10_Block13
        self.gx10_Block16 = gx10_Block16
        self.gx10_Block18 = gx10_Block18
        self.gx10_Block = gx10_Block
        self.inBlock = inBlock if inBlock is not None else set()
        
        pass
    @property
    def inBlock(self):
        return self.__inBlock

    @inBlock.setter
    def inBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Block__inBlock", None)
        self.__inBlock = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement"):
                    opp_val = getattr(item, "Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement"):
                    opp_val = getattr(item, "Statement", None)
                    
                    setattr(item, "Statement", self)
                    

    @property
    def gx10_Block18(self):
        return self.__gx10_Block18

    @gx10_Block18.setter
    def gx10_Block18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Block__gx10_Block18", None)
        self.__gx10_Block18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_While"):
                opp_val = getattr(old_value, "gx10_While", None)
                if opp_val == self:
                    setattr(old_value, "gx10_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_While"):
                opp_val = getattr(value, "gx10_While", None)
                setattr(value, "gx10_While", self)

    @property
    def gx10_Block(self):
        return self.__gx10_Block

    @gx10_Block.setter
    def gx10_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Block__gx10_Block", None)
        self.__gx10_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Method4"):
                opp_val = getattr(old_value, "gx10_Method4", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Method4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Method4"):
                opp_val = getattr(value, "gx10_Method4", None)
                setattr(value, "gx10_Method4", self)

    @property
    def gx10_Block13(self):
        return self.__gx10_Block13

    @gx10_Block13.setter
    def gx10_Block13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Block__gx10_Block13", None)
        self.__gx10_Block13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_If"):
                opp_val = getattr(old_value, "gx10_If", None)
                if opp_val == self:
                    setattr(old_value, "gx10_If", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_If"):
                opp_val = getattr(value, "gx10_If", None)
                setattr(value, "gx10_If", self)

    @property
    def Block(self):
        return self.__Block

    @Block.setter
    def Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Block__Block", None)
        self.__Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blockStatements"):
                opp_val = getattr(old_value, "blockStatements", None)
                if opp_val == self:
                    setattr(old_value, "blockStatements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blockStatements"):
                opp_val = getattr(value, "blockStatements", None)
                setattr(value, "blockStatements", self)

    @property
    def gx10_Block16(self):
        return self.__gx10_Block16

    @gx10_Block16.setter
    def gx10_Block16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Block__gx10_Block16", None)
        self.__gx10_Block16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_If15"):
                opp_val = getattr(old_value, "gx10_If15", None)
                if opp_val == self:
                    setattr(old_value, "gx10_If15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_If15"):
                opp_val = getattr(value, "gx10_If15", None)
                setattr(value, "gx10_If15", self)

    def initBlock(self):
        # TODO: Implement initBlock method
        pass

class gx10_Method:

    def __init__(self, name: bool, Method: "gx10_Program" = None, gx10_Method: "gx10_Program" = None, methods: "gx10_Program" = None, gx10_Method4: "gx10_Block" = None, methodToCall: set["gx10_MethodCall"] = None, gx10_Method7: set["gx10_Referentiable"] = None, Method32: "gx10_MethodCall" = None):
        self.name = name
        self.Method = Method
        self.gx10_Method = gx10_Method
        self.methods = methods
        self.gx10_Method4 = gx10_Method4
        self.methodToCall = methodToCall if methodToCall is not None else set()
        self.gx10_Method7 = gx10_Method7 if gx10_Method7 is not None else set()
        self.Method32 = Method32
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name


    @property
    def methodToCall(self):
        return self.__methodToCall

    @methodToCall.setter
    def methodToCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__methodToCall", None)
        self.__methodToCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MethodCall"):
                    opp_val = getattr(item, "MethodCall", None)
                    
                    if opp_val == self:
                        setattr(item, "MethodCall", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MethodCall"):
                    opp_val = getattr(item, "MethodCall", None)
                    
                    setattr(item, "MethodCall", self)
                    

    @property
    def gx10_Method(self):
        return self.__gx10_Method

    @gx10_Method.setter
    def gx10_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__gx10_Method", None)
        self.__gx10_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Program"):
                opp_val = getattr(old_value, "gx10_Program", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Program"):
                opp_val = getattr(value, "gx10_Program", None)
                setattr(value, "gx10_Program", self)

    @property
    def Method32(self):
        return self.__Method32

    @Method32.setter
    def Method32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__Method32", None)
        self.__Method32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calledBy"):
                opp_val = getattr(old_value, "calledBy", None)
                if opp_val == self:
                    setattr(old_value, "calledBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calledBy"):
                opp_val = getattr(value, "calledBy", None)
                setattr(value, "calledBy", self)

    @property
    def gx10_Method7(self):
        return self.__gx10_Method7

    @gx10_Method7.setter
    def gx10_Method7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__gx10_Method7", None)
        self.__gx10_Method7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gx10_Referentiable"):
                    opp_val = getattr(item, "gx10_Referentiable", None)
                    
                    if opp_val == self:
                        setattr(item, "gx10_Referentiable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gx10_Referentiable"):
                    opp_val = getattr(item, "gx10_Referentiable", None)
                    
                    setattr(item, "gx10_Referentiable", self)
                    

    @property
    def gx10_Method4(self):
        return self.__gx10_Method4

    @gx10_Method4.setter
    def gx10_Method4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__gx10_Method4", None)
        self.__gx10_Method4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gx10_Block"):
                opp_val = getattr(old_value, "gx10_Block", None)
                if opp_val == self:
                    setattr(old_value, "gx10_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gx10_Block"):
                opp_val = getattr(value, "gx10_Block", None)
                setattr(value, "gx10_Block", self)

    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__methods", None)
        self.__methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program"):
                opp_val = getattr(old_value, "Program", None)
                if opp_val == self:
                    setattr(old_value, "Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program"):
                opp_val = getattr(value, "Program", None)
                setattr(value, "Program", self)

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gx10_Method__Method", None)
        self.__Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inProgram"):
                opp_val = getattr(old_value, "inProgram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inProgram"):
                opp_val = getattr(value, "inProgram", None)
                if opp_val is None:
                    setattr(value, "inProgram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gx10_Program:

    pass