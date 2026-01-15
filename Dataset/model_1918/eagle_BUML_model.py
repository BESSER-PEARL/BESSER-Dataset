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
WireCap: Enumeration = Enumeration(
    name="WireCap",
    literals={
            EnumerationLiteral(name="flat"),
			EnumerationLiteral(name="round")
    }
)

DimensionType: Enumeration = Enumeration(
    name="DimensionType",
    literals={
            EnumerationLiteral(name="parallel"),
			EnumerationLiteral(name="horizontal"),
			EnumerationLiteral(name="vertical"),
			EnumerationLiteral(name="radius"),
			EnumerationLiteral(name="diameter"),
			EnumerationLiteral(name="leader")
    }
)

Severity: Enumeration = Enumeration(
    name="Severity",
    literals={
            EnumerationLiteral(name="info"),
			EnumerationLiteral(name="warning"),
			EnumerationLiteral(name="error")
    }
)

GateAddLevel: Enumeration = Enumeration(
    name="GateAddLevel",
    literals={
            EnumerationLiteral(name="must"),
			EnumerationLiteral(name="can"),
			EnumerationLiteral(name="next"),
			EnumerationLiteral(name="request"),
			EnumerationLiteral(name="always")
    }
)

WireStyle: Enumeration = Enumeration(
    name="WireStyle",
    literals={
            EnumerationLiteral(name="dashdot"),
			EnumerationLiteral(name="continuous"),
			EnumerationLiteral(name="longdash"),
			EnumerationLiteral(name="shortdash")
    }
)

PadShape: Enumeration = Enumeration(
    name="PadShape",
    literals={
            EnumerationLiteral(name="square"),
			EnumerationLiteral(name="round"),
			EnumerationLiteral(name="octagon"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="offset")
    }
)

PolygonPour: Enumeration = Enumeration(
    name="PolygonPour",
    literals={
            EnumerationLiteral(name="solid"),
			EnumerationLiteral(name="hatch"),
			EnumerationLiteral(name="cutout")
    }
)

GridUnit: Enumeration = Enumeration(
    name="GridUnit",
    literals={
            EnumerationLiteral(name="mic"),
			EnumerationLiteral(name="mm"),
			EnumerationLiteral(name="mil"),
			EnumerationLiteral(name="inch")
    }
)

GridStyle: Enumeration = Enumeration(
    name="GridStyle",
    literals={
            EnumerationLiteral(name="lines"),
			EnumerationLiteral(name="dots")
    }
)

TextFont: Enumeration = Enumeration(
    name="TextFont",
    literals={
            EnumerationLiteral(name="vector"),
			EnumerationLiteral(name="proportional"),
			EnumerationLiteral(name="fixed")
    }
)

Align: Enumeration = Enumeration(
    name="Align",
    literals={
            EnumerationLiteral(name="topright"),
			EnumerationLiteral(name="bottomleft"),
			EnumerationLiteral(name="bottomcenter"),
			EnumerationLiteral(name="bottomright"),
			EnumerationLiteral(name="centerleft"),
			EnumerationLiteral(name="center"),
			EnumerationLiteral(name="centerright"),
			EnumerationLiteral(name="topleft"),
			EnumerationLiteral(name="topcenter")
    }
)

AttributeDisplay: Enumeration = Enumeration(
    name="AttributeDisplay",
    literals={
            EnumerationLiteral(name="off"),
			EnumerationLiteral(name="value"),
			EnumerationLiteral(name="name"),
			EnumerationLiteral(name="both")
    }
)

VerticalText: Enumeration = Enumeration(
    name="VerticalText",
    literals={
            EnumerationLiteral(name="up"),
			EnumerationLiteral(name="down")
    }
)

PinVisible: Enumeration = Enumeration(
    name="PinVisible",
    literals={
            EnumerationLiteral(name="off"),
			EnumerationLiteral(name="pad"),
			EnumerationLiteral(name="pin"),
			EnumerationLiteral(name="both")
    }
)

PinLength: Enumeration = Enumeration(
    name="PinLength",
    literals={
            EnumerationLiteral(name="point"),
			EnumerationLiteral(name="short"),
			EnumerationLiteral(name="middle"),
			EnumerationLiteral(name="long")
    }
)

PinDirection: Enumeration = Enumeration(
    name="PinDirection",
    literals={
            EnumerationLiteral(name="nc"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="io"),
			EnumerationLiteral(name="oc"),
			EnumerationLiteral(name="pwr"),
			EnumerationLiteral(name="pas"),
			EnumerationLiteral(name="hiz"),
			EnumerationLiteral(name="sup")
    }
)

PinFunction: Enumeration = Enumeration(
    name="PinFunction",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="dot"),
			EnumerationLiteral(name="clk"),
			EnumerationLiteral(name="dotclk")
    }
)

ContactRoute: Enumeration = Enumeration(
    name="ContactRoute",
    literals={
            EnumerationLiteral(name="all"),
			EnumerationLiteral(name="any")
    }
)

# Classes
eaglemodel_Eagle = Class(name="eaglemodel::Eagle")
eaglemodel_Compatibility = Class(name="eaglemodel::Compatibility")
eaglemodel_Drawing = Class(name="eaglemodel::Drawing")
eaglemodel_Note = Class(name="eaglemodel::Note")
eaglemodel_Settings = Class(name="eaglemodel::Settings")
eaglemodel_Grid = Class(name="eaglemodel::Grid")
eaglemodel_Layers = Class(name="eaglemodel::Layers")
eaglemodel_Schematic = Class(name="eaglemodel::Schematic")
eaglemodel_Setting = Class(name="eaglemodel::Setting")
eaglemodel_Libraries = Class(name="eaglemodel::Libraries")
eaglemodel_Attributes = Class(name="eaglemodel::Attributes")
eaglemodel_Variantdefs = Class(name="eaglemodel::Variantdefs")
eaglemodel_Layer = Class(name="eaglemodel::Layer")
eaglemodel_Description = Class(name="eaglemodel::Description")
eaglemodel_Packages = Class(name="eaglemodel::Packages")
eaglemodel_Symbols = Class(name="eaglemodel::Symbols")
eaglemodel_Classes = Class(name="eaglemodel::Classes")
eaglemodel_Devicesets = Class(name="eaglemodel::Devicesets")
eaglemodel_Parts = Class(name="eaglemodel::Parts")
eaglemodel_Sheets = Class(name="eaglemodel::Sheets")
eaglemodel_Errors = Class(name="eaglemodel::Errors")
eaglemodel_Library = Class(name="eaglemodel::Library")
eaglemodel_Variantdef = Class(name="eaglemodel::Variantdef")
eaglemodel_Attribute = Class(name="eaglemodel::Attribute")
eaglemodel_Part = Class(name="eaglemodel::Part")
eaglemodel_Variant = Class(name="eaglemodel::Variant")
eaglemodel_Class = Class(name="eaglemodel::Class")
eaglemodel_Clearance = Class(name="eaglemodel::Clearance")
eaglemodel_Plain = Class(name="eaglemodel::Plain")
eaglemodel_Instances = Class(name="eaglemodel::Instances")
eaglemodel_Busses = Class(name="eaglemodel::Busses")
eaglemodel_Sheet = Class(name="eaglemodel::Sheet")
eaglemodel_Text = Class(name="eaglemodel::Text")
eaglemodel_Dimension = Class(name="eaglemodel::Dimension")
eaglemodel_Circle = Class(name="eaglemodel::Circle")
eaglemodel_Rectangle = Class(name="eaglemodel::Rectangle")
eaglemodel_Nets = Class(name="eaglemodel::Nets")
eaglemodel_Approved = Class(name="eaglemodel::Approved")
eaglemodel_Package = Class(name="eaglemodel::Package")
eaglemodel_Polygon = Class(name="eaglemodel::Polygon")
eaglemodel_Wire = Class(name="eaglemodel::Wire")
eaglemodel_Frame = Class(name="eaglemodel::Frame")
eaglemodel_Hole = Class(name="eaglemodel::Hole")
eaglemodel_Pad = Class(name="eaglemodel::Pad")
eaglemodel_SMD = Class(name="eaglemodel::SMD")
eaglemodel_Symbol = Class(name="eaglemodel::Symbol")
eaglemodel_Gates = Class(name="eaglemodel::Gates")
eaglemodel_Devices = Class(name="eaglemodel::Devices")
eaglemodel_Pin = Class(name="eaglemodel::Pin")
eaglemodel_Deviceset = Class(name="eaglemodel::Deviceset")
eaglemodel_Vertex = Class(name="eaglemodel::Vertex")
eaglemodel_Gate = Class(name="eaglemodel::Gate")
eaglemodel_Technology = Class(name="eaglemodel::Technology")
eaglemodel_Device = Class(name="eaglemodel::Device")
eaglemodel_Connects = Class(name="eaglemodel::Connects")
eaglemodel_Technologies = Class(name="eaglemodel::Technologies")
eaglemodel_Connect = Class(name="eaglemodel::Connect")
eaglemodel_Instance = Class(name="eaglemodel::Instance")
eaglemodel_Segment = Class(name="eaglemodel::Segment")
eaglemodel_Net = Class(name="eaglemodel::Net")
eaglemodel_Bus = Class(name="eaglemodel::Bus")
eaglemodel_Pinref = Class(name="eaglemodel::Pinref")
eaglemodel_Junction = Class(name="eaglemodel::Junction")
eaglemodel_Label = Class(name="eaglemodel::Label")

