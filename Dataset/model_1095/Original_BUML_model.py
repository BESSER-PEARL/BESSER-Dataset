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
petrinets_Net = Class(name="petrinets::Net")
petrinets_Place = Class(name="petrinets::Place")
petrinets_Transition = Class(name="petrinets::Transition")

# petrinets_Net class attributes and methods

# petrinets_Place class attributes and methods
petrinets_Place_name: Property = Property(name="name", type=StringType)
petrinets_Place.attributes={petrinets_Place_name}

# petrinets_Transition class attributes and methods
petrinets_Transition_name: Property = Property(name="name", type=StringType)
petrinets_Transition.attributes={petrinets_Transition_name}

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=petrinets_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=petrinets_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=petrinets_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=petrinets_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="Net", type=petrinets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=petrinets_Net, multiplicity=Multiplicity(1, 1))
    }
)
src4: BinaryAssociation = BinaryAssociation(
    name="src4",
    ends={
        Property(name="Transition5", type=petrinets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=petrinets_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
dst6: BinaryAssociation = BinaryAssociation(
    name="dst6",
    ends={
        Property(name="Transition7", type=petrinets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=petrinets_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
net8: BinaryAssociation = BinaryAssociation(
    name="net8",
    ends={
        Property(name="Net9", type=petrinets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=petrinets_Net, multiplicity=Multiplicity(1, 1))
    }
)
src10: BinaryAssociation = BinaryAssociation(
    name="src10",
    ends={
        Property(name="Place12", type=petrinets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst11", type=petrinets_Place, multiplicity=Multiplicity(1, 9999))
    }
)
dst13: BinaryAssociation = BinaryAssociation(
    name="dst13",
    ends={
        Property(name="Place15", type=petrinets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src14", type=petrinets_Place, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="petrinets",
    types={petrinets_Net, petrinets_Place, petrinets_Transition},
    associations={places0, transitions1, net3, src4, dst6, net8, src10, dst13},
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