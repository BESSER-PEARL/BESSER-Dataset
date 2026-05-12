from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class floor_s_buttons:

    def __init__(self, number: bool):
        self.number = number
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: bool):
        self.__number = number



class elevator_s_buttons:

    def __init__(self, number: int):
        self.number = number
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number



class button:

    def __init__(self, number: int, elevator3: "elevator" = None):
        self.number = number
        self.elevator3 = elevator3
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def elevator3(self):
        return self.__elevator3
    @elevator3.setter
    def elevator3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_button__elevator3", None)
        self.__elevator3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "button2"):
                opp_val = getattr(old_value, "button2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "button2"):
                opp_val = getattr(value, "button2", None)
                if opp_val is None:
                    setattr(value, "button2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class door:

    def __init__(self, close: bool, elevator1: "elevator" = None):
        self.close = close
        self.elevator1 = elevator1
        
        pass
    @property
    def close(self):
        return self.__close
    @close.setter
    def close(self, close: bool):
        self.__close = close

    @property
    def elevator1(self):
        return self.__elevator1
    @elevator1.setter
    def elevator1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_door__elevator1", None)
        self.__elevator1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "door0"):
                opp_val = getattr(old_value, "door0", None)
                if opp_val == self:
                    setattr(old_value, "door0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "door0"):
                opp_val = getattr(value, "door0", None)
                setattr(value, "door0", self)



class elevator:

    def __init__(self, floor: int, door0: "door" = None, button2: set["button"] = None):
        self.floor = floor
        self.door0 = door0
        self.button2 = button2 if button2 is not None else set()
        
        pass
    @property
    def floor(self):
        return self.__floor
    @floor.setter
    def floor(self, floor: int):
        self.__floor = floor

    @property
    def door0(self):
        return self.__door0
    @door0.setter
    def door0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_elevator__door0", None)
        self.__door0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator1"):
                opp_val = getattr(old_value, "elevator1", None)
                if opp_val == self:
                    setattr(old_value, "elevator1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator1"):
                opp_val = getattr(value, "elevator1", None)
                setattr(value, "elevator1", self)

    @property
    def button2(self):
        return self.__button2
    @button2.setter
    def button2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_elevator__button2", None)
        self.__button2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elevator3"):
                    opp_val = getattr(item, "elevator3", None)
                    
                    if opp_val == self:
                        setattr(item, "elevator3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elevator3"):
                    opp_val = getattr(item, "elevator3", None)
                    
                    setattr(item, "elevator3", self)
                    

