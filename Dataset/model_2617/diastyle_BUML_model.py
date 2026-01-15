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
DColor: Enumeration = Enumeration(
    name="DColor",
    literals={
            EnumerationLiteral(name="white"),
			EnumerationLiteral(name="black"),
			EnumerationLiteral(name="lightGray"),
			EnumerationLiteral(name="gray"),
			EnumerationLiteral(name="darkGray"),
			EnumerationLiteral(name="lightGreen"),
			EnumerationLiteral(name="darkGreen"),
			EnumerationLiteral(name="cyan"),
			EnumerationLiteral(name="lightBlue"),
			EnumerationLiteral(name="blue"),
			EnumerationLiteral(name="darkBlue"),
			EnumerationLiteral(name="red"),
			EnumerationLiteral(name="orange"),
			EnumerationLiteral(name="yellow"),
			EnumerationLiteral(name="green")
    }
)

DLayout: Enumeration = Enumeration(
    name="DLayout",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="free"),
			EnumerationLiteral(name="horizontal"),
			EnumerationLiteral(name="vertical")
    }
)

DLine: Enumeration = Enumeration(
    name="DLine",
    literals={
            EnumerationLiteral(name="solid"),
			EnumerationLiteral(name="dash"),
			EnumerationLiteral(name="dot"),
			EnumerationLiteral(name="dashdot"),
			EnumerationLiteral(name="dashdotdot"),
			EnumerationLiteral(name="custom")
    }
)

DDirection: Enumeration = Enumeration(
    name="DDirection",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right"),
			EnumerationLiteral(name="bidirectional")
    }
)

DShape: Enumeration = Enumeration(
    name="DShape",
    literals={
            EnumerationLiteral(name="rectangle"),
			EnumerationLiteral(name="roundedRectangle"),
			EnumerationLiteral(name="ellipse"),
			EnumerationLiteral(name="dot"),
			EnumerationLiteral(name="custom"),
			EnumerationLiteral(name="arrow"),
			EnumerationLiteral(name="triangle")
    }
)

DFontStyle: Enumeration = Enumeration(
    name="DFontStyle",
    literals={
            EnumerationLiteral(name="normal"),
			EnumerationLiteral(name="bold"),
			EnumerationLiteral(name="italic")
    }
)

DFontName: Enumeration = Enumeration(
    name="DFontName",
    literals={
            EnumerationLiteral(name="arial"),
			EnumerationLiteral(name="courier"),
			EnumerationLiteral(name="times")
    }
)

DAlignment: Enumeration = Enumeration(
    name="DAlignment",
    literals={
            EnumerationLiteral(name="fill"),
			EnumerationLiteral(name="beginning"),
			EnumerationLiteral(name="center"),
			EnumerationLiteral(name="end")
    }
)

# Classes
diastyle_DNodeEdgeStyle = Class(name="diastyle::DNodeEdgeStyle", is_abstract=True)
EModelElement = Class(name="EModelElement")
DBaseStyle = Class(name="DBaseStyle")
diastyle_DStyle = Class(name="diastyle::DStyle")
diastyle_DBaseStyle = Class(name="diastyle::DBaseStyle", is_abstract=True)
diastyle_DGraph = Class(name="diastyle::DGraph")
diastyle_DStyleBridge = Class(name="diastyle::DStyleBridge")
diastyle_DGraphElement = Class(name="diastyle::DGraphElement")
diastyle_DNodeStyle = Class(name="diastyle::DNodeStyle")
DNodeEdgeStyle = Class(name="DNodeEdgeStyle")
diastyle_DEdgeStyle = Class(name="diastyle::DEdgeStyle")
diastyle_DNestingEdgeStyle = Class(name="diastyle::DNestingEdgeStyle")