# eaglemodel_Eagle class attributes and methods
eaglemodel_Eagle_version: Property = Property(name="version", type=StringType)
eaglemodel_Eagle.attributes={eaglemodel_Eagle_version}

# eaglemodel_Compatibility class attributes and methods

# eaglemodel_Drawing class attributes and methods

# eaglemodel_Note class attributes and methods
eaglemodel_Note_version: Property = Property(name="version", type=StringType)
eaglemodel_Note_severity: Property = Property(name="severity", type=StringType)
eaglemodel_Note_value: Property = Property(name="value", type=StringType)
eaglemodel_Note.attributes={eaglemodel_Note_severity, eaglemodel_Note_value, eaglemodel_Note_version}

# eaglemodel_Settings class attributes and methods

# eaglemodel_Grid class attributes and methods
eaglemodel_Grid_style: Property = Property(name="style", type=StringType)
eaglemodel_Grid_multiple: Property = Property(name="multiple", type=IntegerType)
eaglemodel_Grid_display: Property = Property(name="display", type=BooleanType)
eaglemodel_Grid_distance: Property = Property(name="distance", type=FloatType)
eaglemodel_Grid_unitdist: Property = Property(name="unitdist", type=StringType)
eaglemodel_Grid_unit: Property = Property(name="unit", type=StringType)
eaglemodel_Grid_altdistance: Property = Property(name="altdistance", type=FloatType)
eaglemodel_Grid_altunitdist: Property = Property(name="altunitdist", type=StringType)
eaglemodel_Grid_altunit: Property = Property(name="altunit", type=StringType)
eaglemodel_Grid.attributes={eaglemodel_Grid_style, eaglemodel_Grid_altdistance, eaglemodel_Grid_multiple, eaglemodel_Grid_altunitdist, eaglemodel_Grid_altunit, eaglemodel_Grid_distance, eaglemodel_Grid_unitdist, eaglemodel_Grid_unit, eaglemodel_Grid_display}

# eaglemodel_Layers class attributes and methods

# eaglemodel_Schematic class attributes and methods
eaglemodel_Schematic_xreflabel: Property = Property(name="xreflabel", type=StringType)
eaglemodel_Schematic_xrefpart: Property = Property(name="xrefpart", type=StringType)
eaglemodel_Schematic.attributes={eaglemodel_Schematic_xreflabel, eaglemodel_Schematic_xrefpart}

# eaglemodel_Setting class attributes and methods
eaglemodel_Setting_alwaysvectorfont: Property = Property(name="alwaysvectorfont", type=BooleanType)
eaglemodel_Setting_verticaltext: Property = Property(name="verticaltext", type=StringType)
eaglemodel_Setting.attributes={eaglemodel_Setting_alwaysvectorfont, eaglemodel_Setting_verticaltext}

# eaglemodel_Libraries class attributes and methods

# eaglemodel_Attributes class attributes and methods

# eaglemodel_Variantdefs class attributes and methods

# eaglemodel_Layer class attributes and methods
eaglemodel_Layer_number: Property = Property(name="number", type=IntegerType)
eaglemodel_Layer_name: Property = Property(name="name", type=StringType)
eaglemodel_Layer_color: Property = Property(name="color", type=IntegerType)
eaglemodel_Layer_fill: Property = Property(name="fill", type=IntegerType)
eaglemodel_Layer_visible: Property = Property(name="visible", type=BooleanType)
eaglemodel_Layer_active: Property = Property(name="active", type=BooleanType)
eaglemodel_Layer.attributes={eaglemodel_Layer_name, eaglemodel_Layer_color, eaglemodel_Layer_fill, eaglemodel_Layer_visible, eaglemodel_Layer_active, eaglemodel_Layer_number}

# eaglemodel_Description class attributes and methods
eaglemodel_Description_language: Property = Property(name="language", type=StringType)
eaglemodel_Description_value: Property = Property(name="value", type=StringType)
eaglemodel_Description.attributes={eaglemodel_Description_language, eaglemodel_Description_value}

# eaglemodel_Packages class attributes and methods

# eaglemodel_Symbols class attributes and methods

# eaglemodel_Classes class attributes and methods

# eaglemodel_Devicesets class attributes and methods

# eaglemodel_Parts class attributes and methods

# eaglemodel_Sheets class attributes and methods

# eaglemodel_Errors class attributes and methods

# eaglemodel_Library class attributes and methods
eaglemodel_Library_name: Property = Property(name="name", type=StringType)
eaglemodel_Library.attributes={eaglemodel_Library_name}

# eaglemodel_Variantdef class attributes and methods
eaglemodel_Variantdef_name: Property = Property(name="name", type=StringType)
eaglemodel_Variantdef_current: Property = Property(name="current", type=BooleanType)
eaglemodel_Variantdef.attributes={eaglemodel_Variantdef_current, eaglemodel_Variantdef_name}

