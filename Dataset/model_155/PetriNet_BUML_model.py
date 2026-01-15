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
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_Place = Class(name="petrinet::Place")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_PetriNet = Class(name="petrinet::PetriNet")

# petrinet_Arc class attributes and methods
petrinet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_Arc_toPlace: Property = Property(name="toPlace", type=BooleanType)
petrinet_Arc.attributes={petrinet_Arc_toPlace, petrinet_Arc_weight}

# petrinet_Place class attributes and methods
petrinet_Place_token: Property = Property(name="token", type=IntegerType)
petrinet_Place_name: Property = Property(name="name", type=StringType)
petrinet_Place.attributes={petrinet_Place_token, petrinet_Place_name}

# petrinet_Transition class attributes and methods
petrinet_Transition_name: Property = Property(name="name", type=StringType)
petrinet_Transition.attributes={petrinet_Transition_name}

# petrinet_PetriNet class attributes and methods
petrinet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinet_PetriNet.attributes={petrinet_PetriNet_name}

# Relationships
transition2: BinaryAssociation = BinaryAssociation(
    name="transition2",
    ends={
        Property(name="petrinet_Transition3", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
place4: BinaryAssociation = BinaryAssociation(
    name="place4",
    ends={
        Property(name="petrinet_Place6", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc5", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
net7: BinaryAssociation = BinaryAssociation(
    name="net7",
    ends={
        Property(name="PetriNet8", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
net9: BinaryAssociation = BinaryAssociation(
    name="net9",
    ends={
        Property(name="PetriNet10", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
places11: BinaryAssociation = BinaryAssociation(
    name="places11",
    ends={
        Property(name="Place", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inhibitorArc0: BinaryAssociation = BinaryAssociation(
    name="inhibitorArc0",
    ends={
        Property(name="petrinet_Transition", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
arcs12: BinaryAssociation = BinaryAssociation(
    name="arcs12",
    ends={
        Property(name="Arc", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net13", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net1: BinaryAssociation = BinaryAssociation(
    name="net1",
    ends={
        Property(name="PetriNet", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
transitions14: BinaryAssociation = BinaryAssociation(
    name="transitions14",
    ends={
        Property(name="Transition", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net15", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Arc, petrinet_Place, petrinet_Transition, petrinet_PetriNet},
    associations={transition2, place4, net7, net9, places11, inhibitorArc0, arcs12, net1, transitions14},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)