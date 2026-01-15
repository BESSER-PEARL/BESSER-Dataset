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
PetriNetMM0_Net = Class(name="PetriNetMM0::Net")
PetriNetMM0_Place = Class(name="PetriNetMM0::Place")
PetriNetMM0_Transition = Class(name="PetriNetMM0::Transition")

# PetriNetMM0_Net class attributes and methods

# PetriNetMM0_Place class attributes and methods

# PetriNetMM0_Transition class attributes and methods

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=PetriNetMM0_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=PetriNetMM0_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net8: BinaryAssociation = BinaryAssociation(
    name="net8",
    ends={
        Property(name="Net9", type=PetriNetMM0_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=PetriNetMM0_Net, multiplicity=Multiplicity(1, 1))
    }
)
src10: BinaryAssociation = BinaryAssociation(
    name="src10",
    ends={
        Property(name="Place12", type=PetriNetMM0_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst11", type=PetriNetMM0_Place, multiplicity=Multiplicity(1, 1))
    }
)
dst13: BinaryAssociation = BinaryAssociation(
    name="dst13",
    ends={
        Property(name="Place15", type=PetriNetMM0_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src14", type=PetriNetMM0_Place, multiplicity=Multiplicity(1, 1))
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=PetriNetMM0_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=PetriNetMM0_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="Net", type=PetriNetMM0_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=PetriNetMM0_Net, multiplicity=Multiplicity(1, 1))
    }
)
dst4: BinaryAssociation = BinaryAssociation(
    name="dst4",
    ends={
        Property(name="Transition5", type=PetriNetMM0_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=PetriNetMM0_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src6: BinaryAssociation = BinaryAssociation(
    name="src6",
    ends={
        Property(name="Transition7", type=PetriNetMM0_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=PetriNetMM0_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="PetriNetMM0",
    types={PetriNetMM0_Net, PetriNetMM0_Place, PetriNetMM0_Transition},
    associations={places0, net8, src10, dst13, transitions1, net3, dst4, src6},
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