# diastyle_DNodeEdgeStyle class attributes and methods
diastyle_DNodeEdgeStyle_line: Property = Property(name="line", type=StringType)
diastyle_DNodeEdgeStyle_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
diastyle_DNodeEdgeStyle_fontName: Property = Property(name="fontName", type=StringType)
diastyle_DNodeEdgeStyle_fontStyle: Property = Property(name="fontStyle", type=StringType)
diastyle_DNodeEdgeStyle_fontSize: Property = Property(name="fontSize", type=IntegerType)
diastyle_DNodeEdgeStyle_fontColor: Property = Property(name="fontColor", type=StringType)
diastyle_DNodeEdgeStyle_textAlignment: Property = Property(name="textAlignment", type=StringType)
diastyle_DNodeEdgeStyle_icon: Property = Property(name="icon", type=StringType)
diastyle_DNodeEdgeStyle.attributes={diastyle_DNodeEdgeStyle_fontStyle, diastyle_DNodeEdgeStyle_lineWidth, diastyle_DNodeEdgeStyle_fontSize, diastyle_DNodeEdgeStyle_fontColor, diastyle_DNodeEdgeStyle_fontName, diastyle_DNodeEdgeStyle_textAlignment, diastyle_DNodeEdgeStyle_icon, diastyle_DNodeEdgeStyle_line}

# EModelElement class attributes and methods

# DBaseStyle class attributes and methods

# diastyle_DStyle class attributes and methods
diastyle_DStyle_styleHandler: Property = Property(name="styleHandler", type=StringType)
diastyle_DStyle_m_getBackgroundColor: Method = Method(name="getBackgroundColor", parameters={Parameter(name='element')}, type=StringType)
diastyle_DStyle_m_getIcon: Method = Method(name="getIcon", parameters={Parameter(name='element')}, type=StringType)
diastyle_DStyle_m_getFigure: Method = Method(name="getFigure", parameters={Parameter(name='element')}, type=StringType)
diastyle_DStyle.attributes={diastyle_DStyle_styleHandler}
diastyle_DStyle.methods={diastyle_DStyle_m_getIcon, diastyle_DStyle_m_getFigure, diastyle_DStyle_m_getBackgroundColor}

# diastyle_DBaseStyle class attributes and methods
diastyle_DBaseStyle_name: Property = Property(name="name", type=StringType)
diastyle_DBaseStyle_color: Property = Property(name="color", type=StringType)
diastyle_DBaseStyle_parentName: Property = Property(name="parentName", type=StringType)
diastyle_DBaseStyle.attributes={diastyle_DBaseStyle_parentName, diastyle_DBaseStyle_name, diastyle_DBaseStyle_color}

# diastyle_DGraph class attributes and methods

# diastyle_DStyleBridge class attributes and methods
diastyle_DStyleBridge_name: Property = Property(name="name", type=StringType)
diastyle_DStyleBridge.attributes={diastyle_DStyleBridge_name}

# diastyle_DGraphElement class attributes and methods

# diastyle_DNodeStyle class attributes and methods
diastyle_DNodeStyle_radius: Property = Property(name="radius", type=IntegerType)
diastyle_DNodeStyle_shape: Property = Property(name="shape", type=StringType)
diastyle_DNodeStyle_sizeY: Property = Property(name="sizeY", type=IntegerType)
diastyle_DNodeStyle_figure: Property = Property(name="figure", type=StringType)
diastyle_DNodeStyle_shapeData: Property = Property(name="shapeData", type=StringType)
diastyle_DNodeStyle_layout: Property = Property(name="layout", type=StringType)
diastyle_DNodeStyle_sizeX: Property = Property(name="sizeX", type=IntegerType)
diastyle_DNodeStyle.attributes={diastyle_DNodeStyle_sizeX, diastyle_DNodeStyle_radius, diastyle_DNodeStyle_sizeY, diastyle_DNodeStyle_figure, diastyle_DNodeStyle_shapeData, diastyle_DNodeStyle_shape, diastyle_DNodeStyle_layout}

# DNodeEdgeStyle class attributes and methods

