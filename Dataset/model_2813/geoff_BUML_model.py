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
RendererHint: Enumeration = Enumeration(
    name="RendererHint",
    literals={
            EnumerationLiteral(name="CANVAS"),
			EnumerationLiteral(name="DOM"),
			EnumerationLiteral(name="WEBGL")
    }
)

ScriptContext: Enumeration = Enumeration(
    name="ScriptContext",
    literals={
            EnumerationLiteral(name="GLOBAL"),
			EnumerationLiteral(name="MAP"),
			EnumerationLiteral(name="LAYER")
    }
)

SourceFormat: Enumeration = Enumeration(
    name="SourceFormat",
    literals={
            EnumerationLiteral(name="INTERNAL"),
			EnumerationLiteral(name="GeoJSON"),
			EnumerationLiteral(name="GPX"),
			EnumerationLiteral(name="KML")
    }
)

EventCondition: Enumeration = Enumeration(
    name="EventCondition",
    literals={
            EnumerationLiteral(name="SINGLE_CLICK"),
			EnumerationLiteral(name="CLICK"),
			EnumerationLiteral(name="HOVER")
    }
)

# Classes
geoff_Identifiable = Class(name="geoff::Identifiable", is_abstract=True)
geoff_GeoMap = Class(name="geoff::GeoMap")
Identifiable = Class(name="Identifiable")
Descriptive = Class(name="Descriptive")
Layer = Class(name="Layer")
geoff_View = Class(name="geoff::View")
geoff_Script = Class(name="geoff::Script")
Interaction = Class(name="Interaction")
geoff_Location = Class(name="geoff::Location", is_abstract=True)
geoff_XYZLocation = Class(name="geoff::XYZLocation")
geoff_Descriptive = Class(name="geoff::Descriptive", is_abstract=True)
geoff_Feature = Class(name="geoff::Feature")
Geometry = Class(name="Geometry")
Style = Class(name="Style")
geoff_StringToStringMapEntry = Class(name="geoff::StringToStringMapEntry")
geoff_Color = Class(name="geoff::Color")
geoff_StyleEntry = Class(name="geoff::StyleEntry")
Location = Class(name="Location")
geoff_layer_Layer = Class(name="geoff::layer::Layer", is_abstract=True)
Source = Class(name="Source")
geoff_source_Source = Class(name="geoff::source::Source", is_abstract=True)
geoff_source_TileSource = Class(name="geoff::source::TileSource", is_abstract=True)
geoff_source_TileImage = Class(name="geoff::source::TileImage", is_abstract=True)
TileSource = Class(name="TileSource")
geoff_source_XYZ = Class(name="geoff::source::XYZ", is_abstract=True)
TileImage = Class(name="TileImage")
geoff_source_OSM = Class(name="geoff::source::OSM")
XYZ = Class(name="XYZ")
geoff_source_MapQuest = Class(name="geoff::source::MapQuest")
geoff_source_BingMaps = Class(name="geoff::source::BingMaps")
geoff_source_VectorSource = Class(name="geoff::source::VectorSource")
source_geoff_Feature = Class(name="source::geoff::Feature")
geoff_geom_Geometry = Class(name="geoff::geom::Geometry", is_abstract=True)
geoff_layer_TileLayer = Class(name="geoff::layer::TileLayer")
geoff_layer_VectorLayer = Class(name="geoff::layer::VectorLayer")
layer_geoff_StyleEntry = Class(name="layer::geoff::StyleEntry")
geoff_style_Style = Class(name="geoff::style::Style")
Image = Class(name="Image")
Fill = Class(name="Fill")
Stroke = Class(name="Stroke")
Text = Class(name="Text")
geoff_style_Image = Class(name="geoff::style::Image")
geoff_style_Icon = Class(name="geoff::style::Icon")
geoff_style_Fill = Class(name="geoff::style::Fill")
style_geoff_Color = Class(name="style::geoff::Color")
geoff_style_Stroke = Class(name="geoff::style::Stroke")
geoff_style_Circle = Class(name="geoff::style::Circle")
geoff_geom_SimpleGeometry = Class(name="geoff::geom::SimpleGeometry")
geoff_geom_Point = Class(name="geoff::geom::Point")
SimpleGeometry = Class(name="SimpleGeometry")
geom_geoff_Location = Class(name="geom::geoff::Location")
geoff_geom_LineString = Class(name="geoff::geom::LineString")
geoff_geom_Polygon = Class(name="geoff::geom::Polygon")
geoff_interaction_Interaction = Class(name="geoff::interaction::Interaction", is_abstract=True)
geoff_interaction_Select = Class(name="geoff::interaction::Select")
geoff_style_Text = Class(name="geoff::style::Text")

