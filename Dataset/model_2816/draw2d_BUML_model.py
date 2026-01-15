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
			EnumerationLiteral(name="MIDDLE"),
			EnumerationLiteral(name="BOTTOM")
    }
)

Orientation: Enumeration = Enumeration(
    name="Orientation",
    literals={
            EnumerationLiteral(name="HORIZONTAL"),
			EnumerationLiteral(name="VERTICAL")
    }
)

Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="NORTH"),
			EnumerationLiteral(name="SOUTH"),
			EnumerationLiteral(name="EAST"),
			EnumerationLiteral(name="WEST")
    }
)

# Classes
draw2d_Draw2DCanvas = Class(name="draw2d::Draw2DCanvas")
Canvas = Class(name="Canvas")
draw2d_Figure = Class(name="draw2d::Figure")
draw2d_Font = Class(name="draw2d::Font")
draw2d_Border = Class(name="draw2d::Border", is_abstract=True)
draw2d_Label = Class(name="draw2d::Label")
Figure = Class(name="Figure")
draw2d_Shape = Class(name="draw2d::Shape", is_abstract=True)
draw2d_Color = Class(name="draw2d::Color")
draw2d_RectangleFigure = Class(name="draw2d::RectangleFigure")
Shape = Class(name="Shape")
draw2d_RoundedRectangle = Class(name="draw2d::RoundedRectangle")
draw2d_Ellipse = Class(name="draw2d::Ellipse")
draw2d_Triangle = Class(name="draw2d::Triangle")
draw2d_PointListShape = Class(name="draw2d::PointListShape", is_abstract=True)
draw2d_Polyline = Class(name="draw2d::Polyline")
PointListShape = Class(name="PointListShape")
draw2d_Polygon = Class(name="draw2d::Polygon")
Polyline = Class(name="Polyline")
draw2d_PolylineShape = Class(name="draw2d::PolylineShape")
draw2d_ConnectionAnchor = Class(name="draw2d::ConnectionAnchor", is_abstract=True)
draw2d_XYAnchor = Class(name="draw2d::XYAnchor")
ConnectionAnchor = Class(name="ConnectionAnchor")
draw2d_BlockFlow = Class(name="draw2d::BlockFlow")
draw2d_LabeledBorder = Class(name="draw2d::LabeledBorder", is_abstract=True)
Border = Class(name="Border")
draw2d_FrameBorder = Class(name="draw2d::FrameBorder")
LabeledBorder = Class(name="LabeledBorder")
draw2d_ColoredLabeledBorder = Class(name="draw2d::ColoredLabeledBorder", is_abstract=True)
draw2d_GroupBoxBorder = Class(name="draw2d::GroupBoxBorder")
ColoredLabeledBorder = Class(name="ColoredLabeledBorder")
draw2d_PolygonShape = Class(name="draw2d::PolygonShape")
draw2d_ImageFigure = Class(name="draw2d::ImageFigure")
draw2d_TitleBarBorder = Class(name="draw2d::TitleBarBorder")
draw2d_FlowBorder = Class(name="draw2d::FlowBorder")

# draw2d_Draw2DCanvas class attributes and methods

# Canvas class attributes and methods

# draw2d_Figure class attributes and methods
draw2d_Figure_enabled: Property = Property(name="enabled", type=BooleanType)
draw2d_Figure_visible: Property = Property(name="visible", type=BooleanType)
draw2d_Figure_opaque: Property = Property(name="opaque", type=BooleanType)
draw2d_Figure_focusTraversable: Property = Property(name="focusTraversable", type=BooleanType)
draw2d_Figure_bounds: Property = Property(name="bounds", type=StringType)
draw2d_Figure_minimumSize: Property = Property(name="minimumSize", type=StringType)
draw2d_Figure_preferredSize: Property = Property(name="preferredSize", type=StringType)
draw2d_Figure_maximumSize: Property = Property(name="maximumSize", type=StringType)
draw2d_Figure.attributes={draw2d_Figure_opaque, draw2d_Figure_maximumSize, draw2d_Figure_minimumSize, draw2d_Figure_bounds, draw2d_Figure_focusTraversable, draw2d_Figure_preferredSize, draw2d_Figure_visible, draw2d_Figure_enabled}

# draw2d_Font class attributes and methods

# draw2d_Border class attributes and methods
draw2d_Border_opaque: Property = Property(name="opaque", type=BooleanType)
draw2d_Border.attributes={draw2d_Border_opaque}

