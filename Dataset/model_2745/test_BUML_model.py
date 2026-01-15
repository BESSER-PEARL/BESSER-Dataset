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

# Classes
samplemodel_CommonBaseClass = Class(name="samplemodel::CommonBaseClass", is_abstract=True)
samplemodel_LinkAtoC = Class(name="samplemodel::LinkAtoC")
samplemodel_LinkAtoC_Cardinality2 = Class(name="samplemodel::LinkAtoC::Cardinality2")
samplemodel_LinkAtoC_Cardinality1 = Class(name="samplemodel::LinkAtoC::Cardinality1")
samplemodel_LinkAtoA = Class(name="samplemodel::LinkAtoA")
samplemodel_UltimateContainer = Class(name="samplemodel::UltimateContainer")
samplemodel_NodeSrcA = Class(name="samplemodel::NodeSrcA")
CommonBaseClass = Class(name="CommonBaseClass")
samplemodel_NodeTargetB = Class(name="samplemodel::NodeTargetB")
NodeTargetB = Class(name="NodeTargetB")
samplemodel_NodeTargetD = Class(name="samplemodel::NodeTargetD")
samplemodel_Link2Link = Class(name="samplemodel::Link2Link")
samplemodel_LinkFromLink = Class(name="samplemodel::LinkFromLink")
samplemodel_Child = Class(name="samplemodel::Child")
samplemodel_Child2 = Class(name="samplemodel::Child2")
samplemodel_NodeTargetC = Class(name="samplemodel::NodeTargetC")
samplemodel_LinkCrossLink = Class(name="samplemodel::LinkCrossLink")

# samplemodel_CommonBaseClass class attributes and methods

# samplemodel_LinkAtoC class attributes and methods

# samplemodel_LinkAtoC_Cardinality2 class attributes and methods

# samplemodel_LinkAtoC_Cardinality1 class attributes and methods

# samplemodel_LinkAtoA class attributes and methods

# samplemodel_UltimateContainer class attributes and methods
samplemodel_UltimateContainer_diagramAttribute: Property = Property(name="diagramAttribute", type=StringType)
samplemodel_UltimateContainer.attributes={samplemodel_UltimateContainer_diagramAttribute}

# samplemodel_NodeSrcA class attributes and methods
samplemodel_NodeSrcA_label: Property = Property(name="label", type=StringType)
samplemodel_NodeSrcA.attributes={samplemodel_NodeSrcA_label}

# CommonBaseClass class attributes and methods

# samplemodel_NodeTargetB class attributes and methods
samplemodel_NodeTargetB_title: Property = Property(name="title", type=StringType)
samplemodel_NodeTargetB.attributes={samplemodel_NodeTargetB_title}

# NodeTargetB class attributes and methods

# samplemodel_NodeTargetD class attributes and methods

# samplemodel_Link2Link class attributes and methods

# samplemodel_LinkFromLink class attributes and methods

# samplemodel_Child class attributes and methods
samplemodel_Child_childLabel: Property = Property(name="childLabel", type=StringType)
samplemodel_Child.attributes={samplemodel_Child_childLabel}

# samplemodel_Child2 class attributes and methods
samplemodel_Child2_childLabel: Property = Property(name="childLabel", type=StringType)
samplemodel_Child2.attributes={samplemodel_Child2_childLabel}

# samplemodel_NodeTargetC class attributes and methods

# samplemodel_LinkCrossLink class attributes and methods

