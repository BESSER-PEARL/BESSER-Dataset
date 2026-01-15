from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ValueSpecification:

    pass
class minuml2_OpaqueExpression(ValueSpecification):

    def __init__(self, language: str, body: str):
        self.language = language
        self.body = body
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class ActivityEdge:

    pass
class minuml2_ObjectFlow(ActivityEdge):

    pass
class minuml2_ControlFlow(ActivityEdge):

    pass
class minuml2_ValueSpecification:

    pass
class ActivityNode:

    pass
class minuml2_ForkNode(ActivityNode):

    pass
class minuml2_ActivityFinalNode(ActivityNode):

    pass
class minuml2_DecisionNode(ActivityNode):

    pass
class minuml2_JoinNode(ActivityNode):

    pass
class minuml2_OpaqueAction(ActivityNode):

    pass
class ActivityGroup:

    pass
class minuml2_ActivityPartition(ActivityGroup):

    pass
class minuml2_ActivityGroup(ABC):

    pass
class minuml2_ActivityEdge:

    pass
class minuml2_ActivityNode:

    pass
class minuml2_Activity:

    pass