# eaglemodel_Attribute class attributes and methods
eaglemodel_Attribute_name: Property = Property(name="name", type=StringType)
eaglemodel_Attribute_value: Property = Property(name="value", type=StringType)
eaglemodel_Attribute_x: Property = Property(name="x", type=FloatType)
eaglemodel_Attribute_y: Property = Property(name="y", type=FloatType)
eaglemodel_Attribute_size: Property = Property(name="size", type=FloatType)
eaglemodel_Attribute_layer: Property = Property(name="layer", type=IntegerType)
eaglemodel_Attribute_font: Property = Property(name="font", type=StringType)
eaglemodel_Attribute_ratio: Property = Property(name="ratio", type=IntegerType)
eaglemodel_Attribute_rot: Property = Property(name="rot", type=IntegerType)
eaglemodel_Attribute_display: Property = Property(name="display", type=StringType)
eaglemodel_Attribute_constant: Property = Property(name="constant", type=BooleanType)
eaglemodel_Attribute.attributes={eaglemodel_Attribute_display, eaglemodel_Attribute_y, eaglemodel_Attribute_value, eaglemodel_Attribute_font, eaglemodel_Attribute_rot, eaglemodel_Attribute_ratio, eaglemodel_Attribute_name, eaglemodel_Attribute_layer, eaglemodel_Attribute_constant, eaglemodel_Attribute_x, eaglemodel_Attribute_size}

# eaglemodel_Part class attributes and methods
eaglemodel_Part_name: Property = Property(name="name", type=StringType)
eaglemodel_Part_library: Property = Property(name="library", type=StringType)
eaglemodel_Part_deviceset: Property = Property(name="deviceset", type=StringType)
eaglemodel_Part_device: Property = Property(name="device", type=StringType)
eaglemodel_Part_technology: Property = Property(name="technology", type=StringType)
eaglemodel_Part_value: Property = Property(name="value", type=StringType)
eaglemodel_Part_gate: Property = Property(name="gate", type=StringType)
eaglemodel_Part_x: Property = Property(name="x", type=FloatType)
eaglemodel_Part_y: Property = Property(name="y", type=FloatType)
eaglemodel_Part_smashed: Property = Property(name="smashed", type=BooleanType)
eaglemodel_Part_rot: Property = Property(name="rot", type=IntegerType)
eaglemodel_Part_uid: Property = Property(name="uid", type=IntegerType)
eaglemodel_Part.attributes={eaglemodel_Part_device, eaglemodel_Part_gate, eaglemodel_Part_y, eaglemodel_Part_rot, eaglemodel_Part_uid, eaglemodel_Part_value, eaglemodel_Part_deviceset, eaglemodel_Part_name, eaglemodel_Part_smashed, eaglemodel_Part_library, eaglemodel_Part_technology, eaglemodel_Part_x}

# eaglemodel_Variant class attributes and methods
eaglemodel_Variant_name: Property = Property(name="name", type=StringType)
eaglemodel_Variant_populate: Property = Property(name="populate", type=BooleanType)
eaglemodel_Variant_value: Property = Property(name="value", type=StringType)
eaglemodel_Variant_technology: Property = Property(name="technology", type=StringType)
eaglemodel_Variant.attributes={eaglemodel_Variant_technology, eaglemodel_Variant_name, eaglemodel_Variant_value, eaglemodel_Variant_populate}

# eaglemodel_Class class attributes and methods
eaglemodel_Class_number: Property = Property(name="number", type=IntegerType)
eaglemodel_Class_name: Property = Property(name="name", type=StringType)
eaglemodel_Class_width: Property = Property(name="width", type=FloatType)
eaglemodel_Class_drill: Property = Property(name="drill", type=FloatType)
eaglemodel_Class.attributes={eaglemodel_Class_width, eaglemodel_Class_number, eaglemodel_Class_drill, eaglemodel_Class_name}

# eaglemodel_Clearance class attributes and methods
eaglemodel_Clearance_class: Property = Property(name="class", type=IntegerType)
eaglemodel_Clearance_value: Property = Property(name="value", type=FloatType)
eaglemodel_Clearance.attributes={eaglemodel_Clearance_value, eaglemodel_Clearance_class}

# eaglemodel_Plain class attributes and methods

# eaglemodel_Instances class attributes and methods

# eaglemodel_Busses class attributes and methods

# eaglemodel_Sheet class attributes and methods

# eaglemodel_Text class attributes and methods
eaglemodel_Text_x: Property = Property(name="x", type=FloatType)
eaglemodel_Text_y: Property = Property(name="y", type=FloatType)
eaglemodel_Text_size: Property = Property(name="size", type=FloatType)
eaglemodel_Text_layer: Property = Property(name="layer", type=IntegerType)
eaglemodel_Text_font: Property = Property(name="font", type=StringType)
eaglemodel_Text_ratio: Property = Property(name="ratio", type=IntegerType)
eaglemodel_Text_rot: Property = Property(name="rot", type=IntegerType)
eaglemodel_Text_align: Property = Property(name="align", type=StringType)
eaglemodel_Text_distance: Property = Property(name="distance", type=IntegerType)
eaglemodel_Text_value: Property = Property(name="value", type=StringType)
eaglemodel_Text.attributes={eaglemodel_Text_size, eaglemodel_Text_value, eaglemodel_Text_font, eaglemodel_Text_distance, eaglemodel_Text_rot, eaglemodel_Text_align, eaglemodel_Text_x, eaglemodel_Text_y, eaglemodel_Text_layer, eaglemodel_Text_ratio}

# eaglemodel_Dimension class attributes and methods
eaglemodel_Dimension_x2: Property = Property(name="x2", type=FloatType)
eaglemodel_Dimension_y2: Property = Property(name="y2", type=FloatType)
eaglemodel_Dimension_x3: Property = Property(name="x3", type=FloatType)
eaglemodel_Dimension_y3: Property = Property(name="y3", type=FloatType)
eaglemodel_Dimension_layer: Property = Property(name="layer", type=IntegerType)
eaglemodel_Dimension_dtype: Property = Property(name="dtype", type=StringType)
eaglemodel_Dimension_width: Property = Property(name="width", type=FloatType)
eaglemodel_Dimension_extwidth: Property = Property(name="extwidth", type=FloatType)
eaglemodel_Dimension_extlength: Property = Property(name="extlength", type=FloatType)
eaglemodel_Dimension_extoffset: Property = Property(name="extoffset", type=FloatType)
eaglemodel_Dimension_x1: Property = Property(name="x1", type=FloatType)
eaglemodel_Dimension_y1: Property = Property(name="y1", type=FloatType)
eaglemodel_Dimension_textsize: Property = Property(name="textsize", type=FloatType)
eaglemodel_Dimension_textratio: Property = Property(name="textratio", type=IntegerType)
eaglemodel_Dimension_unit: Property = Property(name="unit", type=StringType)
eaglemodel_Dimension_precision: Property = Property(name="precision", type=IntegerType)
eaglemodel_Dimension_visible: Property = Property(name="visible", type=BooleanType)
eaglemodel_Dimension.attributes={eaglemodel_Dimension_x3, eaglemodel_Dimension_layer, eaglemodel_Dimension_y1, eaglemodel_Dimension_dtype, eaglemodel_Dimension_textsize, eaglemodel_Dimension_y2, eaglemodel_Dimension_y3, eaglemodel_Dimension_visible, eaglemodel_Dimension_x2, eaglemodel_Dimension_width, eaglemodel_Dimension_extoffset, eaglemodel_Dimension_textratio, eaglemodel_Dimension_extlength, eaglemodel_Dimension_unit, eaglemodel_Dimension_extwidth, eaglemodel_Dimension_x1, eaglemodel_Dimension_precision}

# eaglemodel_Circle class attributes and methods
eaglemodel_Circle_x: Property = Property(name="x", type=FloatType)
eaglemodel_Circle_y: Property = Property(name="y", type=FloatType)
eaglemodel_Circle_radius: Property = Property(name="radius", type=FloatType)
eaglemodel_Circle_width: Property = Property(name="width", type=FloatType)
eaglemodel_Circle_layer: Property = Property(name="layer", type=IntegerType)
eaglemodel_Circle.attributes={eaglemodel_Circle_width, eaglemodel_Circle_y, eaglemodel_Circle_x, eaglemodel_Circle_layer, eaglemodel_Circle_radius}

