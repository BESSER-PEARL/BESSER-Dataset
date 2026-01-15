from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsmgen_FSMGenElement:

    pass
class fsmgen_AbstractInterfaceItem:

    pass
class fsmgen_TransitionBase:

    pass
class fsmgen_EObject:

    pass
class fsmgen_StateGraphNode:

    pass
class GraphItem:

    pass
class fsmgen_StateGraph:

    pass
class fsmgen_Link(GraphItem):

    def __init__(self, ifitemTriggered: bool, Link: "fsmgen_Graph" = None, Link14: "fsmgen_Node" = None, Link16: "fsmgen_Node" = None, incoming: "fsmgen_Node" = None, fsmgen_Link: "fsmgen_Link" = None, fsmgen_Link26: set["fsmgen_Link"] = None, fsmgen_Link29: "fsmgen_EObject" = None, fsmgen_Link31: "fsmgen_TransitionBase" = None, fsmgen_Link39: "fsmgen_CommonTrigger" = None, links: "fsmgen_Graph" = None, outgoing: "fsmgen_Node" = None):
        self.ifitemTriggered = ifitemTriggered
        self.Link = Link
        self.Link14 = Link14
        self.Link16 = Link16
        self.incoming = incoming
        self.fsmgen_Link = fsmgen_Link
        self.fsmgen_Link26 = fsmgen_Link26 if fsmgen_Link26 is not None else set()
        self.fsmgen_Link29 = fsmgen_Link29
        self.fsmgen_Link31 = fsmgen_Link31
        self.fsmgen_Link39 = fsmgen_Link39
        self.links = links
        self.outgoing = outgoing
        
    @property
    def ifitemTriggered(self) -> bool:
        return self.__ifitemTriggered

    @ifitemTriggered.setter
    def ifitemTriggered(self, ifitemTriggered: bool):
        self.__ifitemTriggered = ifitemTriggered

    @property
    def Link(self):
        return self.__Link

    @Link.setter
    def Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Link__Link", None)
        self.__Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph5"):
                opp_val = getattr(old_value, "graph5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph5"):
                opp_val = getattr(value, "graph5", None)
                if opp_val is None:
                    setattr(value, "graph5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsmgen_Link(self):
        return self.__fsmgen_Link

    @fsmgen_Link.setter
    def fsmgen_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Link__fsmgen_Link", None)
        self.__fsmgen_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmgen_Link26"):
                opp_val = getattr(old_value, "fsmgen_Link26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmgen_Link26"):
                opp_val = getattr(value, "fsmgen_Link26", None)
                if opp_val is None:
                    setattr(value, "fsmgen_Link26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsmgen_Link31(self):
        return self.__fsmgen_Link31

    @fsmgen_Link31.setter
    def fsmgen_Link31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Link__fsmgen_Link31", None)
        self.__fsmgen_Link31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmgen_TransitionBase"):
                opp_val = getattr(old_value, "fsmgen_TransitionBase", None)
                if opp_val == self:
                    setattr(old_value, "fsmgen_TransitionBase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmgen_TransitionBase"):
                opp_val = getattr(value, "fsmgen_TransitionBase", None)
                setattr(value, "fsmgen_TransitionBase", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Link__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node23"):
                opp_val = getattr(old_value, "Node23", None)
                if opp_val == self:
                    setattr(old_value, "Node23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node23"):
                opp_val = getattr(value, "Node23", None)
                setattr(value, "Node23", self)

    @property
    def fsmgen_Link39(self):
        return self.__fsmgen_Link39

    @fsmgen_Link39.setter
    def fsmgen_Link39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Link__fsmgen_Link39", None)
        self.__fsmgen_Link39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmgen_CommonTrigger38"):
                opp_val = getattr(old_value, "fsmgen_CommonTrigger38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmgen_CommonTrigger38"):
                opp_val = getattr(value, "fsmgen_CommonTrigger38", None)
                if opp_val is None:
                    setattr(value, "fsmgen_CommonTrigger38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Link__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node25"):
                opp_val = getattr(old_value, "Node25", None)
                if opp_val == self:
                    setattr(old_value, "Node25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node25"):
                opp_val = getattr(value, "Node25", None)
                setattr(value, "Node25", self)

    @property
    def fsmgen_Link26(self):
        return self.__fsmgen_Link26

    @fsmgen_Link26.setter
    def fsmgen_Link26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Link__fsmgen_Link26", None)
        self.__fsmgen_Link26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmgen_Link"):
                    opp_val = getattr(item, "fsmgen_Link", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmgen_Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmgen_Link"):
                    opp_val = getattr(item, "fsmgen_Link", None)
                    
                    setattr(item, "fsmgen_Link", self)
                    

    @property
    def links(self):
        return self.__links

    @links.setter
    def links(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Link__links", None)
        self.__links = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph21"):
                opp_val = getattr(old_value, "Graph21", None)
                if opp_val == self:
                    setattr(old_value, "Graph21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph21"):
                opp_val = getattr(value, "Graph21", None)
                setattr(value, "Graph21", self)

    @property
    def Link16(self):
        return self.__Link16

    @Link16.setter
    def Link16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Link__Link16", None)
        self.__Link16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Link14(self):
        return self.__Link14

    @Link14.setter
    def Link14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Link__Link14", None)
        self.__Link14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsmgen_Link29(self):
        return self.__fsmgen_Link29

    @fsmgen_Link29.setter
    def fsmgen_Link29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Link__fsmgen_Link29", None)
        self.__fsmgen_Link29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmgen_EObject"):
                opp_val = getattr(old_value, "fsmgen_EObject", None)
                if opp_val == self:
                    setattr(old_value, "fsmgen_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmgen_EObject"):
                opp_val = getattr(value, "fsmgen_EObject", None)
                setattr(value, "fsmgen_EObject", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class fsmgen_Node(GraphItem):

    def __init__(self, inheritanceLevel: int, Node: "fsmgen_Graph" = None, Node9: "fsmgen_Graph" = None, nodes: "fsmgen_Graph" = None, node: "fsmgen_Graph" = None, source: set["fsmgen_Link"] = None, target: set["fsmgen_Link"] = None, fsmgen_Node: "fsmgen_StateGraphNode" = None, fsmgen_Node19: set["fsmgen_CommonTrigger"] = None, Node25: "fsmgen_Link" = None, Node23: "fsmgen_Link" = None):
        self.inheritanceLevel = inheritanceLevel
        self.Node = Node
        self.Node9 = Node9
        self.nodes = nodes
        self.node = node
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.fsmgen_Node = fsmgen_Node
        self.fsmgen_Node19 = fsmgen_Node19 if fsmgen_Node19 is not None else set()
        self.Node25 = Node25
        self.Node23 = Node23
        
    @property
    def inheritanceLevel(self) -> int:
        return self.__inheritanceLevel

    @inheritanceLevel.setter
    def inheritanceLevel(self, inheritanceLevel: int):
        self.__inheritanceLevel = inheritanceLevel

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Node__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph"):
                opp_val = getattr(old_value, "Graph", None)
                if opp_val == self:
                    setattr(old_value, "Graph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph"):
                opp_val = getattr(value, "Graph", None)
                setattr(value, "Graph", self)

    @property
    def Node9(self):
        return self.__Node9

    @Node9.setter
    def Node9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Node__Node9", None)
        self.__Node9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subgraph"):
                opp_val = getattr(old_value, "subgraph", None)
                if opp_val == self:
                    setattr(old_value, "subgraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subgraph"):
                opp_val = getattr(value, "subgraph", None)
                setattr(value, "subgraph", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link14"):
                    opp_val = getattr(item, "Link14", None)
                    
                    if opp_val == self:
                        setattr(item, "Link14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link14"):
                    opp_val = getattr(item, "Link14", None)
                    
                    setattr(item, "Link14", self)
                    

    @property
    def Node23(self):
        return self.__Node23

    @Node23.setter
    def Node23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Node__Node23", None)
        self.__Node23 = value
        
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
    def fsmgen_Node(self):
        return self.__fsmgen_Node

    @fsmgen_Node.setter
    def fsmgen_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Node__fsmgen_Node", None)
        self.__fsmgen_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmgen_StateGraphNode"):
                opp_val = getattr(old_value, "fsmgen_StateGraphNode", None)
                if opp_val == self:
                    setattr(old_value, "fsmgen_StateGraphNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmgen_StateGraphNode"):
                opp_val = getattr(value, "fsmgen_StateGraphNode", None)
                setattr(value, "fsmgen_StateGraphNode", self)

    @property
    def Node25(self):
        return self.__Node25

    @Node25.setter
    def Node25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Node__Node25", None)
        self.__Node25 = value
        
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
    def fsmgen_Node19(self):
        return self.__fsmgen_Node19

    @fsmgen_Node19.setter
    def fsmgen_Node19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Node__fsmgen_Node19", None)
        self.__fsmgen_Node19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmgen_CommonTrigger"):
                    opp_val = getattr(item, "fsmgen_CommonTrigger", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmgen_CommonTrigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmgen_CommonTrigger"):
                    opp_val = getattr(item, "fsmgen_CommonTrigger", None)
                    
                    setattr(item, "fsmgen_CommonTrigger", self)
                    

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Node__node", None)
        self.__node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph12"):
                opp_val = getattr(old_value, "Graph12", None)
                if opp_val == self:
                    setattr(old_value, "Graph12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph12"):
                opp_val = getattr(value, "Graph12", None)
                setattr(value, "Graph12", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph"):
                opp_val = getattr(old_value, "graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph"):
                opp_val = getattr(value, "graph", None)
                if opp_val is None:
                    setattr(value, "graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link16"):
                    opp_val = getattr(item, "Link16", None)
                    
                    if opp_val == self:
                        setattr(item, "Link16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link16"):
                    opp_val = getattr(item, "Link16", None)
                    
                    setattr(item, "Link16", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class fsmgen_ModelComponent:

    pass
class FSMGenElement:

    pass
class fsmgen_Graph(FSMGenElement):

    def __init__(self, fsmgen_Graph: "fsmgen_GraphContainer" = None, graph: set["fsmgen_Node"] = None, graph5: set["fsmgen_Link"] = None, fsmgen_Graph7: "fsmgen_StateGraph" = None, subgraph: "fsmgen_Node" = None, Graph: "fsmgen_Node" = None, Graph12: "fsmgen_Node" = None, Graph21: "fsmgen_Link" = None):
        self.fsmgen_Graph = fsmgen_Graph
        self.graph = graph if graph is not None else set()
        self.graph5 = graph5 if graph5 is not None else set()
        self.fsmgen_Graph7 = fsmgen_Graph7
        self.subgraph = subgraph
        self.Graph = Graph
        self.Graph12 = Graph12
        self.Graph21 = Graph21
        
    @property
    def subgraph(self):
        return self.__subgraph

    @subgraph.setter
    def subgraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Graph__subgraph", None)
        self.__subgraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node9"):
                opp_val = getattr(old_value, "Node9", None)
                if opp_val == self:
                    setattr(old_value, "Node9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node9"):
                opp_val = getattr(value, "Node9", None)
                setattr(value, "Node9", self)

    @property
    def Graph(self):
        return self.__Graph

    @Graph.setter
    def Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Graph__Graph", None)
        self.__Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

    @property
    def fsmgen_Graph(self):
        return self.__fsmgen_Graph

    @fsmgen_Graph.setter
    def fsmgen_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Graph__fsmgen_Graph", None)
        self.__fsmgen_Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmgen_GraphContainer"):
                opp_val = getattr(old_value, "fsmgen_GraphContainer", None)
                if opp_val == self:
                    setattr(old_value, "fsmgen_GraphContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmgen_GraphContainer"):
                opp_val = getattr(value, "fsmgen_GraphContainer", None)
                setattr(value, "fsmgen_GraphContainer", self)

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Graph__graph", None)
        self.__graph = value if value is not None else set()
        
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
    def Graph12(self):
        return self.__Graph12

    @Graph12.setter
    def Graph12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Graph__Graph12", None)
        self.__Graph12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node"):
                opp_val = getattr(old_value, "node", None)
                if opp_val == self:
                    setattr(old_value, "node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node"):
                opp_val = getattr(value, "node", None)
                setattr(value, "node", self)

    @property
    def Graph21(self):
        return self.__Graph21

    @Graph21.setter
    def Graph21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Graph__Graph21", None)
        self.__Graph21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "links"):
                opp_val = getattr(old_value, "links", None)
                if opp_val == self:
                    setattr(old_value, "links", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "links"):
                opp_val = getattr(value, "links", None)
                setattr(value, "links", self)

    @property
    def fsmgen_Graph7(self):
        return self.__fsmgen_Graph7

    @fsmgen_Graph7.setter
    def fsmgen_Graph7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Graph__fsmgen_Graph7", None)
        self.__fsmgen_Graph7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmgen_StateGraph"):
                opp_val = getattr(old_value, "fsmgen_StateGraph", None)
                if opp_val == self:
                    setattr(old_value, "fsmgen_StateGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmgen_StateGraph"):
                opp_val = getattr(value, "fsmgen_StateGraph", None)
                setattr(value, "fsmgen_StateGraph", self)

    @property
    def graph5(self):
        return self.__graph5

    @graph5.setter
    def graph5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_Graph__graph5", None)
        self.__graph5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link"):
                    opp_val = getattr(item, "Link", None)
                    
                    if opp_val == self:
                        setattr(item, "Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link"):
                    opp_val = getattr(item, "Link", None)
                    
                    setattr(item, "Link", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class fsmgen_GraphItem(FSMGenElement):

    def __init__(self, inherited: bool):
        self.inherited = inherited
        
    @property
    def inherited(self) -> bool:
        return self.__inherited

    @inherited.setter
    def inherited(self, inherited: bool):
        self.__inherited = inherited

class fsmgen_CommonTrigger(FSMGenElement):

    def __init__(self, hasGuard: bool, trigger: str, fsmgen_CommonTrigger: "fsmgen_Node" = None, fsmgen_CommonTrigger33: "fsmgen_EObject" = None, fsmgen_CommonTrigger36: "fsmgen_AbstractInterfaceItem" = None, fsmgen_CommonTrigger38: set["fsmgen_Link"] = None):
        self.hasGuard = hasGuard
        self.trigger = trigger
        self.fsmgen_CommonTrigger = fsmgen_CommonTrigger
        self.fsmgen_CommonTrigger33 = fsmgen_CommonTrigger33
        self.fsmgen_CommonTrigger36 = fsmgen_CommonTrigger36
        self.fsmgen_CommonTrigger38 = fsmgen_CommonTrigger38 if fsmgen_CommonTrigger38 is not None else set()
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def hasGuard(self) -> bool:
        return self.__hasGuard

    @hasGuard.setter
    def hasGuard(self, hasGuard: bool):
        self.__hasGuard = hasGuard

    @property
    def fsmgen_CommonTrigger36(self):
        return self.__fsmgen_CommonTrigger36

    @fsmgen_CommonTrigger36.setter
    def fsmgen_CommonTrigger36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_CommonTrigger__fsmgen_CommonTrigger36", None)
        self.__fsmgen_CommonTrigger36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmgen_AbstractInterfaceItem"):
                opp_val = getattr(old_value, "fsmgen_AbstractInterfaceItem", None)
                if opp_val == self:
                    setattr(old_value, "fsmgen_AbstractInterfaceItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmgen_AbstractInterfaceItem"):
                opp_val = getattr(value, "fsmgen_AbstractInterfaceItem", None)
                setattr(value, "fsmgen_AbstractInterfaceItem", self)

    @property
    def fsmgen_CommonTrigger(self):
        return self.__fsmgen_CommonTrigger

    @fsmgen_CommonTrigger.setter
    def fsmgen_CommonTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_CommonTrigger__fsmgen_CommonTrigger", None)
        self.__fsmgen_CommonTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmgen_Node19"):
                opp_val = getattr(old_value, "fsmgen_Node19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmgen_Node19"):
                opp_val = getattr(value, "fsmgen_Node19", None)
                if opp_val is None:
                    setattr(value, "fsmgen_Node19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsmgen_CommonTrigger38(self):
        return self.__fsmgen_CommonTrigger38

    @fsmgen_CommonTrigger38.setter
    def fsmgen_CommonTrigger38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_CommonTrigger__fsmgen_CommonTrigger38", None)
        self.__fsmgen_CommonTrigger38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmgen_Link39"):
                    opp_val = getattr(item, "fsmgen_Link39", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmgen_Link39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmgen_Link39"):
                    opp_val = getattr(item, "fsmgen_Link39", None)
                    
                    setattr(item, "fsmgen_Link39", self)
                    

    @property
    def fsmgen_CommonTrigger33(self):
        return self.__fsmgen_CommonTrigger33

    @fsmgen_CommonTrigger33.setter
    def fsmgen_CommonTrigger33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_CommonTrigger__fsmgen_CommonTrigger33", None)
        self.__fsmgen_CommonTrigger33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmgen_EObject34"):
                opp_val = getattr(old_value, "fsmgen_EObject34", None)
                if opp_val == self:
                    setattr(old_value, "fsmgen_EObject34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmgen_EObject34"):
                opp_val = getattr(value, "fsmgen_EObject34", None)
                setattr(value, "fsmgen_EObject34", self)

class fsmgen_GraphContainer(FSMGenElement):

    def __init__(self, initializedTriggersInStates: bool, initializedChainHeads: bool, initializedCommonData: bool, fsmgen_GraphContainer2: "fsmgen_ModelComponent" = None, fsmgen_GraphContainer: "fsmgen_Graph" = None):
        self.initializedTriggersInStates = initializedTriggersInStates
        self.initializedChainHeads = initializedChainHeads
        self.initializedCommonData = initializedCommonData
        self.fsmgen_GraphContainer2 = fsmgen_GraphContainer2
        self.fsmgen_GraphContainer = fsmgen_GraphContainer
        
    @property
    def initializedCommonData(self) -> bool:
        return self.__initializedCommonData

    @initializedCommonData.setter
    def initializedCommonData(self, initializedCommonData: bool):
        self.__initializedCommonData = initializedCommonData

    @property
    def initializedChainHeads(self) -> bool:
        return self.__initializedChainHeads

    @initializedChainHeads.setter
    def initializedChainHeads(self, initializedChainHeads: bool):
        self.__initializedChainHeads = initializedChainHeads

    @property
    def initializedTriggersInStates(self) -> bool:
        return self.__initializedTriggersInStates

    @initializedTriggersInStates.setter
    def initializedTriggersInStates(self, initializedTriggersInStates: bool):
        self.__initializedTriggersInStates = initializedTriggersInStates

    @property
    def fsmgen_GraphContainer(self):
        return self.__fsmgen_GraphContainer

    @fsmgen_GraphContainer.setter
    def fsmgen_GraphContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_GraphContainer__fsmgen_GraphContainer", None)
        self.__fsmgen_GraphContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmgen_Graph"):
                opp_val = getattr(old_value, "fsmgen_Graph", None)
                if opp_val == self:
                    setattr(old_value, "fsmgen_Graph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmgen_Graph"):
                opp_val = getattr(value, "fsmgen_Graph", None)
                setattr(value, "fsmgen_Graph", self)

    @property
    def fsmgen_GraphContainer2(self):
        return self.__fsmgen_GraphContainer2

    @fsmgen_GraphContainer2.setter
    def fsmgen_GraphContainer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmgen_GraphContainer__fsmgen_GraphContainer2", None)
        self.__fsmgen_GraphContainer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmgen_ModelComponent"):
                opp_val = getattr(old_value, "fsmgen_ModelComponent", None)
                if opp_val == self:
                    setattr(old_value, "fsmgen_ModelComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmgen_ModelComponent"):
                opp_val = getattr(value, "fsmgen_ModelComponent", None)
                setattr(value, "fsmgen_ModelComponent", self)