# draw2d_Label class attributes and methods
draw2d_Label_text: Property = Property(name="text", type=StringType)
draw2d_Label_textAlignment: Property = Property(name="textAlignment", type=StringType)
draw2d_Label_textPlacement: Property = Property(name="textPlacement", type=StringType)
draw2d_Label_icon: Property = Property(name="icon", type=StringType)
draw2d_Label_iconAlignment: Property = Property(name="iconAlignment", type=StringType)
draw2d_Label_iconTextGap: Property = Property(name="iconTextGap", type=IntegerType)
draw2d_Label.attributes={draw2d_Label_iconTextGap, draw2d_Label_iconAlignment, draw2d_Label_icon, draw2d_Label_text, draw2d_Label_textAlignment, draw2d_Label_textPlacement}

# Figure class attributes and methods

# draw2d_Shape class attributes and methods
draw2d_Shape_fill: Property = Property(name="fill", type=BooleanType)
draw2d_Shape_fillXOR: Property = Property(name="fillXOR", type=BooleanType)
draw2d_Shape_outline: Property = Property(name="outline", type=BooleanType)
draw2d_Shape_outlineXOR: Property = Property(name="outlineXOR", type=BooleanType)
draw2d_Shape_alpha: Property = Property(name="alpha", type=StringType)
draw2d_Shape_antialias: Property = Property(name="antialias", type=StringType)
draw2d_Shape_lineDash: Property = Property(name="lineDash", type=FloatType)
draw2d_Shape_lineDashOffset: Property = Property(name="lineDashOffset", type=FloatType)
draw2d_Shape_lineMiterLimit: Property = Property(name="lineMiterLimit", type=FloatType)
draw2d_Shape_lineWidthFloat: Property = Property(name="lineWidthFloat", type=FloatType)
draw2d_Shape_lineStyle: Property = Property(name="lineStyle", type=StringType)
draw2d_Shape_lineCap: Property = Property(name="lineCap", type=StringType)
draw2d_Shape_lineJoin: Property = Property(name="lineJoin", type=StringType)
draw2d_Shape.attributes={draw2d_Shape_antialias, draw2d_Shape_fill, draw2d_Shape_lineStyle, draw2d_Shape_lineDash, draw2d_Shape_lineMiterLimit, draw2d_Shape_lineJoin, draw2d_Shape_lineWidthFloat, draw2d_Shape_lineCap, draw2d_Shape_alpha, draw2d_Shape_outlineXOR, draw2d_Shape_outline, draw2d_Shape_lineDashOffset, draw2d_Shape_fillXOR}

# draw2d_Color class attributes and methods

# draw2d_RectangleFigure class attributes and methods

# Shape class attributes and methods

# draw2d_RoundedRectangle class attributes and methods
draw2d_RoundedRectangle_cornerDimensions: Property = Property(name="cornerDimensions", type=StringType)
draw2d_RoundedRectangle.attributes={draw2d_RoundedRectangle_cornerDimensions}

# draw2d_Ellipse class attributes and methods

# draw2d_Triangle class attributes and methods
draw2d_Triangle_orientation: Property = Property(name="orientation", type=StringType)
draw2d_Triangle_direction: Property = Property(name="direction", type=StringType)
draw2d_Triangle.attributes={draw2d_Triangle_direction, draw2d_Triangle_orientation}

# draw2d_PointListShape class attributes and methods
draw2d_PointListShape_pointList: Property = Property(name="pointList", type=IntegerType)
draw2d_PointListShape.attributes={draw2d_PointListShape_pointList}

# draw2d_Polyline class attributes and methods
draw2d_Polyline_tolerance: Property = Property(name="tolerance", type=IntegerType)
draw2d_Polyline.attributes={draw2d_Polyline_tolerance}

# PointListShape class attributes and methods

# draw2d_Polygon class attributes and methods

# Polyline class attributes and methods

# draw2d_PolylineShape class attributes and methods
draw2d_PolylineShape_tolerance: Property = Property(name="tolerance", type=IntegerType)
draw2d_PolylineShape.attributes={draw2d_PolylineShape_tolerance}

# draw2d_ConnectionAnchor class attributes and methods

# draw2d_XYAnchor class attributes and methods
draw2d_XYAnchor_location: Property = Property(name="location", type=StringType)
draw2d_XYAnchor.attributes={draw2d_XYAnchor_location}

# ConnectionAnchor class attributes and methods

# draw2d_BlockFlow class attributes and methods
draw2d_BlockFlow_orientation: Property = Property(name="orientation", type=StringType)
draw2d_BlockFlow.attributes={draw2d_BlockFlow_orientation}

