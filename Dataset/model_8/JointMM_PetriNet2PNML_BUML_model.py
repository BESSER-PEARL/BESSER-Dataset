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
jointPackage_PetriNet2PNML_SrcNamedElement = Class(name="jointPackage::PetriNet2PNML::SrcNamedElement", is_abstract=True)
SrcLocatedElement = Class(name="SrcLocatedElement")
SrcNamedElement = Class(name="SrcNamedElement")
jointPackage_PetriNet2PNML_SrcElement = Class(name="jointPackage::PetriNet2PNML::SrcElement", is_abstract=True)
jointPackage_PetriNet2PNML_SrcArc = Class(name="jointPackage::PetriNet2PNML::SrcArc", is_abstract=True)
jointPackage_PetriNet2PNML_JointMM = Class(name="jointPackage::PetriNet2PNML::JointMM")
jointPackage_PetriNet2PNML_SrcPetriNet = Class(name="jointPackage::PetriNet2PNML::SrcPetriNet")
jointPackage_PetriNet2PNML_TrgPNMLDocument = Class(name="jointPackage::PetriNet2PNML::TrgPNMLDocument")
jointPackage_PetriNet2PNML_SrcLocatedElement = Class(name="jointPackage::PetriNet2PNML::SrcLocatedElement", is_abstract=True)
TrgLocatedElement = Class(name="TrgLocatedElement")
jointPackage_PetriNet2PNML_TrgURI = Class(name="jointPackage::PetriNet2PNML::TrgURI")
jointPackage_PetriNet2PNML_TrgNetElement = Class(name="jointPackage::PetriNet2PNML::TrgNetElement")
jointPackage_PetriNet2PNML_TrgLocatedElement = Class(name="jointPackage::PetriNet2PNML::TrgLocatedElement", is_abstract=True)
jointPackage_PetriNet2PNML_TrgIdedElement = Class(name="jointPackage::PetriNet2PNML::TrgIdedElement", is_abstract=True)
jointPackage_PetriNet2PNML_SrcPlace = Class(name="jointPackage::PetriNet2PNML::SrcPlace")
SrcElement = Class(name="SrcElement")
jointPackage_PetriNet2PNML_SrcTransitionToPlace = Class(name="jointPackage::PetriNet2PNML::SrcTransitionToPlace")
jointPackage_PetriNet2PNML_SrcPlaceToTransition = Class(name="jointPackage::PetriNet2PNML::SrcPlaceToTransition")
jointPackage_PetriNet2PNML_SrcTransition = Class(name="jointPackage::PetriNet2PNML::SrcTransition")
SrcArc = Class(name="SrcArc")
jointPackage_PetriNet2PNML_TrgArc = Class(name="jointPackage::PetriNet2PNML::TrgArc")
jointPackage_PetriNet2PNML_TrgPlace = Class(name="jointPackage::PetriNet2PNML::TrgPlace")
TrgNetContentElement = Class(name="TrgNetContentElement")
jointPackage_PetriNet2PNML_TrgTransition = Class(name="jointPackage::PetriNet2PNML::TrgTransition")
TrgIdedElement = Class(name="TrgIdedElement")
jointPackage_PetriNet2PNML_TrgNetContent = Class(name="jointPackage::PetriNet2PNML::TrgNetContent", is_abstract=True)
jointPackage_PetriNet2PNML_TrgName = Class(name="jointPackage::PetriNet2PNML::TrgName")
jointPackage_PetriNet2PNML_TrgLabeledElement = Class(name="jointPackage::PetriNet2PNML::TrgLabeledElement", is_abstract=True)
jointPackage_PetriNet2PNML_TrgLabel = Class(name="jointPackage::PetriNet2PNML::TrgLabel")
TrgLabeledElement = Class(name="TrgLabeledElement")
jointPackage_PetriNet2PNML_TrgNetContentElement = Class(name="jointPackage::PetriNet2PNML::TrgNetContentElement", is_abstract=True)
TrgNetContent = Class(name="TrgNetContent")

