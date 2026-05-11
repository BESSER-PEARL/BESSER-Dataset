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
Orientation: Enumeration = Enumeration(
    name="Orientation",
    literals={
            EnumerationLiteral(name="ALIGNMENT_CENTER"),
			EnumerationLiteral(name="ALIGNMENT_LEFT"),
			EnumerationLiteral(name="ALIGNMENT_TOP"),
			EnumerationLiteral(name="ALIGNMENT_RIGHT"),
			EnumerationLiteral(name="ALIGNMENT_BOTTOM"),
			EnumerationLiteral(name="ALIGNMENT_MIDDLE"),
			EnumerationLiteral(name="UNSPECIFIED")
    }
)

LocationType: Enumeration = Enumeration(
    name="LocationType",
    literals={
            EnumerationLiteral(name="LOCATION_TYPE_RELATIVE"),
			EnumerationLiteral(name="LOCATION_TYPE_ABSOLUTE_START"),
			EnumerationLiteral(name="LOCATION_TYPE_ABSOLUTE_END")
    }
)

LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="DOT"),
			EnumerationLiteral(name="UNSPECIFIED"),
			EnumerationLiteral(name="SOLID"),
			EnumerationLiteral(name="DASH"),
			EnumerationLiteral(name="DASHDOT"),
			EnumerationLiteral(name="DASHDOTDOT")
    }
)

# Classes
mm_PropertyContainer = Class(name="mm_PropertyContainer", is_abstract=True)
mm_GraphicsAlgorithmContainer = Class(name="mm_GraphicsAlgorithmContainer", is_abstract=True)
PropertyContainer = Class(name="PropertyContainer")
mm_StyleContainer = Class(name="mm_StyleContainer", is_abstract=True)
styles_Style = Class(name="styles_Style")
mm_pictograms_Shape = Class(name="mm_pictograms_Shape")
AnchorContainer = Class(name="AnchorContainer")
ContainerShape = Class(name="ContainerShape")
mm_pictograms_ContainerShape = Class(name="mm_pictograms_ContainerShape")
Shape = Class(name="Shape")
mm_pictograms_Diagram = Class(name="mm_pictograms_Diagram")
pictograms_ContainerShape = Class(name="pictograms_ContainerShape")
mm_Property = Class(name="mm_Property")
mm_pictograms_PictogramElement = Class(name="mm_pictograms_PictogramElement", is_abstract=True)
GraphicsAlgorithmContainer = Class(name="GraphicsAlgorithmContainer")
GraphicsAlgorithm = Class(name="GraphicsAlgorithm")
mm_pictograms_Connection = Class(name="mm_pictograms_Connection")
Anchor = Class(name="Anchor")
Diagram = Class(name="Diagram")
StyleContainer = Class(name="StyleContainer")
Connection = Class(name="Connection")
styles_Color = Class(name="styles_Color")
styles_Font = Class(name="styles_Font")
PictogramLink = Class(name="PictogramLink")
mm_pictograms_ChopboxAnchor = Class(name="mm_pictograms_ChopboxAnchor")
mm_pictograms_ConnectionDecorator = Class(name="mm_pictograms_ConnectionDecorator")
mm_pictograms_FreeFormConnection = Class(name="mm_pictograms_FreeFormConnection")
mm_pictograms_ManhattanConnection = Class(name="mm_pictograms_ManhattanConnection")
mm_pictograms_PictogramLink = Class(name="mm_pictograms_PictogramLink")
ConnectionDecorator = Class(name="ConnectionDecorator")
mm_pictograms_Anchor = Class(name="mm_pictograms_Anchor", is_abstract=True)
PictogramElement = Class(name="PictogramElement")
mm_pictograms_AnchorContainer = Class(name="mm_pictograms_AnchorContainer", is_abstract=True)
mm_pictograms_FixPointAnchor = Class(name="mm_pictograms_FixPointAnchor")
AdvancedAnchor = Class(name="AdvancedAnchor")
styles_Point = Class(name="styles_Point")
mm_pictograms_BoxRelativeAnchor = Class(name="mm_pictograms_BoxRelativeAnchor")
mm_algorithms_Polyline = Class(name="mm_algorithms_Polyline")
mm_algorithms_Ellipse = Class(name="mm_algorithms_Ellipse")
mm_algorithms_Text = Class(name="mm_algorithms_Text")
AbstractText = Class(name="AbstractText")
mm_algorithms_Polygon = Class(name="mm_algorithms_Polygon")
Polyline = Class(name="Polyline")
mm_algorithms_Rectangle = Class(name="mm_algorithms_Rectangle")
mm_algorithms_RoundedRectangle = Class(name="mm_algorithms_RoundedRectangle")
pictograms_mm_EObject = Class(name="pictograms_mm_EObject")
mm_pictograms_AdvancedAnchor = Class(name="mm_pictograms_AdvancedAnchor", is_abstract=True)
mm_pictograms_CurvedConnection = Class(name="mm_pictograms_CurvedConnection")
styles_PrecisionPoint = Class(name="styles_PrecisionPoint")
mm_pictograms_CompositeConnection = Class(name="mm_pictograms_CompositeConnection")
CurvedConnection = Class(name="CurvedConnection")
mm_algorithms_GraphicsAlgorithm = Class(name="mm_algorithms_GraphicsAlgorithm", is_abstract=True)
styles_AbstractStyle = Class(name="styles_AbstractStyle")
mm_styles_RenderingStyle = Class(name="mm_styles_RenderingStyle")
styles_AdaptedGradientColoredAreas = Class(name="styles_AdaptedGradientColoredAreas")
mm_styles_Style = Class(name="mm_styles_Style")
mm_algorithms_Image = Class(name="mm_algorithms_Image")
mm_algorithms_PlatformGraphicsAlgorithm = Class(name="mm_algorithms_PlatformGraphicsAlgorithm")
mm_algorithms_AbstractText = Class(name="mm_algorithms_AbstractText", is_abstract=True)
mm_algorithms_MultiText = Class(name="mm_algorithms_MultiText")
mm_styles_GradientColoredAreas = Class(name="mm_styles_GradientColoredAreas")
styles_GradientColoredArea = Class(name="styles_GradientColoredArea")
mm_styles_AdaptedGradientColoredAreas = Class(name="mm_styles_AdaptedGradientColoredAreas")
styles_GradientColoredAreas = Class(name="styles_GradientColoredAreas")
mm_styles_Font = Class(name="mm_styles_Font")
styles_mm_StyleContainer = Class(name="styles_mm_StyleContainer")
mm_styles_AbstractStyle = Class(name="mm_styles_AbstractStyle", is_abstract=True)
styles_RenderingStyle = Class(name="styles_RenderingStyle")
mm_styles_GradientColoredLocation = Class(name="mm_styles_GradientColoredLocation")
mm_styles_GradientColoredArea = Class(name="mm_styles_GradientColoredArea")
styles_GradientColoredLocation = Class(name="styles_GradientColoredLocation")
mm_styles_Point = Class(name="mm_styles_Point")
mm_styles_Color = Class(name="mm_styles_Color")
mm_styles_PrecisionPoint = Class(name="mm_styles_PrecisionPoint")

