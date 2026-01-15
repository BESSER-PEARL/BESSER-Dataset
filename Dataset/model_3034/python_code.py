from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myfsm_State:

    def __init__(self, name: str, myfsm_State5: set["myfsm_Trans"] = None, myfsm_State8: "myfsm_Trans" = None, myfsm_State: "myfsm_Machine" = None, myfsm_State3: "myfsm_Machine" = None):
        self.name = name
        self.myfsm_State5 = myfsm_State5 if myfsm_State5 is not None else set()
        self.myfsm_State8 = myfsm_State8
        self.myfsm_State = myfsm_State
        self.myfsm_State3 = myfsm_State3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myfsm_State8(self):
        return self.__myfsm_State8

    @myfsm_State8.setter
    def myfsm_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myfsm_State__myfsm_State8", None)
        self.__myfsm_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myfsm_Trans7"):
                opp_val = getattr(old_value, "myfsm_Trans7", None)
                if opp_val == self:
                    setattr(old_value, "myfsm_Trans7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myfsm_Trans7"):
                opp_val = getattr(value, "myfsm_Trans7", None)
                setattr(value, "myfsm_Trans7", self)

    @property
    def myfsm_State3(self):
        return self.__myfsm_State3

    @myfsm_State3.setter
    def myfsm_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myfsm_State__myfsm_State3", None)
        self.__myfsm_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myfsm_Machine2"):
                opp_val = getattr(old_value, "myfsm_Machine2", None)
                if opp_val == self:
                    setattr(old_value, "myfsm_Machine2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myfsm_Machine2"):
                opp_val = getattr(value, "myfsm_Machine2", None)
                setattr(value, "myfsm_Machine2", self)

    @property
    def myfsm_State5(self):
        return self.__myfsm_State5

    @myfsm_State5.setter
    def myfsm_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myfsm_State__myfsm_State5", None)
        self.__myfsm_State5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myfsm_Trans"):
                    opp_val = getattr(item, "myfsm_Trans", None)
                    
                    if opp_val == self:
                        setattr(item, "myfsm_Trans", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myfsm_Trans"):
                    opp_val = getattr(item, "myfsm_Trans", None)
                    
                    setattr(item, "myfsm_Trans", self)
                    

    @property
    def myfsm_State(self):
        return self.__myfsm_State

    @myfsm_State.setter
    def myfsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myfsm_State__myfsm_State", None)
        self.__myfsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myfsm_Machine"):
                opp_val = getattr(old_value, "myfsm_Machine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myfsm_Machine"):
                opp_val = getattr(value, "myfsm_Machine", None)
                if opp_val is None:
                    setattr(value, "myfsm_Machine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myfsm_Machine:

    def __init__(self, name: str, myfsm_Machine: set["myfsm_State"] = None, myfsm_Machine2: "myfsm_State" = None):
        self.name = name
        self.myfsm_Machine = myfsm_Machine if myfsm_Machine is not None else set()
        self.myfsm_Machine2 = myfsm_Machine2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myfsm_Machine(self):
        return self.__myfsm_Machine

    @myfsm_Machine.setter
    def myfsm_Machine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myfsm_Machine__myfsm_Machine", None)
        self.__myfsm_Machine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myfsm_State"):
                    opp_val = getattr(item, "myfsm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "myfsm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myfsm_State"):
                    opp_val = getattr(item, "myfsm_State", None)
                    
                    setattr(item, "myfsm_State", self)
                    

    @property
    def myfsm_Machine2(self):
        return self.__myfsm_Machine2

    @myfsm_Machine2.setter
    def myfsm_Machine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myfsm_Machine__myfsm_Machine2", None)
        self.__myfsm_Machine2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myfsm_State3"):
                opp_val = getattr(old_value, "myfsm_State3", None)
                if opp_val == self:
                    setattr(old_value, "myfsm_State3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myfsm_State3"):
                opp_val = getattr(value, "myfsm_State3", None)
                setattr(value, "myfsm_State3", self)

class myfsm_Trans:

    def __init__(self, event: str, myfsm_Trans: "myfsm_State" = None, myfsm_Trans7: "myfsm_State" = None):
        self.event = event
        self.myfsm_Trans = myfsm_Trans
        self.myfsm_Trans7 = myfsm_Trans7
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def myfsm_Trans(self):
        return self.__myfsm_Trans

    @myfsm_Trans.setter
    def myfsm_Trans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myfsm_Trans__myfsm_Trans", None)
        self.__myfsm_Trans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myfsm_State5"):
                opp_val = getattr(old_value, "myfsm_State5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myfsm_State5"):
                opp_val = getattr(value, "myfsm_State5", None)
                if opp_val is None:
                    setattr(value, "myfsm_State5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myfsm_Trans7(self):
        return self.__myfsm_Trans7

    @myfsm_Trans7.setter
    def myfsm_Trans7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myfsm_Trans__myfsm_Trans7", None)
        self.__myfsm_Trans7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myfsm_State8"):
                opp_val = getattr(old_value, "myfsm_State8", None)
                if opp_val == self:
                    setattr(old_value, "myfsm_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myfsm_State8"):
                opp_val = getattr(value, "myfsm_State8", None)
                setattr(value, "myfsm_State8", self)
