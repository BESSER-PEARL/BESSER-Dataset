from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class graph2_GraphComponent(ABC):

    def __init__(self, text: str, graph2_GraphComponent: "graph2_Graph" = None):
        self.text = text
        self.graph2_GraphComponent = graph2_GraphComponent
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def graph2_GraphComponent(self):
        return self.__graph2_GraphComponent

    @graph2_GraphComponent.setter
    def graph2_GraphComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph2_GraphComponent__graph2_GraphComponent", None)
        self.__graph2_GraphComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph2_Graph"):
                opp_val = getattr(old_value, "graph2_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph2_Graph"):
                opp_val = getattr(value, "graph2_Graph", None)
                if opp_val is None:
                    setattr(value, "graph2_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graph2_Graph:

    pass
class GraphComponent:

    pass
class graph2_Edge(GraphComponent):

    pass
class graph2_Node(GraphComponent):

    pass