from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Operation:

    pass
class gseq_While(Operation):

    pass
class gseq_IntegerExpression(Operation):

    def __init__(self, gseq_IntegerExpression29: "gseq_Assign" = None, gseq_IntegerExpression31: "gseq_Plus" = None, gseq_IntegerExpression: "gseq_Equality" = None, gseq_IntegerExpression20: "gseq_Equality" = None, gseq_IntegerExpression34: "gseq_Plus" = None, gseq_IntegerExpression36: "gseq_GreaterThan" = None, gseq_IntegerExpression39: "gseq_GreaterThan" = None, gseq_IntegerExpression44: "gseq_While" = None):
        self.gseq_IntegerExpression29 = gseq_IntegerExpression29
        self.gseq_IntegerExpression31 = gseq_IntegerExpression31
        self.gseq_IntegerExpression = gseq_IntegerExpression
        self.gseq_IntegerExpression20 = gseq_IntegerExpression20
        self.gseq_IntegerExpression34 = gseq_IntegerExpression34
        self.gseq_IntegerExpression36 = gseq_IntegerExpression36
        self.gseq_IntegerExpression39 = gseq_IntegerExpression39
        self.gseq_IntegerExpression44 = gseq_IntegerExpression44
        
    @property
    def gseq_IntegerExpression(self):
        return self.__gseq_IntegerExpression

    @gseq_IntegerExpression.setter
    def gseq_IntegerExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_IntegerExpression__gseq_IntegerExpression", None)
        self.__gseq_IntegerExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_Equality"):
                opp_val = getattr(old_value, "gseq_Equality", None)
                if opp_val == self:
                    setattr(old_value, "gseq_Equality", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_Equality"):
                opp_val = getattr(value, "gseq_Equality", None)
                setattr(value, "gseq_Equality", self)

    @property
    def gseq_IntegerExpression31(self):
        return self.__gseq_IntegerExpression31

    @gseq_IntegerExpression31.setter
    def gseq_IntegerExpression31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_IntegerExpression__gseq_IntegerExpression31", None)
        self.__gseq_IntegerExpression31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_Plus"):
                opp_val = getattr(old_value, "gseq_Plus", None)
                if opp_val == self:
                    setattr(old_value, "gseq_Plus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_Plus"):
                opp_val = getattr(value, "gseq_Plus", None)
                setattr(value, "gseq_Plus", self)

    @property
    def gseq_IntegerExpression34(self):
        return self.__gseq_IntegerExpression34

    @gseq_IntegerExpression34.setter
    def gseq_IntegerExpression34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_IntegerExpression__gseq_IntegerExpression34", None)
        self.__gseq_IntegerExpression34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_Plus33"):
                opp_val = getattr(old_value, "gseq_Plus33", None)
                if opp_val == self:
                    setattr(old_value, "gseq_Plus33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_Plus33"):
                opp_val = getattr(value, "gseq_Plus33", None)
                setattr(value, "gseq_Plus33", self)

    @property
    def gseq_IntegerExpression44(self):
        return self.__gseq_IntegerExpression44

    @gseq_IntegerExpression44.setter
    def gseq_IntegerExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_IntegerExpression__gseq_IntegerExpression44", None)
        self.__gseq_IntegerExpression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_While43"):
                opp_val = getattr(old_value, "gseq_While43", None)
                if opp_val == self:
                    setattr(old_value, "gseq_While43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_While43"):
                opp_val = getattr(value, "gseq_While43", None)
                setattr(value, "gseq_While43", self)

    @property
    def gseq_IntegerExpression20(self):
        return self.__gseq_IntegerExpression20

    @gseq_IntegerExpression20.setter
    def gseq_IntegerExpression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_IntegerExpression__gseq_IntegerExpression20", None)
        self.__gseq_IntegerExpression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_Equality19"):
                opp_val = getattr(old_value, "gseq_Equality19", None)
                if opp_val == self:
                    setattr(old_value, "gseq_Equality19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_Equality19"):
                opp_val = getattr(value, "gseq_Equality19", None)
                setattr(value, "gseq_Equality19", self)

    @property
    def gseq_IntegerExpression36(self):
        return self.__gseq_IntegerExpression36

    @gseq_IntegerExpression36.setter
    def gseq_IntegerExpression36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_IntegerExpression__gseq_IntegerExpression36", None)
        self.__gseq_IntegerExpression36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_GreaterThan"):
                opp_val = getattr(old_value, "gseq_GreaterThan", None)
                if opp_val == self:
                    setattr(old_value, "gseq_GreaterThan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_GreaterThan"):
                opp_val = getattr(value, "gseq_GreaterThan", None)
                setattr(value, "gseq_GreaterThan", self)

    @property
    def gseq_IntegerExpression29(self):
        return self.__gseq_IntegerExpression29

    @gseq_IntegerExpression29.setter
    def gseq_IntegerExpression29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_IntegerExpression__gseq_IntegerExpression29", None)
        self.__gseq_IntegerExpression29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_Assign"):
                opp_val = getattr(old_value, "gseq_Assign", None)
                if opp_val == self:
                    setattr(old_value, "gseq_Assign", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_Assign"):
                opp_val = getattr(value, "gseq_Assign", None)
                setattr(value, "gseq_Assign", self)

    @property
    def gseq_IntegerExpression39(self):
        return self.__gseq_IntegerExpression39

    @gseq_IntegerExpression39.setter
    def gseq_IntegerExpression39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_IntegerExpression__gseq_IntegerExpression39", None)
        self.__gseq_IntegerExpression39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_GreaterThan38"):
                opp_val = getattr(old_value, "gseq_GreaterThan38", None)
                if opp_val == self:
                    setattr(old_value, "gseq_GreaterThan38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_GreaterThan38"):
                opp_val = getattr(value, "gseq_GreaterThan38", None)
                setattr(value, "gseq_GreaterThan38", self)

    def ivalue(self) -> str:
        # TODO: Implement ivalue method
        pass

    def pretty(self) -> str:
        # TODO: Implement pretty method
        pass

class gseq_Assign(Operation):

    def __init__(self, varName: str, gseq_Assign: "gseq_IntegerExpression" = None):
        self.varName = varName
        self.gseq_Assign = gseq_Assign
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def gseq_Assign(self):
        return self.__gseq_Assign

    @gseq_Assign.setter
    def gseq_Assign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Assign__gseq_Assign", None)
        self.__gseq_Assign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_IntegerExpression29"):
                opp_val = getattr(old_value, "gseq_IntegerExpression29", None)
                if opp_val == self:
                    setattr(old_value, "gseq_IntegerExpression29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_IntegerExpression29"):
                opp_val = getattr(value, "gseq_IntegerExpression29", None)
                setattr(value, "gseq_IntegerExpression29", self)

class gseq_Print(Operation):

    def __init__(self, gseq_Print: "gseq_Operation" = None):
        self.gseq_Print = gseq_Print
        
    @property
    def gseq_Print(self):
        return self.__gseq_Print

    @gseq_Print.setter
    def gseq_Print(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Print__gseq_Print", None)
        self.__gseq_Print = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_Operation"):
                opp_val = getattr(old_value, "gseq_Operation", None)
                if opp_val == self:
                    setattr(old_value, "gseq_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_Operation"):
                opp_val = getattr(value, "gseq_Operation", None)
                setattr(value, "gseq_Operation", self)

    def print(self):
        # TODO: Implement print method
        pass

class BooleanExpression:

    pass
class gseq_And(BooleanExpression):

    pass
class gseq_Not(BooleanExpression):

    pass
class gseq_Equality(BooleanExpression):

    pass
class gseq_GreaterThan(BooleanExpression):

    pass
class gseq_False(BooleanExpression):

    pass
class gseq_True(BooleanExpression):

    pass
class gseq_If(Operation):

    pass
class gseq_BooleanExpression(Operation):

    def __init__(self, gseq_BooleanExpression: "gseq_If" = None, gseq_BooleanExpression27: "gseq_And" = None, gseq_BooleanExpression22: "gseq_Not" = None, gseq_BooleanExpression24: "gseq_And" = None, gseq_BooleanExpression41: "gseq_While" = None):
        self.gseq_BooleanExpression = gseq_BooleanExpression
        self.gseq_BooleanExpression27 = gseq_BooleanExpression27
        self.gseq_BooleanExpression22 = gseq_BooleanExpression22
        self.gseq_BooleanExpression24 = gseq_BooleanExpression24
        self.gseq_BooleanExpression41 = gseq_BooleanExpression41
        
    @property
    def gseq_BooleanExpression22(self):
        return self.__gseq_BooleanExpression22

    @gseq_BooleanExpression22.setter
    def gseq_BooleanExpression22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_BooleanExpression__gseq_BooleanExpression22", None)
        self.__gseq_BooleanExpression22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_Not"):
                opp_val = getattr(old_value, "gseq_Not", None)
                if opp_val == self:
                    setattr(old_value, "gseq_Not", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_Not"):
                opp_val = getattr(value, "gseq_Not", None)
                setattr(value, "gseq_Not", self)

    @property
    def gseq_BooleanExpression27(self):
        return self.__gseq_BooleanExpression27

    @gseq_BooleanExpression27.setter
    def gseq_BooleanExpression27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_BooleanExpression__gseq_BooleanExpression27", None)
        self.__gseq_BooleanExpression27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_And26"):
                opp_val = getattr(old_value, "gseq_And26", None)
                if opp_val == self:
                    setattr(old_value, "gseq_And26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_And26"):
                opp_val = getattr(value, "gseq_And26", None)
                setattr(value, "gseq_And26", self)

    @property
    def gseq_BooleanExpression(self):
        return self.__gseq_BooleanExpression

    @gseq_BooleanExpression.setter
    def gseq_BooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_BooleanExpression__gseq_BooleanExpression", None)
        self.__gseq_BooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_If16"):
                opp_val = getattr(old_value, "gseq_If16", None)
                if opp_val == self:
                    setattr(old_value, "gseq_If16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_If16"):
                opp_val = getattr(value, "gseq_If16", None)
                setattr(value, "gseq_If16", self)

    @property
    def gseq_BooleanExpression41(self):
        return self.__gseq_BooleanExpression41

    @gseq_BooleanExpression41.setter
    def gseq_BooleanExpression41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_BooleanExpression__gseq_BooleanExpression41", None)
        self.__gseq_BooleanExpression41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_While"):
                opp_val = getattr(old_value, "gseq_While", None)
                if opp_val == self:
                    setattr(old_value, "gseq_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_While"):
                opp_val = getattr(value, "gseq_While", None)
                setattr(value, "gseq_While", self)

    @property
    def gseq_BooleanExpression24(self):
        return self.__gseq_BooleanExpression24

    @gseq_BooleanExpression24.setter
    def gseq_BooleanExpression24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_BooleanExpression__gseq_BooleanExpression24", None)
        self.__gseq_BooleanExpression24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_And"):
                opp_val = getattr(old_value, "gseq_And", None)
                if opp_val == self:
                    setattr(old_value, "gseq_And", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_And"):
                opp_val = getattr(value, "gseq_And", None)
                setattr(value, "gseq_And", self)

    def bvalue(self) -> bool:
        # TODO: Implement bvalue method
        pass

    def pretty(self) -> str:
        # TODO: Implement pretty method
        pass

class IntegerExpression:

    pass
class gseq_MethodCall(IntegerExpression):

    pass
class gseq_Plus(IntegerExpression):

    pass
class gseq_Const(IntegerExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class gseq_Var(IntegerExpression):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class gseq_Method:

    def __init__(self, name: str, Method: "gseq_Program" = None, gseq_Method: "gseq_Program" = None, executedBy: set["gseq_Operation"] = None, Method9: "gseq_MethodCall" = None, methods: "gseq_Program" = None, methodToCall: set["gseq_MethodCall"] = None, Method6: "gseq_Operation" = None):
        self.name = name
        self.Method = Method
        self.gseq_Method = gseq_Method
        self.executedBy = executedBy if executedBy is not None else set()
        self.Method9 = Method9
        self.methods = methods
        self.methodToCall = methodToCall if methodToCall is not None else set()
        self.Method6 = Method6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gseq_Method(self):
        return self.__gseq_Method

    @gseq_Method.setter
    def gseq_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Method__gseq_Method", None)
        self.__gseq_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_Program"):
                opp_val = getattr(old_value, "gseq_Program", None)
                if opp_val == self:
                    setattr(old_value, "gseq_Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_Program"):
                opp_val = getattr(value, "gseq_Program", None)
                setattr(value, "gseq_Program", self)

    @property
    def Method6(self):
        return self.__Method6

    @Method6.setter
    def Method6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Method__Method6", None)
        self.__Method6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operations"):
                opp_val = getattr(old_value, "operations", None)
                if opp_val == self:
                    setattr(old_value, "operations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operations"):
                opp_val = getattr(value, "operations", None)
                setattr(value, "operations", self)

    @property
    def Method9(self):
        return self.__Method9

    @Method9.setter
    def Method9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Method__Method9", None)
        self.__Method9 = value
        
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
    def executedBy(self):
        return self.__executedBy

    @executedBy.setter
    def executedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Method__executedBy", None)
        self.__executedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Method__methods", None)
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
        old_value = getattr(self, f"_gseq_Method__Method", None)
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

    @property
    def methodToCall(self):
        return self.__methodToCall

    @methodToCall.setter
    def methodToCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Method__methodToCall", None)
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
                    

    def call(self):
        # TODO: Implement call method
        pass

class gseq_Program:

    def __init__(self, inProgram: set["gseq_Method"] = None, gseq_Program: "gseq_Method" = None, Program: "gseq_Method" = None):
        self.inProgram = inProgram if inProgram is not None else set()
        self.gseq_Program = gseq_Program
        self.Program = Program
        
    @property
    def Program(self):
        return self.__Program

    @Program.setter
    def Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Program__Program", None)
        self.__Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methods"):
                opp_val = getattr(old_value, "methods", None)
                if opp_val == self:
                    setattr(old_value, "methods", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methods"):
                opp_val = getattr(value, "methods", None)
                setattr(value, "methods", self)

    @property
    def gseq_Program(self):
        return self.__gseq_Program

    @gseq_Program.setter
    def gseq_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Program__gseq_Program", None)
        self.__gseq_Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_Method"):
                opp_val = getattr(old_value, "gseq_Method", None)
                if opp_val == self:
                    setattr(old_value, "gseq_Method", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_Method"):
                opp_val = getattr(value, "gseq_Method", None)
                setattr(value, "gseq_Method", self)

    @property
    def inProgram(self):
        return self.__inProgram

    @inProgram.setter
    def inProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Program__inProgram", None)
        self.__inProgram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    setattr(item, "Method", self)
                    

    def init(self):
        # TODO: Implement init method
        pass

class gseq_Operation(ABC):

    def __init__(self, Operation: "gseq_Method" = None, gseq_Operation11: "gseq_If" = None, gseq_Operation14: "gseq_If" = None, operations: "gseq_Method" = None, gseq_Operation: "gseq_Print" = None):
        self.Operation = Operation
        self.gseq_Operation11 = gseq_Operation11
        self.gseq_Operation14 = gseq_Operation14
        self.operations = operations
        self.gseq_Operation = gseq_Operation
        
    @property
    def gseq_Operation14(self):
        return self.__gseq_Operation14

    @gseq_Operation14.setter
    def gseq_Operation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Operation__gseq_Operation14", None)
        self.__gseq_Operation14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_If13"):
                opp_val = getattr(old_value, "gseq_If13", None)
                if opp_val == self:
                    setattr(old_value, "gseq_If13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_If13"):
                opp_val = getattr(value, "gseq_If13", None)
                setattr(value, "gseq_If13", self)

    @property
    def gseq_Operation11(self):
        return self.__gseq_Operation11

    @gseq_Operation11.setter
    def gseq_Operation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Operation__gseq_Operation11", None)
        self.__gseq_Operation11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_If"):
                opp_val = getattr(old_value, "gseq_If", None)
                if opp_val == self:
                    setattr(old_value, "gseq_If", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_If"):
                opp_val = getattr(value, "gseq_If", None)
                setattr(value, "gseq_If", self)

    @property
    def gseq_Operation(self):
        return self.__gseq_Operation

    @gseq_Operation.setter
    def gseq_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Operation__gseq_Operation", None)
        self.__gseq_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gseq_Print"):
                opp_val = getattr(old_value, "gseq_Print", None)
                if opp_val == self:
                    setattr(old_value, "gseq_Print", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gseq_Print"):
                opp_val = getattr(value, "gseq_Print", None)
                setattr(value, "gseq_Print", self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executedBy"):
                opp_val = getattr(old_value, "executedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executedBy"):
                opp_val = getattr(value, "executedBy", None)
                if opp_val is None:
                    setattr(value, "executedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operations(self):
        return self.__operations

    @operations.setter
    def operations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gseq_Operation__operations", None)
        self.__operations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Method6"):
                opp_val = getattr(old_value, "Method6", None)
                if opp_val == self:
                    setattr(old_value, "Method6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Method6"):
                opp_val = getattr(value, "Method6", None)
                setattr(value, "Method6", self)

    def execute(self):
        # TODO: Implement execute method
        pass
