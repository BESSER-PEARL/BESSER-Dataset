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
ColorConstants: Enumeration = Enumeration(
    name="ColorConstants",
    literals={
            EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="LIGHT_LIGHT_GRAY"),
			EnumerationLiteral(name="LIGHT_GRAY"),
			EnumerationLiteral(name="GRAY"),
			EnumerationLiteral(name="DARK_GRAY"),
			EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="DARK_BLUE"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="LIGHT_ORANGE"),
			EnumerationLiteral(name="ORANGE"),
			EnumerationLiteral(name="DARK_ORANGE"),
			EnumerationLiteral(name="YELLOW"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="LIGHT_GREEN"),
			EnumerationLiteral(name="DARK_GREEN"),
			EnumerationLiteral(name="CYAN"),
			EnumerationLiteral(name="LIGHT_BLUE"),
			EnumerationLiteral(name="NULL")
    }
)

LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="SOLID"),
			EnumerationLiteral(name="DOT"),
			EnumerationLiteral(name="DASH"),
			EnumerationLiteral(name="DASHDOT"),
			EnumerationLiteral(name="DASHDOTDOT"),
			EnumerationLiteral(name="NULL")
    }
)

YesNoBool: Enumeration = Enumeration(
    name="YesNoBool",
    literals={
            EnumerationLiteral(name="YES"),
			EnumerationLiteral(name="NO"),
			EnumerationLiteral(name="NULL")
    }
)

GradientAllignment: Enumeration = Enumeration(
    name="GradientAllignment",
    literals={
            EnumerationLiteral(name="VERTICAL"),
			EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="HORIZONTAL")
    }
)

# Classes
styles_Style = Class(name="styles_Style")
styles_StyleContainer = Class(name="styles_StyleContainer")
styles_StyleContainerElement = Class(name="styles_StyleContainerElement")
styles_ColorOrGradient = Class(name="styles_ColorOrGradient")
styles_HighlightingValues = Class(name="styles_HighlightingValues")
StyleContainerElement = Class(name="StyleContainerElement")
styles_JvmTypeReference = Class(name="styles_JvmTypeReference")
styles_StyleLayout = Class(name="styles_StyleLayout")
styles_Gradient = Class(name="styles_Gradient")
styles_GradientLayout = Class(name="styles_GradientLayout")
styles_GradientColorArea = Class(name="styles_GradientColorArea")
styles_ColorWithTransparency = Class(name="styles_ColorWithTransparency")
styles_Color = Class(name="styles_Color")
ColorOrGradient = Class(name="ColorOrGradient")
ColorWithTransparency = Class(name="ColorWithTransparency")
styles_RGBColor = Class(name="styles_RGBColor")
Color = Class(name="Color")
styles_GradientRef = Class(name="styles_GradientRef")
styles_ColorConstantRef = Class(name="styles_ColorConstantRef")
styles_Transparent = Class(name="styles_Transparent")

# styles_Style class attributes and methods

# styles_StyleContainer class attributes and methods

# styles_StyleContainerElement class attributes and methods
styles_StyleContainerElement_name: Property = Property(name="name", type=StringType)
styles_StyleContainerElement_description: Property = Property(name="description", type=StringType)
styles_StyleContainerElement.attributes={styles_StyleContainerElement_description, styles_StyleContainerElement_name}

# styles_ColorOrGradient class attributes and methods

# styles_HighlightingValues class attributes and methods

# StyleContainerElement class attributes and methods

# styles_JvmTypeReference class attributes and methods

# styles_StyleLayout class attributes and methods
styles_StyleLayout_transparency: Property = Property(name="transparency", type=FloatType)
styles_StyleLayout_gradient_orientation: Property = Property(name="gradient_orientation", type=StringType)
styles_StyleLayout_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
styles_StyleLayout_lineStyle: Property = Property(name="lineStyle", type=StringType)
styles_StyleLayout_fontName: Property = Property(name="fontName", type=StringType)
styles_StyleLayout_fontSize: Property = Property(name="fontSize", type=IntegerType)
styles_StyleLayout_fontItalic: Property = Property(name="fontItalic", type=StringType)
styles_StyleLayout_fontBold: Property = Property(name="fontBold", type=StringType)
styles_StyleLayout.attributes={styles_StyleLayout_fontItalic, styles_StyleLayout_transparency, styles_StyleLayout_fontSize, styles_StyleLayout_gradient_orientation, styles_StyleLayout_fontName, styles_StyleLayout_fontBold, styles_StyleLayout_lineStyle, styles_StyleLayout_lineWidth}

