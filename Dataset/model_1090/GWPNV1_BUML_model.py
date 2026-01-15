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
PetriNet_Place = Class(name="PetriNet::Place")
PetriNet_Net = Class(name="PetriNet::Net")
PetriNet_Transition = Class(name="PetriNet::Transition")

# PetriNet_Place class attributes and methods

# PetriNet_Net class attributes and methods

# PetriNet_Transition class attributes and methods

# Relationships
net0: BinaryAssociation = BinaryAssociation(
    name="net0",
    ends={
        Property(name="Net", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
src1: BinaryAssociation = BinaryAssociation(
    name="src1",
    ends={
        Property(name="Transition", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
dst2: BinaryAssociation = BinaryAssociation(
    name="dst2",
    ends={
        Property(name="Transition3", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
net4: BinaryAssociation = BinaryAssociation(
    name="net4",
    ends={
        Property(name="Net5", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
src6: BinaryAssociation = BinaryAssociation(
    name="src6",
    ends={
        Property(name="Place", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst7", type=PetriNet_Place, multiplicity=Multiplicity(1, 9999))
    }
)
dst8: BinaryAssociation = BinaryAssociation(
    name="dst8",
    ends={
        Property(name="Place10", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src9", type=PetriNet_Place, multiplicity=Multiplicity(1, 9999))
    }
)
place11: BinaryAssociation = BinaryAssociation(
    name="place11",
    ends={
        Property(name="Place12", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=PetriNet_Place, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transition13: BinaryAssociation = BinaryAssociation(
    name="transition13",
    ends={
        Property(name="Transition15", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net14", type=PetriNet_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_Place, PetriNet_Net, PetriNet_Transition},
    associations={net0, src1, dst2, net4, src6, dst8, place11, transition13},
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