# draw2d_LabeledBorder class attributes and methods
draw2d_LabeledBorder_label: Property = Property(name="label", type=StringType)
draw2d_LabeledBorder.attributes={draw2d_LabeledBorder_label}

# Border class attributes and methods

# draw2d_FrameBorder class attributes and methods

# LabeledBorder class attributes and methods

# draw2d_ColoredLabeledBorder class attributes and methods

# draw2d_GroupBoxBorder class attributes and methods

# ColoredLabeledBorder class attributes and methods

# draw2d_PolygonShape class attributes and methods

# draw2d_ImageFigure class attributes and methods
draw2d_ImageFigure_image: Property = Property(name="image", type=StringType)
draw2d_ImageFigure.attributes={draw2d_ImageFigure_image}

# draw2d_TitleBarBorder class attributes and methods

# draw2d_FlowBorder class attributes and methods
draw2d_FlowBorder_rightMargin: Property = Property(name="rightMargin", type=IntegerType)
draw2d_FlowBorder_topMargin: Property = Property(name="topMargin", type=IntegerType)
draw2d_FlowBorder_bottomMargin: Property = Property(name="bottomMargin", type=IntegerType)
draw2d_FlowBorder_leftMargin: Property = Property(name="leftMargin", type=IntegerType)
draw2d_FlowBorder.attributes={draw2d_FlowBorder_leftMargin, draw2d_FlowBorder_rightMargin, draw2d_FlowBorder_topMargin, draw2d_FlowBorder_bottomMargin}

