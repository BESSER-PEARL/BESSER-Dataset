from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class automata_Automata:

    pass
class automata_Final:

    def __init__(self, name: str, automata_Final: "automata_Automata" = None, automata_Final19: "automata_State" = None):
        self.name = name
        self.automata_Final = automata_Final
        self.automata_Final19 = automata_Final19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def automata_Final19(self):
        return self.__automata_Final19

    @automata_Final19.setter
    def automata_Final19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_Final__automata_Final19", None)
        self.__automata_Final19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_State20"):
                opp_val = getattr(old_value, "automata_State20", None)
                if opp_val == self:
                    setattr(old_value, "automata_State20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_State20"):
                opp_val = getattr(value, "automata_State20", None)
                setattr(value, "automata_State20", self)

    @property
    def automata_Final(self):
        return self.__automata_Final

    @automata_Final.setter
    def automata_Final(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_Final__automata_Final", None)
        self.__automata_Final = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Automata8"):
                opp_val = getattr(old_value, "automata_Automata8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Automata8"):
                opp_val = getattr(value, "automata_Automata8", None)
                if opp_val is None:
                    setattr(value, "automata_Automata8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class automata_Transition:

    def __init__(self, token: str, name: str, automata_Transition: "automata_Automata" = None, automata_Transition10: "automata_State" = None, automata_Transition13: "automata_State" = None):
        self.token = token
        self.name = name
        self.automata_Transition = automata_Transition
        self.automata_Transition10 = automata_Transition10
        self.automata_Transition13 = automata_Transition13
        
    @property
    def token(self) -> str:
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def automata_Transition13(self):
        return self.__automata_Transition13

    @automata_Transition13.setter
    def automata_Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_Transition__automata_Transition13", None)
        self.__automata_Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_State14"):
                opp_val = getattr(old_value, "automata_State14", None)
                if opp_val == self:
                    setattr(old_value, "automata_State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_State14"):
                opp_val = getattr(value, "automata_State14", None)
                setattr(value, "automata_State14", self)

    @property
    def automata_Transition10(self):
        return self.__automata_Transition10

    @automata_Transition10.setter
    def automata_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_Transition__automata_Transition10", None)
        self.__automata_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_State11"):
                opp_val = getattr(old_value, "automata_State11", None)
                if opp_val == self:
                    setattr(old_value, "automata_State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_State11"):
                opp_val = getattr(value, "automata_State11", None)
                setattr(value, "automata_State11", self)

    @property
    def automata_Transition(self):
        return self.__automata_Transition

    @automata_Transition.setter
    def automata_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_Transition__automata_Transition", None)
        self.__automata_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Automata6"):
                opp_val = getattr(old_value, "automata_Automata6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Automata6"):
                opp_val = getattr(value, "automata_Automata6", None)
                if opp_val is None:
                    setattr(value, "automata_Automata6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class automata_State:

    def __init__(self, name: str, automata_State: "automata_Automata" = None, automata_State23: "automata_Current" = None, automata_State11: "automata_Transition" = None, automata_State14: "automata_Transition" = None, automata_State17: "automata_Initial" = None, automata_State20: "automata_Final" = None):
        self.name = name
        self.automata_State = automata_State
        self.automata_State23 = automata_State23
        self.automata_State11 = automata_State11
        self.automata_State14 = automata_State14
        self.automata_State17 = automata_State17
        self.automata_State20 = automata_State20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def automata_State23(self):
        return self.__automata_State23

    @automata_State23.setter
    def automata_State23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_State__automata_State23", None)
        self.__automata_State23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Current22"):
                opp_val = getattr(old_value, "automata_Current22", None)
                if opp_val == self:
                    setattr(old_value, "automata_Current22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Current22"):
                opp_val = getattr(value, "automata_Current22", None)
                setattr(value, "automata_Current22", self)

    @property
    def automata_State14(self):
        return self.__automata_State14

    @automata_State14.setter
    def automata_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_State__automata_State14", None)
        self.__automata_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Transition13"):
                opp_val = getattr(old_value, "automata_Transition13", None)
                if opp_val == self:
                    setattr(old_value, "automata_Transition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Transition13"):
                opp_val = getattr(value, "automata_Transition13", None)
                setattr(value, "automata_Transition13", self)

    @property
    def automata_State17(self):
        return self.__automata_State17

    @automata_State17.setter
    def automata_State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_State__automata_State17", None)
        self.__automata_State17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Initial16"):
                opp_val = getattr(old_value, "automata_Initial16", None)
                if opp_val == self:
                    setattr(old_value, "automata_Initial16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Initial16"):
                opp_val = getattr(value, "automata_Initial16", None)
                setattr(value, "automata_Initial16", self)

    @property
    def automata_State11(self):
        return self.__automata_State11

    @automata_State11.setter
    def automata_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_State__automata_State11", None)
        self.__automata_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Transition10"):
                opp_val = getattr(old_value, "automata_Transition10", None)
                if opp_val == self:
                    setattr(old_value, "automata_Transition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Transition10"):
                opp_val = getattr(value, "automata_Transition10", None)
                setattr(value, "automata_Transition10", self)

    @property
    def automata_State20(self):
        return self.__automata_State20

    @automata_State20.setter
    def automata_State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_State__automata_State20", None)
        self.__automata_State20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Final19"):
                opp_val = getattr(old_value, "automata_Final19", None)
                if opp_val == self:
                    setattr(old_value, "automata_Final19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Final19"):
                opp_val = getattr(value, "automata_Final19", None)
                setattr(value, "automata_Final19", self)

    @property
    def automata_State(self):
        return self.__automata_State

    @automata_State.setter
    def automata_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_State__automata_State", None)
        self.__automata_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Automata4"):
                opp_val = getattr(old_value, "automata_Automata4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Automata4"):
                opp_val = getattr(value, "automata_Automata4", None)
                if opp_val is None:
                    setattr(value, "automata_Automata4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class automata_Initial:

    def __init__(self, name: str, automata_Initial: "automata_Automata" = None, automata_Initial16: "automata_State" = None):
        self.name = name
        self.automata_Initial = automata_Initial
        self.automata_Initial16 = automata_Initial16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def automata_Initial(self):
        return self.__automata_Initial

    @automata_Initial.setter
    def automata_Initial(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_Initial__automata_Initial", None)
        self.__automata_Initial = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Automata2"):
                opp_val = getattr(old_value, "automata_Automata2", None)
                if opp_val == self:
                    setattr(old_value, "automata_Automata2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Automata2"):
                opp_val = getattr(value, "automata_Automata2", None)
                setattr(value, "automata_Automata2", self)

    @property
    def automata_Initial16(self):
        return self.__automata_Initial16

    @automata_Initial16.setter
    def automata_Initial16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_Initial__automata_Initial16", None)
        self.__automata_Initial16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_State17"):
                opp_val = getattr(old_value, "automata_State17", None)
                if opp_val == self:
                    setattr(old_value, "automata_State17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_State17"):
                opp_val = getattr(value, "automata_State17", None)
                setattr(value, "automata_State17", self)

class automata_Current:

    def __init__(self, name: str, automata_Current: "automata_Automata" = None, automata_Current22: "automata_State" = None):
        self.name = name
        self.automata_Current = automata_Current
        self.automata_Current22 = automata_Current22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def automata_Current22(self):
        return self.__automata_Current22

    @automata_Current22.setter
    def automata_Current22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_Current__automata_Current22", None)
        self.__automata_Current22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_State23"):
                opp_val = getattr(old_value, "automata_State23", None)
                if opp_val == self:
                    setattr(old_value, "automata_State23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_State23"):
                opp_val = getattr(value, "automata_State23", None)
                setattr(value, "automata_State23", self)

    @property
    def automata_Current(self):
        return self.__automata_Current

    @automata_Current.setter
    def automata_Current(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automata_Current__automata_Current", None)
        self.__automata_Current = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata_Automata"):
                opp_val = getattr(old_value, "automata_Automata", None)
                if opp_val == self:
                    setattr(old_value, "automata_Automata", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata_Automata"):
                opp_val = getattr(value, "automata_Automata", None)
                setattr(value, "automata_Automata", self)
