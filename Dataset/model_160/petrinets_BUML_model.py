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
Petrinet_PetriNet = Class(name="Petrinet::PetriNet")
Petrinet_Place = Class(name="Petrinet::Place")
Petrinet_Transition = Class(name="Petrinet::Transition")

# Petrinet_PetriNet class attributes and methods

# Petrinet_Place class attributes and methods
Petrinet_Place_name: Property = Property(name="name", type=StringType)
Petrinet_Place_tokens: Property = Property(name="tokens", type=IntegerType)
Petrinet_Place.attributes={Petrinet_Place_name, Petrinet_Place_tokens}

# Petrinet_Transition class attributes and methods
Petrinet_Transition_name: Property = Property(name="name", type=StringType)
Petrinet_Transition.attributes={Petrinet_Transition_name}

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Petrinet_Place", type=Petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="Petrinet_PetriNet", type=Petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Petrinet_Transition", type=Petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="Petrinet_PetriNet2", type=Petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p2t3: BinaryAssociation = BinaryAssociation(
    name="p2t3",
    ends={
        Property(name="Petrinet_Transition5", type=Petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="Petrinet_Place4", type=Petrinet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
t2p6: BinaryAssociation = BinaryAssociation(
    name="t2p6",
    ends={
        Property(name="Petrinet_Place8", type=Petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Petrinet_Transition7", type=Petrinet_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Petrinet",
    types={Petrinet_PetriNet, Petrinet_Place, Petrinet_Transition},
    associations={places0, transitions1, p2t3, t2p6},
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