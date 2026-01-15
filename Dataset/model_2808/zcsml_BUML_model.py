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
CSOrientation: Enumeration = Enumeration(
    name="CSOrientation",
    literals={
            EnumerationLiteral(name="VERTICAL"),
			EnumerationLiteral(name="HORIZONTAL")
    }
)

CSFitType: Enumeration = Enumeration(
    name="CSFitType",
    literals={
            EnumerationLiteral(name="AUTO_EXPAND"),
			EnumerationLiteral(name="FIT_TO_CHILDREN")
    }
)

# Classes
cs_CSRoot = Class(name="cs::CSRoot")
CSElement = Class(name="CSElement")
cs_CSElement = Class(name="cs::CSElement")
ENamedElement = Class(name="ENamedElement")
cs_CSStroke = Class(name="cs::CSStroke")
cs_CSColor = Class(name="cs::CSColor")
cs_CSNode = Class(name="cs::CSNode")
cs_CSConnection = Class(name="cs::CSConnection")
cs_CSShape = Class(name="cs::CSShape")
cs_CSTransform = Class(name="cs::CSTransform")
cs_EObject = Class(name="cs::EObject")
cs_EStructuralFeature = Class(name="cs::EStructuralFeature")
cs_CSLayout = Class(name="cs::CSLayout")
cs_CSConnectionEnd = Class(name="cs::CSConnectionEnd")
cs_CSText = Class(name="cs::CSText")
CSNode = Class(name="CSNode")
cs_CSPoint = Class(name="cs::CSPoint")
cs_CSTemplateDescription = Class(name="cs::CSTemplateDescription")
cs_EClass = Class(name="cs::EClass")

# cs_CSRoot class attributes and methods

# CSElement class attributes and methods

# cs_CSElement class attributes and methods
cs_CSElement_selectable: Property = Property(name="selectable", type=StringType)
cs_CSElement_draggable: Property = Property(name="draggable", type=BooleanType)
cs_CSElement_resizable: Property = Property(name="resizable", type=BooleanType)
cs_CSElement_templateRoot: Property = Property(name="templateRoot", type=BooleanType)
cs_CSElement_minZoom: Property = Property(name="minZoom", type=StringType)
cs_CSElement_maxZoom: Property = Property(name="maxZoom", type=StringType)
cs_CSElement.attributes={cs_CSElement_templateRoot, cs_CSElement_selectable, cs_CSElement_maxZoom, cs_CSElement_draggable, cs_CSElement_minZoom, cs_CSElement_resizable}

# ENamedElement class attributes and methods

# cs_CSStroke class attributes and methods
cs_CSStroke_width: Property = Property(name="width", type=FloatType)
cs_CSStroke_join: Property = Property(name="join", type=IntegerType)
cs_CSStroke_cap: Property = Property(name="cap", type=IntegerType)
cs_CSStroke_miterlimit: Property = Property(name="miterlimit", type=FloatType)
cs_CSStroke_dash: Property = Property(name="dash", type=FloatType)
cs_CSStroke_dash_phase: Property = Property(name="dash_phase", type=FloatType)
cs_CSStroke.attributes={cs_CSStroke_dash_phase, cs_CSStroke_width, cs_CSStroke_cap, cs_CSStroke_join, cs_CSStroke_dash, cs_CSStroke_miterlimit}

# cs_CSColor class attributes and methods
cs_CSColor_r: Property = Property(name="r", type=FloatType)
cs_CSColor_g: Property = Property(name="g", type=FloatType)
cs_CSColor_b: Property = Property(name="b", type=FloatType)
cs_CSColor_a: Property = Property(name="a", type=FloatType)
cs_CSColor.attributes={cs_CSColor_r, cs_CSColor_g, cs_CSColor_a, cs_CSColor_b}

# cs_CSNode class attributes and methods
cs_CSNode_height: Property = Property(name="height", type=StringType)
cs_CSNode_width: Property = Property(name="width", type=StringType)
cs_CSNode_x: Property = Property(name="x", type=StringType)
cs_CSNode_y: Property = Property(name="y", type=StringType)
cs_CSNode_horizontalAlign: Property = Property(name="horizontalAlign", type=StringType)
cs_CSNode_verticalAlign: Property = Property(name="verticalAlign", type=StringType)
cs_CSNode_widthRatioToParent: Property = Property(name="widthRatioToParent", type=StringType)
cs_CSNode_heightRatioToParent: Property = Property(name="heightRatioToParent", type=StringType)
cs_CSNode_minHeight: Property = Property(name="minHeight", type=StringType)
cs_CSNode_maxHeight: Property = Property(name="maxHeight", type=StringType)
cs_CSNode_minWidth: Property = Property(name="minWidth", type=StringType)
cs_CSNode_maxWidth: Property = Property(name="maxWidth", type=StringType)
cs_CSNode.attributes={cs_CSNode_height, cs_CSNode_verticalAlign, cs_CSNode_horizontalAlign, cs_CSNode_width, cs_CSNode_minWidth, cs_CSNode_maxWidth, cs_CSNode_maxHeight, cs_CSNode_x, cs_CSNode_minHeight, cs_CSNode_heightRatioToParent, cs_CSNode_y, cs_CSNode_widthRatioToParent}

