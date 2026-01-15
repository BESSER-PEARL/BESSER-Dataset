from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ComplexNodeShape:

    pass
class DOT_PolygonNodeShape(ComplexNodeShape):

    def __init__(self, skew: int, distortion: int, isRegular: bool, orientation: int, sides: int):
        self.skew = skew
        self.distortion = distortion
        self.isRegular = isRegular
        self.orientation = orientation
        self.sides = sides
        
    @property
    def sides(self) -> int:
        return self.__sides

    @sides.setter
    def sides(self, sides: int):
        self.__sides = sides

    @property
    def isRegular(self) -> bool:
        return self.__isRegular

    @isRegular.setter
    def isRegular(self, isRegular: bool):
        self.__isRegular = isRegular

    @property
    def skew(self) -> int:
        return self.__skew

    @skew.setter
    def skew(self, skew: int):
        self.__skew = skew

    @property
    def distortion(self) -> int:
        return self.__distortion

    @distortion.setter
    def distortion(self, distortion: int):
        self.__distortion = distortion

    @property
    def orientation(self) -> int:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: int):
        self.__orientation = orientation

class NodeShape:

    pass
class DOT_ComplexNodeShape(NodeShape):

    pass
class DOT_PointNodeShape(NodeShape):

    pass
class DOT_SimpleNodeShape(NodeShape):

    pass
class Shape:

    pass
class DOT_ArrowShape(Shape):

    def __init__(self, clipping: str, isPlain: bool, size: int, DOT_ArrowShape: "DOT_DirectedArc" = None, DOT_ArrowShape50: "DOT_DirectedArc" = None):
        self.clipping = clipping
        self.isPlain = isPlain
        self.size = size
        self.DOT_ArrowShape = DOT_ArrowShape
        self.DOT_ArrowShape50 = DOT_ArrowShape50
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def isPlain(self) -> bool:
        return self.__isPlain

    @isPlain.setter
    def isPlain(self, isPlain: bool):
        self.__isPlain = isPlain

    @property
    def clipping(self) -> str:
        return self.__clipping

    @clipping.setter
    def clipping(self, clipping: str):
        self.__clipping = clipping

    @property
    def DOT_ArrowShape50(self):
        return self.__DOT_ArrowShape50

    @DOT_ArrowShape50.setter
    def DOT_ArrowShape50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_ArrowShape__DOT_ArrowShape50", None)
        self.__DOT_ArrowShape50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOT_DirectedArc49"):
                opp_val = getattr(old_value, "DOT_DirectedArc49", None)
                if opp_val == self:
                    setattr(old_value, "DOT_DirectedArc49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOT_DirectedArc49"):
                opp_val = getattr(value, "DOT_DirectedArc49", None)
                setattr(value, "DOT_DirectedArc49", self)

    @property
    def DOT_ArrowShape(self):
        return self.__DOT_ArrowShape

    @DOT_ArrowShape.setter
    def DOT_ArrowShape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_ArrowShape__DOT_ArrowShape", None)
        self.__DOT_ArrowShape = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOT_DirectedArc"):
                opp_val = getattr(old_value, "DOT_DirectedArc", None)
                if opp_val == self:
                    setattr(old_value, "DOT_DirectedArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOT_DirectedArc"):
                opp_val = getattr(value, "DOT_DirectedArc", None)
                setattr(value, "DOT_DirectedArc", self)

class Arc:

    pass
class DOT_UndirectedArc(Arc):

    pass
