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
petrinet_Place = Class(name="petrinet::Place")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_PetriNet = Class(name="petrinet::PetriNet")

# petrinet_Place class attributes and methods
petrinet_Place_token: Property = Property(name="token", type=IntegerType)
petrinet_Place_name: Property = Property(name="name", type=StringType)
petrinet_Place.attributes={petrinet_Place_name, petrinet_Place_token}

# petrinet_Transition class attributes and methods
petrinet_Transition_name: Property = Property(name="name", type=StringType)
petrinet_Transition.attributes={petrinet_Transition_name}

# petrinet_Arc class attributes and methods
petrinet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_Arc_toPlace: Property = Property(name="toPlace", type=BooleanType)
petrinet_Arc.attributes={petrinet_Arc_weight, petrinet_Arc_toPlace}

# petrinet_PetriNet class attributes and methods
petrinet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinet_PetriNet.attributes={petrinet_PetriNet_name}

# Relationships
inhibitorArc0: BinaryAssociation = BinaryAssociation(
    name="inhibitorArc0",
    ends={
        Property(name="petrinet_Transition", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="petrinet_Transition2", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
place3: BinaryAssociation = BinaryAssociation(
    name="place3",
    ends={
        Property(name="petrinet_Place5", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc4", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
places6: BinaryAssociation = BinaryAssociation(
    name="places6",
    ends={
        Property(name="petrinet_Place7", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs8: BinaryAssociation = BinaryAssociation(
    name="arcs8",
    ends={
        Property(name="petrinet_Arc10", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet9", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions11: BinaryAssociation = BinaryAssociation(
    name="transitions11",
    ends={
        Property(name="petrinet_Transition13", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet12", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Place, petrinet_Transition, petrinet_Arc, petrinet_PetriNet},
    associations={inhibitorArc0, transition1, place3, places6, arcs8, transitions11},
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