from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudoStateKind(Enum):
    initial = "initial"


############################################
# Definition of Classes
############################################

class BehavioralFeature:

    pass
class statemachine_Operation(BehavioralFeature):

    pass
class MessageEvent:

    pass
class statemachine_CallEvent(MessageEvent):

    pass
class Event:

    pass
class statemachine_MessageEvent(Event):

    pass
class statemachine_Event:

    pass
class State:

    pass
class statemachine_FinalState(State):

    pass
class Vertex:

    pass
class statemachine_State(Vertex):

    pass
class statemachine_PseudoState(Vertex):

    def __init__(self, kind: str):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class statemachine_Trigger:

    pass
class statemachine_Constraint:

    pass
class NamedElement:

    pass
class statemachine_BehavioralFeature:

    pass
class statemachine_Transition(NamedElement):

    pass
class statemachine_Vertex(NamedElement):

    pass
class statemachine_Behavior:

    pass
class statemachine_BehavioredClassifier:

    pass
class statemachine_NamedElement:

    pass
class statemachine_Region:

    pass
class Behavior:

    pass
class statemachine_OpaqueBehavior(Behavior):

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


class statemachine_StateMachine(Behavior):

    pass
class BehavioredClassifier:

    pass
class statemachine_Class(BehavioredClassifier):

    pass