# styles_Gradient class attributes and methods

# styles_GradientLayout class attributes and methods

# styles_GradientColorArea class attributes and methods
styles_GradientColorArea_offset: Property = Property(name="offset", type=FloatType)
styles_GradientColorArea.attributes={styles_GradientColorArea_offset}

# styles_ColorWithTransparency class attributes and methods

# styles_Color class attributes and methods

# ColorOrGradient class attributes and methods

# ColorWithTransparency class attributes and methods

# styles_RGBColor class attributes and methods
styles_RGBColor_red: Property = Property(name="red", type=IntegerType)
styles_RGBColor_green: Property = Property(name="green", type=IntegerType)
styles_RGBColor_blue: Property = Property(name="blue", type=IntegerType)
styles_RGBColor.attributes={styles_RGBColor_red, styles_RGBColor_green, styles_RGBColor_blue}

# Color class attributes and methods

# styles_GradientRef class attributes and methods

# styles_ColorConstantRef class attributes and methods
styles_ColorConstantRef_value: Property = Property(name="value", type=StringType)
styles_ColorConstantRef.attributes={styles_ColorConstantRef_value}

# styles_Transparent class attributes and methods
styles_Transparent_transparent: Property = Property(name="transparent", type=BooleanType)
styles_Transparent.attributes={styles_Transparent_transparent}

