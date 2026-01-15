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

Orientation: Enumeration = Enumeration(
    name="Orientation",
    literals={
            EnumerationLiteral(name="NORTH"),
			EnumerationLiteral(name="SOUTH"),
			EnumerationLiteral(name="EAST"),
			EnumerationLiteral(name="WEST")
    }
)

SystemCursorType: Enumeration = Enumeration(
    name="SystemCursorType",
    literals={
            EnumerationLiteral(name="ARROW"),
			EnumerationLiteral(name="HAND")
    }
)

GridAlignment: Enumeration = Enumeration(
    name="GridAlignment",
    literals={
            EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="FILL"),
			EnumerationLiteral(name="BEGINNING"),
			EnumerationLiteral(name="END")
    }
)

# Classes
model_Primitive = Class(name="model::Primitive", is_abstract=True)
model_StringToStringMap = Class(name="model::StringToStringMap")
model_Cursor = Class(name="model::Cursor", is_abstract=True)
model_Dimension = Class(name="model::Dimension")
model_Connection = Class(name="model::Connection")
model_Container = Class(name="model::Container", is_abstract=True)
Primitive = Class(name="Primitive")
model_Shape = Class(name="model::Shape", is_abstract=True)
Figure = Class(name="Figure")
model_Symbol = Class(name="model::Symbol")
model_Child = Class(name="model::Child")
model_XYChild = Class(name="model::XYChild")
Child = Class(name="Child")
model_Position = Class(name="model::Position")
model_XYContainer = Class(name="model::XYContainer")
Container = Class(name="Container")
model_Line = Class(name="model::Line")
model_Figure = Class(name="model::Figure", is_abstract=True)
model_Rectangle = Class(name="model::Rectangle")
Shape = Class(name="Shape")
model_Text = Class(name="model::Text")
model_SymbolReference = Class(name="model::SymbolReference")
model_SystemCursor = Class(name="model::SystemCursor")
Cursor = Class(name="Cursor")
model_GridContainer = Class(name="model::GridContainer")
model_FigureContainer = Class(name="model::FigureContainer")
model_Image = Class(name="model::Image")
model_Ellipse = Class(name="model::Ellipse")
model_Arc = Class(name="model::Arc")
model_GridChild = Class(name="model::GridChild")
model_BorderContainer = Class(name="model::BorderContainer")
model_BorderChild = Class(name="model::BorderChild")
model_RoundedRectangle = Class(name="model::RoundedRectangle")
model_StackContainer = Class(name="model::StackContainer")
model_Polygon = Class(name="model::Polygon")

# model_Primitive class attributes and methods
model_Primitive_name: Property = Property(name="name", type=StringType)
model_Primitive.attributes={model_Primitive_name}

# model_StringToStringMap class attributes and methods
model_StringToStringMap_key: Property = Property(name="key", type=StringType)
model_StringToStringMap_value: Property = Property(name="value", type=StringType)
model_StringToStringMap.attributes={model_StringToStringMap_key, model_StringToStringMap_value}

# model_Cursor class attributes and methods

# model_Dimension class attributes and methods
model_Dimension_width: Property = Property(name="width", type=FloatType)
model_Dimension_height: Property = Property(name="height", type=FloatType)
model_Dimension.attributes={model_Dimension_height, model_Dimension_width}

# model_Connection class attributes and methods

# model_Container class attributes and methods

# Primitive class attributes and methods

# model_Shape class attributes and methods
model_Shape_lineWidth: Property = Property(name="lineWidth", type=FloatType)
model_Shape_antialias: Property = Property(name="antialias", type=StringType)
model_Shape_alpha: Property = Property(name="alpha", type=StringType)
model_Shape_fill: Property = Property(name="fill", type=BooleanType)
model_Shape_outline: Property = Property(name="outline", type=BooleanType)
model_Shape.attributes={model_Shape_antialias, model_Shape_alpha, model_Shape_outline, model_Shape_lineWidth, model_Shape_fill}

# Figure class attributes and methods

# model_Symbol class attributes and methods
model_Symbol_onInit: Property = Property(name="onInit", type=StringType)
model_Symbol_onDispose: Property = Property(name="onDispose", type=StringType)
model_Symbol_onUpdate: Property = Property(name="onUpdate", type=StringType)
model_Symbol_scriptModules: Property = Property(name="scriptModules", type=StringType)
model_Symbol_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
model_Symbol_backgroundImage: Property = Property(name="backgroundImage", type=StringType)
model_Symbol.attributes={model_Symbol_scriptModules, model_Symbol_onDispose, model_Symbol_backgroundImage, model_Symbol_backgroundColor, model_Symbol_onInit, model_Symbol_onUpdate}