# geoff_Identifiable class attributes and methods
geoff_Identifiable_id: Property = Property(name="id", type=StringType)
geoff_Identifiable.attributes={geoff_Identifiable_id}

# geoff_GeoMap class attributes and methods
geoff_GeoMap_rendererHint: Property = Property(name="rendererHint", type=StringType)
geoff_GeoMap.attributes={geoff_GeoMap_rendererHint}

# Identifiable class attributes and methods

# Descriptive class attributes and methods

# Layer class attributes and methods

# geoff_View class attributes and methods
geoff_View_zoom: Property = Property(name="zoom", type=IntegerType)
geoff_View.attributes={geoff_View_zoom}

# geoff_Script class attributes and methods
geoff_Script_src: Property = Property(name="src", type=StringType)
geoff_Script_type: Property = Property(name="type", type=StringType)
geoff_Script_context: Property = Property(name="context", type=StringType)
geoff_Script.attributes={geoff_Script_context, geoff_Script_type, geoff_Script_src}

# Interaction class attributes and methods

# geoff_Location class attributes and methods
geoff_Location_projectionCode: Property = Property(name="projectionCode", type=StringType)
geoff_Location.attributes={geoff_Location_projectionCode}

# geoff_XYZLocation class attributes and methods
geoff_XYZLocation_x: Property = Property(name="x", type=FloatType)
geoff_XYZLocation_y: Property = Property(name="y", type=FloatType)
geoff_XYZLocation_z: Property = Property(name="z", type=FloatType)
geoff_XYZLocation.attributes={geoff_XYZLocation_x, geoff_XYZLocation_y, geoff_XYZLocation_z}

# geoff_Descriptive class attributes and methods
geoff_Descriptive_longDescription: Property = Property(name="longDescription", type=StringType)
geoff_Descriptive_shortDescription: Property = Property(name="shortDescription", type=StringType)
geoff_Descriptive.attributes={geoff_Descriptive_shortDescription, geoff_Descriptive_longDescription}

# geoff_Feature class attributes and methods
geoff_Feature_onclick: Property = Property(name="onclick", type=StringType)
geoff_Feature.attributes={geoff_Feature_onclick}

# Geometry class attributes and methods

# Style class attributes and methods

# geoff_StringToStringMapEntry class attributes and methods
geoff_StringToStringMapEntry_key: Property = Property(name="key", type=StringType)
geoff_StringToStringMapEntry_value: Property = Property(name="value", type=StringType)
geoff_StringToStringMapEntry.attributes={geoff_StringToStringMapEntry_value, geoff_StringToStringMapEntry_key}

# geoff_Color class attributes and methods
geoff_Color_red: Property = Property(name="red", type=IntegerType)
geoff_Color_green: Property = Property(name="green", type=IntegerType)
geoff_Color_blue: Property = Property(name="blue", type=IntegerType)
geoff_Color_alpha: Property = Property(name="alpha", type=FloatType)
geoff_Color.attributes={geoff_Color_blue, geoff_Color_alpha, geoff_Color_red, geoff_Color_green}

# geoff_StyleEntry class attributes and methods
geoff_StyleEntry_key: Property = Property(name="key", type=StringType)
geoff_StyleEntry.attributes={geoff_StyleEntry_key}

# Location class attributes and methods

# geoff_layer_Layer class attributes and methods

# Source class attributes and methods

# geoff_source_Source class attributes and methods

# geoff_source_TileSource class attributes and methods

# geoff_source_TileImage class attributes and methods

# TileSource class attributes and methods

# geoff_source_XYZ class attributes and methods

# TileImage class attributes and methods

