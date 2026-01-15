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
jointPackage_Grafcet2PetriNet_SrcElement = Class(name="jointPackage::Grafcet2PetriNet::SrcElement", is_abstract=True)
jointPackage_Grafcet2PetriNet_JointMM = Class(name="jointPackage::Grafcet2PetriNet::JointMM")
jointPackage_Grafcet2PetriNet_SrcGrafcet = Class(name="jointPackage::Grafcet2PetriNet::SrcGrafcet")
jointPackage_Grafcet2PetriNet_TrgPetriNet = Class(name="jointPackage::Grafcet2PetriNet::TrgPetriNet")
jointPackage_Grafcet2PetriNet_SrcLocatedElement = Class(name="jointPackage::Grafcet2PetriNet::SrcLocatedElement", is_abstract=True)
jointPackage_Grafcet2PetriNet_SrcNamedElement = Class(name="jointPackage::Grafcet2PetriNet::SrcNamedElement", is_abstract=True)
SrcLocatedElement = Class(name="SrcLocatedElement")
SrcNamedElement = Class(name="SrcNamedElement")
jointPackage_Grafcet2PetriNet_SrcTransitionToStep = Class(name="jointPackage::Grafcet2PetriNet::SrcTransitionToStep")
jointPackage_Grafcet2PetriNet_SrcConnection = Class(name="jointPackage::Grafcet2PetriNet::SrcConnection", is_abstract=True)
jointPackage_Grafcet2PetriNet_SrcStep = Class(name="jointPackage::Grafcet2PetriNet::SrcStep")
SrcElement = Class(name="SrcElement")
SrcConnection = Class(name="SrcConnection")
jointPackage_Grafcet2PetriNet_SrcStepToTransition = Class(name="jointPackage::Grafcet2PetriNet::SrcStepToTransition")
jointPackage_Grafcet2PetriNet_SrcTransition = Class(name="jointPackage::Grafcet2PetriNet::SrcTransition")
jointPackage_Grafcet2PetriNet_TrgNamedElement = Class(name="jointPackage::Grafcet2PetriNet::TrgNamedElement", is_abstract=True)
TrgLocatedElement = Class(name="TrgLocatedElement")
jointPackage_Grafcet2PetriNet_TrgLocatedElement = Class(name="jointPackage::Grafcet2PetriNet::TrgLocatedElement", is_abstract=True)
jointPackage_Grafcet2PetriNet_TrgTransitionToPlace = Class(name="jointPackage::Grafcet2PetriNet::TrgTransitionToPlace")
TrgNamedElement = Class(name="TrgNamedElement")
jointPackage_Grafcet2PetriNet_TrgElement = Class(name="jointPackage::Grafcet2PetriNet::TrgElement", is_abstract=True)
jointPackage_Grafcet2PetriNet_TrgArc = Class(name="jointPackage::Grafcet2PetriNet::TrgArc", is_abstract=True)
jointPackage_Grafcet2PetriNet_TrgPlace = Class(name="jointPackage::Grafcet2PetriNet::TrgPlace")
TrgElement = Class(name="TrgElement")
TrgArc = Class(name="TrgArc")
jointPackage_Grafcet2PetriNet_TrgPlaceToTransition = Class(name="jointPackage::Grafcet2PetriNet::TrgPlaceToTransition")
jointPackage_Grafcet2PetriNet_TrgTransition = Class(name="jointPackage::Grafcet2PetriNet::TrgTransition")

# jointPackage_Grafcet2PetriNet_SrcElement class attributes and methods

# jointPackage_Grafcet2PetriNet_JointMM class attributes and methods

# jointPackage_Grafcet2PetriNet_SrcGrafcet class attributes and methods

# jointPackage_Grafcet2PetriNet_TrgPetriNet class attributes and methods

# jointPackage_Grafcet2PetriNet_SrcLocatedElement class attributes and methods
jointPackage_Grafcet2PetriNet_SrcLocatedElement_location: Property = Property(name="location", type=StringType)
jointPackage_Grafcet2PetriNet_SrcLocatedElement.attributes={jointPackage_Grafcet2PetriNet_SrcLocatedElement_location}

# jointPackage_Grafcet2PetriNet_SrcNamedElement class attributes and methods
jointPackage_Grafcet2PetriNet_SrcNamedElement_name: Property = Property(name="name", type=StringType)
jointPackage_Grafcet2PetriNet_SrcNamedElement.attributes={jointPackage_Grafcet2PetriNet_SrcNamedElement_name}

# SrcLocatedElement class attributes and methods

