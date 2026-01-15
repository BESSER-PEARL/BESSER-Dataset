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
MessageVisibleKind: Enumeration = Enumeration(
    name="MessageVisibleKind",
    literals={
            EnumerationLiteral(name="initiating"),
			EnumerationLiteral(name="non_initiating")
    }
)

ParticipantBandKind: Enumeration = Enumeration(
    name="ParticipantBandKind",
    literals={
            EnumerationLiteral(name="top_initiating"),
			EnumerationLiteral(name="middle_initiating"),
			EnumerationLiteral(name="bottom_initiating"),
			EnumerationLiteral(name="top_non_initiating"),
			EnumerationLiteral(name="middle_non_initiating"),
			EnumerationLiteral(name="bottom_non_initiating")
    }
)

# Classes
di_DocumentRoot = Class(name="di::DocumentRoot")
di_EStringToStringMapEntry = Class(name="di::EStringToStringMapEntry")
di_BPMNDiagram = Class(name="di::BPMNDiagram")
di_BPMNEdge = Class(name="di::BPMNEdge")
di_BPMNLabel = Class(name="di::BPMNLabel")
di_BPMNPlane = Class(name="di::BPMNPlane")
di_BPMNShape = Class(name="di::BPMNShape")
Diagram = Class(name="Diagram")
LabeledEdge = Class(name="LabeledEdge")
di_BaseElement = Class(name="di::BaseElement")
di_BPMNLabelStyle = Class(name="di::BPMNLabelStyle")
Label = Class(name="Label")
Style = Class(name="Style")
di_Font = Class(name="di::Font")
Plane = Class(name="Plane")
LabeledShape = Class(name="LabeledShape")
di_DiagramElement = Class(name="di::DiagramElement")

# di_DocumentRoot class attributes and methods
di_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
di_DocumentRoot.attributes={di_DocumentRoot_mixed}

# di_EStringToStringMapEntry class attributes and methods

# di_BPMNDiagram class attributes and methods

# di_BPMNEdge class attributes and methods
di_BPMNEdge_messageVisibleKind: Property = Property(name="messageVisibleKind", type=StringType)
di_BPMNEdge.attributes={di_BPMNEdge_messageVisibleKind}

# di_BPMNLabel class attributes and methods

# di_BPMNPlane class attributes and methods

# di_BPMNShape class attributes and methods
di_BPMNShape_isExpanded: Property = Property(name="isExpanded", type=BooleanType)
di_BPMNShape_isMessageVisible: Property = Property(name="isMessageVisible", type=BooleanType)
di_BPMNShape_participantBandKind: Property = Property(name="participantBandKind", type=StringType)
di_BPMNShape_isHorizontal: Property = Property(name="isHorizontal", type=BooleanType)
di_BPMNShape_isMarkerVisible: Property = Property(name="isMarkerVisible", type=BooleanType)
di_BPMNShape.attributes={di_BPMNShape_isMessageVisible, di_BPMNShape_participantBandKind, di_BPMNShape_isExpanded, di_BPMNShape_isMarkerVisible, di_BPMNShape_isHorizontal}

# Diagram class attributes and methods

# LabeledEdge class attributes and methods

# di_BaseElement class attributes and methods

# di_BPMNLabelStyle class attributes and methods

# Label class attributes and methods

# Style class attributes and methods

# di_Font class attributes and methods

# Plane class attributes and methods

# LabeledShape class attributes and methods

