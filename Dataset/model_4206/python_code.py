from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Model:

    pass
class Greeting:

    pass
class myDsl_Selecao(Greeting):

    pass
class myDsl_Define(Greeting):

    pass
class myDsl_Expressao(Greeting):

    def __init__(self, name: str, myDsl_Expressao: "myDsl_Greeting" = None):
        self.name = name
        self.myDsl_Expressao = myDsl_Expressao
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Expressao(self):
        return self.__myDsl_Expressao

    @myDsl_Expressao.setter
    def myDsl_Expressao(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expressao__myDsl_Expressao", None)
        self.__myDsl_Expressao = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Greeting2"):
                opp_val = getattr(old_value, "myDsl_Greeting2", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Greeting2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Greeting2"):
                opp_val = getattr(value, "myDsl_Greeting2", None)
                setattr(value, "myDsl_Greeting2", self)

class myDsl_Greeting:

    def __init__(self, value: int, myDsl_Greeting: "myDsl_Model" = None, myDsl_Greeting2: "myDsl_Expressao" = None):
        self.value = value
        self.myDsl_Greeting = myDsl_Greeting
        self.myDsl_Greeting2 = myDsl_Greeting2
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

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

    @property
    def myDsl_Greeting2(self):
        return self.__myDsl_Greeting2

    @myDsl_Greeting2.setter
    def myDsl_Greeting2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Greeting__myDsl_Greeting2", None)
        self.__myDsl_Greeting2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expressao"):
                opp_val = getattr(old_value, "myDsl_Expressao", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expressao", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expressao"):
                opp_val = getattr(value, "myDsl_Expressao", None)
                setattr(value, "myDsl_Expressao", self)
