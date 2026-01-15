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
Sorting: Enumeration = Enumeration(
    name="Sorting",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Manual"),
			EnumerationLiteral(name="Automatic")
    }
)

Filtering: Enumeration = Enumeration(
    name="Filtering",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Manual"),
			EnumerationLiteral(name="Automatic")
    }
)

Routing: Enumeration = Enumeration(
    name="Routing",
    literals={
            EnumerationLiteral(name="Manual"),
			EnumerationLiteral(name="Rectilinear"),
			EnumerationLiteral(name="Tree")
    }
)

Smoothness: Enumeration = Enumeration(
    name="Smoothness",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Normal"),
			EnumerationLiteral(name="Less"),
			EnumerationLiteral(name="More")
    }
)

JumpLinkStatus: Enumeration = Enumeration(
    name="JumpLinkStatus",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="All"),
			EnumerationLiteral(name="Below"),
			EnumerationLiteral(name="Above")
    }
)

JumpLinkType: Enumeration = Enumeration(
    name="JumpLinkType",
    literals={
            EnumerationLiteral(name="Semicircle"),
			EnumerationLiteral(name="Square"),
			EnumerationLiteral(name="Chamfered")
    }
)

Alignment: Enumeration = Enumeration(
    name="Alignment",
    literals={
            EnumerationLiteral(name="Left"),
			EnumerationLiteral(name="Right"),
			EnumerationLiteral(name="Center"),
			EnumerationLiteral(name="Top"),
			EnumerationLiteral(name="Bottom")
    }
)

SortingDirection: Enumeration = Enumeration(
    name="SortingDirection",
    literals={
            EnumerationLiteral(name="Ascending"),
			EnumerationLiteral(name="Descending")
    }
)

MeasurementUnit: Enumeration = Enumeration(
    name="MeasurementUnit",
    literals={
            EnumerationLiteral(name="Himetric"),
			EnumerationLiteral(name="Pixel")
    }
)

TextAlignment: Enumeration = Enumeration(
    name="TextAlignment",
    literals={
            EnumerationLiteral(name="Left"),
			EnumerationLiteral(name="Right"),
			EnumerationLiteral(name="Center")
    }
)

LineType: Enumeration = Enumeration(
    name="LineType",
    literals={
            EnumerationLiteral(name="Solid"),
			EnumerationLiteral(name="Dash"),
			EnumerationLiteral(name="Dot"),
			EnumerationLiteral(name="DashDot"),
			EnumerationLiteral(name="DashDotDot"),
			EnumerationLiteral(name="Double")
    }
)

ArrowType: Enumeration = Enumeration(
    name="ArrowType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="OpenArrow"),
			EnumerationLiteral(name="SolidArrow")
    }
)

GradientStyle: Enumeration = Enumeration(
    name="GradientStyle",
    literals={
            EnumerationLiteral(name="Vertical"),
			EnumerationLiteral(name="Horizontal")
    }
)

# Classes
notation_Edge = Class(name="notation::Edge")
View = Class(name="View")
notation_View = Class(name="notation::View", is_abstract=True)
notation_Bendpoints = Class(name="notation::Bendpoints", is_abstract=True)
notation_Anchor = Class(name="notation::Anchor", is_abstract=True)
notation_Node = Class(name="notation::Node")
notation_LayoutConstraint = Class(name="notation::LayoutConstraint", is_abstract=True)
notation_Style = Class(name="notation::Style", is_abstract=True)
notation_FillStyle = Class(name="notation::FillStyle")
Style = Class(name="Style")
notation_LineStyle = Class(name="notation::LineStyle")
notation_TitleStyle = Class(name="notation::TitleStyle")
notation_SortingStyle = Class(name="notation::SortingStyle")
notation_EObject = Class(name="notation::EObject")
notation_DescriptionStyle = Class(name="notation::DescriptionStyle")
notation_Size = Class(name="notation::Size")
LayoutConstraint = Class(name="LayoutConstraint")
notation_Location = Class(name="notation::Location")
notation_Bounds = Class(name="notation::Bounds")
Location = Class(name="Location")
Size = Class(name="Size")
notation_Ratio = Class(name="notation::Ratio")
notation_IdentityAnchor = Class(name="notation::IdentityAnchor")
Anchor = Class(name="Anchor")
notation_FontStyle = Class(name="notation::FontStyle")
notation_RoutingStyle = Class(name="notation::RoutingStyle")
RoundedCornersStyle = Class(name="RoundedCornersStyle")
EModelElement = Class(name="EModelElement")
notation_Diagram = Class(name="notation::Diagram")
notation_RelativeBendpoints = Class(name="notation::RelativeBendpoints")
Bendpoints = Class(name="Bendpoints")
notation_Image = Class(name="notation::Image")
notation_CanonicalStyle = Class(name="notation::CanonicalStyle")
notation_ShapeStyle = Class(name="notation::ShapeStyle")
FontStyle = Class(name="FontStyle")
DescriptionStyle = Class(name="DescriptionStyle")
FillStyle = Class(name="FillStyle")
LineStyle = Class(name="LineStyle")
notation_ConnectorStyle = Class(name="notation::ConnectorStyle")
RoutingStyle = Class(name="RoutingStyle")
notation_PageStyle = Class(name="notation::PageStyle")
notation_DrawerStyle = Class(name="notation::DrawerStyle")
notation_GuideStyle = Class(name="notation::GuideStyle")
notation_Guide = Class(name="notation::Guide")
notation_NodeEntry = Class(name="notation::NodeEntry")
notation_FilteringStyle = Class(name="notation::FilteringStyle")
notation_DiagramStyle = Class(name="notation::DiagramStyle")
PageStyle = Class(name="PageStyle")
GuideStyle = Class(name="GuideStyle")
notation_ImageStyle = Class(name="notation::ImageStyle")
notation_ImageBufferStyle = Class(name="notation::ImageBufferStyle")
ImageStyle = Class(name="ImageStyle")
notation_PropertiesSetStyle = Class(name="notation::PropertiesSetStyle")
NamedStyle = Class(name="NamedStyle")
notation_StringToPropertyValueMapEntry = Class(name="notation::StringToPropertyValueMapEntry")
notation_PropertyValue = Class(name="notation::PropertyValue")
StringObjectConverter = Class(name="StringObjectConverter")
notation_EDataType = Class(name="notation::EDataType")
notation_ListValueStyle = Class(name="notation::ListValueStyle")
notation_NamedStyle = Class(name="notation::NamedStyle")
notation_StringObjectConverter = Class(name="notation::StringObjectConverter", is_abstract=True)
notation_DataTypeStyle = Class(name="notation::DataTypeStyle")
notation_IntValueStyle = Class(name="notation::IntValueStyle")
notation_IntListValueStyle = Class(name="notation::IntListValueStyle")
notation_BooleanValueStyle = Class(name="notation::BooleanValueStyle")
notation_DoubleValueStyle = Class(name="notation::DoubleValueStyle")
notation_DoubleListValueStyle = Class(name="notation::DoubleListValueStyle")
notation_StringValueStyle = Class(name="notation::StringValueStyle")
notation_StringListValueStyle = Class(name="notation::StringListValueStyle")
notation_EObjectValueStyle = Class(name="notation::EObjectValueStyle")
notation_EObjectListValueStyle = Class(name="notation::EObjectListValueStyle")
notation_ByteArrayValueStyle = Class(name="notation::ByteArrayValueStyle")
notation_BooleanListValueStyle = Class(name="notation::BooleanListValueStyle")
notation_HintedDiagramLinkStyle = Class(name="notation::HintedDiagramLinkStyle")
DiagramLinkStyle = Class(name="DiagramLinkStyle")
notation_SingleValueStyle = Class(name="notation::SingleValueStyle")
DataTypeStyle = Class(name="DataTypeStyle")
notation_DiagramLinkStyle = Class(name="notation::DiagramLinkStyle")
notation_MultiDiagramLinkStyle = Class(name="notation::MultiDiagramLinkStyle")
notation_TextStyle = Class(name="notation::TextStyle")
notation_LineTypeStyle = Class(name="notation::LineTypeStyle")
notation_ArrowStyle = Class(name="notation::ArrowStyle")
notation_Shape = Class(name="notation::Shape")
Node = Class(name="Node")
ShapeStyle = Class(name="ShapeStyle")
notation_Compartment = Class(name="notation::Compartment")
BasicCompartment = Class(name="BasicCompartment")
CanonicalStyle = Class(name="CanonicalStyle")
TitleStyle = Class(name="TitleStyle")
notation_ListCompartment = Class(name="notation::ListCompartment")
SortingStyle = Class(name="SortingStyle")
FilteringStyle = Class(name="FilteringStyle")
notation_Connector = Class(name="notation::Connector")
Edge = Class(name="Edge")
ConnectorStyle = Class(name="ConnectorStyle")
notation_StandardDiagram = Class(name="notation::StandardDiagram")
Diagram = Class(name="Diagram")
DiagramStyle = Class(name="DiagramStyle")
DrawerStyle = Class(name="DrawerStyle")
notation_BasicSemanticCompartment = Class(name="notation::BasicSemanticCompartment")
notation_SemanticListCompartment = Class(name="notation::SemanticListCompartment")
BasicSemanticCompartment = Class(name="BasicSemanticCompartment")
notation_RoundedCornersStyle = Class(name="notation::RoundedCornersStyle")
notation_DecorationNode = Class(name="notation::DecorationNode")
BasicDecorationNode = Class(name="BasicDecorationNode")
notation_BasicDecorationNode = Class(name="notation::BasicDecorationNode")
notation_BasicCompartment = Class(name="notation::BasicCompartment")
DecorationNode = Class(name="DecorationNode")

