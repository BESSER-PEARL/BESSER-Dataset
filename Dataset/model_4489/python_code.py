from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActionEnum(Enum):
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
    STOP = "STOP"
class ColorEnum(Enum):
    NONE = "NONE"
    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"
    WHITE = "WHITE"
    BROWN = "BROWN"
class TouchEnum(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class LREnum(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class FBEnum(Enum):
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
class EdgeEnum(Enum):
    FRONTLEFT = "FRONTLEFT"
    FRONTRIGHT = "FRONTRIGHT"
    BACK = "BACK"


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

class dSL_ORexpression(Expression):

    pass
class dSL_DistanceLiteral(Expression):

    def __init__(self, distance: int):
        self.distance = distance
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

class dSL_ColorLiteral(Expression):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

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

class dSL_ExpressionBracket(Expression):

    pass
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
class dSL_MovementAction:

    def __init__(self, actionenum: str, dSL_MovementAction7: "dSL_RightMovementAction" = None, dSL_MovementAction: "dSL_LeftMovementAction" = None):
        self.actionenum = actionenum
        self.dSL_MovementAction7 = dSL_MovementAction7
        self.dSL_MovementAction = dSL_MovementAction
        
    @property
    def actionenum(self) -> str:
        return self.__actionenum

    @actionenum.setter
    def actionenum(self, actionenum: str):
        self.__actionenum = actionenum

    @property
    def dSL_MovementAction7(self):
        return self.__dSL_MovementAction7

    @dSL_MovementAction7.setter
    def dSL_MovementAction7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_MovementAction__dSL_MovementAction7", None)
        self.__dSL_MovementAction7 = value
        
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
class dSL_Actions:

    pass
class dSL_Expression:

    pass
class dSL_Behaviors:

    def __init__(self, name: str, dSL_Behaviors: "dSL_RobotBehavior" = None, dSL_Behaviors2: "dSL_Expression" = None, dSL_Behaviors4: set["dSL_Actions"] = None):
        self.name = name
        self.dSL_Behaviors = dSL_Behaviors
        self.dSL_Behaviors2 = dSL_Behaviors2
        self.dSL_Behaviors4 = dSL_Behaviors4 if dSL_Behaviors4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dSL_Behaviors(self):
        return self.__dSL_Behaviors

    @dSL_Behaviors.setter
    def dSL_Behaviors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Behaviors__dSL_Behaviors", None)
        self.__dSL_Behaviors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_RobotBehavior"):
                opp_val = getattr(old_value, "dSL_RobotBehavior", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_RobotBehavior"):
                opp_val = getattr(value, "dSL_RobotBehavior", None)
                if opp_val is None:
                    setattr(value, "dSL_RobotBehavior", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dSL_Behaviors2(self):
        return self.__dSL_Behaviors2

    @dSL_Behaviors2.setter
    def dSL_Behaviors2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Behaviors__dSL_Behaviors2", None)
        self.__dSL_Behaviors2 = value
        
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
    def dSL_Behaviors4(self):
        return self.__dSL_Behaviors4

    @dSL_Behaviors4.setter
    def dSL_Behaviors4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Behaviors__dSL_Behaviors4", None)
        self.__dSL_Behaviors4 = value if value is not None else set()
        
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
                    

class dSL_RobotBehavior:

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

class dSL_RotateMovementAction(Actions):

    pass
class dSL_RightMovementAction(Actions):

    pass