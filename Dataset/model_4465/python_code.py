from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class rover_PositionQuantity:

    pass
class rover_SingleQuantity:

    pass
class rover_SetLightColor:

    def __init__(self, color: str, rover_SetLightColor: "rover_Command" = None):
        self.color = color
        self.rover_SetLightColor = rover_SetLightColor
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def rover_SetLightColor(self):
        return self.__rover_SetLightColor

    @rover_SetLightColor.setter
    def rover_SetLightColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_SetLightColor__rover_SetLightColor", None)
        self.__rover_SetLightColor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Command20"):
                opp_val = getattr(old_value, "rover_Command20", None)
                if opp_val == self:
                    setattr(old_value, "rover_Command20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Command20"):
                opp_val = getattr(value, "rover_Command20", None)
                setattr(value, "rover_Command20", self)

class rover_Wait:

    def __init__(self, time: int, rover_Wait: "rover_Command" = None):
        self.time = time
        self.rover_Wait = rover_Wait
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def rover_Wait(self):
        return self.__rover_Wait

    @rover_Wait.setter
    def rover_Wait(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Wait__rover_Wait", None)
        self.__rover_Wait = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Command18"):
                opp_val = getattr(old_value, "rover_Command18", None)
                if opp_val == self:
                    setattr(old_value, "rover_Command18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Command18"):
                opp_val = getattr(value, "rover_Command18", None)
                setattr(value, "rover_Command18", self)

class rover_Move:

    def __init__(self, length: int, velocity: int, rover_Move: "rover_Command" = None):
        self.length = length
        self.velocity = velocity
        self.rover_Move = rover_Move
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def velocity(self) -> int:
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity: int):
        self.__velocity = velocity

    @property
    def rover_Move(self):
        return self.__rover_Move

    @rover_Move.setter
    def rover_Move(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Move__rover_Move", None)
        self.__rover_Move = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Command16"):
                opp_val = getattr(old_value, "rover_Command16", None)
                if opp_val == self:
                    setattr(old_value, "rover_Command16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Command16"):
                opp_val = getattr(value, "rover_Command16", None)
                setattr(value, "rover_Command16", self)

class rover_Rotate:

    def __init__(self, angel: int, rover_Rotate: "rover_Command" = None):
        self.angel = angel
        self.rover_Rotate = rover_Rotate
        
    @property
    def angel(self) -> int:
        return self.__angel

    @angel.setter
    def angel(self, angel: int):
        self.__angel = angel

    @property
    def rover_Rotate(self):
        return self.__rover_Rotate

    @rover_Rotate.setter
    def rover_Rotate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Rotate__rover_Rotate", None)
        self.__rover_Rotate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Command14"):
                opp_val = getattr(old_value, "rover_Command14", None)
                if opp_val == self:
                    setattr(old_value, "rover_Command14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Command14"):
                opp_val = getattr(value, "rover_Command14", None)
                setattr(value, "rover_Command14", self)

class rover_Repeate:

    def __init__(self, count: int, rover_Repeate: "rover_Command" = None):
        self.count = count
        self.rover_Repeate = rover_Repeate
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def rover_Repeate(self):
        return self.__rover_Repeate

    @rover_Repeate.setter
    def rover_Repeate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Repeate__rover_Repeate", None)
        self.__rover_Repeate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Command12"):
                opp_val = getattr(old_value, "rover_Command12", None)
                if opp_val == self:
                    setattr(old_value, "rover_Command12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Command12"):
                opp_val = getattr(value, "rover_Command12", None)
                setattr(value, "rover_Command12", self)

class rover_Command:

    pass
class rover_Block:

    def __init__(self, name: str, rover_Block: "rover_Program" = None, rover_Block7: set["rover_Command"] = None, rover_Block9: set["rover_Tansition"] = None):
        self.name = name
        self.rover_Block = rover_Block
        self.rover_Block7 = rover_Block7 if rover_Block7 is not None else set()
        self.rover_Block9 = rover_Block9 if rover_Block9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rover_Block7(self):
        return self.__rover_Block7

    @rover_Block7.setter
    def rover_Block7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Block__rover_Block7", None)
        self.__rover_Block7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rover_Command"):
                    opp_val = getattr(item, "rover_Command", None)
                    
                    if opp_val == self:
                        setattr(item, "rover_Command", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rover_Command"):
                    opp_val = getattr(item, "rover_Command", None)
                    
                    setattr(item, "rover_Command", self)
                    

    @property
    def rover_Block9(self):
        return self.__rover_Block9

    @rover_Block9.setter
    def rover_Block9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Block__rover_Block9", None)
        self.__rover_Block9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rover_Tansition10"):
                    opp_val = getattr(item, "rover_Tansition10", None)
                    
                    if opp_val == self:
                        setattr(item, "rover_Tansition10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rover_Tansition10"):
                    opp_val = getattr(item, "rover_Tansition10", None)
                    
                    setattr(item, "rover_Tansition10", self)
                    

    @property
    def rover_Block(self):
        return self.__rover_Block

    @rover_Block.setter
    def rover_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Block__rover_Block", None)
        self.__rover_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Program5"):
                opp_val = getattr(old_value, "rover_Program5", None)
                if opp_val == self:
                    setattr(old_value, "rover_Program5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Program5"):
                opp_val = getattr(value, "rover_Program5", None)
                setattr(value, "rover_Program5", self)

class Actuator:

    pass
class rover_Light(Actuator):

    pass
class rover_Motor(Actuator):

    pass
class Sensor:

    pass
class rover_directionFacing(Sensor):

    def __init__(self, currentlyFacing: float):
        self.currentlyFacing = currentlyFacing
        
    @property
    def currentlyFacing(self) -> float:
        return self.__currentlyFacing

    @currentlyFacing.setter
    def currentlyFacing(self, currentlyFacing: float):
        self.__currentlyFacing = currentlyFacing

class rover_Compass(Sensor):

    pass
class rover_DistanceSensor(Sensor):

    def __init__(self, remainingDistance: float):
        self.remainingDistance = remainingDistance
        
    @property
    def remainingDistance(self) -> float:
        return self.__remainingDistance

    @remainingDistance.setter
    def remainingDistance(self, remainingDistance: float):
        self.__remainingDistance = remainingDistance

class rover_GPS(Sensor):

    def __init__(self, currentPosition: float):
        self.currentPosition = currentPosition
        
    @property
    def currentPosition(self) -> float:
        return self.__currentPosition

    @currentPosition.setter
    def currentPosition(self, currentPosition: float):
        self.__currentPosition = currentPosition

class rover_Tansition:

    def __init__(self, comparedQuantity: str, operationUsed: str, rover_Tansition: "rover_Sensor" = None, Tansition: "rover_Command" = None, rover_Tansition10: "rover_Block" = None, Tansition23: "rover_Command" = None, outgoingTransition: "rover_Command" = None, incomingTransition: "rover_Command" = None):
        self.comparedQuantity = comparedQuantity
        self.operationUsed = operationUsed
        self.rover_Tansition = rover_Tansition
        self.Tansition = Tansition
        self.rover_Tansition10 = rover_Tansition10
        self.Tansition23 = Tansition23
        self.outgoingTransition = outgoingTransition
        self.incomingTransition = incomingTransition
        
    @property
    def operationUsed(self) -> str:
        return self.__operationUsed

    @operationUsed.setter
    def operationUsed(self, operationUsed: str):
        self.__operationUsed = operationUsed

    @property
    def comparedQuantity(self) -> str:
        return self.__comparedQuantity

    @comparedQuantity.setter
    def comparedQuantity(self, comparedQuantity: str):
        self.__comparedQuantity = comparedQuantity

    @property
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Tansition__outgoingTransition", None)
        self.__outgoingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Command"):
                opp_val = getattr(old_value, "Command", None)
                if opp_val == self:
                    setattr(old_value, "Command", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Command"):
                opp_val = getattr(value, "Command", None)
                setattr(value, "Command", self)

    @property
    def rover_Tansition10(self):
        return self.__rover_Tansition10

    @rover_Tansition10.setter
    def rover_Tansition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Tansition__rover_Tansition10", None)
        self.__rover_Tansition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Block9"):
                opp_val = getattr(old_value, "rover_Block9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Block9"):
                opp_val = getattr(value, "rover_Block9", None)
                if opp_val is None:
                    setattr(value, "rover_Block9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rover_Tansition(self):
        return self.__rover_Tansition

    @rover_Tansition.setter
    def rover_Tansition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Tansition__rover_Tansition", None)
        self.__rover_Tansition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Sensor"):
                opp_val = getattr(old_value, "rover_Sensor", None)
                if opp_val == self:
                    setattr(old_value, "rover_Sensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Sensor"):
                opp_val = getattr(value, "rover_Sensor", None)
                setattr(value, "rover_Sensor", self)

    @property
    def Tansition23(self):
        return self.__Tansition23

    @Tansition23.setter
    def Tansition23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Tansition__Tansition23", None)
        self.__Tansition23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetCommand"):
                opp_val = getattr(old_value, "targetCommand", None)
                if opp_val == self:
                    setattr(old_value, "targetCommand", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetCommand"):
                opp_val = getattr(value, "targetCommand", None)
                setattr(value, "targetCommand", self)

    @property
    def incomingTransition(self):
        return self.__incomingTransition

    @incomingTransition.setter
    def incomingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Tansition__incomingTransition", None)
        self.__incomingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Command26"):
                opp_val = getattr(old_value, "Command26", None)
                if opp_val == self:
                    setattr(old_value, "Command26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Command26"):
                opp_val = getattr(value, "Command26", None)
                setattr(value, "Command26", self)

    @property
    def Tansition(self):
        return self.__Tansition

    @Tansition.setter
    def Tansition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Tansition__Tansition", None)
        self.__Tansition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceCommand"):
                opp_val = getattr(old_value, "sourceCommand", None)
                if opp_val == self:
                    setattr(old_value, "sourceCommand", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceCommand"):
                opp_val = getattr(value, "sourceCommand", None)
                setattr(value, "sourceCommand", self)

class Component:

    pass
class rover_Actuator(Component):

    pass
class rover_Sensor(Component):

    pass
class rover_Program:

    def __init__(self, name: str, rover_Program: "rover_Rover" = None, rover_Program5: "rover_Block" = None):
        self.name = name
        self.rover_Program = rover_Program
        self.rover_Program5 = rover_Program5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rover_Program(self):
        return self.__rover_Program

    @rover_Program.setter
    def rover_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Program__rover_Program", None)
        self.__rover_Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Rover2"):
                opp_val = getattr(old_value, "rover_Rover2", None)
                if opp_val == self:
                    setattr(old_value, "rover_Rover2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Rover2"):
                opp_val = getattr(value, "rover_Rover2", None)
                setattr(value, "rover_Rover2", self)

    @property
    def rover_Program5(self):
        return self.__rover_Program5

    @rover_Program5.setter
    def rover_Program5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Program__rover_Program5", None)
        self.__rover_Program5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Block"):
                opp_val = getattr(old_value, "rover_Block", None)
                if opp_val == self:
                    setattr(old_value, "rover_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Block"):
                opp_val = getattr(value, "rover_Block", None)
                setattr(value, "rover_Block", self)

class rover_Component(ABC):

    def __init__(self, name: str, rover_Component: "rover_Rover" = None):
        self.name = name
        self.rover_Component = rover_Component
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rover_Component(self):
        return self.__rover_Component

    @rover_Component.setter
    def rover_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Component__rover_Component", None)
        self.__rover_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Rover"):
                opp_val = getattr(old_value, "rover_Rover", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Rover"):
                opp_val = getattr(value, "rover_Rover", None)
                if opp_val is None:
                    setattr(value, "rover_Rover", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rover_Rover:

    pass