# notation_Edge class attributes and methods
notation_Edge_m_createBendpoints: Method = Method(name="createBendpoints", parameters={Parameter(name='eClass')}, type=StringType)
notation_Edge_m_createSourceAnchor: Method = Method(name="createSourceAnchor", parameters={Parameter(name='eClass')}, type=StringType)
notation_Edge_m_createTargetAnchor: Method = Method(name="createTargetAnchor", parameters={Parameter(name='eClass')}, type=StringType)
notation_Edge.methods={notation_Edge_m_createBendpoints, notation_Edge_m_createTargetAnchor, notation_Edge_m_createSourceAnchor}

# View class attributes and methods

# notation_View class attributes and methods
notation_View_visible: Property = Property(name="visible", type=BooleanType)
notation_View_type: Property = Property(name="type", type=StringType)
notation_View_mutable: Property = Property(name="mutable", type=BooleanType)
notation_View_m_getStyle: Method = Method(name="getStyle", parameters={Parameter(name='eClass')}, type=Style)
notation_View_m_createChild: Method = Method(name="createChild", parameters={Parameter(name='eClass')}, type=StringType)
notation_View_m_createStyle: Method = Method(name="createStyle", parameters={Parameter(name='eClass')}, type=Style)
notation_View_m_getNamedStyle: Method = Method(name="getNamedStyle", parameters={Parameter(name='name'), Parameter(name='eClass')}, type=StringType)
notation_View.attributes={notation_View_visible, notation_View_type, notation_View_mutable}
notation_View.methods={notation_View_m_createChild, notation_View_m_getNamedStyle, notation_View_m_getStyle, notation_View_m_createStyle}

# notation_Bendpoints class attributes and methods

# notation_Anchor class attributes and methods

# notation_Node class attributes and methods
notation_Node_m_createLayoutConstraint: Method = Method(name="createLayoutConstraint", parameters={Parameter(name='eClass')}, type=StringType)
notation_Node.methods={notation_Node_m_createLayoutConstraint}

# notation_LayoutConstraint class attributes and methods

# notation_Style class attributes and methods

# notation_FillStyle class attributes and methods
notation_FillStyle_fillColor: Property = Property(name="fillColor", type=IntegerType)
notation_FillStyle_transparency: Property = Property(name="transparency", type=IntegerType)
notation_FillStyle_gradient: Property = Property(name="gradient", type=StringType)
notation_FillStyle.attributes={notation_FillStyle_gradient, notation_FillStyle_fillColor, notation_FillStyle_transparency}

# Style class attributes and methods

# notation_LineStyle class attributes and methods
notation_LineStyle_lineColor: Property = Property(name="lineColor", type=IntegerType)
notation_LineStyle_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
notation_LineStyle.attributes={notation_LineStyle_lineWidth, notation_LineStyle_lineColor}

# notation_TitleStyle class attributes and methods
notation_TitleStyle_showTitle: Property = Property(name="showTitle", type=BooleanType)
notation_TitleStyle.attributes={notation_TitleStyle_showTitle}

# notation_SortingStyle class attributes and methods
notation_SortingStyle_sorting: Property = Property(name="sorting", type=StringType)
notation_SortingStyle_sortingKeys: Property = Property(name="sortingKeys", type=StringType)
notation_SortingStyle.attributes={notation_SortingStyle_sorting, notation_SortingStyle_sortingKeys}