# eaglemodel_Rectangle class attributes and methods
eaglemodel_Rectangle_x1: Property = Property(name="x1", type=FloatType)
eaglemodel_Rectangle_y1: Property = Property(name="y1", type=FloatType)
eaglemodel_Rectangle_x2: Property = Property(name="x2", type=FloatType)
eaglemodel_Rectangle_y2: Property = Property(name="y2", type=FloatType)
eaglemodel_Rectangle_layer: Property = Property(name="layer", type=IntegerType)
eaglemodel_Rectangle_rot: Property = Property(name="rot", type=IntegerType)
eaglemodel_Rectangle.attributes={eaglemodel_Rectangle_y2, eaglemodel_Rectangle_rot, eaglemodel_Rectangle_x2, eaglemodel_Rectangle_layer, eaglemodel_Rectangle_y1, eaglemodel_Rectangle_x1}

# eaglemodel_Nets class attributes and methods

# eaglemodel_Approved class attributes and methods
eaglemodel_Approved_hash: Property = Property(name="hash", type=StringType)
eaglemodel_Approved.attributes={eaglemodel_Approved_hash}

# eaglemodel_Package class attributes and methods
eaglemodel_Package_name: Property = Property(name="name", type=StringType)
eaglemodel_Package.attributes={eaglemodel_Package_name}

# eaglemodel_Polygon class attributes and methods
eaglemodel_Polygon_width: Property = Property(name="width", type=FloatType)
eaglemodel_Polygon_layer: Property = Property(name="layer", type=IntegerType)
eaglemodel_Polygon_spacing: Property = Property(name="spacing", type=FloatType)
eaglemodel_Polygon_pour: Property = Property(name="pour", type=StringType)
eaglemodel_Polygon_isolate: Property = Property(name="isolate", type=FloatType)
eaglemodel_Polygon_orphans: Property = Property(name="orphans", type=BooleanType)
eaglemodel_Polygon_thermals: Property = Property(name="thermals", type=BooleanType)
eaglemodel_Polygon_rank: Property = Property(name="rank", type=IntegerType)
eaglemodel_Polygon.attributes={eaglemodel_Polygon_width, eaglemodel_Polygon_layer, eaglemodel_Polygon_pour, eaglemodel_Polygon_thermals, eaglemodel_Polygon_rank, eaglemodel_Polygon_spacing, eaglemodel_Polygon_isolate, eaglemodel_Polygon_orphans}

# eaglemodel_Wire class attributes and methods
eaglemodel_Wire_x1: Property = Property(name="x1", type=FloatType)
eaglemodel_Wire_y1: Property = Property(name="y1", type=FloatType)
eaglemodel_Wire_x2: Property = Property(name="x2", type=FloatType)
eaglemodel_Wire_y2: Property = Property(name="y2", type=FloatType)
eaglemodel_Wire_width: Property = Property(name="width", type=FloatType)
eaglemodel_Wire_layer: Property = Property(name="layer", type=IntegerType)
eaglemodel_Wire_extent: Property = Property(name="extent", type=StringType)
eaglemodel_Wire_style: Property = Property(name="style", type=StringType)
eaglemodel_Wire_curve: Property = Property(name="curve", type=FloatType)
eaglemodel_Wire_cap: Property = Property(name="cap", type=StringType)
eaglemodel_Wire.attributes={eaglemodel_Wire_y1, eaglemodel_Wire_y2, eaglemodel_Wire_x2, eaglemodel_Wire_width, eaglemodel_Wire_style, eaglemodel_Wire_cap, eaglemodel_Wire_x1, eaglemodel_Wire_extent, eaglemodel_Wire_curve, eaglemodel_Wire_layer}

# eaglemodel_Frame class attributes and methods
eaglemodel_Frame_x1: Property = Property(name="x1", type=FloatType)
eaglemodel_Frame_y1: Property = Property(name="y1", type=FloatType)
eaglemodel_Frame_x2: Property = Property(name="x2", type=FloatType)
eaglemodel_Frame_y2: Property = Property(name="y2", type=FloatType)
eaglemodel_Frame_columns: Property = Property(name="columns", type=IntegerType)
eaglemodel_Frame_rows: Property = Property(name="rows", type=IntegerType)
eaglemodel_Frame_layer: Property = Property(name="layer", type=IntegerType)
eaglemodel_Frame_borderleft: Property = Property(name="borderleft", type=BooleanType)
eaglemodel_Frame_bordertop: Property = Property(name="bordertop", type=BooleanType)
eaglemodel_Frame_borderright: Property = Property(name="borderright", type=BooleanType)
eaglemodel_Frame_borderbottom: Property = Property(name="borderbottom", type=BooleanType)
eaglemodel_Frame.attributes={eaglemodel_Frame_layer, eaglemodel_Frame_borderleft, eaglemodel_Frame_borderright, eaglemodel_Frame_y1, eaglemodel_Frame_columns, eaglemodel_Frame_x2, eaglemodel_Frame_borderbottom, eaglemodel_Frame_x1, eaglemodel_Frame_bordertop, eaglemodel_Frame_rows, eaglemodel_Frame_y2}

# eaglemodel_Hole class attributes and methods
eaglemodel_Hole_x: Property = Property(name="x", type=FloatType)
eaglemodel_Hole_y: Property = Property(name="y", type=FloatType)
eaglemodel_Hole_drill: Property = Property(name="drill", type=FloatType)
eaglemodel_Hole.attributes={eaglemodel_Hole_x, eaglemodel_Hole_drill, eaglemodel_Hole_y}

# eaglemodel_Pad class attributes and methods
eaglemodel_Pad_name: Property = Property(name="name", type=StringType)
eaglemodel_Pad_x: Property = Property(name="x", type=FloatType)
eaglemodel_Pad_y: Property = Property(name="y", type=FloatType)
eaglemodel_Pad_drill: Property = Property(name="drill", type=FloatType)
eaglemodel_Pad_diameter: Property = Property(name="diameter", type=FloatType)
eaglemodel_Pad_shape: Property = Property(name="shape", type=StringType)
eaglemodel_Pad_rot: Property = Property(name="rot", type=IntegerType)
eaglemodel_Pad_stop: Property = Property(name="stop", type=BooleanType)
eaglemodel_Pad_thermals: Property = Property(name="thermals", type=BooleanType)
eaglemodel_Pad_first: Property = Property(name="first", type=BooleanType)
eaglemodel_Pad.attributes={eaglemodel_Pad_y, eaglemodel_Pad_thermals, eaglemodel_Pad_diameter, eaglemodel_Pad_x, eaglemodel_Pad_drill, eaglemodel_Pad_name, eaglemodel_Pad_shape, eaglemodel_Pad_rot, eaglemodel_Pad_first, eaglemodel_Pad_stop}

