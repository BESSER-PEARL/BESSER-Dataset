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
        Property(name="1", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
src2: BinaryAssociation = BinaryAssociation(
    name="src2",
    ends={
        Property(name="4", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
dst5: BinaryAssociation = BinaryAssociation(
    name="dst5",
    ends={
        Property(name="7", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
net8: BinaryAssociation = BinaryAssociation(
    name="net8",
    ends={
        Property(name="10", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
src11: BinaryAssociation = BinaryAssociation(
    name="src11",
    ends={
        Property(name="13", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=PetriNet_Place, multiplicity=Multiplicity(1, 9999))
    }
)
dst14: BinaryAssociation = BinaryAssociation(
    name="dst14",
    ends={
        Property(name="16", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=PetriNet_Place, multiplicity=Multiplicity(1, 9999))
    }
)
place17: BinaryAssociation = BinaryAssociation(
    name="place17",
    ends={
        Property(name="19", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition20: BinaryAssociation = BinaryAssociation(
    name="transition20",
    ends={
        Property(name="22", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="21", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_Place, PetriNet_Net, PetriNet_Transition},
    associations={net0, src2, dst5, net8, src11, dst14, place17, transition20},
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