# SrcNamedElement class attributes and methods

# jointPackage_Grafcet2PetriNet_SrcTransitionToStep class attributes and methods

# jointPackage_Grafcet2PetriNet_SrcConnection class attributes and methods

# jointPackage_Grafcet2PetriNet_SrcStep class attributes and methods
jointPackage_Grafcet2PetriNet_SrcStep_isInitial: Property = Property(name="isInitial", type=BooleanType)
jointPackage_Grafcet2PetriNet_SrcStep_isActive: Property = Property(name="isActive", type=BooleanType)
jointPackage_Grafcet2PetriNet_SrcStep_action: Property = Property(name="action", type=StringType)
jointPackage_Grafcet2PetriNet_SrcStep.attributes={jointPackage_Grafcet2PetriNet_SrcStep_action, jointPackage_Grafcet2PetriNet_SrcStep_isActive, jointPackage_Grafcet2PetriNet_SrcStep_isInitial}

# SrcElement class attributes and methods

# SrcConnection class attributes and methods

# jointPackage_Grafcet2PetriNet_SrcStepToTransition class attributes and methods

# jointPackage_Grafcet2PetriNet_SrcTransition class attributes and methods
jointPackage_Grafcet2PetriNet_SrcTransition_condition: Property = Property(name="condition", type=StringType)
jointPackage_Grafcet2PetriNet_SrcTransition.attributes={jointPackage_Grafcet2PetriNet_SrcTransition_condition}

# jointPackage_Grafcet2PetriNet_TrgNamedElement class attributes and methods
jointPackage_Grafcet2PetriNet_TrgNamedElement_name: Property = Property(name="name", type=StringType)
jointPackage_Grafcet2PetriNet_TrgNamedElement.attributes={jointPackage_Grafcet2PetriNet_TrgNamedElement_name}

# TrgLocatedElement class attributes and methods

# jointPackage_Grafcet2PetriNet_TrgLocatedElement class attributes and methods
jointPackage_Grafcet2PetriNet_TrgLocatedElement_location: Property = Property(name="location", type=StringType)
jointPackage_Grafcet2PetriNet_TrgLocatedElement.attributes={jointPackage_Grafcet2PetriNet_TrgLocatedElement_location}

# jointPackage_Grafcet2PetriNet_TrgTransitionToPlace class attributes and methods

# TrgNamedElement class attributes and methods

# jointPackage_Grafcet2PetriNet_TrgElement class attributes and methods

# jointPackage_Grafcet2PetriNet_TrgArc class attributes and methods
jointPackage_Grafcet2PetriNet_TrgArc_weight: Property = Property(name="weight", type=IntegerType)
jointPackage_Grafcet2PetriNet_TrgArc.attributes={jointPackage_Grafcet2PetriNet_TrgArc_weight}

# jointPackage_Grafcet2PetriNet_TrgPlace class attributes and methods

# TrgElement class attributes and methods

# TrgArc class attributes and methods

# jointPackage_Grafcet2PetriNet_TrgPlaceToTransition class attributes and methods

# jointPackage_Grafcet2PetriNet_TrgTransition class attributes and methods

