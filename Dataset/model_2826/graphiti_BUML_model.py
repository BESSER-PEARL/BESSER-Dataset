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
			EnumerationLiteral(name="DASHDOT"),
			EnumerationLiteral(name="DASHDOTDOT"),
			EnumerationLiteral(name="DOT"),
			EnumerationLiteral(name="UNSPECIFIED")
    }
)

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

UnderlineStyle: Enumeration = Enumeration(
    name="UnderlineStyle",
    literals={
            EnumerationLiteral(name="UNDERLINE_SINGLE"),
			EnumerationLiteral(name="UNDERLINE_DOUBLE"),
			EnumerationLiteral(name="UNDERLINE_ERROR"),
			EnumerationLiteral(name="UNDERLINE_SQUIGGLE")
    }
)

# Classes
mm_pictograms_ContainerShape = Class(name="mm::pictograms::ContainerShape")
Shape = Class(name="Shape")
mm_pictograms_Diagram = Class(name="mm::pictograms::Diagram")
pictograms_ContainerShape = Class(name="pictograms::ContainerShape")
StyleContainer = Class(name="StyleContainer")
Connection = Class(name="Connection")
mm_Property = Class(name="mm::Property")
mm_PropertyContainer = Class(name="mm::PropertyContainer", is_abstract=True)
mm_GraphicsAlgorithmContainer = Class(name="mm::GraphicsAlgorithmContainer", is_abstract=True)
PropertyContainer = Class(name="PropertyContainer")
mm_StyleContainer = Class(name="mm::StyleContainer", is_abstract=True)
styles_Style = Class(name="styles::Style")
mm_pictograms_Shape = Class(name="mm::pictograms::Shape")
AnchorContainer = Class(name="AnchorContainer")
ContainerShape = Class(name="ContainerShape")
mm_pictograms_AnchorContainer = Class(name="mm::pictograms::AnchorContainer", is_abstract=True)
mm_pictograms_FixPointAnchor = Class(name="mm::pictograms::FixPointAnchor")
AdvancedAnchor = Class(name="AdvancedAnchor")
styles_Point = Class(name="styles::Point")
mm_pictograms_BoxRelativeAnchor = Class(name="mm::pictograms::BoxRelativeAnchor")
styles_Color = Class(name="styles::Color")
styles_Font = Class(name="styles::Font")
PictogramLink = Class(name="PictogramLink")
mm_pictograms_PictogramElement = Class(name="mm::pictograms::PictogramElement", is_abstract=True)
GraphicsAlgorithmContainer = Class(name="GraphicsAlgorithmContainer")
GraphicsAlgorithm = Class(name="GraphicsAlgorithm")
mm_pictograms_Connection = Class(name="mm::pictograms::Connection")
Anchor = Class(name="Anchor")
Diagram = Class(name="Diagram")
ConnectionDecorator = Class(name="ConnectionDecorator")
mm_pictograms_Anchor = Class(name="mm::pictograms::Anchor", is_abstract=True)
PictogramElement = Class(name="PictogramElement")
mm_algorithms_GraphicsAlgorithm = Class(name="mm::algorithms::GraphicsAlgorithm", is_abstract=True)
styles_AbstractStyle = Class(name="styles::AbstractStyle")
mm_pictograms_ChopboxAnchor = Class(name="mm::pictograms::ChopboxAnchor")
mm_pictograms_ConnectionDecorator = Class(name="mm::pictograms::ConnectionDecorator")
mm_pictograms_FreeFormConnection = Class(name="mm::pictograms::FreeFormConnection")
mm_pictograms_ManhattanConnection = Class(name="mm::pictograms::ManhattanConnection")
mm_pictograms_PictogramLink = Class(name="mm::pictograms::PictogramLink")
pictograms_mm_EObject = Class(name="pictograms::mm::EObject")
mm_pictograms_AdvancedAnchor = Class(name="mm::pictograms::AdvancedAnchor", is_abstract=True)
mm_pictograms_CurvedConnection = Class(name="mm::pictograms::CurvedConnection")
styles_PrecisionPoint = Class(name="styles::PrecisionPoint")
mm_pictograms_CompositeConnection = Class(name="mm::pictograms::CompositeConnection")
CurvedConnection = Class(name="CurvedConnection")
mm_algorithms_Text = Class(name="mm::algorithms::Text")
AbstractText = Class(name="AbstractText")
mm_algorithms_Polygon = Class(name="mm::algorithms::Polygon")
Polyline = Class(name="Polyline")
mm_algorithms_Rectangle = Class(name="mm::algorithms::Rectangle")
mm_algorithms_RoundedRectangle = Class(name="mm::algorithms::RoundedRectangle")
mm_algorithms_Polyline = Class(name="mm::algorithms::Polyline")
mm_algorithms_Ellipse = Class(name="mm::algorithms::Ellipse")
styles_TextStyleRegion = Class(name="styles::TextStyleRegion")
mm_algorithms_MultiText = Class(name="mm::algorithms::MultiText")
mm_algorithms_Image = Class(name="mm::algorithms::Image")
mm_algorithms_PlatformGraphicsAlgorithm = Class(name="mm::algorithms::PlatformGraphicsAlgorithm")
mm_algorithms_AbstractText = Class(name="mm::algorithms::AbstractText", is_abstract=True)
styles_AdaptedGradientColoredAreas = Class(name="styles::AdaptedGradientColoredAreas")
mm_styles_Style = Class(name="mm::styles::Style")
mm_styles_GradientColoredArea = Class(name="mm::styles::GradientColoredArea")
mm_styles_RenderingStyle = Class(name="mm::styles::RenderingStyle")
styles_GradientColoredLocation = Class(name="styles::GradientColoredLocation")
mm_styles_GradientColoredAreas = Class(name="mm::styles::GradientColoredAreas")
styles_GradientColoredArea = Class(name="styles::GradientColoredArea")
mm_styles_AdaptedGradientColoredAreas = Class(name="mm::styles::AdaptedGradientColoredAreas")
styles_GradientColoredAreas = Class(name="styles::GradientColoredAreas")
mm_styles_Font = Class(name="mm::styles::Font")
styles_mm_StyleContainer = Class(name="styles::mm::StyleContainer")
mm_styles_AbstractStyle = Class(name="mm::styles::AbstractStyle", is_abstract=True)
styles_RenderingStyle = Class(name="styles::RenderingStyle")
mm_styles_GradientColoredLocation = Class(name="mm::styles::GradientColoredLocation")
mm_styles_TextStyleRegion = Class(name="mm::styles::TextStyleRegion")
styles_TextStyle = Class(name="styles::TextStyle")
mm_styles_Point = Class(name="mm::styles::Point")
mm_styles_Color = Class(name="mm::styles::Color")
mm_styles_PrecisionPoint = Class(name="mm::styles::PrecisionPoint")
mm_styles_TextStyle = Class(name="mm::styles::TextStyle")

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
mm_pictograms_Diagram.attributes={mm_pictograms_Diagram_name, mm_pictograms_Diagram_gridUnit, mm_pictograms_Diagram_verticalGridUnit, mm_pictograms_Diagram_version, mm_pictograms_Diagram_showGuides, mm_pictograms_Diagram_snapToGrid, mm_pictograms_Diagram_diagramTypeId}