# mm_PropertyContainer class attributes and methods

# mm_GraphicsAlgorithmContainer class attributes and methods

# PropertyContainer class attributes and methods

# mm_StyleContainer class attributes and methods

# styles_Style class attributes and methods

# mm_pictograms_Shape class attributes and methods

# AnchorContainer class attributes and methods

# ContainerShape class attributes and methods

# mm_pictograms_ContainerShape class attributes and methods

# Shape class attributes and methods

# mm_pictograms_Diagram class attributes and methods
mm_pictograms_Diagram_gridUnit: Property = Property(name="gridUnit", type=IntegerType)
mm_pictograms_Diagram_diagramTypeId: Property = Property(name="diagramTypeId", type=StringType)
mm_pictograms_Diagram_name: Property = Property(name="name", type=StringType)
mm_pictograms_Diagram_snapToGrid: Property = Property(name="snapToGrid", type=BooleanType)
mm_pictograms_Diagram_showGuides: Property = Property(name="showGuides", type=BooleanType)
mm_pictograms_Diagram_verticalGridUnit: Property = Property(name="verticalGridUnit", type=IntegerType)
mm_pictograms_Diagram_version: Property = Property(name="version", type=StringType)
mm_pictograms_Diagram.attributes={mm_pictograms_Diagram_verticalGridUnit, mm_pictograms_Diagram_version, mm_pictograms_Diagram_name, mm_pictograms_Diagram_snapToGrid, mm_pictograms_Diagram_gridUnit, mm_pictograms_Diagram_showGuides, mm_pictograms_Diagram_diagramTypeId}

# pictograms_ContainerShape class attributes and methods

# mm_Property class attributes and methods
mm_Property_value: Property = Property(name="value", type=StringType)
mm_Property_key: Property = Property(name="key", type=StringType)
mm_Property.attributes={mm_Property_key, mm_Property_value}

# mm_pictograms_PictogramElement class attributes and methods
mm_pictograms_PictogramElement_visible: Property = Property(name="visible", type=BooleanType)
mm_pictograms_PictogramElement_active: Property = Property(name="active", type=BooleanType)
mm_pictograms_PictogramElement.attributes={mm_pictograms_PictogramElement_visible, mm_pictograms_PictogramElement_active}

# GraphicsAlgorithmContainer class attributes and methods

# GraphicsAlgorithm class attributes and methods

# mm_pictograms_Connection class attributes and methods

# Anchor class attributes and methods

# Diagram class attributes and methods

# StyleContainer class attributes and methods

# Connection class attributes and methods

# styles_Color class attributes and methods

# styles_Font class attributes and methods

# PictogramLink class attributes and methods

# mm_pictograms_ChopboxAnchor class attributes and methods

# mm_pictograms_ConnectionDecorator class attributes and methods
mm_pictograms_ConnectionDecorator_locationRelative: Property = Property(name="locationRelative", type=BooleanType)
mm_pictograms_ConnectionDecorator_location: Property = Property(name="location", type=FloatType)
mm_pictograms_ConnectionDecorator.attributes={mm_pictograms_ConnectionDecorator_location, mm_pictograms_ConnectionDecorator_locationRelative}

