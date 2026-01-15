from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FExpression:

    pass
class fsmWithMethods_Event(FExpression):

    pass
class fsmWithMethods_MethodCall(FExpression):

    pass
class fsmWithMethods_Transition(FExpression):

    pass
class fsmWithMethods_Method(FExpression):

    pass
class fsmWithMethods_Referentiable:

    pass
class Referentiable:

    pass
class fsmWithMethods_FExpression(Referentiable):

    def __init__(self, name: str, fsmWithMethods_FExpression: "fsmWithMethods_Fsm" = None, fsmWithMethods_FExpression4: "fsmWithMethods_Method" = None, fsmWithMethods_FExpression7: "fsmWithMethods_Method" = None, fsmWithMethods_FExpression16: "fsmWithMethods_Transition" = None, fsmWithMethods_FExpression19: "fsmWithMethods_Transition" = None, fsmWithMethods_FExpression13: "fsmWithMethods_Transition" = None):
        self.name = name
        self.fsmWithMethods_FExpression = fsmWithMethods_FExpression
        self.fsmWithMethods_FExpression4 = fsmWithMethods_FExpression4
        self.fsmWithMethods_FExpression7 = fsmWithMethods_FExpression7
        self.fsmWithMethods_FExpression16 = fsmWithMethods_FExpression16
        self.fsmWithMethods_FExpression19 = fsmWithMethods_FExpression19
        self.fsmWithMethods_FExpression13 = fsmWithMethods_FExpression13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsmWithMethods_FExpression16(self):
        return self.__fsmWithMethods_FExpression16

    @fsmWithMethods_FExpression16.setter
    def fsmWithMethods_FExpression16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmWithMethods_FExpression__fsmWithMethods_FExpression16", None)
        self.__fsmWithMethods_FExpression16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmWithMethods_Transition15"):
                opp_val = getattr(old_value, "fsmWithMethods_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "fsmWithMethods_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmWithMethods_Transition15"):
                opp_val = getattr(value, "fsmWithMethods_Transition15", None)
                setattr(value, "fsmWithMethods_Transition15", self)

    @property
    def fsmWithMethods_FExpression13(self):
        return self.__fsmWithMethods_FExpression13

    @fsmWithMethods_FExpression13.setter
    def fsmWithMethods_FExpression13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmWithMethods_FExpression__fsmWithMethods_FExpression13", None)
        self.__fsmWithMethods_FExpression13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmWithMethods_Transition"):
                opp_val = getattr(old_value, "fsmWithMethods_Transition", None)
                if opp_val == self:
                    setattr(old_value, "fsmWithMethods_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmWithMethods_Transition"):
                opp_val = getattr(value, "fsmWithMethods_Transition", None)
                setattr(value, "fsmWithMethods_Transition", self)

    @property
    def fsmWithMethods_FExpression7(self):
        return self.__fsmWithMethods_FExpression7

    @fsmWithMethods_FExpression7.setter
    def fsmWithMethods_FExpression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmWithMethods_FExpression__fsmWithMethods_FExpression7", None)
        self.__fsmWithMethods_FExpression7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmWithMethods_Method6"):
                opp_val = getattr(old_value, "fsmWithMethods_Method6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmWithMethods_Method6"):
                opp_val = getattr(value, "fsmWithMethods_Method6", None)
                if opp_val is None:
                    setattr(value, "fsmWithMethods_Method6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsmWithMethods_FExpression(self):
        return self.__fsmWithMethods_FExpression

    @fsmWithMethods_FExpression.setter
    def fsmWithMethods_FExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmWithMethods_FExpression__fsmWithMethods_FExpression", None)
        self.__fsmWithMethods_FExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmWithMethods_Fsm2"):
                opp_val = getattr(old_value, "fsmWithMethods_Fsm2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmWithMethods_Fsm2"):
                opp_val = getattr(value, "fsmWithMethods_Fsm2", None)
                if opp_val is None:
                    setattr(value, "fsmWithMethods_Fsm2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsmWithMethods_FExpression4(self):
        return self.__fsmWithMethods_FExpression4

    @fsmWithMethods_FExpression4.setter
    def fsmWithMethods_FExpression4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmWithMethods_FExpression__fsmWithMethods_FExpression4", None)
        self.__fsmWithMethods_FExpression4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmWithMethods_Method"):
                opp_val = getattr(old_value, "fsmWithMethods_Method", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmWithMethods_Method"):
                opp_val = getattr(value, "fsmWithMethods_Method", None)
                if opp_val is None:
                    setattr(value, "fsmWithMethods_Method", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsmWithMethods_FExpression19(self):
        return self.__fsmWithMethods_FExpression19

    @fsmWithMethods_FExpression19.setter
    def fsmWithMethods_FExpression19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmWithMethods_FExpression__fsmWithMethods_FExpression19", None)
        self.__fsmWithMethods_FExpression19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmWithMethods_Transition18"):
                opp_val = getattr(old_value, "fsmWithMethods_Transition18", None)
                if opp_val == self:
                    setattr(old_value, "fsmWithMethods_Transition18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmWithMethods_Transition18"):
                opp_val = getattr(value, "fsmWithMethods_Transition18", None)
                setattr(value, "fsmWithMethods_Transition18", self)

class fsmWithMethods_State(FExpression):

    pass
class fsmWithMethods_Fsm:

    def __init__(self, name: str, fsmWithMethods_Fsm2: set["fsmWithMethods_FExpression"] = None, fsmWithMethods_Fsm: "fsmWithMethods_State" = None):
        self.name = name
        self.fsmWithMethods_Fsm2 = fsmWithMethods_Fsm2 if fsmWithMethods_Fsm2 is not None else set()
        self.fsmWithMethods_Fsm = fsmWithMethods_Fsm
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsmWithMethods_Fsm2(self):
        return self.__fsmWithMethods_Fsm2

    @fsmWithMethods_Fsm2.setter
    def fsmWithMethods_Fsm2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmWithMethods_Fsm__fsmWithMethods_Fsm2", None)
        self.__fsmWithMethods_Fsm2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmWithMethods_FExpression"):
                    opp_val = getattr(item, "fsmWithMethods_FExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmWithMethods_FExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmWithMethods_FExpression"):
                    opp_val = getattr(item, "fsmWithMethods_FExpression", None)
                    
                    setattr(item, "fsmWithMethods_FExpression", self)
                    

    @property
    def fsmWithMethods_Fsm(self):
        return self.__fsmWithMethods_Fsm

    @fsmWithMethods_Fsm.setter
    def fsmWithMethods_Fsm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmWithMethods_Fsm__fsmWithMethods_Fsm", None)
        self.__fsmWithMethods_Fsm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmWithMethods_State"):
                opp_val = getattr(old_value, "fsmWithMethods_State", None)
                if opp_val == self:
                    setattr(old_value, "fsmWithMethods_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmWithMethods_State"):
                opp_val = getattr(value, "fsmWithMethods_State", None)
                setattr(value, "fsmWithMethods_State", self)
