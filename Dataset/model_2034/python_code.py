from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dsl_Transition:

    pass
class dsl_Command:

    def __init__(self, name: str, code: str, dsl_Command: "dsl_Statemachine" = None, dsl_Command13: "dsl_State" = None):
        self.name = name
        self.code = code
        self.dsl_Command = dsl_Command
        self.dsl_Command13 = dsl_Command13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def dsl_Command13(self):
        return self.__dsl_Command13

    @dsl_Command13.setter
    def dsl_Command13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Command__dsl_Command13", None)
        self.__dsl_Command13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_State12"):
                opp_val = getattr(old_value, "dsl_State12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_State12"):
                opp_val = getattr(value, "dsl_State12", None)
                if opp_val is None:
                    setattr(value, "dsl_State12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Command(self):
        return self.__dsl_Command

    @dsl_Command.setter
    def dsl_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Command__dsl_Command", None)
        self.__dsl_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statemachine7"):
                opp_val = getattr(old_value, "dsl_Statemachine7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statemachine7"):
                opp_val = getattr(value, "dsl_Statemachine7", None)
                if opp_val is None:
                    setattr(value, "dsl_Statemachine7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Event:

    def __init__(self, name: str, code: str, dsl_Event3: "dsl_Statemachine" = None, dsl_Event: "dsl_Statemachine" = None, dsl_Event21: "dsl_Transition" = None):
        self.name = name
        self.code = code
        self.dsl_Event3 = dsl_Event3
        self.dsl_Event = dsl_Event
        self.dsl_Event21 = dsl_Event21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def dsl_Event21(self):
        return self.__dsl_Event21

    @dsl_Event21.setter
    def dsl_Event21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Event__dsl_Event21", None)
        self.__dsl_Event21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Transition20"):
                opp_val = getattr(old_value, "dsl_Transition20", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Transition20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Transition20"):
                opp_val = getattr(value, "dsl_Transition20", None)
                setattr(value, "dsl_Transition20", self)

    @property
    def dsl_Event3(self):
        return self.__dsl_Event3

    @dsl_Event3.setter
    def dsl_Event3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Event__dsl_Event3", None)
        self.__dsl_Event3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statemachine2"):
                opp_val = getattr(old_value, "dsl_Statemachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statemachine2"):
                opp_val = getattr(value, "dsl_Statemachine2", None)
                if opp_val is None:
                    setattr(value, "dsl_Statemachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Event(self):
        return self.__dsl_Event

    @dsl_Event.setter
    def dsl_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Event__dsl_Event", None)
        self.__dsl_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statemachine"):
                opp_val = getattr(old_value, "dsl_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statemachine"):
                opp_val = getattr(value, "dsl_Statemachine", None)
                if opp_val is None:
                    setattr(value, "dsl_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Statemachine:

    pass
class dsl_State:

    def __init__(self, name: str, dsl_State: "dsl_Statemachine" = None, dsl_State24: "dsl_Transition" = None, dsl_State10: "dsl_Statemachine" = None, dsl_State12: set["dsl_Command"] = None, dsl_State15: set["dsl_Transition"] = None, dsl_State18: "dsl_State" = None, dsl_State16: set["dsl_State"] = None):
        self.name = name
        self.dsl_State = dsl_State
        self.dsl_State24 = dsl_State24
        self.dsl_State10 = dsl_State10
        self.dsl_State12 = dsl_State12 if dsl_State12 is not None else set()
        self.dsl_State15 = dsl_State15 if dsl_State15 is not None else set()
        self.dsl_State18 = dsl_State18
        self.dsl_State16 = dsl_State16 if dsl_State16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_State18(self):
        return self.__dsl_State18

    @dsl_State18.setter
    def dsl_State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State18", None)
        self.__dsl_State18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_State16"):
                opp_val = getattr(old_value, "dsl_State16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_State16"):
                opp_val = getattr(value, "dsl_State16", None)
                if opp_val is None:
                    setattr(value, "dsl_State16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_State10(self):
        return self.__dsl_State10

    @dsl_State10.setter
    def dsl_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State10", None)
        self.__dsl_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statemachine9"):
                opp_val = getattr(old_value, "dsl_Statemachine9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statemachine9"):
                opp_val = getattr(value, "dsl_Statemachine9", None)
                if opp_val is None:
                    setattr(value, "dsl_Statemachine9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_State15(self):
        return self.__dsl_State15

    @dsl_State15.setter
    def dsl_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State15", None)
        self.__dsl_State15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Transition"):
                    opp_val = getattr(item, "dsl_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Transition"):
                    opp_val = getattr(item, "dsl_Transition", None)
                    
                    setattr(item, "dsl_Transition", self)
                    

    @property
    def dsl_State(self):
        return self.__dsl_State

    @dsl_State.setter
    def dsl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State", None)
        self.__dsl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Statemachine5"):
                opp_val = getattr(old_value, "dsl_Statemachine5", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Statemachine5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Statemachine5"):
                opp_val = getattr(value, "dsl_Statemachine5", None)
                setattr(value, "dsl_Statemachine5", self)

    @property
    def dsl_State12(self):
        return self.__dsl_State12

    @dsl_State12.setter
    def dsl_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State12", None)
        self.__dsl_State12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Command13"):
                    opp_val = getattr(item, "dsl_Command13", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Command13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Command13"):
                    opp_val = getattr(item, "dsl_Command13", None)
                    
                    setattr(item, "dsl_Command13", self)
                    

    @property
    def dsl_State16(self):
        return self.__dsl_State16

    @dsl_State16.setter
    def dsl_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State16", None)
        self.__dsl_State16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_State18"):
                    opp_val = getattr(item, "dsl_State18", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_State18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_State18"):
                    opp_val = getattr(item, "dsl_State18", None)
                    
                    setattr(item, "dsl_State18", self)
                    

    @property
    def dsl_State24(self):
        return self.__dsl_State24

    @dsl_State24.setter
    def dsl_State24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State24", None)
        self.__dsl_State24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Transition23"):
                opp_val = getattr(old_value, "dsl_Transition23", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Transition23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Transition23"):
                opp_val = getattr(value, "dsl_Transition23", None)
                setattr(value, "dsl_Transition23", self)
