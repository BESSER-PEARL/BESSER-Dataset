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
RoutingStyle: Enumeration = Enumeration(
    name="RoutingStyle",
    literals={
            EnumerationLiteral(name="Straight"),
			EnumerationLiteral(name="Manhattan"),
			EnumerationLiteral(name="Tree")
    }
)

FontFormat: Enumeration = Enumeration(
    name="FontFormat",
    literals={
            EnumerationLiteral(name="normal"),
			EnumerationLiteral(name="italic"),
			EnumerationLiteral(name="bold"),
			EnumerationLiteral(name="bold_italic")
    }
)

LabelPosition: Enumeration = Enumeration(
    name="LabelPosition",
    literals={
            EnumerationLiteral(name="border"),
			EnumerationLiteral(name="node")
    }
)

LabelAlignment: Enumeration = Enumeration(
    name="LabelAlignment",
    literals={
            EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

AlignmentKind: Enumeration = Enumeration(
    name="AlignmentKind",
    literals={
            EnumerationLiteral(name="VERTICAL"),
			EnumerationLiteral(name="HORIZONTAL"),
			EnumerationLiteral(name="SQUARE")
    }
)

BundledImageShape: Enumeration = Enumeration(
    name="BundledImageShape",
    literals={
            EnumerationLiteral(name="square"),
			EnumerationLiteral(name="stroke"),
			EnumerationLiteral(name="triangle"),
			EnumerationLiteral(name="dot"),
			EnumerationLiteral(name="ring")
    }
)

ContainerShape: Enumeration = Enumeration(
    name="ContainerShape",
    literals={
            EnumerationLiteral(name="parallelogram")
    }
)

BackgroundStyle: Enumeration = Enumeration(
    name="BackgroundStyle",
    literals={
            EnumerationLiteral(name="GradientTopToBottom"),
			EnumerationLiteral(name="GradientLeftToRight"),
			EnumerationLiteral(name="Liquid")
    }
)

# Classes
migrationmodeler_Diagram = Class(name="migrationmodeler::Diagram")
migrationmodeler_Edge = Class(name="migrationmodeler::Edge")
migrationmodeler_Filter = Class(name="migrationmodeler::Filter")
migrationmodeler_Layer = Class(name="migrationmodeler::Layer")
migrationmodeler_GraphicalElement = Class(name="migrationmodeler::GraphicalElement", is_abstract=True)
migrationmodeler_AbstractNode = Class(name="migrationmodeler::AbstractNode", is_abstract=True)
GraphicalElement = Class(name="GraphicalElement")
AbstractNode = Class(name="AbstractNode")
migrationmodeler_NodeRepresentation = Class(name="migrationmodeler::NodeRepresentation")
migrationmodeler_Bordered = Class(name="migrationmodeler::Bordered")
migrationmodeler_BorderedRepresentation = Class(name="migrationmodeler::BorderedRepresentation")
migrationmodeler_ContainerRepresentation = Class(name="migrationmodeler::ContainerRepresentation")
migrationmodeler_EdgeRepresentation = Class(name="migrationmodeler::EdgeRepresentation")
migrationmodeler_AbstractRepresentation = Class(name="migrationmodeler::AbstractRepresentation", is_abstract=True)
migrationmodeler_Layout = Class(name="migrationmodeler::Layout")
Representation = Class(name="Representation")
migrationmodeler_Container = Class(name="migrationmodeler::Container")
migrationmodeler_Node = Class(name="migrationmodeler::Node")
migrationmodeler_Point = Class(name="migrationmodeler::Point")
migrationmodeler_EdgeStyle = Class(name="migrationmodeler::EdgeStyle")
migrationmodeler_AbstractNodeRepresentation = Class(name="migrationmodeler::AbstractNodeRepresentation", is_abstract=True)
migrationmodeler_NodeStyle = Class(name="migrationmodeler::NodeStyle")
AbstractNodeRepresentation = Class(name="AbstractNodeRepresentation")
migrationmodeler_ContainerStyle = Class(name="migrationmodeler::ContainerStyle")
migrationmodeler_Color = Class(name="migrationmodeler::Color")
migrationmodeler_BasicLabelStyle = Class(name="migrationmodeler::BasicLabelStyle")
AbstractRepresentation = Class(name="AbstractRepresentation")
migrationmodeler_TestCase = Class(name="migrationmodeler::TestCase")
migrationmodeler_Representation = Class(name="migrationmodeler::Representation", is_abstract=True)
migrationmodeler_BorderedStyle = Class(name="migrationmodeler::BorderedStyle")
LabelStyle = Class(name="LabelStyle")
BorderedStyle = Class(name="BorderedStyle")
migrationmodeler_Dot = Class(name="migrationmodeler::Dot")
NodeStyle = Class(name="NodeStyle")
migrationmodeler_GaugeSection = Class(name="migrationmodeler::GaugeSection")
migrationmodeler_FlatContainerStyle = Class(name="migrationmodeler::FlatContainerStyle")
ContainerStyle = Class(name="ContainerStyle")
migrationmodeler_ShapeContainerStyle = Class(name="migrationmodeler::ShapeContainerStyle")
migrationmodeler_LabelStyle = Class(name="migrationmodeler::LabelStyle")
BasicLabelStyle = Class(name="BasicLabelStyle")
migrationmodeler_Square = Class(name="migrationmodeler::Square")
migrationmodeler_Ellipse = Class(name="migrationmodeler::Ellipse")
migrationmodeler_Lozenge = Class(name="migrationmodeler::Lozenge")
migrationmodeler_BundledImage = Class(name="migrationmodeler::BundledImage")
migrationmodeler_GaugeCompositeStyle = Class(name="migrationmodeler::GaugeCompositeStyle")
migrationmodeler_Note = Class(name="migrationmodeler::Note")
migrationmodeler_WorkspaceImage = Class(name="migrationmodeler::WorkspaceImage")

# migrationmodeler_Diagram class attributes and methods

# migrationmodeler_Edge class attributes and methods

# migrationmodeler_Filter class attributes and methods
migrationmodeler_Filter_id: Property = Property(name="id", type=StringType)
migrationmodeler_Filter_activated: Property = Property(name="activated", type=BooleanType)
migrationmodeler_Filter.attributes={migrationmodeler_Filter_activated, migrationmodeler_Filter_id}

# migrationmodeler_Layer class attributes and methods
migrationmodeler_Layer_id: Property = Property(name="id", type=StringType)
migrationmodeler_Layer_activated: Property = Property(name="activated", type=BooleanType)
migrationmodeler_Layer.attributes={migrationmodeler_Layer_activated, migrationmodeler_Layer_id}

# migrationmodeler_GraphicalElement class attributes and methods
migrationmodeler_GraphicalElement_id: Property = Property(name="id", type=StringType)
migrationmodeler_GraphicalElement.attributes={migrationmodeler_GraphicalElement_id}

# migrationmodeler_AbstractNode class attributes and methods

# GraphicalElement class attributes and methods

# AbstractNode class attributes and methods

# migrationmodeler_NodeRepresentation class attributes and methods

# migrationmodeler_Bordered class attributes and methods

# migrationmodeler_BorderedRepresentation class attributes and methods

# migrationmodeler_ContainerRepresentation class attributes and methods
migrationmodeler_ContainerRepresentation_autoSized: Property = Property(name="autoSized", type=BooleanType)
migrationmodeler_ContainerRepresentation.attributes={migrationmodeler_ContainerRepresentation_autoSized}

# migrationmodeler_EdgeRepresentation class attributes and methods

# migrationmodeler_AbstractRepresentation class attributes and methods
migrationmodeler_AbstractRepresentation_mappingId: Property = Property(name="mappingId", type=StringType)
migrationmodeler_AbstractRepresentation_displayed: Property = Property(name="displayed", type=BooleanType)
migrationmodeler_AbstractRepresentation_hidden: Property = Property(name="hidden", type=BooleanType)
migrationmodeler_AbstractRepresentation_pinned: Property = Property(name="pinned", type=BooleanType)
migrationmodeler_AbstractRepresentation.attributes={migrationmodeler_AbstractRepresentation_displayed, migrationmodeler_AbstractRepresentation_mappingId, migrationmodeler_AbstractRepresentation_hidden, migrationmodeler_AbstractRepresentation_pinned}

# migrationmodeler_Layout class attributes and methods
migrationmodeler_Layout_x: Property = Property(name="x", type=IntegerType)
migrationmodeler_Layout_y: Property = Property(name="y", type=IntegerType)
migrationmodeler_Layout_width: Property = Property(name="width", type=IntegerType)
migrationmodeler_Layout_height: Property = Property(name="height", type=IntegerType)
migrationmodeler_Layout.attributes={migrationmodeler_Layout_height, migrationmodeler_Layout_width, migrationmodeler_Layout_y, migrationmodeler_Layout_x}

# Representation class attributes and methods

# migrationmodeler_Container class attributes and methods

# migrationmodeler_Node class attributes and methods

# migrationmodeler_Point class attributes and methods
migrationmodeler_Point_x: Property = Property(name="x", type=IntegerType)
migrationmodeler_Point_y: Property = Property(name="y", type=IntegerType)
migrationmodeler_Point.attributes={migrationmodeler_Point_x, migrationmodeler_Point_y}

# migrationmodeler_EdgeStyle class attributes and methods
migrationmodeler_EdgeStyle_routingStyle: Property = Property(name="routingStyle", type=StringType)
migrationmodeler_EdgeStyle.attributes={migrationmodeler_EdgeStyle_routingStyle}

# migrationmodeler_AbstractNodeRepresentation class attributes and methods

# migrationmodeler_NodeStyle class attributes and methods
migrationmodeler_NodeStyle_labelPosition: Property = Property(name="labelPosition", type=StringType)
migrationmodeler_NodeStyle_hideLabelByDefault: Property = Property(name="hideLabelByDefault", type=BooleanType)
migrationmodeler_NodeStyle.attributes={migrationmodeler_NodeStyle_labelPosition, migrationmodeler_NodeStyle_hideLabelByDefault}

# AbstractNodeRepresentation class attributes and methods

# migrationmodeler_ContainerStyle class attributes and methods

# migrationmodeler_Color class attributes and methods
migrationmodeler_Color_red: Property = Property(name="red", type=IntegerType)
migrationmodeler_Color_green: Property = Property(name="green", type=IntegerType)
migrationmodeler_Color_blue: Property = Property(name="blue", type=IntegerType)
migrationmodeler_Color.attributes={migrationmodeler_Color_red, migrationmodeler_Color_green, migrationmodeler_Color_blue}

# migrationmodeler_BasicLabelStyle class attributes and methods
migrationmodeler_BasicLabelStyle_labelSize: Property = Property(name="labelSize", type=IntegerType)
migrationmodeler_BasicLabelStyle_labelFormat: Property = Property(name="labelFormat", type=StringType)
migrationmodeler_BasicLabelStyle_showIcon: Property = Property(name="showIcon", type=BooleanType)
migrationmodeler_BasicLabelStyle_iconPath: Property = Property(name="iconPath", type=StringType)
migrationmodeler_BasicLabelStyle.attributes={migrationmodeler_BasicLabelStyle_showIcon, migrationmodeler_BasicLabelStyle_iconPath, migrationmodeler_BasicLabelStyle_labelSize, migrationmodeler_BasicLabelStyle_labelFormat}

# AbstractRepresentation class attributes and methods

# migrationmodeler_TestCase class attributes and methods

# migrationmodeler_Representation class attributes and methods
migrationmodeler_Representation_name: Property = Property(name="name", type=StringType)
migrationmodeler_Representation.attributes={migrationmodeler_Representation_name}

# migrationmodeler_BorderedStyle class attributes and methods
migrationmodeler_BorderedStyle_borderSize: Property = Property(name="borderSize", type=IntegerType)
migrationmodeler_BorderedStyle.attributes={migrationmodeler_BorderedStyle_borderSize}

# LabelStyle class attributes and methods

# BorderedStyle class attributes and methods

# migrationmodeler_Dot class attributes and methods

# NodeStyle class attributes and methods

# migrationmodeler_GaugeSection class attributes and methods
migrationmodeler_GaugeSection_min: Property = Property(name="min", type=StringType)
migrationmodeler_GaugeSection_max: Property = Property(name="max", type=StringType)
migrationmodeler_GaugeSection_value: Property = Property(name="value", type=StringType)
migrationmodeler_GaugeSection_label: Property = Property(name="label", type=StringType)
migrationmodeler_GaugeSection.attributes={migrationmodeler_GaugeSection_max, migrationmodeler_GaugeSection_value, migrationmodeler_GaugeSection_label, migrationmodeler_GaugeSection_min}

# migrationmodeler_FlatContainerStyle class attributes and methods
migrationmodeler_FlatContainerStyle_backgroundStyle: Property = Property(name="backgroundStyle", type=StringType)
migrationmodeler_FlatContainerStyle.attributes={migrationmodeler_FlatContainerStyle_backgroundStyle}

# ContainerStyle class attributes and methods

# migrationmodeler_ShapeContainerStyle class attributes and methods
migrationmodeler_ShapeContainerStyle_shape: Property = Property(name="shape", type=StringType)
migrationmodeler_ShapeContainerStyle.attributes={migrationmodeler_ShapeContainerStyle_shape}

# migrationmodeler_LabelStyle class attributes and methods
migrationmodeler_LabelStyle_labelAlignment: Property = Property(name="labelAlignment", type=StringType)
migrationmodeler_LabelStyle.attributes={migrationmodeler_LabelStyle_labelAlignment}

# BasicLabelStyle class attributes and methods

# migrationmodeler_Square class attributes and methods
migrationmodeler_Square_width: Property = Property(name="width", type=StringType)
migrationmodeler_Square_height: Property = Property(name="height", type=StringType)
migrationmodeler_Square.attributes={migrationmodeler_Square_width, migrationmodeler_Square_height}

# migrationmodeler_Ellipse class attributes and methods
migrationmodeler_Ellipse_horizontalDiameter: Property = Property(name="horizontalDiameter", type=StringType)
migrationmodeler_Ellipse_verticalDiameter: Property = Property(name="verticalDiameter", type=StringType)
migrationmodeler_Ellipse.attributes={migrationmodeler_Ellipse_horizontalDiameter, migrationmodeler_Ellipse_verticalDiameter}

# migrationmodeler_Lozenge class attributes and methods
migrationmodeler_Lozenge_width: Property = Property(name="width", type=StringType)
migrationmodeler_Lozenge_height: Property = Property(name="height", type=StringType)
migrationmodeler_Lozenge.attributes={migrationmodeler_Lozenge_height, migrationmodeler_Lozenge_width}

# migrationmodeler_BundledImage class attributes and methods
migrationmodeler_BundledImage_shape: Property = Property(name="shape", type=StringType)
migrationmodeler_BundledImage.attributes={migrationmodeler_BundledImage_shape}

# migrationmodeler_GaugeCompositeStyle class attributes and methods
migrationmodeler_GaugeCompositeStyle_alignment: Property = Property(name="alignment", type=StringType)
migrationmodeler_GaugeCompositeStyle.attributes={migrationmodeler_GaugeCompositeStyle_alignment}

# migrationmodeler_Note class attributes and methods

# migrationmodeler_WorkspaceImage class attributes and methods
migrationmodeler_WorkspaceImage_workspacePath: Property = Property(name="workspacePath", type=StringType)
migrationmodeler_WorkspaceImage.attributes={migrationmodeler_WorkspaceImage_workspacePath}

# Relationships
edges3: BinaryAssociation = BinaryAssociation(
    name="edges3",
    ends={
        Property(name="migrationmodeler_Edge", type=migrationmodeler_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Diagram4", type=migrationmodeler_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filters5: BinaryAssociation = BinaryAssociation(
    name="filters5",
    ends={
        Property(name="migrationmodeler_Filter", type=migrationmodeler_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Diagram6", type=migrationmodeler_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layers7: BinaryAssociation = BinaryAssociation(
    name="layers7",
    ends={
        Property(name="migrationmodeler_Layer", type=migrationmodeler_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Diagram8", type=migrationmodeler_Layer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeRepresentations9: BinaryAssociation = BinaryAssociation(
    name="nodeRepresentations9",
    ends={
        Property(name="migrationmodeler_NodeRepresentation", type=migrationmodeler_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Node10", type=migrationmodeler_NodeRepresentation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
borderedRepresentations11: BinaryAssociation = BinaryAssociation(
    name="borderedRepresentations11",
    ends={
        Property(name="migrationmodeler_BorderedRepresentation", type=migrationmodeler_Bordered, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Bordered", type=migrationmodeler_BorderedRepresentation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
containerRepresentations12: BinaryAssociation = BinaryAssociation(
    name="containerRepresentations12",
    ends={
        Property(name="migrationmodeler_ContainerRepresentation", type=migrationmodeler_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Container13", type=migrationmodeler_ContainerRepresentation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements14: BinaryAssociation = BinaryAssociation(
    name="elements14",
    ends={
        Property(name="migrationmodeler_GraphicalElement", type=migrationmodeler_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Container15", type=migrationmodeler_GraphicalElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeRepresentations16: BinaryAssociation = BinaryAssociation(
    name="edgeRepresentations16",
    ends={
        Property(name="migrationmodeler_EdgeRepresentation", type=migrationmodeler_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Edge17", type=migrationmodeler_EdgeRepresentation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source18: BinaryAssociation = BinaryAssociation(
    name="source18",
    ends={
        Property(name="migrationmodeler_GraphicalElement20", type=migrationmodeler_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Edge19", type=migrationmodeler_GraphicalElement, multiplicity=Multiplicity(1, 1))
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="migrationmodeler_GraphicalElement23", type=migrationmodeler_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Edge22", type=migrationmodeler_GraphicalElement, multiplicity=Multiplicity(1, 1))
    }
)
layout24: BinaryAssociation = BinaryAssociation(
    name="layout24",
    ends={
        Property(name="migrationmodeler_Layout", type=migrationmodeler_AbstractRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_AbstractRepresentation", type=migrationmodeler_Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containers0: BinaryAssociation = BinaryAssociation(
    name="containers0",
    ends={
        Property(name="migrationmodeler_Container", type=migrationmodeler_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Diagram", type=migrationmodeler_Container, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="migrationmodeler_Node", type=migrationmodeler_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Diagram2", type=migrationmodeler_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target28: BinaryAssociation = BinaryAssociation(
    name="target28",
    ends={
        Property(name="migrationmodeler_GraphicalElement30", type=migrationmodeler_EdgeRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_EdgeRepresentation29", type=migrationmodeler_GraphicalElement, multiplicity=Multiplicity(0, 1))
    }
)
bendpoints31: BinaryAssociation = BinaryAssociation(
    name="bendpoints31",
    ends={
        Property(name="migrationmodeler_Point", type=migrationmodeler_EdgeRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_EdgeRepresentation32", type=migrationmodeler_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStyle33: BinaryAssociation = BinaryAssociation(
    name="ownedStyle33",
    ends={
        Property(name="migrationmodeler_EdgeStyle", type=migrationmodeler_EdgeRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_EdgeRepresentation34", type=migrationmodeler_EdgeStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bordereds35: BinaryAssociation = BinaryAssociation(
    name="bordereds35",
    ends={
        Property(name="migrationmodeler_Bordered36", type=migrationmodeler_AbstractNodeRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_AbstractNodeRepresentation", type=migrationmodeler_Bordered, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStyle37: BinaryAssociation = BinaryAssociation(
    name="ownedStyle37",
    ends={
        Property(name="migrationmodeler_NodeStyle", type=migrationmodeler_AbstractNodeRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_AbstractNodeRepresentation38", type=migrationmodeler_NodeStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedStyle39: BinaryAssociation = BinaryAssociation(
    name="ownedStyle39",
    ends={
        Property(name="migrationmodeler_ContainerStyle", type=migrationmodeler_ContainerRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_ContainerRepresentation40", type=migrationmodeler_ContainerStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color41: BinaryAssociation = BinaryAssociation(
    name="color41",
    ends={
        Property(name="migrationmodeler_Color", type=migrationmodeler_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_EdgeStyle42", type=migrationmodeler_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
beginLabelStyle43: BinaryAssociation = BinaryAssociation(
    name="beginLabelStyle43",
    ends={
        Property(name="migrationmodeler_BasicLabelStyle", type=migrationmodeler_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_EdgeStyle44", type=migrationmodeler_BasicLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
centerLabelStyle45: BinaryAssociation = BinaryAssociation(
    name="centerLabelStyle45",
    ends={
        Property(name="migrationmodeler_BasicLabelStyle47", type=migrationmodeler_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_EdgeStyle46", type=migrationmodeler_BasicLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endLabelStyle48: BinaryAssociation = BinaryAssociation(
    name="endLabelStyle48",
    ends={
        Property(name="migrationmodeler_BasicLabelStyle50", type=migrationmodeler_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_EdgeStyle49", type=migrationmodeler_BasicLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source25: BinaryAssociation = BinaryAssociation(
    name="source25",
    ends={
        Property(name="migrationmodeler_GraphicalElement27", type=migrationmodeler_EdgeRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_EdgeRepresentation26", type=migrationmodeler_GraphicalElement, multiplicity=Multiplicity(0, 1))
    }
)
representations51: BinaryAssociation = BinaryAssociation(
    name="representations51",
    ends={
        Property(name="migrationmodeler_Representation", type=migrationmodeler_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_TestCase", type=migrationmodeler_Representation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borderColor52: BinaryAssociation = BinaryAssociation(
    name="borderColor52",
    ends={
        Property(name="migrationmodeler_Color53", type=migrationmodeler_BorderedStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_BorderedStyle", type=migrationmodeler_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelColor54: BinaryAssociation = BinaryAssociation(
    name="labelColor54",
    ends={
        Property(name="migrationmodeler_Color56", type=migrationmodeler_BasicLabelStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_BasicLabelStyle55", type=migrationmodeler_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor57: BinaryAssociation = BinaryAssociation(
    name="backgroundColor57",
    ends={
        Property(name="migrationmodeler_Color58", type=migrationmodeler_Dot, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Dot", type=migrationmodeler_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor59: BinaryAssociation = BinaryAssociation(
    name="backgroundColor59",
    ends={
        Property(name="migrationmodeler_Color60", type=migrationmodeler_GaugeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_GaugeSection", type=migrationmodeler_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundColor61: BinaryAssociation = BinaryAssociation(
    name="foregroundColor61",
    ends={
        Property(name="migrationmodeler_Color63", type=migrationmodeler_GaugeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_GaugeSection62", type=migrationmodeler_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor64: BinaryAssociation = BinaryAssociation(
    name="backgroundColor64",
    ends={
        Property(name="migrationmodeler_Color65", type=migrationmodeler_FlatContainerStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_FlatContainerStyle", type=migrationmodeler_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundColor66: BinaryAssociation = BinaryAssociation(
    name="foregroundColor66",
    ends={
        Property(name="migrationmodeler_Color68", type=migrationmodeler_FlatContainerStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_FlatContainerStyle67", type=migrationmodeler_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color71: BinaryAssociation = BinaryAssociation(
    name="color71",
    ends={
        Property(name="migrationmodeler_Color72", type=migrationmodeler_Square, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Square", type=migrationmodeler_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color73: BinaryAssociation = BinaryAssociation(
    name="color73",
    ends={
        Property(name="migrationmodeler_Color74", type=migrationmodeler_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Ellipse", type=migrationmodeler_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color75: BinaryAssociation = BinaryAssociation(
    name="color75",
    ends={
        Property(name="migrationmodeler_Color76", type=migrationmodeler_Lozenge, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Lozenge", type=migrationmodeler_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor69: BinaryAssociation = BinaryAssociation(
    name="backgroundColor69",
    ends={
        Property(name="migrationmodeler_Color70", type=migrationmodeler_ShapeContainerStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_ShapeContainerStyle", type=migrationmodeler_Color, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sections79: BinaryAssociation = BinaryAssociation(
    name="sections79",
    ends={
        Property(name="migrationmodeler_GaugeSection80", type=migrationmodeler_GaugeCompositeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_GaugeCompositeStyle", type=migrationmodeler_GaugeSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
color81: BinaryAssociation = BinaryAssociation(
    name="color81",
    ends={
        Property(name="migrationmodeler_Color82", type=migrationmodeler_Note, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_Note", type=migrationmodeler_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color77: BinaryAssociation = BinaryAssociation(
    name="color77",
    ends={
        Property(name="migrationmodeler_Color78", type=migrationmodeler_BundledImage, multiplicity=Multiplicity(1, 1)),
        Property(name="migrationmodeler_BundledImage", type=migrationmodeler_Color, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_migrationmodeler_AbstractNode_GraphicalElement = Generalization(general=GraphicalElement, specific=migrationmodeler_AbstractNode)
gen_migrationmodeler_Node_AbstractNode = Generalization(general=AbstractNode, specific=migrationmodeler_Node)
gen_migrationmodeler_Bordered_AbstractNode = Generalization(general=AbstractNode, specific=migrationmodeler_Bordered)
gen_migrationmodeler_Container_GraphicalElement = Generalization(general=GraphicalElement, specific=migrationmodeler_Container)
gen_migrationmodeler_Edge_GraphicalElement = Generalization(general=GraphicalElement, specific=migrationmodeler_Edge)
gen_migrationmodeler_Diagram_Representation = Generalization(general=Representation, specific=migrationmodeler_Diagram)
gen_migrationmodeler_AbstractNodeRepresentation_AbstractRepresentation = Generalization(general=AbstractRepresentation, specific=migrationmodeler_AbstractNodeRepresentation)
gen_migrationmodeler_NodeRepresentation_AbstractNodeRepresentation = Generalization(general=AbstractNodeRepresentation, specific=migrationmodeler_NodeRepresentation)
gen_migrationmodeler_BorderedRepresentation_AbstractNodeRepresentation = Generalization(general=AbstractNodeRepresentation, specific=migrationmodeler_BorderedRepresentation)
gen_migrationmodeler_ContainerRepresentation_AbstractRepresentation = Generalization(general=AbstractRepresentation, specific=migrationmodeler_ContainerRepresentation)
gen_migrationmodeler_EdgeRepresentation_AbstractRepresentation = Generalization(general=AbstractRepresentation, specific=migrationmodeler_EdgeRepresentation)
gen_migrationmodeler_NodeStyle_LabelStyle = Generalization(general=LabelStyle, specific=migrationmodeler_NodeStyle)
gen_migrationmodeler_NodeStyle_BorderedStyle = Generalization(general=BorderedStyle, specific=migrationmodeler_NodeStyle)
gen_migrationmodeler_Dot_NodeStyle = Generalization(general=NodeStyle, specific=migrationmodeler_Dot)
gen_migrationmodeler_FlatContainerStyle_ContainerStyle = Generalization(general=ContainerStyle, specific=migrationmodeler_FlatContainerStyle)
gen_migrationmodeler_ShapeContainerStyle_ContainerStyle = Generalization(general=ContainerStyle, specific=migrationmodeler_ShapeContainerStyle)
gen_migrationmodeler_ContainerStyle_LabelStyle = Generalization(general=LabelStyle, specific=migrationmodeler_ContainerStyle)
gen_migrationmodeler_ContainerStyle_BorderedStyle = Generalization(general=BorderedStyle, specific=migrationmodeler_ContainerStyle)
gen_migrationmodeler_LabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=migrationmodeler_LabelStyle)
gen_migrationmodeler_Square_NodeStyle = Generalization(general=NodeStyle, specific=migrationmodeler_Square)
gen_migrationmodeler_Ellipse_NodeStyle = Generalization(general=NodeStyle, specific=migrationmodeler_Ellipse)
gen_migrationmodeler_Lozenge_NodeStyle = Generalization(general=NodeStyle, specific=migrationmodeler_Lozenge)
gen_migrationmodeler_BundledImage_NodeStyle = Generalization(general=NodeStyle, specific=migrationmodeler_BundledImage)
gen_migrationmodeler_GaugeCompositeStyle_NodeStyle = Generalization(general=NodeStyle, specific=migrationmodeler_GaugeCompositeStyle)
gen_migrationmodeler_Note_NodeStyle = Generalization(general=NodeStyle, specific=migrationmodeler_Note)
gen_migrationmodeler_WorkspaceImage_NodeStyle = Generalization(general=NodeStyle, specific=migrationmodeler_WorkspaceImage)
gen_migrationmodeler_WorkspaceImage_ContainerStyle = Generalization(general=ContainerStyle, specific=migrationmodeler_WorkspaceImage)

# Domain Model
domain_model = DomainModel(
    name="migrationmodeler",
    types={migrationmodeler_Diagram, migrationmodeler_Edge, migrationmodeler_Filter, migrationmodeler_Layer, migrationmodeler_GraphicalElement, migrationmodeler_AbstractNode, GraphicalElement, AbstractNode, migrationmodeler_NodeRepresentation, migrationmodeler_Bordered, migrationmodeler_BorderedRepresentation, migrationmodeler_ContainerRepresentation, migrationmodeler_EdgeRepresentation, migrationmodeler_AbstractRepresentation, migrationmodeler_Layout, Representation, migrationmodeler_Container, migrationmodeler_Node, migrationmodeler_Point, migrationmodeler_EdgeStyle, migrationmodeler_AbstractNodeRepresentation, migrationmodeler_NodeStyle, AbstractNodeRepresentation, migrationmodeler_ContainerStyle, migrationmodeler_Color, migrationmodeler_BasicLabelStyle, AbstractRepresentation, migrationmodeler_TestCase, migrationmodeler_Representation, migrationmodeler_BorderedStyle, LabelStyle, BorderedStyle, migrationmodeler_Dot, NodeStyle, migrationmodeler_GaugeSection, migrationmodeler_FlatContainerStyle, ContainerStyle, migrationmodeler_ShapeContainerStyle, migrationmodeler_LabelStyle, BasicLabelStyle, migrationmodeler_Square, migrationmodeler_Ellipse, migrationmodeler_Lozenge, migrationmodeler_BundledImage, migrationmodeler_GaugeCompositeStyle, migrationmodeler_Note, migrationmodeler_WorkspaceImage, RoutingStyle, FontFormat, LabelPosition, LabelAlignment, AlignmentKind, BundledImageShape, ContainerShape, BackgroundStyle},
    associations={edges3, filters5, layers7, nodeRepresentations9, borderedRepresentations11, containerRepresentations12, elements14, edgeRepresentations16, source18, target21, layout24, containers0, nodes1, target28, bendpoints31, ownedStyle33, bordereds35, ownedStyle37, ownedStyle39, color41, beginLabelStyle43, centerLabelStyle45, endLabelStyle48, source25, representations51, borderColor52, labelColor54, backgroundColor57, backgroundColor59, foregroundColor61, backgroundColor64, foregroundColor66, color71, color73, color75, backgroundColor69, sections79, color81, color77},
    generalizations={gen_migrationmodeler_AbstractNode_GraphicalElement, gen_migrationmodeler_Node_AbstractNode, gen_migrationmodeler_Bordered_AbstractNode, gen_migrationmodeler_Container_GraphicalElement, gen_migrationmodeler_Edge_GraphicalElement, gen_migrationmodeler_Diagram_Representation, gen_migrationmodeler_AbstractNodeRepresentation_AbstractRepresentation, gen_migrationmodeler_NodeRepresentation_AbstractNodeRepresentation, gen_migrationmodeler_BorderedRepresentation_AbstractNodeRepresentation, gen_migrationmodeler_ContainerRepresentation_AbstractRepresentation, gen_migrationmodeler_EdgeRepresentation_AbstractRepresentation, gen_migrationmodeler_NodeStyle_LabelStyle, gen_migrationmodeler_NodeStyle_BorderedStyle, gen_migrationmodeler_Dot_NodeStyle, gen_migrationmodeler_FlatContainerStyle_ContainerStyle, gen_migrationmodeler_ShapeContainerStyle_ContainerStyle, gen_migrationmodeler_ContainerStyle_LabelStyle, gen_migrationmodeler_ContainerStyle_BorderedStyle, gen_migrationmodeler_LabelStyle_BasicLabelStyle, gen_migrationmodeler_Square_NodeStyle, gen_migrationmodeler_Ellipse_NodeStyle, gen_migrationmodeler_Lozenge_NodeStyle, gen_migrationmodeler_BundledImage_NodeStyle, gen_migrationmodeler_GaugeCompositeStyle_NodeStyle, gen_migrationmodeler_Note_NodeStyle, gen_migrationmodeler_WorkspaceImage_NodeStyle, gen_migrationmodeler_WorkspaceImage_ContainerStyle},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)