# notation_EObject class attributes and methods

# notation_DescriptionStyle class attributes and methods
notation_DescriptionStyle_description: Property = Property(name="description", type=StringType)
notation_DescriptionStyle.attributes={notation_DescriptionStyle_description}

# notation_Size class attributes and methods
notation_Size_width: Property = Property(name="width", type=IntegerType)
notation_Size_height: Property = Property(name="height", type=IntegerType)
notation_Size.attributes={notation_Size_height, notation_Size_width}

# LayoutConstraint class attributes and methods

# notation_Location class attributes and methods
notation_Location_x: Property = Property(name="x", type=IntegerType)
notation_Location_y: Property = Property(name="y", type=IntegerType)
notation_Location.attributes={notation_Location_y, notation_Location_x}

# notation_Bounds class attributes and methods

# Location class attributes and methods

# Size class attributes and methods

# notation_Ratio class attributes and methods
notation_Ratio_value: Property = Property(name="value", type=FloatType)
notation_Ratio.attributes={notation_Ratio_value}

# notation_IdentityAnchor class attributes and methods
notation_IdentityAnchor_id: Property = Property(name="id", type=StringType)
notation_IdentityAnchor.attributes={notation_IdentityAnchor_id}

# Anchor class attributes and methods

# notation_FontStyle class attributes and methods
notation_FontStyle_fontColor: Property = Property(name="fontColor", type=IntegerType)
notation_FontStyle_fontName: Property = Property(name="fontName", type=StringType)
notation_FontStyle_fontHeight: Property = Property(name="fontHeight", type=IntegerType)
notation_FontStyle_bold: Property = Property(name="bold", type=BooleanType)
notation_FontStyle_italic: Property = Property(name="italic", type=BooleanType)
notation_FontStyle_underline: Property = Property(name="underline", type=BooleanType)
notation_FontStyle_strikeThrough: Property = Property(name="strikeThrough", type=BooleanType)
notation_FontStyle.attributes={notation_FontStyle_underline, notation_FontStyle_fontName, notation_FontStyle_fontHeight, notation_FontStyle_bold, notation_FontStyle_strikeThrough, notation_FontStyle_fontColor, notation_FontStyle_italic}

# notation_RoutingStyle class attributes and methods
notation_RoutingStyle_routing: Property = Property(name="routing", type=StringType)
notation_RoutingStyle_smoothness: Property = Property(name="smoothness", type=StringType)
notation_RoutingStyle_avoidObstructions: Property = Property(name="avoidObstructions", type=BooleanType)
notation_RoutingStyle_closestDistance: Property = Property(name="closestDistance", type=BooleanType)
notation_RoutingStyle_jumpLinkStatus: Property = Property(name="jumpLinkStatus", type=StringType)
notation_RoutingStyle_jumpLinkType: Property = Property(name="jumpLinkType", type=StringType)
notation_RoutingStyle_jumpLinksReverse: Property = Property(name="jumpLinksReverse", type=BooleanType)
notation_RoutingStyle.attributes={notation_RoutingStyle_routing, notation_RoutingStyle_smoothness, notation_RoutingStyle_closestDistance, notation_RoutingStyle_jumpLinksReverse, notation_RoutingStyle_jumpLinkStatus, notation_RoutingStyle_jumpLinkType, notation_RoutingStyle_avoidObstructions}

# RoundedCornersStyle class attributes and methods

# EModelElement class attributes and methods

# notation_Diagram class attributes and methods
notation_Diagram_name: Property = Property(name="name", type=StringType)
notation_Diagram_measurementUnit: Property = Property(name="measurementUnit", type=StringType)
notation_Diagram_m_createEdge: Method = Method(name="createEdge", parameters={Parameter(name='eClass')}, type=StringType)
notation_Diagram.attributes={notation_Diagram_measurementUnit, notation_Diagram_name}
notation_Diagram.methods={notation_Diagram_m_createEdge}

# notation_RelativeBendpoints class attributes and methods
notation_RelativeBendpoints_points: Property = Property(name="points", type=StringType)
notation_RelativeBendpoints.attributes={notation_RelativeBendpoints_points}

# Bendpoints class attributes and methods

# notation_Image class attributes and methods
notation_Image_data: Property = Property(name="data", type=StringType)
notation_Image.attributes={notation_Image_data}

# notation_CanonicalStyle class attributes and methods
notation_CanonicalStyle_canonical: Property = Property(name="canonical", type=BooleanType)
notation_CanonicalStyle.attributes={notation_CanonicalStyle_canonical}

# notation_ShapeStyle class attributes and methods

# FontStyle class attributes and methods

# DescriptionStyle class attributes and methods

# FillStyle class attributes and methods

# LineStyle class attributes and methods

# notation_ConnectorStyle class attributes and methods

# RoutingStyle class attributes and methods

# notation_PageStyle class attributes and methods
notation_PageStyle_pageX: Property = Property(name="pageX", type=IntegerType)
notation_PageStyle_pageY: Property = Property(name="pageY", type=IntegerType)
notation_PageStyle_pageWidth: Property = Property(name="pageWidth", type=IntegerType)
notation_PageStyle_pageHeight: Property = Property(name="pageHeight", type=IntegerType)
notation_PageStyle.attributes={notation_PageStyle_pageHeight, notation_PageStyle_pageWidth, notation_PageStyle_pageY, notation_PageStyle_pageX}

# notation_DrawerStyle class attributes and methods
notation_DrawerStyle_collapsed: Property = Property(name="collapsed", type=BooleanType)
notation_DrawerStyle.attributes={notation_DrawerStyle_collapsed}

# notation_GuideStyle class attributes and methods

# notation_Guide class attributes and methods
notation_Guide_position: Property = Property(name="position", type=IntegerType)
notation_Guide.attributes={notation_Guide_position}

# notation_NodeEntry class attributes and methods
notation_NodeEntry_value: Property = Property(name="value", type=StringType)
notation_NodeEntry.attributes={notation_NodeEntry_value}

# notation_FilteringStyle class attributes and methods
notation_FilteringStyle_filtering: Property = Property(name="filtering", type=StringType)
notation_FilteringStyle_filteringKeys: Property = Property(name="filteringKeys", type=StringType)
notation_FilteringStyle.attributes={notation_FilteringStyle_filtering, notation_FilteringStyle_filteringKeys}

# notation_DiagramStyle class attributes and methods

# PageStyle class attributes and methods

# GuideStyle class attributes and methods

