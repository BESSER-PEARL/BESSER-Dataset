from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class attributetype(Enum):
    graph = "graph"
    node = "node"
    edge = "edge"
class graphtype(Enum):
    graph = "graph"
    digraph = "digraph"
class edgeop(Enum):
    directed = "directed"
    undirected = "undirected"


############################################
# Definition of Classes
############################################

class edgeRHS:

    pass
class dot_edgeRHS_subgraph(edgeRHS):

    pass
class dot_edgeRHS_node(edgeRHS):

    pass
class dot_attr_list:

    pass
class dot_edgeRHS:

    def __init__(self, op: str, dot_edgeRHS: "dot_edge_stmt_node" = None, dot_edgeRHS11: "dot_edge_stmt_subgraph" = None):
        self.op = op
        self.dot_edgeRHS = dot_edgeRHS
        self.dot_edgeRHS11 = dot_edgeRHS11
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def dot_edgeRHS(self):
        return self.__dot_edgeRHS

    @dot_edgeRHS.setter
    def dot_edgeRHS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_edgeRHS__dot_edgeRHS", None)
        self.__dot_edgeRHS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_edge_stmt_node5"):
                opp_val = getattr(old_value, "dot_edge_stmt_node5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_edge_stmt_node5"):
                opp_val = getattr(value, "dot_edge_stmt_node5", None)
                if opp_val is None:
                    setattr(value, "dot_edge_stmt_node5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dot_edgeRHS11(self):
        return self.__dot_edgeRHS11

    @dot_edgeRHS11.setter
    def dot_edgeRHS11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_edgeRHS__dot_edgeRHS11", None)
        self.__dot_edgeRHS11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_edge_stmt_subgraph10"):
                opp_val = getattr(old_value, "dot_edge_stmt_subgraph10", None)
                if opp_val == self:
                    setattr(old_value, "dot_edge_stmt_subgraph10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_edge_stmt_subgraph10"):
                opp_val = getattr(value, "dot_edge_stmt_subgraph10", None)
                setattr(value, "dot_edge_stmt_subgraph10", self)

class dot_a_list:

    def __init__(self, name: str, value: str, dot_a_list: "dot_attr_list" = None):
        self.name = name
        self.value = value
        self.dot_a_list = dot_a_list
        
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
    def dot_a_list(self):
        return self.__dot_a_list

    @dot_a_list.setter
    def dot_a_list(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_a_list__dot_a_list", None)
        self.__dot_a_list = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_attr_list20"):
                opp_val = getattr(old_value, "dot_attr_list20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_attr_list20"):
                opp_val = getattr(value, "dot_attr_list20", None)
                if opp_val is None:
                    setattr(value, "dot_attr_list20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dot_graph:

    def __init__(self, strict: bool, type: str, name: str, dot_graph2: set["dot_stmt"] = None, dot_graph: "dot_graphvizmodel" = None):
        self.strict = strict
        self.type = type
        self.name = name
        self.dot_graph2 = dot_graph2 if dot_graph2 is not None else set()
        self.dot_graph = dot_graph
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def strict(self) -> bool:
        return self.__strict

    @strict.setter
    def strict(self, strict: bool):
        self.__strict = strict

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dot_graph(self):
        return self.__dot_graph

    @dot_graph.setter
    def dot_graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_graph__dot_graph", None)
        self.__dot_graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_graphvizmodel"):
                opp_val = getattr(old_value, "dot_graphvizmodel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_graphvizmodel"):
                opp_val = getattr(value, "dot_graphvizmodel", None)
                if opp_val is None:
                    setattr(value, "dot_graphvizmodel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dot_graph2(self):
        return self.__dot_graph2

    @dot_graph2.setter
    def dot_graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_graph__dot_graph2", None)
        self.__dot_graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dot_stmt"):
                    opp_val = getattr(item, "dot_stmt", None)
                    
                    if opp_val == self:
                        setattr(item, "dot_stmt", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dot_stmt"):
                    opp_val = getattr(item, "dot_stmt", None)
                    
                    setattr(item, "dot_stmt", self)
                    

class dot_graphvizmodel:

    pass
class dot_node_id:

    def __init__(self, name: str, dot_node_id: "dot_edge_stmt_node" = None, dot_node_id25: "dot_edgeRHS_node" = None):
        self.name = name
        self.dot_node_id = dot_node_id
        self.dot_node_id25 = dot_node_id25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dot_node_id25(self):
        return self.__dot_node_id25

    @dot_node_id25.setter
    def dot_node_id25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_node_id__dot_node_id25", None)
        self.__dot_node_id25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_edgeRHS_node"):
                opp_val = getattr(old_value, "dot_edgeRHS_node", None)
                if opp_val == self:
                    setattr(old_value, "dot_edgeRHS_node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_edgeRHS_node"):
                opp_val = getattr(value, "dot_edgeRHS_node", None)
                setattr(value, "dot_edgeRHS_node", self)

    @property
    def dot_node_id(self):
        return self.__dot_node_id

    @dot_node_id.setter
    def dot_node_id(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_node_id__dot_node_id", None)
        self.__dot_node_id = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_edge_stmt_node"):
                opp_val = getattr(old_value, "dot_edge_stmt_node", None)
                if opp_val == self:
                    setattr(old_value, "dot_edge_stmt_node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_edge_stmt_node"):
                opp_val = getattr(value, "dot_edge_stmt_node", None)
                setattr(value, "dot_edge_stmt_node", self)

class stmt:

    pass
class dot_subgraph(stmt):

    def __init__(self, name: str, dot_subgraph: "dot_edge_stmt_subgraph" = None, dot_subgraph22: set["dot_stmt"] = None, dot_subgraph27: "dot_edgeRHS_subgraph" = None):
        self.name = name
        self.dot_subgraph = dot_subgraph
        self.dot_subgraph22 = dot_subgraph22 if dot_subgraph22 is not None else set()
        self.dot_subgraph27 = dot_subgraph27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dot_subgraph22(self):
        return self.__dot_subgraph22

    @dot_subgraph22.setter
    def dot_subgraph22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_subgraph__dot_subgraph22", None)
        self.__dot_subgraph22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dot_stmt23"):
                    opp_val = getattr(item, "dot_stmt23", None)
                    
                    if opp_val == self:
                        setattr(item, "dot_stmt23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dot_stmt23"):
                    opp_val = getattr(item, "dot_stmt23", None)
                    
                    setattr(item, "dot_stmt23", self)
                    

    @property
    def dot_subgraph27(self):
        return self.__dot_subgraph27

    @dot_subgraph27.setter
    def dot_subgraph27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_subgraph__dot_subgraph27", None)
        self.__dot_subgraph27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_edgeRHS_subgraph"):
                opp_val = getattr(old_value, "dot_edgeRHS_subgraph", None)
                if opp_val == self:
                    setattr(old_value, "dot_edgeRHS_subgraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_edgeRHS_subgraph"):
                opp_val = getattr(value, "dot_edgeRHS_subgraph", None)
                setattr(value, "dot_edgeRHS_subgraph", self)

    @property
    def dot_subgraph(self):
        return self.__dot_subgraph

    @dot_subgraph.setter
    def dot_subgraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_subgraph__dot_subgraph", None)
        self.__dot_subgraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_edge_stmt_subgraph"):
                opp_val = getattr(old_value, "dot_edge_stmt_subgraph", None)
                if opp_val == self:
                    setattr(old_value, "dot_edge_stmt_subgraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_edge_stmt_subgraph"):
                opp_val = getattr(value, "dot_edge_stmt_subgraph", None)
                setattr(value, "dot_edge_stmt_subgraph", self)

class dot_edge_stmt_subgraph(stmt):

    pass
class dot_attribute(stmt):

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dot_attr_stmt(stmt):

    def __init__(self, type: str, dot_attr_stmt: set["dot_attr_list"] = None):
        self.type = type
        self.dot_attr_stmt = dot_attr_stmt if dot_attr_stmt is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dot_attr_stmt(self):
        return self.__dot_attr_stmt

    @dot_attr_stmt.setter
    def dot_attr_stmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_attr_stmt__dot_attr_stmt", None)
        self.__dot_attr_stmt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dot_attr_list18"):
                    opp_val = getattr(item, "dot_attr_list18", None)
                    
                    if opp_val == self:
                        setattr(item, "dot_attr_list18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dot_attr_list18"):
                    opp_val = getattr(item, "dot_attr_list18", None)
                    
                    setattr(item, "dot_attr_list18", self)
                    

class dot_node_stmt(stmt):

    def __init__(self, name: str, dot_node_stmt: set["dot_attr_list"] = None):
        self.name = name
        self.dot_node_stmt = dot_node_stmt if dot_node_stmt is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dot_node_stmt(self):
        return self.__dot_node_stmt

    @dot_node_stmt.setter
    def dot_node_stmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_node_stmt__dot_node_stmt", None)
        self.__dot_node_stmt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dot_attr_list16"):
                    opp_val = getattr(item, "dot_attr_list16", None)
                    
                    if opp_val == self:
                        setattr(item, "dot_attr_list16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dot_attr_list16"):
                    opp_val = getattr(item, "dot_attr_list16", None)
                    
                    setattr(item, "dot_attr_list16", self)
                    

class dot_edge_stmt_node(stmt):

    pass
class dot_stmt:

    pass