# Relationships
styleContainerElement0: BinaryAssociation = BinaryAssociation(
    name="styleContainerElement0",
    ends={
        Property(name="styles_StyleContainerElement", type=styles_StyleContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_StyleContainer", type=styles_StyleContainerElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
background8: BinaryAssociation = BinaryAssociation(
    name="background8",
    ends={
        Property(name="styles_ColorOrGradient", type=styles_StyleLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_StyleLayout9", type=styles_ColorOrGradient, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superStyle1: BinaryAssociation = BinaryAssociation(
    name="superStyle1",
    ends={
        Property(name="styles_JvmTypeReference", type=styles_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_Style", type=styles_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superStyleFromDsl3: BinaryAssociation = BinaryAssociation(
    name="superStyleFromDsl3",
    ends={
        Property(name="styles_Style4", type=styles_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_Style2", type=styles_Style, multiplicity=Multiplicity(0, 1))
    }
)
layout5: BinaryAssociation = BinaryAssociation(
    name="layout5",
    ends={
        Property(name="styles_StyleLayout", type=styles_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_Style6", type=styles_StyleLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layout7: BinaryAssociation = BinaryAssociation(
    name="layout7",
    ends={
        Property(name="styles_GradientLayout", type=styles_Gradient, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_Gradient", type=styles_GradientLayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
area16: BinaryAssociation = BinaryAssociation(
    name="area16",
    ends={
        Property(name="styles_GradientColorArea", type=styles_GradientLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_GradientLayout17", type=styles_GradientColorArea, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
highlighting10: BinaryAssociation = BinaryAssociation(
    name="highlighting10",
    ends={
        Property(name="styles_HighlightingValues", type=styles_StyleLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_StyleLayout11", type=styles_HighlightingValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lineColor12: BinaryAssociation = BinaryAssociation(
    name="lineColor12",
    ends={
        Property(name="styles_ColorWithTransparency", type=styles_StyleLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_StyleLayout13", type=styles_ColorWithTransparency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fontColor14: BinaryAssociation = BinaryAssociation(
    name="fontColor14",
    ends={
        Property(name="styles_Color", type=styles_StyleLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_StyleLayout15", type=styles_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selected18: BinaryAssociation = BinaryAssociation(
    name="selected18",
    ends={
        Property(name="styles_ColorOrGradient20", type=styles_HighlightingValues, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_HighlightingValues19", type=styles_ColorOrGradient, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiselected21: BinaryAssociation = BinaryAssociation(
    name="multiselected21",
    ends={
        Property(name="styles_ColorOrGradient23", type=styles_HighlightingValues, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_HighlightingValues22", type=styles_ColorOrGradient, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allowed24: BinaryAssociation = BinaryAssociation(
    name="allowed24",
    ends={
        Property(name="styles_ColorOrGradient26", type=styles_HighlightingValues, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_HighlightingValues25", type=styles_ColorOrGradient, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unallowed27: BinaryAssociation = BinaryAssociation(
    name="unallowed27",
    ends={
        Property(name="styles_ColorOrGradient29", type=styles_HighlightingValues, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_HighlightingValues28", type=styles_ColorOrGradient, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color30: BinaryAssociation = BinaryAssociation(
    name="color30",
    ends={
        Property(name="styles_Color32", type=styles_GradientColorArea, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_GradientColorArea31", type=styles_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gradientRef33: BinaryAssociation = BinaryAssociation(
    name="gradientRef33",
    ends={
        Property(name="styles_JvmTypeReference34", type=styles_GradientRef, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_GradientRef", type=styles_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gradientRefFromDsl35: BinaryAssociation = BinaryAssociation(
    name="gradientRefFromDsl35",
    ends={
        Property(name="styles_Gradient37", type=styles_GradientRef, multiplicity=Multiplicity(1, 1)),
        Property(name="styles_GradientRef36", type=styles_Gradient, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_styles_Style_StyleContainerElement = Generalization(general=StyleContainerElement, specific=styles_Style)
gen_styles_Gradient_StyleContainerElement = Generalization(general=StyleContainerElement, specific=styles_Gradient)
gen_styles_Color_ColorOrGradient = Generalization(general=ColorOrGradient, specific=styles_Color)
gen_styles_Color_ColorWithTransparency = Generalization(general=ColorWithTransparency, specific=styles_Color)
gen_styles_RGBColor_Color = Generalization(general=Color, specific=styles_RGBColor)
gen_styles_GradientRef_ColorOrGradient = Generalization(general=ColorOrGradient, specific=styles_GradientRef)
gen_styles_ColorConstantRef_Color = Generalization(general=Color, specific=styles_ColorConstantRef)
gen_styles_Transparent_ColorOrGradient = Generalization(general=ColorOrGradient, specific=styles_Transparent)
gen_styles_Transparent_ColorWithTransparency = Generalization(general=ColorWithTransparency, specific=styles_Transparent)

# Domain Model
domain_model = DomainModel(
    name="styles",
    types={styles_Style, styles_StyleContainer, styles_StyleContainerElement, styles_ColorOrGradient, styles_HighlightingValues, StyleContainerElement, styles_JvmTypeReference, styles_StyleLayout, styles_Gradient, styles_GradientLayout, styles_GradientColorArea, styles_ColorWithTransparency, styles_Color, ColorOrGradient, ColorWithTransparency, styles_RGBColor, Color, styles_GradientRef, styles_ColorConstantRef, styles_Transparent, ColorConstants, LineStyle, YesNoBool, GradientAllignment},
    associations={styleContainerElement0, background8, superStyle1, superStyleFromDsl3, layout5, layout7, area16, highlighting10, lineColor12, fontColor14, selected18, multiselected21, allowed24, unallowed27, color30, gradientRef33, gradientRefFromDsl35},
    generalizations={gen_styles_Style_StyleContainerElement, gen_styles_Gradient_StyleContainerElement, gen_styles_Color_ColorOrGradient, gen_styles_Color_ColorWithTransparency, gen_styles_RGBColor_Color, gen_styles_GradientRef_ColorOrGradient, gen_styles_ColorConstantRef_Color, gen_styles_Transparent_ColorOrGradient, gen_styles_Transparent_ColorWithTransparency},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)