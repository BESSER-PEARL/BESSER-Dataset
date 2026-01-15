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
            EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="TOP"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="BOTTOM"),
			EnumerationLiteral(name="MIDDLE"),
			EnumerationLiteral(name="UNSPECIFIED")
    }
)

# Classes
sofiagraphics_Style = Class(name="sofiagraphics::Style")
sofiagraphics_Rectangle = Class(name="sofiagraphics::Rectangle")
Widget = Class(name="Widget")
sofiagraphics_RoundedRectangle = Class(name="sofiagraphics::RoundedRectangle")
Rectangle = Class(name="Rectangle")
sofiagraphics_Ellipse = Class(name="sofiagraphics::Ellipse")
sofiagraphics_Polyline = Class(name="sofiagraphics::Polyline")
sofiagraphics_Point = Class(name="sofiagraphics::Point")
sofiagraphics_Dimension = Class(name="sofiagraphics::Dimension")
sofiagraphics_Widget = Class(name="sofiagraphics::Widget", is_abstract=True)
sofiagraphics_Text = Class(name="sofiagraphics::Text")
sofiagraphics_Scene = Class(name="sofiagraphics::Scene")
sofiagraphics_Color = Class(name="sofiagraphics::Color")
sofiagraphics_Gesture = Class(name="sofiagraphics::Gesture")

# sofiagraphics_Style class attributes and methods
sofiagraphics_Style_filled: Property = Property(name="filled", type=BooleanType)
sofiagraphics_Style_lineWidth: Property = Property(name="lineWidth", type=FloatType)
sofiagraphics_Style.attributes={sofiagraphics_Style_lineWidth, sofiagraphics_Style_filled}

# sofiagraphics_Rectangle class attributes and methods

# Widget class attributes and methods

# sofiagraphics_RoundedRectangle class attributes and methods

# Rectangle class attributes and methods

# sofiagraphics_Ellipse class attributes and methods

# sofiagraphics_Polyline class attributes and methods

# sofiagraphics_Point class attributes and methods
sofiagraphics_Point_x: Property = Property(name="x", type=FloatType)
sofiagraphics_Point_y: Property = Property(name="y", type=FloatType)
sofiagraphics_Point_xrelative: Property = Property(name="xrelative", type=BooleanType)
sofiagraphics_Point_yrelative: Property = Property(name="yrelative", type=BooleanType)
sofiagraphics_Point.attributes={sofiagraphics_Point_x, sofiagraphics_Point_xrelative, sofiagraphics_Point_yrelative, sofiagraphics_Point_y}

# sofiagraphics_Dimension class attributes and methods
sofiagraphics_Dimension_width: Property = Property(name="width", type=FloatType)
sofiagraphics_Dimension_height: Property = Property(name="height", type=FloatType)
sofiagraphics_Dimension_wrelative: Property = Property(name="wrelative", type=BooleanType)
sofiagraphics_Dimension_hrelative: Property = Property(name="hrelative", type=BooleanType)
sofiagraphics_Dimension_noresize: Property = Property(name="noresize", type=BooleanType)
sofiagraphics_Dimension.attributes={sofiagraphics_Dimension_width, sofiagraphics_Dimension_wrelative, sofiagraphics_Dimension_hrelative, sofiagraphics_Dimension_height, sofiagraphics_Dimension_noresize}

# sofiagraphics_Widget class attributes and methods
sofiagraphics_Widget_gestureOnly: Property = Property(name="gestureOnly", type=BooleanType)
sofiagraphics_Widget_portYPosition: Property = Property(name="portYPosition", type=FloatType)
sofiagraphics_Widget.attributes={sofiagraphics_Widget_portYPosition, sofiagraphics_Widget_gestureOnly}

# sofiagraphics_Text class attributes and methods
sofiagraphics_Text_text: Property = Property(name="text", type=StringType)
sofiagraphics_Text_halign: Property = Property(name="halign", type=StringType)
sofiagraphics_Text_valign: Property = Property(name="valign", type=StringType)
sofiagraphics_Text_attributeName: Property = Property(name="attributeName", type=StringType)
sofiagraphics_Text.attributes={sofiagraphics_Text_valign, sofiagraphics_Text_attributeName, sofiagraphics_Text_halign, sofiagraphics_Text_text}

# sofiagraphics_Scene class attributes and methods

# sofiagraphics_Color class attributes and methods
sofiagraphics_Color_r: Property = Property(name="r", type=FloatType)
sofiagraphics_Color_g: Property = Property(name="g", type=FloatType)
sofiagraphics_Color_b: Property = Property(name="b", type=FloatType)
sofiagraphics_Color_a: Property = Property(name="a", type=FloatType)
sofiagraphics_Color.attributes={sofiagraphics_Color_b, sofiagraphics_Color_r, sofiagraphics_Color_a, sofiagraphics_Color_g}

# sofiagraphics_Gesture class attributes and methods