# mm_pictograms_FreeFormConnection class attributes and methods

# mm_pictograms_ManhattanConnection class attributes and methods

# mm_pictograms_PictogramLink class attributes and methods

# ConnectionDecorator class attributes and methods

# mm_pictograms_Anchor class attributes and methods

# PictogramElement class attributes and methods

# mm_pictograms_AnchorContainer class attributes and methods

# mm_pictograms_FixPointAnchor class attributes and methods

# AdvancedAnchor class attributes and methods

# styles_Point class attributes and methods

# mm_pictograms_BoxRelativeAnchor class attributes and methods
mm_pictograms_BoxRelativeAnchor_relativeHeight: Property = Property(name="relativeHeight", type=FloatType)
mm_pictograms_BoxRelativeAnchor_relativeWidth: Property = Property(name="relativeWidth", type=FloatType)
mm_pictograms_BoxRelativeAnchor.attributes={mm_pictograms_BoxRelativeAnchor_relativeHeight, mm_pictograms_BoxRelativeAnchor_relativeWidth}

# mm_algorithms_Polyline class attributes and methods

# mm_algorithms_Ellipse class attributes and methods

# mm_algorithms_Text class attributes and methods

# AbstractText class attributes and methods

# mm_algorithms_Polygon class attributes and methods

# Polyline class attributes and methods

# mm_algorithms_Rectangle class attributes and methods

# mm_algorithms_RoundedRectangle class attributes and methods
mm_algorithms_RoundedRectangle_cornerHeight: Property = Property(name="cornerHeight", type=IntegerType)
mm_algorithms_RoundedRectangle_cornerWidth: Property = Property(name="cornerWidth", type=IntegerType)
mm_algorithms_RoundedRectangle.attributes={mm_algorithms_RoundedRectangle_cornerWidth, mm_algorithms_RoundedRectangle_cornerHeight}

# pictograms_mm_EObject class attributes and methods

# mm_pictograms_AdvancedAnchor class attributes and methods
mm_pictograms_AdvancedAnchor_useAnchorLocationAsConnectionEndpoint: Property = Property(name="useAnchorLocationAsConnectionEndpoint", type=BooleanType)
mm_pictograms_AdvancedAnchor.attributes={mm_pictograms_AdvancedAnchor_useAnchorLocationAsConnectionEndpoint}

# mm_pictograms_CurvedConnection class attributes and methods

# styles_PrecisionPoint class attributes and methods

# mm_pictograms_CompositeConnection class attributes and methods

# CurvedConnection class attributes and methods

# mm_algorithms_GraphicsAlgorithm class attributes and methods
mm_algorithms_GraphicsAlgorithm_height: Property = Property(name="height", type=IntegerType)
mm_algorithms_GraphicsAlgorithm_x: Property = Property(name="x", type=IntegerType)
mm_algorithms_GraphicsAlgorithm_y: Property = Property(name="y", type=IntegerType)
mm_algorithms_GraphicsAlgorithm_width: Property = Property(name="width", type=IntegerType)
mm_algorithms_GraphicsAlgorithm.attributes={mm_algorithms_GraphicsAlgorithm_y, mm_algorithms_GraphicsAlgorithm_x, mm_algorithms_GraphicsAlgorithm_height, mm_algorithms_GraphicsAlgorithm_width}

# styles_AbstractStyle class attributes and methods

# mm_styles_RenderingStyle class attributes and methods

# styles_AdaptedGradientColoredAreas class attributes and methods

# mm_styles_Style class attributes and methods
mm_styles_Style_id: Property = Property(name="id", type=StringType)
mm_styles_Style_description: Property = Property(name="description", type=StringType)
mm_styles_Style_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
mm_styles_Style_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
mm_styles_Style_angle: Property = Property(name="angle", type=StringType)
mm_styles_Style_stretchH: Property = Property(name="stretchH", type=StringType)
mm_styles_Style_stretchV: Property = Property(name="stretchV", type=StringType)
mm_styles_Style_proportional: Property = Property(name="proportional", type=StringType)
mm_styles_Style.attributes={mm_styles_Style_proportional, mm_styles_Style_stretchH, mm_styles_Style_verticalAlignment, mm_styles_Style_stretchV, mm_styles_Style_angle, mm_styles_Style_id, mm_styles_Style_description, mm_styles_Style_horizontalAlignment}

# mm_algorithms_Image class attributes and methods
mm_algorithms_Image_id: Property = Property(name="id", type=StringType)
mm_algorithms_Image_stretchH: Property = Property(name="stretchH", type=StringType)
mm_algorithms_Image_stretchV: Property = Property(name="stretchV", type=StringType)
mm_algorithms_Image_proportional: Property = Property(name="proportional", type=StringType)
mm_algorithms_Image.attributes={mm_algorithms_Image_stretchH, mm_algorithms_Image_proportional, mm_algorithms_Image_stretchV, mm_algorithms_Image_id}

