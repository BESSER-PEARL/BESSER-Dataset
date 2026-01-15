####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
DOT_Anchor = Class(name="DOT::Anchor")
DOT_VerticalCompartment = Class(name="DOT::VerticalCompartment")
Compartment = Class(name="Compartment")
DOT_HorizontalCompartment = Class(name="DOT::HorizontalCompartment")
DOT_SimpleCompartment = Class(name="DOT::SimpleCompartment")
DOT_Label = Class(name="DOT::Label", is_abstract=True)
DOT_GraphElement = Class(name="DOT::GraphElement", is_abstract=True)
DOT_SimpleLabel = Class(name="DOT::SimpleLabel")
Label = Class(name="Label")
DOT_ComplexLabel = Class(name="DOT::ComplexLabel")
DOT_Compartment = Class(name="DOT::Compartment", is_abstract=True)
DOT_Arc = Class(name="DOT::Arc", is_abstract=True)
DOT_SubGraph = Class(name="DOT::SubGraph")
DOT_Graph = Class(name="DOT::Graph")
GraphElement = Class(name="GraphElement")
DOT_Nodelike = Class(name="DOT::Nodelike", is_abstract=True)
DOT_Layer = Class(name="DOT::Layer")
Nodelike = Class(name="Nodelike")
DOT_Node = Class(name="DOT::Node")
DOT_NodeShape = Class(name="DOT::NodeShape", is_abstract=True)
DOT_MNodeShape = Class(name="DOT::MNodeShape")
DOT_RecordNodeShape = Class(name="DOT::RecordNodeShape")
DOT_DirectedArc = Class(name="DOT::DirectedArc")
Arc = Class(name="Arc")
DOT_ArrowShape = Class(name="DOT::ArrowShape")
DOT_UndirectedArc = Class(name="DOT::UndirectedArc")
DOT_Shape = Class(name="DOT::Shape", is_abstract=True)
Shape = Class(name="Shape")
DOT_SimpleNodeShape = Class(name="DOT::SimpleNodeShape")
NodeShape = Class(name="NodeShape")
DOT_PointNodeShape = Class(name="DOT::PointNodeShape")
DOT_ComplexNodeShape = Class(name="DOT::ComplexNodeShape", is_abstract=True)
DOT_PolygonNodeShape = Class(name="DOT::PolygonNodeShape")
ComplexNodeShape = Class(name="ComplexNodeShape")

# DOT_Anchor class attributes and methods
DOT_Anchor_name: Property = Property(name="name", type=StringType)
DOT_Anchor.attributes={DOT_Anchor_name}

# DOT_VerticalCompartment class attributes and methods

# Compartment class attributes and methods

# DOT_HorizontalCompartment class attributes and methods

# DOT_SimpleCompartment class attributes and methods
DOT_SimpleCompartment_content: Property = Property(name="content", type=StringType)
DOT_SimpleCompartment.attributes={DOT_SimpleCompartment_content}

# DOT_Label class attributes and methods

# DOT_GraphElement class attributes and methods
DOT_GraphElement_name: Property = Property(name="name", type=StringType)
DOT_GraphElement_style: Property = Property(name="style", type=StringType)
DOT_GraphElement_color: Property = Property(name="color", type=StringType)
DOT_GraphElement.attributes={DOT_GraphElement_name, DOT_GraphElement_style, DOT_GraphElement_color}

# DOT_SimpleLabel class attributes and methods
DOT_SimpleLabel_content: Property = Property(name="content", type=StringType)
DOT_SimpleLabel.attributes={DOT_SimpleLabel_content}

# Label class attributes and methods

# DOT_ComplexLabel class attributes and methods

# DOT_Compartment class attributes and methods

# DOT_Arc class attributes and methods
DOT_Arc_constraint: Property = Property(name="constraint", type=BooleanType)
DOT_Arc_group: Property = Property(name="group", type=StringType)
DOT_Arc_minlen: Property = Property(name="minlen", type=IntegerType)
DOT_Arc_sameHead: Property = Property(name="sameHead", type=StringType)
DOT_Arc_sameTail: Property = Property(name="sameTail", type=StringType)
DOT_Arc_decorate: Property = Property(name="decorate", type=BooleanType)
DOT_Arc.attributes={DOT_Arc_minlen, DOT_Arc_sameHead, DOT_Arc_group, DOT_Arc_constraint, DOT_Arc_sameTail, DOT_Arc_decorate}

