from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class lts2_LTSGenerator(ABC):

    def __init__(self, lts2_LTSGenerator: "lts2_StateMachine" = None):
        self.lts2_LTSGenerator = lts2_LTSGenerator
        
    @property
    def lts2_LTSGenerator(self):
        return self.__lts2_LTSGenerator

    @lts2_LTSGenerator.setter
    def lts2_LTSGenerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts2_LTSGenerator__lts2_LTSGenerator", None)
        self.__lts2_LTSGenerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lts2_StateMachine13"):
                opp_val = getattr(old_value, "lts2_StateMachine13", None)
                if opp_val == self:
                    setattr(old_value, "lts2_StateMachine13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lts2_StateMachine13"):
                opp_val = getattr(value, "lts2_StateMachine13", None)
                setattr(value, "lts2_StateMachine13", self)

    def processUseCase(self, useCase: str):
        # TODO: Implement processUseCase method
        pass

class UseCaseStep:

    pass
class State:

    pass
class lts2_Transition:

    pass
class lts2_State(ABC):

    pass
class lts2_StateMachine:

    pass
class TransitionalState:

    pass
class lts2_InitialState(TransitionalState):

    pass
class lts2_AbortState(State):

    pass
class lts2_FinalState(State):

    pass
class lts2_TransitionalState(State):

    pass