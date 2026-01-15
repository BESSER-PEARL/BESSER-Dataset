from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ArduinoCard_BlockInteraction(ABC):

    def __init__(self, isHigh: bool, name: str, ArduinoCard_BlockInteraction: "ArduinoCard_Card" = None):
        self.isHigh = isHigh
        self.name = name
        self.ArduinoCard_BlockInteraction = ArduinoCard_BlockInteraction
        
    @property
    def isHigh(self) -> bool:
        return self.__isHigh

    @isHigh.setter
    def isHigh(self, isHigh: bool):
        self.__isHigh = isHigh

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ArduinoCard_BlockInteraction(self):
        return self.__ArduinoCard_BlockInteraction

    @ArduinoCard_BlockInteraction.setter
    def ArduinoCard_BlockInteraction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoCard_BlockInteraction__ArduinoCard_BlockInteraction", None)
        self.__ArduinoCard_BlockInteraction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArduinoCard_Card18"):
                opp_val = getattr(old_value, "ArduinoCard_Card18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArduinoCard_Card18"):
                opp_val = getattr(value, "ArduinoCard_Card18", None)
                if opp_val is None:
                    setattr(value, "ArduinoCard_Card18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ArduinoCard_Card:

    pass
class BlockInteraction:

    pass
class ArduinoCard_Condition(BlockInteraction):

    pass
class Block:

    pass
class ArduinoCard_Actuator(Block):

    pass
class ArduinoCard_Sensor(Block):

    pass
class ArduinoCard_Block(ABC):

    def __init__(self, name: str, pinNumber: int, isAnalogic: str, ArduinoCard_Block: "ArduinoCard_Card" = None):
        self.name = name
        self.pinNumber = pinNumber
        self.isAnalogic = isAnalogic
        self.ArduinoCard_Block = ArduinoCard_Block
        
    @property
    def pinNumber(self) -> int:
        return self.__pinNumber

    @pinNumber.setter
    def pinNumber(self, pinNumber: int):
        self.__pinNumber = pinNumber

    @property
    def isAnalogic(self) -> str:
        return self.__isAnalogic

    @isAnalogic.setter
    def isAnalogic(self, isAnalogic: str):
        self.__isAnalogic = isAnalogic

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ArduinoCard_Block(self):
        return self.__ArduinoCard_Block

    @ArduinoCard_Block.setter
    def ArduinoCard_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoCard_Block__ArduinoCard_Block", None)
        self.__ArduinoCard_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArduinoCard_Card20"):
                opp_val = getattr(old_value, "ArduinoCard_Card20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArduinoCard_Card20"):
                opp_val = getattr(value, "ArduinoCard_Card20", None)
                if opp_val is None:
                    setattr(value, "ArduinoCard_Card20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ArduinoCard_Command(BlockInteraction):

    pass
class ArduinoCard_Transition:

    def __init__(self, name: str, ArduinoCard_Transition: "ArduinoCard_State" = None, ArduinoCard_Transition5: "ArduinoCard_State" = None, ArduinoCard_Transition8: set["ArduinoCard_Condition"] = None, ArduinoCard_Transition16: "ArduinoCard_Card" = None):
        self.name = name
        self.ArduinoCard_Transition = ArduinoCard_Transition
        self.ArduinoCard_Transition5 = ArduinoCard_Transition5
        self.ArduinoCard_Transition8 = ArduinoCard_Transition8 if ArduinoCard_Transition8 is not None else set()
        self.ArduinoCard_Transition16 = ArduinoCard_Transition16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ArduinoCard_Transition8(self):
        return self.__ArduinoCard_Transition8

    @ArduinoCard_Transition8.setter
    def ArduinoCard_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoCard_Transition__ArduinoCard_Transition8", None)
        self.__ArduinoCard_Transition8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArduinoCard_Condition9"):
                    opp_val = getattr(item, "ArduinoCard_Condition9", None)
                    
                    if opp_val == self:
                        setattr(item, "ArduinoCard_Condition9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArduinoCard_Condition9"):
                    opp_val = getattr(item, "ArduinoCard_Condition9", None)
                    
                    setattr(item, "ArduinoCard_Condition9", self)
                    

    @property
    def ArduinoCard_Transition16(self):
        return self.__ArduinoCard_Transition16

    @ArduinoCard_Transition16.setter
    def ArduinoCard_Transition16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoCard_Transition__ArduinoCard_Transition16", None)
        self.__ArduinoCard_Transition16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArduinoCard_Card15"):
                opp_val = getattr(old_value, "ArduinoCard_Card15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArduinoCard_Card15"):
                opp_val = getattr(value, "ArduinoCard_Card15", None)
                if opp_val is None:
                    setattr(value, "ArduinoCard_Card15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ArduinoCard_Transition5(self):
        return self.__ArduinoCard_Transition5

    @ArduinoCard_Transition5.setter
    def ArduinoCard_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoCard_Transition__ArduinoCard_Transition5", None)
        self.__ArduinoCard_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArduinoCard_State6"):
                opp_val = getattr(old_value, "ArduinoCard_State6", None)
                if opp_val == self:
                    setattr(old_value, "ArduinoCard_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArduinoCard_State6"):
                opp_val = getattr(value, "ArduinoCard_State6", None)
                setattr(value, "ArduinoCard_State6", self)

    @property
    def ArduinoCard_Transition(self):
        return self.__ArduinoCard_Transition

    @ArduinoCard_Transition.setter
    def ArduinoCard_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoCard_Transition__ArduinoCard_Transition", None)
        self.__ArduinoCard_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArduinoCard_State"):
                opp_val = getattr(old_value, "ArduinoCard_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArduinoCard_State"):
                opp_val = getattr(value, "ArduinoCard_State", None)
                if opp_val is None:
                    setattr(value, "ArduinoCard_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ArduinoCard_State:

    def __init__(self, name: str, isInitial: bool, ArduinoCard_State: set["ArduinoCard_Transition"] = None, ArduinoCard_State2: set["ArduinoCard_Command"] = None, ArduinoCard_State6: "ArduinoCard_Transition" = None, ArduinoCard_State13: "ArduinoCard_Card" = None):
        self.name = name
        self.isInitial = isInitial
        self.ArduinoCard_State = ArduinoCard_State if ArduinoCard_State is not None else set()
        self.ArduinoCard_State2 = ArduinoCard_State2 if ArduinoCard_State2 is not None else set()
        self.ArduinoCard_State6 = ArduinoCard_State6
        self.ArduinoCard_State13 = ArduinoCard_State13
        
    @property
    def isInitial(self) -> bool:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ArduinoCard_State(self):
        return self.__ArduinoCard_State

    @ArduinoCard_State.setter
    def ArduinoCard_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoCard_State__ArduinoCard_State", None)
        self.__ArduinoCard_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArduinoCard_Transition"):
                    opp_val = getattr(item, "ArduinoCard_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "ArduinoCard_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArduinoCard_Transition"):
                    opp_val = getattr(item, "ArduinoCard_Transition", None)
                    
                    setattr(item, "ArduinoCard_Transition", self)
                    

    @property
    def ArduinoCard_State6(self):
        return self.__ArduinoCard_State6

    @ArduinoCard_State6.setter
    def ArduinoCard_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoCard_State__ArduinoCard_State6", None)
        self.__ArduinoCard_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArduinoCard_Transition5"):
                opp_val = getattr(old_value, "ArduinoCard_Transition5", None)
                if opp_val == self:
                    setattr(old_value, "ArduinoCard_Transition5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArduinoCard_Transition5"):
                opp_val = getattr(value, "ArduinoCard_Transition5", None)
                setattr(value, "ArduinoCard_Transition5", self)

    @property
    def ArduinoCard_State2(self):
        return self.__ArduinoCard_State2

    @ArduinoCard_State2.setter
    def ArduinoCard_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoCard_State__ArduinoCard_State2", None)
        self.__ArduinoCard_State2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArduinoCard_Command"):
                    opp_val = getattr(item, "ArduinoCard_Command", None)
                    
                    if opp_val == self:
                        setattr(item, "ArduinoCard_Command", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArduinoCard_Command"):
                    opp_val = getattr(item, "ArduinoCard_Command", None)
                    
                    setattr(item, "ArduinoCard_Command", self)
                    

    @property
    def ArduinoCard_State13(self):
        return self.__ArduinoCard_State13

    @ArduinoCard_State13.setter
    def ArduinoCard_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ArduinoCard_State__ArduinoCard_State13", None)
        self.__ArduinoCard_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArduinoCard_Card"):
                opp_val = getattr(old_value, "ArduinoCard_Card", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArduinoCard_Card"):
                opp_val = getattr(value, "ArduinoCard_Card", None)
                if opp_val is None:
                    setattr(value, "ArduinoCard_Card", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