# DOT_SubGraph class attributes and methods
DOT_SubGraph_labelloc: Property = Property(name="labelloc", type=StringType)
DOT_SubGraph.attributes={DOT_SubGraph_labelloc}

# DOT_Graph class attributes and methods
DOT_Graph_type: Property = Property(name="type", type=StringType)
DOT_Graph_rankDir: Property = Property(name="rankDir", type=StringType)
DOT_Graph_labeljust: Property = Property(name="labeljust", type=StringType)
DOT_Graph_labelloc: Property = Property(name="labelloc", type=StringType)
DOT_Graph_concentrate: Property = Property(name="concentrate", type=BooleanType)
DOT_Graph_boundingBox: Property = Property(name="boundingBox", type=StringType)
DOT_Graph_compound: Property = Property(name="compound", type=BooleanType)
DOT_Graph_nodeSeparation: Property = Property(name="nodeSeparation", type=FloatType)
DOT_Graph_ordering: Property = Property(name="ordering", type=StringType)
DOT_Graph_size: Property = Property(name="size", type=StringType)
DOT_Graph_ratio: Property = Property(name="ratio", type=StringType)
DOT_Graph_center: Property = Property(name="center", type=BooleanType)
DOT_Graph.attributes={DOT_Graph_type, DOT_Graph_labelloc, DOT_Graph_size, DOT_Graph_nodeSeparation, DOT_Graph_center, DOT_Graph_labeljust, DOT_Graph_compound, DOT_Graph_rankDir, DOT_Graph_ordering, DOT_Graph_boundingBox, DOT_Graph_ratio, DOT_Graph_concentrate}

# GraphElement class attributes and methods

# DOT_Nodelike class attributes and methods

# DOT_Layer class attributes and methods
DOT_Layer_layerSeparator: Property = Property(name="layerSeparator", type=StringType)
DOT_Layer.attributes={DOT_Layer_layerSeparator}

# Nodelike class attributes and methods

# DOT_Node class attributes and methods
DOT_Node_fixedSize: Property = Property(name="fixedSize", type=BooleanType)
DOT_Node_fontname: Property = Property(name="fontname", type=StringType)
DOT_Node_fontsize: Property = Property(name="fontsize", type=IntegerType)
DOT_Node_height: Property = Property(name="height", type=IntegerType)
DOT_Node_width: Property = Property(name="width", type=IntegerType)
DOT_Node.attributes={DOT_Node_fontsize, DOT_Node_fontname, DOT_Node_width, DOT_Node_fixedSize, DOT_Node_height}

# DOT_NodeShape class attributes and methods

# DOT_MNodeShape class attributes and methods

# DOT_RecordNodeShape class attributes and methods

# DOT_DirectedArc class attributes and methods
DOT_DirectedArc_tail_lp: Property = Property(name="tail_lp", type=FloatType)
DOT_DirectedArc_head_lp: Property = Property(name="head_lp", type=FloatType)
DOT_DirectedArc.attributes={DOT_DirectedArc_tail_lp, DOT_DirectedArc_head_lp}

# Arc class attributes and methods

# DOT_ArrowShape class attributes and methods
DOT_ArrowShape_clipping: Property = Property(name="clipping", type=StringType)
DOT_ArrowShape_isPlain: Property = Property(name="isPlain", type=BooleanType)
DOT_ArrowShape_size: Property = Property(name="size", type=IntegerType)
DOT_ArrowShape.attributes={DOT_ArrowShape_size, DOT_ArrowShape_isPlain, DOT_ArrowShape_clipping}

# DOT_UndirectedArc class attributes and methods

# DOT_Shape class attributes and methods
DOT_Shape_width: Property = Property(name="width", type=IntegerType)
DOT_Shape_height: Property = Property(name="height", type=IntegerType)
DOT_Shape_peripheries: Property = Property(name="peripheries", type=IntegerType)
DOT_Shape.attributes={DOT_Shape_width, DOT_Shape_peripheries, DOT_Shape_height}

# Shape class attributes and methods

# DOT_SimpleNodeShape class attributes and methods

# NodeShape class attributes and methods

# DOT_PointNodeShape class attributes and methods

# DOT_ComplexNodeShape class attributes and methods

