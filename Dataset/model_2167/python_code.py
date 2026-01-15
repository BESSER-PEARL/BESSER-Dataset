from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class FitPolicy(Enum):
    AUTO = "AUTO"
    CUSTOM = "CUSTOM"


############################################
# Definition of Classes
############################################

class graph_ResourceGraphs:

    pass
class graph_ResourcePlot:

    def __init__(self, name: str, rgb: str, fit: str, min: float, max: float, graph_ResourcePlot: "graph_ResourceGraph" = None):
        self.name = name
        self.rgb = rgb
        self.fit = fit
        self.min = min
        self.max = max
        self.graph_ResourcePlot = graph_ResourcePlot
        
    @property
    def max(self) -> float:
        return self.__max

    @max.setter
    def max(self, max: float):
        self.__max = max

    @property
    def rgb(self) -> str:
        return self.__rgb

    @rgb.setter
    def rgb(self, rgb: str):
        self.__rgb = rgb

    @property
    def min(self) -> float:
        return self.__min

    @min.setter
    def min(self, min: float):
        self.__min = min

    @property
    def fit(self) -> str:
        return self.__fit

    @fit.setter
    def fit(self, fit: str):
        self.__fit = fit

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graph_ResourcePlot(self):
        return self.__graph_ResourcePlot

    @graph_ResourcePlot.setter
    def graph_ResourcePlot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ResourcePlot__graph_ResourcePlot", None)
        self.__graph_ResourcePlot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_ResourceGraph2"):
                opp_val = getattr(old_value, "graph_ResourceGraph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_ResourceGraph2"):
                opp_val = getattr(value, "graph_ResourceGraph2", None)
                if opp_val is None:
                    setattr(value, "graph_ResourceGraph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graph_ResourceGraph:

    def __init__(self, name: str, graph_ResourceGraph: "graph_ResourceGraphs" = None, graph_ResourceGraph2: set["graph_ResourcePlot"] = None):
        self.name = name
        self.graph_ResourceGraph = graph_ResourceGraph
        self.graph_ResourceGraph2 = graph_ResourceGraph2 if graph_ResourceGraph2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graph_ResourceGraph2(self):
        return self.__graph_ResourceGraph2

    @graph_ResourceGraph2.setter
    def graph_ResourceGraph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ResourceGraph__graph_ResourceGraph2", None)
        self.__graph_ResourceGraph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_ResourcePlot"):
                    opp_val = getattr(item, "graph_ResourcePlot", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_ResourcePlot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_ResourcePlot"):
                    opp_val = getattr(item, "graph_ResourcePlot", None)
                    
                    setattr(item, "graph_ResourcePlot", self)
                    

    @property
    def graph_ResourceGraph(self):
        return self.__graph_ResourceGraph

    @graph_ResourceGraph.setter
    def graph_ResourceGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ResourceGraph__graph_ResourceGraph", None)
        self.__graph_ResourceGraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_ResourceGraphs"):
                opp_val = getattr(old_value, "graph_ResourceGraphs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_ResourceGraphs"):
                opp_val = getattr(value, "graph_ResourceGraphs", None)
                if opp_val is None:
                    setattr(value, "graph_ResourceGraphs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