# Relationships
style2: BinaryAssociation = BinaryAssociation(
    name="style2",
    ends={
        Property(name="sofiagraphics_Style", type=sofiagraphics_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Widget", type=sofiagraphics_Style, multiplicity=Multiplicity(0, 1))
    }
)
child4: BinaryAssociation = BinaryAssociation(
    name="child4",
    ends={
        Property(name="Widget5", type=sofiagraphics_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=sofiagraphics_Widget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pos6: BinaryAssociation = BinaryAssociation(
    name="pos6",
    ends={
        Property(name="sofiagraphics_Point", type=sofiagraphics_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Widget7", type=sofiagraphics_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dim8: BinaryAssociation = BinaryAssociation(
    name="dim8",
    ends={
        Property(name="sofiagraphics_Dimension", type=sofiagraphics_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Widget9", type=sofiagraphics_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
corner10: BinaryAssociation = BinaryAssociation(
    name="corner10",
    ends={
        Property(name="sofiagraphics_Dimension11", type=sofiagraphics_RoundedRectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_RoundedRectangle", type=sofiagraphics_Dimension, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
point12: BinaryAssociation = BinaryAssociation(
    name="point12",
    ends={
        Property(name="sofiagraphics_Point13", type=sofiagraphics_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Polyline", type=sofiagraphics_Point, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="Widget", type=sofiagraphics_Widget, multiplicity=Multiplicity(1, 1)),
        Property(name="child", type=sofiagraphics_Widget, multiplicity=Multiplicity(0, 1))
    }
)
fgcolor32: BinaryAssociation = BinaryAssociation(
    name="fgcolor32",
    ends={
        Property(name="sofiagraphics_Color34", type=sofiagraphics_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Style33", type=sofiagraphics_Color, multiplicity=Multiplicity(0, 1))
    }
)
bgcolor35: BinaryAssociation = BinaryAssociation(
    name="bgcolor35",
    ends={
        Property(name="sofiagraphics_Color37", type=sofiagraphics_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Style36", type=sofiagraphics_Color, multiplicity=Multiplicity(0, 1))
    }
)
widget38: BinaryAssociation = BinaryAssociation(
    name="widget38",
    ends={
        Property(name="sofiagraphics_Widget40", type=sofiagraphics_Gesture, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Gesture39", type=sofiagraphics_Widget, multiplicity=Multiplicity(0, 9999))
    }
)
object14: BinaryAssociation = BinaryAssociation(
    name="object14",
    ends={
        Property(name="sofiagraphics_Widget15", type=sofiagraphics_Scene, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Scene", type=sofiagraphics_Widget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root16: BinaryAssociation = BinaryAssociation(
    name="root16",
    ends={
        Property(name="sofiagraphics_Widget18", type=sofiagraphics_Scene, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Scene17", type=sofiagraphics_Widget, multiplicity=Multiplicity(0, 1))
    }
)
point19: BinaryAssociation = BinaryAssociation(
    name="point19",
    ends={
        Property(name="sofiagraphics_Point21", type=sofiagraphics_Scene, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Scene20", type=sofiagraphics_Point, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimension22: BinaryAssociation = BinaryAssociation(
    name="dimension22",
    ends={
        Property(name="sofiagraphics_Dimension24", type=sofiagraphics_Scene, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Scene23", type=sofiagraphics_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
color25: BinaryAssociation = BinaryAssociation(
    name="color25",
    ends={
        Property(name="sofiagraphics_Color", type=sofiagraphics_Scene, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Scene26", type=sofiagraphics_Color, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style27: BinaryAssociation = BinaryAssociation(
    name="style27",
    ends={
        Property(name="sofiagraphics_Style29", type=sofiagraphics_Scene, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Scene28", type=sofiagraphics_Style, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gesture30: BinaryAssociation = BinaryAssociation(
    name="gesture30",
    ends={
        Property(name="sofiagraphics_Gesture", type=sofiagraphics_Scene, multiplicity=Multiplicity(1, 1)),
        Property(name="sofiagraphics_Scene31", type=sofiagraphics_Gesture, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sofiagraphics_Rectangle_Widget = Generalization(general=Widget, specific=sofiagraphics_Rectangle)
gen_sofiagraphics_RoundedRectangle_Rectangle = Generalization(general=Rectangle, specific=sofiagraphics_RoundedRectangle)
gen_sofiagraphics_Ellipse_Widget = Generalization(general=Widget, specific=sofiagraphics_Ellipse)
gen_sofiagraphics_Polyline_Widget = Generalization(general=Widget, specific=sofiagraphics_Polyline)
gen_sofiagraphics_Text_Widget = Generalization(general=Widget, specific=sofiagraphics_Text)

# Domain Model
domain_model = DomainModel(
    name="sofiagraphics",
    types={sofiagraphics_Style, sofiagraphics_Rectangle, Widget, sofiagraphics_RoundedRectangle, Rectangle, sofiagraphics_Ellipse, sofiagraphics_Polyline, sofiagraphics_Point, sofiagraphics_Dimension, sofiagraphics_Widget, sofiagraphics_Text, sofiagraphics_Scene, sofiagraphics_Color, sofiagraphics_Gesture, Alignment},
    associations={style2, child4, pos6, dim8, corner10, point12, parent1, fgcolor32, bgcolor35, widget38, object14, root16, point19, dimension22, color25, style27, gesture30},
    generalizations={gen_sofiagraphics_Rectangle_Widget, gen_sofiagraphics_RoundedRectangle_Rectangle, gen_sofiagraphics_Ellipse_Widget, gen_sofiagraphics_Polyline_Widget, gen_sofiagraphics_Text_Widget},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)