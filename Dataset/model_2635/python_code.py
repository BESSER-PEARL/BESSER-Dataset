from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DShape(Enum):
    rectangle = "rectangle"
    vee = "vee"
    triangle = "triangle"
    dot = "dot"
    circle = "circle"
    roundedRect = "roundedRect"


############################################
# Definition of Classes
############################################

class DNode:

    pass
class DSimpleEdge:

    pass
class diagraph_DNavigationEdge(DSimpleEdge):

    pass
class diagraph_DLineEdge(DSimpleEdge):

    def __init__(self, arrows: str):
        self.arrows = arrows
        
    @property
    def arrows(self) -> str:
        return self.__arrows

    @arrows.setter
    def arrows(self, arrows: str):
        self.__arrows = arrows

class diagraph_EAttribute:

    pass
class diagraph_DPointOfView(DNode):

    pass
class DNestedEdge:

    pass
class diagraph_DAffixedEdge(DNestedEdge):

    pass
class diagraph_DCompartmentEdge(DNestedEdge):

    def __init__(self, partitionName: str, depth: int):
        self.partitionName = partitionName
        self.depth = depth
        
    @property
    def partitionName(self) -> str:
        return self.__partitionName

    @partitionName.setter
    def partitionName(self, partitionName: str):
        self.__partitionName = partitionName

    @property
    def depth(self) -> int:
        return self.__depth

    @depth.setter
    def depth(self, depth: int):
        self.__depth = depth

class DEdge:

    pass
class diagraph_DSimpleEdge(DEdge):

    pass
class diagraph_DOwnedElement(ABC):

    pass
