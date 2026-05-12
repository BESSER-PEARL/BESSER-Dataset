from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Elevator1:

    def __init__(self, id: int):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class Elevator_Request:

    pass


class Floor:

    def __init__(self, Id: int):
        self.Id = Id
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id



class Bridge:

    pass


class Floor_button:

    def __init__(self, Floor_num: int, Direction: bool):
        self.Floor_num = Floor_num
        self.Direction = Direction
        
        pass
    @property
    def Floor_num(self):
        return self.__Floor_num
    @Floor_num.setter
    def Floor_num(self, Floor_num: int):
        self.__Floor_num = Floor_num

    @property
    def Direction(self):
        return self.__Direction
    @Direction.setter
    def Direction(self, Direction: bool):
        self.__Direction = Direction



class Elevator_button:

    def __init__(self, Floor_num: int):
        self.Floor_num = Floor_num
        
        pass
    @property
    def Floor_num(self):
        return self.__Floor_num
    @Floor_num.setter
    def Floor_num(self, Floor_num: int):
        self.__Floor_num = Floor_num



class Button:

    def __init__(self, illuminate: str, m7: "Elevator_Controller" = None):
        self.illuminate = illuminate
        self.m7 = m7
        
        pass
    @property
    def illuminate(self):
        return self.__illuminate
    @illuminate.setter
    def illuminate(self, illuminate: str):
        self.__illuminate = illuminate

    @property
    def m7(self):
        return self.__m7
    @m7.setter
    def m7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Button__m7", None)
        self.__m7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_16"):
                opp_val = getattr(old_value, "_16", None)
                if opp_val == self:
                    setattr(old_value, "_16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_16"):
                opp_val = getattr(value, "_16", None)
                setattr(value, "_16", self)



class Door:

    def __init__(self, Close: str, elevator_Controller3: "Elevator_Controller" = None):
        self.Close = Close
        self.elevator_Controller3 = elevator_Controller3
        
        pass
    @property
    def Close(self):
        return self.__Close
    @Close.setter
    def Close(self, Close: str):
        self.__Close = Close

    @property
    def elevator_Controller3(self):
        return self.__elevator_Controller3
    @elevator_Controller3.setter
    def elevator_Controller3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Door__elevator_Controller3", None)
        self.__elevator_Controller3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "N2"):
                opp_val = getattr(old_value, "N2", None)
                if opp_val == self:
                    setattr(old_value, "N2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "N2"):
                opp_val = getattr(value, "N2", None)
                setattr(value, "N2", self)



class Elevator:

    def __init__(self, Direction: bool, Current_Floor: int, attribute3: str, elevator_Controller0: "Elevator_Controller" = None, _14: "Elevator_Controller" = None):
        self.Direction = Direction
        self.Current_Floor = Current_Floor
        self.attribute3 = attribute3
        self.elevator_Controller0 = elevator_Controller0
        self._14 = _14
        
        pass
    @property
    def Direction(self):
        return self.__Direction
    @Direction.setter
    def Direction(self, Direction: bool):
        self.__Direction = Direction

    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: str):
        self.__attribute3 = attribute3

    @property
    def Current_Floor(self):
        return self.__Current_Floor
    @Current_Floor.setter
    def Current_Floor(self, Current_Floor: int):
        self.__Current_Floor = Current_Floor

    @property
    def _14(self):
        return self.___14
    @_14.setter
    def _14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator___14", None)
        self.___14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "n5"):
                opp_val = getattr(old_value, "n5", None)
                if opp_val == self:
                    setattr(old_value, "n5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "n5"):
                opp_val = getattr(value, "n5", None)
                setattr(value, "n5", self)

    @property
    def elevator_Controller0(self):
        return self.__elevator_Controller0
    @elevator_Controller0.setter
    def elevator_Controller0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator__elevator_Controller0", None)
        self.__elevator_Controller0 = value
        
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



class _unnamed1:

    pass


class Elevator_Controller_2:

    def __init__(self, Floor_ID: int, Position: int, Direction: bool, attribute: str):
        self.Floor_ID = Floor_ID
        self.Position = Position
        self.Direction = Direction
        self.attribute = attribute
        
        pass
    @property
    def Direction(self):
        return self.__Direction
    @Direction.setter
    def Direction(self, Direction: bool):
        self.__Direction = Direction

    @property
    def Position(self):
        return self.__Position
    @Position.setter
    def Position(self, Position: int):
        self.__Position = Position

    @property
    def Floor_ID(self):
        return self.__Floor_ID
    @Floor_ID.setter
    def Floor_ID(self, Floor_ID: int):
        self.__Floor_ID = Floor_ID

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class _unnamed:

    pass


class Elevator_Controller:

    def __init__(self, Floor_ID: int, Position: int, Direction: bool, attribute: str, elevator1: "Elevator" = None, N2: "Door" = None, n5: "Elevator" = None, _16: "Button" = None):
        self.Floor_ID = Floor_ID
        self.Position = Position
        self.Direction = Direction
        self.attribute = attribute
        self.elevator1 = elevator1
        self.N2 = N2
        self.n5 = n5
        self._16 = _16
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Direction(self):
        return self.__Direction
    @Direction.setter
    def Direction(self, Direction: bool):
        self.__Direction = Direction

    @property
    def Floor_ID(self):
        return self.__Floor_ID
    @Floor_ID.setter
    def Floor_ID(self, Floor_ID: int):
        self.__Floor_ID = Floor_ID

    @property
    def Position(self):
        return self.__Position
    @Position.setter
    def Position(self, Position: int):
        self.__Position = Position

    @property
    def N2(self):
        return self.__N2
    @N2.setter
    def N2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator_Controller__N2", None)
        self.__N2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator_Controller3"):
                opp_val = getattr(old_value, "elevator_Controller3", None)
                if opp_val == self:
                    setattr(old_value, "elevator_Controller3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator_Controller3"):
                opp_val = getattr(value, "elevator_Controller3", None)
                setattr(value, "elevator_Controller3", self)

    @property
    def elevator1(self):
        return self.__elevator1
    @elevator1.setter
    def elevator1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator_Controller__elevator1", None)
        self.__elevator1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator_Controller0"):
                opp_val = getattr(old_value, "elevator_Controller0", None)
                if opp_val == self:
                    setattr(old_value, "elevator_Controller0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator_Controller0"):
                opp_val = getattr(value, "elevator_Controller0", None)
                setattr(value, "elevator_Controller0", self)

    @property
    def _16(self):
        return self.___16
    @_16.setter
    def _16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator_Controller___16", None)
        self.___16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "m7"):
                opp_val = getattr(old_value, "m7", None)
                if opp_val == self:
                    setattr(old_value, "m7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "m7"):
                opp_val = getattr(value, "m7", None)
                setattr(value, "m7", self)

    @property
    def n5(self):
        return self.__n5
    @n5.setter
    def n5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator_Controller__n5", None)
        self.__n5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_14"):
                opp_val = getattr(old_value, "_14", None)
                if opp_val == self:
                    setattr(old_value, "_14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_14"):
                opp_val = getattr(value, "_14", None)
                setattr(value, "_14", self)

