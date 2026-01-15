from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class robot_Statement(ABC):

    pass
class ConditionalStatement:

    pass
class robot_UntilStatement(ConditionalStatement):

    pass
class robot_WhileStatement(ConditionalStatement):

    pass
class robot_IfStatement(ConditionalStatement):

    pass
class ControlStatement:

    pass
class robot_RightStatement(ControlStatement):

    pass
class robot_ForwardStatement(ControlStatement):

    pass
class Statement:

    pass
class robot_ExecuteStatement(Statement):

    pass
class robot_PrintStatement(Statement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class robot_ControlStatement(Statement):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class robot_ConditionalStatement(Statement):

    pass
class robot_Condition:

    pass
class robot_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class robot_Connection:

    def __init__(self, ip: str, port: int, robot_Connection: "robot_Robot" = None):
        self.ip = ip
        self.port = port
        self.robot_Connection = robot_Connection
        
    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def ip(self) -> str:
        return self.__ip

    @ip.setter
    def ip(self, ip: str):
        self.__ip = ip

    @property
    def robot_Connection(self):
        return self.__robot_Connection

    @robot_Connection.setter
    def robot_Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robot_Connection__robot_Connection", None)
        self.__robot_Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robot_Robot7"):
                opp_val = getattr(old_value, "robot_Robot7", None)
                if opp_val == self:
                    setattr(old_value, "robot_Robot7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robot_Robot7"):
                opp_val = getattr(value, "robot_Robot7", None)
                setattr(value, "robot_Robot7", self)

class robot_StatementBlock:

    pass
class NamedElement:

    pass
class robot_Scenario(NamedElement):

    pass
class robot_Robot(NamedElement):

    pass
class Condition:

    pass
class robot_TrueCondition(Condition):

    pass
class robot_ObjectAheadCondition(Condition):

    pass