# notation_ImageStyle class attributes and methods
notation_ImageStyle_antiAlias: Property = Property(name="antiAlias", type=StringType)
notation_ImageStyle_maintainAspectRatio: Property = Property(name="maintainAspectRatio", type=StringType)
notation_ImageStyle.attributes={notation_ImageStyle_antiAlias, notation_ImageStyle_maintainAspectRatio}

# notation_ImageBufferStyle class attributes and methods

# ImageStyle class attributes and methods

# notation_PropertiesSetStyle class attributes and methods
notation_PropertiesSetStyle_m_getProperty: Method = Method(name="getProperty", parameters={Parameter(name='propertyName')}, type=StringType)
notation_PropertiesSetStyle_m_setProperty: Method = Method(name="setProperty", parameters={Parameter(name='propertyName'), Parameter(name='newValue')}, type=BooleanType)
notation_PropertiesSetStyle_m_createProperty: Method = Method(name="createProperty", parameters={Parameter(name='initialValue'), Parameter(name='propertyName'), Parameter(name='instanceType')}, type=BooleanType)
notation_PropertiesSetStyle_m_removeProperty: Method = Method(name="removeProperty", parameters={Parameter(name='propertyName')}, type=BooleanType)
notation_PropertiesSetStyle_m_hasProperty: Method = Method(name="hasProperty", parameters={Parameter(name='propertyName')}, type=BooleanType)
notation_PropertiesSetStyle_m_createProperty: Method = Method(name="createProperty", parameters={Parameter(name='initialValue'), Parameter(name='propertyName')}, type=BooleanType)
notation_PropertiesSetStyle.methods={notation_PropertiesSetStyle_m_createProperty, notation_PropertiesSetStyle_m_setProperty, notation_PropertiesSetStyle_m_createProperty, notation_PropertiesSetStyle_m_removeProperty, notation_PropertiesSetStyle_m_getProperty, notation_PropertiesSetStyle_m_hasProperty}

# NamedStyle class attributes and methods

# notation_StringToPropertyValueMapEntry class attributes and methods
notation_StringToPropertyValueMapEntry_key: Property = Property(name="key", type=StringType)
notation_StringToPropertyValueMapEntry.attributes={notation_StringToPropertyValueMapEntry_key}

# notation_PropertyValue class attributes and methods
notation_PropertyValue_rawValue: Property = Property(name="rawValue", type=StringType)
notation_PropertyValue_m_getValue: Method = Method(name="getValue", parameters={}, type=StringType)
notation_PropertyValue_m_setValue: Method = Method(name="setValue", parameters={Parameter(name='newValue')})
notation_PropertyValue.attributes={notation_PropertyValue_rawValue}
notation_PropertyValue.methods={notation_PropertyValue_m_setValue, notation_PropertyValue_m_getValue}

# StringObjectConverter class attributes and methods

# notation_EDataType class attributes and methods

# notation_ListValueStyle class attributes and methods
notation_ListValueStyle_rawValuesList: Property = Property(name="rawValuesList", type=StringType)
notation_ListValueStyle.attributes={notation_ListValueStyle_rawValuesList}

# notation_NamedStyle class attributes and methods
notation_NamedStyle_name: Property = Property(name="name", type=StringType)
notation_NamedStyle.attributes={notation_NamedStyle_name}

# notation_StringObjectConverter class attributes and methods
notation_StringObjectConverter_m_getStringFromObject: Method = Method(name="getStringFromObject", parameters={Parameter(name='objectValue')}, type=StringType)
notation_StringObjectConverter_m_getObjectFromString: Method = Method(name="getObjectFromString", parameters={Parameter(name='stringValue')}, type=StringType)
notation_StringObjectConverter.methods={notation_StringObjectConverter_m_getStringFromObject, notation_StringObjectConverter_m_getObjectFromString}

# notation_DataTypeStyle class attributes and methods

# notation_IntValueStyle class attributes and methods
notation_IntValueStyle_intValue: Property = Property(name="intValue", type=IntegerType)
notation_IntValueStyle.attributes={notation_IntValueStyle_intValue}

# notation_IntListValueStyle class attributes and methods
notation_IntListValueStyle_intListValue: Property = Property(name="intListValue", type=IntegerType)
notation_IntListValueStyle.attributes={notation_IntListValueStyle_intListValue}

# notation_BooleanValueStyle class attributes and methods
notation_BooleanValueStyle_booleanValue: Property = Property(name="booleanValue", type=BooleanType)
notation_BooleanValueStyle.attributes={notation_BooleanValueStyle_booleanValue}

# notation_DoubleValueStyle class attributes and methods
notation_DoubleValueStyle_doubleValue: Property = Property(name="doubleValue", type=FloatType)
notation_DoubleValueStyle.attributes={notation_DoubleValueStyle_doubleValue}

# notation_DoubleListValueStyle class attributes and methods
notation_DoubleListValueStyle_doubleListValue: Property = Property(name="doubleListValue", type=StringType)
notation_DoubleListValueStyle.attributes={notation_DoubleListValueStyle_doubleListValue}

# notation_StringValueStyle class attributes and methods
notation_StringValueStyle_stringValue: Property = Property(name="stringValue", type=StringType)
notation_StringValueStyle.attributes={notation_StringValueStyle_stringValue}

# notation_StringListValueStyle class attributes and methods
notation_StringListValueStyle_stringListValue: Property = Property(name="stringListValue", type=StringType)
notation_StringListValueStyle.attributes={notation_StringListValueStyle_stringListValue}

# notation_EObjectValueStyle class attributes and methods

# notation_EObjectListValueStyle class attributes and methods

# notation_ByteArrayValueStyle class attributes and methods
notation_ByteArrayValueStyle_byteArrayValue: Property = Property(name="byteArrayValue", type=StringType)
notation_ByteArrayValueStyle.attributes={notation_ByteArrayValueStyle_byteArrayValue}

# notation_BooleanListValueStyle class attributes and methods
notation_BooleanListValueStyle_booleanListValue: Property = Property(name="booleanListValue", type=StringType)
notation_BooleanListValueStyle.attributes={notation_BooleanListValueStyle_booleanListValue}

# notation_HintedDiagramLinkStyle class attributes and methods
notation_HintedDiagramLinkStyle_hint: Property = Property(name="hint", type=StringType)
notation_HintedDiagramLinkStyle.attributes={notation_HintedDiagramLinkStyle_hint}

# DiagramLinkStyle class attributes and methods