# model_Child class attributes and methods
model_Child_name: Property = Property(name="name", type=StringType)
model_Child.attributes={model_Child_name}

# model_XYChild class attributes and methods

# Child class attributes and methods

# model_Position class attributes and methods
model_Position_x: Property = Property(name="x", type=FloatType)
model_Position_y: Property = Property(name="y", type=FloatType)
model_Position.attributes={model_Position_y, model_Position_x}

# model_XYContainer class attributes and methods

# Container class attributes and methods

# model_Line class attributes and methods

# model_Figure class attributes and methods
model_Figure_foregroundColor: Property = Property(name="foregroundColor", type=StringType)
model_Figure_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
model_Figure_onMouseHover: Property = Property(name="onMouseHover", type=StringType)
model_Figure_onMouseDrag: Property = Property(name="onMouseDrag", type=StringType)
model_Figure_onClick: Property = Property(name="onClick", type=StringType)
model_Figure_onDoubleClick: Property = Property(name="onDoubleClick", type=StringType)
model_Figure_visible: Property = Property(name="visible", type=BooleanType)
model_Figure_border: Property = Property(name="border", type=StringType)
model_Figure_opaque: Property = Property(name="opaque", type=StringType)
model_Figure_toolTip: Property = Property(name="toolTip", type=StringType)
model_Figure_onMouseIn: Property = Property(name="onMouseIn", type=StringType)
model_Figure_onMouseOut: Property = Property(name="onMouseOut", type=StringType)
model_Figure_onMouseMove: Property = Property(name="onMouseMove", type=StringType)
model_Figure.attributes={model_Figure_onDoubleClick, model_Figure_onMouseIn, model_Figure_onMouseDrag, model_Figure_opaque, model_Figure_visible, model_Figure_border, model_Figure_onClick, model_Figure_onMouseMove, model_Figure_backgroundColor, model_Figure_onMouseHover, model_Figure_onMouseOut, model_Figure_toolTip, model_Figure_foregroundColor}

# model_Rectangle class attributes and methods

# Shape class attributes and methods

# model_Text class attributes and methods
model_Text_fontBold: Property = Property(name="fontBold", type=BooleanType)
model_Text_fontItalic: Property = Property(name="fontItalic", type=BooleanType)
model_Text_alpha: Property = Property(name="alpha", type=StringType)
model_Text_text: Property = Property(name="text", type=StringType)
model_Text_labelAlignment: Property = Property(name="labelAlignment", type=StringType)
model_Text_iconAlignment: Property = Property(name="iconAlignment", type=StringType)
model_Text_textAlignment: Property = Property(name="textAlignment", type=StringType)
model_Text_textPlacement: Property = Property(name="textPlacement", type=StringType)
model_Text_fontName: Property = Property(name="fontName", type=StringType)
model_Text_fontSize: Property = Property(name="fontSize", type=IntegerType)
model_Text.attributes={model_Text_text, model_Text_fontItalic, model_Text_labelAlignment, model_Text_alpha, model_Text_textPlacement, model_Text_fontName, model_Text_fontBold, model_Text_textAlignment, model_Text_iconAlignment, model_Text_fontSize}

# model_SymbolReference class attributes and methods
model_SymbolReference_uri: Property = Property(name="uri", type=StringType)
model_SymbolReference_zoom: Property = Property(name="zoom", type=StringType)
model_SymbolReference_onCreateProperties: Property = Property(name="onCreateProperties", type=StringType)
model_SymbolReference.attributes={model_SymbolReference_uri, model_SymbolReference_zoom, model_SymbolReference_onCreateProperties}

# model_SystemCursor class attributes and methods
model_SystemCursor_type: Property = Property(name="type", type=StringType)
model_SystemCursor.attributes={model_SystemCursor_type}

# Cursor class attributes and methods

# model_GridContainer class attributes and methods
model_GridContainer_columns: Property = Property(name="columns", type=IntegerType)
model_GridContainer_equalWidth: Property = Property(name="equalWidth", type=BooleanType)
model_GridContainer_horizontalSpacing: Property = Property(name="horizontalSpacing", type=IntegerType)
model_GridContainer_verticalSpacing: Property = Property(name="verticalSpacing", type=IntegerType)
model_GridContainer_marginWidth: Property = Property(name="marginWidth", type=IntegerType)
model_GridContainer_marginHeight: Property = Property(name="marginHeight", type=IntegerType)
model_GridContainer.attributes={model_GridContainer_equalWidth, model_GridContainer_marginWidth, model_GridContainer_horizontalSpacing, model_GridContainer_marginHeight, model_GridContainer_verticalSpacing, model_GridContainer_columns}

# model_FigureContainer class attributes and methods

