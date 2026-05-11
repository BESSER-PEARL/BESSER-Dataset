from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SensorPort(Enum):
    S1 = "S1"
    S2 = "S2"
    S3 = "S3"
    S4 = "S4"
class MotorType(Enum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
class ComparisonOperator(Enum):
    LESS = "LESS"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    GREATER = "GREATER"
    EQUAL = "EQUAL"
    UNEQUAL = "UNEQUAL"
class SensorType(Enum):
    COLOR = "COLOR"
class SensorMode(Enum):
    RED = "RED"
    AMBIENT = "AMBIENT"
    COLOR_ID = "COLOR_ID"
class ExprOperation(Enum):
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
class MotorPort(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
class Direction(Enum):
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


############################################
# Definition of Classes
############################################

class robo_condition_Condition(ABC):

    def __init__(self):
        
        pass
    def evaluate(self) :
        # TODO: Implement evaluate method
        pass

class robo_expression_Expr(ABC):

    def __init__(self):
        
        pass
    def evaluate(self) :
        # TODO: Implement evaluate method
        pass

class Condition:

    pass
class robo_condition_Comparison(Condition):

    def __init__(self, operator: str, robo_condition_Comparison: "Expr" = None, robo_condition_Comparison35: "Expr" = None, Condition21: "robo_command_Branch" = None, Condition16: "robo_command_Loop" = None, Condition: "robo_command_Drive" = None):
        self.operator = operator
        self.robo_condition_Comparison = robo_condition_Comparison
        self.robo_condition_Comparison35 = robo_condition_Comparison35
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def robo_condition_Comparison35(self):
        return self.__robo_condition_Comparison35

    @robo_condition_Comparison35.setter
    def robo_condition_Comparison35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robo_condition_Comparison__robo_condition_Comparison35", None)
        self.__robo_condition_Comparison35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expr36"):
                opp_val = getattr(old_value, "Expr36", None)
                if opp_val == self:
                    setattr(old_value, "Expr36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expr36"):
                opp_val = getattr(value, "Expr36", None)
                setattr(value, "Expr36", self)

    @property
    def robo_condition_Comparison(self):
        return self.__robo_condition_Comparison

    @robo_condition_Comparison.setter
    def robo_condition_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robo_condition_Comparison__robo_condition_Comparison", None)
        self.__robo_condition_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expr33"):
                opp_val = getattr(old_value, "Expr33", None)
                if opp_val == self:
                    setattr(old_value, "Expr33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expr33"):
                opp_val = getattr(value, "Expr33", None)
                setattr(value, "Expr33", self)

class Expr:

    pass
class robo_expression_Literal(Expr):

    def __init__(self, value: float, Expr28: "robo_expression_Operation" = None, Expr36: "robo_condition_Comparison" = None, Expr: "robo_command_Drive" = None, Expr33: "robo_condition_Comparison" = None, Expr31: "robo_expression_Operation" = None, Expr26: "robo_command_Assignment" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class robo_expression_Operation(Expr):

    def __init__(self, operator: str, robo_expression_Operation: "Expr" = None, robo_expression_Operation30: "Expr" = None, Expr28: "robo_expression_Operation" = None, Expr36: "robo_condition_Comparison" = None, Expr: "robo_command_Drive" = None, Expr33: "robo_condition_Comparison" = None, Expr31: "robo_expression_Operation" = None, Expr26: "robo_command_Assignment" = None):
        self.operator = operator
        self.robo_expression_Operation = robo_expression_Operation
        self.robo_expression_Operation30 = robo_expression_Operation30
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def robo_expression_Operation30(self):
        return self.__robo_expression_Operation30

    @robo_expression_Operation30.setter
    def robo_expression_Operation30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robo_expression_Operation__robo_expression_Operation30", None)
        self.__robo_expression_Operation30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expr31"):
                opp_val = getattr(old_value, "Expr31", None)
                if opp_val == self:
                    setattr(old_value, "Expr31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expr31"):
                opp_val = getattr(value, "Expr31", None)
                setattr(value, "Expr31", self)

    @property
    def robo_expression_Operation(self):
        return self.__robo_expression_Operation

    @robo_expression_Operation.setter
    def robo_expression_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robo_expression_Operation__robo_expression_Operation", None)
        self.__robo_expression_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expr28"):
                opp_val = getattr(old_value, "Expr28", None)
                if opp_val == self:
                    setattr(old_value, "Expr28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expr28"):
                opp_val = getattr(value, "Expr28", None)
                setattr(value, "Expr28", self)

class robo_expression_Variable(Expr):

    def __init__(self, name: str, Expr28: "robo_expression_Operation" = None, Expr36: "robo_condition_Comparison" = None, Expr: "robo_command_Drive" = None, Expr33: "robo_condition_Comparison" = None, Expr31: "robo_expression_Operation" = None, Expr26: "robo_command_Assignment" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Command:

    pass
class robo_command_Assignment(Command):

    def __init__(self, variable: str, robo_command_Assignment: "Expr" = None, Command24: "robo_command_Branch" = None, Command: "robo_Program" = None, Command19: "robo_command_Loop" = None):
        self.variable = variable
        self.robo_command_Assignment = robo_command_Assignment
        
        pass
    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable


    @property
    def robo_command_Assignment(self):
        return self.__robo_command_Assignment

    @robo_command_Assignment.setter
    def robo_command_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robo_command_Assignment__robo_command_Assignment", None)
        self.__robo_command_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expr26"):
                opp_val = getattr(old_value, "Expr26", None)
                if opp_val == self:
                    setattr(old_value, "Expr26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expr26"):
                opp_val = getattr(value, "Expr26", None)
                setattr(value, "Expr26", self)

class robo_command_Branch(Command):

    pass
class robo_command_Loop(Command):

    pass
class robo_command_Drive(Command):

    def __init__(self, direction: str, robo_command_Drive: "Expr" = None, robo_command_Drive14: "Condition" = None, Command24: "robo_command_Branch" = None, Command: "robo_Program" = None, Command19: "robo_command_Loop" = None):
        self.direction = direction
        self.robo_command_Drive = robo_command_Drive
        self.robo_command_Drive14 = robo_command_Drive14
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def robo_command_Drive(self):
        return self.__robo_command_Drive

    @robo_command_Drive.setter
    def robo_command_Drive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robo_command_Drive__robo_command_Drive", None)
        self.__robo_command_Drive = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expr"):
                opp_val = getattr(old_value, "Expr", None)
                if opp_val == self:
                    setattr(old_value, "Expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expr"):
                opp_val = getattr(value, "Expr", None)
                setattr(value, "Expr", self)

    @property
    def robo_command_Drive14(self):
        return self.__robo_command_Drive14

    @robo_command_Drive14.setter
    def robo_command_Drive14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robo_command_Drive__robo_command_Drive14", None)
        self.__robo_command_Drive14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Condition"):
                opp_val = getattr(old_value, "Condition", None)
                if opp_val == self:
                    setattr(old_value, "Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Condition"):
                opp_val = getattr(value, "Condition", None)
                setattr(value, "Condition", self)

class robo_command_Command(ABC):

    pass
class robo_Motor:

    def __init__(self, port: str, type: str, speed: float, reversed: bool, robo_Motor: "robo_Setup" = None, robo_Motor7: "robo_Setup" = None):
        self.port = port
        self.type = type
        self.speed = speed
        self.reversed = reversed
        self.robo_Motor = robo_Motor
        self.robo_Motor7 = robo_Motor7
        
        pass
    @property
    def reversed(self):
        return self.__reversed

    @reversed.setter
    def reversed(self, reversed: bool):
        self.__reversed = reversed


    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: float):
        self.__speed = speed


    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def robo_Motor(self):
        return self.__robo_Motor

    @robo_Motor.setter
    def robo_Motor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robo_Motor__robo_Motor", None)
        self.__robo_Motor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robo_Setup4"):
                opp_val = getattr(old_value, "robo_Setup4", None)
                if opp_val == self:
                    setattr(old_value, "robo_Setup4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robo_Setup4"):
                opp_val = getattr(value, "robo_Setup4", None)
                setattr(value, "robo_Setup4", self)

    @property
    def robo_Motor7(self):
        return self.__robo_Motor7

    @robo_Motor7.setter
    def robo_Motor7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robo_Motor__robo_Motor7", None)
        self.__robo_Motor7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robo_Setup6"):
                opp_val = getattr(old_value, "robo_Setup6", None)
                if opp_val == self:
                    setattr(old_value, "robo_Setup6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robo_Setup6"):
                opp_val = getattr(value, "robo_Setup6", None)
                setattr(value, "robo_Setup6", self)

class robo_Setup:

    pass
class robo_Program:

    def __init__(self, name: str, robo_Program11: set["Command"] = None, robo_Program: "robo_Robot" = None):
        self.name = name
        self.robo_Program11 = robo_Program11 if robo_Program11 is not None else set()
        self.robo_Program = robo_Program
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def robo_Program(self):
        return self.__robo_Program

    @robo_Program.setter
    def robo_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robo_Program__robo_Program", None)
        self.__robo_Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robo_Robot"):
                opp_val = getattr(old_value, "robo_Robot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robo_Robot"):
                opp_val = getattr(value, "robo_Robot", None)
                if opp_val is None:
                    setattr(value, "robo_Robot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robo_Program11(self):
        return self.__robo_Program11

    @robo_Program11.setter
    def robo_Program11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robo_Program__robo_Program11", None)
        self.__robo_Program11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Command"):
                    opp_val = getattr(item, "Command", None)
                    
                    if opp_val == self:
                        setattr(item, "Command", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Command"):
                    opp_val = getattr(item, "Command", None)
                    
                    setattr(item, "Command", self)
                    

class robo_Robot:

    pass
class robo_Sensor:

    def __init__(self, port: str, type: str, mode: str, name: str, robo_Sensor: "robo_Setup" = None):
        self.port = port
        self.type = type
        self.mode = mode
        self.name = name
        self.robo_Sensor = robo_Sensor
        
        pass
    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port


    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def robo_Sensor(self):
        return self.__robo_Sensor

    @robo_Sensor.setter
    def robo_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robo_Sensor__robo_Sensor", None)
        self.__robo_Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robo_Setup9"):
                opp_val = getattr(old_value, "robo_Setup9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robo_Setup9"):
                opp_val = getattr(value, "robo_Setup9", None)
                if opp_val is None:
                    setattr(value, "robo_Setup9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