# pictograms_ContainerShape class attributes and methods

# StyleContainer class attributes and methods

# Connection class attributes and methods

# mm_Property class attributes and methods
mm_Property_key: Property = Property(name="key", type=StringType)
mm_Property_value: Property = Property(name="value", type=StringType)
mm_Property.attributes={mm_Property_key, mm_Property_value}

# mm_PropertyContainer class attributes and methods

# mm_GraphicsAlgorithmContainer class attributes and methods

# PropertyContainer class attributes and methods

# mm_StyleContainer class attributes and methods

# styles_Style class attributes and methods

# mm_pictograms_Shape class attributes and methods

# AnchorContainer class attributes and methods

# ContainerShape class attributes and methods

# mm_pictograms_AnchorContainer class attributes and methods

# mm_pictograms_FixPointAnchor class attributes and methods

# AdvancedAnchor class attributes and methods

# styles_Point class attributes and methods

# mm_pictograms_BoxRelativeAnchor class attributes and methods
mm_pictograms_BoxRelativeAnchor_relativeWidth: Property = Property(name="relativeWidth", type=FloatType)
mm_pictograms_BoxRelativeAnchor_relativeHeight: Property = Property(name="relativeHeight", type=FloatType)
mm_pictograms_BoxRelativeAnchor.attributes={mm_pictograms_BoxRelativeAnchor_relativeWidth, mm_pictograms_BoxRelativeAnchor_relativeHeight}

# styles_Color class attributes and methods

# styles_Font class attributes and methods

# PictogramLink class attributes and methods

# mm_pictograms_PictogramElement class attributes and methods
mm_pictograms_PictogramElement_visible: Property = Property(name="visible", type=BooleanType)
mm_pictograms_PictogramElement_active: Property = Property(name="active", type=BooleanType)
mm_pictograms_PictogramElement.attributes={mm_pictograms_PictogramElement_visible, mm_pictograms_PictogramElement_active}

# GraphicsAlgorithmContainer class attributes and methods

# GraphicsAlgorithm class attributes and methods

# mm_pictograms_Connection class attributes and methods

# Anchor class attributes and methods

# Diagram class attributes and methods

# ConnectionDecorator class attributes and methods

# mm_pictograms_Anchor class attributes and methods

# PictogramElement class attributes and methods

# mm_algorithms_GraphicsAlgorithm class attributes and methods
mm_algorithms_GraphicsAlgorithm_width: Property = Property(name="width", type=IntegerType)
mm_algorithms_GraphicsAlgorithm_height: Property = Property(name="height", type=IntegerType)
mm_algorithms_GraphicsAlgorithm_x: Property = Property(name="x", type=IntegerType)
mm_algorithms_GraphicsAlgorithm_y: Property = Property(name="y", type=IntegerType)
mm_algorithms_GraphicsAlgorithm.attributes={mm_algorithms_GraphicsAlgorithm_height, mm_algorithms_GraphicsAlgorithm_x, mm_algorithms_GraphicsAlgorithm_width, mm_algorithms_GraphicsAlgorithm_y}

# styles_AbstractStyle class attributes and methods

# mm_pictograms_ChopboxAnchor class attributes and methods