# model_Image class attributes and methods
model_Image_uri: Property = Property(name="uri", type=StringType)
model_Image_imageAlignment: Property = Property(name="imageAlignment", type=StringType)
model_Image.attributes={model_Image_imageAlignment, model_Image_uri}

# model_Ellipse class attributes and methods

# model_Arc class attributes and methods
model_Arc_start: Property = Property(name="start", type=IntegerType)
model_Arc_length: Property = Property(name="length", type=IntegerType)
model_Arc.attributes={model_Arc_length, model_Arc_start}

# model_GridChild class attributes and methods
model_GridChild_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
model_GridChild_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
model_GridChild_grabHorizontalSpace: Property = Property(name="grabHorizontalSpace", type=BooleanType)
model_GridChild_grabVerticalSpace: Property = Property(name="grabVerticalSpace", type=BooleanType)
model_GridChild_spanCols: Property = Property(name="spanCols", type=IntegerType)
model_GridChild_spanRows: Property = Property(name="spanRows", type=StringType)
model_GridChild_widthHint: Property = Property(name="widthHint", type=StringType)
model_GridChild_heightHint: Property = Property(name="heightHint", type=StringType)
model_GridChild.attributes={model_GridChild_grabVerticalSpace, model_GridChild_widthHint, model_GridChild_horizontalAlignment, model_GridChild_verticalAlignment, model_GridChild_grabHorizontalSpace, model_GridChild_spanCols, model_GridChild_heightHint, model_GridChild_spanRows}

# model_BorderContainer class attributes and methods
model_BorderContainer_verticalSpacing: Property = Property(name="verticalSpacing", type=IntegerType)
model_BorderContainer_horizontalSpacing: Property = Property(name="horizontalSpacing", type=IntegerType)
model_BorderContainer.attributes={model_BorderContainer_verticalSpacing, model_BorderContainer_horizontalSpacing}

# model_BorderChild class attributes and methods
model_BorderChild_alignment: Property = Property(name="alignment", type=StringType)
model_BorderChild.attributes={model_BorderChild_alignment}

# model_RoundedRectangle class attributes and methods

# model_StackContainer class attributes and methods

