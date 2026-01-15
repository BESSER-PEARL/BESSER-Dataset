from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AttributeType(Enum):
    graph = "graph"
    node = "node"
    edge = "edge"
class EdgeOperator(Enum):
    directed = "directed"
    undirected = "undirected"
class GraphType(Enum):
    graph = "graph"
    digraph = "digraph"


############################################
# Definition of Classes
############################################

class dot_Graph:

    def __init__(self, strict: bool, type: str, name: str, dot_Graph2: set["dot_Statement"] = None, dot_Graph: "dot_GraphvizModel" = None):
        self.strict = strict
        self.type = type
        self.name = name
        self.dot_Graph2 = dot_Graph2 if dot_Graph2 is not None else set()
        self.dot_Graph = dot_Graph
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def strict(self) -> bool:
        return self.__strict

    @strict.setter
    def strict(self, strict: bool):
        self.__strict = strict

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dot_Graph(self):
        return self.__dot_Graph

    @dot_Graph.setter
    def dot_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Graph__dot_Graph", None)
        self.__dot_Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_GraphvizModel"):
                opp_val = getattr(old_value, "dot_GraphvizModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_GraphvizModel"):
                opp_val = getattr(value, "dot_GraphvizModel", None)
                if opp_val is None:
                    setattr(value, "dot_GraphvizModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dot_Graph2(self):
        return self.__dot_Graph2

    @dot_Graph2.setter
    def dot_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Graph__dot_Graph2", None)
        self.__dot_Graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dot_Statement"):
                    opp_val = getattr(item, "dot_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "dot_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dot_Statement"):
                    opp_val = getattr(item, "dot_Statement", None)
                    
                    setattr(item, "dot_Statement", self)
                    

class dot_GraphvizModel:

    pass
class dot_EdgeTarget:

    def __init__(self, operator: str, dot_EdgeTarget: "dot_EdgeStatement" = None, dot_EdgeTarget16: "dot_Subgraph" = None, dot_EdgeTarget18: "dot_Node" = None):
        self.operator = operator
        self.dot_EdgeTarget = dot_EdgeTarget
        self.dot_EdgeTarget16 = dot_EdgeTarget16
        self.dot_EdgeTarget18 = dot_EdgeTarget18
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def dot_EdgeTarget(self):
        return self.__dot_EdgeTarget

    @dot_EdgeTarget.setter
    def dot_EdgeTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_EdgeTarget__dot_EdgeTarget", None)
        self.__dot_EdgeTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_EdgeStatement11"):
                opp_val = getattr(old_value, "dot_EdgeStatement11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_EdgeStatement11"):
                opp_val = getattr(value, "dot_EdgeStatement11", None)
                if opp_val is None:
                    setattr(value, "dot_EdgeStatement11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dot_EdgeTarget16(self):
        return self.__dot_EdgeTarget16

    @dot_EdgeTarget16.setter
    def dot_EdgeTarget16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_EdgeTarget__dot_EdgeTarget16", None)
        self.__dot_EdgeTarget16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_Subgraph"):
                opp_val = getattr(old_value, "dot_Subgraph", None)
                if opp_val == self:
                    setattr(old_value, "dot_Subgraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_Subgraph"):
                opp_val = getattr(value, "dot_Subgraph", None)
                setattr(value, "dot_Subgraph", self)

    @property
    def dot_EdgeTarget18(self):
        return self.__dot_EdgeTarget18

    @dot_EdgeTarget18.setter
    def dot_EdgeTarget18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_EdgeTarget__dot_EdgeTarget18", None)
        self.__dot_EdgeTarget18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_Node19"):
                opp_val = getattr(old_value, "dot_Node19", None)
                if opp_val == self:
                    setattr(old_value, "dot_Node19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_Node19"):
                opp_val = getattr(value, "dot_Node19", None)
                setattr(value, "dot_Node19", self)

class dot_Port:

    def __init__(self, compass_pt: str, name: str, dot_Port: "dot_Node" = None):
        self.compass_pt = compass_pt
        self.name = name
        self.dot_Port = dot_Port
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def compass_pt(self) -> str:
        return self.__compass_pt

    @compass_pt.setter
    def compass_pt(self, compass_pt: str):
        self.__compass_pt = compass_pt

    @property
    def dot_Port(self):
        return self.__dot_Port

    @dot_Port.setter
    def dot_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Port__dot_Port", None)
        self.__dot_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_Node7"):
                opp_val = getattr(old_value, "dot_Node7", None)
                if opp_val == self:
                    setattr(old_value, "dot_Node7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_Node7"):
                opp_val = getattr(value, "dot_Node7", None)
                setattr(value, "dot_Node7", self)

class dot_Node:

    def __init__(self, name: str, dot_Node: "dot_NodeStatement" = None, dot_Node7: "dot_Port" = None, dot_Node9: "dot_EdgeStatement" = None, dot_Node19: "dot_EdgeTarget" = None):
        self.name = name
        self.dot_Node = dot_Node
        self.dot_Node7 = dot_Node7
        self.dot_Node9 = dot_Node9
        self.dot_Node19 = dot_Node19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dot_Node9(self):
        return self.__dot_Node9

    @dot_Node9.setter
    def dot_Node9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Node__dot_Node9", None)
        self.__dot_Node9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_EdgeStatement"):
                opp_val = getattr(old_value, "dot_EdgeStatement", None)
                if opp_val == self:
                    setattr(old_value, "dot_EdgeStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_EdgeStatement"):
                opp_val = getattr(value, "dot_EdgeStatement", None)
                setattr(value, "dot_EdgeStatement", self)

    @property
    def dot_Node7(self):
        return self.__dot_Node7

    @dot_Node7.setter
    def dot_Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Node__dot_Node7", None)
        self.__dot_Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_Port"):
                opp_val = getattr(old_value, "dot_Port", None)
                if opp_val == self:
                    setattr(old_value, "dot_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_Port"):
                opp_val = getattr(value, "dot_Port", None)
                setattr(value, "dot_Port", self)

    @property
    def dot_Node(self):
        return self.__dot_Node

    @dot_Node.setter
    def dot_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Node__dot_Node", None)
        self.__dot_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_NodeStatement"):
                opp_val = getattr(old_value, "dot_NodeStatement", None)
                if opp_val == self:
                    setattr(old_value, "dot_NodeStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_NodeStatement"):
                opp_val = getattr(value, "dot_NodeStatement", None)
                setattr(value, "dot_NodeStatement", self)

    @property
    def dot_Node19(self):
        return self.__dot_Node19

    @dot_Node19.setter
    def dot_Node19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Node__dot_Node19", None)
        self.__dot_Node19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_EdgeTarget18"):
                opp_val = getattr(old_value, "dot_EdgeTarget18", None)
                if opp_val == self:
                    setattr(old_value, "dot_EdgeTarget18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_EdgeTarget18"):
                opp_val = getattr(value, "dot_EdgeTarget18", None)
                setattr(value, "dot_EdgeTarget18", self)

class Statement:

    pass
class dot_EdgeStatement(Statement):

    pass
class dot_AttributeStatement(Statement):

    def __init__(self, type: str, dot_AttributeStatement: set["dot_Attribute"] = None):
        self.type = type
        self.dot_AttributeStatement = dot_AttributeStatement if dot_AttributeStatement is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dot_AttributeStatement(self):
        return self.__dot_AttributeStatement

    @dot_AttributeStatement.setter
    def dot_AttributeStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_AttributeStatement__dot_AttributeStatement", None)
        self.__dot_AttributeStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dot_Attribute21"):
                    opp_val = getattr(item, "dot_Attribute21", None)
                    
                    if opp_val == self:
                        setattr(item, "dot_Attribute21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dot_Attribute21"):
                    opp_val = getattr(item, "dot_Attribute21", None)
                    
                    setattr(item, "dot_Attribute21", self)
                    

class dot_Subgraph(Statement):

    def __init__(self, name: str, dot_Subgraph: "dot_EdgeTarget" = None, dot_Subgraph23: set["dot_Statement"] = None):
        self.name = name
        self.dot_Subgraph = dot_Subgraph
        self.dot_Subgraph23 = dot_Subgraph23 if dot_Subgraph23 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dot_Subgraph(self):
        return self.__dot_Subgraph

    @dot_Subgraph.setter
    def dot_Subgraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Subgraph__dot_Subgraph", None)
        self.__dot_Subgraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_EdgeTarget16"):
                opp_val = getattr(old_value, "dot_EdgeTarget16", None)
                if opp_val == self:
                    setattr(old_value, "dot_EdgeTarget16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_EdgeTarget16"):
                opp_val = getattr(value, "dot_EdgeTarget16", None)
                setattr(value, "dot_EdgeTarget16", self)

    @property
    def dot_Subgraph23(self):
        return self.__dot_Subgraph23

    @dot_Subgraph23.setter
    def dot_Subgraph23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Subgraph__dot_Subgraph23", None)
        self.__dot_Subgraph23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dot_Statement24"):
                    opp_val = getattr(item, "dot_Statement24", None)
                    
                    if opp_val == self:
                        setattr(item, "dot_Statement24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dot_Statement24"):
                    opp_val = getattr(item, "dot_Statement24", None)
                    
                    setattr(item, "dot_Statement24", self)
                    

class dot_NodeStatement(Statement):

    pass
class dot_Attribute(Statement):

    def __init__(self, name: str, value: str, dot_Attribute: "dot_NodeStatement" = None, dot_Attribute14: "dot_EdgeStatement" = None, dot_Attribute21: "dot_AttributeStatement" = None):
        self.name = name
        self.value = value
        self.dot_Attribute = dot_Attribute
        self.dot_Attribute14 = dot_Attribute14
        self.dot_Attribute21 = dot_Attribute21
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dot_Attribute14(self):
        return self.__dot_Attribute14

    @dot_Attribute14.setter
    def dot_Attribute14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Attribute__dot_Attribute14", None)
        self.__dot_Attribute14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_EdgeStatement13"):
                opp_val = getattr(old_value, "dot_EdgeStatement13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_EdgeStatement13"):
                opp_val = getattr(value, "dot_EdgeStatement13", None)
                if opp_val is None:
                    setattr(value, "dot_EdgeStatement13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dot_Attribute21(self):
        return self.__dot_Attribute21

    @dot_Attribute21.setter
    def dot_Attribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Attribute__dot_Attribute21", None)
        self.__dot_Attribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_AttributeStatement"):
                opp_val = getattr(old_value, "dot_AttributeStatement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_AttributeStatement"):
                opp_val = getattr(value, "dot_AttributeStatement", None)
                if opp_val is None:
                    setattr(value, "dot_AttributeStatement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dot_Attribute(self):
        return self.__dot_Attribute

    @dot_Attribute.setter
    def dot_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Attribute__dot_Attribute", None)
        self.__dot_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_NodeStatement5"):
                opp_val = getattr(old_value, "dot_NodeStatement5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_NodeStatement5"):
                opp_val = getattr(value, "dot_NodeStatement5", None)
                if opp_val is None:
                    setattr(value, "dot_NodeStatement5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dot_Statement:

    pass