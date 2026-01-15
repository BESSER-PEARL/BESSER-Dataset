from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class StatementVertex:

    pass
class cfgraph_CallVertex(StatementVertex):

    pass
class cfgraph_SimpleStatementVertex(StatementVertex):

    pass
class BodyVertex:

    pass
class cfgraph_BranchingVertex(BodyVertex):

    pass
class cfgraph_StatementVertex(BodyVertex):

    pass
class cfgraph_EndVertex(BodyVertex):

    pass
class ControlFlowVertex:

    pass
class cfgraph_ControlFlowVertex(ABC):

    pass
class cfgraph_BodyVertex(ControlFlowVertex):

    pass
class cfgraph_ControlFlowEdge:

    def __init__(self, backward: bool, incomingEdges: "cfgraph_BodyVertex" = None, cfgraph_ControlFlowEdge: "cfgraph_StartVertex" = None, ControlFlowEdge: "cfgraph_BodyVertex" = None, cfgraph_ControlFlowEdge6: "cfgraph_StatementVertex" = None, cfgraph_ControlFlowEdge10: "cfgraph_BranchingVertex" = None):
        self.backward = backward
        self.incomingEdges = incomingEdges
        self.cfgraph_ControlFlowEdge = cfgraph_ControlFlowEdge
        self.ControlFlowEdge = ControlFlowEdge
        self.cfgraph_ControlFlowEdge6 = cfgraph_ControlFlowEdge6
        self.cfgraph_ControlFlowEdge10 = cfgraph_ControlFlowEdge10
        
    @property
    def backward(self) -> bool:
        return self.__backward

    @backward.setter
    def backward(self, backward: bool):
        self.__backward = backward

    @property
    def cfgraph_ControlFlowEdge(self):
        return self.__cfgraph_ControlFlowEdge

    @cfgraph_ControlFlowEdge.setter
    def cfgraph_ControlFlowEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cfgraph_ControlFlowEdge__cfgraph_ControlFlowEdge", None)
        self.__cfgraph_ControlFlowEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cfgraph_StartVertex3"):
                opp_val = getattr(old_value, "cfgraph_StartVertex3", None)
                if opp_val == self:
                    setattr(old_value, "cfgraph_StartVertex3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cfgraph_StartVertex3"):
                opp_val = getattr(value, "cfgraph_StartVertex3", None)
                setattr(value, "cfgraph_StartVertex3", self)

    @property
    def cfgraph_ControlFlowEdge6(self):
        return self.__cfgraph_ControlFlowEdge6

    @cfgraph_ControlFlowEdge6.setter
    def cfgraph_ControlFlowEdge6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cfgraph_ControlFlowEdge__cfgraph_ControlFlowEdge6", None)
        self.__cfgraph_ControlFlowEdge6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cfgraph_StatementVertex"):
                opp_val = getattr(old_value, "cfgraph_StatementVertex", None)
                if opp_val == self:
                    setattr(old_value, "cfgraph_StatementVertex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cfgraph_StatementVertex"):
                opp_val = getattr(value, "cfgraph_StatementVertex", None)
                setattr(value, "cfgraph_StatementVertex", self)

    @property
    def incomingEdges(self):
        return self.__incomingEdges

    @incomingEdges.setter
    def incomingEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cfgraph_ControlFlowEdge__incomingEdges", None)
        self.__incomingEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BodyVertex"):
                opp_val = getattr(old_value, "BodyVertex", None)
                if opp_val == self:
                    setattr(old_value, "BodyVertex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BodyVertex"):
                opp_val = getattr(value, "BodyVertex", None)
                setattr(value, "BodyVertex", self)

    @property
    def ControlFlowEdge(self):
        return self.__ControlFlowEdge

    @ControlFlowEdge.setter
    def ControlFlowEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cfgraph_ControlFlowEdge__ControlFlowEdge", None)
        self.__ControlFlowEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "end"):
                opp_val = getattr(old_value, "end", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "end"):
                opp_val = getattr(value, "end", None)
                if opp_val is None:
                    setattr(value, "end", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cfgraph_ControlFlowEdge10(self):
        return self.__cfgraph_ControlFlowEdge10

    @cfgraph_ControlFlowEdge10.setter
    def cfgraph_ControlFlowEdge10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cfgraph_ControlFlowEdge__cfgraph_ControlFlowEdge10", None)
        self.__cfgraph_ControlFlowEdge10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cfgraph_BranchingVertex"):
                opp_val = getattr(old_value, "cfgraph_BranchingVertex", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cfgraph_BranchingVertex"):
                opp_val = getattr(value, "cfgraph_BranchingVertex", None)
                if opp_val is None:
                    setattr(value, "cfgraph_BranchingVertex", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cfgraph_StartVertex(ControlFlowVertex):

    pass
class cfgraph_ControlFlowGraph:

    pass