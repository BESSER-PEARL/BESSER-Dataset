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

# Enumerations
LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="SOLID"),
			EnumerationLiteral(name="DASH"),
			EnumerationLiteral(name="DOT"),
			EnumerationLiteral(name="DASHDOT"),
			EnumerationLiteral(name="DASHDOTDOT"),
			EnumerationLiteral(name="LINE_CUSTOM")
    }
)

RulerUnit: Enumeration = Enumeration(
    name="RulerUnit",
    literals={
            EnumerationLiteral(name="INCHES"),
			EnumerationLiteral(name="CENTIMETERS"),
			EnumerationLiteral(name="PIXELS")
    }
)

Alignment: Enumeration = Enumeration(
    name="Alignment",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="TOP"),
			EnumerationLiteral(name="BOTTOM")
    }
)

# Classes
di_Node = Class(name="di_Node", is_abstract=True)
View = Class(name="View")
di_CommentLink = Class(name="di_CommentLink")
di_View = Class(name="di_View", is_abstract=True)
di_EObject = Class(name="di_EObject")
di_Container = Class(name="di_Container", is_abstract=True)
di_Shape = Class(name="di_Shape")
di_Line = Class(name="di_Line", is_abstract=True)
di_Connector = Class(name="di_Connector")
di_Diagram = Class(name="di_Diagram")
Container = Class(name="Container")
di_Comment = Class(name="di_Comment")
di_Grid = Class(name="di_Grid")
Node = Class(name="Node")
di_Ruler = Class(name="di_Ruler")
di_GradientShape = Class(name="di_GradientShape")
Shape = Class(name="Shape")
Line = Class(name="Line")
di_Guide = Class(name="di_Guide")
di_ElementEntry = Class(name="di_ElementEntry")

# di_Node class attributes and methods
di_Node_allOutgoingLines: Property = Property(name="allOutgoingLines", type=StringType)
di_Node_allIncomingLines: Property = Property(name="allIncomingLines", type=StringType)
di_Node.attributes={di_Node_allIncomingLines, di_Node_allOutgoingLines}

# View class attributes and methods

# di_CommentLink class attributes and methods

# di_View class attributes and methods
di_View_label: Property = Property(name="label", type=StringType)
di_View_id: Property = Property(name="id", type=StringType)
di_View.attributes={di_View_label, di_View_id}

# di_EObject class attributes and methods

# di_Container class attributes and methods
di_Container_allLines: Property = Property(name="allLines", type=StringType)
di_Container_allShapes: Property = Property(name="allShapes", type=StringType)
di_Container.attributes={di_Container_allShapes, di_Container_allLines}

# di_Shape class attributes and methods
di_Shape_background: Property = Property(name="background", type=IntegerType)
di_Shape_foreground: Property = Property(name="foreground", type=IntegerType)
di_Shape_bounds: Property = Property(name="bounds", type=StringType)
di_Shape.attributes={di_Shape_background, di_Shape_foreground, di_Shape_bounds}

# di_Line class attributes and methods
di_Line_color: Property = Property(name="color", type=IntegerType)
di_Line_width: Property = Property(name="width", type=IntegerType)
di_Line_sourceAnchor: Property = Property(name="sourceAnchor", type=StringType)
di_Line_targetAnchor: Property = Property(name="targetAnchor", type=StringType)
di_Line_sourceNode: Property = Property(name="sourceNode", type=StringType)
di_Line_targetNode: Property = Property(name="targetNode", type=StringType)
di_Line_style: Property = Property(name="style", type=StringType)
di_Line_lineDash: Property = Property(name="lineDash", type=IntegerType)
di_Line.attributes={di_Line_targetNode, di_Line_targetAnchor, di_Line_sourceAnchor, di_Line_style, di_Line_lineDash, di_Line_width, di_Line_sourceNode, di_Line_color}

# di_Connector class attributes and methods

