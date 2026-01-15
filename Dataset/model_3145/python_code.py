from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class LiteralExp:

    pass
class XPath_StringExp(LiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class XPath_IntegerExp(LiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class Axis:

    pass
class XPath_AttributeAxis(Axis):

    pass
class XPath_PrecedingAxis(Axis):

    pass
class XPath_AncestorOrSelfAxis(Axis):

    pass
class XPath_ChildAxis(Axis):

    pass
class XPath_NamespaceAxis(Axis):

    pass
class XPath_DescendantOrSelfAxis(Axis):

    pass
class XPath_FollowingSiblingAxis(Axis):

    pass
class XPath_DescendantAxis(Axis):

    pass
class XPath_FollowingAxis(Axis):

    pass
class XPath_SelfAxis(Axis):

    pass
class XPath_ParentAxis(Axis):

    pass
class XPath_PrecedingSiblingAxis(Axis):

    pass
class XPath_AncestorAxis(Axis):

    pass
class NodeTest:

    pass
class XPath_IsNodeTest(NodeTest):

    pass
class XPath_IsTextTest(NodeTest):

    pass
class XPath_WildCardTest(NodeTest):

    pass
class XPath_LocatedElement(ABC):

    def __init__(self, commentsAfter: str, location: str, commentsBefore: str):
        self.commentsAfter = commentsAfter
        self.location = location
        self.commentsBefore = commentsBefore
        
    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

class NamedElement:

    pass
class XPath_NameTest(NodeTest, NamedElement):

    pass
class Expression:

    pass
class XPath_OperatorCallExp(Expression, NamedElement):

    pass
class XPath_PathExpression(Expression):

    def __init__(self, isAbsolute: str, XPath_PathExpression: set["XPath_Step"] = None):
        self.isAbsolute = isAbsolute
        self.XPath_PathExpression = XPath_PathExpression if XPath_PathExpression is not None else set()
        
    @property
    def isAbsolute(self) -> str:
        return self.__isAbsolute

    @isAbsolute.setter
    def isAbsolute(self, isAbsolute: str):
        self.__isAbsolute = isAbsolute

    @property
    def XPath_PathExpression(self):
        return self.__XPath_PathExpression

    @XPath_PathExpression.setter
    def XPath_PathExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XPath_PathExpression__XPath_PathExpression", None)
        self.__XPath_PathExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XPath_Step"):
                    opp_val = getattr(item, "XPath_Step", None)
                    
                    if opp_val == self:
                        setattr(item, "XPath_Step", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XPath_Step"):
                    opp_val = getattr(item, "XPath_Step", None)
                    
                    setattr(item, "XPath_Step", self)
                    

class XPath_FunctionCallExp(Expression, NamedElement):

    pass
class XPath_LiteralExp(Expression):

    pass
class XPath_VariableExp(Expression, NamedElement):

    pass
class LocatedElement:

    pass
class XPath_Step(LocatedElement):

    pass
class XPath_Predicate(LocatedElement):

    pass
class XPath_Axis(LocatedElement):

    pass
class XPath_Expression(LocatedElement):

    pass
class XPath_NodeTest(LocatedElement):

    pass
class XPath_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
