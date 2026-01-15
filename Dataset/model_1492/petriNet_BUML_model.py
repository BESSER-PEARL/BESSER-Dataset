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
ArcDirection: Enumeration = Enumeration(
    name="ArcDirection",
    literals={
            EnumerationLiteral(name="P2T"),
			EnumerationLiteral(name="T2P")
    }
)

# Classes
petriNet_PetriElement = Class(name="petriNet::PetriElement", is_abstract=True)
petriNet_Place = Class(name="petriNet::Place")
petriNet_Transition = Class(name="petriNet::Transition")
PetriElement = Class(name="PetriElement")
petriNet_Arc = Class(name="petriNet::Arc")
petriNet_PetriNetwork = Class(name="petriNet::PetriNetwork")

# petriNet_PetriElement class attributes and methods
petriNet_PetriElement_name: Property = Property(name="name", type=StringType)
petriNet_PetriElement.attributes={petriNet_PetriElement_name}

# petriNet_Place class attributes and methods
petriNet_Place_nbJetons: Property = Property(name="nbJetons", type=IntegerType)
petriNet_Place.attributes={petriNet_Place_nbJetons}

# petriNet_Transition class attributes and methods
petriNet_Transition_m_newOperation1: Method = Method(name="newOperation1", parameters={})
petriNet_Transition.methods={petriNet_Transition_m_newOperation1}

# PetriElement class attributes and methods

# petriNet_Arc class attributes and methods
petriNet_Arc_jetonsTransferes: Property = Property(name="jetonsTransferes", type=IntegerType)
petriNet_Arc_Direction: Property = Property(name="Direction", type=StringType)
petriNet_Arc.attributes={petriNet_Arc_jetonsTransferes, petriNet_Arc_Direction}

# petriNet_PetriNetwork class attributes and methods
petriNet_PetriNetwork_name: Property = Property(name="name", type=StringType)
petriNet_PetriNetwork.attributes={petriNet_PetriNetwork_name}

# Relationships
arcEntrants4: BinaryAssociation = BinaryAssociation(
    name="arcEntrants4",
    ends={
        Property(name="petriNet_Arc5", type=petriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_Place", type=petriNet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
arcSortants6: BinaryAssociation = BinaryAssociation(
    name="arcSortants6",
    ends={
        Property(name="petriNet_Arc8", type=petriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_Place7", type=petriNet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
transition9: BinaryAssociation = BinaryAssociation(
    name="transition9",
    ends={
        Property(name="petriNet_Transition11", type=petriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_Arc10", type=petriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
arcSortants0: BinaryAssociation = BinaryAssociation(
    name="arcSortants0",
    ends={
        Property(name="petriNet_Arc", type=petriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_Transition", type=petriNet_Arc, multiplicity=Multiplicity(1, 9999))
    }
)
arcEntrants1: BinaryAssociation = BinaryAssociation(
    name="arcEntrants1",
    ends={
        Property(name="petriNet_Arc3", type=petriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_Transition2", type=petriNet_Arc, multiplicity=Multiplicity(1, 9999))
    }
)
petrielement15: BinaryAssociation = BinaryAssociation(
    name="petrielement15",
    ends={
        Property(name="petriNet_PetriNetwork", type=petriNet_PetriElement, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="petriNet_PetriElement", type=petriNet_PetriNetwork, multiplicity=Multiplicity(1, 1))
    }
)
place12: BinaryAssociation = BinaryAssociation(
    name="place12",
    ends={
        Property(name="petriNet_Place14", type=petriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_Arc13", type=petriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petriNet_Place_PetriElement = Generalization(general=PetriElement, specific=petriNet_Place)
gen_petriNet_Arc_PetriElement = Generalization(general=PetriElement, specific=petriNet_Arc)
gen_petriNet_Transition_PetriElement = Generalization(general=PetriElement, specific=petriNet_Transition)

# Domain Model
domain_model = DomainModel(
    name="petriNet",
    types={petriNet_PetriElement, petriNet_Place, petriNet_Transition, PetriElement, petriNet_Arc, petriNet_PetriNetwork, ArcDirection},
    associations={arcEntrants4, arcSortants6, transition9, arcSortants0, arcEntrants1, petrielement15, place12},
    generalizations={gen_petriNet_Place_PetriElement, gen_petriNet_Arc_PetriElement, gen_petriNet_Transition_PetriElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)