# Relationships
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="draw2d_Figure", type=draw2d_Draw2DCanvas, multiplicity=Multiplicity(1, 1)),
        Property(name="draw2d_Draw2DCanvas", type=draw2d_Figure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="Figure", type=draw2d_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=draw2d_Figure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent4: BinaryAssociation = BinaryAssociation(
    name="parent4",
    ends={
        Property(name="Figure5", type=draw2d_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=draw2d_Figure, multiplicity=Multiplicity(0, 1))
    }
)
toolTip7: BinaryAssociation = BinaryAssociation(
    name="toolTip7",
    ends={
        Property(name="draw2d_Figure8", type=draw2d_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="draw2d_Figure6", type=draw2d_Figure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundColor11: BinaryAssociation = BinaryAssociation(
    name="foregroundColor11",
    ends={
        Property(name="draw2d_Figure12", type=draw2d_Color, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="draw2d_Color13", type=draw2d_Figure, multiplicity=Multiplicity(1, 1))
    }
)
font14: BinaryAssociation = BinaryAssociation(
    name="font14",
    ends={
        Property(name="draw2d_Font", type=draw2d_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="draw2d_Figure15", type=draw2d_Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
border16: BinaryAssociation = BinaryAssociation(
    name="border16",
    ends={
        Property(name="draw2d_Border", type=draw2d_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="draw2d_Figure17", type=draw2d_Border, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor9: BinaryAssociation = BinaryAssociation(
    name="backgroundColor9",
    ends={
        Property(name="draw2d_Color", type=draw2d_Figure, multiplicity=Multiplicity(1, 1)),
        Property(name="draw2d_Figure10", type=draw2d_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner18: BinaryAssociation = BinaryAssociation(
    name="owner18",
    ends={
        Property(name="draw2d_Figure19", type=draw2d_ConnectionAnchor, multiplicity=Multiplicity(1, 1)),
        Property(name="draw2d_ConnectionAnchor", type=draw2d_Figure, multiplicity=Multiplicity(0, 1))
    }
)
font20: BinaryAssociation = BinaryAssociation(
    name="font20",
    ends={
        Property(name="draw2d_Font21", type=draw2d_LabeledBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="draw2d_LabeledBorder", type=draw2d_Font, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
textColor22: BinaryAssociation = BinaryAssociation(
    name="textColor22",
    ends={
        Property(name="draw2d_Color23", type=draw2d_ColoredLabeledBorder, multiplicity=Multiplicity(1, 1)),
        Property(name="draw2d_ColoredLabeledBorder", type=draw2d_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_draw2d_Draw2DCanvas_Canvas = Generalization(general=Canvas, specific=draw2d_Draw2DCanvas)
gen_draw2d_Label_Figure = Generalization(general=Figure, specific=draw2d_Label)
gen_draw2d_Shape_Figure = Generalization(general=Figure, specific=draw2d_Shape)
gen_draw2d_RectangleFigure_Shape = Generalization(general=Shape, specific=draw2d_RectangleFigure)
gen_draw2d_RoundedRectangle_Shape = Generalization(general=Shape, specific=draw2d_RoundedRectangle)
gen_draw2d_Ellipse_Shape = Generalization(general=Shape, specific=draw2d_Ellipse)
gen_draw2d_Triangle_Shape = Generalization(general=Shape, specific=draw2d_Triangle)
gen_draw2d_PointListShape_Shape = Generalization(general=Shape, specific=draw2d_PointListShape)
gen_draw2d_Polyline_PointListShape = Generalization(general=PointListShape, specific=draw2d_Polyline)
gen_draw2d_Polygon_Polyline = Generalization(general=Polyline, specific=draw2d_Polygon)
gen_draw2d_PolylineShape_PointListShape = Generalization(general=PointListShape, specific=draw2d_PolylineShape)
gen_draw2d_XYAnchor_ConnectionAnchor = Generalization(general=ConnectionAnchor, specific=draw2d_XYAnchor)
gen_draw2d_BlockFlow_Figure = Generalization(general=Figure, specific=draw2d_BlockFlow)
gen_draw2d_LabeledBorder_Border = Generalization(general=Border, specific=draw2d_LabeledBorder)
gen_draw2d_FrameBorder_LabeledBorder = Generalization(general=LabeledBorder, specific=draw2d_FrameBorder)
gen_draw2d_ColoredLabeledBorder_LabeledBorder = Generalization(general=LabeledBorder, specific=draw2d_ColoredLabeledBorder)
gen_draw2d_PolygonShape_PointListShape = Generalization(general=PointListShape, specific=draw2d_PolygonShape)
gen_draw2d_ImageFigure_Figure = Generalization(general=Figure, specific=draw2d_ImageFigure)
gen_draw2d_GroupBoxBorder_ColoredLabeledBorder = Generalization(general=ColoredLabeledBorder, specific=draw2d_GroupBoxBorder)
gen_draw2d_TitleBarBorder_ColoredLabeledBorder = Generalization(general=ColoredLabeledBorder, specific=draw2d_TitleBarBorder)
gen_draw2d_FlowBorder_Border = Generalization(general=Border, specific=draw2d_FlowBorder)

# Domain Model
domain_model = DomainModel(
    name="draw2d",
    types={draw2d_Draw2DCanvas, Canvas, draw2d_Figure, draw2d_Font, draw2d_Border, draw2d_Label, Figure, draw2d_Shape, draw2d_Color, draw2d_RectangleFigure, Shape, draw2d_RoundedRectangle, draw2d_Ellipse, draw2d_Triangle, draw2d_PointListShape, draw2d_Polyline, PointListShape, draw2d_Polygon, Polyline, draw2d_PolylineShape, draw2d_ConnectionAnchor, draw2d_XYAnchor, ConnectionAnchor, draw2d_BlockFlow, draw2d_LabeledBorder, Border, draw2d_FrameBorder, LabeledBorder, draw2d_ColoredLabeledBorder, draw2d_GroupBoxBorder, ColoredLabeledBorder, draw2d_PolygonShape, draw2d_ImageFigure, draw2d_TitleBarBorder, draw2d_FlowBorder, Alignment, Orientation, Direction},
    associations={contents0, children2, parent4, toolTip7, foregroundColor11, font14, border16, backgroundColor9, owner18, font20, textColor22},
    generalizations={gen_draw2d_Draw2DCanvas_Canvas, gen_draw2d_Label_Figure, gen_draw2d_Shape_Figure, gen_draw2d_RectangleFigure_Shape, gen_draw2d_RoundedRectangle_Shape, gen_draw2d_Ellipse_Shape, gen_draw2d_Triangle_Shape, gen_draw2d_PointListShape_Shape, gen_draw2d_Polyline_PointListShape, gen_draw2d_Polygon_Polyline, gen_draw2d_PolylineShape_PointListShape, gen_draw2d_XYAnchor_ConnectionAnchor, gen_draw2d_BlockFlow_Figure, gen_draw2d_LabeledBorder_Border, gen_draw2d_FrameBorder_LabeledBorder, gen_draw2d_ColoredLabeledBorder_LabeledBorder, gen_draw2d_PolygonShape_PointListShape, gen_draw2d_ImageFigure_Figure, gen_draw2d_GroupBoxBorder_ColoredLabeledBorder, gen_draw2d_TitleBarBorder_ColoredLabeledBorder, gen_draw2d_FlowBorder_Border},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)