from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Object(Enum):
    ROCK = "ROCK"
    LAKE = "LAKE"
class Speed(Enum):
    FAST = "FAST"
    NORMAL = "NORMAL"
    SLOW = "SLOW"
class Color(Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"


############################################
# Definition of Classes
############################################

class DriveAction:

    pass
class taskDSL_TurnLeft(DriveAction):

    def __init__(self, degrees: int):
        self.degrees = degrees
        
    @property
    def degrees(self) -> int:
        return self.__degrees

    @degrees.setter
    def degrees(self, degrees: int):
        self.__degrees = degrees

class taskDSL_TurnRight(DriveAction):

    def __init__(self, degrees: int):
        self.degrees = degrees
        
    @property
    def degrees(self) -> int:
        return self.__degrees

    @degrees.setter
    def degrees(self, degrees: int):
        self.__degrees = degrees

class taskDSL_MoveBack(DriveAction):

    def __init__(self, meters: int):
        self.meters = meters
        
    @property
    def meters(self) -> int:
        return self.__meters

    @meters.setter
    def meters(self, meters: int):
        self.__meters = meters

class taskDSL_DriveAction:

    pass
class taskDSL_Mission:

    def __init__(self, name: str, taskDSL_Mission4: set["taskDSL_Task"] = None, taskDSL_Mission: "taskDSL_DSL" = None):
        self.name = name
        self.taskDSL_Mission4 = taskDSL_Mission4 if taskDSL_Mission4 is not None else set()
        self.taskDSL_Mission = taskDSL_Mission
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def taskDSL_Mission4(self):
        return self.__taskDSL_Mission4

    @taskDSL_Mission4.setter
    def taskDSL_Mission4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_taskDSL_Mission__taskDSL_Mission4", None)
        self.__taskDSL_Mission4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "taskDSL_Task5"):
                    opp_val = getattr(item, "taskDSL_Task5", None)
                    
                    if opp_val == self:
                        setattr(item, "taskDSL_Task5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "taskDSL_Task5"):
                    opp_val = getattr(item, "taskDSL_Task5", None)
                    
                    setattr(item, "taskDSL_Task5", self)
                    

    @property
    def taskDSL_Mission(self):
        return self.__taskDSL_Mission

    @taskDSL_Mission.setter
    def taskDSL_Mission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_taskDSL_Mission__taskDSL_Mission", None)
        self.__taskDSL_Mission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskDSL_DSL"):
                opp_val = getattr(old_value, "taskDSL_DSL", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskDSL_DSL"):
                opp_val = getattr(value, "taskDSL_DSL", None)
                if opp_val is None:
                    setattr(value, "taskDSL_DSL", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class taskDSL_DSL:

    pass
class Action:

    pass
class taskDSL_Investigate(Action):

    def __init__(self, speed: str):
        self.speed = speed
        
    @property
    def speed(self) -> str:
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed

class taskDSL_FollowLine(Action):

    def __init__(self, distance: int):
        self.distance = distance
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

class taskDSL_Speak(Action):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class taskDSL_DriveUntil(Action):

    def __init__(self, speed: str, color: str, object: str):
        self.speed = speed
        self.color = color
        self.object = object
        
    @property
    def object(self) -> str:
        return self.__object

    @object.setter
    def object(self, object: str):
        self.__object = object

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def speed(self) -> str:
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed

class taskDSL_Avoid:

    def __init__(self, color: str, object: str, taskDSL_Avoid: "taskDSL_Detector" = None, taskDSL_Avoid13: set["taskDSL_DriveAction"] = None):
        self.color = color
        self.object = object
        self.taskDSL_Avoid = taskDSL_Avoid
        self.taskDSL_Avoid13 = taskDSL_Avoid13 if taskDSL_Avoid13 is not None else set()
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def object(self) -> str:
        return self.__object

    @object.setter
    def object(self, object: str):
        self.__object = object

    @property
    def taskDSL_Avoid(self):
        return self.__taskDSL_Avoid

    @taskDSL_Avoid.setter
    def taskDSL_Avoid(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_taskDSL_Avoid__taskDSL_Avoid", None)
        self.__taskDSL_Avoid = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskDSL_Detector11"):
                opp_val = getattr(old_value, "taskDSL_Detector11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskDSL_Detector11"):
                opp_val = getattr(value, "taskDSL_Detector11", None)
                if opp_val is None:
                    setattr(value, "taskDSL_Detector11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def taskDSL_Avoid13(self):
        return self.__taskDSL_Avoid13

    @taskDSL_Avoid13.setter
    def taskDSL_Avoid13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_taskDSL_Avoid__taskDSL_Avoid13", None)
        self.__taskDSL_Avoid13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "taskDSL_DriveAction"):
                    opp_val = getattr(item, "taskDSL_DriveAction", None)
                    
                    if opp_val == self:
                        setattr(item, "taskDSL_DriveAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "taskDSL_DriveAction"):
                    opp_val = getattr(item, "taskDSL_DriveAction", None)
                    
                    setattr(item, "taskDSL_DriveAction", self)
                    

class taskDSL_Detector:

    pass
class taskDSL_Action:

    pass
class taskDSL_Task:

    def __init__(self, name: str, taskDSL_Task: "taskDSL_DSL" = None, taskDSL_Task5: "taskDSL_Mission" = None, taskDSL_Task7: "taskDSL_Action" = None, taskDSL_Task9: "taskDSL_Detector" = None):
        self.name = name
        self.taskDSL_Task = taskDSL_Task
        self.taskDSL_Task5 = taskDSL_Task5
        self.taskDSL_Task7 = taskDSL_Task7
        self.taskDSL_Task9 = taskDSL_Task9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def taskDSL_Task9(self):
        return self.__taskDSL_Task9

    @taskDSL_Task9.setter
    def taskDSL_Task9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_taskDSL_Task__taskDSL_Task9", None)
        self.__taskDSL_Task9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskDSL_Detector"):
                opp_val = getattr(old_value, "taskDSL_Detector", None)
                if opp_val == self:
                    setattr(old_value, "taskDSL_Detector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskDSL_Detector"):
                opp_val = getattr(value, "taskDSL_Detector", None)
                setattr(value, "taskDSL_Detector", self)

    @property
    def taskDSL_Task5(self):
        return self.__taskDSL_Task5

    @taskDSL_Task5.setter
    def taskDSL_Task5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_taskDSL_Task__taskDSL_Task5", None)
        self.__taskDSL_Task5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskDSL_Mission4"):
                opp_val = getattr(old_value, "taskDSL_Mission4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskDSL_Mission4"):
                opp_val = getattr(value, "taskDSL_Mission4", None)
                if opp_val is None:
                    setattr(value, "taskDSL_Mission4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def taskDSL_Task7(self):
        return self.__taskDSL_Task7

    @taskDSL_Task7.setter
    def taskDSL_Task7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_taskDSL_Task__taskDSL_Task7", None)
        self.__taskDSL_Task7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskDSL_Action"):
                opp_val = getattr(old_value, "taskDSL_Action", None)
                if opp_val == self:
                    setattr(old_value, "taskDSL_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskDSL_Action"):
                opp_val = getattr(value, "taskDSL_Action", None)
                setattr(value, "taskDSL_Action", self)

    @property
    def taskDSL_Task(self):
        return self.__taskDSL_Task

    @taskDSL_Task.setter
    def taskDSL_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_taskDSL_Task__taskDSL_Task", None)
        self.__taskDSL_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskDSL_DSL2"):
                opp_val = getattr(old_value, "taskDSL_DSL2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskDSL_DSL2"):
                opp_val = getattr(value, "taskDSL_DSL2", None)
                if opp_val is None:
                    setattr(value, "taskDSL_DSL2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
