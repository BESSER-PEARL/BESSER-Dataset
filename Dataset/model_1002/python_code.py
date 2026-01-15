from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FunctionType(Enum):
    Boolean = "Boolean"
    Gausian = "Gausian"
class VariableType(Enum):
    Boolean = "Boolean"
    Real = "Real"
    Categorial = "Categorial"
class MessageType(Enum):
    MarginalEdge = "MarginalEdge"
    VariableToFactor = "VariableToFactor"


############################################
# Definition of Classes
############################################

class Node:

    pass
class graphEditor_Variablenode(Node):

    def __init__(self, type: str, values: float, isKnown: bool):
        self.type = type
        self.values = values
        self.isKnown = isKnown
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def isKnown(self) -> bool:
        return self.__isKnown

    @isKnown.setter
    def isKnown(self, isKnown: bool):
        self.__isKnown = isKnown

    @property
    def values(self) -> float:
        return self.__values

    @values.setter
    def values(self, values: float):
        self.__values = values

class graphEditor_Factornode(Node):

    def __init__(self, type: str, values: str):
        self.type = type
        self.values = values
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class GraphElement:

    pass
class graphEditor_GraphElement(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class graphEditor_Message(GraphElement):

    def __init__(self, count: int, type: str, graphEditor_Message: "graphEditor_Graph" = None, graphEditor_Message6: "graphEditor_Node" = None, graphEditor_Message9: "graphEditor_Node" = None):
        self.count = count
        self.type = type
        self.graphEditor_Message = graphEditor_Message
        self.graphEditor_Message6 = graphEditor_Message6
        self.graphEditor_Message9 = graphEditor_Message9
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def graphEditor_Message9(self):
        return self.__graphEditor_Message9

    @graphEditor_Message9.setter
    def graphEditor_Message9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphEditor_Message__graphEditor_Message9", None)
        self.__graphEditor_Message9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphEditor_Node10"):
                opp_val = getattr(old_value, "graphEditor_Node10", None)
                if opp_val == self:
                    setattr(old_value, "graphEditor_Node10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphEditor_Node10"):
                opp_val = getattr(value, "graphEditor_Node10", None)
                setattr(value, "graphEditor_Node10", self)

    @property
    def graphEditor_Message6(self):
        return self.__graphEditor_Message6

    @graphEditor_Message6.setter
    def graphEditor_Message6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphEditor_Message__graphEditor_Message6", None)
        self.__graphEditor_Message6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphEditor_Node7"):
                opp_val = getattr(old_value, "graphEditor_Node7", None)
                if opp_val == self:
                    setattr(old_value, "graphEditor_Node7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphEditor_Node7"):
                opp_val = getattr(value, "graphEditor_Node7", None)
                setattr(value, "graphEditor_Node7", self)

    @property
    def graphEditor_Message(self):
        return self.__graphEditor_Message

    @graphEditor_Message.setter
    def graphEditor_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphEditor_Message__graphEditor_Message", None)
        self.__graphEditor_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphEditor_Graph4"):
                opp_val = getattr(old_value, "graphEditor_Graph4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphEditor_Graph4"):
                opp_val = getattr(value, "graphEditor_Graph4", None)
                if opp_val is None:
                    setattr(value, "graphEditor_Graph4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphEditor_Edge(GraphElement):

    pass
class graphEditor_Node(GraphElement):

    def __init__(self, name: str, graphEditor_Node13: "graphEditor_Edge" = None, graphEditor_Node16: "graphEditor_Edge" = None, graphEditor_Node: "graphEditor_Graph" = None, graphEditor_Node7: "graphEditor_Message" = None, graphEditor_Node10: "graphEditor_Message" = None):
        self.name = name
        self.graphEditor_Node13 = graphEditor_Node13
        self.graphEditor_Node16 = graphEditor_Node16
        self.graphEditor_Node = graphEditor_Node
        self.graphEditor_Node7 = graphEditor_Node7
        self.graphEditor_Node10 = graphEditor_Node10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graphEditor_Node13(self):
        return self.__graphEditor_Node13

    @graphEditor_Node13.setter
    def graphEditor_Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphEditor_Node__graphEditor_Node13", None)
        self.__graphEditor_Node13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphEditor_Edge12"):
                opp_val = getattr(old_value, "graphEditor_Edge12", None)
                if opp_val == self:
                    setattr(old_value, "graphEditor_Edge12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphEditor_Edge12"):
                opp_val = getattr(value, "graphEditor_Edge12", None)
                setattr(value, "graphEditor_Edge12", self)

    @property
    def graphEditor_Node7(self):
        return self.__graphEditor_Node7

    @graphEditor_Node7.setter
    def graphEditor_Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphEditor_Node__graphEditor_Node7", None)
        self.__graphEditor_Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphEditor_Message6"):
                opp_val = getattr(old_value, "graphEditor_Message6", None)
                if opp_val == self:
                    setattr(old_value, "graphEditor_Message6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphEditor_Message6"):
                opp_val = getattr(value, "graphEditor_Message6", None)
                setattr(value, "graphEditor_Message6", self)

    @property
    def graphEditor_Node16(self):
        return self.__graphEditor_Node16

    @graphEditor_Node16.setter
    def graphEditor_Node16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphEditor_Node__graphEditor_Node16", None)
        self.__graphEditor_Node16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphEditor_Edge15"):
                opp_val = getattr(old_value, "graphEditor_Edge15", None)
                if opp_val == self:
                    setattr(old_value, "graphEditor_Edge15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphEditor_Edge15"):
                opp_val = getattr(value, "graphEditor_Edge15", None)
                setattr(value, "graphEditor_Edge15", self)

    @property
    def graphEditor_Node(self):
        return self.__graphEditor_Node

    @graphEditor_Node.setter
    def graphEditor_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphEditor_Node__graphEditor_Node", None)
        self.__graphEditor_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphEditor_Graph"):
                opp_val = getattr(old_value, "graphEditor_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphEditor_Graph"):
                opp_val = getattr(value, "graphEditor_Graph", None)
                if opp_val is None:
                    setattr(value, "graphEditor_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphEditor_Node10(self):
        return self.__graphEditor_Node10

    @graphEditor_Node10.setter
    def graphEditor_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphEditor_Node__graphEditor_Node10", None)
        self.__graphEditor_Node10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphEditor_Message9"):
                opp_val = getattr(old_value, "graphEditor_Message9", None)
                if opp_val == self:
                    setattr(old_value, "graphEditor_Message9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphEditor_Message9"):
                opp_val = getattr(value, "graphEditor_Message9", None)
                setattr(value, "graphEditor_Message9", self)

class graphEditor_Graph:

    def __init__(self, name: str, result: str, graphEditor_Graph: set["graphEditor_Node"] = None, graphEditor_Graph2: set["graphEditor_Edge"] = None, graphEditor_Graph4: set["graphEditor_Message"] = None):
        self.name = name
        self.result = result
        self.graphEditor_Graph = graphEditor_Graph if graphEditor_Graph is not None else set()
        self.graphEditor_Graph2 = graphEditor_Graph2 if graphEditor_Graph2 is not None else set()
        self.graphEditor_Graph4 = graphEditor_Graph4 if graphEditor_Graph4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def result(self) -> str:
        return self.__result

    @result.setter
    def result(self, result: str):
        self.__result = result

    @property
    def graphEditor_Graph4(self):
        return self.__graphEditor_Graph4

    @graphEditor_Graph4.setter
    def graphEditor_Graph4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphEditor_Graph__graphEditor_Graph4", None)
        self.__graphEditor_Graph4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphEditor_Message"):
                    opp_val = getattr(item, "graphEditor_Message", None)
                    
                    if opp_val == self:
                        setattr(item, "graphEditor_Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphEditor_Message"):
                    opp_val = getattr(item, "graphEditor_Message", None)
                    
                    setattr(item, "graphEditor_Message", self)
                    

    @property
    def graphEditor_Graph2(self):
        return self.__graphEditor_Graph2

    @graphEditor_Graph2.setter
    def graphEditor_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphEditor_Graph__graphEditor_Graph2", None)
        self.__graphEditor_Graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphEditor_Edge"):
                    opp_val = getattr(item, "graphEditor_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "graphEditor_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphEditor_Edge"):
                    opp_val = getattr(item, "graphEditor_Edge", None)
                    
                    setattr(item, "graphEditor_Edge", self)
                    

    @property
    def graphEditor_Graph(self):
        return self.__graphEditor_Graph

    @graphEditor_Graph.setter
    def graphEditor_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphEditor_Graph__graphEditor_Graph", None)
        self.__graphEditor_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphEditor_Node"):
                    opp_val = getattr(item, "graphEditor_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "graphEditor_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphEditor_Node"):
                    opp_val = getattr(item, "graphEditor_Node", None)
                    
                    setattr(item, "graphEditor_Node", self)
                    

    def getConnectingVariablenodes(self, node: str) -> str:
        # TODO: Implement getConnectingVariablenodes method
        pass

    def getGraphElement(self, id: str) -> str:
        # TODO: Implement getGraphElement method
        pass