# geoff_source_OSM class attributes and methods

# XYZ class attributes and methods

# geoff_source_MapQuest class attributes and methods
geoff_source_MapQuest_layer: Property = Property(name="layer", type=StringType)
geoff_source_MapQuest.attributes={geoff_source_MapQuest_layer}

# geoff_source_BingMaps class attributes and methods
geoff_source_BingMaps_key: Property = Property(name="key", type=StringType)
geoff_source_BingMaps_imagerySet: Property = Property(name="imagerySet", type=StringType)
geoff_source_BingMaps.attributes={geoff_source_BingMaps_imagerySet, geoff_source_BingMaps_key}

# geoff_source_VectorSource class attributes and methods
geoff_source_VectorSource_url: Property = Property(name="url", type=StringType)
geoff_source_VectorSource_projection: Property = Property(name="projection", type=StringType)
geoff_source_VectorSource_format: Property = Property(name="format", type=StringType)
geoff_source_VectorSource.attributes={geoff_source_VectorSource_projection, geoff_source_VectorSource_format, geoff_source_VectorSource_url}

# source_geoff_Feature class attributes and methods

# geoff_geom_Geometry class attributes and methods

# geoff_layer_TileLayer class attributes and methods

# geoff_layer_VectorLayer class attributes and methods

# layer_geoff_StyleEntry class attributes and methods

# geoff_style_Style class attributes and methods
geoff_style_Style_zindex: Property = Property(name="zindex", type=StringType)
geoff_style_Style.attributes={geoff_style_Style_zindex}

# Image class attributes and methods

# Fill class attributes and methods

# Stroke class attributes and methods

# Text class attributes and methods

# geoff_style_Image class attributes and methods

# geoff_style_Icon class attributes and methods
geoff_style_Icon_src: Property = Property(name="src", type=StringType)
geoff_style_Icon.attributes={geoff_style_Icon_src}

# geoff_style_Fill class attributes and methods

# style_geoff_Color class attributes and methods

# geoff_style_Stroke class attributes and methods
geoff_style_Stroke_lineCap: Property = Property(name="lineCap", type=StringType)
geoff_style_Stroke_lineJoin: Property = Property(name="lineJoin", type=StringType)
geoff_style_Stroke_miterLimit: Property = Property(name="miterLimit", type=StringType)
geoff_style_Stroke_width: Property = Property(name="width", type=StringType)
geoff_style_Stroke_lineDash: Property = Property(name="lineDash", type=FloatType)
geoff_style_Stroke.attributes={geoff_style_Stroke_lineCap, geoff_style_Stroke_miterLimit, geoff_style_Stroke_lineDash, geoff_style_Stroke_width, geoff_style_Stroke_lineJoin}

# geoff_style_Circle class attributes and methods
geoff_style_Circle_radius: Property = Property(name="radius", type=FloatType)
geoff_style_Circle.attributes={geoff_style_Circle_radius}

# geoff_geom_SimpleGeometry class attributes and methods

# geoff_geom_Point class attributes and methods

# SimpleGeometry class attributes and methods

# geom_geoff_Location class attributes and methods

# geoff_geom_LineString class attributes and methods

# geoff_geom_Polygon class attributes and methods

# geoff_interaction_Interaction class attributes and methods

# geoff_interaction_Select class attributes and methods
geoff_interaction_Select_condition: Property = Property(name="condition", type=StringType)
geoff_interaction_Select_multi: Property = Property(name="multi", type=BooleanType)
geoff_interaction_Select.attributes={geoff_interaction_Select_multi, geoff_interaction_Select_condition}

# geoff_style_Text class attributes and methods
geoff_style_Text_textAlign: Property = Property(name="textAlign", type=StringType)
geoff_style_Text_textBaseLine: Property = Property(name="textBaseLine", type=StringType)
geoff_style_Text_font: Property = Property(name="font", type=StringType)
geoff_style_Text_offsetX: Property = Property(name="offsetX", type=FloatType)
geoff_style_Text_offsetY: Property = Property(name="offsetY", type=FloatType)
geoff_style_Text_rotation: Property = Property(name="rotation", type=StringType)
geoff_style_Text_scale: Property = Property(name="scale", type=StringType)
geoff_style_Text_text: Property = Property(name="text", type=StringType)
geoff_style_Text.attributes={geoff_style_Text_scale, geoff_style_Text_textAlign, geoff_style_Text_text, geoff_style_Text_textBaseLine, geoff_style_Text_offsetY, geoff_style_Text_rotation, geoff_style_Text_font, geoff_style_Text_offsetX}