# model_Polygon class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="model_Primitive", type=model_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Symbol", type=model_Primitive, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties1: BinaryAssociation = BinaryAssociation(
    name="properties1",
    ends={
        Property(name="model_StringToStringMap", type=model_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Symbol2", type=model_StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cursors3: BinaryAssociation = BinaryAssociation(
    name="cursors3",
    ends={
        Property(name="model_Cursor", type=model_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Symbol4", type=model_Cursor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
designSize5: BinaryAssociation = BinaryAssociation(
    name="designSize5",
    ends={
        Property(name="model_Dimension", type=model_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Symbol6", type=model_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connections7: BinaryAssociation = BinaryAssociation(
    name="connections7",
    ends={
        Property(name="model_Connection", type=model_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Symbol8", type=model_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element9: BinaryAssociation = BinaryAssociation(
    name="element9",
    ends={
        Property(name="model_Primitive10", type=model_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Child", type=model_Primitive, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
position11: BinaryAssociation = BinaryAssociation(
    name="position11",
    ends={
        Property(name="model_Position", type=model_XYChild, multiplicity=Multiplicity(1, 1)),
        Property(name="model_XYChild", type=model_Position, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimension12: BinaryAssociation = BinaryAssociation(
    name="dimension12",
    ends={
        Property(name="model_Dimension14", type=model_XYChild, multiplicity=Multiplicity(1, 1)),
        Property(name="model_XYChild13", type=model_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children15: BinaryAssociation = BinaryAssociation(
    name="children15",
    ends={
        Property(name="model_XYChild16", type=model_XYContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_XYContainer", type=model_XYChild, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
points17: BinaryAssociation = BinaryAssociation(
    name="points17",
    ends={
        Property(name="model_Position18", type=model_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Line", type=model_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties24: BinaryAssociation = BinaryAssociation(
    name="properties24",
    ends={
        Property(name="model_StringToStringMap25", type=model_SymbolReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_SymbolReference", type=model_StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
size19: BinaryAssociation = BinaryAssociation(
    name="size19",
    ends={
        Property(name="model_Dimension20", type=model_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Figure", type=model_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cursor21: BinaryAssociation = BinaryAssociation(
    name="cursor21",
    ends={
        Property(name="model_Cursor23", type=model_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Figure22", type=model_Cursor, multiplicity=Multiplicity(0, 1))
    }
)
content28: BinaryAssociation = BinaryAssociation(
    name="content28",
    ends={
        Property(name="model_Primitive29", type=model_FigureContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FigureContainer", type=model_Primitive, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children26: BinaryAssociation = BinaryAssociation(
    name="children26",
    ends={
        Property(name="model_GridChild", type=model_GridContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_GridContainer", type=model_GridChild, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children27: BinaryAssociation = BinaryAssociation(
    name="children27",
    ends={
        Property(name="model_BorderChild", type=model_BorderContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BorderContainer", type=model_BorderChild, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
corner40: BinaryAssociation = BinaryAssociation(
    name="corner40",
    ends={
        Property(name="model_Dimension41", type=model_RoundedRectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RoundedRectangle", type=model_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start30: BinaryAssociation = BinaryAssociation(
    name="start30",
    ends={
        Property(name="model_Primitive32", type=model_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Connection31", type=model_Primitive, multiplicity=Multiplicity(1, 1))
    }
)
end33: BinaryAssociation = BinaryAssociation(
    name="end33",
    ends={
        Property(name="model_Primitive35", type=model_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Connection34", type=model_Primitive, multiplicity=Multiplicity(1, 1))
    }
)
children36: BinaryAssociation = BinaryAssociation(
    name="children36",
    ends={
        Property(name="model_Primitive37", type=model_StackContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_StackContainer", type=model_Primitive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
points38: BinaryAssociation = BinaryAssociation(
    name="points38",
    ends={
        Property(name="model_Position39", type=model_Polygon, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Polygon", type=model_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_model_Container_Primitive = Generalization(general=Primitive, specific=model_Container)
gen_model_Shape_Figure = Generalization(general=Figure, specific=model_Shape)
gen_model_XYChild_Child = Generalization(general=Child, specific=model_XYChild)
gen_model_XYContainer_Container = Generalization(general=Container, specific=model_XYContainer)
gen_model_Line_Shape = Generalization(general=Shape, specific=model_Line)
gen_model_Figure_Primitive = Generalization(general=Primitive, specific=model_Figure)
gen_model_Rectangle_Shape = Generalization(general=Shape, specific=model_Rectangle)
gen_model_Text_Figure = Generalization(general=Figure, specific=model_Text)
gen_model_SymbolReference_Primitive = Generalization(general=Primitive, specific=model_SymbolReference)
gen_model_SystemCursor_Cursor = Generalization(general=Cursor, specific=model_SystemCursor)
gen_model_GridContainer_Container = Generalization(general=Container, specific=model_GridContainer)
gen_model_BorderChild_Child = Generalization(general=Child, specific=model_BorderChild)
gen_model_GridChild_Child = Generalization(general=Child, specific=model_GridChild)
gen_model_FigureContainer_Figure = Generalization(general=Figure, specific=model_FigureContainer)
gen_model_Image_Figure = Generalization(general=Figure, specific=model_Image)
gen_model_Ellipse_Shape = Generalization(general=Shape, specific=model_Ellipse)
gen_model_Arc_Shape = Generalization(general=Shape, specific=model_Arc)
gen_model_BorderContainer_Container = Generalization(general=Container, specific=model_BorderContainer)
gen_model_RoundedRectangle_Shape = Generalization(general=Shape, specific=model_RoundedRectangle)
gen_model_StackContainer_Container = Generalization(general=Container, specific=model_StackContainer)
gen_model_Polygon_Shape = Generalization(general=Shape, specific=model_Polygon)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Primitive, model_StringToStringMap, model_Cursor, model_Dimension, model_Connection, model_Container, Primitive, model_Shape, Figure, model_Symbol, model_Child, model_XYChild, Child, model_Position, model_XYContainer, Container, model_Line, model_Figure, model_Rectangle, Shape, model_Text, model_SymbolReference, model_SystemCursor, Cursor, model_GridContainer, model_FigureContainer, model_Image, model_Ellipse, model_Arc, model_GridChild, model_BorderContainer, model_BorderChild, model_RoundedRectangle, model_StackContainer, model_Polygon, Alignment, Orientation, SystemCursorType, GridAlignment},
    associations={root0, properties1, cursors3, designSize5, connections7, element9, position11, dimension12, children15, points17, properties24, size19, cursor21, content28, children26, children27, corner40, start30, end33, children36, points38},
    generalizations={gen_model_Container_Primitive, gen_model_Shape_Figure, gen_model_XYChild_Child, gen_model_XYContainer_Container, gen_model_Line_Shape, gen_model_Figure_Primitive, gen_model_Rectangle_Shape, gen_model_Text_Figure, gen_model_SymbolReference_Primitive, gen_model_SystemCursor_Cursor, gen_model_GridContainer_Container, gen_model_BorderChild_Child, gen_model_GridChild_Child, gen_model_FigureContainer_Figure, gen_model_Image_Figure, gen_model_Ellipse_Shape, gen_model_Arc_Shape, gen_model_BorderContainer_Container, gen_model_RoundedRectangle_Shape, gen_model_StackContainer_Container, gen_model_Polygon_Shape},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)