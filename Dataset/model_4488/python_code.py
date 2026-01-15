from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EdgeEnum(Enum):
    FRONTLEFT = "FRONTLEFT"
    FRONTRIGHT = "FRONTRIGHT"
    BACK = "BACK"
class BackEnum(Enum):
    BACK = "BACK"
class TouchEnum(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class Tenum(Enum):
    TRUE = "TRUE"
class ColorEnum(Enum):
    NONE = "NONE"
    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"
    WHITE = "WHITE"
    BROWN = "BROWN"
class LREnum(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class MAEnum(Enum):
    MEASURE = "MEASURE"
class FBEnum(Enum):
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
class ActionEnum(Enum):
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
    STOP = "STOP"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class dSL_EdgeLiteral(Expression):

    def __init__(self, edge: str):
        self.edge = edge
        
    @property
    def edge(self) -> str:
        return self.__edge

    @edge.setter
    def edge(self, edge: str):
        self.__edge = edge

class dSL_ExpressionBracket(Expression):

    pass
class dSL_ANDexpression(Expression):

    pass
class dSL_TouchLiteral(Expression):

    def __init__(self, touch: str):
        self.touch = touch
        
    @property
    def touch(self) -> str:
        return self.__touch

    @touch.setter
    def touch(self, touch: str):
        self.__touch = touch

class dSL_ORexpression(Expression):

    pass
class dSL_ColorLiteral(Expression):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class dSL_DistanceLiteral(Expression):

    def __init__(self, distance: int):
        self.distance = distance
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

class dSL_DepthLiteral(Expression):

    def __init__(self, back: str):
        self.back = back
        
    @property
    def back(self) -> str:
        return self.__back

    @back.setter
    def back(self, back: str):
        self.__back = back

class dSL_TrueLiteral(Expression):

    def __init__(self, t: str):
        self.t = t
        
    @property
    def t(self) -> str:
        return self.__t

    @t.setter
    def t(self, t: str):
        self.__t = t

class RotatePoints:

    pass
class dSL_RightRotatePoint(RotatePoints):

    def __init__(self, rightdir: str):
        self.rightdir = rightdir
        
    @property
    def rightdir(self) -> str:
        return self.__rightdir

    @rightdir.setter
    def rightdir(self, rightdir: str):
        self.__rightdir = rightdir

class dSL_MiddleRotatePoint(RotatePoints):

    def __init__(self, middledir: str):
        self.middledir = middledir
        
    @property
    def middledir(self) -> str:
        return self.__middledir

    @middledir.setter
    def middledir(self, middledir: str):
        self.__middledir = middledir

class dSL_LeftRotatePoint(RotatePoints):

    def __init__(self, leftdir: str):
        self.leftdir = leftdir
        
    @property
    def leftdir(self) -> str:
        return self.__leftdir

    @leftdir.setter
    def leftdir(self, leftdir: str):
        self.__leftdir = leftdir

class RotateMovementAction:

    pass
class dSL_RotatePoints(RotateMovementAction):

    def __init__(self, degrees: int):
        self.degrees = degrees
        
    @property
    def degrees(self) -> int:
        return self.__degrees

    @degrees.setter
    def degrees(self, degrees: int):
        self.__degrees = degrees

class dSL_MovementAction:

    def __init__(self, actionenum: str, dSL_MovementAction: "dSL_LeftMovementAction" = None, dSL_MovementAction15: "dSL_RightMovementAction" = None):
        self.actionenum = actionenum
        self.dSL_MovementAction = dSL_MovementAction
        self.dSL_MovementAction15 = dSL_MovementAction15
        
    @property
    def actionenum(self) -> str:
        return self.__actionenum

    @actionenum.setter
    def actionenum(self, actionenum: str):
        self.__actionenum = actionenum

    @property
    def dSL_MovementAction15(self):
        return self.__dSL_MovementAction15

    @dSL_MovementAction15.setter
    def dSL_MovementAction15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_MovementAction__dSL_MovementAction15", None)
        self.__dSL_MovementAction15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_RightMovementAction"):
                opp_val = getattr(old_value, "dSL_RightMovementAction", None)
                if opp_val == self:
                    setattr(old_value, "dSL_RightMovementAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_RightMovementAction"):
                opp_val = getattr(value, "dSL_RightMovementAction", None)
                setattr(value, "dSL_RightMovementAction", self)

    @property
    def dSL_MovementAction(self):
        return self.__dSL_MovementAction

    @dSL_MovementAction.setter
    def dSL_MovementAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_MovementAction__dSL_MovementAction", None)
        self.__dSL_MovementAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_LeftMovementAction"):
                opp_val = getattr(old_value, "dSL_LeftMovementAction", None)
                if opp_val == self:
                    setattr(old_value, "dSL_LeftMovementAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_LeftMovementAction"):
                opp_val = getattr(value, "dSL_LeftMovementAction", None)
                setattr(value, "dSL_LeftMovementAction", self)

class Actions:

    pass
class dSL_LeftMovementAction(Actions):

    pass
class dSL_MeasurementAction(Actions):

    def __init__(self, measure: str):
        self.measure = measure
        
    @property
    def measure(self) -> str:
        return self.__measure

    @measure.setter
    def measure(self, measure: str):
        self.__measure = measure

class dSL_RotateMovementAction(Actions):

    pass
class dSL_RightMovementAction(Actions):

    pass
class dSL_MoveAction(Actions):

    def __init__(self, dir: str):
        self.dir = dir
        
    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

class dSL_Actions:

    pass
class dSL_Expression:

    pass
class EndCondition:

    pass
class dSL_EndAfter(EndCondition):

    def __init__(self, time: int):
        self.time = time
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

class dSL_EndWhen:

    def __init__(self, name: str, times: int, dSL_EndWhen: "dSL_EndCondition" = None):
        self.name = name
        self.times = times
        self.dSL_EndWhen = dSL_EndWhen
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def times(self) -> int:
        return self.__times

    @times.setter
    def times(self, times: int):
        self.__times = times

    @property
    def dSL_EndWhen(self):
        return self.__dSL_EndWhen

    @dSL_EndWhen.setter
    def dSL_EndWhen(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_EndWhen__dSL_EndWhen", None)
        self.__dSL_EndWhen = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_EndCondition8"):
                opp_val = getattr(old_value, "dSL_EndCondition8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_EndCondition8"):
                opp_val = getattr(value, "dSL_EndCondition8", None)
                if opp_val is None:
                    setattr(value, "dSL_EndCondition8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dSL_EndCondition:

    pass
class dSL_BehaviorName:

    def __init__(self, name: str, dSL_BehaviorName: "dSL_Mission" = None):
        self.name = name
        self.dSL_BehaviorName = dSL_BehaviorName
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dSL_BehaviorName(self):
        return self.__dSL_BehaviorName

    @dSL_BehaviorName.setter
    def dSL_BehaviorName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_BehaviorName__dSL_BehaviorName", None)
        self.__dSL_BehaviorName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_Mission4"):
                opp_val = getattr(old_value, "dSL_Mission4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_Mission4"):
                opp_val = getattr(value, "dSL_Mission4", None)
                if opp_val is None:
                    setattr(value, "dSL_Mission4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dSL_Behavior:

    def __init__(self, name: str, dSL_Behavior: "dSL_MarsRoverExpedition" = None, dSL_Behavior10: "dSL_Expression" = None, dSL_Behavior12: set["dSL_Actions"] = None):
        self.name = name
        self.dSL_Behavior = dSL_Behavior
        self.dSL_Behavior10 = dSL_Behavior10
        self.dSL_Behavior12 = dSL_Behavior12 if dSL_Behavior12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dSL_Behavior(self):
        return self.__dSL_Behavior

    @dSL_Behavior.setter
    def dSL_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Behavior__dSL_Behavior", None)
        self.__dSL_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_MarsRoverExpedition2"):
                opp_val = getattr(old_value, "dSL_MarsRoverExpedition2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_MarsRoverExpedition2"):
                opp_val = getattr(value, "dSL_MarsRoverExpedition2", None)
                if opp_val is None:
                    setattr(value, "dSL_MarsRoverExpedition2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dSL_Behavior10(self):
        return self.__dSL_Behavior10

    @dSL_Behavior10.setter
    def dSL_Behavior10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Behavior__dSL_Behavior10", None)
        self.__dSL_Behavior10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_Expression"):
                opp_val = getattr(old_value, "dSL_Expression", None)
                if opp_val == self:
                    setattr(old_value, "dSL_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_Expression"):
                opp_val = getattr(value, "dSL_Expression", None)
                setattr(value, "dSL_Expression", self)

    @property
    def dSL_Behavior12(self):
        return self.__dSL_Behavior12

    @dSL_Behavior12.setter
    def dSL_Behavior12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Behavior__dSL_Behavior12", None)
        self.__dSL_Behavior12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dSL_Actions"):
                    opp_val = getattr(item, "dSL_Actions", None)
                    
                    if opp_val == self:
                        setattr(item, "dSL_Actions", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dSL_Actions"):
                    opp_val = getattr(item, "dSL_Actions", None)
                    
                    setattr(item, "dSL_Actions", self)
                    

class dSL_Mission:

    def __init__(self, name: str, dSL_Mission: "dSL_MarsRoverExpedition" = None, dSL_Mission4: set["dSL_BehaviorName"] = None, dSL_Mission6: "dSL_EndCondition" = None):
        self.name = name
        self.dSL_Mission = dSL_Mission
        self.dSL_Mission4 = dSL_Mission4 if dSL_Mission4 is not None else set()
        self.dSL_Mission6 = dSL_Mission6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dSL_Mission4(self):
        return self.__dSL_Mission4

    @dSL_Mission4.setter
    def dSL_Mission4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Mission__dSL_Mission4", None)
        self.__dSL_Mission4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dSL_BehaviorName"):
                    opp_val = getattr(item, "dSL_BehaviorName", None)
                    
                    if opp_val == self:
                        setattr(item, "dSL_BehaviorName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dSL_BehaviorName"):
                    opp_val = getattr(item, "dSL_BehaviorName", None)
                    
                    setattr(item, "dSL_BehaviorName", self)
                    

    @property
    def dSL_Mission(self):
        return self.__dSL_Mission

    @dSL_Mission.setter
    def dSL_Mission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Mission__dSL_Mission", None)
        self.__dSL_Mission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_MarsRoverExpedition"):
                opp_val = getattr(old_value, "dSL_MarsRoverExpedition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_MarsRoverExpedition"):
                opp_val = getattr(value, "dSL_MarsRoverExpedition", None)
                if opp_val is None:
                    setattr(value, "dSL_MarsRoverExpedition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dSL_Mission6(self):
        return self.__dSL_Mission6

    @dSL_Mission6.setter
    def dSL_Mission6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Mission__dSL_Mission6", None)
        self.__dSL_Mission6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_EndCondition"):
                opp_val = getattr(old_value, "dSL_EndCondition", None)
                if opp_val == self:
                    setattr(old_value, "dSL_EndCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_EndCondition"):
                opp_val = getattr(value, "dSL_EndCondition", None)
                setattr(value, "dSL_EndCondition", self)

class dSL_MarsRoverExpedition:

    pass