# notation_SingleValueStyle class attributes and methods
notation_SingleValueStyle_rawValue: Property = Property(name="rawValue", type=StringType)
notation_SingleValueStyle_m_getValue: Method = Method(name="getValue", parameters={}, type=StringType)
notation_SingleValueStyle_m_setValue: Method = Method(name="setValue", parameters={Parameter(name='newValue')})
notation_SingleValueStyle.attributes={notation_SingleValueStyle_rawValue}
notation_SingleValueStyle.methods={notation_SingleValueStyle_m_getValue, notation_SingleValueStyle_m_setValue}

# DataTypeStyle class attributes and methods

# notation_DiagramLinkStyle class attributes and methods

# notation_MultiDiagramLinkStyle class attributes and methods

# notation_TextStyle class attributes and methods
notation_TextStyle_textAlignment: Property = Property(name="textAlignment", type=StringType)
notation_TextStyle.attributes={notation_TextStyle_textAlignment}

# notation_LineTypeStyle class attributes and methods
notation_LineTypeStyle_lineType: Property = Property(name="lineType", type=StringType)
notation_LineTypeStyle.attributes={notation_LineTypeStyle_lineType}

# notation_ArrowStyle class attributes and methods
notation_ArrowStyle_arrowSource: Property = Property(name="arrowSource", type=StringType)
notation_ArrowStyle_arrowTarget: Property = Property(name="arrowTarget", type=StringType)
notation_ArrowStyle.attributes={notation_ArrowStyle_arrowSource, notation_ArrowStyle_arrowTarget}

# notation_Shape class attributes and methods

# Node class attributes and methods

# ShapeStyle class attributes and methods

# notation_Compartment class attributes and methods

# BasicCompartment class attributes and methods

# CanonicalStyle class attributes and methods

# TitleStyle class attributes and methods

# notation_ListCompartment class attributes and methods

# SortingStyle class attributes and methods

# FilteringStyle class attributes and methods

# notation_Connector class attributes and methods

# Edge class attributes and methods

# ConnectorStyle class attributes and methods

# notation_StandardDiagram class attributes and methods

# Diagram class attributes and methods

# DiagramStyle class attributes and methods

# DrawerStyle class attributes and methods

# notation_BasicSemanticCompartment class attributes and methods

# notation_SemanticListCompartment class attributes and methods

# BasicSemanticCompartment class attributes and methods

# notation_RoundedCornersStyle class attributes and methods
notation_RoundedCornersStyle_roundedBendpointsRadius: Property = Property(name="roundedBendpointsRadius", type=IntegerType)
notation_RoundedCornersStyle.attributes={notation_RoundedCornersStyle_roundedBendpointsRadius}

# notation_DecorationNode class attributes and methods

# BasicDecorationNode class attributes and methods

# notation_BasicDecorationNode class attributes and methods

# notation_BasicCompartment class attributes and methods

