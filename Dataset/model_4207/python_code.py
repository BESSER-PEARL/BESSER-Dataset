from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Greeting:

    pass
class myDsl_Conditional(Greeting):

    def __init__(self, value2: int, value3: int):
        self.value2 = value2
        self.value3 = value3
        
    @property
    def value3(self) -> int:
        return self.__value3

    @value3.setter
    def value3(self, value3: int):
        self.__value3 = value3

    @property
    def value2(self) -> int:
        return self.__value2

    @value2.setter
    def value2(self, value2: int):
        self.__value2 = value2

class myDsl_Lambda(Greeting):

    pass
class myDsl_Operation(Greeting):

    def __init__(self, op: str, value2: int):
        self.op = op
        self.value2 = value2
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def value2(self) -> int:
        return self.__value2

    @value2.setter
    def value2(self, value2: int):
        self.__value2 = value2

class myDsl_Square(Greeting):

    pass
class myDsl_Define(Greeting):

    pass
class myDsl_Model:

    pass
class myDsl_Greeting:

    def __init__(self, value: int, name: str, myDsl_Greeting: "myDsl_Model" = None):
        self.value = value
        self.name = name
        self.myDsl_Greeting = myDsl_Greeting
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Greeting(self):
        return self.__myDsl_Greeting

    @myDsl_Greeting.setter
    def myDsl_Greeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Greeting__myDsl_Greeting", None)
        self.__myDsl_Greeting = value
        
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
