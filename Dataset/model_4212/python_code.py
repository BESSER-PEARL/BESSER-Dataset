from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class myDsl_Conditional(Expression):

    def __init__(self, name: str, value2: int, value3: int):
        self.name = name
        self.value2 = value2
        self.value3 = value3
        
    @property
    def value2(self) -> int:
        return self.__value2

    @value2.setter
    def value2(self, value2: int):
        self.__value2 = value2

    @property
    def value3(self) -> int:
        return self.__value3

    @value3.setter
    def value3(self, value3: int):
        self.__value3 = value3

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_Operation(Expression):

    def __init__(self, op: str, value2: int):
        self.op = op
        self.value2 = value2
        
    @property
    def value2(self) -> int:
        return self.__value2

    @value2.setter
    def value2(self, value2: int):
        self.__value2 = value2

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class myDsl_Lambda(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_Define(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_Expression:

    def __init__(self, value: int, myDsl_Expression: "myDsl_Model" = None):
        self.value = value
        self.myDsl_Expression = myDsl_Expression
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def myDsl_Expression(self):
        return self.__myDsl_Expression

    @myDsl_Expression.setter
    def myDsl_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression", None)
        self.__myDsl_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Model"):
                opp_val = getattr(old_value, "myDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Model"):
                opp_val = getattr(value, "myDsl_Model", None)
                if opp_val is None:
                    setattr(value, "myDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Model:

    pass