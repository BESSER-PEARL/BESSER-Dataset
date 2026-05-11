from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class IntermediateState:

    pass
class workflow_Decision(IntermediateState):

    pass
class workflow_Processing(IntermediateState):

    pass
class workflow_Task(IntermediateState):

    pass
class ToState:

    pass
class FromState:

    pass
class AbstractState:

    pass
class workflow_End(AbstractState, ToState):

    pass
class workflow_IntermediateState(AbstractState, FromState, ToState):

    pass
class workflow_Start(AbstractState, FromState):

    pass
class workflow_StateContainer(ABC):

    pass
class workflow_ToState(ABC):

    pass
class workflow_FromState(ABC):

    pass
class EObject:

    pass
class workflow_Named(EObject):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class workflow_Join(IntermediateState):

    pass
class workflow_Fork(IntermediateState):

    pass
class StateContainer:

    pass
class workflow_SubProcess(StateContainer, IntermediateState):

    pass
class Named:

    pass
class workflow_AbstractState(Named):

    def __init__(self, associatedClass: str):
        self.associatedClass = associatedClass
        
        pass
    @property
    def associatedClass(self):
        return self.__associatedClass

    @associatedClass.setter
    def associatedClass(self, associatedClass: str):
        self.__associatedClass = associatedClass


class workflow_StateTransition(Named):

    pass
class workflow_Workflow(StateContainer, Named):

    pass