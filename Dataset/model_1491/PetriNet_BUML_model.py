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
PetriNet_NamedElement = Class(name="PetriNet::NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")
NamedElement = Class(name="NamedElement")
PetriNet_Element = Class(name="PetriNet::Element", is_abstract=True)
PetriNet_LocatedElement = Class(name="PetriNet::LocatedElement", is_abstract=True)
PetriNet_Place = Class(name="PetriNet::Place")
Element = Class(name="Element")
PetriNet_Transition = Class(name="PetriNet::Transition")

# PetriNet_NamedElement class attributes and methods
PetriNet_NamedElement_name: Property = Property(name="name", type=StringType)
PetriNet_NamedElement.attributes={PetriNet_NamedElement_name}

# LocatedElement class attributes and methods

# PetriNet_PetriNet class attributes and methods

# NamedElement class attributes and methods

# PetriNet_Element class attributes and methods

# PetriNet_LocatedElement class attributes and methods
PetriNet_LocatedElement_location: Property = Property(name="location", type=StringType)
PetriNet_LocatedElement.attributes={PetriNet_LocatedElement_location}

# PetriNet_Place class attributes and methods

# Element class attributes and methods

# PetriNet_Transition class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="Element", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=PetriNet_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net1: BinaryAssociation = BinaryAssociation(
    name="net1",
    ends={
        Property(name="PetriNet", type=PetriNet_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
incomingArc5: BinaryAssociation = BinaryAssociation(
    name="incomingArc5",
    ends={
        Property(name="outgoingArc6", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999)),
        Property(name="Place", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
outgoingArc7: BinaryAssociation = BinaryAssociation(
    name="outgoingArc7",
    ends={
        Property(name="Place9", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc8", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999))
    }
)
incomingArc2: BinaryAssociation = BinaryAssociation(
    name="incomingArc2",
    ends={
        Property(name="Transition", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArc", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingArc3: BinaryAssociation = BinaryAssociation(
    name="outgoingArc3",
    ends={
        Property(name="Transition4", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArc", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_PetriNet_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=PetriNet_NamedElement)
gen_PetriNet_PetriNet_NamedElement = Generalization(general=NamedElement, specific=PetriNet_PetriNet)
gen_PetriNet_Element_NamedElement = Generalization(general=NamedElement, specific=PetriNet_Element)
gen_PetriNet_Place_Element = Generalization(general=Element, specific=PetriNet_Place)
gen_PetriNet_Transition_Element = Generalization(general=Element, specific=PetriNet_Transition)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_NamedElement, LocatedElement, PetriNet_PetriNet, NamedElement, PetriNet_Element, PetriNet_LocatedElement, PetriNet_Place, Element, PetriNet_Transition},
    associations={elements0, net1, incomingArc5, outgoingArc7, incomingArc2, outgoingArc3},
    generalizations={gen_PetriNet_NamedElement_LocatedElement, gen_PetriNet_PetriNet_NamedElement, gen_PetriNet_Element_NamedElement, gen_PetriNet_Place_Element, gen_PetriNet_Transition_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)