# Relationships
refLinkToB_Cardinality15: BinaryAssociation = BinaryAssociation(
    name="refLinkToB_Cardinality15",
    ends={
        Property(name="samplemodel_NodeTargetB7", type=samplemodel_NodeSrcA, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeSrcA6", type=samplemodel_NodeTargetB, multiplicity=Multiplicity(0, 1))
    }
)
refLinkToA9: BinaryAssociation = BinaryAssociation(
    name="refLinkToA9",
    ends={
        Property(name="samplemodel_NodeSrcA10", type=samplemodel_NodeSrcA, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeSrcA8", type=samplemodel_NodeSrcA, multiplicity=Multiplicity(0, 9999))
    }
)
classLinkToC11: BinaryAssociation = BinaryAssociation(
    name="classLinkToC11",
    ends={
        Property(name="samplemodel_LinkAtoC", type=samplemodel_NodeSrcA, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeSrcA12", type=samplemodel_LinkAtoC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classLinkToC_Cardinality213: BinaryAssociation = BinaryAssociation(
    name="classLinkToC_Cardinality213",
    ends={
        Property(name="samplemodel_LinkAtoC_Cardinality2", type=samplemodel_NodeSrcA, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeSrcA14", type=samplemodel_LinkAtoC_Cardinality2, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
classLinkToC_Cardinality115: BinaryAssociation = BinaryAssociation(
    name="classLinkToC_Cardinality115",
    ends={
        Property(name="samplemodel_LinkAtoC_Cardinality1", type=samplemodel_NodeSrcA, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeSrcA16", type=samplemodel_LinkAtoC_Cardinality1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
all0: BinaryAssociation = BinaryAssociation(
    name="all0",
    ends={
        Property(name="samplemodel_CommonBaseClass", type=samplemodel_UltimateContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_UltimateContainer", type=samplemodel_CommonBaseClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refLinkToB1: BinaryAssociation = BinaryAssociation(
    name="refLinkToB1",
    ends={
        Property(name="samplemodel_NodeTargetB", type=samplemodel_NodeSrcA, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeSrcA", type=samplemodel_NodeTargetB, multiplicity=Multiplicity(0, 9999))
    }
)
refLinkToB_Cardinality22: BinaryAssociation = BinaryAssociation(
    name="refLinkToB_Cardinality22",
    ends={
        Property(name="samplemodel_NodeTargetB4", type=samplemodel_NodeSrcA, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeSrcA3", type=samplemodel_NodeTargetB, multiplicity=Multiplicity(0, 2))
    }
)
refLinkToLink26: BinaryAssociation = BinaryAssociation(
    name="refLinkToLink26",
    ends={
        Property(name="samplemodel_LinkAtoC27", type=samplemodel_NodeTargetD, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeTargetD", type=samplemodel_LinkAtoC, multiplicity=Multiplicity(0, 3))
    }
)
classLinkToLink28: BinaryAssociation = BinaryAssociation(
    name="classLinkToLink28",
    ends={
        Property(name="samplemodel_Link2Link", type=samplemodel_NodeTargetD, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeTargetD29", type=samplemodel_Link2Link, multiplicity=Multiplicity(0, 3), is_composite=True)
    }
)
refLinkFromLink30: BinaryAssociation = BinaryAssociation(
    name="refLinkFromLink30",
    ends={
        Property(name="samplemodel_NodeTargetD32", type=samplemodel_LinkAtoC, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_LinkAtoC31", type=samplemodel_NodeTargetD, multiplicity=Multiplicity(0, 4))
    }
)
refLinkCrossLink34: BinaryAssociation = BinaryAssociation(
    name="refLinkCrossLink34",
    ends={
        Property(name="samplemodel_LinkAtoC35", type=samplemodel_LinkAtoC, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_LinkAtoC33", type=samplemodel_LinkAtoC, multiplicity=Multiplicity(0, 5))
    }
)
trg36: BinaryAssociation = BinaryAssociation(
    name="trg36",
    ends={
        Property(name="samplemodel_NodeTargetC", type=samplemodel_LinkAtoC, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_LinkAtoC37", type=samplemodel_NodeTargetC, multiplicity=Multiplicity(0, 1))
    }
)
classLinkToA17: BinaryAssociation = BinaryAssociation(
    name="classLinkToA17",
    ends={
        Property(name="samplemodel_LinkAtoA", type=samplemodel_NodeSrcA, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeSrcA18", type=samplemodel_LinkAtoA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children1OfA19: BinaryAssociation = BinaryAssociation(
    name="children1OfA19",
    ends={
        Property(name="samplemodel_Child", type=samplemodel_NodeSrcA, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeSrcA20", type=samplemodel_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children2OfA21: BinaryAssociation = BinaryAssociation(
    name="children2OfA21",
    ends={
        Property(name="samplemodel_Child2", type=samplemodel_NodeSrcA, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeSrcA22", type=samplemodel_Child2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenOfB23: BinaryAssociation = BinaryAssociation(
    name="childrenOfB23",
    ends={
        Property(name="samplemodel_Child25", type=samplemodel_NodeTargetB, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_NodeTargetB24", type=samplemodel_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trg48: BinaryAssociation = BinaryAssociation(
    name="trg48",
    ends={
        Property(name="samplemodel_NodeSrcA50", type=samplemodel_LinkAtoA, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_LinkAtoA49", type=samplemodel_NodeSrcA, multiplicity=Multiplicity(0, 1))
    }
)
innerChildrenOfBChild52: BinaryAssociation = BinaryAssociation(
    name="innerChildrenOfBChild52",
    ends={
        Property(name="samplemodel_Child53", type=samplemodel_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_Child51", type=samplemodel_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trg54: BinaryAssociation = BinaryAssociation(
    name="trg54",
    ends={
        Property(name="samplemodel_LinkAtoC56", type=samplemodel_Link2Link, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_Link2Link55", type=samplemodel_LinkAtoC, multiplicity=Multiplicity(0, 1))
    }
)
trg57: BinaryAssociation = BinaryAssociation(
    name="trg57",
    ends={
        Property(name="samplemodel_NodeTargetD59", type=samplemodel_LinkFromLink, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_LinkFromLink58", type=samplemodel_NodeTargetD, multiplicity=Multiplicity(0, 1))
    }
)
trg60: BinaryAssociation = BinaryAssociation(
    name="trg60",
    ends={
        Property(name="samplemodel_LinkAtoC62", type=samplemodel_LinkCrossLink, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_LinkCrossLink61", type=samplemodel_LinkAtoC, multiplicity=Multiplicity(0, 1))
    }
)
classLinkFromLink38: BinaryAssociation = BinaryAssociation(
    name="classLinkFromLink38",
    ends={
        Property(name="samplemodel_LinkFromLink", type=samplemodel_LinkAtoC, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_LinkAtoC39", type=samplemodel_LinkFromLink, multiplicity=Multiplicity(0, 4), is_composite=True)
    }
)
classLinkCrossLink40: BinaryAssociation = BinaryAssociation(
    name="classLinkCrossLink40",
    ends={
        Property(name="samplemodel_LinkCrossLink", type=samplemodel_LinkAtoC, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_LinkAtoC41", type=samplemodel_LinkCrossLink, multiplicity=Multiplicity(0, 5), is_composite=True)
    }
)
trg42: BinaryAssociation = BinaryAssociation(
    name="trg42",
    ends={
        Property(name="samplemodel_NodeTargetC44", type=samplemodel_LinkAtoC_Cardinality2, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_LinkAtoC_Cardinality243", type=samplemodel_NodeTargetC, multiplicity=Multiplicity(0, 9999))
    }
)
trg45: BinaryAssociation = BinaryAssociation(
    name="trg45",
    ends={
        Property(name="samplemodel_NodeTargetC47", type=samplemodel_LinkAtoC_Cardinality1, multiplicity=Multiplicity(1, 1)),
        Property(name="samplemodel_LinkAtoC_Cardinality146", type=samplemodel_NodeTargetC, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_samplemodel_NodeSrcA_CommonBaseClass = Generalization(general=CommonBaseClass, specific=samplemodel_NodeSrcA)
gen_samplemodel_NodeTargetC_NodeTargetB = Generalization(general=NodeTargetB, specific=samplemodel_NodeTargetC)
gen_samplemodel_NodeTargetD_NodeTargetB = Generalization(general=NodeTargetB, specific=samplemodel_NodeTargetD)
gen_samplemodel_NodeTargetB_CommonBaseClass = Generalization(general=CommonBaseClass, specific=samplemodel_NodeTargetB)

# Domain Model
domain_model = DomainModel(
    name="samplemodel",
    types={samplemodel_CommonBaseClass, samplemodel_LinkAtoC, samplemodel_LinkAtoC_Cardinality2, samplemodel_LinkAtoC_Cardinality1, samplemodel_LinkAtoA, samplemodel_UltimateContainer, samplemodel_NodeSrcA, CommonBaseClass, samplemodel_NodeTargetB, NodeTargetB, samplemodel_NodeTargetD, samplemodel_Link2Link, samplemodel_LinkFromLink, samplemodel_Child, samplemodel_Child2, samplemodel_NodeTargetC, samplemodel_LinkCrossLink},
    associations={refLinkToB_Cardinality15, refLinkToA9, classLinkToC11, classLinkToC_Cardinality213, classLinkToC_Cardinality115, all0, refLinkToB1, refLinkToB_Cardinality22, refLinkToLink26, classLinkToLink28, refLinkFromLink30, refLinkCrossLink34, trg36, classLinkToA17, children1OfA19, children2OfA21, childrenOfB23, trg48, innerChildrenOfBChild52, trg54, trg57, trg60, classLinkFromLink38, classLinkCrossLink40, trg42, trg45},
    generalizations={gen_samplemodel_NodeSrcA_CommonBaseClass, gen_samplemodel_NodeTargetC_NodeTargetB, gen_samplemodel_NodeTargetD_NodeTargetB, gen_samplemodel_NodeTargetB_CommonBaseClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)