# diastyle_DEdgeStyle class attributes and methods
diastyle_DEdgeStyle_arrowDirection: Property = Property(name="arrowDirection", type=StringType)
diastyle_DEdgeStyle_arrowSize: Property = Property(name="arrowSize", type=IntegerType)
diastyle_DEdgeStyle_shape: Property = Property(name="shape", type=StringType)
diastyle_DEdgeStyle.attributes={diastyle_DEdgeStyle_arrowSize, diastyle_DEdgeStyle_shape, diastyle_DEdgeStyle_arrowDirection}

# diastyle_DNestingEdgeStyle class attributes and methods

# Relationships
styles0: BinaryAssociation = BinaryAssociation(
    name="styles0",
    ends={
        Property(name="diastyle_DBaseStyle", type=diastyle_DStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diastyle_DStyle", type=diastyle_DBaseStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dGraph1: BinaryAssociation = BinaryAssociation(
    name="dGraph1",
    ends={
        Property(name="diastyle_DGraph", type=diastyle_DStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diastyle_DStyle2", type=diastyle_DGraph, multiplicity=Multiplicity(0, 1))
    }
)
dGraphElement3: BinaryAssociation = BinaryAssociation(
    name="dGraphElement3",
    ends={
        Property(name="diastyle_DGraphElement", type=diastyle_DStyleBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="diastyle_DStyleBridge", type=diastyle_DGraphElement, multiplicity=Multiplicity(0, 1))
    }
)
styleBridges4: BinaryAssociation = BinaryAssociation(
    name="styleBridges4",
    ends={
        Property(name="diastyle_DStyleBridge6", type=diastyle_DBaseStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diastyle_DBaseStyle5", type=diastyle_DStyleBridge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent8: BinaryAssociation = BinaryAssociation(
    name="parent8",
    ends={
        Property(name="diastyle_DBaseStyle9", type=diastyle_DBaseStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="diastyle_DBaseStyle7", type=diastyle_DBaseStyle, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_diastyle_DNodeEdgeStyle_EModelElement = Generalization(general=EModelElement, specific=diastyle_DNodeEdgeStyle)
gen_diastyle_DNodeEdgeStyle_DBaseStyle = Generalization(general=DBaseStyle, specific=diastyle_DNodeEdgeStyle)
gen_diastyle_DStyle_EModelElement = Generalization(general=EModelElement, specific=diastyle_DStyle)
gen_diastyle_DNodeStyle_DNodeEdgeStyle = Generalization(general=DNodeEdgeStyle, specific=diastyle_DNodeStyle)
gen_diastyle_DEdgeStyle_DNodeEdgeStyle = Generalization(general=DNodeEdgeStyle, specific=diastyle_DEdgeStyle)
gen_diastyle_DNestingEdgeStyle_DBaseStyle = Generalization(general=DBaseStyle, specific=diastyle_DNestingEdgeStyle)

# Domain Model
domain_model = DomainModel(
    name="diastyle",
    types={diastyle_DNodeEdgeStyle, EModelElement, DBaseStyle, diastyle_DStyle, diastyle_DBaseStyle, diastyle_DGraph, diastyle_DStyleBridge, diastyle_DGraphElement, diastyle_DNodeStyle, DNodeEdgeStyle, diastyle_DEdgeStyle, diastyle_DNestingEdgeStyle, DColor, DLayout, DLine, DDirection, DShape, DFontStyle, DFontName, DAlignment},
    associations={styles0, dGraph1, dGraphElement3, styleBridges4, parent8},
    generalizations={gen_diastyle_DNodeEdgeStyle_EModelElement, gen_diastyle_DNodeEdgeStyle_DBaseStyle, gen_diastyle_DStyle_EModelElement, gen_diastyle_DNodeStyle_DNodeEdgeStyle, gen_diastyle_DEdgeStyle_DNodeEdgeStyle, gen_diastyle_DNestingEdgeStyle_DBaseStyle},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)