class DOT_DirectedArc(Arc):

    def __init__(self, tail_lp: float, head_lp: float, DOT_DirectedArc: "DOT_ArrowShape" = None, DOT_DirectedArc44: "DOT_Label" = None, DOT_DirectedArc46: "DOT_Label" = None, DOT_DirectedArc49: "DOT_ArrowShape" = None):
        self.tail_lp = tail_lp
        self.head_lp = head_lp
        self.DOT_DirectedArc = DOT_DirectedArc
        self.DOT_DirectedArc44 = DOT_DirectedArc44
        self.DOT_DirectedArc46 = DOT_DirectedArc46
        self.DOT_DirectedArc49 = DOT_DirectedArc49
        
    @property
    def tail_lp(self) -> float:
        return self.__tail_lp

    @tail_lp.setter
    def tail_lp(self, tail_lp: float):
        self.__tail_lp = tail_lp

    @property
    def head_lp(self) -> float:
        return self.__head_lp

    @head_lp.setter
    def head_lp(self, head_lp: float):
        self.__head_lp = head_lp

    @property
    def DOT_DirectedArc46(self):
        return self.__DOT_DirectedArc46

    @DOT_DirectedArc46.setter
    def DOT_DirectedArc46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_DirectedArc__DOT_DirectedArc46", None)
        self.__DOT_DirectedArc46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOT_Label47"):
                opp_val = getattr(old_value, "DOT_Label47", None)
                if opp_val == self:
                    setattr(old_value, "DOT_Label47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOT_Label47"):
                opp_val = getattr(value, "DOT_Label47", None)
                setattr(value, "DOT_Label47", self)

    @property
    def DOT_DirectedArc49(self):
        return self.__DOT_DirectedArc49

    @DOT_DirectedArc49.setter
    def DOT_DirectedArc49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_DirectedArc__DOT_DirectedArc49", None)
        self.__DOT_DirectedArc49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOT_ArrowShape50"):
                opp_val = getattr(old_value, "DOT_ArrowShape50", None)
                if opp_val == self:
                    setattr(old_value, "DOT_ArrowShape50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOT_ArrowShape50"):
                opp_val = getattr(value, "DOT_ArrowShape50", None)
                setattr(value, "DOT_ArrowShape50", self)

    @property
    def DOT_DirectedArc44(self):
        return self.__DOT_DirectedArc44

    @DOT_DirectedArc44.setter
    def DOT_DirectedArc44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_DirectedArc__DOT_DirectedArc44", None)
        self.__DOT_DirectedArc44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOT_Label"):
                opp_val = getattr(old_value, "DOT_Label", None)
                if opp_val == self:
                    setattr(old_value, "DOT_Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOT_Label"):
                opp_val = getattr(value, "DOT_Label", None)
                setattr(value, "DOT_Label", self)

    @property
    def DOT_DirectedArc(self):
        return self.__DOT_DirectedArc

    @DOT_DirectedArc.setter
    def DOT_DirectedArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_DirectedArc__DOT_DirectedArc", None)
        self.__DOT_DirectedArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOT_ArrowShape"):
                opp_val = getattr(old_value, "DOT_ArrowShape", None)
                if opp_val == self:
                    setattr(old_value, "DOT_ArrowShape", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOT_ArrowShape"):
                opp_val = getattr(value, "DOT_ArrowShape", None)
                setattr(value, "DOT_ArrowShape", self)

class DOT_RecordNodeShape(ComplexNodeShape):

    pass
class DOT_MNodeShape(ComplexNodeShape):

    pass
class DOT_NodeShape(Shape):

    pass
class Nodelike:

    pass
class DOT_Node(Nodelike):

    def __init__(self, fixedSize: bool, fontname: str, fontsize: int, height: int, width: int, DOT_Node: "DOT_NodeShape" = None):
        self.fixedSize = fixedSize
        self.fontname = fontname
        self.fontsize = fontsize
        self.height = height
        self.width = width
        self.DOT_Node = DOT_Node
        
    @property
    def fontsize(self) -> int:
        return self.__fontsize

    @fontsize.setter
    def fontsize(self, fontsize: int):
        self.__fontsize = fontsize

    @property
    def fontname(self) -> str:
        return self.__fontname

    @fontname.setter
    def fontname(self, fontname: str):
        self.__fontname = fontname

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def fixedSize(self) -> bool:
        return self.__fixedSize

    @fixedSize.setter
    def fixedSize(self, fixedSize: bool):
        self.__fixedSize = fixedSize

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def DOT_Node(self):
        return self.__DOT_Node

    @DOT_Node.setter
    def DOT_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Node__DOT_Node", None)
        self.__DOT_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOT_NodeShape"):
                opp_val = getattr(old_value, "DOT_NodeShape", None)
                if opp_val == self:
                    setattr(old_value, "DOT_NodeShape", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOT_NodeShape"):
                opp_val = getattr(value, "DOT_NodeShape", None)
                setattr(value, "DOT_NodeShape", self)

class GraphElement:

    pass
class DOT_Shape(GraphElement):

    def __init__(self, width: int, height: int, peripheries: int):
        self.width = width
        self.height = height
        self.peripheries = peripheries
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def peripheries(self) -> int:
        return self.__peripheries

    @peripheries.setter
    def peripheries(self, peripheries: int):
        self.__peripheries = peripheries

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

class DOT_Layer(GraphElement):

    def __init__(self, layerSeparator: str, layers: set["DOT_Nodelike"] = None, layers15: set["DOT_Arc"] = None, layers17: "DOT_Graph" = None, Layer: "DOT_Graph" = None, Layer37: "DOT_Arc" = None, Layer28: "DOT_Nodelike" = None):
        self.layerSeparator = layerSeparator
        self.layers = layers if layers is not None else set()
        self.layers15 = layers15 if layers15 is not None else set()
        self.layers17 = layers17
        self.Layer = Layer
        self.Layer37 = Layer37
        self.Layer28 = Layer28
        
    @property
    def layerSeparator(self) -> str:
        return self.__layerSeparator

    @layerSeparator.setter
    def layerSeparator(self, layerSeparator: str):
        self.__layerSeparator = layerSeparator

    @property
    def Layer37(self):
        return self.__Layer37

    @Layer37.setter
    def Layer37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Layer__Layer37", None)
        self.__Layer37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arcs"):
                opp_val = getattr(old_value, "arcs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arcs"):
                opp_val = getattr(value, "arcs", None)
                if opp_val is None:
                    setattr(value, "arcs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def layers(self):
        return self.__layers

    @layers.setter
    def layers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Layer__layers", None)
        self.__layers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Nodelike13"):
                    opp_val = getattr(item, "Nodelike13", None)
                    
                    if opp_val == self:
                        setattr(item, "Nodelike13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Nodelike13"):
                    opp_val = getattr(item, "Nodelike13", None)
                    
                    setattr(item, "Nodelike13", self)
                    

    @property
    def Layer(self):
        return self.__Layer

    @Layer.setter
    def Layer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Layer__Layer", None)
        self.__Layer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph11"):
                opp_val = getattr(old_value, "graph11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph11"):
                opp_val = getattr(value, "graph11", None)
                if opp_val is None:
                    setattr(value, "graph11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Layer28(self):
        return self.__Layer28

    @Layer28.setter
    def Layer28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Layer__Layer28", None)
        self.__Layer28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes27"):
                opp_val = getattr(old_value, "nodes27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes27"):
                opp_val = getattr(value, "nodes27", None)
                if opp_val is None:
                    setattr(value, "nodes27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def layers17(self):
        return self.__layers17

    @layers17.setter
    def layers17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Layer__layers17", None)
        self.__layers17 = value
        
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
    def layers15(self):
        return self.__layers15

    @layers15.setter
    def layers15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Layer__layers15", None)
        self.__layers15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    setattr(item, "Arc", self)
                    

class DOT_Nodelike(GraphElement):

    pass
class DOT_Graph(GraphElement):

    def __init__(self, type: str, rankDir: str, labeljust: str, labelloc: str, concentrate: bool, boundingBox: str, compound: bool, nodeSeparation: float, ordering: str, size: str, ratio: str, center: bool, Graph: "DOT_Layer" = None, graph: set["DOT_Nodelike"] = None, graph11: set["DOT_Layer"] = None, Graph25: "DOT_Nodelike" = None):
        self.type = type
        self.rankDir = rankDir
        self.labeljust = labeljust
        self.labelloc = labelloc
        self.concentrate = concentrate
        self.boundingBox = boundingBox
        self.compound = compound
        self.nodeSeparation = nodeSeparation
        self.ordering = ordering
        self.size = size
        self.ratio = ratio
        self.center = center
        self.Graph = Graph
        self.graph = graph if graph is not None else set()
        self.graph11 = graph11 if graph11 is not None else set()
        self.Graph25 = Graph25
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def labelloc(self) -> str:
        return self.__labelloc

    @labelloc.setter
    def labelloc(self, labelloc: str):
        self.__labelloc = labelloc

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def nodeSeparation(self) -> float:
        return self.__nodeSeparation

    @nodeSeparation.setter
    def nodeSeparation(self, nodeSeparation: float):
        self.__nodeSeparation = nodeSeparation

    @property
    def center(self) -> bool:
        return self.__center

    @center.setter
    def center(self, center: bool):
        self.__center = center

    @property
    def labeljust(self) -> str:
        return self.__labeljust

    @labeljust.setter
    def labeljust(self, labeljust: str):
        self.__labeljust = labeljust

    @property
    def compound(self) -> bool:
        return self.__compound

    @compound.setter
    def compound(self, compound: bool):
        self.__compound = compound

    @property
    def rankDir(self) -> str:
        return self.__rankDir

    @rankDir.setter
    def rankDir(self, rankDir: str):
        self.__rankDir = rankDir

    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def boundingBox(self) -> str:
        return self.__boundingBox

    @boundingBox.setter
    def boundingBox(self, boundingBox: str):
        self.__boundingBox = boundingBox

    @property
    def ratio(self) -> str:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: str):
        self.__ratio = ratio

    @property
    def concentrate(self) -> bool:
        return self.__concentrate

    @concentrate.setter
    def concentrate(self, concentrate: bool):
        self.__concentrate = concentrate

    @property
    def Graph(self):
        return self.__Graph

    @Graph.setter
    def Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Graph__Graph", None)
        self.__Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "layers17"):
                opp_val = getattr(old_value, "layers17", None)
                if opp_val == self:
                    setattr(old_value, "layers17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "layers17"):
                opp_val = getattr(value, "layers17", None)
                setattr(value, "layers17", self)

    @property
    def graph11(self):
        return self.__graph11

    @graph11.setter
    def graph11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Graph__graph11", None)
        self.__graph11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Layer"):
                    opp_val = getattr(item, "Layer", None)
                    
                    if opp_val == self:
                        setattr(item, "Layer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Layer"):
                    opp_val = getattr(item, "Layer", None)
                    
                    setattr(item, "Layer", self)
                    

    @property
    def Graph25(self):
        return self.__Graph25

    @Graph25.setter
    def Graph25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Graph__Graph25", None)
        self.__Graph25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes24"):
                opp_val = getattr(old_value, "nodes24", None)
                if opp_val == self:
                    setattr(old_value, "nodes24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes24"):
                opp_val = getattr(value, "nodes24", None)
                setattr(value, "nodes24", self)

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Graph__graph", None)
        self.__graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Nodelike"):
                    opp_val = getattr(item, "Nodelike", None)
                    
                    if opp_val == self:
                        setattr(item, "Nodelike", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Nodelike"):
                    opp_val = getattr(item, "Nodelike", None)
                    
                    setattr(item, "Nodelike", self)
                    

class DOT_SubGraph(Nodelike):

    def __init__(self, labelloc: str, SubGraph: "DOT_Nodelike" = None, owner: set["DOT_Nodelike"] = None):
        self.labelloc = labelloc
        self.SubGraph = SubGraph
        self.owner = owner if owner is not None else set()
        
    @property
    def labelloc(self) -> str:
        return self.__labelloc

    @labelloc.setter
    def labelloc(self, labelloc: str):
        self.__labelloc = labelloc

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_SubGraph__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Nodelike30"):
                    opp_val = getattr(item, "Nodelike30", None)
                    
                    if opp_val == self:
                        setattr(item, "Nodelike30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Nodelike30"):
                    opp_val = getattr(item, "Nodelike30", None)
                    
                    setattr(item, "Nodelike30", self)
                    

    @property
    def SubGraph(self):
        return self.__SubGraph

    @SubGraph.setter
    def SubGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_SubGraph__SubGraph", None)
        self.__SubGraph = value
        
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

class DOT_Arc(GraphElement):

    def __init__(self, constraint: bool, group: str, minlen: int, sameHead: str, sameTail: str, decorate: bool, Arc: "DOT_Layer" = None, Arc20: "DOT_Nodelike" = None, arcs: set["DOT_Layer"] = None, DOT_Arc: "DOT_Nodelike" = None, DOT_Arc40: "DOT_Nodelike" = None, Arc22: "DOT_Nodelike" = None, refers: "DOT_Nodelike" = None, referredBy: "DOT_Nodelike" = None):
        self.constraint = constraint
        self.group = group
        self.minlen = minlen
        self.sameHead = sameHead
        self.sameTail = sameTail
        self.decorate = decorate
        self.Arc = Arc
        self.Arc20 = Arc20
        self.arcs = arcs if arcs is not None else set()
        self.DOT_Arc = DOT_Arc
        self.DOT_Arc40 = DOT_Arc40
        self.Arc22 = Arc22
        self.refers = refers
        self.referredBy = referredBy
        
    @property
    def minlen(self) -> int:
        return self.__minlen

    @minlen.setter
    def minlen(self, minlen: int):
        self.__minlen = minlen

    @property
    def sameHead(self) -> str:
        return self.__sameHead

    @sameHead.setter
    def sameHead(self, sameHead: str):
        self.__sameHead = sameHead

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def constraint(self) -> bool:
        return self.__constraint

    @constraint.setter
    def constraint(self, constraint: bool):
        self.__constraint = constraint

    @property
    def sameTail(self) -> str:
        return self.__sameTail

    @sameTail.setter
    def sameTail(self, sameTail: str):
        self.__sameTail = sameTail

    @property
    def decorate(self) -> bool:
        return self.__decorate

    @decorate.setter
    def decorate(self, decorate: bool):
        self.__decorate = decorate

    @property
    def referredBy(self):
        return self.__referredBy

    @referredBy.setter
    def referredBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Arc__referredBy", None)
        self.__referredBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Nodelike35"):
                opp_val = getattr(old_value, "Nodelike35", None)
                if opp_val == self:
                    setattr(old_value, "Nodelike35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Nodelike35"):
                opp_val = getattr(value, "Nodelike35", None)
                setattr(value, "Nodelike35", self)

    @property
    def Arc22(self):
        return self.__Arc22

    @Arc22.setter
    def Arc22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Arc__Arc22", None)
        self.__Arc22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toNode"):
                opp_val = getattr(old_value, "toNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toNode"):
                opp_val = getattr(value, "toNode", None)
                if opp_val is None:
                    setattr(value, "toNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def refers(self):
        return self.__refers

    @refers.setter
    def refers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Arc__refers", None)
        self.__refers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Nodelike33"):
                opp_val = getattr(old_value, "Nodelike33", None)
                if opp_val == self:
                    setattr(old_value, "Nodelike33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Nodelike33"):
                opp_val = getattr(value, "Nodelike33", None)
                setattr(value, "Nodelike33", self)

    @property
    def DOT_Arc(self):
        return self.__DOT_Arc

    @DOT_Arc.setter
    def DOT_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Arc__DOT_Arc", None)
        self.__DOT_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOT_Nodelike"):
                opp_val = getattr(old_value, "DOT_Nodelike", None)
                if opp_val == self:
                    setattr(old_value, "DOT_Nodelike", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOT_Nodelike"):
                opp_val = getattr(value, "DOT_Nodelike", None)
                setattr(value, "DOT_Nodelike", self)

    @property
    def DOT_Arc40(self):
        return self.__DOT_Arc40

    @DOT_Arc40.setter
    def DOT_Arc40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Arc__DOT_Arc40", None)
        self.__DOT_Arc40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DOT_Nodelike41"):
                opp_val = getattr(old_value, "DOT_Nodelike41", None)
                if opp_val == self:
                    setattr(old_value, "DOT_Nodelike41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DOT_Nodelike41"):
                opp_val = getattr(value, "DOT_Nodelike41", None)
                setattr(value, "DOT_Nodelike41", self)

    @property
    def arcs(self):
        return self.__arcs

    @arcs.setter
    def arcs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Arc__arcs", None)
        self.__arcs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Layer37"):
                    opp_val = getattr(item, "Layer37", None)
                    
                    if opp_val == self:
                        setattr(item, "Layer37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Layer37"):
                    opp_val = getattr(item, "Layer37", None)
                    
                    setattr(item, "Layer37", self)
                    

    @property
    def Arc20(self):
        return self.__Arc20

    @Arc20.setter
    def Arc20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Arc__Arc20", None)
        self.__Arc20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fromNode"):
                opp_val = getattr(old_value, "fromNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fromNode"):
                opp_val = getattr(value, "fromNode", None)
                if opp_val is None:
                    setattr(value, "fromNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Arc__Arc", None)
        self.__Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "layers15"):
                opp_val = getattr(old_value, "layers15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "layers15"):
                opp_val = getattr(value, "layers15", None)
                if opp_val is None:
                    setattr(value, "layers15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DOT_Compartment(ABC):

    pass
class Label:

    pass
class DOT_ComplexLabel(Label):

    pass
class DOT_SimpleLabel(Label):

    def __init__(self, content: str):
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class DOT_GraphElement(ABC):

    def __init__(self, name: str, style: str, color: str, GraphElement: "DOT_Label" = None, element: "DOT_Label" = None):
        self.name = name
        self.style = style
        self.color = color
        self.GraphElement = GraphElement
        self.element = element
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def GraphElement(self):
        return self.__GraphElement

    @GraphElement.setter
    def GraphElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_GraphElement__GraphElement", None)
        self.__GraphElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "label"):
                opp_val = getattr(old_value, "label", None)
                if opp_val == self:
                    setattr(old_value, "label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "label"):
                opp_val = getattr(value, "label", None)
                setattr(value, "label", self)

    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_GraphElement__element", None)
        self.__element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Label"):
                opp_val = getattr(old_value, "Label", None)
                if opp_val == self:
                    setattr(old_value, "Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Label"):
                opp_val = getattr(value, "Label", None)
                setattr(value, "Label", self)

class DOT_Label(ABC):

    pass
class Compartment:

    pass
class DOT_SimpleCompartment(Compartment):

    def __init__(self, content: str):
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class DOT_HorizontalCompartment(Compartment):

    pass
class DOT_VerticalCompartment(Compartment):

    pass
class DOT_Anchor:

    def __init__(self, name: str, Anchor: "DOT_Compartment" = None, anchor: "DOT_Compartment" = None):
        self.name = name
        self.Anchor = Anchor
        self.anchor = anchor
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def anchor(self):
        return self.__anchor

    @anchor.setter
    def anchor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Anchor__anchor", None)
        self.__anchor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Compartment7"):
                opp_val = getattr(old_value, "Compartment7", None)
                if opp_val == self:
                    setattr(old_value, "Compartment7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Compartment7"):
                opp_val = getattr(value, "Compartment7", None)
                setattr(value, "Compartment7", self)

    @property
    def Anchor(self):
        return self.__Anchor

    @Anchor.setter
    def Anchor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DOT_Anchor__Anchor", None)
        self.__Anchor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if opp_val == self:
                    setattr(old_value, "source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                setattr(value, "source", self)