# jointPackage_PetriNet2PNML_SrcNamedElement class attributes and methods
jointPackage_PetriNet2PNML_SrcNamedElement_name: Property = Property(name="name", type=StringType)
jointPackage_PetriNet2PNML_SrcNamedElement.attributes={jointPackage_PetriNet2PNML_SrcNamedElement_name}

# SrcLocatedElement class attributes and methods

# SrcNamedElement class attributes and methods

# jointPackage_PetriNet2PNML_SrcElement class attributes and methods

# jointPackage_PetriNet2PNML_SrcArc class attributes and methods
jointPackage_PetriNet2PNML_SrcArc_weight: Property = Property(name="weight", type=IntegerType)
jointPackage_PetriNet2PNML_SrcArc.attributes={jointPackage_PetriNet2PNML_SrcArc_weight}

# jointPackage_PetriNet2PNML_JointMM class attributes and methods

# jointPackage_PetriNet2PNML_SrcPetriNet class attributes and methods

# jointPackage_PetriNet2PNML_TrgPNMLDocument class attributes and methods

# jointPackage_PetriNet2PNML_SrcLocatedElement class attributes and methods
jointPackage_PetriNet2PNML_SrcLocatedElement_location: Property = Property(name="location", type=StringType)
jointPackage_PetriNet2PNML_SrcLocatedElement.attributes={jointPackage_PetriNet2PNML_SrcLocatedElement_location}

# TrgLocatedElement class attributes and methods

# jointPackage_PetriNet2PNML_TrgURI class attributes and methods
jointPackage_PetriNet2PNML_TrgURI_value: Property = Property(name="value", type=StringType)
jointPackage_PetriNet2PNML_TrgURI.attributes={jointPackage_PetriNet2PNML_TrgURI_value}

# jointPackage_PetriNet2PNML_TrgNetElement class attributes and methods

# jointPackage_PetriNet2PNML_TrgLocatedElement class attributes and methods
jointPackage_PetriNet2PNML_TrgLocatedElement_location: Property = Property(name="location", type=StringType)
jointPackage_PetriNet2PNML_TrgLocatedElement.attributes={jointPackage_PetriNet2PNML_TrgLocatedElement_location}

# jointPackage_PetriNet2PNML_TrgIdedElement class attributes and methods
jointPackage_PetriNet2PNML_TrgIdedElement_id: Property = Property(name="id", type=StringType)
jointPackage_PetriNet2PNML_TrgIdedElement.attributes={jointPackage_PetriNet2PNML_TrgIdedElement_id}

# jointPackage_PetriNet2PNML_SrcPlace class attributes and methods

# SrcElement class attributes and methods

# jointPackage_PetriNet2PNML_SrcTransitionToPlace class attributes and methods

# jointPackage_PetriNet2PNML_SrcPlaceToTransition class attributes and methods

# jointPackage_PetriNet2PNML_SrcTransition class attributes and methods

# SrcArc class attributes and methods

# jointPackage_PetriNet2PNML_TrgArc class attributes and methods

# jointPackage_PetriNet2PNML_TrgPlace class attributes and methods

# TrgNetContentElement class attributes and methods

# jointPackage_PetriNet2PNML_TrgTransition class attributes and methods

# TrgIdedElement class attributes and methods

# jointPackage_PetriNet2PNML_TrgNetContent class attributes and methods

# jointPackage_PetriNet2PNML_TrgName class attributes and methods

# jointPackage_PetriNet2PNML_TrgLabeledElement class attributes and methods

# jointPackage_PetriNet2PNML_TrgLabel class attributes and methods
jointPackage_PetriNet2PNML_TrgLabel_text: Property = Property(name="text", type=StringType)
jointPackage_PetriNet2PNML_TrgLabel.attributes={jointPackage_PetriNet2PNML_TrgLabel_text}