# cs_CSConnection class attributes and methods

# cs_CSShape class attributes and methods
cs_CSShape_closed: Property = Property(name="closed", type=BooleanType)
cs_CSShape.attributes={cs_CSShape_closed}

# cs_CSTransform class attributes and methods
cs_CSTransform_m11: Property = Property(name="m11", type=FloatType)
cs_CSTransform_m12: Property = Property(name="m12", type=FloatType)
cs_CSTransform_m20: Property = Property(name="m20", type=FloatType)
cs_CSTransform_m21: Property = Property(name="m21", type=FloatType)
cs_CSTransform_m22: Property = Property(name="m22", type=FloatType)
cs_CSTransform_m00: Property = Property(name="m00", type=FloatType)
cs_CSTransform_m01: Property = Property(name="m01", type=FloatType)
cs_CSTransform_m02: Property = Property(name="m02", type=FloatType)
cs_CSTransform_m10: Property = Property(name="m10", type=FloatType)
cs_CSTransform.attributes={cs_CSTransform_m21, cs_CSTransform_m20, cs_CSTransform_m11, cs_CSTransform_m12, cs_CSTransform_m02, cs_CSTransform_m00, cs_CSTransform_m10, cs_CSTransform_m01, cs_CSTransform_m22}

# cs_EObject class attributes and methods

# cs_EStructuralFeature class attributes and methods

# cs_CSLayout class attributes and methods

# cs_CSConnectionEnd class attributes and methods
cs_CSConnectionEnd_tipType: Property = Property(name="tipType", type=IntegerType)
cs_CSConnectionEnd.attributes={cs_CSConnectionEnd_tipType}

# cs_CSText class attributes and methods
cs_CSText_text: Property = Property(name="text", type=StringType)
cs_CSText.attributes={cs_CSText_text}

# CSNode class attributes and methods

# cs_CSPoint class attributes and methods
cs_CSPoint_x: Property = Property(name="x", type=FloatType)
cs_CSPoint_y: Property = Property(name="y", type=FloatType)
cs_CSPoint.attributes={cs_CSPoint_y, cs_CSPoint_x}

# cs_CSTemplateDescription class attributes and methods
cs_CSTemplateDescription_scale: Property = Property(name="scale", type=FloatType)
cs_CSTemplateDescription.attributes={cs_CSTemplateDescription_scale}

# cs_EClass class attributes and methods

