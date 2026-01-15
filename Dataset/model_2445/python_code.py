from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ioautomaton_Object:

    def __init__(self, name: str, ioautomaton_Object: "ioautomaton_OutMessage" = None):
        self.name = name
        self.ioautomaton_Object = ioautomaton_Object
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioautomaton_Object(self):
        return self.__ioautomaton_Object

    @ioautomaton_Object.setter
    def ioautomaton_Object(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_Object__ioautomaton_Object", None)
        self.__ioautomaton_Object = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioautomaton_OutMessage24"):
                opp_val = getattr(old_value, "ioautomaton_OutMessage24", None)
                if opp_val == self:
                    setattr(old_value, "ioautomaton_OutMessage24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioautomaton_OutMessage24"):
                opp_val = getattr(value, "ioautomaton_OutMessage24", None)
                setattr(value, "ioautomaton_OutMessage24", self)

class ioautomaton_OutMessage:

    pass
class ioautomaton_Return:

    def __init__(self, value: str, ioautomaton_Return: "ioautomaton_Transition" = None, ioautomaton_Return22: "ioautomaton_OutMessage" = None):
        self.value = value
        self.ioautomaton_Return = ioautomaton_Return
        self.ioautomaton_Return22 = ioautomaton_Return22
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ioautomaton_Return(self):
        return self.__ioautomaton_Return

    @ioautomaton_Return.setter
    def ioautomaton_Return(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_Return__ioautomaton_Return", None)
        self.__ioautomaton_Return = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioautomaton_Transition14"):
                opp_val = getattr(old_value, "ioautomaton_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "ioautomaton_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioautomaton_Transition14"):
                opp_val = getattr(value, "ioautomaton_Transition14", None)
                setattr(value, "ioautomaton_Transition14", self)

    @property
    def ioautomaton_Return22(self):
        return self.__ioautomaton_Return22

    @ioautomaton_Return22.setter
    def ioautomaton_Return22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_Return__ioautomaton_Return22", None)
        self.__ioautomaton_Return22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioautomaton_OutMessage21"):
                opp_val = getattr(old_value, "ioautomaton_OutMessage21", None)
                if opp_val == self:
                    setattr(old_value, "ioautomaton_OutMessage21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioautomaton_OutMessage21"):
                opp_val = getattr(value, "ioautomaton_OutMessage21", None)
                setattr(value, "ioautomaton_OutMessage21", self)

class ioautomaton_Operation:

    def __init__(self, name: str, ioautomaton_Operation: "ioautomaton_Transition" = None, ioautomaton_Operation27: "ioautomaton_OutMessage" = None):
        self.name = name
        self.ioautomaton_Operation = ioautomaton_Operation
        self.ioautomaton_Operation27 = ioautomaton_Operation27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioautomaton_Operation(self):
        return self.__ioautomaton_Operation

    @ioautomaton_Operation.setter
    def ioautomaton_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_Operation__ioautomaton_Operation", None)
        self.__ioautomaton_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioautomaton_Transition12"):
                opp_val = getattr(old_value, "ioautomaton_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "ioautomaton_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioautomaton_Transition12"):
                opp_val = getattr(value, "ioautomaton_Transition12", None)
                setattr(value, "ioautomaton_Transition12", self)

    @property
    def ioautomaton_Operation27(self):
        return self.__ioautomaton_Operation27

    @ioautomaton_Operation27.setter
    def ioautomaton_Operation27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_Operation__ioautomaton_Operation27", None)
        self.__ioautomaton_Operation27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioautomaton_OutMessage26"):
                opp_val = getattr(old_value, "ioautomaton_OutMessage26", None)
                if opp_val == self:
                    setattr(old_value, "ioautomaton_OutMessage26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioautomaton_OutMessage26"):
                opp_val = getattr(value, "ioautomaton_OutMessage26", None)
                setattr(value, "ioautomaton_OutMessage26", self)

class ioautomaton_Transition:

    pass
class ioautomaton_State:

    def __init__(self, name: str, ioautomaton_State: "ioautomaton_Automaton" = None, ioautomaton_State7: "ioautomaton_Automaton" = None, prestate: set["ioautomaton_Transition"] = None, poststate: set["ioautomaton_Transition"] = None, State: "ioautomaton_Transition" = None, State19: "ioautomaton_Transition" = None):
        self.name = name
        self.ioautomaton_State = ioautomaton_State
        self.ioautomaton_State7 = ioautomaton_State7
        self.prestate = prestate if prestate is not None else set()
        self.poststate = poststate if poststate is not None else set()
        self.State = State
        self.State19 = State19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State19(self):
        return self.__State19

    @State19.setter
    def State19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_State__State19", None)
        self.__State19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingtransition"):
                opp_val = getattr(old_value, "incomingtransition", None)
                if opp_val == self:
                    setattr(old_value, "incomingtransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingtransition"):
                opp_val = getattr(value, "incomingtransition", None)
                setattr(value, "incomingtransition", self)

    @property
    def poststate(self):
        return self.__poststate

    @poststate.setter
    def poststate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_State__poststate", None)
        self.__poststate = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition10"):
                    opp_val = getattr(item, "Transition10", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition10"):
                    opp_val = getattr(item, "Transition10", None)
                    
                    setattr(item, "Transition10", self)
                    

    @property
    def ioautomaton_State7(self):
        return self.__ioautomaton_State7

    @ioautomaton_State7.setter
    def ioautomaton_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_State__ioautomaton_State7", None)
        self.__ioautomaton_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioautomaton_Automaton6"):
                opp_val = getattr(old_value, "ioautomaton_Automaton6", None)
                if opp_val == self:
                    setattr(old_value, "ioautomaton_Automaton6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioautomaton_Automaton6"):
                opp_val = getattr(value, "ioautomaton_Automaton6", None)
                setattr(value, "ioautomaton_Automaton6", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingtransition"):
                opp_val = getattr(old_value, "outgoingtransition", None)
                if opp_val == self:
                    setattr(old_value, "outgoingtransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingtransition"):
                opp_val = getattr(value, "outgoingtransition", None)
                setattr(value, "outgoingtransition", self)

    @property
    def ioautomaton_State(self):
        return self.__ioautomaton_State

    @ioautomaton_State.setter
    def ioautomaton_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_State__ioautomaton_State", None)
        self.__ioautomaton_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioautomaton_Automaton2"):
                opp_val = getattr(old_value, "ioautomaton_Automaton2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioautomaton_Automaton2"):
                opp_val = getattr(value, "ioautomaton_Automaton2", None)
                if opp_val is None:
                    setattr(value, "ioautomaton_Automaton2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def prestate(self):
        return self.__prestate

    @prestate.setter
    def prestate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_State__prestate", None)
        self.__prestate = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

class ioautomaton_Automaton:

    def __init__(self, sender: str, ioautomaton_Automaton: "ioautomaton_AutomatonContainer" = None, ioautomaton_Automaton2: set["ioautomaton_State"] = None, ioautomaton_Automaton4: set["ioautomaton_Transition"] = None, ioautomaton_Automaton6: "ioautomaton_State" = None):
        self.sender = sender
        self.ioautomaton_Automaton = ioautomaton_Automaton
        self.ioautomaton_Automaton2 = ioautomaton_Automaton2 if ioautomaton_Automaton2 is not None else set()
        self.ioautomaton_Automaton4 = ioautomaton_Automaton4 if ioautomaton_Automaton4 is not None else set()
        self.ioautomaton_Automaton6 = ioautomaton_Automaton6
        
    @property
    def sender(self) -> str:
        return self.__sender

    @sender.setter
    def sender(self, sender: str):
        self.__sender = sender

    @property
    def ioautomaton_Automaton4(self):
        return self.__ioautomaton_Automaton4

    @ioautomaton_Automaton4.setter
    def ioautomaton_Automaton4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_Automaton__ioautomaton_Automaton4", None)
        self.__ioautomaton_Automaton4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioautomaton_Transition"):
                    opp_val = getattr(item, "ioautomaton_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "ioautomaton_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioautomaton_Transition"):
                    opp_val = getattr(item, "ioautomaton_Transition", None)
                    
                    setattr(item, "ioautomaton_Transition", self)
                    

    @property
    def ioautomaton_Automaton2(self):
        return self.__ioautomaton_Automaton2

    @ioautomaton_Automaton2.setter
    def ioautomaton_Automaton2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_Automaton__ioautomaton_Automaton2", None)
        self.__ioautomaton_Automaton2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioautomaton_State"):
                    opp_val = getattr(item, "ioautomaton_State", None)
                    
                    if opp_val == self:
                        setattr(item, "ioautomaton_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioautomaton_State"):
                    opp_val = getattr(item, "ioautomaton_State", None)
                    
                    setattr(item, "ioautomaton_State", self)
                    

    @property
    def ioautomaton_Automaton(self):
        return self.__ioautomaton_Automaton

    @ioautomaton_Automaton.setter
    def ioautomaton_Automaton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_Automaton__ioautomaton_Automaton", None)
        self.__ioautomaton_Automaton = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioautomaton_AutomatonContainer"):
                opp_val = getattr(old_value, "ioautomaton_AutomatonContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioautomaton_AutomatonContainer"):
                opp_val = getattr(value, "ioautomaton_AutomatonContainer", None)
                if opp_val is None:
                    setattr(value, "ioautomaton_AutomatonContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioautomaton_Automaton6(self):
        return self.__ioautomaton_Automaton6

    @ioautomaton_Automaton6.setter
    def ioautomaton_Automaton6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioautomaton_Automaton__ioautomaton_Automaton6", None)
        self.__ioautomaton_Automaton6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioautomaton_State7"):
                opp_val = getattr(old_value, "ioautomaton_State7", None)
                if opp_val == self:
                    setattr(old_value, "ioautomaton_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioautomaton_State7"):
                opp_val = getattr(value, "ioautomaton_State7", None)
                setattr(value, "ioautomaton_State7", self)

class ioautomaton_AutomatonContainer:

    pass