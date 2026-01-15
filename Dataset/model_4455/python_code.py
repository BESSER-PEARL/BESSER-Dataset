from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Action:

    pass
class arduinoml_On(Action):

    def __init__(self):
        
    def turnOn(self):
        # TODO: Implement turnOn method
        pass

class arduinoml_Off(Action):

    def __init__(self):
        
    def turnOff(self):
        # TODO: Implement turnOff method
        pass

class arduinoml_ActuatorState:

    def __init__(self, isOn: bool, arduinoml_ActuatorState: "arduinoml_Actuator" = None, arduinoml_ActuatorState20: "arduinoml_Transition" = None):
        self.isOn = isOn
        self.arduinoml_ActuatorState = arduinoml_ActuatorState
        self.arduinoml_ActuatorState20 = arduinoml_ActuatorState20
        
    @property
    def isOn(self) -> bool:
        return self.__isOn

    @isOn.setter
    def isOn(self, isOn: bool):
        self.__isOn = isOn

    @property
    def arduinoml_ActuatorState(self):
        return self.__arduinoml_ActuatorState

    @arduinoml_ActuatorState.setter
    def arduinoml_ActuatorState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_ActuatorState__arduinoml_ActuatorState", None)
        self.__arduinoml_ActuatorState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_Actuator"):
                opp_val = getattr(old_value, "arduinoml_Actuator", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_Actuator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_Actuator"):
                opp_val = getattr(value, "arduinoml_Actuator", None)
                setattr(value, "arduinoml_Actuator", self)

    @property
    def arduinoml_ActuatorState20(self):
        return self.__arduinoml_ActuatorState20

    @arduinoml_ActuatorState20.setter
    def arduinoml_ActuatorState20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_ActuatorState__arduinoml_ActuatorState20", None)
        self.__arduinoml_ActuatorState20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_Transition21"):
                opp_val = getattr(old_value, "arduinoml_Transition21", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_Transition21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_Transition21"):
                opp_val = getattr(value, "arduinoml_Transition21", None)
                setattr(value, "arduinoml_Transition21", self)

class Brick:

    pass
class arduinoml_Sensor(Brick):

    pass
class arduinoml_Actuator(Brick):

    pass
class arduinoml_Transition:

    pass
class arduinoml_Action(ABC):

    pass
class arduinoml_Brick(ABC):

    def __init__(self, name: str, pin: int, arduinoml_Brick: "arduinoml_Board" = None):
        self.name = name
        self.pin = pin
        self.arduinoml_Brick = arduinoml_Brick
        
    @property
    def pin(self) -> int:
        return self.__pin

    @pin.setter
    def pin(self, pin: int):
        self.__pin = pin

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduinoml_Brick(self):
        return self.__arduinoml_Brick

    @arduinoml_Brick.setter
    def arduinoml_Brick(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_Brick__arduinoml_Brick", None)
        self.__arduinoml_Brick = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_Board5"):
                opp_val = getattr(old_value, "arduinoml_Board5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_Board5"):
                opp_val = getattr(value, "arduinoml_Board5", None)
                if opp_val is None:
                    setattr(value, "arduinoml_Board5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduinoml_State:

    def __init__(self, name: str, arduinoml_State: "arduinoml_Board" = None, arduinoml_State3: "arduinoml_Board" = None, arduinoml_State7: set["arduinoml_Action"] = None, arduinoml_State9: set["arduinoml_Transition"] = None, arduinoml_State13: "arduinoml_Transition" = None, arduinoml_State16: "arduinoml_Transition" = None):
        self.name = name
        self.arduinoml_State = arduinoml_State
        self.arduinoml_State3 = arduinoml_State3
        self.arduinoml_State7 = arduinoml_State7 if arduinoml_State7 is not None else set()
        self.arduinoml_State9 = arduinoml_State9 if arduinoml_State9 is not None else set()
        self.arduinoml_State13 = arduinoml_State13
        self.arduinoml_State16 = arduinoml_State16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduinoml_State3(self):
        return self.__arduinoml_State3

    @arduinoml_State3.setter
    def arduinoml_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_State__arduinoml_State3", None)
        self.__arduinoml_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_Board2"):
                opp_val = getattr(old_value, "arduinoml_Board2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_Board2"):
                opp_val = getattr(value, "arduinoml_Board2", None)
                if opp_val is None:
                    setattr(value, "arduinoml_Board2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduinoml_State(self):
        return self.__arduinoml_State

    @arduinoml_State.setter
    def arduinoml_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_State__arduinoml_State", None)
        self.__arduinoml_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_Board"):
                opp_val = getattr(old_value, "arduinoml_Board", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_Board", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_Board"):
                opp_val = getattr(value, "arduinoml_Board", None)
                setattr(value, "arduinoml_Board", self)

    @property
    def arduinoml_State16(self):
        return self.__arduinoml_State16

    @arduinoml_State16.setter
    def arduinoml_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_State__arduinoml_State16", None)
        self.__arduinoml_State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_Transition15"):
                opp_val = getattr(old_value, "arduinoml_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_Transition15"):
                opp_val = getattr(value, "arduinoml_Transition15", None)
                setattr(value, "arduinoml_Transition15", self)

    @property
    def arduinoml_State9(self):
        return self.__arduinoml_State9

    @arduinoml_State9.setter
    def arduinoml_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_State__arduinoml_State9", None)
        self.__arduinoml_State9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoml_Transition"):
                    opp_val = getattr(item, "arduinoml_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoml_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoml_Transition"):
                    opp_val = getattr(item, "arduinoml_Transition", None)
                    
                    setattr(item, "arduinoml_Transition", self)
                    

    @property
    def arduinoml_State13(self):
        return self.__arduinoml_State13

    @arduinoml_State13.setter
    def arduinoml_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_State__arduinoml_State13", None)
        self.__arduinoml_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_Transition12"):
                opp_val = getattr(old_value, "arduinoml_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_Transition12"):
                opp_val = getattr(value, "arduinoml_Transition12", None)
                setattr(value, "arduinoml_Transition12", self)

    @property
    def arduinoml_State7(self):
        return self.__arduinoml_State7

    @arduinoml_State7.setter
    def arduinoml_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_State__arduinoml_State7", None)
        self.__arduinoml_State7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoml_Action"):
                    opp_val = getattr(item, "arduinoml_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoml_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoml_Action"):
                    opp_val = getattr(item, "arduinoml_Action", None)
                    
                    setattr(item, "arduinoml_Action", self)
                    

class arduinoml_Board:

    pass