# Relationships
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="SrcElement", type=jointPackage_Grafcet2PetriNet_SrcGrafcet, multiplicity=Multiplicity(1, 1)),
        Property(name="grafcet", type=jointPackage_Grafcet2PetriNet_SrcElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceRoot0: BinaryAssociation = BinaryAssociation(
    name="sourceRoot0",
    ends={
        Property(name="jointPackage_Grafcet2PetriNet_SrcGrafcet", type=jointPackage_Grafcet2PetriNet_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Grafcet2PetriNet_JointMM", type=jointPackage_Grafcet2PetriNet_SrcGrafcet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetRoot1: BinaryAssociation = BinaryAssociation(
    name="targetRoot1",
    ends={
        Property(name="jointPackage_Grafcet2PetriNet_TrgPetriNet", type=jointPackage_Grafcet2PetriNet_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Grafcet2PetriNet_JointMM2", type=jointPackage_Grafcet2PetriNet_TrgPetriNet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
incomingConnections7: BinaryAssociation = BinaryAssociation(
    name="incomingConnections7",
    ends={
        Property(name="SrcTransitionToStep", type=jointPackage_Grafcet2PetriNet_SrcStep, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=jointPackage_Grafcet2PetriNet_SrcTransitionToStep, multiplicity=Multiplicity(0, 9999))
    }
)
connections4: BinaryAssociation = BinaryAssociation(
    name="connections4",
    ends={
        Property(name="SrcConnection", type=jointPackage_Grafcet2PetriNet_SrcGrafcet, multiplicity=Multiplicity(1, 1)),
        Property(name="grafcet5", type=jointPackage_Grafcet2PetriNet_SrcConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
grafcet6: BinaryAssociation = BinaryAssociation(
    name="grafcet6",
    ends={
        Property(name="SrcGrafcet", type=jointPackage_Grafcet2PetriNet_SrcElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=jointPackage_Grafcet2PetriNet_SrcGrafcet, multiplicity=Multiplicity(1, 1))
    }
)
outgoingConnections8: BinaryAssociation = BinaryAssociation(
    name="outgoingConnections8",
    ends={
        Property(name="SrcStepToTransition", type=jointPackage_Grafcet2PetriNet_SrcStep, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=jointPackage_Grafcet2PetriNet_SrcStepToTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingConnections9: BinaryAssociation = BinaryAssociation(
    name="incomingConnections9",
    ends={
        Property(name="SrcStepToTransition11", type=jointPackage_Grafcet2PetriNet_SrcTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="to10", type=jointPackage_Grafcet2PetriNet_SrcStepToTransition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingConnections12: BinaryAssociation = BinaryAssociation(
    name="outgoingConnections12",
    ends={
        Property(name="SrcTransitionToStep14", type=jointPackage_Grafcet2PetriNet_SrcTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="from13", type=jointPackage_Grafcet2PetriNet_SrcTransitionToStep, multiplicity=Multiplicity(0, 9999))
    }
)
grafcet15: BinaryAssociation = BinaryAssociation(
    name="grafcet15",
    ends={
        Property(name="SrcGrafcet16", type=jointPackage_Grafcet2PetriNet_SrcConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connections", type=jointPackage_Grafcet2PetriNet_SrcGrafcet, multiplicity=Multiplicity(1, 1))
    }
)
from17: BinaryAssociation = BinaryAssociation(
    name="from17",
    ends={
        Property(name="SrcStep", type=jointPackage_Grafcet2PetriNet_SrcStepToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingConnections", type=jointPackage_Grafcet2PetriNet_SrcStep, multiplicity=Multiplicity(1, 1))
    }
)
to18: BinaryAssociation = BinaryAssociation(
    name="to18",
    ends={
        Property(name="SrcTransition", type=jointPackage_Grafcet2PetriNet_SrcStepToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingConnections", type=jointPackage_Grafcet2PetriNet_SrcTransition, multiplicity=Multiplicity(1, 1))
    }
)
from19: BinaryAssociation = BinaryAssociation(
    name="from19",
    ends={
        Property(name="SrcTransition21", type=jointPackage_Grafcet2PetriNet_SrcTransitionToStep, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingConnections20", type=jointPackage_Grafcet2PetriNet_SrcTransition, multiplicity=Multiplicity(1, 1))
    }
)
to22: BinaryAssociation = BinaryAssociation(
    name="to22",
    ends={
        Property(name="SrcStep24", type=jointPackage_Grafcet2PetriNet_SrcTransitionToStep, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingConnections23", type=jointPackage_Grafcet2PetriNet_SrcStep, multiplicity=Multiplicity(1, 1))
    }
)
incomingArc30: BinaryAssociation = BinaryAssociation(
    name="incomingArc30",
    ends={
        Property(name="TrgTransitionToPlace", type=jointPackage_Grafcet2PetriNet_TrgPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="to31", type=jointPackage_Grafcet2PetriNet_TrgTransitionToPlace, multiplicity=Multiplicity(0, 9999))
    }
)
elements25: BinaryAssociation = BinaryAssociation(
    name="elements25",
    ends={
        Property(name="TrgElement", type=jointPackage_Grafcet2PetriNet_TrgPetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=jointPackage_Grafcet2PetriNet_TrgElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs26: BinaryAssociation = BinaryAssociation(
    name="arcs26",
    ends={
        Property(name="TrgArc", type=jointPackage_Grafcet2PetriNet_TrgPetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net27", type=jointPackage_Grafcet2PetriNet_TrgArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net28: BinaryAssociation = BinaryAssociation(
    name="net28",
    ends={
        Property(name="TrgPetriNet", type=jointPackage_Grafcet2PetriNet_TrgElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements29", type=jointPackage_Grafcet2PetriNet_TrgPetriNet, multiplicity=Multiplicity(1, 1))
    }
)
outgoingArc32: BinaryAssociation = BinaryAssociation(
    name="outgoingArc32",
    ends={
        Property(name="TrgPlaceToTransition", type=jointPackage_Grafcet2PetriNet_TrgPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="from33", type=jointPackage_Grafcet2PetriNet_TrgPlaceToTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingArc34: BinaryAssociation = BinaryAssociation(
    name="incomingArc34",
    ends={
        Property(name="TrgPlaceToTransition36", type=jointPackage_Grafcet2PetriNet_TrgTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="to35", type=jointPackage_Grafcet2PetriNet_TrgPlaceToTransition, multiplicity=Multiplicity(1, 9999))
    }
)
outgoingArc37: BinaryAssociation = BinaryAssociation(
    name="outgoingArc37",
    ends={
        Property(name="TrgTransitionToPlace39", type=jointPackage_Grafcet2PetriNet_TrgTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="from38", type=jointPackage_Grafcet2PetriNet_TrgTransitionToPlace, multiplicity=Multiplicity(1, 9999))
    }
)
net40: BinaryAssociation = BinaryAssociation(
    name="net40",
    ends={
        Property(name="TrgPetriNet41", type=jointPackage_Grafcet2PetriNet_TrgArc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=jointPackage_Grafcet2PetriNet_TrgPetriNet, multiplicity=Multiplicity(1, 1))
    }
)
from42: BinaryAssociation = BinaryAssociation(
    name="from42",
    ends={
        Property(name="TrgPlace", type=jointPackage_Grafcet2PetriNet_TrgPlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArc", type=jointPackage_Grafcet2PetriNet_TrgPlace, multiplicity=Multiplicity(1, 1))
    }
)
to43: BinaryAssociation = BinaryAssociation(
    name="to43",
    ends={
        Property(name="TrgTransition", type=jointPackage_Grafcet2PetriNet_TrgPlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc", type=jointPackage_Grafcet2PetriNet_TrgTransition, multiplicity=Multiplicity(1, 1))
    }
)
from44: BinaryAssociation = BinaryAssociation(
    name="from44",
    ends={
        Property(name="TrgTransition46", type=jointPackage_Grafcet2PetriNet_TrgTransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArc45", type=jointPackage_Grafcet2PetriNet_TrgTransition, multiplicity=Multiplicity(1, 1))
    }
)
to47: BinaryAssociation = BinaryAssociation(
    name="to47",
    ends={
        Property(name="TrgPlace49", type=jointPackage_Grafcet2PetriNet_TrgTransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc48", type=jointPackage_Grafcet2PetriNet_TrgPlace, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_jointPackage_Grafcet2PetriNet_SrcNamedElement_SrcLocatedElement = Generalization(general=SrcLocatedElement, specific=jointPackage_Grafcet2PetriNet_SrcNamedElement)
gen_jointPackage_Grafcet2PetriNet_SrcGrafcet_SrcNamedElement = Generalization(general=SrcNamedElement, specific=jointPackage_Grafcet2PetriNet_SrcGrafcet)
gen_jointPackage_Grafcet2PetriNet_SrcElement_SrcNamedElement = Generalization(general=SrcNamedElement, specific=jointPackage_Grafcet2PetriNet_SrcElement)
gen_jointPackage_Grafcet2PetriNet_SrcStep_SrcElement = Generalization(general=SrcElement, specific=jointPackage_Grafcet2PetriNet_SrcStep)
gen_jointPackage_Grafcet2PetriNet_SrcStepToTransition_SrcConnection = Generalization(general=SrcConnection, specific=jointPackage_Grafcet2PetriNet_SrcStepToTransition)
gen_jointPackage_Grafcet2PetriNet_SrcTransition_SrcElement = Generalization(general=SrcElement, specific=jointPackage_Grafcet2PetriNet_SrcTransition)
gen_jointPackage_Grafcet2PetriNet_SrcConnection_SrcNamedElement = Generalization(general=SrcNamedElement, specific=jointPackage_Grafcet2PetriNet_SrcConnection)
gen_jointPackage_Grafcet2PetriNet_SrcTransitionToStep_SrcConnection = Generalization(general=SrcConnection, specific=jointPackage_Grafcet2PetriNet_SrcTransitionToStep)
gen_jointPackage_Grafcet2PetriNet_TrgNamedElement_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_Grafcet2PetriNet_TrgNamedElement)
gen_jointPackage_Grafcet2PetriNet_TrgPetriNet_TrgNamedElement = Generalization(general=TrgNamedElement, specific=jointPackage_Grafcet2PetriNet_TrgPetriNet)
gen_jointPackage_Grafcet2PetriNet_TrgElement_TrgNamedElement = Generalization(general=TrgNamedElement, specific=jointPackage_Grafcet2PetriNet_TrgElement)
gen_jointPackage_Grafcet2PetriNet_TrgPlace_TrgElement = Generalization(general=TrgElement, specific=jointPackage_Grafcet2PetriNet_TrgPlace)
gen_jointPackage_Grafcet2PetriNet_TrgPlaceToTransition_TrgArc = Generalization(general=TrgArc, specific=jointPackage_Grafcet2PetriNet_TrgPlaceToTransition)
gen_jointPackage_Grafcet2PetriNet_TrgTransition_TrgElement = Generalization(general=TrgElement, specific=jointPackage_Grafcet2PetriNet_TrgTransition)
gen_jointPackage_Grafcet2PetriNet_TrgArc_TrgNamedElement = Generalization(general=TrgNamedElement, specific=jointPackage_Grafcet2PetriNet_TrgArc)
gen_jointPackage_Grafcet2PetriNet_TrgTransitionToPlace_TrgArc = Generalization(general=TrgArc, specific=jointPackage_Grafcet2PetriNet_TrgTransitionToPlace)

# Domain Model
domain_model = DomainModel(
    name="jointPackage_Grafcet2PetriNet",
    types={jointPackage_Grafcet2PetriNet_SrcElement, jointPackage_Grafcet2PetriNet_JointMM, jointPackage_Grafcet2PetriNet_SrcGrafcet, jointPackage_Grafcet2PetriNet_TrgPetriNet, jointPackage_Grafcet2PetriNet_SrcLocatedElement, jointPackage_Grafcet2PetriNet_SrcNamedElement, SrcLocatedElement, SrcNamedElement, jointPackage_Grafcet2PetriNet_SrcTransitionToStep, jointPackage_Grafcet2PetriNet_SrcConnection, jointPackage_Grafcet2PetriNet_SrcStep, SrcElement, SrcConnection, jointPackage_Grafcet2PetriNet_SrcStepToTransition, jointPackage_Grafcet2PetriNet_SrcTransition, jointPackage_Grafcet2PetriNet_TrgNamedElement, TrgLocatedElement, jointPackage_Grafcet2PetriNet_TrgLocatedElement, jointPackage_Grafcet2PetriNet_TrgTransitionToPlace, TrgNamedElement, jointPackage_Grafcet2PetriNet_TrgElement, jointPackage_Grafcet2PetriNet_TrgArc, jointPackage_Grafcet2PetriNet_TrgPlace, TrgElement, TrgArc, jointPackage_Grafcet2PetriNet_TrgPlaceToTransition, jointPackage_Grafcet2PetriNet_TrgTransition},
    associations={elements3, sourceRoot0, targetRoot1, incomingConnections7, connections4, grafcet6, outgoingConnections8, incomingConnections9, outgoingConnections12, grafcet15, from17, to18, from19, to22, incomingArc30, elements25, arcs26, net28, outgoingArc32, incomingArc34, outgoingArc37, net40, from42, to43, from44, to47},
    generalizations={gen_jointPackage_Grafcet2PetriNet_SrcNamedElement_SrcLocatedElement, gen_jointPackage_Grafcet2PetriNet_SrcGrafcet_SrcNamedElement, gen_jointPackage_Grafcet2PetriNet_SrcElement_SrcNamedElement, gen_jointPackage_Grafcet2PetriNet_SrcStep_SrcElement, gen_jointPackage_Grafcet2PetriNet_SrcStepToTransition_SrcConnection, gen_jointPackage_Grafcet2PetriNet_SrcTransition_SrcElement, gen_jointPackage_Grafcet2PetriNet_SrcConnection_SrcNamedElement, gen_jointPackage_Grafcet2PetriNet_SrcTransitionToStep_SrcConnection, gen_jointPackage_Grafcet2PetriNet_TrgNamedElement_TrgLocatedElement, gen_jointPackage_Grafcet2PetriNet_TrgPetriNet_TrgNamedElement, gen_jointPackage_Grafcet2PetriNet_TrgElement_TrgNamedElement, gen_jointPackage_Grafcet2PetriNet_TrgPlace_TrgElement, gen_jointPackage_Grafcet2PetriNet_TrgPlaceToTransition_TrgArc, gen_jointPackage_Grafcet2PetriNet_TrgTransition_TrgElement, gen_jointPackage_Grafcet2PetriNet_TrgArc_TrgNamedElement, gen_jointPackage_Grafcet2PetriNet_TrgTransitionToPlace_TrgArc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)