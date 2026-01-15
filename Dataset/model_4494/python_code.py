from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    COLOR_BLACK = "COLOR_BLACK"
    COLOR_OFF = "COLOR_OFF"
    COLOR_RED = "COLOR_RED"
    COLOR_BLUE = "COLOR_BLUE"
    COLOR_GREEN = "COLOR_GREEN"
    COLOR_ORANGE = "COLOR_ORANGE"
    COLOR_WHITE = "COLOR_WHITE"
class LED_Color(Enum):
    LED_ORANGE = "LED_ORANGE"
    LED_RED = "LED_RED"
    LED_GREEN = "LED_GREEN"
    LED_OFF = "LED_OFF"


############################################
# Definition of Classes
############################################

class marsRover_park:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class marsRover_color_indication:

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class marsRover_message:

    def __init__(self, name: str, msg: str):
        self.name = name
        self.msg = msg
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def msg(self) -> str:
        return self.__msg

    @msg.setter
    def msg(self, msg: str):
        self.__msg = msg

class marsRover_sound:

    def __init__(self, name: str, duration: int, frequency: int):
        self.name = name
        self.duration = duration
        self.frequency = frequency
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def frequency(self) -> int:
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: int):
        self.__frequency = frequency

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

class marsRover_indication:

    def __init__(self, name: str, marsRover_indication: "marsRover_after_action" = None, marsRover_indication11: "marsRover_EObject" = None):
        self.name = name
        self.marsRover_indication = marsRover_indication
        self.marsRover_indication11 = marsRover_indication11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def marsRover_indication11(self):
        return self.__marsRover_indication11

    @marsRover_indication11.setter
    def marsRover_indication11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_marsRover_indication__marsRover_indication11", None)
        self.__marsRover_indication11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "marsRover_EObject12"):
                opp_val = getattr(old_value, "marsRover_EObject12", None)
                if opp_val == self:
                    setattr(old_value, "marsRover_EObject12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "marsRover_EObject12"):
                opp_val = getattr(value, "marsRover_EObject12", None)
                setattr(value, "marsRover_EObject12", self)

    @property
    def marsRover_indication(self):
        return self.__marsRover_indication

    @marsRover_indication.setter
    def marsRover_indication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_marsRover_indication__marsRover_indication", None)
        self.__marsRover_indication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "marsRover_after_action9"):
                opp_val = getattr(old_value, "marsRover_after_action9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "marsRover_after_action9"):
                opp_val = getattr(value, "marsRover_after_action9", None)
                if opp_val is None:
                    setattr(value, "marsRover_after_action9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class marsRover_push_obstacles:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class marsRover_avoid_lakes:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class marsRover_avoid_obstacles:

    def __init__(self, name: str, marsRover_avoid_obstacles: set["marsRover_EObject"] = None):
        self.name = name
        self.marsRover_avoid_obstacles = marsRover_avoid_obstacles if marsRover_avoid_obstacles is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def marsRover_avoid_obstacles(self):
        return self.__marsRover_avoid_obstacles

    @marsRover_avoid_obstacles.setter
    def marsRover_avoid_obstacles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_marsRover_avoid_obstacles__marsRover_avoid_obstacles", None)
        self.__marsRover_avoid_obstacles = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "marsRover_EObject4"):
                    opp_val = getattr(item, "marsRover_EObject4", None)
                    
                    if opp_val == self:
                        setattr(item, "marsRover_EObject4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "marsRover_EObject4"):
                    opp_val = getattr(item, "marsRover_EObject4", None)
                    
                    setattr(item, "marsRover_EObject4", self)
                    

class marsRover_EObject:

    pass
class marsRover_mission:

    def __init__(self, name: str, marsRover_mission: "marsRover_Robot" = None, marsRover_mission2: "marsRover_EObject" = None):
        self.name = name
        self.marsRover_mission = marsRover_mission
        self.marsRover_mission2 = marsRover_mission2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def marsRover_mission(self):
        return self.__marsRover_mission

    @marsRover_mission.setter
    def marsRover_mission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_marsRover_mission__marsRover_mission", None)
        self.__marsRover_mission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "marsRover_Robot"):
                opp_val = getattr(old_value, "marsRover_Robot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "marsRover_Robot"):
                opp_val = getattr(value, "marsRover_Robot", None)
                if opp_val is None:
                    setattr(value, "marsRover_Robot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def marsRover_mission2(self):
        return self.__marsRover_mission2

    @marsRover_mission2.setter
    def marsRover_mission2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_marsRover_mission__marsRover_mission2", None)
        self.__marsRover_mission2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "marsRover_EObject"):
                opp_val = getattr(old_value, "marsRover_EObject", None)
                if opp_val == self:
                    setattr(old_value, "marsRover_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "marsRover_EObject"):
                opp_val = getattr(value, "marsRover_EObject", None)
                setattr(value, "marsRover_EObject", self)

class marsRover_Robot:

    def __init__(self, name: str, slave_address: str, drive_speed: int, special_speed: int, marsRover_Robot: set["marsRover_mission"] = None):
        self.name = name
        self.slave_address = slave_address
        self.drive_speed = drive_speed
        self.special_speed = special_speed
        self.marsRover_Robot = marsRover_Robot if marsRover_Robot is not None else set()
        
    @property
    def drive_speed(self) -> int:
        return self.__drive_speed

    @drive_speed.setter
    def drive_speed(self, drive_speed: int):
        self.__drive_speed = drive_speed

    @property
    def slave_address(self) -> str:
        return self.__slave_address

    @slave_address.setter
    def slave_address(self, slave_address: str):
        self.__slave_address = slave_address

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def special_speed(self) -> int:
        return self.__special_speed

    @special_speed.setter
    def special_speed(self, special_speed: int):
        self.__special_speed = special_speed

    @property
    def marsRover_Robot(self):
        return self.__marsRover_Robot

    @marsRover_Robot.setter
    def marsRover_Robot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_marsRover_Robot__marsRover_Robot", None)
        self.__marsRover_Robot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "marsRover_mission"):
                    opp_val = getattr(item, "marsRover_mission", None)
                    
                    if opp_val == self:
                        setattr(item, "marsRover_mission", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "marsRover_mission"):
                    opp_val = getattr(item, "marsRover_mission", None)
                    
                    setattr(item, "marsRover_mission", self)
                    

class marsRover_detect_rocks:

    def __init__(self, name: str, number_of_rocks: int, marsRover_detect_rocks: "marsRover_after_action" = None):
        self.name = name
        self.number_of_rocks = number_of_rocks
        self.marsRover_detect_rocks = marsRover_detect_rocks
        
    @property
    def number_of_rocks(self) -> int:
        return self.__number_of_rocks

    @number_of_rocks.setter
    def number_of_rocks(self, number_of_rocks: int):
        self.__number_of_rocks = number_of_rocks

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def marsRover_detect_rocks(self):
        return self.__marsRover_detect_rocks

    @marsRover_detect_rocks.setter
    def marsRover_detect_rocks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_marsRover_detect_rocks__marsRover_detect_rocks", None)
        self.__marsRover_detect_rocks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "marsRover_after_action7"):
                opp_val = getattr(old_value, "marsRover_after_action7", None)
                if opp_val == self:
                    setattr(old_value, "marsRover_after_action7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "marsRover_after_action7"):
                opp_val = getattr(value, "marsRover_after_action7", None)
                setattr(value, "marsRover_after_action7", self)

class marsRover_after_action:

    def __init__(self, action: str, marsRover_after_action: "marsRover_detect_lakes" = None, marsRover_after_action7: "marsRover_detect_rocks" = None, marsRover_after_action9: set["marsRover_indication"] = None):
        self.action = action
        self.marsRover_after_action = marsRover_after_action
        self.marsRover_after_action7 = marsRover_after_action7
        self.marsRover_after_action9 = marsRover_after_action9 if marsRover_after_action9 is not None else set()
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def marsRover_after_action9(self):
        return self.__marsRover_after_action9

    @marsRover_after_action9.setter
    def marsRover_after_action9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_marsRover_after_action__marsRover_after_action9", None)
        self.__marsRover_after_action9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "marsRover_indication"):
                    opp_val = getattr(item, "marsRover_indication", None)
                    
                    if opp_val == self:
                        setattr(item, "marsRover_indication", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "marsRover_indication"):
                    opp_val = getattr(item, "marsRover_indication", None)
                    
                    setattr(item, "marsRover_indication", self)
                    

    @property
    def marsRover_after_action7(self):
        return self.__marsRover_after_action7

    @marsRover_after_action7.setter
    def marsRover_after_action7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_marsRover_after_action__marsRover_after_action7", None)
        self.__marsRover_after_action7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "marsRover_detect_rocks"):
                opp_val = getattr(old_value, "marsRover_detect_rocks", None)
                if opp_val == self:
                    setattr(old_value, "marsRover_detect_rocks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "marsRover_detect_rocks"):
                opp_val = getattr(value, "marsRover_detect_rocks", None)
                setattr(value, "marsRover_detect_rocks", self)

    @property
    def marsRover_after_action(self):
        return self.__marsRover_after_action

    @marsRover_after_action.setter
    def marsRover_after_action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_marsRover_after_action__marsRover_after_action", None)
        self.__marsRover_after_action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "marsRover_detect_lakes"):
                opp_val = getattr(old_value, "marsRover_detect_lakes", None)
                if opp_val == self:
                    setattr(old_value, "marsRover_detect_lakes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "marsRover_detect_lakes"):
                opp_val = getattr(value, "marsRover_detect_lakes", None)
                setattr(value, "marsRover_detect_lakes", self)

class marsRover_detect_lakes:

    def __init__(self, name: str, number_of_lakes: int, lakes_colors: str, marsRover_detect_lakes: "marsRover_after_action" = None):
        self.name = name
        self.number_of_lakes = number_of_lakes
        self.lakes_colors = lakes_colors
        self.marsRover_detect_lakes = marsRover_detect_lakes
        
    @property
    def lakes_colors(self) -> str:
        return self.__lakes_colors

    @lakes_colors.setter
    def lakes_colors(self, lakes_colors: str):
        self.__lakes_colors = lakes_colors

    @property
    def number_of_lakes(self) -> int:
        return self.__number_of_lakes

    @number_of_lakes.setter
    def number_of_lakes(self, number_of_lakes: int):
        self.__number_of_lakes = number_of_lakes

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def marsRover_detect_lakes(self):
        return self.__marsRover_detect_lakes

    @marsRover_detect_lakes.setter
    def marsRover_detect_lakes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_marsRover_detect_lakes__marsRover_detect_lakes", None)
        self.__marsRover_detect_lakes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "marsRover_after_action"):
                opp_val = getattr(old_value, "marsRover_after_action", None)
                if opp_val == self:
                    setattr(old_value, "marsRover_after_action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "marsRover_after_action"):
                opp_val = getattr(value, "marsRover_after_action", None)
                setattr(value, "marsRover_after_action", self)

class marsRover_bumpers:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class marsRover_ultra:

    def __init__(self, name: str, distance: int):
        self.name = name
        self.distance = distance
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance
