from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph3_Graph:

    pass
class graph3_Node:

    def __init__(self, text: str, graph3_Node: "graph3_Node" = None, graph3_Node0: set["graph3_Node"] = None, graph3_Node3: "graph3_Graph" = None):
        self.text = text
        self.graph3_Node = graph3_Node
        self.graph3_Node0 = graph3_Node0 if graph3_Node0 is not None else set()
        self.graph3_Node3 = graph3_Node3
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def graph3_Node(self):
        return self.__graph3_Node

    @graph3_Node.setter
    def graph3_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph3_Node__graph3_Node", None)
        self.__graph3_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph3_Node0"):
                opp_val = getattr(old_value, "graph3_Node0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph3_Node0"):
                opp_val = getattr(value, "graph3_Node0", None)
                if opp_val is None:
                    setattr(value, "graph3_Node0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph3_Node3(self):
        return self.__graph3_Node3

    @graph3_Node3.setter
    def graph3_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph3_Node__graph3_Node3", None)
        self.__graph3_Node3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph3_Graph"):
                opp_val = getattr(old_value, "graph3_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph3_Graph"):
                opp_val = getattr(value, "graph3_Graph", None)
                if opp_val is None:
                    setattr(value, "graph3_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph3_Node0(self):
        return self.__graph3_Node0

    @graph3_Node0.setter
    def graph3_Node0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph3_Node__graph3_Node0", None)
        self.__graph3_Node0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph3_Node"):
                    opp_val = getattr(item, "graph3_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "graph3_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph3_Node"):
                    opp_val = getattr(item, "graph3_Node", None)
                    
                    setattr(item, "graph3_Node", self)
                    
