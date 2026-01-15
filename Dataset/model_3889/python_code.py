from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ToState:

    pass
class FromState:

    pass
class AbstractState:

    pass
class IntermediateState:

    pass
class workflow_Processing(IntermediateState):

    pass
class workflow_Decision(IntermediateState):

    pass
class workflow_Join(IntermediateState):

    pass
class workflow_Fork(IntermediateState):

    pass
class workflow_Task(IntermediateState):

    pass
class workflow_End(ToState, AbstractState):

    pass
class workflow_IntermediateState(ToState, AbstractState, FromState):

    pass
class workflow_Start(AbstractState, FromState):

    pass
class workflow_StateContainer(ABC):

    pass
class workflow_ToState(ABC):

    pass
class workflow_FromState(ABC):

    pass
class StateContainer:

    pass
class workflow_SubProcess(IntermediateState, StateContainer):

    pass
class Named:

    pass
class workflow_AbstractState(Named):

    def __init__(self, associatedClass: str):
        self.associatedClass = associatedClass
        
    @property
    def associatedClass(self) -> str:
        return self.__associatedClass

    @associatedClass.setter
    def associatedClass(self, associatedClass: str):
        self.__associatedClass = associatedClass

class workflow_StateTransition(Named):

    pass
class workflow_Workflow(Named, StateContainer):

    pass
class EObject:

    pass
class workflow_Named(EObject):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
