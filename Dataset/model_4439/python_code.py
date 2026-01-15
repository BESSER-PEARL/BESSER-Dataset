from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CompareOp(Enum):
    EQ = "EQ"
    NEQ = "NEQ"
    GEQ = "GEQ"
    GT = "GT"
    LEQ = "LEQ"
    LT = "LT"
class Color(Enum):
    BLACK = "BLACK"
    BLUE = "BLUE"
    BROWN = "BROWN"
    CYAN = "CYAN"
    DARK_GRAY = "DARK_GRAY"
    GRAY = "GRAY"
    GREEN = "GREEN"
    LIGHT_GRAY = "LIGHT_GRAY"
    MAGENTA = "MAGENTA"
    ORANGE = "ORANGE"
    PINK = "PINK"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"
class Sensor(Enum):
    COLORIDSENSOR = "COLORIDSENSOR"
    LEFTLIGHTSENSOR = "LEFTLIGHTSENSOR"
    RIGHTLIGHTSENSOR = "RIGHTLIGHTSENSOR"
    FRONTULTRASONICSENSOR = "FRONTULTRASONICSENSOR"
    REARULTRASONICSENSOR = "REARULTRASONICSENSOR"
    TOUCHSENSORL = "TOUCHSENSORL"
    TOUCHSENSORR = "TOUCHSENSORR"
    ANGLESENSOR = "ANGLESENSOR"
class BBinaryOp(Enum):
    AND = "AND"
    OR = "OR"
class Sound(Enum):
    BEEP = "BEEP"
    BUZZ = "BUZZ"
class EMotor(Enum):
    LEFTMOTOR = "LEFTMOTOR"
    RIGHTMOTOR = "RIGHTMOTOR"


############################################
# Definition of Classes
############################################

class ValueExpression:

    pass
class roverDSL_BVBracket(ValueExpression):

    pass
class roverDSL_BSensorLiteral(ValueExpression):

    def __init__(self, sensor: str):
        self.sensor = sensor
        
    @property
    def sensor(self) -> str:
        return self.__sensor

    @sensor.setter
    def sensor(self, sensor: str):
        self.__sensor = sensor