# TrgLabeledElement class attributes and methods

# jointPackage_PetriNet2PNML_TrgNetContentElement class attributes and methods

# TrgNetContent class attributes and methods

# Relationships
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="SrcElement", type=jointPackage_PetriNet2PNML_SrcPetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=jointPackage_PetriNet2PNML_SrcElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs4: BinaryAssociation = BinaryAssociation(
    name="arcs4",
    ends={
        Property(name="SrcArc", type=jointPackage_PetriNet2PNML_SrcPetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net5", type=jointPackage_PetriNet2PNML_SrcArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net6: BinaryAssociation = BinaryAssociation(
    name="net6",
    ends={
        Property(name="SrcPetriNet", type=jointPackage_PetriNet2PNML_SrcElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=jointPackage_PetriNet2PNML_SrcPetriNet, multiplicity=Multiplicity(1, 1))
    }
)
sourceRoot0: BinaryAssociation = BinaryAssociation(
    name="sourceRoot0",
    ends={
        Property(name="jointPackage_PetriNet2PNML_SrcPetriNet", type=jointPackage_PetriNet2PNML_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_PetriNet2PNML_JointMM", type=jointPackage_PetriNet2PNML_SrcPetriNet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetRoot1: BinaryAssociation = BinaryAssociation(
    name="targetRoot1",
    ends={
        Property(name="jointPackage_PetriNet2PNML_TrgPNMLDocument", type=jointPackage_PetriNet2PNML_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_PetriNet2PNML_JointMM2", type=jointPackage_PetriNet2PNML_TrgPNMLDocument, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from19: BinaryAssociation = BinaryAssociation(
    name="from19",
    ends={
        Property(name="outgoingArc20", type=jointPackage_PetriNet2PNML_SrcTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="SrcTransition21", type=jointPackage_PetriNet2PNML_SrcTransitionToPlace, multiplicity=Multiplicity(1, 1))
    }
)
to22: BinaryAssociation = BinaryAssociation(
    name="to22",
    ends={
        Property(name="SrcPlace24", type=jointPackage_PetriNet2PNML_SrcTransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc23", type=jointPackage_PetriNet2PNML_SrcPlace, multiplicity=Multiplicity(1, 1))
    }
)
xmlns25: BinaryAssociation = BinaryAssociation(
    name="xmlns25",
    ends={
        Property(name="jointPackage_PetriNet2PNML_TrgURI", type=jointPackage_PetriNet2PNML_TrgPNMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_PetriNet2PNML_TrgPNMLDocument26", type=jointPackage_PetriNet2PNML_TrgURI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nets27: BinaryAssociation = BinaryAssociation(
    name="nets27",
    ends={
        Property(name="jointPackage_PetriNet2PNML_TrgNetElement", type=jointPackage_PetriNet2PNML_TrgPNMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_PetriNet2PNML_TrgPNMLDocument28", type=jointPackage_PetriNet2PNML_TrgNetElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
incomingArc7: BinaryAssociation = BinaryAssociation(
    name="incomingArc7",
    ends={
        Property(name="SrcTransitionToPlace", type=jointPackage_PetriNet2PNML_SrcPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=jointPackage_PetriNet2PNML_SrcTransitionToPlace, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingArc8: BinaryAssociation = BinaryAssociation(
    name="outgoingArc8",
    ends={
        Property(name="SrcPlaceToTransition", type=jointPackage_PetriNet2PNML_SrcPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=jointPackage_PetriNet2PNML_SrcPlaceToTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingArc9: BinaryAssociation = BinaryAssociation(
    name="incomingArc9",
    ends={
        Property(name="SrcPlaceToTransition11", type=jointPackage_PetriNet2PNML_SrcTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="to10", type=jointPackage_PetriNet2PNML_SrcPlaceToTransition, multiplicity=Multiplicity(1, 9999))
    }
)
outgoingArc12: BinaryAssociation = BinaryAssociation(
    name="outgoingArc12",
    ends={
        Property(name="SrcTransitionToPlace14", type=jointPackage_PetriNet2PNML_SrcTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="from13", type=jointPackage_PetriNet2PNML_SrcTransitionToPlace, multiplicity=Multiplicity(1, 9999))
    }
)
net15: BinaryAssociation = BinaryAssociation(
    name="net15",
    ends={
        Property(name="SrcPetriNet16", type=jointPackage_PetriNet2PNML_SrcArc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=jointPackage_PetriNet2PNML_SrcPetriNet, multiplicity=Multiplicity(1, 1))
    }
)
from17: BinaryAssociation = BinaryAssociation(
    name="from17",
    ends={
        Property(name="SrcPlace", type=jointPackage_PetriNet2PNML_SrcPlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArc", type=jointPackage_PetriNet2PNML_SrcPlace, multiplicity=Multiplicity(1, 1))
    }
)
to18: BinaryAssociation = BinaryAssociation(
    name="to18",
    ends={
        Property(name="SrcTransition", type=jointPackage_PetriNet2PNML_SrcPlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc", type=jointPackage_PetriNet2PNML_SrcTransition, multiplicity=Multiplicity(1, 1))
    }
)
source40: BinaryAssociation = BinaryAssociation(
    name="source40",
    ends={
        Property(name="jointPackage_PetriNet2PNML_TrgNetContentElement", type=jointPackage_PetriNet2PNML_TrgArc, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_PetriNet2PNML_TrgArc", type=jointPackage_PetriNet2PNML_TrgNetContentElement, multiplicity=Multiplicity(1, 1))
    }
)
target41: BinaryAssociation = BinaryAssociation(
    name="target41",
    ends={
        Property(name="jointPackage_PetriNet2PNML_TrgNetContentElement43", type=jointPackage_PetriNet2PNML_TrgArc, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_PetriNet2PNML_TrgArc42", type=jointPackage_PetriNet2PNML_TrgNetContentElement, multiplicity=Multiplicity(1, 1))
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="jointPackage_PetriNet2PNML_TrgURI31", type=jointPackage_PetriNet2PNML_TrgNetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_PetriNet2PNML_TrgNetElement30", type=jointPackage_PetriNet2PNML_TrgURI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contents32: BinaryAssociation = BinaryAssociation(
    name="contents32",
    ends={
        Property(name="jointPackage_PetriNet2PNML_TrgNetContent", type=jointPackage_PetriNet2PNML_TrgNetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_PetriNet2PNML_TrgNetElement33", type=jointPackage_PetriNet2PNML_TrgNetContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name34: BinaryAssociation = BinaryAssociation(
    name="name34",
    ends={
        Property(name="jointPackage_PetriNet2PNML_TrgName", type=jointPackage_PetriNet2PNML_TrgNetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_PetriNet2PNML_TrgNetElement35", type=jointPackage_PetriNet2PNML_TrgName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name36: BinaryAssociation = BinaryAssociation(
    name="name36",
    ends={
        Property(name="jointPackage_PetriNet2PNML_TrgName38", type=jointPackage_PetriNet2PNML_TrgNetContent, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_PetriNet2PNML_TrgNetContent37", type=jointPackage_PetriNet2PNML_TrgName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labels39: BinaryAssociation = BinaryAssociation(
    name="labels39",
    ends={
        Property(name="jointPackage_PetriNet2PNML_TrgLabel", type=jointPackage_PetriNet2PNML_TrgLabeledElement, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_PetriNet2PNML_TrgLabeledElement", type=jointPackage_PetriNet2PNML_TrgLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_jointPackage_PetriNet2PNML_SrcNamedElement_SrcLocatedElement = Generalization(general=SrcLocatedElement, specific=jointPackage_PetriNet2PNML_SrcNamedElement)
gen_jointPackage_PetriNet2PNML_SrcPetriNet_SrcNamedElement = Generalization(general=SrcNamedElement, specific=jointPackage_PetriNet2PNML_SrcPetriNet)
gen_jointPackage_PetriNet2PNML_SrcElement_SrcNamedElement = Generalization(general=SrcNamedElement, specific=jointPackage_PetriNet2PNML_SrcElement)
gen_jointPackage_PetriNet2PNML_TrgPNMLDocument_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_PetriNet2PNML_TrgPNMLDocument)
gen_jointPackage_PetriNet2PNML_TrgIdedElement_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_PetriNet2PNML_TrgIdedElement)
gen_jointPackage_PetriNet2PNML_SrcPlace_SrcElement = Generalization(general=SrcElement, specific=jointPackage_PetriNet2PNML_SrcPlace)
gen_jointPackage_PetriNet2PNML_SrcTransition_SrcElement = Generalization(general=SrcElement, specific=jointPackage_PetriNet2PNML_SrcTransition)
gen_jointPackage_PetriNet2PNML_SrcArc_SrcNamedElement = Generalization(general=SrcNamedElement, specific=jointPackage_PetriNet2PNML_SrcArc)
gen_jointPackage_PetriNet2PNML_SrcPlaceToTransition_SrcArc = Generalization(general=SrcArc, specific=jointPackage_PetriNet2PNML_SrcPlaceToTransition)
gen_jointPackage_PetriNet2PNML_SrcTransitionToPlace_SrcArc = Generalization(general=SrcArc, specific=jointPackage_PetriNet2PNML_SrcTransitionToPlace)
gen_jointPackage_PetriNet2PNML_TrgArc_TrgNetContent = Generalization(general=TrgNetContent, specific=jointPackage_PetriNet2PNML_TrgArc)
gen_jointPackage_PetriNet2PNML_TrgArc_TrgIdedElement = Generalization(general=TrgIdedElement, specific=jointPackage_PetriNet2PNML_TrgArc)
gen_jointPackage_PetriNet2PNML_TrgPlace_TrgNetContentElement = Generalization(general=TrgNetContentElement, specific=jointPackage_PetriNet2PNML_TrgPlace)
gen_jointPackage_PetriNet2PNML_TrgTransition_TrgNetContentElement = Generalization(general=TrgNetContentElement, specific=jointPackage_PetriNet2PNML_TrgTransition)
gen_jointPackage_PetriNet2PNML_TrgURI_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_PetriNet2PNML_TrgURI)
gen_jointPackage_PetriNet2PNML_TrgNetElement_TrgIdedElement = Generalization(general=TrgIdedElement, specific=jointPackage_PetriNet2PNML_TrgNetElement)
gen_jointPackage_PetriNet2PNML_TrgNetContent_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_PetriNet2PNML_TrgNetContent)
gen_jointPackage_PetriNet2PNML_TrgLabeledElement_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_PetriNet2PNML_TrgLabeledElement)
gen_jointPackage_PetriNet2PNML_TrgLabel_TrgLocatedElement = Generalization(general=TrgLocatedElement, specific=jointPackage_PetriNet2PNML_TrgLabel)
gen_jointPackage_PetriNet2PNML_TrgName_TrgLabeledElement = Generalization(general=TrgLabeledElement, specific=jointPackage_PetriNet2PNML_TrgName)
gen_jointPackage_PetriNet2PNML_TrgNetContentElement_TrgNetContent = Generalization(general=TrgNetContent, specific=jointPackage_PetriNet2PNML_TrgNetContentElement)
gen_jointPackage_PetriNet2PNML_TrgNetContentElement_TrgIdedElement = Generalization(general=TrgIdedElement, specific=jointPackage_PetriNet2PNML_TrgNetContentElement)

# Domain Model
domain_model = DomainModel(
    name="jointPackage_PetriNet2PNML",
    types={jointPackage_PetriNet2PNML_SrcNamedElement, SrcLocatedElement, SrcNamedElement, jointPackage_PetriNet2PNML_SrcElement, jointPackage_PetriNet2PNML_SrcArc, jointPackage_PetriNet2PNML_JointMM, jointPackage_PetriNet2PNML_SrcPetriNet, jointPackage_PetriNet2PNML_TrgPNMLDocument, jointPackage_PetriNet2PNML_SrcLocatedElement, TrgLocatedElement, jointPackage_PetriNet2PNML_TrgURI, jointPackage_PetriNet2PNML_TrgNetElement, jointPackage_PetriNet2PNML_TrgLocatedElement, jointPackage_PetriNet2PNML_TrgIdedElement, jointPackage_PetriNet2PNML_SrcPlace, SrcElement, jointPackage_PetriNet2PNML_SrcTransitionToPlace, jointPackage_PetriNet2PNML_SrcPlaceToTransition, jointPackage_PetriNet2PNML_SrcTransition, SrcArc, jointPackage_PetriNet2PNML_TrgArc, jointPackage_PetriNet2PNML_TrgPlace, TrgNetContentElement, jointPackage_PetriNet2PNML_TrgTransition, TrgIdedElement, jointPackage_PetriNet2PNML_TrgNetContent, jointPackage_PetriNet2PNML_TrgName, jointPackage_PetriNet2PNML_TrgLabeledElement, jointPackage_PetriNet2PNML_TrgLabel, TrgLabeledElement, jointPackage_PetriNet2PNML_TrgNetContentElement, TrgNetContent},
    associations={elements3, arcs4, net6, sourceRoot0, targetRoot1, from19, to22, xmlns25, nets27, incomingArc7, outgoingArc8, incomingArc9, outgoingArc12, net15, from17, to18, source40, target41, type29, contents32, name34, name36, labels39},
    generalizations={gen_jointPackage_PetriNet2PNML_SrcNamedElement_SrcLocatedElement, gen_jointPackage_PetriNet2PNML_SrcPetriNet_SrcNamedElement, gen_jointPackage_PetriNet2PNML_SrcElement_SrcNamedElement, gen_jointPackage_PetriNet2PNML_TrgPNMLDocument_TrgLocatedElement, gen_jointPackage_PetriNet2PNML_TrgIdedElement_TrgLocatedElement, gen_jointPackage_PetriNet2PNML_SrcPlace_SrcElement, gen_jointPackage_PetriNet2PNML_SrcTransition_SrcElement, gen_jointPackage_PetriNet2PNML_SrcArc_SrcNamedElement, gen_jointPackage_PetriNet2PNML_SrcPlaceToTransition_SrcArc, gen_jointPackage_PetriNet2PNML_SrcTransitionToPlace_SrcArc, gen_jointPackage_PetriNet2PNML_TrgArc_TrgNetContent, gen_jointPackage_PetriNet2PNML_TrgArc_TrgIdedElement, gen_jointPackage_PetriNet2PNML_TrgPlace_TrgNetContentElement, gen_jointPackage_PetriNet2PNML_TrgTransition_TrgNetContentElement, gen_jointPackage_PetriNet2PNML_TrgURI_TrgLocatedElement, gen_jointPackage_PetriNet2PNML_TrgNetElement_TrgIdedElement, gen_jointPackage_PetriNet2PNML_TrgNetContent_TrgLocatedElement, gen_jointPackage_PetriNet2PNML_TrgLabeledElement_TrgLocatedElement, gen_jointPackage_PetriNet2PNML_TrgLabel_TrgLocatedElement, gen_jointPackage_PetriNet2PNML_TrgName_TrgLabeledElement, gen_jointPackage_PetriNet2PNML_TrgNetContentElement_TrgNetContent, gen_jointPackage_PetriNet2PNML_TrgNetContentElement_TrgIdedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)