# eaglemodel_SMD class attributes and methods
eaglemodel_SMD_thermals: Property = Property(name="thermals", type=BooleanType)
eaglemodel_SMD_cream: Property = Property(name="cream", type=BooleanType)
eaglemodel_SMD_name: Property = Property(name="name", type=StringType)
eaglemodel_SMD_x: Property = Property(name="x", type=FloatType)
eaglemodel_SMD_y: Property = Property(name="y", type=FloatType)
eaglemodel_SMD_dx: Property = Property(name="dx", type=FloatType)
eaglemodel_SMD_dy: Property = Property(name="dy", type=FloatType)
eaglemodel_SMD_layer: Property = Property(name="layer", type=IntegerType)
eaglemodel_SMD_roundness: Property = Property(name="roundness", type=IntegerType)
eaglemodel_SMD_rot: Property = Property(name="rot", type=IntegerType)
eaglemodel_SMD_stop: Property = Property(name="stop", type=BooleanType)
eaglemodel_SMD.attributes={eaglemodel_SMD_y, eaglemodel_SMD_cream, eaglemodel_SMD_name, eaglemodel_SMD_dx, eaglemodel_SMD_dy, eaglemodel_SMD_stop, eaglemodel_SMD_roundness, eaglemodel_SMD_x, eaglemodel_SMD_thermals, eaglemodel_SMD_layer, eaglemodel_SMD_rot}

# eaglemodel_Symbol class attributes and methods
eaglemodel_Symbol_name: Property = Property(name="name", type=StringType)
eaglemodel_Symbol.attributes={eaglemodel_Symbol_name}

# eaglemodel_Gates class attributes and methods

# eaglemodel_Devices class attributes and methods

# eaglemodel_Pin class attributes and methods
eaglemodel_Pin_name: Property = Property(name="name", type=StringType)
eaglemodel_Pin_x: Property = Property(name="x", type=FloatType)
eaglemodel_Pin_y: Property = Property(name="y", type=FloatType)
eaglemodel_Pin_visible: Property = Property(name="visible", type=StringType)
eaglemodel_Pin_length: Property = Property(name="length", type=StringType)
eaglemodel_Pin_direction: Property = Property(name="direction", type=StringType)
eaglemodel_Pin_function: Property = Property(name="function", type=StringType)
eaglemodel_Pin_swaplevel: Property = Property(name="swaplevel", type=IntegerType)
eaglemodel_Pin_rot: Property = Property(name="rot", type=IntegerType)
eaglemodel_Pin.attributes={eaglemodel_Pin_swaplevel, eaglemodel_Pin_visible, eaglemodel_Pin_y, eaglemodel_Pin_function, eaglemodel_Pin_name, eaglemodel_Pin_x, eaglemodel_Pin_direction, eaglemodel_Pin_rot, eaglemodel_Pin_length}

# eaglemodel_Deviceset class attributes and methods
eaglemodel_Deviceset_name: Property = Property(name="name", type=StringType)
eaglemodel_Deviceset_prefix: Property = Property(name="prefix", type=StringType)
eaglemodel_Deviceset_uservalue: Property = Property(name="uservalue", type=BooleanType)
eaglemodel_Deviceset.attributes={eaglemodel_Deviceset_prefix, eaglemodel_Deviceset_uservalue, eaglemodel_Deviceset_name}

# eaglemodel_Vertex class attributes and methods
eaglemodel_Vertex_x: Property = Property(name="x", type=FloatType)
eaglemodel_Vertex_y: Property = Property(name="y", type=FloatType)
eaglemodel_Vertex_curve: Property = Property(name="curve", type=FloatType)
eaglemodel_Vertex.attributes={eaglemodel_Vertex_x, eaglemodel_Vertex_curve, eaglemodel_Vertex_y}

# eaglemodel_Gate class attributes and methods
eaglemodel_Gate_name: Property = Property(name="name", type=StringType)
eaglemodel_Gate_symbol: Property = Property(name="symbol", type=StringType)
eaglemodel_Gate_x: Property = Property(name="x", type=FloatType)
eaglemodel_Gate_y: Property = Property(name="y", type=FloatType)
eaglemodel_Gate_addlevel: Property = Property(name="addlevel", type=StringType)
eaglemodel_Gate_swaplevel: Property = Property(name="swaplevel", type=IntegerType)
eaglemodel_Gate.attributes={eaglemodel_Gate_swaplevel, eaglemodel_Gate_addlevel, eaglemodel_Gate_name, eaglemodel_Gate_x, eaglemodel_Gate_symbol, eaglemodel_Gate_y}

# eaglemodel_Technology class attributes and methods
eaglemodel_Technology_name: Property = Property(name="name", type=StringType)
eaglemodel_Technology.attributes={eaglemodel_Technology_name}

# eaglemodel_Device class attributes and methods
eaglemodel_Device_name: Property = Property(name="name", type=StringType)
eaglemodel_Device_package: Property = Property(name="package", type=StringType)
eaglemodel_Device.attributes={eaglemodel_Device_package, eaglemodel_Device_name}

# eaglemodel_Connects class attributes and methods

# eaglemodel_Technologies class attributes and methods

# eaglemodel_Connect class attributes and methods
eaglemodel_Connect_gate: Property = Property(name="gate", type=StringType)
eaglemodel_Connect_pin: Property = Property(name="pin", type=StringType)
eaglemodel_Connect_pad: Property = Property(name="pad", type=StringType)
eaglemodel_Connect_route: Property = Property(name="route", type=StringType)
eaglemodel_Connect.attributes={eaglemodel_Connect_pad, eaglemodel_Connect_pin, eaglemodel_Connect_route, eaglemodel_Connect_gate}

# eaglemodel_Instance class attributes and methods
eaglemodel_Instance_part: Property = Property(name="part", type=StringType)
eaglemodel_Instance_gate: Property = Property(name="gate", type=StringType)
eaglemodel_Instance_x: Property = Property(name="x", type=FloatType)
eaglemodel_Instance_y: Property = Property(name="y", type=FloatType)
eaglemodel_Instance_smashed: Property = Property(name="smashed", type=BooleanType)
eaglemodel_Instance_rot: Property = Property(name="rot", type=IntegerType)
eaglemodel_Instance.attributes={eaglemodel_Instance_rot, eaglemodel_Instance_y, eaglemodel_Instance_gate, eaglemodel_Instance_part, eaglemodel_Instance_smashed, eaglemodel_Instance_x}

# eaglemodel_Segment class attributes and methods

# eaglemodel_Net class attributes and methods
eaglemodel_Net_name: Property = Property(name="name", type=StringType)
eaglemodel_Net_class: Property = Property(name="class", type=IntegerType)
eaglemodel_Net.attributes={eaglemodel_Net_class, eaglemodel_Net_name}

# eaglemodel_Bus class attributes and methods
eaglemodel_Bus_name: Property = Property(name="name", type=StringType)
eaglemodel_Bus.attributes={eaglemodel_Bus_name}

# eaglemodel_Pinref class attributes and methods
eaglemodel_Pinref_part: Property = Property(name="part", type=StringType)
eaglemodel_Pinref_gate: Property = Property(name="gate", type=StringType)
eaglemodel_Pinref_pin: Property = Property(name="pin", type=StringType)
eaglemodel_Pinref.attributes={eaglemodel_Pinref_pin, eaglemodel_Pinref_gate, eaglemodel_Pinref_part}

# eaglemodel_Junction class attributes and methods
eaglemodel_Junction_x: Property = Property(name="x", type=FloatType)
eaglemodel_Junction_y: Property = Property(name="y", type=FloatType)
eaglemodel_Junction.attributes={eaglemodel_Junction_y, eaglemodel_Junction_x}