class roverDSL_ExpressionBinOp(ValueExpression):

    def __init__(self, bop: str, roverDSL_ExpressionBinOp: "roverDSL_ValueExpression" = None, roverDSL_ExpressionBinOp74: "roverDSL_ValueExpression" = None):
        self.bop = bop
        self.roverDSL_ExpressionBinOp = roverDSL_ExpressionBinOp
        self.roverDSL_ExpressionBinOp74 = roverDSL_ExpressionBinOp74
        
    @property
    def bop(self) -> str:
        return self.__bop

    @bop.setter
    def bop(self, bop: str):
        self.__bop = bop

    @property
    def roverDSL_ExpressionBinOp74(self):
        return self.__roverDSL_ExpressionBinOp74

    @roverDSL_ExpressionBinOp74.setter
    def roverDSL_ExpressionBinOp74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_ExpressionBinOp__roverDSL_ExpressionBinOp74", None)
        self.__roverDSL_ExpressionBinOp74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_ValueExpression75"):
                opp_val = getattr(old_value, "roverDSL_ValueExpression75", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_ValueExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_ValueExpression75"):
                opp_val = getattr(value, "roverDSL_ValueExpression75", None)
                setattr(value, "roverDSL_ValueExpression75", self)

    @property
    def roverDSL_ExpressionBinOp(self):
        return self.__roverDSL_ExpressionBinOp

    @roverDSL_ExpressionBinOp.setter
    def roverDSL_ExpressionBinOp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_ExpressionBinOp__roverDSL_ExpressionBinOp", None)
        self.__roverDSL_ExpressionBinOp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_ValueExpression72"):
                opp_val = getattr(old_value, "roverDSL_ValueExpression72", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_ValueExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_ValueExpression72"):
                opp_val = getattr(value, "roverDSL_ValueExpression72", None)
                setattr(value, "roverDSL_ValueExpression72", self)

class roverDSL_ColorLiteral(ValueExpression):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class roverDSL_ExpressionBinComp(ValueExpression):

    def __init__(self, bcomp: str, roverDSL_ExpressionBinComp: "roverDSL_ValueExpression" = None, roverDSL_ExpressionBinComp79: "roverDSL_ValueExpression" = None):
        self.bcomp = bcomp
        self.roverDSL_ExpressionBinComp = roverDSL_ExpressionBinComp
        self.roverDSL_ExpressionBinComp79 = roverDSL_ExpressionBinComp79
        
    @property
    def bcomp(self) -> str:
        return self.__bcomp

    @bcomp.setter
    def bcomp(self, bcomp: str):
        self.__bcomp = bcomp

    @property
    def roverDSL_ExpressionBinComp79(self):
        return self.__roverDSL_ExpressionBinComp79

    @roverDSL_ExpressionBinComp79.setter
    def roverDSL_ExpressionBinComp79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_ExpressionBinComp__roverDSL_ExpressionBinComp79", None)
        self.__roverDSL_ExpressionBinComp79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_ValueExpression80"):
                opp_val = getattr(old_value, "roverDSL_ValueExpression80", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_ValueExpression80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_ValueExpression80"):
                opp_val = getattr(value, "roverDSL_ValueExpression80", None)
                setattr(value, "roverDSL_ValueExpression80", self)

    @property
    def roverDSL_ExpressionBinComp(self):
        return self.__roverDSL_ExpressionBinComp

    @roverDSL_ExpressionBinComp.setter
    def roverDSL_ExpressionBinComp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_ExpressionBinComp__roverDSL_ExpressionBinComp", None)
        self.__roverDSL_ExpressionBinComp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_ValueExpression77"):
                opp_val = getattr(old_value, "roverDSL_ValueExpression77", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_ValueExpression77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_ValueExpression77"):
                opp_val = getattr(value, "roverDSL_ValueExpression77", None)
                setattr(value, "roverDSL_ValueExpression77", self)

class roverDSL_BBLiteral(ValueExpression):

    def __init__(self, bValue: bool):
        self.bValue = bValue
        
    @property
    def bValue(self) -> bool:
        return self.__bValue

    @bValue.setter
    def bValue(self, bValue: bool):
        self.__bValue = bValue

class roverDSL_BVarLiteral(ValueExpression):

    def __init__(self, var: str):
        self.var = var
        
    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

class roverDSL_BVLiteral(ValueExpression):

    def __init__(self, neg: bool, aValue: int):
        self.neg = neg
        self.aValue = aValue
        
    @property
    def aValue(self) -> int:
        return self.__aValue

    @aValue.setter
    def aValue(self, aValue: int):
        self.__aValue = aValue

    @property
    def neg(self) -> bool:
        return self.__neg

    @neg.setter
    def neg(self, neg: bool):
        self.__neg = neg

class roverDSL_BNotExpr(ValueExpression):

    pass
class roverDSL_Expression:

    pass
class Action:

    pass
class roverDSL_StopAction(Action):

    pass
class roverDSL_ShowAction(Action):

    def __init__(self, string: str, sensor: str):
        self.string = string
        self.sensor = sensor
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def sensor(self) -> str:
        return self.__sensor

    @sensor.setter
    def sensor(self, sensor: str):
        self.__sensor = sensor

class roverDSL_SSpeedAction(Action):

    pass
class roverDSL_SoundAction(Action):

    def __init__(self, sound: str):
        self.sound = sound
        
    @property
    def sound(self) -> str:
        return self.__sound

    @sound.setter
    def sound(self, sound: str):
        self.__sound = sound

class roverDSL_SAccelerationAction(Action):

    pass
class roverDSL_FreeAction(Action):

    pass
class roverDSL_MeasureAction(Action):

    pass
class roverDSL_SubRoutineAction(Action):

    pass
class roverDSL_RotateAction(Action):

    def __init__(self, blocking: bool, roverDSL_RotateAction: "roverDSL_Motor" = None, roverDSL_RotateAction49: "roverDSL_ValueExpression" = None):
        self.blocking = blocking
        self.roverDSL_RotateAction = roverDSL_RotateAction
        self.roverDSL_RotateAction49 = roverDSL_RotateAction49
        
    @property
    def blocking(self) -> bool:
        return self.__blocking

    @blocking.setter
    def blocking(self, blocking: bool):
        self.__blocking = blocking

    @property
    def roverDSL_RotateAction49(self):
        return self.__roverDSL_RotateAction49

    @roverDSL_RotateAction49.setter
    def roverDSL_RotateAction49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_RotateAction__roverDSL_RotateAction49", None)
        self.__roverDSL_RotateAction49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_ValueExpression50"):
                opp_val = getattr(old_value, "roverDSL_ValueExpression50", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_ValueExpression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_ValueExpression50"):
                opp_val = getattr(value, "roverDSL_ValueExpression50", None)
                setattr(value, "roverDSL_ValueExpression50", self)

    @property
    def roverDSL_RotateAction(self):
        return self.__roverDSL_RotateAction

    @roverDSL_RotateAction.setter
    def roverDSL_RotateAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_RotateAction__roverDSL_RotateAction", None)
        self.__roverDSL_RotateAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Motor47"):
                opp_val = getattr(old_value, "roverDSL_Motor47", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_Motor47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Motor47"):
                opp_val = getattr(value, "roverDSL_Motor47", None)
                setattr(value, "roverDSL_Motor47", self)

class roverDSL_ForwardAction(Action):

    pass
class Expression:

    pass
class roverDSL_WHILEExpression(Expression):

    pass
class roverDSL_IFExpression(Expression):

    pass
class roverDSL_AssignExpression(Expression):

    pass
class roverDSL_Action(Expression):

    pass
class roverDSL_ValExpr(Expression):

    pass
class roverDSL_Motor:

    def __init__(self, m: str, roverDSL_Motor: "roverDSL_ForwardAction" = None, roverDSL_Motor47: "roverDSL_RotateAction" = None, roverDSL_Motor59: "roverDSL_SSpeedAction" = None, roverDSL_Motor66: "roverDSL_FreeAction" = None, roverDSL_Motor52: "roverDSL_StopAction" = None, roverDSL_Motor54: "roverDSL_SAccelerationAction" = None):
        self.m = m
        self.roverDSL_Motor = roverDSL_Motor
        self.roverDSL_Motor47 = roverDSL_Motor47
        self.roverDSL_Motor59 = roverDSL_Motor59
        self.roverDSL_Motor66 = roverDSL_Motor66
        self.roverDSL_Motor52 = roverDSL_Motor52
        self.roverDSL_Motor54 = roverDSL_Motor54
        
    @property
    def m(self) -> str:
        return self.__m

    @m.setter
    def m(self, m: str):
        self.__m = m

    @property
    def roverDSL_Motor59(self):
        return self.__roverDSL_Motor59

    @roverDSL_Motor59.setter
    def roverDSL_Motor59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Motor__roverDSL_Motor59", None)
        self.__roverDSL_Motor59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_SSpeedAction"):
                opp_val = getattr(old_value, "roverDSL_SSpeedAction", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_SSpeedAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_SSpeedAction"):
                opp_val = getattr(value, "roverDSL_SSpeedAction", None)
                setattr(value, "roverDSL_SSpeedAction", self)

    @property
    def roverDSL_Motor66(self):
        return self.__roverDSL_Motor66

    @roverDSL_Motor66.setter
    def roverDSL_Motor66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Motor__roverDSL_Motor66", None)
        self.__roverDSL_Motor66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_FreeAction"):
                opp_val = getattr(old_value, "roverDSL_FreeAction", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_FreeAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_FreeAction"):
                opp_val = getattr(value, "roverDSL_FreeAction", None)
                setattr(value, "roverDSL_FreeAction", self)

    @property
    def roverDSL_Motor(self):
        return self.__roverDSL_Motor

    @roverDSL_Motor.setter
    def roverDSL_Motor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Motor__roverDSL_Motor", None)
        self.__roverDSL_Motor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_ForwardAction"):
                opp_val = getattr(old_value, "roverDSL_ForwardAction", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_ForwardAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_ForwardAction"):
                opp_val = getattr(value, "roverDSL_ForwardAction", None)
                setattr(value, "roverDSL_ForwardAction", self)

    @property
    def roverDSL_Motor52(self):
        return self.__roverDSL_Motor52

    @roverDSL_Motor52.setter
    def roverDSL_Motor52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Motor__roverDSL_Motor52", None)
        self.__roverDSL_Motor52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_StopAction"):
                opp_val = getattr(old_value, "roverDSL_StopAction", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_StopAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_StopAction"):
                opp_val = getattr(value, "roverDSL_StopAction", None)
                setattr(value, "roverDSL_StopAction", self)

    @property
    def roverDSL_Motor47(self):
        return self.__roverDSL_Motor47

    @roverDSL_Motor47.setter
    def roverDSL_Motor47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Motor__roverDSL_Motor47", None)
        self.__roverDSL_Motor47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_RotateAction"):
                opp_val = getattr(old_value, "roverDSL_RotateAction", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_RotateAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_RotateAction"):
                opp_val = getattr(value, "roverDSL_RotateAction", None)
                setattr(value, "roverDSL_RotateAction", self)

    @property
    def roverDSL_Motor54(self):
        return self.__roverDSL_Motor54

    @roverDSL_Motor54.setter
    def roverDSL_Motor54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Motor__roverDSL_Motor54", None)
        self.__roverDSL_Motor54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_SAccelerationAction"):
                opp_val = getattr(old_value, "roverDSL_SAccelerationAction", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_SAccelerationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_SAccelerationAction"):
                opp_val = getattr(value, "roverDSL_SAccelerationAction", None)
                setattr(value, "roverDSL_SAccelerationAction", self)

class roverDSL_SubRoutine:

    def __init__(self, name: str, roverDSL_SubRoutine: "roverDSL_Robot" = None, roverDSL_SubRoutine23: set["roverDSL_Expression"] = None, roverDSL_SubRoutine64: "roverDSL_SubRoutineAction" = None):
        self.name = name
        self.roverDSL_SubRoutine = roverDSL_SubRoutine
        self.roverDSL_SubRoutine23 = roverDSL_SubRoutine23 if roverDSL_SubRoutine23 is not None else set()
        self.roverDSL_SubRoutine64 = roverDSL_SubRoutine64
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def roverDSL_SubRoutine(self):
        return self.__roverDSL_SubRoutine

    @roverDSL_SubRoutine.setter
    def roverDSL_SubRoutine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_SubRoutine__roverDSL_SubRoutine", None)
        self.__roverDSL_SubRoutine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Robot10"):
                opp_val = getattr(old_value, "roverDSL_Robot10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Robot10"):
                opp_val = getattr(value, "roverDSL_Robot10", None)
                if opp_val is None:
                    setattr(value, "roverDSL_Robot10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def roverDSL_SubRoutine64(self):
        return self.__roverDSL_SubRoutine64

    @roverDSL_SubRoutine64.setter
    def roverDSL_SubRoutine64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_SubRoutine__roverDSL_SubRoutine64", None)
        self.__roverDSL_SubRoutine64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_SubRoutineAction"):
                opp_val = getattr(old_value, "roverDSL_SubRoutineAction", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_SubRoutineAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_SubRoutineAction"):
                opp_val = getattr(value, "roverDSL_SubRoutineAction", None)
                setattr(value, "roverDSL_SubRoutineAction", self)

    @property
    def roverDSL_SubRoutine23(self):
        return self.__roverDSL_SubRoutine23

    @roverDSL_SubRoutine23.setter
    def roverDSL_SubRoutine23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_SubRoutine__roverDSL_SubRoutine23", None)
        self.__roverDSL_SubRoutine23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "roverDSL_Expression24"):
                    opp_val = getattr(item, "roverDSL_Expression24", None)
                    
                    if opp_val == self:
                        setattr(item, "roverDSL_Expression24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "roverDSL_Expression24"):
                    opp_val = getattr(item, "roverDSL_Expression24", None)
                    
                    setattr(item, "roverDSL_Expression24", self)
                    

class roverDSL_Implementation:

    pass
class roverDSL_ValueExpression:

    pass
class roverDSL_Static:

    def __init__(self, name: str, roverDSL_Static: "roverDSL_Robot" = None, roverDSL_Static12: "roverDSL_ValueExpression" = None):
        self.name = name
        self.roverDSL_Static = roverDSL_Static
        self.roverDSL_Static12 = roverDSL_Static12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def roverDSL_Static12(self):
        return self.__roverDSL_Static12

    @roverDSL_Static12.setter
    def roverDSL_Static12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Static__roverDSL_Static12", None)
        self.__roverDSL_Static12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_ValueExpression13"):
                opp_val = getattr(old_value, "roverDSL_ValueExpression13", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_ValueExpression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_ValueExpression13"):
                opp_val = getattr(value, "roverDSL_ValueExpression13", None)
                setattr(value, "roverDSL_ValueExpression13", self)

    @property
    def roverDSL_Static(self):
        return self.__roverDSL_Static

    @roverDSL_Static.setter
    def roverDSL_Static(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Static__roverDSL_Static", None)
        self.__roverDSL_Static = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Robot4"):
                opp_val = getattr(old_value, "roverDSL_Robot4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Robot4"):
                opp_val = getattr(value, "roverDSL_Robot4", None)
                if opp_val is None:
                    setattr(value, "roverDSL_Robot4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class roverDSL_Global:

    def __init__(self, name: str, roverDSL_Global: "roverDSL_Robot" = None, roverDSL_Global41: "roverDSL_AssignExpression" = None):
        self.name = name
        self.roverDSL_Global = roverDSL_Global
        self.roverDSL_Global41 = roverDSL_Global41
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def roverDSL_Global(self):
        return self.__roverDSL_Global

    @roverDSL_Global.setter
    def roverDSL_Global(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Global__roverDSL_Global", None)
        self.__roverDSL_Global = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Robot2"):
                opp_val = getattr(old_value, "roverDSL_Robot2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Robot2"):
                opp_val = getattr(value, "roverDSL_Robot2", None)
                if opp_val is None:
                    setattr(value, "roverDSL_Robot2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def roverDSL_Global41(self):
        return self.__roverDSL_Global41

    @roverDSL_Global41.setter
    def roverDSL_Global41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Global__roverDSL_Global41", None)
        self.__roverDSL_Global41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_AssignExpression"):
                opp_val = getattr(old_value, "roverDSL_AssignExpression", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_AssignExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_AssignExpression"):
                opp_val = getattr(value, "roverDSL_AssignExpression", None)
                setattr(value, "roverDSL_AssignExpression", self)

class roverDSL_BehaviorName:

    def __init__(self, name: str, roverDSL_BehaviorName: "roverDSL_Robot" = None, roverDSL_BehaviorName16: "roverDSL_Implementation" = None):
        self.name = name
        self.roverDSL_BehaviorName = roverDSL_BehaviorName
        self.roverDSL_BehaviorName16 = roverDSL_BehaviorName16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def roverDSL_BehaviorName(self):
        return self.__roverDSL_BehaviorName

    @roverDSL_BehaviorName.setter
    def roverDSL_BehaviorName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_BehaviorName__roverDSL_BehaviorName", None)
        self.__roverDSL_BehaviorName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Robot"):
                opp_val = getattr(old_value, "roverDSL_Robot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Robot"):
                opp_val = getattr(value, "roverDSL_Robot", None)
                if opp_val is None:
                    setattr(value, "roverDSL_Robot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def roverDSL_BehaviorName16(self):
        return self.__roverDSL_BehaviorName16

    @roverDSL_BehaviorName16.setter
    def roverDSL_BehaviorName16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_BehaviorName__roverDSL_BehaviorName16", None)
        self.__roverDSL_BehaviorName16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Implementation15"):
                opp_val = getattr(old_value, "roverDSL_Implementation15", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_Implementation15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Implementation15"):
                opp_val = getattr(value, "roverDSL_Implementation15", None)
                setattr(value, "roverDSL_Implementation15", self)

class roverDSL_Robot:

    pass