# mm_pictograms_ConnectionDecorator class attributes and methods
mm_pictograms_ConnectionDecorator_locationRelative: Property = Property(name="locationRelative", type=BooleanType)
mm_pictograms_ConnectionDecorator_location: Property = Property(name="location", type=FloatType)
mm_pictograms_ConnectionDecorator.attributes={mm_pictograms_ConnectionDecorator_locationRelative, mm_pictograms_ConnectionDecorator_location}

# mm_pictograms_FreeFormConnection class attributes and methods

# mm_pictograms_ManhattanConnection class attributes and methods

# mm_pictograms_PictogramLink class attributes and methods

# pictograms_mm_EObject class attributes and methods

# mm_pictograms_AdvancedAnchor class attributes and methods
mm_pictograms_AdvancedAnchor_useAnchorLocationAsConnectionEndpoint: Property = Property(name="useAnchorLocationAsConnectionEndpoint", type=BooleanType)
mm_pictograms_AdvancedAnchor.attributes={mm_pictograms_AdvancedAnchor_useAnchorLocationAsConnectionEndpoint}

# mm_pictograms_CurvedConnection class attributes and methods

# styles_PrecisionPoint class attributes and methods

# mm_pictograms_CompositeConnection class attributes and methods

# CurvedConnection class attributes and methods

# mm_algorithms_Text class attributes and methods

# AbstractText class attributes and methods

# mm_algorithms_Polygon class attributes and methods

# Polyline class attributes and methods

# mm_algorithms_Rectangle class attributes and methods

# mm_algorithms_RoundedRectangle class attributes and methods
mm_algorithms_RoundedRectangle_cornerHeight: Property = Property(name="cornerHeight", type=IntegerType)
mm_algorithms_RoundedRectangle_cornerWidth: Property = Property(name="cornerWidth", type=IntegerType)
mm_algorithms_RoundedRectangle.attributes={mm_algorithms_RoundedRectangle_cornerHeight, mm_algorithms_RoundedRectangle_cornerWidth}

# mm_algorithms_Polyline class attributes and methods

# mm_algorithms_Ellipse class attributes and methods

# styles_TextStyleRegion class attributes and methods

# mm_algorithms_MultiText class attributes and methods

# mm_algorithms_Image class attributes and methods
mm_algorithms_Image_id: Property = Property(name="id", type=StringType)
mm_algorithms_Image_stretchH: Property = Property(name="stretchH", type=StringType)
mm_algorithms_Image_stretchV: Property = Property(name="stretchV", type=StringType)
mm_algorithms_Image_proportional: Property = Property(name="proportional", type=StringType)
mm_algorithms_Image.attributes={mm_algorithms_Image_stretchH, mm_algorithms_Image_stretchV, mm_algorithms_Image_proportional, mm_algorithms_Image_id}

# mm_algorithms_PlatformGraphicsAlgorithm class attributes and methods
mm_algorithms_PlatformGraphicsAlgorithm_id: Property = Property(name="id", type=StringType)
mm_algorithms_PlatformGraphicsAlgorithm.attributes={mm_algorithms_PlatformGraphicsAlgorithm_id}

# mm_algorithms_AbstractText class attributes and methods
mm_algorithms_AbstractText_angle: Property = Property(name="angle", type=StringType)
mm_algorithms_AbstractText_value: Property = Property(name="value", type=StringType)
mm_algorithms_AbstractText_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
mm_algorithms_AbstractText_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
mm_algorithms_AbstractText.attributes={mm_algorithms_AbstractText_verticalAlignment, mm_algorithms_AbstractText_value, mm_algorithms_AbstractText_horizontalAlignment, mm_algorithms_AbstractText_angle}

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
mm_styles_Style.attributes={mm_styles_Style_angle, mm_styles_Style_description, mm_styles_Style_verticalAlignment, mm_styles_Style_stretchV, mm_styles_Style_id, mm_styles_Style_proportional, mm_styles_Style_stretchH, mm_styles_Style_horizontalAlignment}

# mm_styles_GradientColoredArea class attributes and methods

# mm_styles_RenderingStyle class attributes and methods

# styles_GradientColoredLocation class attributes and methods

# mm_styles_GradientColoredAreas class attributes and methods
mm_styles_GradientColoredAreas_styleAdaption: Property = Property(name="styleAdaption", type=StringType)
mm_styles_GradientColoredAreas.attributes={mm_styles_GradientColoredAreas_styleAdaption}

# styles_GradientColoredArea class attributes and methods

# mm_styles_AdaptedGradientColoredAreas class attributes and methods
mm_styles_AdaptedGradientColoredAreas_definedStyleId: Property = Property(name="definedStyleId", type=StringType)
mm_styles_AdaptedGradientColoredAreas_gradientType: Property = Property(name="gradientType", type=StringType)
mm_styles_AdaptedGradientColoredAreas.attributes={mm_styles_AdaptedGradientColoredAreas_definedStyleId, mm_styles_AdaptedGradientColoredAreas_gradientType}

# styles_GradientColoredAreas class attributes and methods