# di_Diagram class attributes and methods
di_Diagram_snapToGrid: Property = Property(name="snapToGrid", type=BooleanType)
di_Diagram_snapToGeometry: Property = Property(name="snapToGeometry", type=BooleanType)
di_Diagram_rulers: Property = Property(name="rulers", type=StringType)
di_Diagram.attributes={di_Diagram_snapToGeometry, di_Diagram_snapToGrid, di_Diagram_rulers}

# Container class attributes and methods

# di_Comment class attributes and methods

# di_Grid class attributes and methods
di_Grid_spacing: Property = Property(name="spacing", type=IntegerType)
di_Grid_style: Property = Property(name="style", type=StringType)
di_Grid_color: Property = Property(name="color", type=IntegerType)
di_Grid.attributes={di_Grid_spacing, di_Grid_color, di_Grid_style}

# Node class attributes and methods

# di_Ruler class attributes and methods
di_Ruler_unit: Property = Property(name="unit", type=StringType)
di_Ruler.attributes={di_Ruler_unit}

# di_GradientShape class attributes and methods
di_GradientShape_gradientColor: Property = Property(name="gradientColor", type=IntegerType)
di_GradientShape_verticalGradient: Property = Property(name="verticalGradient", type=BooleanType)
di_GradientShape_usingGradient: Property = Property(name="usingGradient", type=BooleanType)
di_GradientShape.attributes={di_GradientShape_verticalGradient, di_GradientShape_usingGradient, di_GradientShape_gradientColor}

# Shape class attributes and methods

# Line class attributes and methods

# di_Guide class attributes and methods
di_Guide_position: Property = Property(name="position", type=IntegerType)
di_Guide.attributes={di_Guide_position}

# di_ElementEntry class attributes and methods
di_ElementEntry_value: Property = Property(name="value", type=StringType)
di_ElementEntry.attributes={di_ElementEntry_value}