# DecorationNode class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="View", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceEdges", type=notation_View, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="View2", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="targetEdges", type=notation_View, multiplicity=Multiplicity(1, 1))
    }
)
bendpoints3: BinaryAssociation = BinaryAssociation(
    name="bendpoints3",
    ends={
        Property(name="notation_Bendpoints", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Edge", type=notation_Bendpoints, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceAnchor4: BinaryAssociation = BinaryAssociation(
    name="sourceAnchor4",
    ends={
        Property(name="notation_Anchor", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Edge5", type=notation_Anchor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetAnchor6: BinaryAssociation = BinaryAssociation(
    name="targetAnchor6",
    ends={
        Property(name="notation_Anchor8", type=notation_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Edge7", type=notation_Anchor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layoutConstraint9: BinaryAssociation = BinaryAssociation(
    name="layoutConstraint9",
    ends={
        Property(name="notation_LayoutConstraint", type=notation_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Node", type=notation_LayoutConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sortedObjects10: BinaryAssociation = BinaryAssociation(
    name="sortedObjects10",
    ends={
        Property(name="notation_EObject", type=notation_SortingStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_SortingStyle", type=notation_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
sourceEdges11: BinaryAssociation = BinaryAssociation(
    name="sourceEdges11",
    ends={
        Property(name="Edge", type=notation_View, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=notation_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
targetEdges12: BinaryAssociation = BinaryAssociation(
    name="targetEdges12",
    ends={
        Property(name="Edge13", type=notation_View, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=notation_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
persistedChildren14: BinaryAssociation = BinaryAssociation(
    name="persistedChildren14",
    ends={
        Property(name="notation_Node15", type=notation_View, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_View", type=notation_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styles16: BinaryAssociation = BinaryAssociation(
    name="styles16",
    ends={
        Property(name="notation_Style", type=notation_View, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_View17", type=notation_Style, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element18: BinaryAssociation = BinaryAssociation(
    name="element18",
    ends={
        Property(name="notation_EObject20", type=notation_View, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_View19", type=notation_EObject, multiplicity=Multiplicity(0, 1))
    }
)
diagram21: BinaryAssociation = BinaryAssociation(
    name="diagram21",
    ends={
        Property(name="notation_Diagram", type=notation_View, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_View22", type=notation_Diagram, multiplicity=Multiplicity(1, 1))
    }
)
transientChildren23: BinaryAssociation = BinaryAssociation(
    name="transientChildren23",
    ends={
        Property(name="notation_Node25", type=notation_View, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_View24", type=notation_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
persistedEdges26: BinaryAssociation = BinaryAssociation(
    name="persistedEdges26",
    ends={
        Property(name="notation_Edge28", type=notation_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Diagram27", type=notation_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TransientEdges29: BinaryAssociation = BinaryAssociation(
    name="TransientEdges29",
    ends={
        Property(name="notation_Edge31", type=notation_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Diagram30", type=notation_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
horizontalGuides32: BinaryAssociation = BinaryAssociation(
    name="horizontalGuides32",
    ends={
        Property(name="notation_Guide", type=notation_GuideStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_GuideStyle", type=notation_Guide, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
verticalGuides33: BinaryAssociation = BinaryAssociation(
    name="verticalGuides33",
    ends={
        Property(name="notation_Guide35", type=notation_GuideStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_GuideStyle34", type=notation_Guide, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeMap36: BinaryAssociation = BinaryAssociation(
    name="nodeMap36",
    ends={
        Property(name="notation_NodeEntry", type=notation_Guide, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_Guide37", type=notation_NodeEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key38: BinaryAssociation = BinaryAssociation(
    name="key38",
    ends={
        Property(name="notation_Node40", type=notation_NodeEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_NodeEntry39", type=notation_Node, multiplicity=Multiplicity(1, 1))
    }
)
filteredObjects41: BinaryAssociation = BinaryAssociation(
    name="filteredObjects41",
    ends={
        Property(name="notation_EObject42", type=notation_FilteringStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_FilteringStyle", type=notation_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
cropBound43: BinaryAssociation = BinaryAssociation(
    name="cropBound43",
    ends={
        Property(name="notation_Bounds", type=notation_ImageStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_ImageStyle", type=notation_Bounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
imageBuffer44: BinaryAssociation = BinaryAssociation(
    name="imageBuffer44",
    ends={
        Property(name="notation_Image", type=notation_ImageBufferStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_ImageBufferStyle", type=notation_Image, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
propertiesMap45: BinaryAssociation = BinaryAssociation(
    name="propertiesMap45",
    ends={
        Property(name="notation_StringToPropertyValueMapEntry", type=notation_PropertiesSetStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_PropertiesSetStyle", type=notation_StringToPropertyValueMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value46: BinaryAssociation = BinaryAssociation(
    name="value46",
    ends={
        Property(name="notation_PropertyValue", type=notation_StringToPropertyValueMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_StringToPropertyValueMapEntry47", type=notation_PropertyValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instanceType48: BinaryAssociation = BinaryAssociation(
    name="instanceType48",
    ends={
        Property(name="notation_EDataType", type=notation_PropertyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_PropertyValue49", type=notation_EDataType, multiplicity=Multiplicity(0, 1))
    }
)
instanceType50: BinaryAssociation = BinaryAssociation(
    name="instanceType50",
    ends={
        Property(name="notation_EDataType51", type=notation_DataTypeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_DataTypeStyle", type=notation_EDataType, multiplicity=Multiplicity(0, 1))
    }
)
eObjectValue52: BinaryAssociation = BinaryAssociation(
    name="eObjectValue52",
    ends={
        Property(name="notation_EObject53", type=notation_EObjectValueStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_EObjectValueStyle", type=notation_EObject, multiplicity=Multiplicity(0, 1))
    }
)
eObjectListValue54: BinaryAssociation = BinaryAssociation(
    name="eObjectListValue54",
    ends={
        Property(name="notation_EObject55", type=notation_EObjectListValueStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_EObjectListValueStyle", type=notation_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
diagramLink56: BinaryAssociation = BinaryAssociation(
    name="diagramLink56",
    ends={
        Property(name="notation_Diagram57", type=notation_DiagramLinkStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_DiagramLinkStyle", type=notation_Diagram, multiplicity=Multiplicity(0, 1))
    }
)
diagramLinks58: BinaryAssociation = BinaryAssociation(
    name="diagramLinks58",
    ends={
        Property(name="notation_Diagram59", type=notation_MultiDiagramLinkStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="notation_MultiDiagramLinkStyle", type=notation_Diagram, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_notation_Edge_View = Generalization(general=View, specific=notation_Edge)
gen_notation_Node_View = Generalization(general=View, specific=notation_Node)
gen_notation_FillStyle_Style = Generalization(general=Style, specific=notation_FillStyle)
gen_notation_LineStyle_Style = Generalization(general=Style, specific=notation_LineStyle)
gen_notation_TitleStyle_Style = Generalization(general=Style, specific=notation_TitleStyle)
gen_notation_SortingStyle_Style = Generalization(general=Style, specific=notation_SortingStyle)
gen_notation_DescriptionStyle_Style = Generalization(general=Style, specific=notation_DescriptionStyle)
gen_notation_Size_LayoutConstraint = Generalization(general=LayoutConstraint, specific=notation_Size)
gen_notation_Location_LayoutConstraint = Generalization(general=LayoutConstraint, specific=notation_Location)
gen_notation_Bounds_Location = Generalization(general=Location, specific=notation_Bounds)
gen_notation_Bounds_Size = Generalization(general=Size, specific=notation_Bounds)
gen_notation_Ratio_LayoutConstraint = Generalization(general=LayoutConstraint, specific=notation_Ratio)
gen_notation_IdentityAnchor_Anchor = Generalization(general=Anchor, specific=notation_IdentityAnchor)
gen_notation_FontStyle_Style = Generalization(general=Style, specific=notation_FontStyle)
gen_notation_RoutingStyle_RoundedCornersStyle = Generalization(general=RoundedCornersStyle, specific=notation_RoutingStyle)
gen_notation_View_EModelElement = Generalization(general=EModelElement, specific=notation_View)
gen_notation_RelativeBendpoints_Bendpoints = Generalization(general=Bendpoints, specific=notation_RelativeBendpoints)
gen_notation_Diagram_View = Generalization(general=View, specific=notation_Diagram)
gen_notation_CanonicalStyle_Style = Generalization(general=Style, specific=notation_CanonicalStyle)
gen_notation_ShapeStyle_FontStyle = Generalization(general=FontStyle, specific=notation_ShapeStyle)
gen_notation_ShapeStyle_DescriptionStyle = Generalization(general=DescriptionStyle, specific=notation_ShapeStyle)
gen_notation_ShapeStyle_FillStyle = Generalization(general=FillStyle, specific=notation_ShapeStyle)
gen_notation_ShapeStyle_LineStyle = Generalization(general=LineStyle, specific=notation_ShapeStyle)
gen_notation_ShapeStyle_RoundedCornersStyle = Generalization(general=RoundedCornersStyle, specific=notation_ShapeStyle)
gen_notation_ConnectorStyle_RoutingStyle = Generalization(general=RoutingStyle, specific=notation_ConnectorStyle)
gen_notation_ConnectorStyle_LineStyle = Generalization(general=LineStyle, specific=notation_ConnectorStyle)
gen_notation_PageStyle_Style = Generalization(general=Style, specific=notation_PageStyle)
gen_notation_DrawerStyle_Style = Generalization(general=Style, specific=notation_DrawerStyle)
gen_notation_GuideStyle_Style = Generalization(general=Style, specific=notation_GuideStyle)
gen_notation_FilteringStyle_Style = Generalization(general=Style, specific=notation_FilteringStyle)
gen_notation_DiagramStyle_PageStyle = Generalization(general=PageStyle, specific=notation_DiagramStyle)
gen_notation_DiagramStyle_GuideStyle = Generalization(general=GuideStyle, specific=notation_DiagramStyle)
gen_notation_DiagramStyle_DescriptionStyle = Generalization(general=DescriptionStyle, specific=notation_DiagramStyle)
gen_notation_ImageStyle_Style = Generalization(general=Style, specific=notation_ImageStyle)
gen_notation_ImageBufferStyle_ImageStyle = Generalization(general=ImageStyle, specific=notation_ImageBufferStyle)
gen_notation_PropertiesSetStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_PropertiesSetStyle)
gen_notation_PropertyValue_StringObjectConverter = Generalization(general=StringObjectConverter, specific=notation_PropertyValue)
gen_notation_ListValueStyle_DataTypeStyle = Generalization(general=DataTypeStyle, specific=notation_ListValueStyle)
gen_notation_NamedStyle_Style = Generalization(general=Style, specific=notation_NamedStyle)
gen_notation_DataTypeStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_DataTypeStyle)
gen_notation_DataTypeStyle_StringObjectConverter = Generalization(general=StringObjectConverter, specific=notation_DataTypeStyle)
gen_notation_IntValueStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_IntValueStyle)
gen_notation_IntListValueStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_IntListValueStyle)
gen_notation_BooleanValueStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_BooleanValueStyle)
gen_notation_DoubleValueStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_DoubleValueStyle)
gen_notation_DoubleListValueStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_DoubleListValueStyle)
gen_notation_StringValueStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_StringValueStyle)
gen_notation_StringListValueStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_StringListValueStyle)
gen_notation_EObjectValueStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_EObjectValueStyle)
gen_notation_EObjectListValueStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_EObjectListValueStyle)
gen_notation_ByteArrayValueStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_ByteArrayValueStyle)
gen_notation_BooleanListValueStyle_NamedStyle = Generalization(general=NamedStyle, specific=notation_BooleanListValueStyle)
gen_notation_HintedDiagramLinkStyle_DiagramLinkStyle = Generalization(general=DiagramLinkStyle, specific=notation_HintedDiagramLinkStyle)
gen_notation_HintedDiagramLinkStyle_Style = Generalization(general=Style, specific=notation_HintedDiagramLinkStyle)
gen_notation_SingleValueStyle_DataTypeStyle = Generalization(general=DataTypeStyle, specific=notation_SingleValueStyle)
gen_notation_DiagramLinkStyle_Style = Generalization(general=Style, specific=notation_DiagramLinkStyle)
gen_notation_MultiDiagramLinkStyle_Style = Generalization(general=Style, specific=notation_MultiDiagramLinkStyle)
gen_notation_TextStyle_Style = Generalization(general=Style, specific=notation_TextStyle)
gen_notation_LineTypeStyle_Style = Generalization(general=Style, specific=notation_LineTypeStyle)
gen_notation_ArrowStyle_Style = Generalization(general=Style, specific=notation_ArrowStyle)
gen_notation_Shape_Node = Generalization(general=Node, specific=notation_Shape)
gen_notation_Shape_ShapeStyle = Generalization(general=ShapeStyle, specific=notation_Shape)
gen_notation_Compartment_BasicCompartment = Generalization(general=BasicCompartment, specific=notation_Compartment)
gen_notation_Compartment_CanonicalStyle = Generalization(general=CanonicalStyle, specific=notation_Compartment)
gen_notation_Compartment_TitleStyle = Generalization(general=TitleStyle, specific=notation_Compartment)
gen_notation_ListCompartment_BasicCompartment = Generalization(general=BasicCompartment, specific=notation_ListCompartment)
gen_notation_ListCompartment_SortingStyle = Generalization(general=SortingStyle, specific=notation_ListCompartment)
gen_notation_ListCompartment_FilteringStyle = Generalization(general=FilteringStyle, specific=notation_ListCompartment)
gen_notation_ListCompartment_TitleStyle = Generalization(general=TitleStyle, specific=notation_ListCompartment)
gen_notation_Connector_Edge = Generalization(general=Edge, specific=notation_Connector)
gen_notation_Connector_ConnectorStyle = Generalization(general=ConnectorStyle, specific=notation_Connector)
gen_notation_StandardDiagram_Diagram = Generalization(general=Diagram, specific=notation_StandardDiagram)
gen_notation_StandardDiagram_DiagramStyle = Generalization(general=DiagramStyle, specific=notation_StandardDiagram)
gen_notation_BasicCompartment_DrawerStyle = Generalization(general=DrawerStyle, specific=notation_BasicCompartment)
gen_notation_BasicSemanticCompartment_BasicDecorationNode = Generalization(general=BasicDecorationNode, specific=notation_BasicSemanticCompartment)
gen_notation_BasicSemanticCompartment_DrawerStyle = Generalization(general=DrawerStyle, specific=notation_BasicSemanticCompartment)
gen_notation_SemanticListCompartment_BasicSemanticCompartment = Generalization(general=BasicSemanticCompartment, specific=notation_SemanticListCompartment)
gen_notation_SemanticListCompartment_SortingStyle = Generalization(general=SortingStyle, specific=notation_SemanticListCompartment)
gen_notation_SemanticListCompartment_FilteringStyle = Generalization(general=FilteringStyle, specific=notation_SemanticListCompartment)
gen_notation_SemanticListCompartment_TitleStyle = Generalization(general=TitleStyle, specific=notation_SemanticListCompartment)
gen_notation_RoundedCornersStyle_Style = Generalization(general=Style, specific=notation_RoundedCornersStyle)
gen_notation_DecorationNode_BasicDecorationNode = Generalization(general=BasicDecorationNode, specific=notation_DecorationNode)
gen_notation_BasicDecorationNode_Node = Generalization(general=Node, specific=notation_BasicDecorationNode)
gen_notation_BasicCompartment_DecorationNode = Generalization(general=DecorationNode, specific=notation_BasicCompartment)

# Domain Model
domain_model = DomainModel(
    name="notation",
    types={notation_Edge, View, notation_View, notation_Bendpoints, notation_Anchor, notation_Node, notation_LayoutConstraint, notation_Style, notation_FillStyle, Style, notation_LineStyle, notation_TitleStyle, notation_SortingStyle, notation_EObject, notation_DescriptionStyle, notation_Size, LayoutConstraint, notation_Location, notation_Bounds, Location, Size, notation_Ratio, notation_IdentityAnchor, Anchor, notation_FontStyle, notation_RoutingStyle, RoundedCornersStyle, EModelElement, notation_Diagram, notation_RelativeBendpoints, Bendpoints, notation_Image, notation_CanonicalStyle, notation_ShapeStyle, FontStyle, DescriptionStyle, FillStyle, LineStyle, notation_ConnectorStyle, RoutingStyle, notation_PageStyle, notation_DrawerStyle, notation_GuideStyle, notation_Guide, notation_NodeEntry, notation_FilteringStyle, notation_DiagramStyle, PageStyle, GuideStyle, notation_ImageStyle, notation_ImageBufferStyle, ImageStyle, notation_PropertiesSetStyle, NamedStyle, notation_StringToPropertyValueMapEntry, notation_PropertyValue, StringObjectConverter, notation_EDataType, notation_ListValueStyle, notation_NamedStyle, notation_StringObjectConverter, notation_DataTypeStyle, notation_IntValueStyle, notation_IntListValueStyle, notation_BooleanValueStyle, notation_DoubleValueStyle, notation_DoubleListValueStyle, notation_StringValueStyle, notation_StringListValueStyle, notation_EObjectValueStyle, notation_EObjectListValueStyle, notation_ByteArrayValueStyle, notation_BooleanListValueStyle, notation_HintedDiagramLinkStyle, DiagramLinkStyle, notation_SingleValueStyle, DataTypeStyle, notation_DiagramLinkStyle, notation_MultiDiagramLinkStyle, notation_TextStyle, notation_LineTypeStyle, notation_ArrowStyle, notation_Shape, Node, ShapeStyle, notation_Compartment, BasicCompartment, CanonicalStyle, TitleStyle, notation_ListCompartment, SortingStyle, FilteringStyle, notation_Connector, Edge, ConnectorStyle, notation_StandardDiagram, Diagram, DiagramStyle, DrawerStyle, notation_BasicSemanticCompartment, notation_SemanticListCompartment, BasicSemanticCompartment, notation_RoundedCornersStyle, notation_DecorationNode, BasicDecorationNode, notation_BasicDecorationNode, notation_BasicCompartment, DecorationNode, Sorting, Filtering, Routing, Smoothness, JumpLinkStatus, JumpLinkType, Alignment, SortingDirection, MeasurementUnit, TextAlignment, LineType, ArrowType, GradientStyle},
    associations={source0, target1, bendpoints3, sourceAnchor4, targetAnchor6, layoutConstraint9, sortedObjects10, sourceEdges11, targetEdges12, persistedChildren14, styles16, element18, diagram21, transientChildren23, persistedEdges26, TransientEdges29, horizontalGuides32, verticalGuides33, nodeMap36, key38, filteredObjects41, cropBound43, imageBuffer44, propertiesMap45, value46, instanceType48, instanceType50, eObjectValue52, eObjectListValue54, diagramLink56, diagramLinks58},
    generalizations={gen_notation_Edge_View, gen_notation_Node_View, gen_notation_FillStyle_Style, gen_notation_LineStyle_Style, gen_notation_TitleStyle_Style, gen_notation_SortingStyle_Style, gen_notation_DescriptionStyle_Style, gen_notation_Size_LayoutConstraint, gen_notation_Location_LayoutConstraint, gen_notation_Bounds_Location, gen_notation_Bounds_Size, gen_notation_Ratio_LayoutConstraint, gen_notation_IdentityAnchor_Anchor, gen_notation_FontStyle_Style, gen_notation_RoutingStyle_RoundedCornersStyle, gen_notation_View_EModelElement, gen_notation_RelativeBendpoints_Bendpoints, gen_notation_Diagram_View, gen_notation_CanonicalStyle_Style, gen_notation_ShapeStyle_FontStyle, gen_notation_ShapeStyle_DescriptionStyle, gen_notation_ShapeStyle_FillStyle, gen_notation_ShapeStyle_LineStyle, gen_notation_ShapeStyle_RoundedCornersStyle, gen_notation_ConnectorStyle_RoutingStyle, gen_notation_ConnectorStyle_LineStyle, gen_notation_PageStyle_Style, gen_notation_DrawerStyle_Style, gen_notation_GuideStyle_Style, gen_notation_FilteringStyle_Style, gen_notation_DiagramStyle_PageStyle, gen_notation_DiagramStyle_GuideStyle, gen_notation_DiagramStyle_DescriptionStyle, gen_notation_ImageStyle_Style, gen_notation_ImageBufferStyle_ImageStyle, gen_notation_PropertiesSetStyle_NamedStyle, gen_notation_PropertyValue_StringObjectConverter, gen_notation_ListValueStyle_DataTypeStyle, gen_notation_NamedStyle_Style, gen_notation_DataTypeStyle_NamedStyle, gen_notation_DataTypeStyle_StringObjectConverter, gen_notation_IntValueStyle_NamedStyle, gen_notation_IntListValueStyle_NamedStyle, gen_notation_BooleanValueStyle_NamedStyle, gen_notation_DoubleValueStyle_NamedStyle, gen_notation_DoubleListValueStyle_NamedStyle, gen_notation_StringValueStyle_NamedStyle, gen_notation_StringListValueStyle_NamedStyle, gen_notation_EObjectValueStyle_NamedStyle, gen_notation_EObjectListValueStyle_NamedStyle, gen_notation_ByteArrayValueStyle_NamedStyle, gen_notation_BooleanListValueStyle_NamedStyle, gen_notation_HintedDiagramLinkStyle_DiagramLinkStyle, gen_notation_HintedDiagramLinkStyle_Style, gen_notation_SingleValueStyle_DataTypeStyle, gen_notation_DiagramLinkStyle_Style, gen_notation_MultiDiagramLinkStyle_Style, gen_notation_TextStyle_Style, gen_notation_LineTypeStyle_Style, gen_notation_ArrowStyle_Style, gen_notation_Shape_Node, gen_notation_Shape_ShapeStyle, gen_notation_Compartment_BasicCompartment, gen_notation_Compartment_CanonicalStyle, gen_notation_Compartment_TitleStyle, gen_notation_ListCompartment_BasicCompartment, gen_notation_ListCompartment_SortingStyle, gen_notation_ListCompartment_FilteringStyle, gen_notation_ListCompartment_TitleStyle, gen_notation_Connector_Edge, gen_notation_Connector_ConnectorStyle, gen_notation_StandardDiagram_Diagram, gen_notation_StandardDiagram_DiagramStyle, gen_notation_BasicCompartment_DrawerStyle, gen_notation_BasicSemanticCompartment_BasicDecorationNode, gen_notation_BasicSemanticCompartment_DrawerStyle, gen_notation_SemanticListCompartment_BasicSemanticCompartment, gen_notation_SemanticListCompartment_SortingStyle, gen_notation_SemanticListCompartment_FilteringStyle, gen_notation_SemanticListCompartment_TitleStyle, gen_notation_RoundedCornersStyle_Style, gen_notation_DecorationNode_BasicDecorationNode, gen_notation_BasicDecorationNode_Node, gen_notation_BasicCompartment_DecorationNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)