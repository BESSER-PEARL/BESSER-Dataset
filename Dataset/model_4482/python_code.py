from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class farmbot_modeling_BooleanExpression(ABC):

    def __init__(self, value: int, axe: str, pinNumber: int, farmbot_modeling_BooleanExpression: "farmbot_modeling_If" = None):
        self.value = value
        self.axe = axe
        self.pinNumber = pinNumber
        self.farmbot_modeling_BooleanExpression = farmbot_modeling_BooleanExpression
        
    @property
    def pinNumber(self) -> int:
        return self.__pinNumber

    @pinNumber.setter
    def pinNumber(self, pinNumber: int):
        self.__pinNumber = pinNumber

    @property
    def axe(self) -> str:
        return self.__axe

    @axe.setter
    def axe(self, axe: str):
        self.__axe = axe

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def farmbot_modeling_BooleanExpression(self):
        return self.__farmbot_modeling_BooleanExpression

    @farmbot_modeling_BooleanExpression.setter
    def farmbot_modeling_BooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farmbot_modeling_BooleanExpression__farmbot_modeling_BooleanExpression", None)
        self.__farmbot_modeling_BooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "farmbot_modeling_If"):
                opp_val = getattr(old_value, "farmbot_modeling_If", None)
                if opp_val == self:
                    setattr(old_value, "farmbot_modeling_If", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "farmbot_modeling_If"):
                opp_val = getattr(value, "farmbot_modeling_If", None)
                setattr(value, "farmbot_modeling_If", self)

class Instruction:

    pass
class farmbot_modeling_Command(Instruction):

    pass
class farmbot_modeling_SequenceInstruction(Instruction):

    pass
class farmbot_modeling_Sequence(Instruction):

    def __init__(self, name: str, farmbot_modeling_Sequence: set["farmbot_modeling_SequenceInstruction"] = None):
        self.name = name
        self.farmbot_modeling_Sequence = farmbot_modeling_Sequence if farmbot_modeling_Sequence is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def farmbot_modeling_Sequence(self):
        return self.__farmbot_modeling_Sequence

    @farmbot_modeling_Sequence.setter
    def farmbot_modeling_Sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farmbot_modeling_Sequence__farmbot_modeling_Sequence", None)
        self.__farmbot_modeling_Sequence = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "farmbot_modeling_SequenceInstruction"):
                    opp_val = getattr(item, "farmbot_modeling_SequenceInstruction", None)
                    
                    if opp_val == self:
                        setattr(item, "farmbot_modeling_SequenceInstruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "farmbot_modeling_SequenceInstruction"):
                    opp_val = getattr(item, "farmbot_modeling_SequenceInstruction", None)
                    
                    setattr(item, "farmbot_modeling_SequenceInstruction", self)
                    

class BooleanExpression:

    pass
class farmbot_modeling_IsGreaterThan(BooleanExpression):

    pass
class farmbot_modeling_IsNotEqualTo(BooleanExpression):

    pass
class farmbot_modeling_IsLowerThan(BooleanExpression):

    pass
class farmbot_modeling_IsEqualTo(BooleanExpression):

    pass
class Move:

    pass
class farmbot_modeling_MoveAbsolute(Move):

    pass
class farmbot_modeling_MoveRelative(Move):

    pass
class SequenceCommand:

    pass
class farmbot_modeling_SendMessage(SequenceCommand):

    def __init__(self, message: str, messageType: str):
        self.message = message
        self.messageType = messageType
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def messageType(self) -> str:
        return self.__messageType

    @messageType.setter
    def messageType(self, messageType: str):
        self.__messageType = messageType

class farmbot_modeling_Wait(SequenceCommand):

    def __init__(self, duration: float):
        self.duration = duration
        
    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, duration: float):
        self.__duration = duration

class farmbot_modeling_TurnOnDigital(SequenceCommand):

    def __init__(self, pin: int):
        self.pin = pin
        
    @property
    def pin(self) -> int:
        return self.__pin

    @pin.setter
    def pin(self, pin: int):
        self.__pin = pin