# di_DiagramElement class attributes and methods

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="di_EStringToStringMapEntry", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot", type=di_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="di_EStringToStringMapEntry3", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot2", type=di_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bPMNDiagram4: BinaryAssociation = BinaryAssociation(
    name="bPMNDiagram4",
    ends={
        Property(name="di_BPMNDiagram", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot5", type=di_BPMNDiagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bPMNEdge6: BinaryAssociation = BinaryAssociation(
    name="bPMNEdge6",
    ends={
        Property(name="di_BPMNEdge", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot7", type=di_BPMNEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bPMNLabel8: BinaryAssociation = BinaryAssociation(
    name="bPMNLabel8",
    ends={
        Property(name="di_BPMNLabel", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot9", type=di_BPMNLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bPMNPlane12: BinaryAssociation = BinaryAssociation(
    name="bPMNPlane12",
    ends={
        Property(name="di_BPMNPlane", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot13", type=di_BPMNPlane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bPMNShape14: BinaryAssociation = BinaryAssociation(
    name="bPMNShape14",
    ends={
        Property(name="di_BPMNShape", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot15", type=di_BPMNShape, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
plane16: BinaryAssociation = BinaryAssociation(
    name="plane16",
    ends={
        Property(name="di_BPMNPlane18", type=di_BPMNDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="di_BPMNDiagram17", type=di_BPMNPlane, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
labelStyle19: BinaryAssociation = BinaryAssociation(
    name="labelStyle19",
    ends={
        Property(name="di_BPMNLabelStyle21", type=di_BPMNDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="di_BPMNDiagram20", type=di_BPMNLabelStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label22: BinaryAssociation = BinaryAssociation(
    name="label22",
    ends={
        Property(name="di_BPMNLabel24", type=di_BPMNEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="di_BPMNEdge23", type=di_BPMNLabel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bpmnElement25: BinaryAssociation = BinaryAssociation(
    name="bpmnElement25",
    ends={
        Property(name="di_BaseElement", type=di_BPMNEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="di_BPMNEdge26", type=di_BaseElement, multiplicity=Multiplicity(0, 1))
    }
)
bPMNLabelStyle10: BinaryAssociation = BinaryAssociation(
    name="bPMNLabelStyle10",
    ends={
        Property(name="di_BPMNLabelStyle", type=di_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="di_DocumentRoot11", type=di_BPMNLabelStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelStyle32: BinaryAssociation = BinaryAssociation(
    name="labelStyle32",
    ends={
        Property(name="di_BPMNLabelStyle34", type=di_BPMNLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="di_BPMNLabel33", type=di_BPMNLabelStyle, multiplicity=Multiplicity(0, 1))
    }
)
font35: BinaryAssociation = BinaryAssociation(
    name="font35",
    ends={
        Property(name="di_Font", type=di_BPMNLabelStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="di_BPMNLabelStyle36", type=di_Font, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bpmnElement37: BinaryAssociation = BinaryAssociation(
    name="bpmnElement37",
    ends={
        Property(name="di_BaseElement39", type=di_BPMNPlane, multiplicity=Multiplicity(1, 1)),
        Property(name="di_BPMNPlane38", type=di_BaseElement, multiplicity=Multiplicity(0, 1))
    }
)
label40: BinaryAssociation = BinaryAssociation(
    name="label40",
    ends={
        Property(name="di_BPMNLabel42", type=di_BPMNShape, multiplicity=Multiplicity(1, 1)),
        Property(name="di_BPMNShape41", type=di_BPMNLabel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bpmnElement43: BinaryAssociation = BinaryAssociation(
    name="bpmnElement43",
    ends={
        Property(name="di_BaseElement45", type=di_BPMNShape, multiplicity=Multiplicity(1, 1)),
        Property(name="di_BPMNShape44", type=di_BaseElement, multiplicity=Multiplicity(0, 1))
    }
)
choreographyActivityShape47: BinaryAssociation = BinaryAssociation(
    name="choreographyActivityShape47",
    ends={
        Property(name="di_BPMNShape48", type=di_BPMNShape, multiplicity=Multiplicity(1, 1)),
        Property(name="di_BPMNShape46", type=di_BPMNShape, multiplicity=Multiplicity(0, 1))
    }
)
sourceElement27: BinaryAssociation = BinaryAssociation(
    name="sourceElement27",
    ends={
        Property(name="di_DiagramElement", type=di_BPMNEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="di_BPMNEdge28", type=di_DiagramElement, multiplicity=Multiplicity(0, 1))
    }
)
targetElement29: BinaryAssociation = BinaryAssociation(
    name="targetElement29",
    ends={
        Property(name="di_DiagramElement31", type=di_BPMNEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="di_BPMNEdge30", type=di_DiagramElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_di_BPMNDiagram_Diagram = Generalization(general=Diagram, specific=di_BPMNDiagram)
gen_di_BPMNEdge_LabeledEdge = Generalization(general=LabeledEdge, specific=di_BPMNEdge)
gen_di_BPMNLabel_Label = Generalization(general=Label, specific=di_BPMNLabel)
gen_di_BPMNLabelStyle_Style = Generalization(general=Style, specific=di_BPMNLabelStyle)
gen_di_BPMNPlane_Plane = Generalization(general=Plane, specific=di_BPMNPlane)
gen_di_BPMNShape_LabeledShape = Generalization(general=LabeledShape, specific=di_BPMNShape)

# Domain Model
domain_model = DomainModel(
    name="di",
    types={di_DocumentRoot, di_EStringToStringMapEntry, di_BPMNDiagram, di_BPMNEdge, di_BPMNLabel, di_BPMNPlane, di_BPMNShape, Diagram, LabeledEdge, di_BaseElement, di_BPMNLabelStyle, Label, Style, di_Font, Plane, LabeledShape, di_DiagramElement, MessageVisibleKind, ParticipantBandKind},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, bPMNDiagram4, bPMNEdge6, bPMNLabel8, bPMNPlane12, bPMNShape14, plane16, labelStyle19, label22, bpmnElement25, bPMNLabelStyle10, labelStyle32, font35, bpmnElement37, label40, bpmnElement43, choreographyActivityShape47, sourceElement27, targetElement29},
    generalizations={gen_di_BPMNDiagram_Diagram, gen_di_BPMNEdge_LabeledEdge, gen_di_BPMNLabel_Label, gen_di_BPMNLabelStyle_Style, gen_di_BPMNPlane_Plane, gen_di_BPMNShape_LabeledShape},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)