# mm_algorithms_PlatformGraphicsAlgorithm class attributes and methods
mm_algorithms_PlatformGraphicsAlgorithm_id: Property = Property(name="id", type=StringType)
mm_algorithms_PlatformGraphicsAlgorithm.attributes={mm_algorithms_PlatformGraphicsAlgorithm_id}

# mm_algorithms_AbstractText class attributes and methods
mm_algorithms_AbstractText_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
mm_algorithms_AbstractText_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
mm_algorithms_AbstractText_angle: Property = Property(name="angle", type=StringType)
mm_algorithms_AbstractText_value: Property = Property(name="value", type=StringType)
mm_algorithms_AbstractText.attributes={mm_algorithms_AbstractText_value, mm_algorithms_AbstractText_horizontalAlignment, mm_algorithms_AbstractText_verticalAlignment, mm_algorithms_AbstractText_angle}

# mm_algorithms_MultiText class attributes and methods

# mm_styles_GradientColoredAreas class attributes and methods
mm_styles_GradientColoredAreas_styleAdaption: Property = Property(name="styleAdaption", type=StringType)
mm_styles_GradientColoredAreas.attributes={mm_styles_GradientColoredAreas_styleAdaption}

# styles_GradientColoredArea class attributes and methods

# mm_styles_AdaptedGradientColoredAreas class attributes and methods
mm_styles_AdaptedGradientColoredAreas_definedStyleId: Property = Property(name="definedStyleId", type=StringType)
mm_styles_AdaptedGradientColoredAreas_gradientType: Property = Property(name="gradientType", type=StringType)
mm_styles_AdaptedGradientColoredAreas.attributes={mm_styles_AdaptedGradientColoredAreas_gradientType, mm_styles_AdaptedGradientColoredAreas_definedStyleId}

# styles_GradientColoredAreas class attributes and methods

# mm_styles_Font class attributes and methods
mm_styles_Font_name: Property = Property(name="name", type=StringType)
mm_styles_Font_size: Property = Property(name="size", type=IntegerType)
mm_styles_Font_italic: Property = Property(name="italic", type=BooleanType)
mm_styles_Font_bold: Property = Property(name="bold", type=BooleanType)
mm_styles_Font.attributes={mm_styles_Font_italic, mm_styles_Font_name, mm_styles_Font_size, mm_styles_Font_bold}

# styles_mm_StyleContainer class attributes and methods

# mm_styles_AbstractStyle class attributes and methods
mm_styles_AbstractStyle_lineWidth: Property = Property(name="lineWidth", type=StringType)
mm_styles_AbstractStyle_lineStyle: Property = Property(name="lineStyle", type=StringType)
mm_styles_AbstractStyle_filled: Property = Property(name="filled", type=StringType)
mm_styles_AbstractStyle_lineVisible: Property = Property(name="lineVisible", type=StringType)
mm_styles_AbstractStyle_transparency: Property = Property(name="transparency", type=StringType)
mm_styles_AbstractStyle.attributes={mm_styles_AbstractStyle_lineWidth, mm_styles_AbstractStyle_lineVisible, mm_styles_AbstractStyle_filled, mm_styles_AbstractStyle_lineStyle, mm_styles_AbstractStyle_transparency}

# styles_RenderingStyle class attributes and methods

# mm_styles_GradientColoredLocation class attributes and methods
mm_styles_GradientColoredLocation_locationType: Property = Property(name="locationType", type=StringType)
mm_styles_GradientColoredLocation_locationValue: Property = Property(name="locationValue", type=StringType)
mm_styles_GradientColoredLocation.attributes={mm_styles_GradientColoredLocation_locationType, mm_styles_GradientColoredLocation_locationValue}

# mm_styles_GradientColoredArea class attributes and methods

# styles_GradientColoredLocation class attributes and methods

# mm_styles_Point class attributes and methods
mm_styles_Point_x: Property = Property(name="x", type=IntegerType)
mm_styles_Point_y: Property = Property(name="y", type=IntegerType)
mm_styles_Point_before: Property = Property(name="before", type=IntegerType)
mm_styles_Point_after: Property = Property(name="after", type=IntegerType)
mm_styles_Point.attributes={mm_styles_Point_after, mm_styles_Point_before, mm_styles_Point_y, mm_styles_Point_x}

# mm_styles_Color class attributes and methods
mm_styles_Color_red: Property = Property(name="red", type=IntegerType)
mm_styles_Color_green: Property = Property(name="green", type=IntegerType)
mm_styles_Color_blue: Property = Property(name="blue", type=IntegerType)
mm_styles_Color.attributes={mm_styles_Color_red, mm_styles_Color_green, mm_styles_Color_blue}

# mm_styles_PrecisionPoint class attributes and methods
mm_styles_PrecisionPoint_x: Property = Property(name="x", type=FloatType)
mm_styles_PrecisionPoint_y: Property = Property(name="y", type=FloatType)
mm_styles_PrecisionPoint.attributes={mm_styles_PrecisionPoint_y, mm_styles_PrecisionPoint_x}

