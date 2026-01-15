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
PetriNet_Net = Class(name="PetriNet::Net")
PetriNet_Place = Class(name="PetriNet::Place")
PetriNet_Transition = Class(name="PetriNet::Transition")

# PetriNet_Net class attributes and methods

# PetriNet_Place class attributes and methods
PetriNet_Place_name: Property = Property(name="name", type=StringType)
PetriNet_Place.attributes={PetriNet_Place_name}

# PetriNet_Transition class attributes and methods
PetriNet_Transition_name: Property = Property(name="name", type=StringType)
PetriNet_Transition.attributes={PetriNet_Transition_name}

# Relationships
dst6: BinaryAssociation = BinaryAssociation(
    name="dst6",
    ends={
        Property(name="src", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999)),
        Property(name="Transition7", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="Net", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=PetriNet_Net, multiplicity=Multiplicity(0, 1))
    }
)
src4: BinaryAssociation = BinaryAssociation(
    name="src4",
    ends={
        Property(name="Transition5", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
net8: BinaryAssociation = BinaryAssociation(
    name="net8",
    ends={
        Property(name="Net9", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=PetriNet_Net, multiplicity=Multiplicity(0, 1))
    }
)
src10: BinaryAssociation = BinaryAssociation(
    name="src10",
    ends={
        Property(name="Place12", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst11", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
dst13: BinaryAssociation = BinaryAssociation(
    name="dst13",
    ends={
        Property(name="Place15", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src14", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_Net, PetriNet_Place, PetriNet_Transition},
    associations={dst6, places0, transitions1, net3, src4, net8, src10, dst13},
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