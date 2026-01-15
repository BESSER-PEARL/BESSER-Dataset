from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class statemachine_Thing:

    def __init__(self, name: str, statemachine_Thing: "statemachine_State" = None, statemachine_Thing43: "statemachine_Guard" = None):
        self.name = name
        self.statemachine_Thing = statemachine_Thing
        self.statemachine_Thing43 = statemachine_Thing43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_Thing43(self):
        return self.__statemachine_Thing43

    @statemachine_Thing43.setter
    def statemachine_Thing43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Thing__statemachine_Thing43", None)
        self.__statemachine_Thing43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Guard44"):
                opp_val = getattr(old_value, "statemachine_Guard44", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Guard44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Guard44"):
                opp_val = getattr(value, "statemachine_Guard44", None)
                setattr(value, "statemachine_Guard44", self)

    @property
    def statemachine_Thing(self):
        return self.__statemachine_Thing

    @statemachine_Thing.setter
    def statemachine_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Thing__statemachine_Thing", None)
        self.__statemachine_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State32"):
                opp_val = getattr(old_value, "statemachine_State32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State32"):
                opp_val = getattr(value, "statemachine_State32", None)
                if opp_val is None:
                    setattr(value, "statemachine_State32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_Transition:

    pass
class Value:

    pass
class statemachine_IntLiteral(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class statemachine_ConstantRef(Value):

    pass
class statemachine_Value:

    pass
class statemachine_Guard:

    pass
class statemachine_State:

    def __init__(self, name: str, description: str, statemachine_State: "statemachine_Statemachine" = None, statemachine_State27: set["statemachine_Command"] = None, statemachine_State30: set["statemachine_Transition"] = None, statemachine_State32: set["statemachine_Thing"] = None, statemachine_State41: "statemachine_Transition" = None):
        self.name = name
        self.description = description
        self.statemachine_State = statemachine_State
        self.statemachine_State27 = statemachine_State27 if statemachine_State27 is not None else set()
        self.statemachine_State30 = statemachine_State30 if statemachine_State30 is not None else set()
        self.statemachine_State32 = statemachine_State32 if statemachine_State32 is not None else set()
        self.statemachine_State41 = statemachine_State41
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_State41(self):
        return self.__statemachine_State41

    @statemachine_State41.setter
    def statemachine_State41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State41", None)
        self.__statemachine_State41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition40"):
                opp_val = getattr(old_value, "statemachine_Transition40", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition40"):
                opp_val = getattr(value, "statemachine_Transition40", None)
                setattr(value, "statemachine_Transition40", self)

    @property
    def statemachine_State30(self):
        return self.__statemachine_State30

    @statemachine_State30.setter
    def statemachine_State30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State30", None)
        self.__statemachine_State30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Transition"):
                    opp_val = getattr(item, "statemachine_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Transition"):
                    opp_val = getattr(item, "statemachine_Transition", None)
                    
                    setattr(item, "statemachine_Transition", self)
                    

    @property
    def statemachine_State32(self):
        return self.__statemachine_State32

    @statemachine_State32.setter
    def statemachine_State32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State32", None)
        self.__statemachine_State32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Thing"):
                    opp_val = getattr(item, "statemachine_Thing", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Thing", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Thing"):
                    opp_val = getattr(item, "statemachine_Thing", None)
                    
                    setattr(item, "statemachine_Thing", self)
                    

    @property
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine9"):
                opp_val = getattr(old_value, "statemachine_Statemachine9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine9"):
                opp_val = getattr(value, "statemachine_Statemachine9", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State27(self):
        return self.__statemachine_State27

    @statemachine_State27.setter
    def statemachine_State27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State27", None)
        self.__statemachine_State27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Command28"):
                    opp_val = getattr(item, "statemachine_Command28", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Command28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Command28"):
                    opp_val = getattr(item, "statemachine_Command28", None)
                    
                    setattr(item, "statemachine_Command28", self)
                    

class statemachine_Constant:

    def __init__(self, name: str, statemachine_Constant: "statemachine_Statemachine" = None, statemachine_Constant24: "statemachine_Value" = None, statemachine_Constant19: "statemachine_ConstantRef" = None):
        self.name = name
        self.statemachine_Constant = statemachine_Constant
        self.statemachine_Constant24 = statemachine_Constant24
        self.statemachine_Constant19 = statemachine_Constant19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_Constant24(self):
        return self.__statemachine_Constant24

    @statemachine_Constant24.setter
    def statemachine_Constant24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Constant__statemachine_Constant24", None)
        self.__statemachine_Constant24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Value25"):
                opp_val = getattr(old_value, "statemachine_Value25", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Value25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Value25"):
                opp_val = getattr(value, "statemachine_Value25", None)
                setattr(value, "statemachine_Value25", self)

    @property
    def statemachine_Constant19(self):
        return self.__statemachine_Constant19

    @statemachine_Constant19.setter
    def statemachine_Constant19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Constant__statemachine_Constant19", None)
        self.__statemachine_Constant19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_ConstantRef"):
                opp_val = getattr(old_value, "statemachine_ConstantRef", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_ConstantRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_ConstantRef"):
                opp_val = getattr(value, "statemachine_ConstantRef", None)
                setattr(value, "statemachine_ConstantRef", self)

    @property
    def statemachine_Constant(self):
        return self.__statemachine_Constant

    @statemachine_Constant.setter
    def statemachine_Constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Constant__statemachine_Constant", None)
        self.__statemachine_Constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine7"):
                opp_val = getattr(old_value, "statemachine_Statemachine7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine7"):
                opp_val = getattr(value, "statemachine_Statemachine7", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_Command:

    def __init__(self, name: str, code: int, statemachine_Command: "statemachine_Statemachine" = None, statemachine_Command21: "statemachine_Guard" = None, statemachine_Command28: "statemachine_State" = None):
        self.name = name
        self.code = code
        self.statemachine_Command = statemachine_Command
        self.statemachine_Command21 = statemachine_Command21
        self.statemachine_Command28 = statemachine_Command28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> int:
        return self.__code

    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def statemachine_Command(self):
        return self.__statemachine_Command

    @statemachine_Command.setter
    def statemachine_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Command__statemachine_Command", None)
        self.__statemachine_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine5"):
                opp_val = getattr(old_value, "statemachine_Statemachine5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine5"):
                opp_val = getattr(value, "statemachine_Statemachine5", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Command21(self):
        return self.__statemachine_Command21

    @statemachine_Command21.setter
    def statemachine_Command21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Command__statemachine_Command21", None)
        self.__statemachine_Command21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Guard22"):
                opp_val = getattr(old_value, "statemachine_Guard22", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Guard22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Guard22"):
                opp_val = getattr(value, "statemachine_Guard22", None)
                setattr(value, "statemachine_Guard22", self)

    @property
    def statemachine_Command28(self):
        return self.__statemachine_Command28

    @statemachine_Command28.setter
    def statemachine_Command28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Command__statemachine_Command28", None)
        self.__statemachine_Command28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State27"):
                opp_val = getattr(old_value, "statemachine_State27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State27"):
                opp_val = getattr(value, "statemachine_State27", None)
                if opp_val is None:
                    setattr(value, "statemachine_State27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_Event:

    def __init__(self, name: str, code: int, statemachine_Event: "statemachine_Statemachine" = None, statemachine_Event3: "statemachine_Statemachine" = None, statemachine_Event11: "statemachine_Guard" = None, statemachine_Event35: "statemachine_Transition" = None):
        self.name = name
        self.code = code
        self.statemachine_Event = statemachine_Event
        self.statemachine_Event3 = statemachine_Event3
        self.statemachine_Event11 = statemachine_Event11
        self.statemachine_Event35 = statemachine_Event35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> int:
        return self.__code

    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def statemachine_Event11(self):
        return self.__statemachine_Event11

    @statemachine_Event11.setter
    def statemachine_Event11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Event__statemachine_Event11", None)
        self.__statemachine_Event11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Guard"):
                opp_val = getattr(old_value, "statemachine_Guard", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Guard"):
                opp_val = getattr(value, "statemachine_Guard", None)
                setattr(value, "statemachine_Guard", self)

    @property
    def statemachine_Event3(self):
        return self.__statemachine_Event3

    @statemachine_Event3.setter
    def statemachine_Event3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Event__statemachine_Event3", None)
        self.__statemachine_Event3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine2"):
                opp_val = getattr(old_value, "statemachine_Statemachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine2"):
                opp_val = getattr(value, "statemachine_Statemachine2", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Event(self):
        return self.__statemachine_Event

    @statemachine_Event.setter
    def statemachine_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Event__statemachine_Event", None)
        self.__statemachine_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine"):
                opp_val = getattr(old_value, "statemachine_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine"):
                opp_val = getattr(value, "statemachine_Statemachine", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Event35(self):
        return self.__statemachine_Event35

    @statemachine_Event35.setter
    def statemachine_Event35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Event__statemachine_Event35", None)
        self.__statemachine_Event35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition34"):
                opp_val = getattr(old_value, "statemachine_Transition34", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition34"):
                opp_val = getattr(value, "statemachine_Transition34", None)
                setattr(value, "statemachine_Transition34", self)

class statemachine_Statemachine:

    def __init__(self, name: str, statemachine_Statemachine: set["statemachine_Event"] = None, statemachine_Statemachine2: set["statemachine_Event"] = None, statemachine_Statemachine5: set["statemachine_Command"] = None, statemachine_Statemachine7: set["statemachine_Constant"] = None, statemachine_Statemachine9: set["statemachine_State"] = None):
        self.name = name
        self.statemachine_Statemachine = statemachine_Statemachine if statemachine_Statemachine is not None else set()
        self.statemachine_Statemachine2 = statemachine_Statemachine2 if statemachine_Statemachine2 is not None else set()
        self.statemachine_Statemachine5 = statemachine_Statemachine5 if statemachine_Statemachine5 is not None else set()
        self.statemachine_Statemachine7 = statemachine_Statemachine7 if statemachine_Statemachine7 is not None else set()
        self.statemachine_Statemachine9 = statemachine_Statemachine9 if statemachine_Statemachine9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_Statemachine7(self):
        return self.__statemachine_Statemachine7

    @statemachine_Statemachine7.setter
    def statemachine_Statemachine7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statemachine__statemachine_Statemachine7", None)
        self.__statemachine_Statemachine7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Constant"):
                    opp_val = getattr(item, "statemachine_Constant", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Constant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Constant"):
                    opp_val = getattr(item, "statemachine_Constant", None)
                    
                    setattr(item, "statemachine_Constant", self)
                    

    @property
    def statemachine_Statemachine(self):
        return self.__statemachine_Statemachine

    @statemachine_Statemachine.setter
    def statemachine_Statemachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statemachine__statemachine_Statemachine", None)
        self.__statemachine_Statemachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Event"):
                    opp_val = getattr(item, "statemachine_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Event"):
                    opp_val = getattr(item, "statemachine_Event", None)
                    
                    setattr(item, "statemachine_Event", self)
                    

    @property
    def statemachine_Statemachine2(self):
        return self.__statemachine_Statemachine2

    @statemachine_Statemachine2.setter
    def statemachine_Statemachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statemachine__statemachine_Statemachine2", None)
        self.__statemachine_Statemachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Event3"):
                    opp_val = getattr(item, "statemachine_Event3", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Event3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Event3"):
                    opp_val = getattr(item, "statemachine_Event3", None)
                    
                    setattr(item, "statemachine_Event3", self)
                    

    @property
    def statemachine_Statemachine9(self):
        return self.__statemachine_Statemachine9

    @statemachine_Statemachine9.setter
    def statemachine_Statemachine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statemachine__statemachine_Statemachine9", None)
        self.__statemachine_Statemachine9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_State"):
                    opp_val = getattr(item, "statemachine_State", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_State"):
                    opp_val = getattr(item, "statemachine_State", None)
                    
                    setattr(item, "statemachine_State", self)
                    

    @property
    def statemachine_Statemachine5(self):
        return self.__statemachine_Statemachine5

    @statemachine_Statemachine5.setter
    def statemachine_Statemachine5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statemachine__statemachine_Statemachine5", None)
        self.__statemachine_Statemachine5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Command"):
                    opp_val = getattr(item, "statemachine_Command", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Command", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Command"):
                    opp_val = getattr(item, "statemachine_Command", None)
                    
                    setattr(item, "statemachine_Command", self)
                    

class Guard:

    pass
class statemachine_RangeGuard(Guard):

    pass
class statemachine_ValueGuard(Guard):

    pass