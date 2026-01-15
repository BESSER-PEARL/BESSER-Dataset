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
SystemCursorType: Enumeration = Enumeration(
    name="SystemCursorType",
    literals={
            EnumerationLiteral(name="ARROW"),
			EnumerationLiteral(name="HAND")
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

Orientation: Enumeration = Enumeration(
    name="Orientation",
    literals={
            EnumerationLiteral(name="NORTH"),
			EnumerationLiteral(name="SOUTH"),
			EnumerationLiteral(name="EAST"),
			EnumerationLiteral(name="WEST")
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
VisualInterface_Cursor = Class(name="VisualInterface::Cursor", is_abstract=True)
VisualInterface_Symbol = Class(name="VisualInterface::Symbol")
VisualInterface_Primitive = Class(name="VisualInterface::Primitive", is_abstract=True)
VisualInterface_StringToStringMap = Class(name="VisualInterface::StringToStringMap")
VisualInterface_XYContainer = Class(name="VisualInterface::XYContainer")
Container = Class(name="Container")
VisualInterface_Dimension = Class(name="VisualInterface::Dimension")
VisualInterface_Connection = Class(name="VisualInterface::Connection")
VisualInterface_Container = Class(name="VisualInterface::Container", is_abstract=True)
Primitive = Class(name="Primitive")
VisualInterface_Shape = Class(name="VisualInterface::Shape", is_abstract=True)
Figure = Class(name="Figure")
VisualInterface_Rectangle = Class(name="VisualInterface::Rectangle")
Shape = Class(name="Shape")
VisualInterface_Text = Class(name="VisualInterface::Text")
VisualInterface_Child = Class(name="VisualInterface::Child")
VisualInterface_XYChild = Class(name="VisualInterface::XYChild")
Child = Class(name="Child")
VisualInterface_Position = Class(name="VisualInterface::Position")
VisualInterface_GridContainer = Class(name="VisualInterface::GridContainer")
VisualInterface_GridChild = Class(name="VisualInterface::GridChild")
VisualInterface_Line = Class(name="VisualInterface::Line")
VisualInterface_Figure = Class(name="VisualInterface::Figure", is_abstract=True)
VisualInterface_SymbolReference = Class(name="VisualInterface::SymbolReference")
VisualInterface_SystemCursor = Class(name="VisualInterface::SystemCursor")
Cursor = Class(name="Cursor")
VisualInterface_StackContainer = Class(name="VisualInterface::StackContainer")
VisualInterface_BorderContainer = Class(name="VisualInterface::BorderContainer")
VisualInterface_BorderChild = Class(name="VisualInterface::BorderChild")
VisualInterface_FigureContainer = Class(name="VisualInterface::FigureContainer")
VisualInterface_Image = Class(name="VisualInterface::Image")
VisualInterface_Ellipse = Class(name="VisualInterface::Ellipse")
VisualInterface_Arc = Class(name="VisualInterface::Arc")

# VisualInterface_Cursor class attributes and methods

# VisualInterface_Symbol class attributes and methods
VisualInterface_Symbol_onInit: Property = Property(name="onInit", type=StringType)
VisualInterface_Symbol_onDispose: Property = Property(name="onDispose", type=StringType)
VisualInterface_Symbol_onUpdate: Property = Property(name="onUpdate", type=StringType)
VisualInterface_Symbol_scriptModules: Property = Property(name="scriptModules", type=StringType)
VisualInterface_Symbol_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
VisualInterface_Symbol.attributes={VisualInterface_Symbol_onUpdate, VisualInterface_Symbol_onInit, VisualInterface_Symbol_onDispose, VisualInterface_Symbol_scriptModules, VisualInterface_Symbol_backgroundColor}

# VisualInterface_Primitive class attributes and methods
VisualInterface_Primitive_name: Property = Property(name="name", type=StringType)
VisualInterface_Primitive.attributes={VisualInterface_Primitive_name}

# VisualInterface_StringToStringMap class attributes and methods
VisualInterface_StringToStringMap_key: Property = Property(name="key", type=StringType)
VisualInterface_StringToStringMap_value: Property = Property(name="value", type=StringType)
VisualInterface_StringToStringMap.attributes={VisualInterface_StringToStringMap_value, VisualInterface_StringToStringMap_key}

# VisualInterface_XYContainer class attributes and methods

# Container class attributes and methods

# VisualInterface_Dimension class attributes and methods
VisualInterface_Dimension_width: Property = Property(name="width", type=FloatType)
VisualInterface_Dimension_height: Property = Property(name="height", type=FloatType)
VisualInterface_Dimension.attributes={VisualInterface_Dimension_height, VisualInterface_Dimension_width}

# VisualInterface_Connection class attributes and methods

# VisualInterface_Container class attributes and methods

# Primitive class attributes and methods

# VisualInterface_Shape class attributes and methods
VisualInterface_Shape_lineWidth: Property = Property(name="lineWidth", type=FloatType)
VisualInterface_Shape_antialias: Property = Property(name="antialias", type=StringType)
VisualInterface_Shape_alpha: Property = Property(name="alpha", type=StringType)
VisualInterface_Shape_fill: Property = Property(name="fill", type=BooleanType)
VisualInterface_Shape_outline: Property = Property(name="outline", type=BooleanType)
VisualInterface_Shape.attributes={VisualInterface_Shape_fill, VisualInterface_Shape_antialias, VisualInterface_Shape_outline, VisualInterface_Shape_lineWidth, VisualInterface_Shape_alpha}

# Figure class attributes and methods

# VisualInterface_Rectangle class attributes and methods

# Shape class attributes and methods

# VisualInterface_Text class attributes and methods
VisualInterface_Text_text: Property = Property(name="text", type=StringType)
VisualInterface_Text_labelAlignment: Property = Property(name="labelAlignment", type=StringType)
VisualInterface_Text_iconAlignment: Property = Property(name="iconAlignment", type=StringType)
VisualInterface_Text_textAlignment: Property = Property(name="textAlignment", type=StringType)
VisualInterface_Text_textPlacement: Property = Property(name="textPlacement", type=StringType)
VisualInterface_Text_fontName: Property = Property(name="fontName", type=StringType)
VisualInterface_Text_fontSize: Property = Property(name="fontSize", type=IntegerType)
VisualInterface_Text_fontBold: Property = Property(name="fontBold", type=BooleanType)
VisualInterface_Text_fontItalic: Property = Property(name="fontItalic", type=BooleanType)
VisualInterface_Text.attributes={VisualInterface_Text_textPlacement, VisualInterface_Text_fontSize, VisualInterface_Text_fontBold, VisualInterface_Text_fontName, VisualInterface_Text_fontItalic, VisualInterface_Text_textAlignment, VisualInterface_Text_iconAlignment, VisualInterface_Text_text, VisualInterface_Text_labelAlignment}

# VisualInterface_Child class attributes and methods
VisualInterface_Child_name: Property = Property(name="name", type=StringType)
VisualInterface_Child.attributes={VisualInterface_Child_name}

# VisualInterface_XYChild class attributes and methods

# Child class attributes and methods

# VisualInterface_Position class attributes and methods
VisualInterface_Position_x: Property = Property(name="x", type=FloatType)
VisualInterface_Position_y: Property = Property(name="y", type=FloatType)
VisualInterface_Position.attributes={VisualInterface_Position_y, VisualInterface_Position_x}

# VisualInterface_GridContainer class attributes and methods
VisualInterface_GridContainer_columns: Property = Property(name="columns", type=IntegerType)
VisualInterface_GridContainer_equalWidth: Property = Property(name="equalWidth", type=BooleanType)
VisualInterface_GridContainer_horizontalSpacing: Property = Property(name="horizontalSpacing", type=IntegerType)
VisualInterface_GridContainer_verticalSpacing: Property = Property(name="verticalSpacing", type=IntegerType)
VisualInterface_GridContainer_marginWidth: Property = Property(name="marginWidth", type=IntegerType)
VisualInterface_GridContainer_marginHeight: Property = Property(name="marginHeight", type=IntegerType)
VisualInterface_GridContainer.attributes={VisualInterface_GridContainer_marginWidth, VisualInterface_GridContainer_verticalSpacing, VisualInterface_GridContainer_columns, VisualInterface_GridContainer_equalWidth, VisualInterface_GridContainer_marginHeight, VisualInterface_GridContainer_horizontalSpacing}

# VisualInterface_GridChild class attributes and methods
VisualInterface_GridChild_horizontalAlignment: Property = Property(name="horizontalAlignment", type=StringType)
VisualInterface_GridChild_verticalAlignment: Property = Property(name="verticalAlignment", type=StringType)
VisualInterface_GridChild_grabHorizontalSpace: Property = Property(name="grabHorizontalSpace", type=BooleanType)
VisualInterface_GridChild_grabVerticalSpace: Property = Property(name="grabVerticalSpace", type=BooleanType)
VisualInterface_GridChild_spanCols: Property = Property(name="spanCols", type=IntegerType)
VisualInterface_GridChild_spanRows: Property = Property(name="spanRows", type=StringType)
VisualInterface_GridChild_widthHint: Property = Property(name="widthHint", type=StringType)
VisualInterface_GridChild_heightHint: Property = Property(name="heightHint", type=StringType)
VisualInterface_GridChild.attributes={VisualInterface_GridChild_grabHorizontalSpace, VisualInterface_GridChild_heightHint, VisualInterface_GridChild_spanRows, VisualInterface_GridChild_horizontalAlignment, VisualInterface_GridChild_widthHint, VisualInterface_GridChild_spanCols, VisualInterface_GridChild_grabVerticalSpace, VisualInterface_GridChild_verticalAlignment}

# VisualInterface_Line class attributes and methods

# VisualInterface_Figure class attributes and methods
VisualInterface_Figure_foregroundColor: Property = Property(name="foregroundColor", type=StringType)
VisualInterface_Figure_backgroundColor: Property = Property(name="backgroundColor", type=StringType)
VisualInterface_Figure_onClick: Property = Property(name="onClick", type=StringType)
VisualInterface_Figure_onDoubleClick: Property = Property(name="onDoubleClick", type=StringType)
VisualInterface_Figure_visible: Property = Property(name="visible", type=BooleanType)
VisualInterface_Figure_border: Property = Property(name="border", type=StringType)
VisualInterface_Figure_opaque: Property = Property(name="opaque", type=StringType)
VisualInterface_Figure_toolTip: Property = Property(name="toolTip", type=StringType)
VisualInterface_Figure.attributes={VisualInterface_Figure_onClick, VisualInterface_Figure_onDoubleClick, VisualInterface_Figure_visible, VisualInterface_Figure_backgroundColor, VisualInterface_Figure_foregroundColor, VisualInterface_Figure_border, VisualInterface_Figure_opaque, VisualInterface_Figure_toolTip}

# VisualInterface_SymbolReference class attributes and methods
VisualInterface_SymbolReference_uri: Property = Property(name="uri", type=StringType)
VisualInterface_SymbolReference_zoom: Property = Property(name="zoom", type=StringType)
VisualInterface_SymbolReference_onCreateProperties: Property = Property(name="onCreateProperties", type=StringType)
VisualInterface_SymbolReference.attributes={VisualInterface_SymbolReference_onCreateProperties, VisualInterface_SymbolReference_zoom, VisualInterface_SymbolReference_uri}

# VisualInterface_SystemCursor class attributes and methods
VisualInterface_SystemCursor_type: Property = Property(name="type", type=StringType)
VisualInterface_SystemCursor.attributes={VisualInterface_SystemCursor_type}

# Cursor class attributes and methods

# VisualInterface_StackContainer class attributes and methods

# VisualInterface_BorderContainer class attributes and methods
VisualInterface_BorderContainer_verticalSpacing: Property = Property(name="verticalSpacing", type=IntegerType)
VisualInterface_BorderContainer_horizontalSpacing: Property = Property(name="horizontalSpacing", type=IntegerType)
VisualInterface_BorderContainer.attributes={VisualInterface_BorderContainer_verticalSpacing, VisualInterface_BorderContainer_horizontalSpacing}

# VisualInterface_BorderChild class attributes and methods
VisualInterface_BorderChild_alignment: Property = Property(name="alignment", type=StringType)
VisualInterface_BorderChild.attributes={VisualInterface_BorderChild_alignment}

# VisualInterface_FigureContainer class attributes and methods

# VisualInterface_Image class attributes and methods
VisualInterface_Image_uri: Property = Property(name="uri", type=StringType)
VisualInterface_Image.attributes={VisualInterface_Image_uri}

# VisualInterface_Ellipse class attributes and methods

# VisualInterface_Arc class attributes and methods
VisualInterface_Arc_start: Property = Property(name="start", type=IntegerType)
VisualInterface_Arc_length: Property = Property(name="length", type=IntegerType)
VisualInterface_Arc.attributes={VisualInterface_Arc_length, VisualInterface_Arc_start}

# Relationships
properties1: BinaryAssociation = BinaryAssociation(
    name="properties1",
    ends={
        Property(name="VisualInterface_Symbol2", type=VisualInterface_StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="VisualInterface_StringToStringMap", type=VisualInterface_Symbol, multiplicity=Multiplicity(1, 1))
    }
)
cursors3: BinaryAssociation = BinaryAssociation(
    name="cursors3",
    ends={
        Property(name="VisualInterface_Cursor", type=VisualInterface_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_Symbol4", type=VisualInterface_Cursor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="VisualInterface_Primitive", type=VisualInterface_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_Symbol", type=VisualInterface_Primitive, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimension12: BinaryAssociation = BinaryAssociation(
    name="dimension12",
    ends={
        Property(name="VisualInterface_Dimension14", type=VisualInterface_XYChild, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_XYChild13", type=VisualInterface_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children15: BinaryAssociation = BinaryAssociation(
    name="children15",
    ends={
        Property(name="VisualInterface_XYChild16", type=VisualInterface_XYContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_XYContainer", type=VisualInterface_XYChild, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
designSize5: BinaryAssociation = BinaryAssociation(
    name="designSize5",
    ends={
        Property(name="VisualInterface_Dimension", type=VisualInterface_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_Symbol6", type=VisualInterface_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connections7: BinaryAssociation = BinaryAssociation(
    name="connections7",
    ends={
        Property(name="VisualInterface_Connection", type=VisualInterface_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_Symbol8", type=VisualInterface_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element9: BinaryAssociation = BinaryAssociation(
    name="element9",
    ends={
        Property(name="VisualInterface_Primitive10", type=VisualInterface_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_Child", type=VisualInterface_Primitive, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
position11: BinaryAssociation = BinaryAssociation(
    name="position11",
    ends={
        Property(name="VisualInterface_Position", type=VisualInterface_XYChild, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_XYChild", type=VisualInterface_Position, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children26: BinaryAssociation = BinaryAssociation(
    name="children26",
    ends={
        Property(name="VisualInterface_GridChild", type=VisualInterface_GridContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_GridContainer", type=VisualInterface_GridChild, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
points17: BinaryAssociation = BinaryAssociation(
    name="points17",
    ends={
        Property(name="VisualInterface_Position18", type=VisualInterface_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_Line", type=VisualInterface_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
size19: BinaryAssociation = BinaryAssociation(
    name="size19",
    ends={
        Property(name="VisualInterface_Dimension20", type=VisualInterface_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_Figure", type=VisualInterface_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cursor21: BinaryAssociation = BinaryAssociation(
    name="cursor21",
    ends={
        Property(name="VisualInterface_Cursor23", type=VisualInterface_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_Figure22", type=VisualInterface_Cursor, multiplicity=Multiplicity(0, 1))
    }
)
properties24: BinaryAssociation = BinaryAssociation(
    name="properties24",
    ends={
        Property(name="VisualInterface_StringToStringMap25", type=VisualInterface_SymbolReference, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_SymbolReference", type=VisualInterface_StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start30: BinaryAssociation = BinaryAssociation(
    name="start30",
    ends={
        Property(name="VisualInterface_Primitive32", type=VisualInterface_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_Connection31", type=VisualInterface_Primitive, multiplicity=Multiplicity(1, 1))
    }
)
end33: BinaryAssociation = BinaryAssociation(
    name="end33",
    ends={
        Property(name="VisualInterface_Primitive35", type=VisualInterface_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_Connection34", type=VisualInterface_Primitive, multiplicity=Multiplicity(1, 1))
    }
)
children36: BinaryAssociation = BinaryAssociation(
    name="children36",
    ends={
        Property(name="VisualInterface_Primitive37", type=VisualInterface_StackContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_StackContainer", type=VisualInterface_Primitive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children27: BinaryAssociation = BinaryAssociation(
    name="children27",
    ends={
        Property(name="VisualInterface_BorderChild", type=VisualInterface_BorderContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_BorderContainer", type=VisualInterface_BorderChild, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content28: BinaryAssociation = BinaryAssociation(
    name="content28",
    ends={
        Property(name="VisualInterface_Primitive29", type=VisualInterface_FigureContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="VisualInterface_FigureContainer", type=VisualInterface_Primitive, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_VisualInterface_XYContainer_Container = Generalization(general=Container, specific=VisualInterface_XYContainer)
gen_VisualInterface_Container_Primitive = Generalization(general=Primitive, specific=VisualInterface_Container)
gen_VisualInterface_Shape_Figure = Generalization(general=Figure, specific=VisualInterface_Shape)
gen_VisualInterface_Rectangle_Shape = Generalization(general=Shape, specific=VisualInterface_Rectangle)
gen_VisualInterface_Text_Figure = Generalization(general=Figure, specific=VisualInterface_Text)
gen_VisualInterface_XYChild_Child = Generalization(general=Child, specific=VisualInterface_XYChild)
gen_VisualInterface_GridContainer_Container = Generalization(general=Container, specific=VisualInterface_GridContainer)
gen_VisualInterface_Line_Shape = Generalization(general=Shape, specific=VisualInterface_Line)
gen_VisualInterface_Figure_Primitive = Generalization(general=Primitive, specific=VisualInterface_Figure)
gen_VisualInterface_SymbolReference_Primitive = Generalization(general=Primitive, specific=VisualInterface_SymbolReference)
gen_VisualInterface_SystemCursor_Cursor = Generalization(general=Cursor, specific=VisualInterface_SystemCursor)
gen_VisualInterface_StackContainer_Container = Generalization(general=Container, specific=VisualInterface_StackContainer)
gen_VisualInterface_BorderContainer_Container = Generalization(general=Container, specific=VisualInterface_BorderContainer)
gen_VisualInterface_BorderChild_Child = Generalization(general=Child, specific=VisualInterface_BorderChild)
gen_VisualInterface_GridChild_Child = Generalization(general=Child, specific=VisualInterface_GridChild)
gen_VisualInterface_FigureContainer_Figure = Generalization(general=Figure, specific=VisualInterface_FigureContainer)
gen_VisualInterface_Image_Figure = Generalization(general=Figure, specific=VisualInterface_Image)
gen_VisualInterface_Ellipse_Shape = Generalization(general=Shape, specific=VisualInterface_Ellipse)
gen_VisualInterface_Arc_Shape = Generalization(general=Shape, specific=VisualInterface_Arc)

# Domain Model
domain_model = DomainModel(
    name="VisualInterface",
    types={VisualInterface_Cursor, VisualInterface_Symbol, VisualInterface_Primitive, VisualInterface_StringToStringMap, VisualInterface_XYContainer, Container, VisualInterface_Dimension, VisualInterface_Connection, VisualInterface_Container, Primitive, VisualInterface_Shape, Figure, VisualInterface_Rectangle, Shape, VisualInterface_Text, VisualInterface_Child, VisualInterface_XYChild, Child, VisualInterface_Position, VisualInterface_GridContainer, VisualInterface_GridChild, VisualInterface_Line, VisualInterface_Figure, VisualInterface_SymbolReference, VisualInterface_SystemCursor, Cursor, VisualInterface_StackContainer, VisualInterface_BorderContainer, VisualInterface_BorderChild, VisualInterface_FigureContainer, VisualInterface_Image, VisualInterface_Ellipse, VisualInterface_Arc, SystemCursorType, Alignment, Orientation, GridAlignment},
    associations={properties1, cursors3, root0, dimension12, children15, designSize5, connections7, element9, position11, children26, points17, size19, cursor21, properties24, start30, end33, children36, children27, content28},
    generalizations={gen_VisualInterface_XYContainer_Container, gen_VisualInterface_Container_Primitive, gen_VisualInterface_Shape_Figure, gen_VisualInterface_Rectangle_Shape, gen_VisualInterface_Text_Figure, gen_VisualInterface_XYChild_Child, gen_VisualInterface_GridContainer_Container, gen_VisualInterface_Line_Shape, gen_VisualInterface_Figure_Primitive, gen_VisualInterface_SymbolReference_Primitive, gen_VisualInterface_SystemCursor_Cursor, gen_VisualInterface_StackContainer_Container, gen_VisualInterface_BorderContainer_Container, gen_VisualInterface_BorderChild_Child, gen_VisualInterface_GridChild_Child, gen_VisualInterface_FigureContainer_Figure, gen_VisualInterface_Image_Figure, gen_VisualInterface_Ellipse_Shape, gen_VisualInterface_Arc_Shape},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)