# Relationships
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="mm_Property", type=mm_PropertyContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_PropertyContainer", type=mm_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styles1: BinaryAssociation = BinaryAssociation(
    name="styles1",
    ends={
        Property(name="Style", type=mm_StyleContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="styleContainer", type=styles_Style, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container2: BinaryAssociation = BinaryAssociation(
    name="container2",
    ends={
        Property(name="ContainerShape", type=mm_pictograms_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=ContainerShape, multiplicity=Multiplicity(0, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="Shape", type=mm_pictograms_ContainerShape, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphicsAlgorithm10: BinaryAssociation = BinaryAssociation(
    name="graphicsAlgorithm10",
    ends={
        Property(name="GraphicsAlgorithm", type=mm_pictograms_PictogramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pictogramElement", type=GraphicsAlgorithm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
link11: BinaryAssociation = BinaryAssociation(
    name="link11",
    ends={
        Property(name="PictogramLink13", type=mm_pictograms_PictogramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pictogramElement12", type=PictogramLink, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start14: BinaryAssociation = BinaryAssociation(
    name="start14",
    ends={
        Property(name="Anchor", type=mm_pictograms_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingConnections", type=Anchor, multiplicity=Multiplicity(1, 1))
    }
)
end15: BinaryAssociation = BinaryAssociation(
    name="end15",
    ends={
        Property(name="Anchor16", type=mm_pictograms_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingConnections", type=Anchor, multiplicity=Multiplicity(1, 1))
    }
)
parent17: BinaryAssociation = BinaryAssociation(
    name="parent17",
    ends={
        Property(name="Diagram", type=mm_pictograms_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connections", type=Diagram, multiplicity=Multiplicity(1, 1))
    }
)
connections4: BinaryAssociation = BinaryAssociation(
    name="connections4",
    ends={
        Property(name="Connection", type=mm_pictograms_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colors5: BinaryAssociation = BinaryAssociation(
    name="colors5",
    ends={
        Property(name="styles_Color", type=mm_pictograms_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_Diagram", type=styles_Color, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fonts6: BinaryAssociation = BinaryAssociation(
    name="fonts6",
    ends={
        Property(name="styles_Font", type=mm_pictograms_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_Diagram7", type=styles_Font, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pictogramLinks8: BinaryAssociation = BinaryAssociation(
    name="pictogramLinks8",
    ends={
        Property(name="PictogramLink", type=mm_pictograms_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_Diagram9", type=PictogramLink, multiplicity=Multiplicity(0, 9999))
    }
)
connection30: BinaryAssociation = BinaryAssociation(
    name="connection30",
    ends={
        Property(name="Connection31", type=mm_pictograms_ConnectionDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="connectionDecorators", type=Connection, multiplicity=Multiplicity(1, 1))
    }
)
bendpoints32: BinaryAssociation = BinaryAssociation(
    name="bendpoints32",
    ends={
        Property(name="styles_Point33", type=mm_pictograms_FreeFormConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_FreeFormConnection", type=styles_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pictogramElement34: BinaryAssociation = BinaryAssociation(
    name="pictogramElement34",
    ends={
        Property(name="PictogramElement", type=mm_pictograms_PictogramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="link", type=PictogramElement, multiplicity=Multiplicity(0, 1))
    }
)
connectionDecorators18: BinaryAssociation = BinaryAssociation(
    name="connectionDecorators18",
    ends={
        Property(name="ConnectionDecorator", type=mm_pictograms_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=ConnectionDecorator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent19: BinaryAssociation = BinaryAssociation(
    name="parent19",
    ends={
        Property(name="AnchorContainer", type=mm_pictograms_Anchor, multiplicity=Multiplicity(1, 1)),
        Property(name="anchors", type=AnchorContainer, multiplicity=Multiplicity(1, 1))
    }
)
outgoingConnections20: BinaryAssociation = BinaryAssociation(
    name="outgoingConnections20",
    ends={
        Property(name="Connection21", type=mm_pictograms_Anchor, multiplicity=Multiplicity(1, 1)),
        Property(name="start", type=Connection, multiplicity=Multiplicity(0, 9999))
    }
)
incomingConnections22: BinaryAssociation = BinaryAssociation(
    name="incomingConnections22",
    ends={
        Property(name="Connection23", type=mm_pictograms_Anchor, multiplicity=Multiplicity(1, 1)),
        Property(name="end", type=Connection, multiplicity=Multiplicity(0, 9999))
    }
)
referencedGraphicsAlgorithm24: BinaryAssociation = BinaryAssociation(
    name="referencedGraphicsAlgorithm24",
    ends={
        Property(name="GraphicsAlgorithm25", type=mm_pictograms_Anchor, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_Anchor", type=GraphicsAlgorithm, multiplicity=Multiplicity(0, 1))
    }
)
anchors26: BinaryAssociation = BinaryAssociation(
    name="anchors26",
    ends={
        Property(name="Anchor28", type=mm_pictograms_AnchorContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="parent27", type=Anchor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location29: BinaryAssociation = BinaryAssociation(
    name="location29",
    ends={
        Property(name="styles_Point", type=mm_pictograms_FixPointAnchor, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_FixPointAnchor", type=styles_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
style44: BinaryAssociation = BinaryAssociation(
    name="style44",
    ends={
        Property(name="styles_Style", type=mm_algorithms_GraphicsAlgorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_algorithms_GraphicsAlgorithm", type=styles_Style, multiplicity=Multiplicity(0, 1))
    }
)
points45: BinaryAssociation = BinaryAssociation(
    name="points45",
    ends={
        Property(name="styles_Point46", type=mm_algorithms_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_algorithms_Polyline", type=styles_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessObjects35: BinaryAssociation = BinaryAssociation(
    name="businessObjects35",
    ends={
        Property(name="pictograms_mm_EObject", type=mm_pictograms_PictogramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_PictogramLink", type=pictograms_mm_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
controlPoints36: BinaryAssociation = BinaryAssociation(
    name="controlPoints36",
    ends={
        Property(name="styles_PrecisionPoint", type=mm_pictograms_CurvedConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_CurvedConnection", type=styles_PrecisionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children37: BinaryAssociation = BinaryAssociation(
    name="children37",
    ends={
        Property(name="CurvedConnection", type=mm_pictograms_CompositeConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_CompositeConnection", type=CurvedConnection, multiplicity=Multiplicity(0, 9999))
    }
)
graphicsAlgorithmChildren38: BinaryAssociation = BinaryAssociation(
    name="graphicsAlgorithmChildren38",
    ends={
        Property(name="GraphicsAlgorithm39", type=mm_algorithms_GraphicsAlgorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="parentGraphicsAlgorithm", type=GraphicsAlgorithm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentGraphicsAlgorithm40: BinaryAssociation = BinaryAssociation(
    name="parentGraphicsAlgorithm40",
    ends={
        Property(name="GraphicsAlgorithm41", type=mm_algorithms_GraphicsAlgorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="graphicsAlgorithmChildren", type=GraphicsAlgorithm, multiplicity=Multiplicity(0, 1))
    }
)
pictogramElement42: BinaryAssociation = BinaryAssociation(
    name="pictogramElement42",
    ends={
        Property(name="PictogramElement43", type=mm_algorithms_GraphicsAlgorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="graphicsAlgorithm", type=PictogramElement, multiplicity=Multiplicity(0, 1))
    }
)
adaptedGradientColoredAreas49: BinaryAssociation = BinaryAssociation(
    name="adaptedGradientColoredAreas49",
    ends={
        Property(name="styles_AdaptedGradientColoredAreas", type=mm_styles_RenderingStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_RenderingStyle", type=styles_AdaptedGradientColoredAreas, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font50: BinaryAssociation = BinaryAssociation(
    name="font50",
    ends={
        Property(name="styles_Font51", type=mm_styles_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_Style", type=styles_Font, multiplicity=Multiplicity(0, 1))
    }
)
font47: BinaryAssociation = BinaryAssociation(
    name="font47",
    ends={
        Property(name="styles_Font48", type=mm_algorithms_AbstractText, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_algorithms_AbstractText", type=styles_Font, multiplicity=Multiplicity(0, 1))
    }
)
start62: BinaryAssociation = BinaryAssociation(
    name="start62",
    ends={
        Property(name="mm_styles_GradientColoredArea", type=styles_GradientColoredLocation, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="styles_GradientColoredLocation", type=mm_styles_GradientColoredArea, multiplicity=Multiplicity(1, 1))
    }
)
end63: BinaryAssociation = BinaryAssociation(
    name="end63",
    ends={
        Property(name="styles_GradientColoredLocation65", type=mm_styles_GradientColoredArea, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_GradientColoredArea64", type=styles_GradientColoredLocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gradientColor66: BinaryAssociation = BinaryAssociation(
    name="gradientColor66",
    ends={
        Property(name="styles_GradientColoredArea", type=mm_styles_GradientColoredAreas, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_GradientColoredAreas", type=styles_GradientColoredArea, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
adaptedGradientColoredAreas67: BinaryAssociation = BinaryAssociation(
    name="adaptedGradientColoredAreas67",
    ends={
        Property(name="styles_GradientColoredAreas", type=mm_styles_AdaptedGradientColoredAreas, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_AdaptedGradientColoredAreas", type=styles_GradientColoredAreas, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styleContainer52: BinaryAssociation = BinaryAssociation(
    name="styleContainer52",
    ends={
        Property(name="StyleContainer", type=mm_styles_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="styles", type=styles_mm_StyleContainer, multiplicity=Multiplicity(1, 1))
    }
)
background53: BinaryAssociation = BinaryAssociation(
    name="background53",
    ends={
        Property(name="styles_Color54", type=mm_styles_AbstractStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_AbstractStyle", type=styles_Color, multiplicity=Multiplicity(0, 1))
    }
)
foreground55: BinaryAssociation = BinaryAssociation(
    name="foreground55",
    ends={
        Property(name="styles_Color57", type=mm_styles_AbstractStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_AbstractStyle56", type=styles_Color, multiplicity=Multiplicity(0, 1))
    }
)
renderingStyle58: BinaryAssociation = BinaryAssociation(
    name="renderingStyle58",
    ends={
        Property(name="styles_RenderingStyle", type=mm_styles_AbstractStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_AbstractStyle59", type=styles_RenderingStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color60: BinaryAssociation = BinaryAssociation(
    name="color60",
    ends={
        Property(name="styles_Color61", type=mm_styles_GradientColoredLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_GradientColoredLocation", type=styles_Color, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_mm_GraphicsAlgorithmContainer_PropertyContainer = Generalization(general=PropertyContainer, specific=mm_GraphicsAlgorithmContainer)
gen_mm_pictograms_Shape_AnchorContainer = Generalization(general=AnchorContainer, specific=mm_pictograms_Shape)
gen_mm_pictograms_ContainerShape_Shape = Generalization(general=Shape, specific=mm_pictograms_ContainerShape)
gen_mm_pictograms_Diagram_pictograms_ContainerShape = Generalization(general=pictograms_ContainerShape, specific=mm_pictograms_Diagram)
gen_mm_pictograms_PictogramElement_GraphicsAlgorithmContainer = Generalization(general=GraphicsAlgorithmContainer, specific=mm_pictograms_PictogramElement)
gen_mm_pictograms_Connection_AnchorContainer = Generalization(general=AnchorContainer, specific=mm_pictograms_Connection)
gen_mm_pictograms_Diagram_StyleContainer = Generalization(general=StyleContainer, specific=mm_pictograms_Diagram)
gen_mm_pictograms_ChopboxAnchor_Anchor = Generalization(general=Anchor, specific=mm_pictograms_ChopboxAnchor)
gen_mm_pictograms_ConnectionDecorator_Shape = Generalization(general=Shape, specific=mm_pictograms_ConnectionDecorator)
gen_mm_pictograms_FreeFormConnection_Connection = Generalization(general=Connection, specific=mm_pictograms_FreeFormConnection)
gen_mm_pictograms_ManhattanConnection_Connection = Generalization(general=Connection, specific=mm_pictograms_ManhattanConnection)
gen_mm_pictograms_PictogramLink_PropertyContainer = Generalization(general=PropertyContainer, specific=mm_pictograms_PictogramLink)
gen_mm_pictograms_Anchor_PictogramElement = Generalization(general=PictogramElement, specific=mm_pictograms_Anchor)
gen_mm_pictograms_AnchorContainer_PictogramElement = Generalization(general=PictogramElement, specific=mm_pictograms_AnchorContainer)
gen_mm_pictograms_FixPointAnchor_AdvancedAnchor = Generalization(general=AdvancedAnchor, specific=mm_pictograms_FixPointAnchor)
gen_mm_pictograms_BoxRelativeAnchor_AdvancedAnchor = Generalization(general=AdvancedAnchor, specific=mm_pictograms_BoxRelativeAnchor)
gen_mm_algorithms_Polyline_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_Polyline)
gen_mm_algorithms_Ellipse_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_Ellipse)
gen_mm_algorithms_Text_AbstractText = Generalization(general=AbstractText, specific=mm_algorithms_Text)
gen_mm_algorithms_Polygon_Polyline = Generalization(general=Polyline, specific=mm_algorithms_Polygon)
gen_mm_algorithms_Rectangle_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_Rectangle)
gen_mm_algorithms_RoundedRectangle_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_RoundedRectangle)
gen_mm_pictograms_AdvancedAnchor_Anchor = Generalization(general=Anchor, specific=mm_pictograms_AdvancedAnchor)
gen_mm_pictograms_CurvedConnection_Connection = Generalization(general=Connection, specific=mm_pictograms_CurvedConnection)
gen_mm_pictograms_CompositeConnection_Connection = Generalization(general=Connection, specific=mm_pictograms_CompositeConnection)
gen_mm_algorithms_GraphicsAlgorithm_GraphicsAlgorithmContainer = Generalization(general=GraphicsAlgorithmContainer, specific=mm_algorithms_GraphicsAlgorithm)
gen_mm_algorithms_GraphicsAlgorithm_styles_AbstractStyle = Generalization(general=styles_AbstractStyle, specific=mm_algorithms_GraphicsAlgorithm)
gen_mm_styles_Style_StyleContainer = Generalization(general=StyleContainer, specific=mm_styles_Style)
gen_mm_styles_Style_styles_AbstractStyle = Generalization(general=styles_AbstractStyle, specific=mm_styles_Style)
gen_mm_algorithms_Image_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_Image)
gen_mm_algorithms_PlatformGraphicsAlgorithm_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_PlatformGraphicsAlgorithm)
gen_mm_algorithms_AbstractText_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_AbstractText)
gen_mm_algorithms_MultiText_AbstractText = Generalization(general=AbstractText, specific=mm_algorithms_MultiText)

# Domain Model
domain_model = DomainModel(
    name="mm",
    types={mm_PropertyContainer, mm_GraphicsAlgorithmContainer, PropertyContainer, mm_StyleContainer, styles_Style, mm_pictograms_Shape, AnchorContainer, ContainerShape, mm_pictograms_ContainerShape, Shape, mm_pictograms_Diagram, pictograms_ContainerShape, mm_Property, mm_pictograms_PictogramElement, GraphicsAlgorithmContainer, GraphicsAlgorithm, mm_pictograms_Connection, Anchor, Diagram, StyleContainer, Connection, styles_Color, styles_Font, PictogramLink, mm_pictograms_ChopboxAnchor, mm_pictograms_ConnectionDecorator, mm_pictograms_FreeFormConnection, mm_pictograms_ManhattanConnection, mm_pictograms_PictogramLink, ConnectionDecorator, mm_pictograms_Anchor, PictogramElement, mm_pictograms_AnchorContainer, mm_pictograms_FixPointAnchor, AdvancedAnchor, styles_Point, mm_pictograms_BoxRelativeAnchor, mm_algorithms_Polyline, mm_algorithms_Ellipse, mm_algorithms_Text, AbstractText, mm_algorithms_Polygon, Polyline, mm_algorithms_Rectangle, mm_algorithms_RoundedRectangle, pictograms_mm_EObject, mm_pictograms_AdvancedAnchor, mm_pictograms_CurvedConnection, styles_PrecisionPoint, mm_pictograms_CompositeConnection, CurvedConnection, mm_algorithms_GraphicsAlgorithm, styles_AbstractStyle, mm_styles_RenderingStyle, styles_AdaptedGradientColoredAreas, mm_styles_Style, mm_algorithms_Image, mm_algorithms_PlatformGraphicsAlgorithm, mm_algorithms_AbstractText, mm_algorithms_MultiText, mm_styles_GradientColoredAreas, styles_GradientColoredArea, mm_styles_AdaptedGradientColoredAreas, styles_GradientColoredAreas, mm_styles_Font, styles_mm_StyleContainer, mm_styles_AbstractStyle, styles_RenderingStyle, mm_styles_GradientColoredLocation, mm_styles_GradientColoredArea, styles_GradientColoredLocation, mm_styles_Point, mm_styles_Color, mm_styles_PrecisionPoint, Orientation, LocationType, LineStyle},
    associations={properties0, styles1, container2, children3, graphicsAlgorithm10, link11, start14, end15, parent17, connections4, colors5, fonts6, pictogramLinks8, connection30, bendpoints32, pictogramElement34, connectionDecorators18, parent19, outgoingConnections20, incomingConnections22, referencedGraphicsAlgorithm24, anchors26, location29, style44, points45, businessObjects35, controlPoints36, children37, graphicsAlgorithmChildren38, parentGraphicsAlgorithm40, pictogramElement42, adaptedGradientColoredAreas49, font50, font47, start62, end63, gradientColor66, adaptedGradientColoredAreas67, styleContainer52, background53, foreground55, renderingStyle58, color60},
    generalizations={gen_mm_GraphicsAlgorithmContainer_PropertyContainer, gen_mm_pictograms_Shape_AnchorContainer, gen_mm_pictograms_ContainerShape_Shape, gen_mm_pictograms_Diagram_pictograms_ContainerShape, gen_mm_pictograms_PictogramElement_GraphicsAlgorithmContainer, gen_mm_pictograms_Connection_AnchorContainer, gen_mm_pictograms_Diagram_StyleContainer, gen_mm_pictograms_ChopboxAnchor_Anchor, gen_mm_pictograms_ConnectionDecorator_Shape, gen_mm_pictograms_FreeFormConnection_Connection, gen_mm_pictograms_ManhattanConnection_Connection, gen_mm_pictograms_PictogramLink_PropertyContainer, gen_mm_pictograms_Anchor_PictogramElement, gen_mm_pictograms_AnchorContainer_PictogramElement, gen_mm_pictograms_FixPointAnchor_AdvancedAnchor, gen_mm_pictograms_BoxRelativeAnchor_AdvancedAnchor, gen_mm_algorithms_Polyline_GraphicsAlgorithm, gen_mm_algorithms_Ellipse_GraphicsAlgorithm, gen_mm_algorithms_Text_AbstractText, gen_mm_algorithms_Polygon_Polyline, gen_mm_algorithms_Rectangle_GraphicsAlgorithm, gen_mm_algorithms_RoundedRectangle_GraphicsAlgorithm, gen_mm_pictograms_AdvancedAnchor_Anchor, gen_mm_pictograms_CurvedConnection_Connection, gen_mm_pictograms_CompositeConnection_Connection, gen_mm_algorithms_GraphicsAlgorithm_GraphicsAlgorithmContainer, gen_mm_algorithms_GraphicsAlgorithm_styles_AbstractStyle, gen_mm_styles_Style_StyleContainer, gen_mm_styles_Style_styles_AbstractStyle, gen_mm_algorithms_Image_GraphicsAlgorithm, gen_mm_algorithms_PlatformGraphicsAlgorithm_GraphicsAlgorithm, gen_mm_algorithms_AbstractText_GraphicsAlgorithm, gen_mm_algorithms_MultiText_AbstractText},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)