# mm_styles_Font class attributes and methods
mm_styles_Font_name: Property = Property(name="name", type=StringType)
mm_styles_Font_size: Property = Property(name="size", type=IntegerType)
mm_styles_Font_italic: Property = Property(name="italic", type=BooleanType)
mm_styles_Font_bold: Property = Property(name="bold", type=BooleanType)
mm_styles_Font.attributes={mm_styles_Font_italic, mm_styles_Font_bold, mm_styles_Font_size, mm_styles_Font_name}

# styles_mm_StyleContainer class attributes and methods

# mm_styles_AbstractStyle class attributes and methods
mm_styles_AbstractStyle_lineWidth: Property = Property(name="lineWidth", type=StringType)
mm_styles_AbstractStyle_lineStyle: Property = Property(name="lineStyle", type=StringType)
mm_styles_AbstractStyle_filled: Property = Property(name="filled", type=StringType)
mm_styles_AbstractStyle_lineVisible: Property = Property(name="lineVisible", type=StringType)
mm_styles_AbstractStyle_transparency: Property = Property(name="transparency", type=StringType)
mm_styles_AbstractStyle.attributes={mm_styles_AbstractStyle_transparency, mm_styles_AbstractStyle_lineVisible, mm_styles_AbstractStyle_lineWidth, mm_styles_AbstractStyle_filled, mm_styles_AbstractStyle_lineStyle}

# styles_RenderingStyle class attributes and methods

# mm_styles_GradientColoredLocation class attributes and methods
mm_styles_GradientColoredLocation_locationType: Property = Property(name="locationType", type=StringType)
mm_styles_GradientColoredLocation_locationValue: Property = Property(name="locationValue", type=StringType)
mm_styles_GradientColoredLocation.attributes={mm_styles_GradientColoredLocation_locationValue, mm_styles_GradientColoredLocation_locationType}

# mm_styles_TextStyleRegion class attributes and methods
mm_styles_TextStyleRegion_start: Property = Property(name="start", type=IntegerType)
mm_styles_TextStyleRegion_end: Property = Property(name="end", type=IntegerType)
mm_styles_TextStyleRegion.attributes={mm_styles_TextStyleRegion_start, mm_styles_TextStyleRegion_end}

# styles_TextStyle class attributes and methods

# mm_styles_Point class attributes and methods
mm_styles_Point_x: Property = Property(name="x", type=IntegerType)
mm_styles_Point_y: Property = Property(name="y", type=IntegerType)
mm_styles_Point_before: Property = Property(name="before", type=IntegerType)
mm_styles_Point_after: Property = Property(name="after", type=IntegerType)
mm_styles_Point.attributes={mm_styles_Point_after, mm_styles_Point_before, mm_styles_Point_x, mm_styles_Point_y}

# mm_styles_Color class attributes and methods
mm_styles_Color_red: Property = Property(name="red", type=IntegerType)
mm_styles_Color_green: Property = Property(name="green", type=IntegerType)
mm_styles_Color_blue: Property = Property(name="blue", type=IntegerType)
mm_styles_Color.attributes={mm_styles_Color_green, mm_styles_Color_red, mm_styles_Color_blue}

# mm_styles_PrecisionPoint class attributes and methods
mm_styles_PrecisionPoint_x: Property = Property(name="x", type=FloatType)
mm_styles_PrecisionPoint_y: Property = Property(name="y", type=FloatType)
mm_styles_PrecisionPoint.attributes={mm_styles_PrecisionPoint_x, mm_styles_PrecisionPoint_y}

# mm_styles_TextStyle class attributes and methods
mm_styles_TextStyle_underline: Property = Property(name="underline", type=BooleanType)
mm_styles_TextStyle_underlineStyle: Property = Property(name="underlineStyle", type=StringType)
mm_styles_TextStyle_strikeout: Property = Property(name="strikeout", type=BooleanType)
mm_styles_TextStyle.attributes={mm_styles_TextStyle_underline, mm_styles_TextStyle_underlineStyle, mm_styles_TextStyle_strikeout}