class diagraph_DLabel:

    def __init__(self, propagated: bool, inferred: bool, abztract: bool, diagraph_DLabel: "diagraph_DLabeledElement" = None, diagraph_DLabel21: "diagraph_EAttribute" = None):
        self.propagated = propagated
        self.inferred = inferred
        self.abztract = abztract
        self.diagraph_DLabel = diagraph_DLabel
        self.diagraph_DLabel21 = diagraph_DLabel21
        
    @property
    def abztract(self) -> bool:
        return self.__abztract

    @abztract.setter
    def abztract(self, abztract: bool):
        self.__abztract = abztract

    @property
    def propagated(self) -> bool:
        return self.__propagated

    @propagated.setter
    def propagated(self, propagated: bool):
        self.__propagated = propagated

    @property
    def inferred(self) -> bool:
        return self.__inferred

    @inferred.setter
    def inferred(self, inferred: bool):
        self.__inferred = inferred

    @property
    def diagraph_DLabel21(self):
        return self.__diagraph_DLabel21

    @diagraph_DLabel21.setter
    def diagraph_DLabel21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DLabel__diagraph_DLabel21", None)
        self.__diagraph_DLabel21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_EAttribute"):
                opp_val = getattr(old_value, "diagraph_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "diagraph_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_EAttribute"):
                opp_val = getattr(value, "diagraph_EAttribute", None)
                setattr(value, "diagraph_EAttribute", self)

    @property
    def diagraph_DLabel(self):
        return self.__diagraph_DLabel

    @diagraph_DLabel.setter
    def diagraph_DLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DLabel__diagraph_DLabel", None)
        self.__diagraph_DLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_DLabeledElement14"):
                opp_val = getattr(old_value, "diagraph_DLabeledElement14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_DLabeledElement14"):
                opp_val = getattr(value, "diagraph_DLabeledElement14", None)
                if opp_val is None:
                    setattr(value, "diagraph_DLabeledElement14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class diagraph_EClass:

    pass
class diagraph_DGraph:

    def __init__(self, viewName: str, facade1: str, facade2: str, DGraph: "diagraph_DGraphElement" = None, graph: set["diagraph_DGraphElement"] = None, diagraph_DGraph: "diagraph_DPointOfView" = None, diagraph_DGraph18: "diagraph_DViewNavigation" = None):
        self.viewName = viewName
        self.facade1 = facade1
        self.facade2 = facade2
        self.DGraph = DGraph
        self.graph = graph if graph is not None else set()
        self.diagraph_DGraph = diagraph_DGraph
        self.diagraph_DGraph18 = diagraph_DGraph18
        
    @property
    def facade2(self) -> str:
        return self.__facade2

    @facade2.setter
    def facade2(self, facade2: str):
        self.__facade2 = facade2

    @property
    def viewName(self) -> str:
        return self.__viewName

    @viewName.setter
    def viewName(self, viewName: str):
        self.__viewName = viewName

    @property
    def facade1(self) -> str:
        return self.__facade1

    @facade1.setter
    def facade1(self, facade1: str):
        self.__facade1 = facade1

    @property
    def DGraph(self):
        return self.__DGraph

    @DGraph.setter
    def DGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DGraph__DGraph", None)
        self.__DGraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elements"):
                opp_val = getattr(old_value, "elements", None)
                if opp_val == self:
                    setattr(old_value, "elements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elements"):
                opp_val = getattr(value, "elements", None)
                setattr(value, "elements", self)

    @property
    def diagraph_DGraph(self):
        return self.__diagraph_DGraph

    @diagraph_DGraph.setter
    def diagraph_DGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DGraph__diagraph_DGraph", None)
        self.__diagraph_DGraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_DPointOfView"):
                opp_val = getattr(old_value, "diagraph_DPointOfView", None)
                if opp_val == self:
                    setattr(old_value, "diagraph_DPointOfView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_DPointOfView"):
                opp_val = getattr(value, "diagraph_DPointOfView", None)
                setattr(value, "diagraph_DPointOfView", self)

    @property
    def diagraph_DGraph18(self):
        return self.__diagraph_DGraph18

    @diagraph_DGraph18.setter
    def diagraph_DGraph18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DGraph__diagraph_DGraph18", None)
        self.__diagraph_DGraph18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_DViewNavigation"):
                opp_val = getattr(old_value, "diagraph_DViewNavigation", None)
                if opp_val == self:
                    setattr(old_value, "diagraph_DViewNavigation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_DViewNavigation"):
                opp_val = getattr(value, "diagraph_DViewNavigation", None)
                setattr(value, "diagraph_DViewNavigation", self)

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DGraph__graph", None)
        self.__graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DGraphElement"):
                    opp_val = getattr(item, "DGraphElement", None)
                    
                    if opp_val == self:
                        setattr(item, "DGraphElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DGraphElement"):
                    opp_val = getattr(item, "DGraphElement", None)
                    
                    setattr(item, "DGraphElement", self)
                    

class DLineEdge:

    pass
class diagraph_DReference(DLineEdge):

    pass
class DOwnedEdge:

    pass
class diagraph_DNestedEdge(DOwnedEdge):

    pass
class diagraph_DContainment:

    def __init__(self, name: str, DContainment: "diagraph_DNode" = None, diagraph_DContainment: "diagraph_DNestedEdge" = None, diagraph_DContainment25: set["diagraph_DNestedEdge"] = None, containments: "diagraph_DNode" = None):
        self.name = name
        self.DContainment = DContainment
        self.diagraph_DContainment = diagraph_DContainment
        self.diagraph_DContainment25 = diagraph_DContainment25 if diagraph_DContainment25 is not None else set()
        self.containments = containments
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def diagraph_DContainment(self):
        return self.__diagraph_DContainment

    @diagraph_DContainment.setter
    def diagraph_DContainment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DContainment__diagraph_DContainment", None)
        self.__diagraph_DContainment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_DNestedEdge"):
                opp_val = getattr(old_value, "diagraph_DNestedEdge", None)
                if opp_val == self:
                    setattr(old_value, "diagraph_DNestedEdge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_DNestedEdge"):
                opp_val = getattr(value, "diagraph_DNestedEdge", None)
                setattr(value, "diagraph_DNestedEdge", self)

    @property
    def containments(self):
        return self.__containments

    @containments.setter
    def containments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DContainment__containments", None)
        self.__containments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DNode23"):
                opp_val = getattr(old_value, "DNode23", None)
                if opp_val == self:
                    setattr(old_value, "DNode23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DNode23"):
                opp_val = getattr(value, "DNode23", None)
                setattr(value, "DNode23", self)

    @property
    def diagraph_DContainment25(self):
        return self.__diagraph_DContainment25

    @diagraph_DContainment25.setter
    def diagraph_DContainment25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DContainment__diagraph_DContainment25", None)
        self.__diagraph_DContainment25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagraph_DNestedEdge26"):
                    opp_val = getattr(item, "diagraph_DNestedEdge26", None)
                    
                    if opp_val == self:
                        setattr(item, "diagraph_DNestedEdge26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagraph_DNestedEdge26"):
                    opp_val = getattr(item, "diagraph_DNestedEdge26", None)
                    
                    setattr(item, "diagraph_DNestedEdge26", self)
                    

    @property
    def DContainment(self):
        return self.__DContainment

    @DContainment.setter
    def DContainment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DContainment__DContainment", None)
        self.__DContainment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node"):
                opp_val = getattr(old_value, "node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node"):
                opp_val = getattr(value, "node", None)
                if opp_val is None:
                    setattr(value, "node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class diagraph_DViewNavigation:

    def __init__(self, id: str, DViewNavigation: "diagraph_DNode" = None, viewNavigation: "diagraph_DNode" = None, diagraph_DViewNavigation: "diagraph_DGraph" = None):
        self.id = id
        self.DViewNavigation = DViewNavigation
        self.viewNavigation = viewNavigation
        self.diagraph_DViewNavigation = diagraph_DViewNavigation
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def diagraph_DViewNavigation(self):
        return self.__diagraph_DViewNavigation

    @diagraph_DViewNavigation.setter
    def diagraph_DViewNavigation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DViewNavigation__diagraph_DViewNavigation", None)
        self.__diagraph_DViewNavigation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_DGraph18"):
                opp_val = getattr(old_value, "diagraph_DGraph18", None)
                if opp_val == self:
                    setattr(old_value, "diagraph_DGraph18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_DGraph18"):
                opp_val = getattr(value, "diagraph_DGraph18", None)
                setattr(value, "diagraph_DGraph18", self)

    @property
    def DViewNavigation(self):
        return self.__DViewNavigation

    @DViewNavigation.setter
    def DViewNavigation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DViewNavigation__DViewNavigation", None)
        self.__DViewNavigation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "navigationSource"):
                opp_val = getattr(old_value, "navigationSource", None)
                if opp_val == self:
                    setattr(old_value, "navigationSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "navigationSource"):
                opp_val = getattr(value, "navigationSource", None)
                setattr(value, "navigationSource", self)

    @property
    def viewNavigation(self):
        return self.__viewNavigation

    @viewNavigation.setter
    def viewNavigation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DViewNavigation__viewNavigation", None)
        self.__viewNavigation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DNode"):
                opp_val = getattr(old_value, "DNode", None)
                if opp_val == self:
                    setattr(old_value, "DNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DNode"):
                opp_val = getattr(value, "DNode", None)
                setattr(value, "DNode", self)

class DOwnedElement:

    pass
class diagraph_DOwnedEdge(DOwnedElement, DEdge):

    pass
class DLabeledElement:

    pass
class diagraph_DLabeledEdge(DLabeledElement, DLineEdge, DOwnedEdge):

    pass
class diagraph_DGeneric(DLabeledElement):

    pass
class diagraph_ENamedElement:

    pass
class diagraph_DGraphElement(ABC):

    def __init__(self, name: str, icon: str, abztract: bool, diagraph_DGraphElement: "diagraph_ENamedElement" = None, elements: "diagraph_DGraph" = None, DGraphElement: "diagraph_DGraph" = None):
        self.name = name
        self.icon = icon
        self.abztract = abztract
        self.diagraph_DGraphElement = diagraph_DGraphElement
        self.elements = elements
        self.DGraphElement = DGraphElement
        
    @property
    def abztract(self) -> bool:
        return self.__abztract

    @abztract.setter
    def abztract(self, abztract: bool):
        self.__abztract = abztract

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def DGraphElement(self):
        return self.__DGraphElement

    @DGraphElement.setter
    def DGraphElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DGraphElement__DGraphElement", None)
        self.__DGraphElement = value
        
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
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DGraphElement__elements", None)
        self.__elements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DGraph"):
                opp_val = getattr(old_value, "DGraph", None)
                if opp_val == self:
                    setattr(old_value, "DGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DGraph"):
                opp_val = getattr(value, "DGraph", None)
                setattr(value, "DGraph", self)

    @property
    def diagraph_DGraphElement(self):
        return self.__diagraph_DGraphElement

    @diagraph_DGraphElement.setter
    def diagraph_DGraphElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DGraphElement__diagraph_DGraphElement", None)
        self.__diagraph_DGraphElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_ENamedElement"):
                opp_val = getattr(old_value, "diagraph_ENamedElement", None)
                if opp_val == self:
                    setattr(old_value, "diagraph_ENamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_ENamedElement"):
                opp_val = getattr(value, "diagraph_ENamedElement", None)
                setattr(value, "diagraph_ENamedElement", self)

class diagraph_EReference:

    pass
class diagraph_DNode(DLabeledElement, DOwnedElement):

    def __init__(self, shape: str, layout: bool, navigationLink: str, diagraph_DNode: "diagraph_DEdge" = None, navigationSource: "diagraph_DViewNavigation" = None, node: set["diagraph_DContainment"] = None, diagraph_DNode16: "diagraph_DOwnedElement" = None, DNode: "diagraph_DViewNavigation" = None, diagraph_DNode28: "diagraph_DSimpleEdge" = None, DNode23: "diagraph_DContainment" = None):
        self.shape = shape
        self.layout = layout
        self.navigationLink = navigationLink
        self.diagraph_DNode = diagraph_DNode
        self.navigationSource = navigationSource
        self.node = node if node is not None else set()
        self.diagraph_DNode16 = diagraph_DNode16
        self.DNode = DNode
        self.diagraph_DNode28 = diagraph_DNode28
        self.DNode23 = DNode23
        
    @property
    def navigationLink(self) -> str:
        return self.__navigationLink

    @navigationLink.setter
    def navigationLink(self, navigationLink: str):
        self.__navigationLink = navigationLink

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def layout(self) -> bool:
        return self.__layout

    @layout.setter
    def layout(self, layout: bool):
        self.__layout = layout

    @property
    def navigationSource(self):
        return self.__navigationSource

    @navigationSource.setter
    def navigationSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DNode__navigationSource", None)
        self.__navigationSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DViewNavigation"):
                opp_val = getattr(old_value, "DViewNavigation", None)
                if opp_val == self:
                    setattr(old_value, "DViewNavigation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DViewNavigation"):
                opp_val = getattr(value, "DViewNavigation", None)
                setattr(value, "DViewNavigation", self)

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DNode__node", None)
        self.__node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DContainment"):
                    opp_val = getattr(item, "DContainment", None)
                    
                    if opp_val == self:
                        setattr(item, "DContainment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DContainment"):
                    opp_val = getattr(item, "DContainment", None)
                    
                    setattr(item, "DContainment", self)
                    

    @property
    def diagraph_DNode28(self):
        return self.__diagraph_DNode28

    @diagraph_DNode28.setter
    def diagraph_DNode28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DNode__diagraph_DNode28", None)
        self.__diagraph_DNode28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_DSimpleEdge"):
                opp_val = getattr(old_value, "diagraph_DSimpleEdge", None)
                if opp_val == self:
                    setattr(old_value, "diagraph_DSimpleEdge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_DSimpleEdge"):
                opp_val = getattr(value, "diagraph_DSimpleEdge", None)
                setattr(value, "diagraph_DSimpleEdge", self)

    @property
    def DNode(self):
        return self.__DNode

    @DNode.setter
    def DNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DNode__DNode", None)
        self.__DNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewNavigation"):
                opp_val = getattr(old_value, "viewNavigation", None)
                if opp_val == self:
                    setattr(old_value, "viewNavigation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewNavigation"):
                opp_val = getattr(value, "viewNavigation", None)
                setattr(value, "viewNavigation", self)

    @property
    def diagraph_DNode(self):
        return self.__diagraph_DNode

    @diagraph_DNode.setter
    def diagraph_DNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DNode__diagraph_DNode", None)
        self.__diagraph_DNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_DEdge"):
                opp_val = getattr(old_value, "diagraph_DEdge", None)
                if opp_val == self:
                    setattr(old_value, "diagraph_DEdge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_DEdge"):
                opp_val = getattr(value, "diagraph_DEdge", None)
                setattr(value, "diagraph_DEdge", self)

    @property
    def diagraph_DNode16(self):
        return self.__diagraph_DNode16

    @diagraph_DNode16.setter
    def diagraph_DNode16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DNode__diagraph_DNode16", None)
        self.__diagraph_DNode16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_DOwnedElement"):
                opp_val = getattr(old_value, "diagraph_DOwnedElement", None)
                if opp_val == self:
                    setattr(old_value, "diagraph_DOwnedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_DOwnedElement"):
                opp_val = getattr(value, "diagraph_DOwnedElement", None)
                setattr(value, "diagraph_DOwnedElement", self)

    @property
    def DNode23(self):
        return self.__DNode23

    @DNode23.setter
    def DNode23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DNode__DNode23", None)
        self.__DNode23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containments"):
                opp_val = getattr(old_value, "containments", None)
                if opp_val == self:
                    setattr(old_value, "containments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containments"):
                opp_val = getattr(value, "containments", None)
                setattr(value, "containments", self)

class DGraphElement:

    pass
class diagraph_DLabeledElement(DGraphElement):

    def __init__(self, labls: str, expression: str, diagraph_DLabeledElement: "diagraph_EClass" = None, diagraph_DLabeledElement14: set["diagraph_DLabel"] = None):
        self.labls = labls
        self.expression = expression
        self.diagraph_DLabeledElement = diagraph_DLabeledElement
        self.diagraph_DLabeledElement14 = diagraph_DLabeledElement14 if diagraph_DLabeledElement14 is not None else set()
        
    @property
    def labls(self) -> str:
        return self.__labls

    @labls.setter
    def labls(self, labls: str):
        self.__labls = labls

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def diagraph_DLabeledElement(self):
        return self.__diagraph_DLabeledElement

    @diagraph_DLabeledElement.setter
    def diagraph_DLabeledElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DLabeledElement__diagraph_DLabeledElement", None)
        self.__diagraph_DLabeledElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_EClass"):
                opp_val = getattr(old_value, "diagraph_EClass", None)
                if opp_val == self:
                    setattr(old_value, "diagraph_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_EClass"):
                opp_val = getattr(value, "diagraph_EClass", None)
                setattr(value, "diagraph_EClass", self)

    @property
    def diagraph_DLabeledElement14(self):
        return self.__diagraph_DLabeledElement14

    @diagraph_DLabeledElement14.setter
    def diagraph_DLabeledElement14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DLabeledElement__diagraph_DLabeledElement14", None)
        self.__diagraph_DLabeledElement14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagraph_DLabel"):
                    opp_val = getattr(item, "diagraph_DLabel", None)
                    
                    if opp_val == self:
                        setattr(item, "diagraph_DLabel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagraph_DLabel"):
                    opp_val = getattr(item, "diagraph_DLabel", None)
                    
                    setattr(item, "diagraph_DLabel", self)
                    

class diagraph_DEdge(DGraphElement):

    def __init__(self, propagated: bool, diagraph_DEdge: "diagraph_DNode" = None, diagraph_DEdge2: "diagraph_EReference" = None):
        self.propagated = propagated
        self.diagraph_DEdge = diagraph_DEdge
        self.diagraph_DEdge2 = diagraph_DEdge2
        
    @property
    def propagated(self) -> bool:
        return self.__propagated

    @propagated.setter
    def propagated(self, propagated: bool):
        self.__propagated = propagated

    @property
    def diagraph_DEdge2(self):
        return self.__diagraph_DEdge2

    @diagraph_DEdge2.setter
    def diagraph_DEdge2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DEdge__diagraph_DEdge2", None)
        self.__diagraph_DEdge2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_EReference"):
                opp_val = getattr(old_value, "diagraph_EReference", None)
                if opp_val == self:
                    setattr(old_value, "diagraph_EReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_EReference"):
                opp_val = getattr(value, "diagraph_EReference", None)
                setattr(value, "diagraph_EReference", self)

    @property
    def diagraph_DEdge(self):
        return self.__diagraph_DEdge

    @diagraph_DEdge.setter
    def diagraph_DEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagraph_DEdge__diagraph_DEdge", None)
        self.__diagraph_DEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagraph_DNode"):
                opp_val = getattr(old_value, "diagraph_DNode", None)
                if opp_val == self:
                    setattr(old_value, "diagraph_DNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagraph_DNode"):
                opp_val = getattr(value, "diagraph_DNode", None)
                setattr(value, "diagraph_DNode", self)