# Relationships
stroke0: BinaryAssociation = BinaryAssociation(
    name="stroke0",
    ends={
        Property(name="cs_CSElement", type=cs_CSStroke, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="cs_CSStroke", type=cs_CSElement, multiplicity=Multiplicity(1, 1))
    }
)
foreground6: BinaryAssociation = BinaryAssociation(
    name="foreground6",
    ends={
        Property(name="cs_CSColor", type=cs_CSElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSElement7", type=cs_CSColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="CSElement", type=cs_CSElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=cs_CSElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent4: BinaryAssociation = BinaryAssociation(
    name="parent4",
    ends={
        Property(name="CSElement5", type=cs_CSElement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=cs_CSElement, multiplicity=Multiplicity(0, 1))
    }
)
connections21: BinaryAssociation = BinaryAssociation(
    name="connections21",
    ends={
        Property(name="cs_CSConnection", type=cs_CSNode, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSNode", type=cs_CSConnection, multiplicity=Multiplicity(0, 9999))
    }
)
background8: BinaryAssociation = BinaryAssociation(
    name="background8",
    ends={
        Property(name="cs_CSColor10", type=cs_CSElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSElement9", type=cs_CSColor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shape11: BinaryAssociation = BinaryAssociation(
    name="shape11",
    ends={
        Property(name="cs_CSShape", type=cs_CSElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSElement12", type=cs_CSShape, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transform13: BinaryAssociation = BinaryAssociation(
    name="transform13",
    ends={
        Property(name="cs_CSTransform", type=cs_CSElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSElement14", type=cs_CSTransform, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object15: BinaryAssociation = BinaryAssociation(
    name="object15",
    ends={
        Property(name="cs_EObject", type=cs_CSElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSElement16", type=cs_EObject, multiplicity=Multiplicity(0, 1))
    }
)
displayedStructuralFeatures17: BinaryAssociation = BinaryAssociation(
    name="displayedStructuralFeatures17",
    ends={
        Property(name="cs_EStructuralFeature", type=cs_CSElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSElement18", type=cs_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
layout19: BinaryAssociation = BinaryAssociation(
    name="layout19",
    ends={
        Property(name="cs_CSLayout", type=cs_CSElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSElement20", type=cs_CSLayout, multiplicity=Multiplicity(0, 1))
    }
)
connectionEnds22: BinaryAssociation = BinaryAssociation(
    name="connectionEnds22",
    ends={
        Property(name="cs_CSConnectionEnd", type=cs_CSConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSConnection23", type=cs_CSConnectionEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
points24: BinaryAssociation = BinaryAssociation(
    name="points24",
    ends={
        Property(name="cs_CSPoint", type=cs_CSShape, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSShape25", type=cs_CSPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerClass26: BinaryAssociation = BinaryAssociation(
    name="containerClass26",
    ends={
        Property(name="cs_EClass", type=cs_CSTemplateDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSTemplateDescription", type=cs_EClass, multiplicity=Multiplicity(0, 1))
    }
)
theClass27: BinaryAssociation = BinaryAssociation(
    name="theClass27",
    ends={
        Property(name="cs_EClass29", type=cs_CSTemplateDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSTemplateDescription28", type=cs_EClass, multiplicity=Multiplicity(0, 1))
    }
)
containerStructuralFeature30: BinaryAssociation = BinaryAssociation(
    name="containerStructuralFeature30",
    ends={
        Property(name="cs_EStructuralFeature32", type=cs_CSTemplateDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSTemplateDescription31", type=cs_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
template33: BinaryAssociation = BinaryAssociation(
    name="template33",
    ends={
        Property(name="cs_CSElement35", type=cs_CSTemplateDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSTemplateDescription34", type=cs_CSElement, multiplicity=Multiplicity(0, 1))
    }
)
node36: BinaryAssociation = BinaryAssociation(
    name="node36",
    ends={
        Property(name="cs_CSNode38", type=cs_CSConnectionEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSConnectionEnd37", type=cs_CSNode, multiplicity=Multiplicity(0, 1))
    }
)
connStructuralFeature39: BinaryAssociation = BinaryAssociation(
    name="connStructuralFeature39",
    ends={
        Property(name="cs_EStructuralFeature41", type=cs_CSConnectionEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSConnectionEnd40", type=cs_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
nodeStructuralFeature42: BinaryAssociation = BinaryAssociation(
    name="nodeStructuralFeature42",
    ends={
        Property(name="cs_EStructuralFeature44", type=cs_CSConnectionEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="cs_CSConnectionEnd43", type=cs_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_cs_CSRoot_CSElement = Generalization(general=CSElement, specific=cs_CSRoot)
gen_cs_CSElement_ENamedElement = Generalization(general=ENamedElement, specific=cs_CSElement)
gen_cs_CSNode_CSElement = Generalization(general=CSElement, specific=cs_CSNode)
gen_cs_CSConnection_CSElement = Generalization(general=CSElement, specific=cs_CSConnection)
gen_cs_CSText_CSNode = Generalization(general=CSNode, specific=cs_CSText)
gen_cs_CSShape_ENamedElement = Generalization(general=ENamedElement, specific=cs_CSShape)
gen_cs_CSTemplateDescription_CSNode = Generalization(general=CSNode, specific=cs_CSTemplateDescription)

# Domain Model
domain_model = DomainModel(
    name="cs",
    types={cs_CSRoot, CSElement, cs_CSElement, ENamedElement, cs_CSStroke, cs_CSColor, cs_CSNode, cs_CSConnection, cs_CSShape, cs_CSTransform, cs_EObject, cs_EStructuralFeature, cs_CSLayout, cs_CSConnectionEnd, cs_CSText, CSNode, cs_CSPoint, cs_CSTemplateDescription, cs_EClass, CSOrientation, CSFitType},
    associations={stroke0, foreground6, children2, parent4, connections21, background8, shape11, transform13, object15, displayedStructuralFeatures17, layout19, connectionEnds22, points24, containerClass26, theClass27, containerStructuralFeature30, template33, node36, connStructuralFeature39, nodeStructuralFeature42},
    generalizations={gen_cs_CSRoot_CSElement, gen_cs_CSElement_ENamedElement, gen_cs_CSNode_CSElement, gen_cs_CSConnection_CSElement, gen_cs_CSText_CSNode, gen_cs_CSShape_ENamedElement, gen_cs_CSTemplateDescription_CSNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)