# Relationships
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="pictograms4", type=mm_pictograms_ContainerShape, multiplicity=Multiplicity(1, 1)),
        Property(name="Shape", type=Shape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections5: BinaryAssociation = BinaryAssociation(
    name="connections5",
    ends={
        Property(name="pictograms6", type=mm_pictograms_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="Connection", type=Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
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
        Property(name="styles_Style", type=mm_StyleContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_StyleContainer", type=styles_Style, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container2: BinaryAssociation = BinaryAssociation(
    name="container2",
    ends={
        Property(name="pictograms", type=mm_pictograms_Shape, multiplicity=Multiplicity(1, 1)),
        Property(name="ContainerShape", type=ContainerShape, multiplicity=Multiplicity(0, 1))
    }
)
outgoingConnections27: BinaryAssociation = BinaryAssociation(
    name="outgoingConnections27",
    ends={
        Property(name="pictograms29", type=mm_pictograms_Anchor, multiplicity=Multiplicity(1, 1)),
        Property(name="Connection28", type=Connection, multiplicity=Multiplicity(0, 9999))
    }
)
incomingConnections30: BinaryAssociation = BinaryAssociation(
    name="incomingConnections30",
    ends={
        Property(name="pictograms32", type=mm_pictograms_Anchor, multiplicity=Multiplicity(1, 1)),
        Property(name="Connection31", type=Connection, multiplicity=Multiplicity(0, 9999))
    }
)
referencedGraphicsAlgorithm33: BinaryAssociation = BinaryAssociation(
    name="referencedGraphicsAlgorithm33",
    ends={
        Property(name="GraphicsAlgorithm34", type=mm_pictograms_Anchor, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_Anchor", type=GraphicsAlgorithm, multiplicity=Multiplicity(0, 1))
    }
)
anchors35: BinaryAssociation = BinaryAssociation(
    name="anchors35",
    ends={
        Property(name="pictograms37", type=mm_pictograms_AnchorContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="Anchor36", type=Anchor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location38: BinaryAssociation = BinaryAssociation(
    name="location38",
    ends={
        Property(name="styles_Point", type=mm_pictograms_FixPointAnchor, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_FixPointAnchor", type=styles_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
colors7: BinaryAssociation = BinaryAssociation(
    name="colors7",
    ends={
        Property(name="styles_Color", type=mm_pictograms_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_Diagram", type=styles_Color, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fonts8: BinaryAssociation = BinaryAssociation(
    name="fonts8",
    ends={
        Property(name="styles_Font", type=mm_pictograms_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_Diagram9", type=styles_Font, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pictogramLinks10: BinaryAssociation = BinaryAssociation(
    name="pictogramLinks10",
    ends={
        Property(name="PictogramLink", type=mm_pictograms_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_Diagram11", type=PictogramLink, multiplicity=Multiplicity(0, 9999))
    }
)
graphicsAlgorithm12: BinaryAssociation = BinaryAssociation(
    name="graphicsAlgorithm12",
    ends={
        Property(name="algorithms", type=mm_pictograms_PictogramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphicsAlgorithm", type=GraphicsAlgorithm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
link13: BinaryAssociation = BinaryAssociation(
    name="link13",
    ends={
        Property(name="pictograms15", type=mm_pictograms_PictogramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PictogramLink14", type=PictogramLink, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start16: BinaryAssociation = BinaryAssociation(
    name="start16",
    ends={
        Property(name="pictograms17", type=mm_pictograms_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="Anchor", type=Anchor, multiplicity=Multiplicity(1, 1))
    }
)
end18: BinaryAssociation = BinaryAssociation(
    name="end18",
    ends={
        Property(name="pictograms20", type=mm_pictograms_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="Anchor19", type=Anchor, multiplicity=Multiplicity(1, 1))
    }
)
parent21: BinaryAssociation = BinaryAssociation(
    name="parent21",
    ends={
        Property(name="pictograms22", type=mm_pictograms_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="Diagram", type=Diagram, multiplicity=Multiplicity(1, 1))
    }
)
connectionDecorators23: BinaryAssociation = BinaryAssociation(
    name="connectionDecorators23",
    ends={
        Property(name="pictograms24", type=mm_pictograms_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="ConnectionDecorator", type=ConnectionDecorator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent25: BinaryAssociation = BinaryAssociation(
    name="parent25",
    ends={
        Property(name="pictograms26", type=mm_pictograms_Anchor, multiplicity=Multiplicity(1, 1)),
        Property(name="AnchorContainer", type=AnchorContainer, multiplicity=Multiplicity(1, 1))
    }
)
graphicsAlgorithmChildren49: BinaryAssociation = BinaryAssociation(
    name="graphicsAlgorithmChildren49",
    ends={
        Property(name="algorithms51", type=mm_algorithms_GraphicsAlgorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphicsAlgorithm50", type=GraphicsAlgorithm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentGraphicsAlgorithm52: BinaryAssociation = BinaryAssociation(
    name="parentGraphicsAlgorithm52",
    ends={
        Property(name="algorithms54", type=mm_algorithms_GraphicsAlgorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphicsAlgorithm53", type=GraphicsAlgorithm, multiplicity=Multiplicity(0, 1))
    }
)
connection39: BinaryAssociation = BinaryAssociation(
    name="connection39",
    ends={
        Property(name="pictograms41", type=mm_pictograms_ConnectionDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="Connection40", type=Connection, multiplicity=Multiplicity(1, 1))
    }
)
bendpoints42: BinaryAssociation = BinaryAssociation(
    name="bendpoints42",
    ends={
        Property(name="styles_Point43", type=mm_pictograms_FreeFormConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_FreeFormConnection", type=styles_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pictogramElement44: BinaryAssociation = BinaryAssociation(
    name="pictogramElement44",
    ends={
        Property(name="pictograms45", type=mm_pictograms_PictogramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="PictogramElement", type=PictogramElement, multiplicity=Multiplicity(0, 1))
    }
)
businessObjects46: BinaryAssociation = BinaryAssociation(
    name="businessObjects46",
    ends={
        Property(name="pictograms_mm_EObject", type=mm_pictograms_PictogramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_PictogramLink", type=pictograms_mm_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
controlPoints47: BinaryAssociation = BinaryAssociation(
    name="controlPoints47",
    ends={
        Property(name="styles_PrecisionPoint", type=mm_pictograms_CurvedConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_CurvedConnection", type=styles_PrecisionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children48: BinaryAssociation = BinaryAssociation(
    name="children48",
    ends={
        Property(name="CurvedConnection", type=mm_pictograms_CompositeConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_pictograms_CompositeConnection", type=CurvedConnection, multiplicity=Multiplicity(0, 9999))
    }
)
pictogramElement55: BinaryAssociation = BinaryAssociation(
    name="pictogramElement55",
    ends={
        Property(name="pictograms57", type=mm_algorithms_GraphicsAlgorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="PictogramElement56", type=PictogramElement, multiplicity=Multiplicity(0, 1))
    }
)
style58: BinaryAssociation = BinaryAssociation(
    name="style58",
    ends={
        Property(name="styles_Style59", type=mm_algorithms_GraphicsAlgorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_algorithms_GraphicsAlgorithm", type=styles_Style, multiplicity=Multiplicity(0, 1))
    }
)
points60: BinaryAssociation = BinaryAssociation(
    name="points60",
    ends={
        Property(name="styles_Point61", type=mm_algorithms_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_algorithms_Polyline", type=styles_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styleRegions64: BinaryAssociation = BinaryAssociation(
    name="styleRegions64",
    ends={
        Property(name="styles_TextStyleRegion", type=mm_algorithms_AbstractText, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_algorithms_AbstractText65", type=styles_TextStyleRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
font62: BinaryAssociation = BinaryAssociation(
    name="font62",
    ends={
        Property(name="styles_Font63", type=mm_algorithms_AbstractText, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_algorithms_AbstractText", type=styles_Font, multiplicity=Multiplicity(0, 1))
    }
)
adaptedGradientColoredAreas66: BinaryAssociation = BinaryAssociation(
    name="adaptedGradientColoredAreas66",
    ends={
        Property(name="styles_AdaptedGradientColoredAreas", type=mm_styles_RenderingStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_RenderingStyle", type=styles_AdaptedGradientColoredAreas, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font67: BinaryAssociation = BinaryAssociation(
    name="font67",
    ends={
        Property(name="styles_Font68", type=mm_styles_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_Style", type=styles_Font, multiplicity=Multiplicity(0, 1))
    }
)
start80: BinaryAssociation = BinaryAssociation(
    name="start80",
    ends={
        Property(name="styles_GradientColoredLocation", type=mm_styles_GradientColoredArea, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_GradientColoredArea", type=styles_GradientColoredLocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end81: BinaryAssociation = BinaryAssociation(
    name="end81",
    ends={
        Property(name="styles_GradientColoredLocation83", type=mm_styles_GradientColoredArea, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_GradientColoredArea82", type=styles_GradientColoredLocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gradientColor84: BinaryAssociation = BinaryAssociation(
    name="gradientColor84",
    ends={
        Property(name="styles_GradientColoredArea", type=mm_styles_GradientColoredAreas, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_GradientColoredAreas", type=styles_GradientColoredArea, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
adaptedGradientColoredAreas85: BinaryAssociation = BinaryAssociation(
    name="adaptedGradientColoredAreas85",
    ends={
        Property(name="styles_GradientColoredAreas", type=mm_styles_AdaptedGradientColoredAreas, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_AdaptedGradientColoredAreas", type=styles_GradientColoredAreas, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styleContainer69: BinaryAssociation = BinaryAssociation(
    name="styleContainer69",
    ends={
        Property(name="styles_mm_StyleContainer", type=mm_styles_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_Style70", type=styles_mm_StyleContainer, multiplicity=Multiplicity(1, 1))
    }
)
background71: BinaryAssociation = BinaryAssociation(
    name="background71",
    ends={
        Property(name="styles_Color72", type=mm_styles_AbstractStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_AbstractStyle", type=styles_Color, multiplicity=Multiplicity(0, 1))
    }
)
foreground73: BinaryAssociation = BinaryAssociation(
    name="foreground73",
    ends={
        Property(name="styles_Color75", type=mm_styles_AbstractStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_AbstractStyle74", type=styles_Color, multiplicity=Multiplicity(0, 1))
    }
)
renderingStyle76: BinaryAssociation = BinaryAssociation(
    name="renderingStyle76",
    ends={
        Property(name="styles_RenderingStyle", type=mm_styles_AbstractStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_AbstractStyle77", type=styles_RenderingStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color78: BinaryAssociation = BinaryAssociation(
    name="color78",
    ends={
        Property(name="styles_Color79", type=mm_styles_GradientColoredLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_GradientColoredLocation", type=styles_Color, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
foreground88: BinaryAssociation = BinaryAssociation(
    name="foreground88",
    ends={
        Property(name="styles_Color90", type=mm_styles_TextStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_TextStyle89", type=styles_Color, multiplicity=Multiplicity(0, 1))
    }
)
background91: BinaryAssociation = BinaryAssociation(
    name="background91",
    ends={
        Property(name="styles_Color93", type=mm_styles_TextStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_TextStyle92", type=styles_Color, multiplicity=Multiplicity(0, 1))
    }
)
underlineColor94: BinaryAssociation = BinaryAssociation(
    name="underlineColor94",
    ends={
        Property(name="styles_Color96", type=mm_styles_TextStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_TextStyle95", type=styles_Color, multiplicity=Multiplicity(0, 1))
    }
)
strikeoutColor97: BinaryAssociation = BinaryAssociation(
    name="strikeoutColor97",
    ends={
        Property(name="styles_Color99", type=mm_styles_TextStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_TextStyle98", type=styles_Color, multiplicity=Multiplicity(0, 1))
    }
)
style100: BinaryAssociation = BinaryAssociation(
    name="style100",
    ends={
        Property(name="styles_TextStyle", type=mm_styles_TextStyleRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_TextStyleRegion", type=styles_TextStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
font86: BinaryAssociation = BinaryAssociation(
    name="font86",
    ends={
        Property(name="styles_Font87", type=mm_styles_TextStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="mm_styles_TextStyle", type=styles_Font, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_mm_pictograms_ContainerShape_Shape = Generalization(general=Shape, specific=mm_pictograms_ContainerShape)
gen_mm_pictograms_Diagram_pictograms_ContainerShape = Generalization(general=pictograms_ContainerShape, specific=mm_pictograms_Diagram)
gen_mm_pictograms_Diagram_StyleContainer = Generalization(general=StyleContainer, specific=mm_pictograms_Diagram)
gen_mm_GraphicsAlgorithmContainer_PropertyContainer = Generalization(general=PropertyContainer, specific=mm_GraphicsAlgorithmContainer)
gen_mm_pictograms_Shape_AnchorContainer = Generalization(general=AnchorContainer, specific=mm_pictograms_Shape)
gen_mm_pictograms_AnchorContainer_PictogramElement = Generalization(general=PictogramElement, specific=mm_pictograms_AnchorContainer)
gen_mm_pictograms_FixPointAnchor_AdvancedAnchor = Generalization(general=AdvancedAnchor, specific=mm_pictograms_FixPointAnchor)
gen_mm_pictograms_BoxRelativeAnchor_AdvancedAnchor = Generalization(general=AdvancedAnchor, specific=mm_pictograms_BoxRelativeAnchor)
gen_mm_pictograms_PictogramElement_GraphicsAlgorithmContainer = Generalization(general=GraphicsAlgorithmContainer, specific=mm_pictograms_PictogramElement)
gen_mm_pictograms_Connection_AnchorContainer = Generalization(general=AnchorContainer, specific=mm_pictograms_Connection)
gen_mm_pictograms_Anchor_PictogramElement = Generalization(general=PictogramElement, specific=mm_pictograms_Anchor)
gen_mm_algorithms_GraphicsAlgorithm_GraphicsAlgorithmContainer = Generalization(general=GraphicsAlgorithmContainer, specific=mm_algorithms_GraphicsAlgorithm)
gen_mm_algorithms_GraphicsAlgorithm_styles_AbstractStyle = Generalization(general=styles_AbstractStyle, specific=mm_algorithms_GraphicsAlgorithm)
gen_mm_pictograms_ChopboxAnchor_Anchor = Generalization(general=Anchor, specific=mm_pictograms_ChopboxAnchor)
gen_mm_pictograms_ConnectionDecorator_Shape = Generalization(general=Shape, specific=mm_pictograms_ConnectionDecorator)
gen_mm_pictograms_FreeFormConnection_Connection = Generalization(general=Connection, specific=mm_pictograms_FreeFormConnection)
gen_mm_pictograms_ManhattanConnection_Connection = Generalization(general=Connection, specific=mm_pictograms_ManhattanConnection)
gen_mm_pictograms_PictogramLink_PropertyContainer = Generalization(general=PropertyContainer, specific=mm_pictograms_PictogramLink)
gen_mm_pictograms_AdvancedAnchor_Anchor = Generalization(general=Anchor, specific=mm_pictograms_AdvancedAnchor)
gen_mm_pictograms_CurvedConnection_Connection = Generalization(general=Connection, specific=mm_pictograms_CurvedConnection)
gen_mm_pictograms_CompositeConnection_Connection = Generalization(general=Connection, specific=mm_pictograms_CompositeConnection)
gen_mm_algorithms_Text_AbstractText = Generalization(general=AbstractText, specific=mm_algorithms_Text)
gen_mm_algorithms_Polygon_Polyline = Generalization(general=Polyline, specific=mm_algorithms_Polygon)
gen_mm_algorithms_Rectangle_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_Rectangle)
gen_mm_algorithms_RoundedRectangle_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_RoundedRectangle)
gen_mm_algorithms_Polyline_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_Polyline)
gen_mm_algorithms_Ellipse_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_Ellipse)
gen_mm_algorithms_MultiText_AbstractText = Generalization(general=AbstractText, specific=mm_algorithms_MultiText)
gen_mm_algorithms_Image_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_Image)
gen_mm_algorithms_PlatformGraphicsAlgorithm_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_PlatformGraphicsAlgorithm)
gen_mm_algorithms_AbstractText_GraphicsAlgorithm = Generalization(general=GraphicsAlgorithm, specific=mm_algorithms_AbstractText)
gen_mm_styles_Style_StyleContainer = Generalization(general=StyleContainer, specific=mm_styles_Style)
gen_mm_styles_Style_styles_AbstractStyle = Generalization(general=styles_AbstractStyle, specific=mm_styles_Style)

# Domain Model
domain_model = DomainModel(
    name="mm",
    types={mm_pictograms_ContainerShape, Shape, mm_pictograms_Diagram, pictograms_ContainerShape, StyleContainer, Connection, mm_Property, mm_PropertyContainer, mm_GraphicsAlgorithmContainer, PropertyContainer, mm_StyleContainer, styles_Style, mm_pictograms_Shape, AnchorContainer, ContainerShape, mm_pictograms_AnchorContainer, mm_pictograms_FixPointAnchor, AdvancedAnchor, styles_Point, mm_pictograms_BoxRelativeAnchor, styles_Color, styles_Font, PictogramLink, mm_pictograms_PictogramElement, GraphicsAlgorithmContainer, GraphicsAlgorithm, mm_pictograms_Connection, Anchor, Diagram, ConnectionDecorator, mm_pictograms_Anchor, PictogramElement, mm_algorithms_GraphicsAlgorithm, styles_AbstractStyle, mm_pictograms_ChopboxAnchor, mm_pictograms_ConnectionDecorator, mm_pictograms_FreeFormConnection, mm_pictograms_ManhattanConnection, mm_pictograms_PictogramLink, pictograms_mm_EObject, mm_pictograms_AdvancedAnchor, mm_pictograms_CurvedConnection, styles_PrecisionPoint, mm_pictograms_CompositeConnection, CurvedConnection, mm_algorithms_Text, AbstractText, mm_algorithms_Polygon, Polyline, mm_algorithms_Rectangle, mm_algorithms_RoundedRectangle, mm_algorithms_Polyline, mm_algorithms_Ellipse, styles_TextStyleRegion, mm_algorithms_MultiText, mm_algorithms_Image, mm_algorithms_PlatformGraphicsAlgorithm, mm_algorithms_AbstractText, styles_AdaptedGradientColoredAreas, mm_styles_Style, mm_styles_GradientColoredArea, mm_styles_RenderingStyle, styles_GradientColoredLocation, mm_styles_GradientColoredAreas, styles_GradientColoredArea, mm_styles_AdaptedGradientColoredAreas, styles_GradientColoredAreas, mm_styles_Font, styles_mm_StyleContainer, mm_styles_AbstractStyle, styles_RenderingStyle, mm_styles_GradientColoredLocation, mm_styles_TextStyleRegion, styles_TextStyle, mm_styles_Point, mm_styles_Color, mm_styles_PrecisionPoint, mm_styles_TextStyle, LineStyle, Orientation, LocationType, UnderlineStyle},
    associations={children3, connections5, properties0, styles1, container2, outgoingConnections27, incomingConnections30, referencedGraphicsAlgorithm33, anchors35, location38, colors7, fonts8, pictogramLinks10, graphicsAlgorithm12, link13, start16, end18, parent21, connectionDecorators23, parent25, graphicsAlgorithmChildren49, parentGraphicsAlgorithm52, connection39, bendpoints42, pictogramElement44, businessObjects46, controlPoints47, children48, pictogramElement55, style58, points60, styleRegions64, font62, adaptedGradientColoredAreas66, font67, start80, end81, gradientColor84, adaptedGradientColoredAreas85, styleContainer69, background71, foreground73, renderingStyle76, color78, foreground88, background91, underlineColor94, strikeoutColor97, style100, font86},
    generalizations={gen_mm_pictograms_ContainerShape_Shape, gen_mm_pictograms_Diagram_pictograms_ContainerShape, gen_mm_pictograms_Diagram_StyleContainer, gen_mm_GraphicsAlgorithmContainer_PropertyContainer, gen_mm_pictograms_Shape_AnchorContainer, gen_mm_pictograms_AnchorContainer_PictogramElement, gen_mm_pictograms_FixPointAnchor_AdvancedAnchor, gen_mm_pictograms_BoxRelativeAnchor_AdvancedAnchor, gen_mm_pictograms_PictogramElement_GraphicsAlgorithmContainer, gen_mm_pictograms_Connection_AnchorContainer, gen_mm_pictograms_Anchor_PictogramElement, gen_mm_algorithms_GraphicsAlgorithm_GraphicsAlgorithmContainer, gen_mm_algorithms_GraphicsAlgorithm_styles_AbstractStyle, gen_mm_pictograms_ChopboxAnchor_Anchor, gen_mm_pictograms_ConnectionDecorator_Shape, gen_mm_pictograms_FreeFormConnection_Connection, gen_mm_pictograms_ManhattanConnection_Connection, gen_mm_pictograms_PictogramLink_PropertyContainer, gen_mm_pictograms_AdvancedAnchor_Anchor, gen_mm_pictograms_CurvedConnection_Connection, gen_mm_pictograms_CompositeConnection_Connection, gen_mm_algorithms_Text_AbstractText, gen_mm_algorithms_Polygon_Polyline, gen_mm_algorithms_Rectangle_GraphicsAlgorithm, gen_mm_algorithms_RoundedRectangle_GraphicsAlgorithm, gen_mm_algorithms_Polyline_GraphicsAlgorithm, gen_mm_algorithms_Ellipse_GraphicsAlgorithm, gen_mm_algorithms_MultiText_AbstractText, gen_mm_algorithms_Image_GraphicsAlgorithm, gen_mm_algorithms_PlatformGraphicsAlgorithm_GraphicsAlgorithm, gen_mm_algorithms_AbstractText_GraphicsAlgorithm, gen_mm_styles_Style_StyleContainer, gen_mm_styles_Style_styles_AbstractStyle},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)