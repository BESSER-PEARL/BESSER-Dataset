from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ActivityEdge:

    pass
class minuml2_ObjectFlow(ActivityEdge):

    pass
class minuml2_ControlFlow(ActivityEdge):

    pass
class minuml2_OpaqueExpression:

    def __init__(self, language: str, body: str, minuml2_OpaqueExpression: "minuml2_ActivityEdge" = None):
        self.language = language
        self.body = body
        self.minuml2_OpaqueExpression = minuml2_OpaqueExpression
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def minuml2_OpaqueExpression(self):
        return self.__minuml2_OpaqueExpression

    @minuml2_OpaqueExpression.setter
    def minuml2_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minuml2_OpaqueExpression__minuml2_OpaqueExpression", None)
        self.__minuml2_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minuml2_ActivityEdge20"):
                opp_val = getattr(old_value, "minuml2_ActivityEdge20", None)
                if opp_val == self:
                    setattr(old_value, "minuml2_ActivityEdge20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minuml2_ActivityEdge20"):
                opp_val = getattr(value, "minuml2_ActivityEdge20", None)
                setattr(value, "minuml2_ActivityEdge20", self)

class ActivityNode:

    pass
class minuml2_ForkNode(ActivityNode):

    pass
class minuml2_InitialNode(ActivityNode):

    pass
class minuml2_JoinNode(ActivityNode):

    pass
class minuml2_DecisionNode(ActivityNode):

    pass
class minuml2_ObjectNode(ActivityNode):

    pass
class minuml2_OpaqueAction(ActivityNode):

    pass
class ModelElement:

    pass
class minuml2_ActivityNode(ModelElement):

    pass
class minuml2_ActivityEdge(ModelElement):

    pass
class minuml2_Activity(ModelElement):

    pass
class minuml2_ActivityPartition(ModelElement):

    pass
class minuml2_ModelElement:

    def __init__(self, name: str, minuml2_ModelElement: "minuml2_ActivityPartition" = None, minuml2_ModelElement22: "minuml2_ObjectFlow" = None):
        self.name = name
        self.minuml2_ModelElement = minuml2_ModelElement
        self.minuml2_ModelElement22 = minuml2_ModelElement22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minuml2_ModelElement(self):
        return self.__minuml2_ModelElement

    @minuml2_ModelElement.setter
    def minuml2_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minuml2_ModelElement__minuml2_ModelElement", None)
        self.__minuml2_ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minuml2_ActivityPartition"):
                opp_val = getattr(old_value, "minuml2_ActivityPartition", None)
                if opp_val == self:
                    setattr(old_value, "minuml2_ActivityPartition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minuml2_ActivityPartition"):
                opp_val = getattr(value, "minuml2_ActivityPartition", None)
                setattr(value, "minuml2_ActivityPartition", self)

    @property
    def minuml2_ModelElement22(self):
        return self.__minuml2_ModelElement22

    @minuml2_ModelElement22.setter
    def minuml2_ModelElement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minuml2_ModelElement__minuml2_ModelElement22", None)
        self.__minuml2_ModelElement22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minuml2_ObjectFlow"):
                opp_val = getattr(old_value, "minuml2_ObjectFlow", None)
                if opp_val == self:
                    setattr(old_value, "minuml2_ObjectFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minuml2_ObjectFlow"):
                opp_val = getattr(value, "minuml2_ObjectFlow", None)
                setattr(value, "minuml2_ObjectFlow", self)

class minuml2_ActivityFinalNode(ActivityNode):

    pass