# eaglemodel_Label class attributes and methods
eaglemodel_Label_x: Property = Property(name="x", type=FloatType)
eaglemodel_Label_y: Property = Property(name="y", type=FloatType)
eaglemodel_Label_size: Property = Property(name="size", type=FloatType)
eaglemodel_Label_layer: Property = Property(name="layer", type=IntegerType)
eaglemodel_Label_font: Property = Property(name="font", type=StringType)
eaglemodel_Label_ratio: Property = Property(name="ratio", type=IntegerType)
eaglemodel_Label_rot: Property = Property(name="rot", type=IntegerType)
eaglemodel_Label_xref: Property = Property(name="xref", type=BooleanType)
eaglemodel_Label.attributes={eaglemodel_Label_size, eaglemodel_Label_rot, eaglemodel_Label_x, eaglemodel_Label_layer, eaglemodel_Label_xref, eaglemodel_Label_ratio, eaglemodel_Label_font, eaglemodel_Label_y}

# Relationships
compatibility0: BinaryAssociation = BinaryAssociation(
    name="compatibility0",
    ends={
        Property(name="eaglemodel_Compatibility", type=eaglemodel_Eagle, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Eagle", type=eaglemodel_Compatibility, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
drawing1: BinaryAssociation = BinaryAssociation(
    name="drawing1",
    ends={
        Property(name="eaglemodel_Drawing", type=eaglemodel_Eagle, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Eagle2", type=eaglemodel_Drawing, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
note3: BinaryAssociation = BinaryAssociation(
    name="note3",
    ends={
        Property(name="eaglemodel_Note", type=eaglemodel_Compatibility, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Compatibility4", type=eaglemodel_Note, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
settings5: BinaryAssociation = BinaryAssociation(
    name="settings5",
    ends={
        Property(name="eaglemodel_Settings", type=eaglemodel_Drawing, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Drawing6", type=eaglemodel_Settings, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
grid7: BinaryAssociation = BinaryAssociation(
    name="grid7",
    ends={
        Property(name="eaglemodel_Grid", type=eaglemodel_Drawing, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Drawing8", type=eaglemodel_Grid, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layers9: BinaryAssociation = BinaryAssociation(
    name="layers9",
    ends={
        Property(name="eaglemodel_Layers", type=eaglemodel_Drawing, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Drawing10", type=eaglemodel_Layers, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
schematic11: BinaryAssociation = BinaryAssociation(
    name="schematic11",
    ends={
        Property(name="eaglemodel_Schematic", type=eaglemodel_Drawing, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Drawing12", type=eaglemodel_Schematic, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
settings13: BinaryAssociation = BinaryAssociation(
    name="settings13",
    ends={
        Property(name="eaglemodel_Setting", type=eaglemodel_Settings, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Settings14", type=eaglemodel_Setting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
libraries19: BinaryAssociation = BinaryAssociation(
    name="libraries19",
    ends={
        Property(name="eaglemodel_Libraries", type=eaglemodel_Schematic, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Schematic20", type=eaglemodel_Libraries, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes21: BinaryAssociation = BinaryAssociation(
    name="attributes21",
    ends={
        Property(name="eaglemodel_Attributes", type=eaglemodel_Schematic, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Schematic22", type=eaglemodel_Attributes, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variantdefs23: BinaryAssociation = BinaryAssociation(
    name="variantdefs23",
    ends={
        Property(name="eaglemodel_Variantdefs", type=eaglemodel_Schematic, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Schematic24", type=eaglemodel_Variantdefs, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
layers15: BinaryAssociation = BinaryAssociation(
    name="layers15",
    ends={
        Property(name="eaglemodel_Layer", type=eaglemodel_Layers, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Layers16", type=eaglemodel_Layer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
description17: BinaryAssociation = BinaryAssociation(
    name="description17",
    ends={
        Property(name="eaglemodel_Description", type=eaglemodel_Schematic, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Schematic18", type=eaglemodel_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description35: BinaryAssociation = BinaryAssociation(
    name="description35",
    ends={
        Property(name="eaglemodel_Description37", type=eaglemodel_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Library36", type=eaglemodel_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packages38: BinaryAssociation = BinaryAssociation(
    name="packages38",
    ends={
        Property(name="eaglemodel_Packages", type=eaglemodel_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Library39", type=eaglemodel_Packages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
symbols40: BinaryAssociation = BinaryAssociation(
    name="symbols40",
    ends={
        Property(name="eaglemodel_Symbols", type=eaglemodel_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Library41", type=eaglemodel_Symbols, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classes25: BinaryAssociation = BinaryAssociation(
    name="classes25",
    ends={
        Property(name="eaglemodel_Classes", type=eaglemodel_Schematic, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Schematic26", type=eaglemodel_Classes, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
devicesets42: BinaryAssociation = BinaryAssociation(
    name="devicesets42",
    ends={
        Property(name="eaglemodel_Devicesets", type=eaglemodel_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Library43", type=eaglemodel_Devicesets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts27: BinaryAssociation = BinaryAssociation(
    name="parts27",
    ends={
        Property(name="eaglemodel_Parts", type=eaglemodel_Schematic, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Schematic28", type=eaglemodel_Parts, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sheets29: BinaryAssociation = BinaryAssociation(
    name="sheets29",
    ends={
        Property(name="eaglemodel_Sheets", type=eaglemodel_Schematic, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Schematic30", type=eaglemodel_Sheets, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
errors31: BinaryAssociation = BinaryAssociation(
    name="errors31",
    ends={
        Property(name="eaglemodel_Errors", type=eaglemodel_Schematic, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Schematic32", type=eaglemodel_Errors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
library33: BinaryAssociation = BinaryAssociation(
    name="library33",
    ends={
        Property(name="eaglemodel_Library", type=eaglemodel_Libraries, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Libraries34", type=eaglemodel_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variantdef46: BinaryAssociation = BinaryAssociation(
    name="variantdef46",
    ends={
        Property(name="eaglemodel_Variantdef", type=eaglemodel_Variantdefs, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Variantdefs47", type=eaglemodel_Variantdef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute44: BinaryAssociation = BinaryAssociation(
    name="attribute44",
    ends={
        Property(name="eaglemodel_Attribute", type=eaglemodel_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Attributes45", type=eaglemodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part52: BinaryAssociation = BinaryAssociation(
    name="part52",
    ends={
        Property(name="eaglemodel_Part", type=eaglemodel_Parts, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Parts53", type=eaglemodel_Part, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class48: BinaryAssociation = BinaryAssociation(
    name="class48",
    ends={
        Property(name="eaglemodel_Class", type=eaglemodel_Classes, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Classes49", type=eaglemodel_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clearance50: BinaryAssociation = BinaryAssociation(
    name="clearance50",
    ends={
        Property(name="eaglemodel_Clearance", type=eaglemodel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Class51", type=eaglemodel_Clearance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description61: BinaryAssociation = BinaryAssociation(
    name="description61",
    ends={
        Property(name="eaglemodel_Description63", type=eaglemodel_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Sheet62", type=eaglemodel_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
plain64: BinaryAssociation = BinaryAssociation(
    name="plain64",
    ends={
        Property(name="eaglemodel_Plain", type=eaglemodel_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Sheet65", type=eaglemodel_Plain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instances66: BinaryAssociation = BinaryAssociation(
    name="instances66",
    ends={
        Property(name="eaglemodel_Instances", type=eaglemodel_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Sheet67", type=eaglemodel_Instances, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
busses68: BinaryAssociation = BinaryAssociation(
    name="busses68",
    ends={
        Property(name="eaglemodel_Busses", type=eaglemodel_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Sheet69", type=eaglemodel_Busses, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute54: BinaryAssociation = BinaryAssociation(
    name="attribute54",
    ends={
        Property(name="eaglemodel_Attribute56", type=eaglemodel_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Part55", type=eaglemodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variant57: BinaryAssociation = BinaryAssociation(
    name="variant57",
    ends={
        Property(name="eaglemodel_Variant", type=eaglemodel_Part, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Part58", type=eaglemodel_Variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sheet59: BinaryAssociation = BinaryAssociation(
    name="sheet59",
    ends={
        Property(name="eaglemodel_Sheet", type=eaglemodel_Sheets, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Sheets60", type=eaglemodel_Sheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wire81: BinaryAssociation = BinaryAssociation(
    name="wire81",
    ends={
        Property(name="eaglemodel_Wire", type=eaglemodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Package82", type=eaglemodel_Wire, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
text83: BinaryAssociation = BinaryAssociation(
    name="text83",
    ends={
        Property(name="eaglemodel_Text", type=eaglemodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Package84", type=eaglemodel_Text, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimension85: BinaryAssociation = BinaryAssociation(
    name="dimension85",
    ends={
        Property(name="eaglemodel_Dimension", type=eaglemodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Package86", type=eaglemodel_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
circle87: BinaryAssociation = BinaryAssociation(
    name="circle87",
    ends={
        Property(name="eaglemodel_Circle", type=eaglemodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Package88", type=eaglemodel_Circle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nets70: BinaryAssociation = BinaryAssociation(
    name="nets70",
    ends={
        Property(name="eaglemodel_Nets", type=eaglemodel_Sheet, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Sheet71", type=eaglemodel_Nets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
error72: BinaryAssociation = BinaryAssociation(
    name="error72",
    ends={
        Property(name="eaglemodel_Approved", type=eaglemodel_Errors, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Errors73", type=eaglemodel_Approved, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package74: BinaryAssociation = BinaryAssociation(
    name="package74",
    ends={
        Property(name="eaglemodel_Package", type=eaglemodel_Packages, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Packages75", type=eaglemodel_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description76: BinaryAssociation = BinaryAssociation(
    name="description76",
    ends={
        Property(name="eaglemodel_Description78", type=eaglemodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Package77", type=eaglemodel_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
polygon79: BinaryAssociation = BinaryAssociation(
    name="polygon79",
    ends={
        Property(name="eaglemodel_Polygon", type=eaglemodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Package80", type=eaglemodel_Polygon, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description101: BinaryAssociation = BinaryAssociation(
    name="description101",
    ends={
        Property(name="eaglemodel_Description103", type=eaglemodel_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Symbol102", type=eaglemodel_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
polygon104: BinaryAssociation = BinaryAssociation(
    name="polygon104",
    ends={
        Property(name="eaglemodel_Polygon106", type=eaglemodel_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Symbol105", type=eaglemodel_Polygon, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wire107: BinaryAssociation = BinaryAssociation(
    name="wire107",
    ends={
        Property(name="eaglemodel_Wire109", type=eaglemodel_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Symbol108", type=eaglemodel_Wire, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
text110: BinaryAssociation = BinaryAssociation(
    name="text110",
    ends={
        Property(name="eaglemodel_Text112", type=eaglemodel_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Symbol111", type=eaglemodel_Text, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rectangle89: BinaryAssociation = BinaryAssociation(
    name="rectangle89",
    ends={
        Property(name="eaglemodel_Rectangle", type=eaglemodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Package90", type=eaglemodel_Rectangle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
frame91: BinaryAssociation = BinaryAssociation(
    name="frame91",
    ends={
        Property(name="eaglemodel_Frame", type=eaglemodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Package92", type=eaglemodel_Frame, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hole93: BinaryAssociation = BinaryAssociation(
    name="hole93",
    ends={
        Property(name="eaglemodel_Hole", type=eaglemodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Package94", type=eaglemodel_Hole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pad95: BinaryAssociation = BinaryAssociation(
    name="pad95",
    ends={
        Property(name="eaglemodel_Pad", type=eaglemodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Package96", type=eaglemodel_Pad, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
smd97: BinaryAssociation = BinaryAssociation(
    name="smd97",
    ends={
        Property(name="eaglemodel_SMD", type=eaglemodel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Package98", type=eaglemodel_SMD, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
symbol99: BinaryAssociation = BinaryAssociation(
    name="symbol99",
    ends={
        Property(name="eaglemodel_Symbol", type=eaglemodel_Symbols, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Symbols100", type=eaglemodel_Symbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description129: BinaryAssociation = BinaryAssociation(
    name="description129",
    ends={
        Property(name="eaglemodel_Description131", type=eaglemodel_Deviceset, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Deviceset130", type=eaglemodel_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gates132: BinaryAssociation = BinaryAssociation(
    name="gates132",
    ends={
        Property(name="eaglemodel_Gates", type=eaglemodel_Deviceset, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Deviceset133", type=eaglemodel_Gates, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
devices134: BinaryAssociation = BinaryAssociation(
    name="devices134",
    ends={
        Property(name="eaglemodel_Devices", type=eaglemodel_Deviceset, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Deviceset135", type=eaglemodel_Devices, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimension113: BinaryAssociation = BinaryAssociation(
    name="dimension113",
    ends={
        Property(name="eaglemodel_Dimension115", type=eaglemodel_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Symbol114", type=eaglemodel_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pin116: BinaryAssociation = BinaryAssociation(
    name="pin116",
    ends={
        Property(name="eaglemodel_Pin", type=eaglemodel_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Symbol117", type=eaglemodel_Pin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
circle118: BinaryAssociation = BinaryAssociation(
    name="circle118",
    ends={
        Property(name="eaglemodel_Circle120", type=eaglemodel_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Symbol119", type=eaglemodel_Circle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rectangle121: BinaryAssociation = BinaryAssociation(
    name="rectangle121",
    ends={
        Property(name="eaglemodel_Rectangle123", type=eaglemodel_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Symbol122", type=eaglemodel_Rectangle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
frame124: BinaryAssociation = BinaryAssociation(
    name="frame124",
    ends={
        Property(name="eaglemodel_Frame126", type=eaglemodel_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Symbol125", type=eaglemodel_Frame, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deviceset127: BinaryAssociation = BinaryAssociation(
    name="deviceset127",
    ends={
        Property(name="eaglemodel_Deviceset", type=eaglemodel_Devicesets, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Devicesets128", type=eaglemodel_Deviceset, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vertex136: BinaryAssociation = BinaryAssociation(
    name="vertex136",
    ends={
        Property(name="eaglemodel_Vertex", type=eaglemodel_Polygon, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Polygon137", type=eaglemodel_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gate138: BinaryAssociation = BinaryAssociation(
    name="gate138",
    ends={
        Property(name="eaglemodel_Gate", type=eaglemodel_Gates, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Gates139", type=eaglemodel_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
technology148: BinaryAssociation = BinaryAssociation(
    name="technology148",
    ends={
        Property(name="eaglemodel_Technology", type=eaglemodel_Technologies, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Technologies149", type=eaglemodel_Technology, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
device140: BinaryAssociation = BinaryAssociation(
    name="device140",
    ends={
        Property(name="eaglemodel_Device", type=eaglemodel_Devices, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Devices141", type=eaglemodel_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connects142: BinaryAssociation = BinaryAssociation(
    name="connects142",
    ends={
        Property(name="eaglemodel_Connects", type=eaglemodel_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Device143", type=eaglemodel_Connects, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
technologies144: BinaryAssociation = BinaryAssociation(
    name="technologies144",
    ends={
        Property(name="eaglemodel_Technologies", type=eaglemodel_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Device145", type=eaglemodel_Technologies, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connect146: BinaryAssociation = BinaryAssociation(
    name="connect146",
    ends={
        Property(name="eaglemodel_Connect", type=eaglemodel_Connects, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Connects147", type=eaglemodel_Connect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
frame171: BinaryAssociation = BinaryAssociation(
    name="frame171",
    ends={
        Property(name="eaglemodel_Frame173", type=eaglemodel_Plain, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Plain172", type=eaglemodel_Frame, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hole174: BinaryAssociation = BinaryAssociation(
    name="hole174",
    ends={
        Property(name="eaglemodel_Hole176", type=eaglemodel_Plain, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Plain175", type=eaglemodel_Hole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instance177: BinaryAssociation = BinaryAssociation(
    name="instance177",
    ends={
        Property(name="eaglemodel_Instance", type=eaglemodel_Instances, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Instances178", type=eaglemodel_Instance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute150: BinaryAssociation = BinaryAssociation(
    name="attribute150",
    ends={
        Property(name="eaglemodel_Attribute152", type=eaglemodel_Technology, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Technology151", type=eaglemodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
polygon153: BinaryAssociation = BinaryAssociation(
    name="polygon153",
    ends={
        Property(name="eaglemodel_Polygon155", type=eaglemodel_Plain, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Plain154", type=eaglemodel_Polygon, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wire156: BinaryAssociation = BinaryAssociation(
    name="wire156",
    ends={
        Property(name="eaglemodel_Wire158", type=eaglemodel_Plain, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Plain157", type=eaglemodel_Wire, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
text159: BinaryAssociation = BinaryAssociation(
    name="text159",
    ends={
        Property(name="eaglemodel_Text161", type=eaglemodel_Plain, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Plain160", type=eaglemodel_Text, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimension162: BinaryAssociation = BinaryAssociation(
    name="dimension162",
    ends={
        Property(name="eaglemodel_Dimension164", type=eaglemodel_Plain, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Plain163", type=eaglemodel_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
circle165: BinaryAssociation = BinaryAssociation(
    name="circle165",
    ends={
        Property(name="eaglemodel_Circle167", type=eaglemodel_Plain, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Plain166", type=eaglemodel_Circle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rectangle168: BinaryAssociation = BinaryAssociation(
    name="rectangle168",
    ends={
        Property(name="eaglemodel_Rectangle170", type=eaglemodel_Plain, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Plain169", type=eaglemodel_Rectangle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
segment184: BinaryAssociation = BinaryAssociation(
    name="segment184",
    ends={
        Property(name="eaglemodel_Segment", type=eaglemodel_Bus, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Bus185", type=eaglemodel_Segment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net186: BinaryAssociation = BinaryAssociation(
    name="net186",
    ends={
        Property(name="eaglemodel_Net", type=eaglemodel_Nets, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Nets187", type=eaglemodel_Net, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute179: BinaryAssociation = BinaryAssociation(
    name="attribute179",
    ends={
        Property(name="eaglemodel_Attribute181", type=eaglemodel_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Instance180", type=eaglemodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bus182: BinaryAssociation = BinaryAssociation(
    name="bus182",
    ends={
        Property(name="eaglemodel_Bus", type=eaglemodel_Busses, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Busses183", type=eaglemodel_Bus, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
segment188: BinaryAssociation = BinaryAssociation(
    name="segment188",
    ends={
        Property(name="eaglemodel_Segment190", type=eaglemodel_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Net189", type=eaglemodel_Segment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pinref191: BinaryAssociation = BinaryAssociation(
    name="pinref191",
    ends={
        Property(name="eaglemodel_Pinref", type=eaglemodel_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Segment192", type=eaglemodel_Pinref, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wire193: BinaryAssociation = BinaryAssociation(
    name="wire193",
    ends={
        Property(name="eaglemodel_Wire195", type=eaglemodel_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Segment194", type=eaglemodel_Wire, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
junction196: BinaryAssociation = BinaryAssociation(
    name="junction196",
    ends={
        Property(name="eaglemodel_Junction", type=eaglemodel_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Segment197", type=eaglemodel_Junction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label198: BinaryAssociation = BinaryAssociation(
    name="label198",
    ends={
        Property(name="eaglemodel_Label", type=eaglemodel_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="eaglemodel_Segment199", type=eaglemodel_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="eaglemodel",
    types={eaglemodel_Eagle, eaglemodel_Compatibility, eaglemodel_Drawing, eaglemodel_Note, eaglemodel_Settings, eaglemodel_Grid, eaglemodel_Layers, eaglemodel_Schematic, eaglemodel_Setting, eaglemodel_Libraries, eaglemodel_Attributes, eaglemodel_Variantdefs, eaglemodel_Layer, eaglemodel_Description, eaglemodel_Packages, eaglemodel_Symbols, eaglemodel_Classes, eaglemodel_Devicesets, eaglemodel_Parts, eaglemodel_Sheets, eaglemodel_Errors, eaglemodel_Library, eaglemodel_Variantdef, eaglemodel_Attribute, eaglemodel_Part, eaglemodel_Variant, eaglemodel_Class, eaglemodel_Clearance, eaglemodel_Plain, eaglemodel_Instances, eaglemodel_Busses, eaglemodel_Sheet, eaglemodel_Text, eaglemodel_Dimension, eaglemodel_Circle, eaglemodel_Rectangle, eaglemodel_Nets, eaglemodel_Approved, eaglemodel_Package, eaglemodel_Polygon, eaglemodel_Wire, eaglemodel_Frame, eaglemodel_Hole, eaglemodel_Pad, eaglemodel_SMD, eaglemodel_Symbol, eaglemodel_Gates, eaglemodel_Devices, eaglemodel_Pin, eaglemodel_Deviceset, eaglemodel_Vertex, eaglemodel_Gate, eaglemodel_Technology, eaglemodel_Device, eaglemodel_Connects, eaglemodel_Technologies, eaglemodel_Connect, eaglemodel_Instance, eaglemodel_Segment, eaglemodel_Net, eaglemodel_Bus, eaglemodel_Pinref, eaglemodel_Junction, eaglemodel_Label, WireCap, DimensionType, Severity, GateAddLevel, WireStyle, PadShape, PolygonPour, GridUnit, GridStyle, TextFont, Align, AttributeDisplay, VerticalText, PinVisible, PinLength, PinDirection, PinFunction, ContactRoute},
    associations={compatibility0, drawing1, note3, settings5, grid7, layers9, schematic11, settings13, libraries19, attributes21, variantdefs23, layers15, description17, description35, packages38, symbols40, classes25, devicesets42, parts27, sheets29, errors31, library33, variantdef46, attribute44, part52, class48, clearance50, description61, plain64, instances66, busses68, attribute54, variant57, sheet59, wire81, text83, dimension85, circle87, nets70, error72, package74, description76, polygon79, description101, polygon104, wire107, text110, rectangle89, frame91, hole93, pad95, smd97, symbol99, description129, gates132, devices134, dimension113, pin116, circle118, rectangle121, frame124, deviceset127, vertex136, gate138, technology148, device140, connects142, technologies144, connect146, frame171, hole174, instance177, attribute150, polygon153, wire156, text159, dimension162, circle165, rectangle168, segment184, net186, attribute179, bus182, segment188, pinref191, wire193, junction196, label198},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)