# Relationships
commentLinks1: BinaryAssociation = BinaryAssociation(
    name="commentLinks1",
    ends={
        Property(name="CommentLink", type=di_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=di_CommentLink, multiplicity=Multiplicity(0, 9999))
    }
)
element0: BinaryAssociation = BinaryAssociation(
    name="element0",
    ends={
        Property(name="di_EObject", type=di_View, multiplicity=Multiplicity(1, 1)),
        Property(name="di_View", type=di_EObject, multiplicity=Multiplicity(0, 1))
    }
)
incomingLines4: BinaryAssociation = BinaryAssociation(
    name="incomingLines4",
    ends={
        Property(name="target", type=di_Connector, multiplicity=Multiplicity(0, 9999)),
        Property(name="Connector5", type=di_Node, multiplicity=Multiplicity(1, 1))
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="di_Shape", type=di_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Container", type=di_Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lines7: BinaryAssociation = BinaryAssociation(
    name="lines7",
    ends={
        Property(name="di_Line", type=di_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Container8", type=di_Line, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingLines2: BinaryAssociation = BinaryAssociation(
    name="outgoingLines2",
    ends={
        Property(name="Connector", type=di_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source3", type=di_Connector, multiplicity=Multiplicity(0, 9999))
    }
)
comments9: BinaryAssociation = BinaryAssociation(
    name="comments9",
    ends={
        Property(name="di_Comment", type=di_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Diagram", type=di_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentLinks10: BinaryAssociation = BinaryAssociation(
    name="commentLinks10",
    ends={
        Property(name="di_CommentLink", type=di_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Diagram11", type=di_CommentLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
verticalRuler14: BinaryAssociation = BinaryAssociation(
    name="verticalRuler14",
    ends={
        Property(name="di_Ruler16", type=di_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Diagram15", type=di_Ruler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
grid17: BinaryAssociation = BinaryAssociation(
    name="grid17",
    ends={
        Property(name="di_Grid", type=di_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Diagram18", type=di_Grid, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
horizontalRuler12: BinaryAssociation = BinaryAssociation(
    name="horizontalRuler12",
    ends={
        Property(name="di_Ruler", type=di_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Diagram13", type=di_Ruler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="Node21", type=di_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingLines", type=di_Node, multiplicity=Multiplicity(0, 1))
    }
)
reverseElement22: BinaryAssociation = BinaryAssociation(
    name="reverseElement22",
    ends={
        Property(name="di_EObject23", type=di_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Connector", type=di_EObject, multiplicity=Multiplicity(0, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="Node", type=di_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingLines", type=di_Node, multiplicity=Multiplicity(0, 1))
    }
)
source27: BinaryAssociation = BinaryAssociation(
    name="source27",
    ends={
        Property(name="Node28", type=di_CommentLink, multiplicity=Multiplicity(1, 1)),
        Property(name="commentLinks", type=di_Node, multiplicity=Multiplicity(0, 1))
    }
)
inputs24: BinaryAssociation = BinaryAssociation(
    name="inputs24",
    ends={
        Property(name="CommentLink26", type=di_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="target25", type=di_CommentLink, multiplicity=Multiplicity(0, 9999))
    }
)
guides30: BinaryAssociation = BinaryAssociation(
    name="guides30",
    ends={
        Property(name="Guide", type=di_Ruler, multiplicity=Multiplicity(1, 1)),
        Property(name="ruler", type=di_Guide, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ruler31: BinaryAssociation = BinaryAssociation(
    name="ruler31",
    ends={
        Property(name="Ruler", type=di_Guide, multiplicity=Multiplicity(1, 1)),
        Property(name="guides", type=di_Ruler, multiplicity=Multiplicity(0, 1))
    }
)
target29: BinaryAssociation = BinaryAssociation(
    name="target29",
    ends={
        Property(name="Comment", type=di_CommentLink, multiplicity=Multiplicity(1, 1)),
        Property(name="inputs", type=di_Comment, multiplicity=Multiplicity(0, 1))
    }
)
elementMap32: BinaryAssociation = BinaryAssociation(
    name="elementMap32",
    ends={
        Property(name="di_ElementEntry", type=di_Guide, multiplicity=Multiplicity(1, 1)),
        Property(name="di_Guide", type=di_ElementEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key33: BinaryAssociation = BinaryAssociation(
    name="key33",
    ends={
        Property(name="di_View35", type=di_ElementEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="di_ElementEntry34", type=di_View, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_di_Node_View = Generalization(general=View, specific=di_Node)
gen_di_Container_View = Generalization(general=View, specific=di_Container)
gen_di_Diagram_Container = Generalization(general=Container, specific=di_Diagram)
gen_di_Shape_Container = Generalization(general=Container, specific=di_Shape)
gen_di_Shape_Node = Generalization(general=Node, specific=di_Shape)
gen_di_Line_Node = Generalization(general=Node, specific=di_Line)
gen_di_GradientShape_Shape = Generalization(general=Shape, specific=di_GradientShape)
gen_di_Connector_Line = Generalization(general=Line, specific=di_Connector)
gen_di_CommentLink_Line = Generalization(general=Line, specific=di_CommentLink)
gen_di_Comment_Shape = Generalization(general=Shape, specific=di_Comment)

# Domain Model
domain_model = DomainModel(
    name="di",
    types={di_Node, View, di_CommentLink, di_View, di_EObject, di_Container, di_Shape, di_Line, di_Connector, di_Diagram, Container, di_Comment, di_Grid, Node, di_Ruler, di_GradientShape, Shape, Line, di_Guide, di_ElementEntry, LineStyle, RulerUnit, Alignment},
    associations={commentLinks1, element0, incomingLines4, children6, lines7, outgoingLines2, comments9, commentLinks10, verticalRuler14, grid17, horizontalRuler12, source20, reverseElement22, target19, source27, inputs24, guides30, ruler31, target29, elementMap32, key33},
    generalizations={gen_di_Node_View, gen_di_Container_View, gen_di_Diagram_Container, gen_di_Shape_Container, gen_di_Shape_Node, gen_di_Line_Node, gen_di_GradientShape_Shape, gen_di_Connector_Line, gen_di_CommentLink_Line, gen_di_Comment_Shape},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)