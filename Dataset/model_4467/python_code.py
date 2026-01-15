from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class polybot_modelling_language_Scene:

    pass
class polybot_modelling_language_Instruction(ABC):

    def __init__(self, nextInstructionTrue: str, nextInstructionFalse: str, name: str, nextInstruction: str, polybot_modelling_language_Instruction: "polybot_modelling_language_Robot" = None):
        self.nextInstructionTrue = nextInstructionTrue
        self.nextInstructionFalse = nextInstructionFalse
        self.name = name
        self.nextInstruction = nextInstruction
        self.polybot_modelling_language_Instruction = polybot_modelling_language_Instruction
        
    @property
    def nextInstructionFalse(self) -> str:
        return self.__nextInstructionFalse

    @nextInstructionFalse.setter
    def nextInstructionFalse(self, nextInstructionFalse: str):
        self.__nextInstructionFalse = nextInstructionFalse

    @property
    def nextInstruction(self) -> str:
        return self.__nextInstruction

    @nextInstruction.setter
    def nextInstruction(self, nextInstruction: str):
        self.__nextInstruction = nextInstruction

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nextInstructionTrue(self) -> str:
        return self.__nextInstructionTrue

    @nextInstructionTrue.setter
    def nextInstructionTrue(self, nextInstructionTrue: str):
        self.__nextInstructionTrue = nextInstructionTrue

    @property
    def polybot_modelling_language_Instruction(self):
        return self.__polybot_modelling_language_Instruction

    @polybot_modelling_language_Instruction.setter
    def polybot_modelling_language_Instruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_polybot_modelling_language_Instruction__polybot_modelling_language_Instruction", None)
        self.__polybot_modelling_language_Instruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "polybot_modelling_language_Robot2"):
                opp_val = getattr(old_value, "polybot_modelling_language_Robot2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "polybot_modelling_language_Robot2"):
                opp_val = getattr(value, "polybot_modelling_language_Robot2", None)
                if opp_val is None:
                    setattr(value, "polybot_modelling_language_Robot2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Turn:

    pass
class polybot_modelling_language_TurnLeft(Turn):

    pass
class polybot_modelling_language_TurnRight(Turn):

    pass
class Instruction:

    pass
class polybot_modelling_language_Turn(Instruction):

    def __init__(self, angle: int):
        self.angle = angle
        
    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

class polybot_modelling_language_Release(Instruction):

    pass
class polybot_modelling_language_ComeHome(Instruction):

    pass
class polybot_modelling_language_Catch(Instruction):

    pass
class polybot_modelling_language_MoveStraight(Instruction):

    def __init__(self, distance: int):
        self.distance = distance
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

class polybot_modelling_language_Robot:

    def __init__(self, debug: bool, polybot_modelling_language_Robot: "polybot_modelling_language_Scene" = None, polybot_modelling_language_Robot2: set["polybot_modelling_language_Instruction"] = None):
        self.debug = debug
        self.polybot_modelling_language_Robot = polybot_modelling_language_Robot
        self.polybot_modelling_language_Robot2 = polybot_modelling_language_Robot2 if polybot_modelling_language_Robot2 is not None else set()
        
    @property
    def debug(self) -> bool:
        return self.__debug

    @debug.setter
    def debug(self, debug: bool):
        self.__debug = debug

    @property
    def polybot_modelling_language_Robot(self):
        return self.__polybot_modelling_language_Robot

    @polybot_modelling_language_Robot.setter
    def polybot_modelling_language_Robot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_polybot_modelling_language_Robot__polybot_modelling_language_Robot", None)
        self.__polybot_modelling_language_Robot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "polybot_modelling_language_Scene"):
                opp_val = getattr(old_value, "polybot_modelling_language_Scene", None)
                if opp_val == self:
                    setattr(old_value, "polybot_modelling_language_Scene", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "polybot_modelling_language_Scene"):
                opp_val = getattr(value, "polybot_modelling_language_Scene", None)
                setattr(value, "polybot_modelling_language_Scene", self)

    @property
    def polybot_modelling_language_Robot2(self):
        return self.__polybot_modelling_language_Robot2

    @polybot_modelling_language_Robot2.setter
    def polybot_modelling_language_Robot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_polybot_modelling_language_Robot__polybot_modelling_language_Robot2", None)
        self.__polybot_modelling_language_Robot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "polybot_modelling_language_Instruction"):
                    opp_val = getattr(item, "polybot_modelling_language_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "polybot_modelling_language_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "polybot_modelling_language_Instruction"):
                    opp_val = getattr(item, "polybot_modelling_language_Instruction", None)
                    
                    setattr(item, "polybot_modelling_language_Instruction", self)
                    
