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
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_Edge = Class(name="petrinet::Edge", is_abstract=True)
petrinet_PetriNet = Class(name="petrinet::PetriNet")
NamedElement = Class(name="NamedElement")
petrinet_Place = Class(name="petrinet::Place")
petrinet_OutputEdge = Class(name="petrinet::OutputEdge")
petrinet_InhibitorEdge = Class(name="petrinet::InhibitorEdge")
petrinet_ReadEdge = Class(name="petrinet::ReadEdge")
petrinet_NamedElement = Class(name="petrinet::NamedElement")
petrinet_InputEdge = Class(name="petrinet::InputEdge")
Edge = Class(name="Edge")

# petrinet_Transition class attributes and methods

# petrinet_Edge class attributes and methods

# petrinet_PetriNet class attributes and methods

# NamedElement class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_tokens: Property = Property(name="tokens", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_tokens}

# petrinet_OutputEdge class attributes and methods

# petrinet_InhibitorEdge class attributes and methods

# petrinet_ReadEdge class attributes and methods

# petrinet_NamedElement class attributes and methods
petrinet_NamedElement_name: Property = Property(name="name", type=StringType)
petrinet_NamedElement.attributes={petrinet_NamedElement_name}

# petrinet_InputEdge class attributes and methods

# Edge class attributes and methods

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="petrinet_Transition", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet2", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges3: BinaryAssociation = BinaryAssociation(
    name="edges3",
    ends={
        Property(name="petrinet_Edge", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet4", type=petrinet_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges5: BinaryAssociation = BinaryAssociation(
    name="edges5",
    ends={
        Property(name="Edge", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=petrinet_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petrinet_Place", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges6: BinaryAssociation = BinaryAssociation(
    name="edges6",
    ends={
        Property(name="Edge7", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=petrinet_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
place8: BinaryAssociation = BinaryAssociation(
    name="place8",
    ends={
        Property(name="Place", type=petrinet_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=petrinet_Place, multiplicity=Multiplicity(0, 1))
    }
)
transition9: BinaryAssociation = BinaryAssociation(
    name="transition9",
    ends={
        Property(name="Transition", type=petrinet_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges10", type=petrinet_Transition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_petrinet_Place_NamedElement = Generalization(general=NamedElement, specific=petrinet_Place)
gen_petrinet_PetriNet_NamedElement = Generalization(general=NamedElement, specific=petrinet_PetriNet)
gen_petrinet_OutputEdge_Edge = Generalization(general=Edge, specific=petrinet_OutputEdge)
gen_petrinet_InhibitorEdge_Edge = Generalization(general=Edge, specific=petrinet_InhibitorEdge)
gen_petrinet_ReadEdge_Edge = Generalization(general=Edge, specific=petrinet_ReadEdge)
gen_petrinet_Transition_NamedElement = Generalization(general=NamedElement, specific=petrinet_Transition)
gen_petrinet_Edge_NamedElement = Generalization(general=NamedElement, specific=petrinet_Edge)
gen_petrinet_InputEdge_Edge = Generalization(general=Edge, specific=petrinet_InputEdge)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Transition, petrinet_Edge, petrinet_PetriNet, NamedElement, petrinet_Place, petrinet_OutputEdge, petrinet_InhibitorEdge, petrinet_ReadEdge, petrinet_NamedElement, petrinet_InputEdge, Edge},
    associations={transitions1, edges3, edges5, places0, edges6, place8, transition9},
    generalizations={gen_petrinet_Place_NamedElement, gen_petrinet_PetriNet_NamedElement, gen_petrinet_OutputEdge_Edge, gen_petrinet_InhibitorEdge_Edge, gen_petrinet_ReadEdge_Edge, gen_petrinet_Transition_NamedElement, gen_petrinet_Edge_NamedElement, gen_petrinet_InputEdge_Edge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)