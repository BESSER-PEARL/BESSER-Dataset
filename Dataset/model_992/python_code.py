from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class DAG_Revision:

    pass
class DAG_Edge:

    def __init__(self, ID: int, name: str, Edge: "DAG_Node" = None, Edge8: "DAG_Node" = None, outgoing: "DAG_Node" = None, incoming: "DAG_Node" = None):
        self.ID = ID
        self.name = name
        self.Edge = Edge
        self.Edge8 = Edge8
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                if opp_val is None:
                    setattr(value, "from", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Edge8(self):
        return self.__Edge8

    @Edge8.setter
    def Edge8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Edge__Edge8", None)
        self.__Edge8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                if opp_val is None:
                    setattr(value, "to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Edge__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node12"):
                opp_val = getattr(old_value, "Node12", None)
                if opp_val == self:
                    setattr(old_value, "Node12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node12"):
                opp_val = getattr(value, "Node12", None)
                setattr(value, "Node12", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Edge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node14"):
                opp_val = getattr(old_value, "Node14", None)
                if opp_val == self:
                    setattr(old_value, "Node14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node14"):
                opp_val = getattr(value, "Node14", None)
                setattr(value, "Node14", self)

class DAG_Node:

    def __init__(self, ID: int, name: str, level: int, DAG_Node: "DAG_Graph" = None, Node: "DAG_Node" = None, children: set["DAG_Node"] = None, Node5: "DAG_Node" = None, parents: set["DAG_Node"] = None, from: set["DAG_Edge"] = None, to: set["DAG_Edge"] = None, DAG_Node10: "DAG_Revision" = None, Node12: "DAG_Edge" = None, Node14: "DAG_Edge" = None):
        self.ID = ID
        self.name = name
        self.level = level
        self.DAG_Node = DAG_Node
        self.Node = Node
        self.children = children if children is not None else set()
        self.Node5 = Node5
        self.parents = parents if parents is not None else set()
        self.from = from if from is not None else set()
        self.to = to if to is not None else set()
        self.DAG_Node10 = DAG_Node10
        self.Node12 = Node12
        self.Node14 = Node14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def parents(self):
        return self.__parents

    @parents.setter
    def parents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Node__parents", None)
        self.__parents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node5"):
                    opp_val = getattr(item, "Node5", None)
                    
                    if opp_val == self:
                        setattr(item, "Node5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node5"):
                    opp_val = getattr(item, "Node5", None)
                    
                    setattr(item, "Node5", self)
                    

    @property
    def Node12(self):
        return self.__Node12

    @Node12.setter
    def Node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Node__Node12", None)
        self.__Node12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def DAG_Node10(self):
        return self.__DAG_Node10

    @DAG_Node10.setter
    def DAG_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Node__DAG_Node10", None)
        self.__DAG_Node10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DAG_Revision"):
                opp_val = getattr(old_value, "DAG_Revision", None)
                if opp_val == self:
                    setattr(old_value, "DAG_Revision", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DAG_Revision"):
                opp_val = getattr(value, "DAG_Revision", None)
                setattr(value, "DAG_Revision", self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Node__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    setattr(item, "Edge", self)
                    

    @property
    def Node14(self):
        return self.__Node14

    @Node14.setter
    def Node14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Node__Node14", None)
        self.__Node14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Node__children", None)
        self.__children = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    if opp_val == self:
                        setattr(item, "Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    setattr(item, "Node", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                if opp_val is None:
                    setattr(value, "children", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DAG_Node(self):
        return self.__DAG_Node

    @DAG_Node.setter
    def DAG_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Node__DAG_Node", None)
        self.__DAG_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DAG_Graph"):
                opp_val = getattr(old_value, "DAG_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DAG_Graph"):
                opp_val = getattr(value, "DAG_Graph", None)
                if opp_val is None:
                    setattr(value, "DAG_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node5(self):
        return self.__Node5

    @Node5.setter
    def Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Node__Node5", None)
        self.__Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parents"):
                opp_val = getattr(old_value, "parents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parents"):
                opp_val = getattr(value, "parents", None)
                if opp_val is None:
                    setattr(value, "parents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Node__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge8"):
                    opp_val = getattr(item, "Edge8", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge8"):
                    opp_val = getattr(item, "Edge8", None)
                    
                    setattr(item, "Edge8", self)
                    

class DAG_Graph:

    def __init__(self, name: str, DAG_Graph: set["DAG_Node"] = None):
        self.name = name
        self.DAG_Graph = DAG_Graph if DAG_Graph is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DAG_Graph(self):
        return self.__DAG_Graph

    @DAG_Graph.setter
    def DAG_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DAG_Graph__DAG_Graph", None)
        self.__DAG_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DAG_Node"):
                    opp_val = getattr(item, "DAG_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "DAG_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DAG_Node"):
                    opp_val = getattr(item, "DAG_Node", None)
                    
                    setattr(item, "DAG_Node", self)
                    