class farmbot_modeling_ExecuteSequence(SequenceCommand):

    def __init__(self, id: int, farmbot_modeling_ExecuteSequence: "farmbot_modeling_If" = None, farmbot_modeling_ExecuteSequence7: "farmbot_modeling_If" = None):
        self.id = id
        self.farmbot_modeling_ExecuteSequence = farmbot_modeling_ExecuteSequence
        self.farmbot_modeling_ExecuteSequence7 = farmbot_modeling_ExecuteSequence7
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def farmbot_modeling_ExecuteSequence7(self):
        return self.__farmbot_modeling_ExecuteSequence7

    @farmbot_modeling_ExecuteSequence7.setter
    def farmbot_modeling_ExecuteSequence7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farmbot_modeling_ExecuteSequence__farmbot_modeling_ExecuteSequence7", None)
        self.__farmbot_modeling_ExecuteSequence7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "farmbot_modeling_If6"):
                opp_val = getattr(old_value, "farmbot_modeling_If6", None)
                if opp_val == self:
                    setattr(old_value, "farmbot_modeling_If6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "farmbot_modeling_If6"):
                opp_val = getattr(value, "farmbot_modeling_If6", None)
                setattr(value, "farmbot_modeling_If6", self)

    @property
    def farmbot_modeling_ExecuteSequence(self):
        return self.__farmbot_modeling_ExecuteSequence

    @farmbot_modeling_ExecuteSequence.setter
    def farmbot_modeling_ExecuteSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_farmbot_modeling_ExecuteSequence__farmbot_modeling_ExecuteSequence", None)
        self.__farmbot_modeling_ExecuteSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "farmbot_modeling_If4"):
                opp_val = getattr(old_value, "farmbot_modeling_If4", None)
                if opp_val == self:
                    setattr(old_value, "farmbot_modeling_If4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "farmbot_modeling_If4"):
                opp_val = getattr(value, "farmbot_modeling_If4", None)
                setattr(value, "farmbot_modeling_If4", self)

class farmbot_modeling_RunFarmware(SequenceCommand):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class farmbot_modeling_TurnOnAnalog(SequenceCommand):

    def __init__(self, pin: int, value: int):
        self.pin = pin
        self.value = value
        
    @property
    def pin(self) -> int:
        return self.__pin

    @pin.setter
    def pin(self, pin: int):
        self.__pin = pin

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class farmbot_modeling_FindHome(SequenceCommand):

    def __init__(self, axis: str):
        self.axis = axis
        
    @property
    def axis(self) -> str:
        return self.__axis

    @axis.setter
    def axis(self, axis: str):
        self.__axis = axis

class farmbot_modeling_TurnOff(SequenceCommand):

    def __init__(self, pin: int):
        self.pin = pin
        
    @property
    def pin(self) -> int:
        return self.__pin

    @pin.setter
    def pin(self, pin: int):
        self.__pin = pin

class farmbot_modeling_TakePhoto(SequenceCommand):

    pass
class farmbot_modeling_Move(SequenceCommand):

    def __init__(self, x: int, y: int, z: int, speed: int):
        self.x = x
        self.y = y
        self.z = z
        self.speed = speed
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def z(self) -> int:
        return self.__z

    @z.setter
    def z(self, z: int):
        self.__z = z

class SequenceInstruction:

    pass
class farmbot_modeling_If(SequenceInstruction):

    pass
class Command:

    pass
class farmbot_modeling_Schedule(Command):

    def __init__(self, sequence: int, startDate: str, startTime: str, repeat: bool, repeatUnit: str, endDate: str, endTime: str):
        self.sequence = sequence
        self.startDate = startDate
        self.startTime = startTime
        self.repeat = repeat
        self.repeatUnit = repeatUnit
        self.endDate = endDate
        self.endTime = endTime
        
    @property
    def endDate(self) -> str:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: str):
        self.__endDate = endDate

    @property
    def repeat(self) -> bool:
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat: bool):
        self.__repeat = repeat

    @property
    def repeatUnit(self) -> str:
        return self.__repeatUnit

    @repeatUnit.setter
    def repeatUnit(self, repeatUnit: str):
        self.__repeatUnit = repeatUnit

    @property
    def sequence(self) -> int:
        return self.__sequence

    @sequence.setter
    def sequence(self, sequence: int):
        self.__sequence = sequence

    @property
    def startTime(self) -> str:
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime: str):
        self.__startTime = startTime

    @property
    def endTime(self) -> str:
        return self.__endTime

    @endTime.setter
    def endTime(self, endTime: str):
        self.__endTime = endTime

    @property
    def startDate(self) -> str:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate

class farmbot_modeling_ListScheduledEvents(Command):

    pass
class farmbot_modeling_ListSequences(Command):

    pass
class farmbot_modeling_SequenceCommand(Command, SequenceInstruction):

    pass
class farmbot_modeling_Instruction(ABC):

    pass
class farmbot_modeling_Farmbot:

    pass