# Relationships
layers0: BinaryAssociation = BinaryAssociation(
    name="layers0",
    ends={
        Property(name="Layer", type=geoff_GeoMap, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_GeoMap", type=Layer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
view1: BinaryAssociation = BinaryAssociation(
    name="view1",
    ends={
        Property(name="geoff_View", type=geoff_GeoMap, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_GeoMap2", type=geoff_View, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scripts3: BinaryAssociation = BinaryAssociation(
    name="scripts3",
    ends={
        Property(name="geoff_Script", type=geoff_GeoMap, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_GeoMap4", type=geoff_Script, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interactions5: BinaryAssociation = BinaryAssociation(
    name="interactions5",
    ends={
        Property(name="Interaction", type=geoff_GeoMap, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_GeoMap6", type=Interaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
center7: BinaryAssociation = BinaryAssociation(
    name="center7",
    ends={
        Property(name="geoff_Location", type=geoff_View, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_View8", type=geoff_Location, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
geometry9: BinaryAssociation = BinaryAssociation(
    name="geometry9",
    ends={
        Property(name="Geometry", type=geoff_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_Feature", type=Geometry, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
style10: BinaryAssociation = BinaryAssociation(
    name="style10",
    ends={
        Property(name="Style", type=geoff_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_Feature11", type=Style, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties12: BinaryAssociation = BinaryAssociation(
    name="properties12",
    ends={
        Property(name="geoff_StringToStringMapEntry", type=geoff_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_Feature13", type=geoff_StringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="Source", type=geoff_layer_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_layer_Layer", type=Source, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value14: BinaryAssociation = BinaryAssociation(
    name="value14",
    ends={
        Property(name="Style15", type=geoff_StyleEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_StyleEntry", type=Style, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
features18: BinaryAssociation = BinaryAssociation(
    name="features18",
    ends={
        Property(name="source_geoff_Feature", type=geoff_source_VectorSource, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_source_VectorSource", type=source_geoff_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styles17: BinaryAssociation = BinaryAssociation(
    name="styles17",
    ends={
        Property(name="layer_geoff_StyleEntry", type=geoff_layer_VectorLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_layer_VectorLayer", type=layer_geoff_StyleEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coordinates22: BinaryAssociation = BinaryAssociation(
    name="coordinates22",
    ends={
        Property(name="geom_geoff_Location23", type=geoff_geom_Polygon, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_geom_Polygon", type=geom_geoff_Location, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
image24: BinaryAssociation = BinaryAssociation(
    name="image24",
    ends={
        Property(name="Image", type=geoff_style_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_style_Style", type=Image, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill25: BinaryAssociation = BinaryAssociation(
    name="fill25",
    ends={
        Property(name="Fill", type=geoff_style_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_style_Style26", type=Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stroke27: BinaryAssociation = BinaryAssociation(
    name="stroke27",
    ends={
        Property(name="Stroke", type=geoff_style_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_style_Style28", type=Stroke, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
text29: BinaryAssociation = BinaryAssociation(
    name="text29",
    ends={
        Property(name="Text", type=geoff_style_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_style_Style30", type=Text, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color31: BinaryAssociation = BinaryAssociation(
    name="color31",
    ends={
        Property(name="style_geoff_Color", type=geoff_style_Fill, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_style_Fill", type=style_geoff_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color32: BinaryAssociation = BinaryAssociation(
    name="color32",
    ends={
        Property(name="style_geoff_Color33", type=geoff_style_Stroke, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_style_Stroke", type=style_geoff_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fill34: BinaryAssociation = BinaryAssociation(
    name="fill34",
    ends={
        Property(name="Fill35", type=geoff_style_Circle, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_style_Circle", type=Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stroke36: BinaryAssociation = BinaryAssociation(
    name="stroke36",
    ends={
        Property(name="Stroke38", type=geoff_style_Circle, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_style_Circle37", type=Stroke, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
coordinates19: BinaryAssociation = BinaryAssociation(
    name="coordinates19",
    ends={
        Property(name="geom_geoff_Location", type=geoff_geom_Point, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_geom_Point", type=geom_geoff_Location, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
coordinates20: BinaryAssociation = BinaryAssociation(
    name="coordinates20",
    ends={
        Property(name="geom_geoff_Location21", type=geoff_geom_LineString, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_geom_LineString", type=geom_geoff_Location, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
fill39: BinaryAssociation = BinaryAssociation(
    name="fill39",
    ends={
        Property(name="Fill40", type=geoff_style_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_style_Text", type=Fill, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stroke41: BinaryAssociation = BinaryAssociation(
    name="stroke41",
    ends={
        Property(name="Stroke43", type=geoff_style_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="geoff_style_Text42", type=Stroke, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_geoff_GeoMap_Identifiable = Generalization(general=Identifiable, specific=geoff_GeoMap)
gen_geoff_GeoMap_Descriptive = Generalization(general=Descriptive, specific=geoff_GeoMap)
gen_geoff_View_Identifiable = Generalization(general=Identifiable, specific=geoff_View)
gen_geoff_Location_Identifiable = Generalization(general=Identifiable, specific=geoff_Location)
gen_geoff_Feature_Identifiable = Generalization(general=Identifiable, specific=geoff_Feature)
gen_geoff_Color_Identifiable = Generalization(general=Identifiable, specific=geoff_Color)
gen_geoff_XYZLocation_Location = Generalization(general=Location, specific=geoff_XYZLocation)
gen_geoff_Script_Identifiable = Generalization(general=Identifiable, specific=geoff_Script)
gen_geoff_layer_Layer_Identifiable = Generalization(general=Identifiable, specific=geoff_layer_Layer)
gen_geoff_layer_Layer_Descriptive = Generalization(general=Descriptive, specific=geoff_layer_Layer)
gen_geoff_source_Source_Identifiable = Generalization(general=Identifiable, specific=geoff_source_Source)
gen_geoff_source_Source_Descriptive = Generalization(general=Descriptive, specific=geoff_source_Source)
gen_geoff_source_TileSource_Source = Generalization(general=Source, specific=geoff_source_TileSource)
gen_geoff_source_TileImage_TileSource = Generalization(general=TileSource, specific=geoff_source_TileImage)
gen_geoff_source_XYZ_TileImage = Generalization(general=TileImage, specific=geoff_source_XYZ)
gen_geoff_source_OSM_XYZ = Generalization(general=XYZ, specific=geoff_source_OSM)
gen_geoff_source_MapQuest_XYZ = Generalization(general=XYZ, specific=geoff_source_MapQuest)
gen_geoff_source_BingMaps_XYZ = Generalization(general=XYZ, specific=geoff_source_BingMaps)
gen_geoff_source_VectorSource_Source = Generalization(general=Source, specific=geoff_source_VectorSource)
gen_geoff_geom_Geometry_Identifiable = Generalization(general=Identifiable, specific=geoff_geom_Geometry)
gen_geoff_layer_TileLayer_Layer = Generalization(general=Layer, specific=geoff_layer_TileLayer)
gen_geoff_layer_VectorLayer_Layer = Generalization(general=Layer, specific=geoff_layer_VectorLayer)
gen_geoff_style_Style_Identifiable = Generalization(general=Identifiable, specific=geoff_style_Style)
gen_geoff_style_Image_Identifiable = Generalization(general=Identifiable, specific=geoff_style_Image)
gen_geoff_style_Icon_Image = Generalization(general=Image, specific=geoff_style_Icon)
gen_geoff_style_Fill_Identifiable = Generalization(general=Identifiable, specific=geoff_style_Fill)
gen_geoff_style_Stroke_Identifiable = Generalization(general=Identifiable, specific=geoff_style_Stroke)
gen_geoff_style_Circle_Image = Generalization(general=Image, specific=geoff_style_Circle)
gen_geoff_geom_SimpleGeometry_Geometry = Generalization(general=Geometry, specific=geoff_geom_SimpleGeometry)
gen_geoff_geom_Point_SimpleGeometry = Generalization(general=SimpleGeometry, specific=geoff_geom_Point)
gen_geoff_geom_LineString_SimpleGeometry = Generalization(general=SimpleGeometry, specific=geoff_geom_LineString)
gen_geoff_geom_Polygon_SimpleGeometry = Generalization(general=SimpleGeometry, specific=geoff_geom_Polygon)
gen_geoff_interaction_Interaction_Identifiable = Generalization(general=Identifiable, specific=geoff_interaction_Interaction)
gen_geoff_interaction_Select_Interaction = Generalization(general=Interaction, specific=geoff_interaction_Select)
gen_geoff_style_Text_Identifiable = Generalization(general=Identifiable, specific=geoff_style_Text)

# Domain Model
domain_model = DomainModel(
    name="geoff",
    types={geoff_Identifiable, geoff_GeoMap, Identifiable, Descriptive, Layer, geoff_View, geoff_Script, Interaction, geoff_Location, geoff_XYZLocation, geoff_Descriptive, geoff_Feature, Geometry, Style, geoff_StringToStringMapEntry, geoff_Color, geoff_StyleEntry, Location, geoff_layer_Layer, Source, geoff_source_Source, geoff_source_TileSource, geoff_source_TileImage, TileSource, geoff_source_XYZ, TileImage, geoff_source_OSM, XYZ, geoff_source_MapQuest, geoff_source_BingMaps, geoff_source_VectorSource, source_geoff_Feature, geoff_geom_Geometry, geoff_layer_TileLayer, geoff_layer_VectorLayer, layer_geoff_StyleEntry, geoff_style_Style, Image, Fill, Stroke, Text, geoff_style_Image, geoff_style_Icon, geoff_style_Fill, style_geoff_Color, geoff_style_Stroke, geoff_style_Circle, geoff_geom_SimpleGeometry, geoff_geom_Point, SimpleGeometry, geom_geoff_Location, geoff_geom_LineString, geoff_geom_Polygon, geoff_interaction_Interaction, geoff_interaction_Select, geoff_style_Text, RendererHint, ScriptContext, SourceFormat, EventCondition},
    associations={layers0, view1, scripts3, interactions5, center7, geometry9, style10, properties12, source16, value14, features18, styles17, coordinates22, image24, fill25, stroke27, text29, color31, color32, fill34, stroke36, coordinates19, coordinates20, fill39, stroke41},
    generalizations={gen_geoff_GeoMap_Identifiable, gen_geoff_GeoMap_Descriptive, gen_geoff_View_Identifiable, gen_geoff_Location_Identifiable, gen_geoff_Feature_Identifiable, gen_geoff_Color_Identifiable, gen_geoff_XYZLocation_Location, gen_geoff_Script_Identifiable, gen_geoff_layer_Layer_Identifiable, gen_geoff_layer_Layer_Descriptive, gen_geoff_source_Source_Identifiable, gen_geoff_source_Source_Descriptive, gen_geoff_source_TileSource_Source, gen_geoff_source_TileImage_TileSource, gen_geoff_source_XYZ_TileImage, gen_geoff_source_OSM_XYZ, gen_geoff_source_MapQuest_XYZ, gen_geoff_source_BingMaps_XYZ, gen_geoff_source_VectorSource_Source, gen_geoff_geom_Geometry_Identifiable, gen_geoff_layer_TileLayer_Layer, gen_geoff_layer_VectorLayer_Layer, gen_geoff_style_Style_Identifiable, gen_geoff_style_Image_Identifiable, gen_geoff_style_Icon_Image, gen_geoff_style_Fill_Identifiable, gen_geoff_style_Stroke_Identifiable, gen_geoff_style_Circle_Image, gen_geoff_geom_SimpleGeometry_Geometry, gen_geoff_geom_Point_SimpleGeometry, gen_geoff_geom_LineString_SimpleGeometry, gen_geoff_geom_Polygon_SimpleGeometry, gen_geoff_interaction_Interaction_Identifiable, gen_geoff_interaction_Select_Interaction, gen_geoff_style_Text_Identifiable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)