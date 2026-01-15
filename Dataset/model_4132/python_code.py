from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class myDsl_Minus(Expression):

    pass
class myDsl_Div(Expression):

    pass
class myDsl_Var(Expression):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class myDsl_Let(Expression):

    def __init__(self, id: str, myDsl_Let: "myDsl_Expression" = None, myDsl_Let26: "myDsl_Expression" = None):
        self.id = id
        self.myDsl_Let = myDsl_Let
        self.myDsl_Let26 = myDsl_Let26
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myDsl_Let26(self):
        return self.__myDsl_Let26

    @myDsl_Let26.setter
    def myDsl_Let26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Let__myDsl_Let26", None)
        self.__myDsl_Let26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression27"):
                opp_val = getattr(old_value, "myDsl_Expression27", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression27"):
                opp_val = getattr(value, "myDsl_Expression27", None)
                setattr(value, "myDsl_Expression27", self)

    @property
    def myDsl_Let(self):
        return self.__myDsl_Let

    @myDsl_Let.setter
    def myDsl_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Let__myDsl_Let", None)
        self.__myDsl_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression24"):
                opp_val = getattr(old_value, "myDsl_Expression24", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression24"):
                opp_val = getattr(value, "myDsl_Expression24", None)
                setattr(value, "myDsl_Expression24", self)

class myDsl_Mult(Expression):

    pass
class myDsl_Num(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class myDsl_Plus(Expression):

    pass
class myDsl_Expression:

    pass
class myDsl_Parameter:

    def __init__(self, name: str, myDsl_Parameter: "myDsl_Method" = None):
        self.name = name
        self.myDsl_Parameter = myDsl_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Parameter(self):
        return self.__myDsl_Parameter

    @myDsl_Parameter.setter
    def myDsl_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Parameter__myDsl_Parameter", None)
        self.__myDsl_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Method"):
                opp_val = getattr(old_value, "myDsl_Method", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Method"):
                opp_val = getattr(value, "myDsl_Method", None)
                if opp_val is None:
                    setattr(value, "myDsl_Method", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Instance:

    pass
class myDsl_MathExp(Instance):

    def __init__(self, text: str, myDsl_MathExp: "myDsl_Expression" = None):
        self.text = text
        self.myDsl_MathExp = myDsl_MathExp
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def myDsl_MathExp(self):
        return self.__myDsl_MathExp

    @myDsl_MathExp.setter
    def myDsl_MathExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_MathExp__myDsl_MathExp", None)
        self.__myDsl_MathExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression"):
                opp_val = getattr(old_value, "myDsl_Expression", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression"):
                opp_val = getattr(value, "myDsl_Expression", None)
                setattr(value, "myDsl_Expression", self)

class myDsl_Method(Instance):

    def __init__(self, name: str, myDsl_Method: set["myDsl_Parameter"] = None):
        self.name = name
        self.myDsl_Method = myDsl_Method if myDsl_Method is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Method(self):
        return self.__myDsl_Method

    @myDsl_Method.setter
    def myDsl_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Method__myDsl_Method", None)
        self.__myDsl_Method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Parameter"):
                    opp_val = getattr(item, "myDsl_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Parameter"):
                    opp_val = getattr(item, "myDsl_Parameter", None)
                    
                    setattr(item, "myDsl_Parameter", self)
                    

class myDsl_Instance:

    pass
class myDsl_Classs:

    pass