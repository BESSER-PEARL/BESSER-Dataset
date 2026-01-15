from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EdgeDecorator:

    pass
class decorators_TestEdgeDecorator1(EdgeDecorator):

    def __init__(self, nodeAURI: str, nodeBURI: str, edgeURI: str):
        self.nodeAURI = nodeAURI
        self.nodeBURI = nodeBURI
        self.edgeURI = edgeURI
        
    @property
    def nodeAURI(self) -> str:
        return self.__nodeAURI

    @nodeAURI.setter
    def nodeAURI(self, nodeAURI: str):
        self.__nodeAURI = nodeAURI

    @property
    def nodeBURI(self) -> str:
        return self.__nodeBURI

    @nodeBURI.setter
    def nodeBURI(self, nodeBURI: str):
        self.__nodeBURI = nodeBURI

    @property
    def edgeURI(self) -> str:
        return self.__edgeURI

    @edgeURI.setter
    def edgeURI(self, edgeURI: str):
        self.__edgeURI = edgeURI

class decorators_NodeDecorator(ABC):

    pass
class decorators_GraphDecorator(ABC):

    pass
class decorators_EdgeDecorator(ABC):

    pass
class decorators_STEMTime:

    pass
class NodeDecorator:

    pass
class decorators_TestNodeDecorator1(NodeDecorator):

    pass
class GraphDecorator:

    pass
class decorators_TestScenarioGraphDecorator1(GraphDecorator):

    def __init__(self, doubleValue: float, intValue: int, stringValue: str, booleanValue: bool, decorators_TestScenarioGraphDecorator1: "decorators_STEMTime" = None):
        self.doubleValue = doubleValue
        self.intValue = intValue
        self.stringValue = stringValue
        self.booleanValue = booleanValue
        self.decorators_TestScenarioGraphDecorator1 = decorators_TestScenarioGraphDecorator1
        
    @property
    def stringValue(self) -> str:
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue

    @property
    def doubleValue(self) -> float:
        return self.__doubleValue

    @doubleValue.setter
    def doubleValue(self, doubleValue: float):
        self.__doubleValue = doubleValue

    @property
    def intValue(self) -> int:
        return self.__intValue

    @intValue.setter
    def intValue(self, intValue: int):
        self.__intValue = intValue

    @property
    def booleanValue(self) -> bool:
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: bool):
        self.__booleanValue = booleanValue

    @property
    def decorators_TestScenarioGraphDecorator1(self):
        return self.__decorators_TestScenarioGraphDecorator1

    @decorators_TestScenarioGraphDecorator1.setter
    def decorators_TestScenarioGraphDecorator1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decorators_TestScenarioGraphDecorator1__decorators_TestScenarioGraphDecorator1", None)
        self.__decorators_TestScenarioGraphDecorator1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decorators_STEMTime"):
                opp_val = getattr(old_value, "decorators_STEMTime", None)
                if opp_val == self:
                    setattr(old_value, "decorators_STEMTime", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decorators_STEMTime"):
                opp_val = getattr(value, "decorators_STEMTime", None)
                setattr(value, "decorators_STEMTime", self)

class decorators_TestGraphDecorator1(GraphDecorator):

    pass