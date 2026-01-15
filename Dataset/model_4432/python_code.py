from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class mindstorms_Instruction(ABC):

    pass
class Action:

    pass
class mindstorms_GoForward(Action):

    def __init__(self, cm: int):
        self.cm = cm
        
    @property
    def cm(self) -> int:
        return self.__cm

    @cm.setter
    def cm(self, cm: int):
        self.__cm = cm

class mindstorms_Rotate(Action):

    def __init__(self, degrees: int, random: bool):
        self.degrees = degrees
        self.random = random
        
    @property
    def degrees(self) -> int:
        return self.__degrees

    @degrees.setter
    def degrees(self, degrees: int):
        self.__degrees = degrees

    @property
    def random(self) -> bool:
        return self.__random

    @random.setter
    def random(self, random: bool):
        self.__random = random

class mindstorms_Release(Action):

    pass
class mindstorms_Grab(Action):

    pass
class Instruction:

    pass
class mindstorms_Action(Instruction):

    pass
class mindstorms_Choreography(Instruction):

    def __init__(self, name: str, mindstorms_Choreography: set["mindstorms_Instruction"] = None):
        self.name = name
        self.mindstorms_Choreography = mindstorms_Choreography if mindstorms_Choreography is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mindstorms_Choreography(self):
        return self.__mindstorms_Choreography

    @mindstorms_Choreography.setter
    def mindstorms_Choreography(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mindstorms_Choreography__mindstorms_Choreography", None)
        self.__mindstorms_Choreography = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mindstorms_Instruction"):
                    opp_val = getattr(item, "mindstorms_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "mindstorms_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mindstorms_Instruction"):
                    opp_val = getattr(item, "mindstorms_Instruction", None)
                    
                    setattr(item, "mindstorms_Instruction", self)
                    