# DOT_PolygonNodeShape class attributes and methods
DOT_PolygonNodeShape_skew: Property = Property(name="skew", type=IntegerType)
DOT_PolygonNodeShape_distortion: Property = Property(name="distortion", type=IntegerType)
DOT_PolygonNodeShape_isRegular: Property = Property(name="isRegular", type=BooleanType)
DOT_PolygonNodeShape_orientation: Property = Property(name="orientation", type=IntegerType)
DOT_PolygonNodeShape_sides: Property = Property(name="sides", type=IntegerType)
DOT_PolygonNodeShape.attributes={DOT_PolygonNodeShape_sides, DOT_PolygonNodeShape_isRegular, DOT_PolygonNodeShape_skew, DOT_PolygonNodeShape_distortion, DOT_PolygonNodeShape_orientation}

# ComplexNodeShape class attributes and methods

# Relationships
compartments4: BinaryAssociation = BinaryAssociation(
    name="compartments4",
    ends={
        Property(name="DOT_Compartment", type=DOT_Compartment, multiplicity=Multiplicity(1, 1)),
        Property(name="DOT_Compartment3", type=DOT_Compartment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anchor5: BinaryAssociation = BinaryAssociation(
    name="anchor5",
    ends={
        Property(name="Anchor", type=DOT_Compartment, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=DOT_Anchor, multiplicity=Multiplicity(0, 1))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="Compartment7", type=DOT_Anchor, multiplicity=Multiplicity(1, 1)),
        Property(name="anchor", type=DOT_Compartment, multiplicity=Multiplicity(0, 1))
    }
)
element0: BinaryAssociation = BinaryAssociation(
    name="element0",
    ends={
        Property(name="GraphElement", type=DOT_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="label", type=DOT_GraphElement, multiplicity=Multiplicity(0, 1))
    }
)
compartments1: BinaryAssociation = BinaryAssociation(
    name="compartments1",
    ends={
        Property(name="Compartment", type=DOT_ComplexLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="complexLabel", type=DOT_Compartment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
complexLabel2: BinaryAssociation = BinaryAssociation(
    name="complexLabel2",
    ends={
        Property(name="ComplexLabel", type=DOT_Compartment, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments", type=DOT_ComplexLabel, multiplicity=Multiplicity(0, 1))
    }
)
label8: BinaryAssociation = BinaryAssociation(
    name="label8",
    ends={
        Property(name="Label", type=DOT_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="element", type=DOT_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodes12: BinaryAssociation = BinaryAssociation(
    name="nodes12",
    ends={
        Property(name="Nodelike13", type=DOT_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="layers", type=DOT_Nodelike, multiplicity=Multiplicity(0, 9999))
    }
)
arcs14: BinaryAssociation = BinaryAssociation(
    name="arcs14",
    ends={
        Property(name="Arc", type=DOT_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="layers15", type=DOT_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
graph16: BinaryAssociation = BinaryAssociation(
    name="graph16",
    ends={
        Property(name="Graph", type=DOT_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="layers17", type=DOT_Graph, multiplicity=Multiplicity(1, 1))
    }
)
owner18: BinaryAssociation = BinaryAssociation(
    name="owner18",
    ends={
        Property(name="SubGraph", type=DOT_Nodelike, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=DOT_SubGraph, multiplicity=Multiplicity(0, 1))
    }
)
refers19: BinaryAssociation = BinaryAssociation(
    name="refers19",
    ends={
        Property(name="Arc20", type=DOT_Nodelike, multiplicity=Multiplicity(1, 1)),
        Property(name="fromNode", type=DOT_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
nodes9: BinaryAssociation = BinaryAssociation(
    name="nodes9",
    ends={
        Property(name="Nodelike", type=DOT_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=DOT_Nodelike, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layers10: BinaryAssociation = BinaryAssociation(
    name="layers10",
    ends={
        Property(name="Layer", type=DOT_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph11", type=DOT_Layer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layers36: BinaryAssociation = BinaryAssociation(
    name="layers36",
    ends={
        Property(name="Layer37", type=DOT_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=DOT_Layer, multiplicity=Multiplicity(0, 9999))
    }
)
lhead38: BinaryAssociation = BinaryAssociation(
    name="lhead38",
    ends={
        Property(name="DOT_Nodelike", type=DOT_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="DOT_Arc", type=DOT_Nodelike, multiplicity=Multiplicity(0, 1))
    }
)
ltail39: BinaryAssociation = BinaryAssociation(
    name="ltail39",
    ends={
        Property(name="DOT_Nodelike41", type=DOT_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="DOT_Arc40", type=DOT_Nodelike, multiplicity=Multiplicity(0, 1))
    }
)
referredBy21: BinaryAssociation = BinaryAssociation(
    name="referredBy21",
    ends={
        Property(name="Arc22", type=DOT_Nodelike, multiplicity=Multiplicity(1, 1)),
        Property(name="toNode", type=DOT_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
graph23: BinaryAssociation = BinaryAssociation(
    name="graph23",
    ends={
        Property(name="Graph25", type=DOT_Nodelike, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes24", type=DOT_Graph, multiplicity=Multiplicity(0, 1))
    }
)
layers26: BinaryAssociation = BinaryAssociation(
    name="layers26",
    ends={
        Property(name="Layer28", type=DOT_Nodelike, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes27", type=DOT_Layer, multiplicity=Multiplicity(0, 9999))
    }
)
nodes29: BinaryAssociation = BinaryAssociation(
    name="nodes29",
    ends={
        Property(name="Nodelike30", type=DOT_SubGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=DOT_Nodelike, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shape31: BinaryAssociation = BinaryAssociation(
    name="shape31",
    ends={
        Property(name="DOT_NodeShape", type=DOT_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="DOT_Node", type=DOT_NodeShape, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromNode32: BinaryAssociation = BinaryAssociation(
    name="fromNode32",
    ends={
        Property(name="Nodelike33", type=DOT_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="refers", type=DOT_Nodelike, multiplicity=Multiplicity(1, 1))
    }
)
toNode34: BinaryAssociation = BinaryAssociation(
    name="toNode34",
    ends={
        Property(name="Nodelike35", type=DOT_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="referredBy", type=DOT_Nodelike, multiplicity=Multiplicity(1, 1))
    }
)
toplabel51: BinaryAssociation = BinaryAssociation(
    name="toplabel51",
    ends={
        Property(name="DOT_Label52", type=DOT_MNodeShape, multiplicity=Multiplicity(1, 1)),
        Property(name="DOT_MNodeShape", type=DOT_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bottomlabel53: BinaryAssociation = BinaryAssociation(
    name="bottomlabel53",
    ends={
        Property(name="DOT_Label55", type=DOT_MNodeShape, multiplicity=Multiplicity(1, 1)),
        Property(name="DOT_MNodeShape54", type=DOT_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrowHead42: BinaryAssociation = BinaryAssociation(
    name="arrowHead42",
    ends={
        Property(name="DOT_ArrowShape", type=DOT_DirectedArc, multiplicity=Multiplicity(1, 1)),
        Property(name="DOT_DirectedArc", type=DOT_ArrowShape, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headlabel43: BinaryAssociation = BinaryAssociation(
    name="headlabel43",
    ends={
        Property(name="DOT_Label", type=DOT_DirectedArc, multiplicity=Multiplicity(1, 1)),
        Property(name="DOT_DirectedArc44", type=DOT_Label, multiplicity=Multiplicity(0, 1))
    }
)
taillabel45: BinaryAssociation = BinaryAssociation(
    name="taillabel45",
    ends={
        Property(name="DOT_Label47", type=DOT_DirectedArc, multiplicity=Multiplicity(1, 1)),
        Property(name="DOT_DirectedArc46", type=DOT_Label, multiplicity=Multiplicity(0, 1))
    }
)
arrowTail48: BinaryAssociation = BinaryAssociation(
    name="arrowTail48",
    ends={
        Property(name="DOT_ArrowShape50", type=DOT_DirectedArc, multiplicity=Multiplicity(1, 1)),
        Property(name="DOT_DirectedArc49", type=DOT_ArrowShape, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_DOT_VerticalCompartment_Compartment = Generalization(general=Compartment, specific=DOT_VerticalCompartment)
gen_DOT_HorizontalCompartment_Compartment = Generalization(general=Compartment, specific=DOT_HorizontalCompartment)
gen_DOT_SimpleCompartment_Compartment = Generalization(general=Compartment, specific=DOT_SimpleCompartment)
gen_DOT_SimpleLabel_Label = Generalization(general=Label, specific=DOT_SimpleLabel)
gen_DOT_ComplexLabel_Label = Generalization(general=Label, specific=DOT_ComplexLabel)
gen_DOT_Nodelike_GraphElement = Generalization(general=GraphElement, specific=DOT_Nodelike)
gen_DOT_Graph_GraphElement = Generalization(general=GraphElement, specific=DOT_Graph)
gen_DOT_Layer_GraphElement = Generalization(general=GraphElement, specific=DOT_Layer)
gen_DOT_SubGraph_Nodelike = Generalization(general=Nodelike, specific=DOT_SubGraph)
gen_DOT_Node_Nodelike = Generalization(general=Nodelike, specific=DOT_Node)
gen_DOT_Arc_GraphElement = Generalization(general=GraphElement, specific=DOT_Arc)
gen_DOT_MNodeShape_ComplexNodeShape = Generalization(general=ComplexNodeShape, specific=DOT_MNodeShape)
gen_DOT_RecordNodeShape_ComplexNodeShape = Generalization(general=ComplexNodeShape, specific=DOT_RecordNodeShape)
gen_DOT_ArrowShape_Shape = Generalization(general=Shape, specific=DOT_ArrowShape)
gen_DOT_DirectedArc_Arc = Generalization(general=Arc, specific=DOT_DirectedArc)
gen_DOT_UndirectedArc_Arc = Generalization(general=Arc, specific=DOT_UndirectedArc)
gen_DOT_Shape_GraphElement = Generalization(general=GraphElement, specific=DOT_Shape)
gen_DOT_NodeShape_Shape = Generalization(general=Shape, specific=DOT_NodeShape)
gen_DOT_SimpleNodeShape_NodeShape = Generalization(general=NodeShape, specific=DOT_SimpleNodeShape)
gen_DOT_PointNodeShape_NodeShape = Generalization(general=NodeShape, specific=DOT_PointNodeShape)
gen_DOT_ComplexNodeShape_NodeShape = Generalization(general=NodeShape, specific=DOT_ComplexNodeShape)
gen_DOT_PolygonNodeShape_ComplexNodeShape = Generalization(general=ComplexNodeShape, specific=DOT_PolygonNodeShape)

# Domain Model
domain_model = DomainModel(
    name="DOT",
    types={DOT_Anchor, DOT_VerticalCompartment, Compartment, DOT_HorizontalCompartment, DOT_SimpleCompartment, DOT_Label, DOT_GraphElement, DOT_SimpleLabel, Label, DOT_ComplexLabel, DOT_Compartment, DOT_Arc, DOT_SubGraph, DOT_Graph, GraphElement, DOT_Nodelike, DOT_Layer, Nodelike, DOT_Node, DOT_NodeShape, DOT_MNodeShape, DOT_RecordNodeShape, DOT_DirectedArc, Arc, DOT_ArrowShape, DOT_UndirectedArc, DOT_Shape, Shape, DOT_SimpleNodeShape, NodeShape, DOT_PointNodeShape, DOT_ComplexNodeShape, DOT_PolygonNodeShape, ComplexNodeShape},
    associations={compartments4, anchor5, source6, element0, compartments1, complexLabel2, label8, nodes12, arcs14, graph16, owner18, refers19, nodes9, layers10, layers36, lhead38, ltail39, referredBy21, graph23, layers26, nodes29, shape31, fromNode32, toNode34, toplabel51, bottomlabel53, arrowHead42, headlabel43, taillabel45, arrowTail48},
    generalizations={gen_DOT_VerticalCompartment_Compartment, gen_DOT_HorizontalCompartment_Compartment, gen_DOT_SimpleCompartment_Compartment, gen_DOT_SimpleLabel_Label, gen_DOT_ComplexLabel_Label, gen_DOT_Nodelike_GraphElement, gen_DOT_Graph_GraphElement, gen_DOT_Layer_GraphElement, gen_DOT_SubGraph_Nodelike, gen_DOT_Node_Nodelike, gen_DOT_Arc_GraphElement, gen_DOT_MNodeShape_ComplexNodeShape, gen_DOT_RecordNodeShape_ComplexNodeShape, gen_DOT_ArrowShape_Shape, gen_DOT_DirectedArc_Arc, gen_DOT_UndirectedArc_Arc, gen_DOT_Shape_GraphElement, gen_DOT_NodeShape_Shape, gen_DOT_SimpleNodeShape_NodeShape, gen_DOT_PointNodeShape_NodeShape, gen_DOT_ComplexNodeShape_NodeShape, gen_DOT_PolygonNodeShape_ComplexNodeShape},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)